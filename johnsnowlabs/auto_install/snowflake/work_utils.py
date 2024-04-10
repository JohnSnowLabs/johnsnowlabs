import json
import time

from johnsnowlabs import nlp
from johnsnowlabs.auto_install.docker.work_utils import check_local_endpoint_health, _destroy_container
from johnsnowlabs.utils.py_process import run_cmd_and_check_succ


def is_snowflake_installed():
    try:
        import snowflake.connector
    except:
        ImportError('Run `pip install snowflake-connector-python` to use Snowflake utilities! ')
    return True


def get_client(user, password, account, warehouse, database, schema, role):
    is_snowflake_installed()
    import snowflake.connector
    conn = snowflake.connector.connect(
        user=user,
        password=password,
        account=account,
        warehouse=warehouse,
        database=database,
        schema=schema,
        role=role,
    )
    return conn


def query_udf(client, udf_name, data):
    cmd_query_udf = """SELECT {udf_name}('{data}')"""
    cur = client.cursor()
    cur.execute(cmd_query_udf.format(udf_name=udf_name, data=data))
    for row in cur:
        data = json.loads(row[0])
        print(data)
    cur.close()
    return data


def get_service_create_cmd(service_name, compute_pool_name, image_path, role, database, warehouse, schema):
    return f"""
    USE ROLE {role};
    USE DATABASE {database};
    USE WAREHOUSE {warehouse};
    USE SCHEMA {schema};
    
    CREATE SERVICE {service_name}
      IN COMPUTE POOL {compute_pool_name}
      FROM SPECIFICATION $$
        spec:
          containers:
          - name: jsl-container
            image: {image_path}
            readinessProbe:
              port: 80
              path: /ping
          endpoints:
          - name: invoke
            port: 80
            public: true
            $$
       MIN_INSTANCES=1
       MAX_INSTANCES=1;
    """


def build_snowflake_image(nlu_ref, image_name, license_path):
    # check_build_serve_query
    nlp.build_image(
        nlu_ref,
        image_name,
        rebuild=True,
        use_cache=True,
        json_license_path=license_path,
    )


def test_snowflake_image_local(image_name, container_name, port):
    # Serve container, destroy if already running. After test destroy local container
    nlp.serve_container(
        destroy_container=True,
        image_name=image_name,
        container_name=container_name,
        host_port=port,
    )
    # todo expo backoff for big models N times maybe
    time.sleep(30)
    check_local_endpoint_health(port)
    _destroy_container(container_name)


def push_snowflake_image(remote_repo, image_name):
    cmd = f'docker push {remote_repo}/{image_name}:latest'
    return run_cmd_and_check_succ(
        [cmd], shell=True, raise_on_fail=True, use_code=True, log=True
    )


def create_service(client, service_name, compute_pool_name, image_path, role, database, warehouse, schema):
    cur = client.cursor()
    cmd = get_service_create_cmd(service_name, compute_pool_name, image_path, role, database, warehouse, schema)
    cur.execute(cmd, num_statements=cmd.count(';'))
    for row in cur:
        print(row)
    cur.close()
    print('service created')


def create_udf(client, service_name, udf_name, role, database, warehouse, schema):
    cur = client.cursor()
    cmd = create_udf_cmd(service_name, udf_name, role, database, warehouse, schema)
    cur.execute(cmd, num_statements=cmd.count(';'))
    for row in cur:
        print(row)
    cur.close()


def create_udf_cmd(service_name, udf_name, role, database, warehouse, schema):
    return f'''
USE ROLE {role};
USE DATABASE {database};
USE WAREHOUSE {warehouse};
USE SCHEMA {schema};

CREATE FUNCTION {udf_name} (InputText varchar, OutputLevel VARCHAR DEFAULT 'document')
  RETURNS object
  SERVICE={service_name}
  ENDPOINT=invoke
  AS '/invoke';
    '''


def test_udf(client, udf_name):
    # this will test service under the hood
    return query_udf(client, udf_name, 'Hello this is my data ')


def tag_image(image_name, remote_repo):
    cmd = f'docker tag {image_name}:latest {remote_repo}/{image_name}:latest'
    return run_cmd_and_check_succ(
        [cmd], shell=True, raise_on_fail=True, use_code=True, log=True
    )


def build_test_and_push_image(nlu_ref, license_path, image_name, local_test_container_name, local_test_port,
                              remote_repo):
    # build image, test it locally, tag it, push it and destroy the local image
    # TODO check while pushing if not authorized/logged in fail or not
    login_cmd = f'docker login {remote_repo}'

    build_snowflake_image(nlu_ref, image_name, license_path)
    test_snowflake_image_local(image_name, local_test_container_name, local_test_port)
    tag_image(image_name, remote_repo)
    # TODO TEST IF ACTUALLY LOGGED IN !!
    push_snowflake_image(remote_repo, image_name)
    # _destroy_image(image_name)


def get_service_logs(snowflake_user, snowflake_password, snowflake_account, warehouse_name, database_name,
                     schema_name, role_name, service_name):
    client = get_client(snowflake_user, snowflake_password, snowflake_account, warehouse_name, database_name,
                        schema_name, role_name)
    cur = client.cursor()
    r = cur.execute(f"SELECT SYSTEM$GET_SERVICE_STATUS('{service_name}');").fetchall()
    print(r)
    import json
    status = json.loads(r[0][0])[0]['status']
    if status == "PENDING":
        return True
    else:
        pass
    return r


def snowflake_common_setup(snowflake_user, snowflake_account, snowflake_password,
                           role_name='test_role',
                           schema_name='data_schema',
                           repo_name='tutorial_repository',
                           stage_name='tutorial_stage',
                           db_name='tutorial_db',
                           warehouse_name='tutorial_warehouse',
                           compute_pool_name='tutorial_compute_pool',
                           ):
    """do commmon setup for Snowflake Container Services.
    Creates Warehouse, Database, Schema, Compute-Pool, Repository and Role to use for Johnsnowlabs Based container services.

    """

    # todo params for warehouse_name size and compute-pool
    base_cmd = f"""
USE ROLE ACCOUNTADMIN;

CREATE ROLE IF NOT EXISTS {role_name};

CREATE DATABASE IF NOT EXISTS {db_name};
GRANT OWNERSHIP ON DATABASE {db_name} TO ROLE {role_name} COPY CURRENT GRANTS;

CREATE OR REPLACE WAREHOUSE {warehouse_name} WITH WAREHOUSE_SIZE='X-SMALL';
GRANT USAGE ON WAREHOUSE {warehouse_name} TO ROLE {role_name};

CREATE SECURITY INTEGRATION IF NOT EXISTS snowservices_ingress_oauth
  TYPE=oauth
  OAUTH_CLIENT=snowservices_ingress
  ENABLED=true;

GRANT BIND SERVICE ENDPOINT ON ACCOUNT TO ROLE {role_name};

CREATE COMPUTE POOL IF NOT EXISTS {compute_pool_name} 
  MIN_NODES = 1
  MAX_NODES = 1
  INSTANCE_FAMILY = CPU_X64_XS;
  
GRANT USAGE, MONITOR ON COMPUTE POOL {compute_pool_name} TO ROLE {role_name};

GRANT ROLE {role_name} TO USER {snowflake_user};
    
    """

    is_snowflake_installed()
    import snowflake.connector
    c = snowflake.connector.connect(user=snowflake_user, password=snowflake_password, account=snowflake_account)
    cur = c.cursor()
    r = cur.execute(base_cmd, num_statements=base_cmd.count(';'))
    succ = r.fetchall()[0][0] == 'Statement executed successfully.'
    if succ:
        print(f'Role {role_name} created and access granted to {snowflake_user}')
        print(f'Database {db_name} created')
        print(f'Warehouse {warehouse_name} crated')
        print(f'Warehouse {warehouse_name} crated')
        print(f'Compute Pool {compute_pool_name} crated')

    create_db_objects_cmd = f"""
USE ROLE {role_name};
USE DATABASE {db_name};
USE WAREHOUSE {warehouse_name};

CREATE SCHEMA IF NOT EXISTS {schema_name};
USE SCHEMA  {schema_name};
CREATE IMAGE REPOSITORY IF NOT EXISTS {repo_name};
CREATE STAGE IF NOT EXISTS {stage_name} DIRECTORY = ( ENABLE = true );
    """

    r = cur.execute(create_db_objects_cmd, num_statements=create_db_objects_cmd.count(';'))

    succ = r.fetchall()[0][0] == 'Statement executed successfully.'
    if succ:
        print(f'Schema {schema_name} crated')
        print(f'Repository {repo_name} crated')
        print(f'Stage {stage_name} crated')
    else:
        print('Failure creating Schema, Repository and Stage!')

    verify_prefix = f'''
USE ROLE {role_name};
USE DATABASE {db_name};
USE WAREHOUSE {warehouse_name};
    '''

    def verify_image_repo(verify_prefix):
        cmd = f'SHOW IMAGE REPOSITORIES;'
        response = cur.execute(cmd, num_statements=cmd.count(';')).fetchall()
        print(response)
        for r in response:
            response_repo = r[1].lower()
            response_db = r[2].lower()
            response_schema = r[3].lower()
            response_repo_url = r[4].lower()
            response_role = r[5].lower()
            if response_repo == repo_name.lower() and response_db == db_name.lower() and response_schema == schema_name.lower() \
                    and response_role == role_name.lower():
                return response_repo_url

    repo_url = verify_image_repo(verify_prefix)

    print(f'Remote repo URL is {repo_url}')
    return role_name, db_name, warehouse_name, schema_name, compute_pool_name, repo_url


def deploy_as_snowflake_udf(nlu_ref,
                            repo_url,
                            role_name,
                            database_name,
                            warehouse_name,
                            schema_name,
                            compute_pool_name,
                            snowflake_user,
                            snowflake_password,
                            snowflake_account,
                            license_path=None,
                            udf_name=None,
                            service_name=None,

                            ):
    client = get_client(snowflake_user, snowflake_password, snowflake_account, warehouse_name, database_name,
                        schema_name, role_name)

    # Local container setup
    clean_nlu_ref = nlu_ref.replace('.', '-').replace('_', '-')

    port = 6645
    container_name = f"{clean_nlu_ref}_container"
    image_name = f"{clean_nlu_ref}-img"

    remote_image = f'{repo_url}/{image_name}:latest'

    if not service_name:
        service_name = f'{clean_nlu_ref}_service'.replace('-', '_')
    if not udf_name:
        udf_name = f'{clean_nlu_ref}_udf'.replace('-', '_')

    # TODO block while status pending optinally
    # r = get_service_logs(snowflake_user, snowflake_password, snowflake_account, warehouse_name, database_name,
    #              schema_name, role_name, service_name)
    # print(r)
    # 2.  Local Docker Setup, Tests and Push to Snowflake
    build_test_and_push_image(nlu_ref, license_path, image_name, container_name, port, repo_url)

    # 3. Snowflake: Create service, create udf and test udf
    print(f'Starting Snowflake Procedure')
    create_service(client, service_name, compute_pool_name, remote_image, role_name, database_name, warehouse_name,
                   schema_name)
    print(f'Service {service_name} created')
    time.sleep(1 * 60)  # wait ~ n seconds for container sto spin up, expo backup..!
    create_udf(client, service_name, udf_name, role_name, database_name, warehouse_name, schema_name)
    print(f'UDF {udf_name} created')

    print('testing UDF...')
    test_udf(client, udf_name)

    return udf_name
