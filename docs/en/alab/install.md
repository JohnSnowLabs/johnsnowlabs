---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Installation
permalink: /docs/en/alab/install
key: docs-training
modify_date: "2023-11-07"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

<style>
th {
  width: 200px;
  text-align: left;
  background-color: #f7f7f7;
  vertical-align: "top";
}
</style>

<div class="h3-box" markdown="1">

## Type of installation

{:.btn-box-install}
[Dedicated Server](#dedicated-server){:.button.button-blue}
[AWS Marketplace](#aws-marketplace){:.button.button-blue}
[Azure Marketplace](#azure-marketplace){:.button.button-blue}
[EKS deployment](#eks-deployment){:.button.button-blue}
[AKS deployment](#aks-deployment){:.button.button-blue}
[AirGap Environment](#airgap-environment){:.button.button-blue}
[OpenShift](#openshift){:.button.button-blue}

</div><div class="h3-box" markdown="1">

## Dedicated Server

Install Generative AI Lab (NLP Lab) on a dedicated server to reduce the likelihood of conflicts or unexpected behavior.

</div><div class="h3-box" markdown="1">

### Fresh install

To install Generative AI Lab run the following command:

```bash
wget https://setup.johnsnowlabs.com/annotationlab/install.sh -O - | sudo bash -s $VERSION
```

Replace `$VERSION` in the above one liners with the version you want to install.

For installing the latest available version of the Generative AI Lab use:

```bash
wget https://setup.johnsnowlabs.com/annotationlab/install.sh -O - | sudo bash -s --
```

</div><div class="h3-box" markdown="1">

### Upgrade

To upgrade your Generative AI Lab installation to a newer version, run the following command on a terminal:

```bash
wget https://setup.johnsnowlabs.com/annotationlab/upgrade.sh -O - | sudo bash -s $VERSION
```

Replace `$VERSION` in the above one liners with the version you want to upgrade to.

For upgrading to the latest version of the Generative AI Lab, use:

```bash
wget https://setup.johnsnowlabs.com/annotationlab/upgrade.sh -O - | sudo bash -s --
```

> **NOTE:** The install/upgrade script displays the login credentials for the _admin_ user on the terminal.

After running the install/upgrade script, the Generative AI Lab is available at http://INSTANCE_IP or https://INSTANCE_IP

![login Screen ALAB](/assets/images/annotation_lab/4.1.0/loginScreenALAB.png)

We have an aesthetically pleasing Sign-In Page with a section highlighting the key features of Generative AI Lab using animated GIFs.

</div><div class="h3-box" markdown="1">

## AWS Marketplace

The Generative AI Lab needs to be installed on a virtual machine. One of the most straight forward method is an installation from AWS Marketplace (also available on Azure). There is no fee for the Generative AI Lab. However, you still have to pay for the underlying AWS EC2 instance (not Free Tier Eligible).

Visit the [product page on AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-nsww5rdpvou4w?sr=0-1&ref_=beagle&applicationId=AWSMPContessa) and follow the instructions on the video below to subscribe and deploy.

<div class="cell cell--12 cell--lg-6 cell--sm-12"><div class="video-item">{%- include extensions/youtube.html id='ebaewU4BcQA' -%}<div class="video-descr">Deploy Generative AI Lab via AWS Marketplace</div></div></div>

</div><div class="h3-box" markdown="1">

## Secure access to Generative AI Lab on AWS

When installed via the AWS Marketplace, Generative AI Lab has a private IP address and listens on an unsecured HTTP port. You can ask your DevOps department to incorporate the resource to your standard procedures to access from the internet in a secure manner. Alternatively, a Cloud Formation script is available that can be used to create a front end proxy (CloudFront, ELB, and auxiliary Lambda Function). Those resources are Free Tier Eligible. 

Create the AWS Cloud Formation Script in YAML format:
   
   ```console
   vi cloudformation_https.yaml
   ```

   ```console
AWSTemplateFormatVersion: '2010-09-09'
Metadata:
  License: Apache-2.0
Description: 'AWS CloudFormation To access Generative AI Lab via https:
  Create an Amazon EC2 instance running the Generative AI Lab Amazon Linux AMI. Once the
  Generative AI Lab instance is created, provide instance hostname as input. This Cloudfromation
  Creates Cloudfront. You can use Cloudfront Domain URL to access Generative AI Lab
  via https protocol.
  '
Parameters:
  NLPlabInstanceHostName:
    Description: HostName of the Generative AI Lab InstanceID
    Type: String
    ConstraintDescription: HostName of the Generative AI Lab InstanceID

Resources:
  CloudFront:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        Enabled: True
        DefaultCacheBehavior:
          AllowedMethods:
            - DELETE
            - GET
            - HEAD
            - OPTIONS
            - PATCH
            - POST
            - PUT
          DefaultTTL: 0
          MaxTTL: 0
          MinTTL: 0
          Compress: True
          ForwardedValues:
            QueryString: true
            Headers:
              - '*'
            Cookies:
              Forward: all
          TargetOriginId: EC2CustomOrigin
          ViewerProtocolPolicy: redirect-to-https
        Origins:
          - DomainName: !Ref NLPlabInstanceHostName
            Id: EC2CustomOrigin
            CustomOriginConfig:
              HTTPPort: '80'
              OriginProtocolPolicy: http-only
Outputs:
  CloudfrontURL:
    Description: Cloudfront URL to access Generative AI Lab
    Value: !Join ["", ['https://', !GetAtt [CloudFront, DomainName]]]

   ```

Click Create a stack, “Upload a template file”. Give the Stack a name and enter the Generative AI Lab instance Hostname(from the EC2 console) as a parameter.

![createStack](/assets/images/annotation_lab/aws/createStack.png)

Next -> Next -> Acknowledge that AWS CloudFormation might create IAM resources. -> Submit. Wait a few minutes until all resources are created.  

![ack](/assets/images/annotation_lab/aws/ack.png)

Once created, go do the Outputs tab and click on the Generative AI Lab URL. You may need to refresh the view. 

![output](/assets/images/annotation_lab/aws/output.png)

Now, to access the Generative AI Lab, you go to the CloudFront URL and log in with username “admin” and password equal to the EC2 Instance ID noted earlier. 

</div><div class="h3-box" markdown="1">

## Azure Marketplace

Visit the [product page on Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/johnsnowlabsinc1646051154808.annotation_lab?tab=Overview) and follow the instructions on the video below to subscribe and deploy.

<div class="cell cell--12 cell--lg-6 cell--sm-12"><div class="video-item">{%- include extensions/youtube.html id='e6aB3z5tB0k' -%}<div class="video-descr">Deploy Generative AI Lab via Azure Marketplace</div></div></div>

</div><div class="h3-box" markdown="1">

## EKS deployment

1. Create NodeGroup for a given cluster

   ```console
   eksctl create nodegroup --config-file eks-nodegroup.yaml

   kind: ClusterConfig
   apiVersion: eksctl.io/v1alpha5
   metadata:
     name: <cluster-name>
     region: <region>
     version: "1.21"
   availabilityZones:
     - <zone-1>
     - <zone-2>
   vpc:
     id: "<vpc-id>"
     subnets:
       private:
         us-east-1d:
           id: "<subnet-id"
         us-east-1f:
           id: "<subent-id>"
     securityGroup: "<security-group>"
   iam:
     withOIDC: true
   managedNodeGroups:
     - name: alab-workers
       instanceType: m5.large
       desiredCapacity: 3
       VolumeSize: 50
       VolumeType: gp2
       privateNetworking: true
       ssh:
         publicKeyPath: <path/to/id_rsa_pub>

   ```

   ```console
   eksctl utils associate-iam-oidc-provider --region=us-east-1 --cluster=<cluster-name> --approve
   ```

2. Create an EFS as shared storage. EFS stands for Elastic File System and is a scalable storage solution that can be used for general purpose workloads.

   ```console
   curl -S https://raw.githubusercontent.com/kubernetes-sigs/aws-efs-csi-driver/v1.2.0/docs/iam-policy-example.json -o iam-policy.json
   aws iam create-policy \
     --policy-name EFSCSIControllerIAMPolicy \
     --policy-document file://iam-policy.json
   ```

   ```console
   eksctl create iamserviceaccount \
     --cluster=<cluster> \
     --region <AWS Region> \
     --namespace=kube-system \
     --name=efs-csi-controller-sa \
     --override-existing-serviceaccounts \
     --attach-policy-arn=arn:aws:iam::<AWS account ID>:policy/EFSCSIControllerIAMPolicy \
     --approve
   ```

   ```console
   helm repo add aws-efs-csi-driver https://kubernetes-sigs.github.io/aws-efs-csi-driver
   ```

   ```console
   helm repo update
   ```

   ```console
   helm upgrade -i aws-efs-csi-driver aws-efs-csi-driver/aws-efs-csi-driver \
     --namespace kube-system \
     --set image.repository=602401143452.dkr.ecr.us-east-1.amazonaws.com/eks/aws-efs-csi-driver \
     --set controller.serviceAccount.create=false \
     --set controller.serviceAccount.name=efs-csi-controller-sa

   ```

3. Create storageClass.yaml

   ```console
   cat <<EOF > storageClass.yaml
   kind: StorageClass
   apiVersion: storage.k8s.io/v1
   metadata:
     name: efs-sc
   provisioner: efs.csi.aws.com
   parameters:
     provisioningMode: efs-ap
     fileSystemId: <EFS file system ID>
     directoryPerms: "700"
   EOF
   ```

   ```console
   kubectl apply -f storageClass.yaml
   ```
Edit annotationlab-installer.sh inside artifact folder as follows:

   ```console
   helm install annotationlab annotationlab-${ANNOTATIONLAB_VERSION}.tgz                                 \
       --set image.tag=${ANNOTATIONLAB_VERSION}                                                          \
       --set model_server.count=1                                                                        \
       --set ingress.enabled=true                                                                        \
       --set networkPolicy.enabled=true                                                                  \
       --set networkPolicy.enabled=true --set extraNetworkPolicies='- namespaceSelector:
       matchLabels:
         kubernetes.io/metadata.name: kube-system
     podSelector:
       matchLabels:
         app.kubernetes.io/name: traefik
         app.kubernetes.io/instance: traefik'                                                            \
       --set keycloak.postgresql.networkPolicy.enabled=true                                              \
       --set sharedData.storageClass=efs-sc                                                              \
       --set airflow.postgresql.networkPolicy.enabled=true                                               \
       --set postgresql.networkPolicy.enabled=true                                                       \
       --set airflow.networkPolicies.enabled=true                                                        \
       --set ingress.defaultBackend=true                                                                 \
       --set ingress.uploadLimitInMegabytes=16                                                           \
       --set 'ingress.hosts[0].host=domain.tld'                                                          \
       --set airflow.model_server.count=1                                                                \
       --set airflow.redis.password=$(bash -c "echo ${password_gen_string}")                             \
       --set configuration.FLASK_SECRET_KEY=$(bash -c "echo ${password_gen_string}")                     \
       --set configuration.KEYCLOAK_CLIENT_SECRET_KEY=$(bash -c "echo ${uuid_gen_string}")               \
       --set postgresql.postgresqlPassword=$(bash -c "echo ${password_gen_string}")                      \
       --set keycloak.postgresql.postgresqlPassword=$(bash -c "echo ${password_gen_string}")             \
       --set keycloak.secrets.admincreds.stringData.user=admin                                           \
       --set keycloak.secrets.admincreds.stringData.password=$(bash -c "echo ${password_gen_string}")

   ```

4. Run annotationlab-installer.sh script
  

   ```console
        ./artifacts/annotationlab-installer.sh
   ```

5. Install ingress Controller


   ```
   helm repo add nginx-stable https://helm.nginx.com/stable
   helm repo update
   helm install my-release nginx-stable/nginx-ingress
   ```

6. Apply ingress.yaml


   ```console
   cat <<EOF > ingress.yaml
   apiVersion: networking.k8s.io/v1
   kind: Ingress
   metadata:
     annotations:
       kubernetes.io/ingress.class: nginx
       meta.helm.sh/release-name: annotationlab
       meta.helm.sh/release-namespace: default
     name: annotationlab
   spec:
     defaultBackend:
       service:
         name: annotationlab
         port:
           name: http
     rules:
     - host: domain.tld
       http:
         paths:
         - backend:
             service:
                 name: annotationlab
                 port:
                   name: http
           path: /
           pathType: ImplementationSpecific
         - backend:
             service:
                 name: annotationlab-keyclo-http
                 port:
                   name: http
           path: /auth
           pathType: ImplementationSpecific
   EOF
   ```

   ```console
   kubectl apply -f ingress.yaml
   ```

</div><div class="h3-box" markdown="1">

## AKS deployment

To deploy Generative AI Lab on Azure Kubernetes Service (AKS) a Kubernetes cluster needs to be created in Microsoft Azure.

1. Login to your [Azure Portal](https://portal.azure.com/) and search for Kubernetes services.

2. On the <bl>Kubernetes services</bl> page click on the `Create` dropdown and select `Create a Kubernetes cluster`.

3. On the <bl>Create Kubernetes cluster</bl> page, select the resource group and provide the name you want to give to the cluster.

   ![AKS create k8 cluster](/assets/images/annotation_lab/AKS-create-k8-cluster.png)

4. You can keep the rest of the fields to default values and click on `Review + create`.

   ![AKS cluster validation](/assets/images/annotation_lab/AKS-cluster-validation.png)

5. Click on `Create` button to start the deployment process.

   ![AKS deployment](/assets/images/annotation_lab/AKS-deployment.png)

6. Once the deployment is completed, click on `Go to resource` button.

7. On the newly created resource page, click on `Connect` button. You will be shown a list of commands to run on the `Cloud Shell` or `Azure CLI` to connect to this resource. We will execute them successively in the following steps.

8. Run the following commands to connect to Azure Kubernetes Service.

   ```sh
   az account set --subscription <subscription-id>
   ```

   > **NOTE:** Replace <subscription-id> with your account's subscription id.

   ```sh
   az aks get-credentials --resource-group <resource-group-name> --name <cluster-name>
   ```

   > **NOTE:** Replace <resource-group-name> and <cluster-name> with what you selected in Step 3.

9. Check to see if `azurefile` or `azuredisk` storage class is present by running the following command:

   ```sh
   kubectl get storageclass
   ```

   Later in the helm script we need to update the value of `sharedData.storageClass` with the respective storage class.

10. Go to the `artifact` directory and from there edit the `annotationlab-installer.sh` script.

    ```sh
    helm install annotationlab annotationlab-${ANNOTATIONLAB_VERSION}.tgz                                 \
        --set image.tag=${ANNOTATIONLAB_VERSION}                                                          \
        --set model_server.count=1                                                                        \
        --set ingress.enabled=true                                                                        \
        --set networkPolicy.enabled=true                                                                  \
        --set networkPolicy.enabled=true --set extraNetworkPolicies='- namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: kube-system
      podSelector:
        matchLabels:
          app.kubernetes.io/name: traefik
          app.kubernetes.io/instance: traefik'                                                            \
        --set keycloak.postgresql.networkPolicy.enabled=true                                              \
        --set sharedData.storageClass=azurefile                                                           \
        --set airflow.postgresql.networkPolicy.enabled=true                                               \
        --set postgresql.networkPolicy.enabled=true                                                       \
        --set airflow.networkPolicies.enabled=true                                                        \
        --set ingress.defaultBackend=true                                                                 \
        --set ingress.uploadLimitInMegabytes=16                                                           \
        --set 'ingress.hosts[0].host=domain.tld'                                                          \
        --set airflow.model_server.count=1                                                                \
        --set airflow.redis.password=$(bash -c "echo ${password_gen_string}")                             \
        --set configuration.FLASK_SECRET_KEY=$(bash -c "echo ${password_gen_string}")                     \
        --set configuration.KEYCLOAK_CLIENT_SECRET_KEY=$(bash -c "echo ${uuid_gen_string}")               \
        --set postgresql.postgresqlPassword=$(bash -c "echo ${password_gen_string}")                      \
        --set keycloak.postgresql.postgresqlPassword=$(bash -c "echo ${password_gen_string}")             \
        --set keycloak.secrets.admincreds.stringData.user=admin                                           \
        --set keycloak.secrets.admincreds.stringData.password=$(bash -c "echo ${password_gen_string}")
    ```

11. Execute the `annotationlab-installer.sh` script to run the Generative AI Lab installation.

    ```sh
    ./annotationlab-installer.sh
    ```

12. Verify if the installation was successful.

    ```sh
    kubectl get pods
    ```

13. Install ingress controller. This will be required for load-balancing purpose.

    ```
    helm repo add nginx-stable https://helm.nginx.com/stable
    helm repo update
    helm install my-release nginx-stable/nginx-ingress
    ```

14. Create a YAML configuration file named `ingress.yaml` with the following configuration

    ```sh
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      annotations:
        kubernetes.io/ingress.class: nginx
        meta.helm.sh/release-name: annotationlab
        meta.helm.sh/release-namespace: default
      name: annotationlab
    spec:
      defaultBackend:
        service:
          name: annotationlab
          port:
            name: http
      rules:
      - host: domain.tld
        http:
          paths:
          - backend:
              service:
                  name: annotationlab
                  port:
                    name: http
            path: /
            pathType: ImplementationSpecific
          - backend:
              service:
                  name: annotationlab-keyclo-http
                  port:
                    name: http
            path: /auth
            pathType: ImplementationSpecific
    ```

15. Apply the `ingress.yaml` by running the following command

    ```sh
    kubectl apply -f ingress.yaml
    ```

</div><div class="h3-box" markdown="1">

## AirGap Environment

### Get Artifact

Run the following command on a terminal to fetch the compressed artifact (_tarball_) of the Generative AI Lab.

```bash
wget https://s3.amazonaws.com/auxdata.johnsnowlabs.com/annotationlab/annotationlab-$VERSION.tar.gz
```

Extract the tarball and the change directory to the extracted folder (_artifacts_):

```bash
tar -xzf annotationlab-$VERSION.tar.gz
cd artifacts
```

Replace `$VERSION` with the version you want to download and install.

</div><div class="h3-box" markdown="1">

### Fresh Install

Run the installer script `annotationlab-installer.sh` with `sudo` privileges.

```bash
$ sudo su
$ ./annotationlab-installer.sh
```

</div><div class="h3-box" markdown="1">

### Upgrade

Run the upgrade script `annotationlab-updater.sh` with `sudo` privileges.

```bash
$ sudo su
$ ./annotationlab-updater.sh
```

</div><div class="h3-box" markdown="1">

## OpenShift

Generative AI Lab can also be installed using the operator framework on an OpenShift cluster. The Generative AI Lab operator can be found under the <bl>OperatorHub</bl>.

</div><div class="h3-box" markdown="1">

### Find and select

The <bl>OperatorHub</bl> has a large list of operators that can be installed into your cluster. Search for Generative AI Lab operator under AI/Machine Learning category and select it.

![Select Operator](/assets/images/annotation_lab/Select-Operator.png)

</div><div class="h3-box" markdown="1">

### Install

Some basic information about this operator is provided on the navigation panel that opens after selecting Generative AI Lab on the previous step.

> **NOTE:** Make sure you have defined shared storage such as `efs/nfs/cephfs` prior to installing the Generative AI Lab Operator.

Click on the `Install` button located on the top-left corner of this panel to start the installation process.

![Install Operator](/assets/images/annotation_lab/Install-Operator.png)

After successful installation of the Generative AI Lab operator, you can access it by navigating to the <bl>Installed Operators</bl> page.

</div><div class="h3-box" markdown="1">

### Create Instance

Next step is to create a cluster instance of the Generative AI Lab. For this, select the Generative AI Lab operator under the <bl>Installed Operators</bl> page and then switch to _Annotationlab_ tab. On this section, click on `Create Annotationlab` button to spawn a new instance of Generative AI Lab.

![Create Instance](/assets/images/annotation_lab/Create-Instance.png)

**Define shared Storage Class**

Update the `storageClass` property in the YAML configuration to define the storage class to one of `efs`, `nfs`, or `cephfs` depending upon what storage you set up before Generative AI Lab operator installation.

![Define Storage Class](/assets/images/annotation_lab/Define-StorageClass.png)

**Define domain name**

Update the `host` property in the YAML configuration to define the required domain name to use instead of the default hostname `annotationlab` as shown in the image below.

![Define Hostname](/assets/images/annotation_lab/Define-Hostname.png)

Click on `Create` button once you have made all the necessary changes. This will also set up all the necessary resources to run the instance in addition to standing up the services themselves.

</div><div class="h3-box" markdown="1">

### View Resources

After the instance is successfully created we can visit its page to view all the resources as well as supporting resources like the secrets, configuration maps, etc that were created.

![View Resources](/assets/images/annotation_lab/View-Resources.png)

Now, we can access the Generative AI Lab from the provided domain name or also from the location defined for this service under the `Networking > Routes` page

</div><div class="h3-box" markdown="1">

## Work over proxy

**Custom CA certificate**

You can provide a custom CA certificate chain to be included into the deployment. To do it add `--set-file custom_cacert=./cachain.pem` options to `helm install/upgrade` command inside `annotationlab-installer.sh` and `annotationlab-updater.sh` files.

_cachain.pem_ must include a certificate in the following format:

```bash
-----BEGIN CERTIFICATE-----
....
-----END CERTIFICATE-----
```

</div><div class="h3-box" markdown="1">

**Proxy env variables**

You can provide a proxy to use for external communications. To do that add

    `--set proxy.http=[protocol://]<host>[:port]`,
    `--set proxy.https=[protocol://]<host>[:port]`,
    `--set proxy.no=<comma-separated list of hosts/domains>`

commands inside `annotationlab-installer.sh` and `annotationlab-updater.sh` files.

</div><div class="h3-box" markdown="1">

## Recommended Configurations

<table class="table2">
  <tr>
    <th>System requirements</th>
    <td>You can install Generative AI Lab on a Ubuntu 20+ machine.</td>
  </tr>
  <tr>
    <th>Port requirements</th>
    <td>Generative AI Lab expects ports <bl>443</bl> and <bl>80</bl> to be open by default.</td>
  </tr>
  <tr>
    <th>Server requirements</th>
    <td>The minimal required configuration is <bl>32GB RAM, 8 Core CPU, 512 SSD</bl>.<br /><br />

    The ideal configuration in case model training and preannotations are required on a large number of tasks is <bl>64 GiB, 16 Core CPU, 512 SSD</bl>.
    </td>

  </tr>
  <tr>
    <th>Web browser support</th>
    <td>Generative AI Lab is tested with the latest version of Google Chrome and is expected to work in the latest versions of:
      <ul>
      <li>Google Chrome</li>
      <li>Apple Safari</li>
      <li>Mozilla Firefox</li>
      </ul>
    </td>
  </tr>
</table>
</div>