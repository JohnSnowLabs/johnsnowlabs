import queue
import time

import pytest
from nlu.utils.environment.offline_load_utils import NLP_ref_to_NLU_ref

from johnsnowlabs import nlp, settings
from johnsnowlabs.auto_install.databricks.install_utils import (
    cluster_exist_with_name_and_runtime,
    get_db_client_for_token,
    get_cluster_id,
    wait_till_cluster_running,
    _get_cluster_id,
)
from johnsnowlabs.auto_install.health_checks.generate_test import (
    generate_endpoint_test,
)
from johnsnowlabs.auto_install.health_checks.generate_test import (
    generate_load_predict_test,
)
from johnsnowlabs.utils.enums import DatabricksClusterStates
from tests.utilsz import secrets as sct

db_cloud_node_params = pytest.mark.parametrize(
    "creds, node_type",
    [
        ("aws_creds", "aws_cpu_node"),
        # ("azure_creds", "azure_cpu_node"),
        # ("azure_creds", "azure_gpu_node_type"),
    ],
    indirect=["creds", "node_type"],
)
db_cloud_params = pytest.mark.parametrize(
    "creds",
    [
        "aws_creds",
        # "azure_creds",
    ],
    indirect=["creds"],
)


@pytest.fixture()
def azure_gpu_node_type():
    return "Standard_NC4as_T4_v3"


@pytest.fixture()
def azure_cpu_node():
    return "Standard_DS3_v2"


@pytest.fixture()
def aws_cpu_node():
    return "i3.xlarge"


@pytest.fixture()
def azure_creds():
    import tests.utilsz.secrets as sct

    lic = sct.db_lic_azure
    host = sct.ckl_host_azure
    token = sct.ckl_token_azure
    return lic, host, token


@pytest.fixture()
def azure_trial_creds():
    import tests.utilsz.secrets as sct

    lic = sct.azure_trail_lic2
    host = sct.azure_trail_host2
    token = sct.azure_trail_token2
    return lic, host, token


@pytest.fixture()
def aws_creds():
    import tests.utilsz.secrets as sct

    lic = sct.ckl_lic_aws
    host = sct.ckl_host_aws
    token = sct.ckl_token_aws
    return lic, host, token


@pytest.fixture
def creds(request):
    return request.getfixturevalue(request.param)


@pytest.fixture
def node_type(request):
    return request.getfixturevalue(request.param)


def host_creds(host):
    if host == "aws":
        return aws_creds()
    elif host == "azure":
        return azure_creds()
    else:
        raise Exception("Unknown host")


def assert_job_suc(state):
    assert state["state"]["result_state"] == "SUCCESS"


def run_endpoint_tests(test_cluster_id, host, token, model):
    # generate job.py script and submit it
    job_id, job_url = nlp.run_in_databricks(
        generate_endpoint_test(model, sct.container_lic_json),
        databricks_cluster_id=test_cluster_id,
        databricks_host=host,
        databricks_token=token,
        run_name=f"endpoint_creation_test_run_{model}",
        return_job_url=True,
    )
    try:
        assert_job_suc(job_id)
    except Exception as e:
        return job_url, False

    return job_url, True


def run_load_predict_tests(test_cluster_id, host, token, model):
    # generate job.py script and submit it
    job_id, job_url = nlp.run_in_databricks(
        generate_load_predict_test(model),
        databricks_cluster_id=test_cluster_id,
        databricks_host=host,
        databricks_token=token,
        run_name=f"load_predict_test_{model}",
        return_job_url=True,
    )

    try:
        assert_job_suc(job_id)
    except Exception as e:
        return job_url, False

    return job_url, True


def run_cluster_test_suite(test_cluster_id, host, token):
    # run test suite again a existing cluster

    # Test modules
    import johnsnowlabs.auto_install.health_checks.hc_test as hc_test
    import johnsnowlabs.auto_install.health_checks.ocr_test as ocr_test
    import johnsnowlabs.auto_install.health_checks.nlp_test as nlp_test

    assert_job_suc(
        nlp.run_in_databricks(
            nlp_test,
            databricks_cluster_id=test_cluster_id,
            databricks_host=host,
            databricks_token=token,
            run_name="nlp_test",
        )
    )

    assert_job_suc(
        nlp.run_in_databricks(
            hc_test,
            databricks_cluster_id=test_cluster_id,
            databricks_host=host,
            databricks_token=token,
            run_name="hc_test",
        )
    )

    assert_job_suc(
        nlp.run_in_databricks(
            ocr_test,
            databricks_cluster_id=test_cluster_id,
            databricks_host=host,
            databricks_token=token,
            run_name="ocr_test",
        )
    )


def get_one_model_per_class():
    # todo actually generate from spellbook
    return [
        # "tokenize",
        "sentiment",
        "ner",
    ]
    #     "bert",
    #     "elmo",
    #     "albert",
    #     "roberta",
    # ]


def delete_all_test_clusters(db_client):
    for i in range(10):
        while _get_cluster_id(db_client, f"TEST_CLUSTER_{i}"):
            cluster_id = _get_cluster_id(db_client, f"TEST_CLUSTER_{i}")
            db_client.cluster.permanent_delete_cluster(cluster_id)
            print(f"Deleted cluster {cluster_id}")
            time.sleep(5)


# TODO add UC cluster!?
def get_or_create_test_cluster(
    creds, node_type, n=0, runtime=None, clean_workspace=False
):
    """
    Creates a cluster with name TEST_CLUSTER_{n} and runtime runtime if it doesn't exist.
    If it exists, it checks if it's running and if not, it starts it.
    "exists" means another cluster with same name and runtime exists.
    """
    # m5d.2xlarge  #
    lic, host, token = creds
    # runtime = "9.1.x-scala2.12"
    if runtime is None:
        runtime = settings.db_spark_version
    cluster_name = f"TEST_CLUSTER_{n}"
    db_client = get_db_client_for_token(host, token)

    # 1) Check if cluster with name and correct runtime exists and it's running state If not, create it.
    if cluster_exist_with_name_and_runtime(db_client, cluster_name, runtime):
        cluster_id = get_cluster_id(db_client, cluster_name, runtime)

        status = DatabricksClusterStates(
            db_client.cluster.get_cluster(
                cluster_id,
            )["state"]
        )

        # if status is terminated, try restart it
        if status == DatabricksClusterStates.TERMINATED:
            db_client.cluster.start_cluster(cluster_id=cluster_id)
            wait_till_cluster_running(db_client, cluster_id)
            status = DatabricksClusterStates(
                db_client.cluster.get_cluster(
                    cluster_id,
                )["state"]
            )
        if status == DatabricksClusterStates.RUNNING:
            return cluster_id
        else:
            print(
                f"Could not find or start {cluster_name} with runtime {runtime} creating a new one"
            )

    else:
        #  no cluster exists, create new one
        cluster_id = nlp.install_to_databricks(
            spark_version=runtime,
            json_license_path=lic,
            databricks_host=host,
            databricks_token=token,
            driver_node_type_id=node_type,
            node_type_id=node_type,
            cluster_name=cluster_name,
            clean_cluster=clean_workspace,
            block_till_cluster_ready=True,
        )
        return cluster_id


test_funcs = {
    "endpoint": run_endpoint_tests,
    "load_predict": run_load_predict_tests,
    # "cluster_test_suite": run_cluster_test_suite,
}


def execute_test(test_type, cluster_id, host, token, model):
    if test_type in test_funcs:
        return test_funcs[test_type](
            cluster_id, host, token, model, raise_on_fail=False
        )
    else:
        raise ValueError(f"Unknown test type {test_type}")


def subtester_thread(cluster_id, job_que, host, token, results, test_type):
    while not job_que.empty():
        try:
            model = job_que.get_nowait()
            result = {"model": model}
        except queue.Empty:
            print("Que Empty Thread done!")
            return
        print(f"Test {model} with {test_type}")
        result["job_url"], result["success"] = test_funcs[test_type](
            cluster_id, host, token, model
        )
        results[model] = result
        print(f"✅ {model} TEST RESULTS {results[model]} ")


mm_models = [
    "ner_chemd_clinical_pipeline",
    "summarizer_clinical_questions_pipeline",
    "summarizer_clinical_guidelines_large_pipeline",
    "summarizer_clinical_jsl_augmented_pipeline",
    "summarizer_clinical_laymen_onnx",
    "summarizer_clinical_laymen",
    "ner_profiling_biobert",
    " ner_jsl_pipeline assertion_jsl_augmented",
    "ner_jsl_langtest_pipeline",
    "ner_living_species_pipeline",
    "ner_jsl_pipeline",
    "sbiobertresolve_cpt_augmented",
    "sbiobertresolve_HPO",
    "sbiobertresolve_icd10cm_augmented_billable_hcc",
    "sbiobertresolve_loinc_augmented",
    "sbiobertresolve_rxnorm_augmented",
    "medication_resolver_transform_pipeline",
    "sbiobertresolve_snomed_findings",
    "umls_disease_syndrome_resolver_pipeline",
    "umls_drug_resolver_pipeline",
    "umls_drug_substance_resolver_pipeline",
    "umls_major_concepts_resolver_pipeline",
    "umls_clinical_findings_resolver_pipeline",
    "bert_sequence_classifier_gender_biobert",
    "ner_cellular_pipeline",
    "summarizer_generic_jsl_pipeline",
    "biogpt_chat_jsl",
    "medical_qa_biogpt",
    "re_test_result_date_pipeline",
    "re_temporal_events_clinical_pipeline",
    "ner_pathogen_pipeline",
    "ner_supplement_clinical_pipeline",
    "clinical_notes_qa_base_onnx",
    "clinical_notes_qa_large_onnx",
    "ner_nihss redl_nihss_biobert",
    "multiclassifierdl_hoc",
    "oncology_general_pipeline",
    "ner_profiling_oncology",
    "ner_oncology_response_to_treatment",
    "ner_oncology_therapy",
    "ner_oncology_test",
    "ner_oncology_tnm",
    "ner_oncology_diagnosis",
    "ner_oncology_anatomy_granular",
    "ner_oncology_posology_langtest_pipeline",
    "ner_radiology_wip_clinical assertion_dl_radiology",
    "ner_chexpert_pipeline",
    "summarizer_radiology_pipeline",
    "ner_risk_factors_biobert_pipeline",
    "ner_sdoh_langtest_pipeline assertion_sdoh_wip",
    "ner_profiling_sdoh assertion_sdoh_wip",
    "ner_sdoh_access_to_healthcare",
    "ner_sdoh_community_condition",
    "ner_sdoh_demographics",
    "ner_sdoh_health_behaviours_problems",
    "ner_sdoh_income_social_status",
    "ner_sdoh_social_environment",
    "ner_sdoh_substance_usage",
    "genericclassifier_sdoh_economics_binary_sbiobert_cased_mli",
    "genericclassifier_sdoh_alcohol_usage_sbiobert_cased_mli",
    "ner_nihss_pipeline",
    "ner_vop assertion_vop_clinical_large",
    "bert_sequence_classifier_vop_hcp_consult",
    "bert_sequence_classifier_vop_self_report",
    "bert_sequence_classifier_vop_sound_medical",
    "bert_sequence_classifier_vop_side_effect",
    "bert_sequence_classifier_vop_drug_side_effect",
    "ner_profiling_vop",
    "zero_shot_ner_roberta",
    "re_zeroshot_biobert",
    "distilbert_base_sequence_classifier_imdb",
    "bert_sequence_classifier_emotion",
    "bert_sequence_classifier_age_news",
    "bert_sequence_classifier_trec_coarse",
    "distilbert_base_sequence_classifier_food",
    "bert_sequence_classifier_multilingual_sentiment",
    "distilbert_multilingual_sequence_classifier_allocine",
    "distilbert_base_sequence_classifier_toxicity",
    "bert_sequence_classifier_toxicity",
    "deberta_v3_xsmall_token_classifier_ontonotes",
    "deberta_v3_small_token_classifier_ontonotes",
    "deberta_v3_base_token_classifier_ontonotes",
    "deberta_v3_large_token_classifier_ontonotes",
    "bert_base_token_classifier_ontonote",
    "bert_large_token_classifier_ontonote",
    "bert_token_classifier_aner",
    "bert_token_classifier_named_entity_recognition_nerkor_hu_hungarian",
    "xlmroberta_ner_uk_ner",
    "sentence_detector_dl",
    "bert_token_classifier_base_chinese_ner",
    "bert_token_classifier_base_turkish_cased_ner",
    "roberta_qa_deepset_base_squad2",
    "bert_qa_arap",
    "camembert_base_qa_fquad",
    "distilbert_qa_base_cased_squadv2",
    "xlm_roberta_qa_xlm_roberta_qa_chaii",
    "bart_large_zero_shot_classifier_mnli",
    "roberta_base_zero_shot_classifier_nli",
    "bert_base_cased_zero_shot_classifier_xnli",
    "distilbert_base_zero_shot_classifier_uncased_mnli",
    "distilbert_base_zero_shot_classifier_turkish_cased_snli",
    "xlm_roberta_large_zero_shot_classifier_xnli_anli",
    "opus_mt_en_zh",
    "opus_mt_en_es",
    "opus_mt_en_fr",
    "opus_mt_en_it",
    "opus_mt_es_en",
    "opus_mt_fr_en",
    "opus_mt_it_en",
    "distilbart_xsum_12_6",
    "distilbart_xsum_6_6",
    "distilbart_cnn_6_6",
    "t5_small",
    "e5_small_v2",
    "e5_base_v2",
    "e5_large_v2",
    "e5_small_v2_quantized",
    "e5_base_v2_quantized",
    "e5_large_v2_quantized",
    "instructor_base",
    "instructor_large",
    "multi_qa_mpnet_base_cos_v1",
    "all_mpnet_base_v2",
]


def get_mm_models():
    # TODO use actual langs and make sure all models are resolved
    nlu_refs = []
    miss = []
    for m in mm_models:
        lang = "en"
        models = m.split(" ")
        nlu_ref = ""
        for model in models:
            partial_ref = NLP_ref_to_NLU_ref(model, lang)
            if partial_ref:
                nlu_ref = nlu_ref + " " + partial_ref
            else:
                print(f"{m} missing!")
                miss.append(m)
                continue
        if nlu_ref:
            nlu_refs.append(nlu_ref)

    print(f"Num Missing : {len(miss)} Num Found : {len(nlu_refs)}")
    print("Missing:", miss)
    print("Found:", nlu_refs)
    return nlu_refs
