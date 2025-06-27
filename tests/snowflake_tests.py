from johnsnowlabs.auto_install.snowflake.work_utils import test_udf, get_client
from tests.utilsz import secrets
from johnsnowlabs import nlp, medical


from johnsnowlabs import nlp
from sparknlp_jsl.annotator import *


def load_re_pipe():
    spark = nlp.start()
    document_assambler = DocumentAssembler() \
        .setInputCol("text") \
        .setOutputCol("document")

    sentence_detector = SentenceDetector() \
        .setInputCols(["document"]) \
        .setOutputCol("sentence")

    tokenizer = sparknlp.annotators.Tokenizer() \
        .setInputCols(["sentence"]) \
        .setOutputCol("token")

    word_embeddings = WordEmbeddingsModel() \
        .pretrained("embeddings_clinical", "en", "clinical/models") \
        .setInputCols(["sentence", "token"]) \
        .setOutputCol("embeddings")

    pos_tagger = PerceptronModel() \
        .pretrained("pos_clinical", "en", "clinical/models") \
        .setInputCols(["sentence", "token"]) \
        .setOutputCol("pos_tags")

    ner_tagger = MedicalNerModel() \
        .pretrained("ner_posology", "en", "clinical/models") \
        .setInputCols("sentence", "token", "embeddings") \
        .setOutputCol("ner_tags")

    ner_chunker = NerConverterInternal() \
        .setInputCols(["sentence", "token", "ner_tags"]) \
        .setOutputCol("ner_chunk")

    dependency_parser = DependencyParserModel() \
        .pretrained("dependency_conllu", "en") \
        .setInputCols(["sentence", "pos_tags", "token"]) \
        .setOutputCol("dependencies")

    reModel = RelationExtractionModel() \
        .pretrained("posology_re") \
        .setInputCols(["embeddings", "pos_tags", "ner_chunk", "dependencies"]) \
        .setOutputCol("relations") \
        .setMaxSyntacticDistance(4)

    pipeline = Pipeline(stages=[
        document_assambler,
        sentence_detector,
        tokenizer,
        word_embeddings,
        pos_tagger,
        ner_tagger,
        ner_chunker,
        dependency_parser,
        reModel
    ])

    empty_data = spark.createDataFrame([[""]]).toDF("text")

    pipe3 = pipeline.fit(empty_data)
    return pipe3


def load_pipeline_customer(): #->
    # pipeline
    # ner_model_path = f"{config['adls_home']}/{config['ner_model_path']}"
    # assertion_model_path = f"{config['adls_home']}/{config['assertion_model_path']}"
    # entity_assertion = config['entity_assertion']
    spark = nlp.start()
    document_assembler = DocumentAssembler() \
        .setInputCol("text") \
        .setOutputCol("document")

    sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models") \
        .setInputCols(["document"]) \
        .setOutputCol("sentence")

    tokenizer = RegexTokenizer() \
        .setInputCols(["sentence"]) \
        .setOutputCol("token")
    # .setPattern(config["token_regex_pattern"])

    word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models") \
        .setInputCols(["sentence","token"]) \
        .setOutputCol("embeddings")

    ner_custom = MedicalNerModel.pretrained("ner_snomed_term", "en", "clinical/models") \
        .setInputCols(["sentence","token","embeddings"]) \
        .setOutputCol("ner_custom")

    ner_chunk_custom = NerConverterInternal() \
        .setInputCols(["sentence","token","ner_custom"]) \
        .setOutputCol("ner_chunk_custom")

    embeddings_bert = BertEmbeddings.pretrained("biobert_pubmed_base_cased") \
        .setInputCols(["sentence", "token"]) \
        .setOutputCol("embeddings_bert")

    ner_bert = MedicalNerModel.pretrained("ner_ade_biobert", "en", "clinical/models") \
        .setInputCols(["sentence", "token", "embeddings_bert"]) \
        .setOutputCol("ner_bert")

    ner_chunk_bert = ( NerConverter()
                       .setInputCols(["sentence", "token", "ner_bert"])
                       .setOutputCol("ner_chunk_bert")
                       .setWhiteList(["ADE"])
                       )

    chunk_merger = ChunkMergeApproach() \
        .setInputCols("ner_chunk_custom", "ner_chunk_bert") \
        .setOutputCol("ner_chunk") \
        .setMergeOverlapping(True) \
        .setSelectionStrategy("Sequential")

    clinical_assertion = ( AssertionDLModel.pretrained("assertion_vop_clinical", "en", "clinical/models")
                           .setInputCols(["sentence", "ner_chunk", "embeddings"])
                           .setOutputCol("assertion")
                           .setEntityAssertionCaseSensitive(False)
                           # .setEntityAssertion(entity_assertion)
                           )

    pos_tagger = PerceptronModel.pretrained("pos_clinical", "en", "clinical/models") \
        .setInputCols(["sentence", "token"]) \
        .setOutputCol("pos_tags")

    dependency_parser = DependencyParserModel.pretrained("dependency_conllu", "en") \
        .setInputCols(["sentence", "pos_tags", "token"]) \
        .setOutputCol("dependencies")

    re_biomarker = ( RelationExtractionModel.pretrained("re_oncology_biomarker_result_wip", "en", "clinical/models") \
                     .setInputCols(["embeddings", "pos_tags", "ner_chunk", "dependencies"]) \
                     .setOutputCol("re_biomarker") \
                     .setRelationPairs([
        'Biomarker-Biomarker_Result', #'Biomarker_Result-Biomarker',
    ])
                     .setPredictionThreshold(0.9)
                     .setMaxSyntacticDistance(4)
                     )
    re_temporal = RelationExtractionModel.pretrained("re_oncology_temporal_wip", "en", "clinical/models") \
        .setInputCols(["embeddings", "pos_tags", "ner_chunk", "dependencies"]) \
        .setOutputCol("re_temporal") \
        .setRelationPairs([
        "Cancer_Dx-Date", #"Date-Cancer_Dx",
        "Staging-Date", "Date-Staging",
        "Invasion-Date", "Date-Invasion",
        "Tumor_Finding-Date", "Date-Tumor_Finding",
        "Adenopathy-Date", "Date-Adenopathy",

        "Biomarker_Result-Date", "Date-Biomarker_Result",
        "Pathology_Result-Date", "Date-Pathology_Result",

        "Cancer_Therapy-Date", "Date-Cancer_Therapy",
        "Radiotherapy-Date", "Date-Radiotherapy",
        "Line_Of_Therapy-Date", "Date-Line_Of_Therapy",
        "Response_to_treatment-Date","Date-Response_to_treatment",
        "ADE-Date","Date-ADE"

    ]) \
        .setMaxSyntacticDistance(10)
    re_location = RelationExtractionModel.pretrained("re_oncology_location_wip", "en", "clinical/models") \
        .setInputCols(["embeddings", "pos_tags", "ner_chunk", "dependencies"]) \
        .setOutputCol("re_location") \
        .setRelationPairs([
        "Tumor_Finding-Anatomical_Site", "Anatomical_Site-Tumor_Finding",
        "Cancer_Dx-Anatomical_Site", "Anatomical_Site-Cancer_Dx",
        "Metastasis-Anatomical_Site", "Anatomical_Site-Metastasis",
        "Invasion-Anatomical_Site",  "Anatomical_Site-Invasion",
    ]) \
        .setMaxSyntacticDistance(6)
    re_pathology = RelationExtractionModel.pretrained("re_oncology_test_result_wip", "en", "clinical/models") \
        .setInputCols(["embeddings", "pos_tags", "ner_chunk", "dependencies"]) \
        .setOutputCol("re_pathology") \
        .setRelationPairs([
        "Pathology_Test-Pathology_Result", "Pathology_Result-Pathology_Test"]) \
        .setMaxSyntacticDistance(4)

    re_ner_chunk_filter = ( RENerChunksFilter()
    .setInputCols(["ner_chunk", "dependencies"])
    .setOutputCol("re_ner_chunk")
    .setMaxSyntacticDistance(6)
    .setRelationPairs([
        "Tumor_Finding-Tumor_Size", "Tumor_Size-Tumor_Finding",
        "Response_To_Treatment-Cancer_Therapy", "Cancer_Therapy-Response_To_Treatment",
        "Response_To_Treatment-Radiotherapy", "Radiotherapy-Response_To_Treatment",
        "Cancer_Dx-Staging", "Staging-Cancer_Dx",
        "Cancer_Dx-Histological_Type","Histological_Type-Cancer_Dx",
        "Cancer_Dx-Grading","Grading-Cancer_Dx",
        "Cancer_Dx-Cancer_Therapy","Cancer_Therapy-Cancer_Dx",
    ])
    )
    re_oncobert = RelationExtractionDLModel.pretrained("redl_oncology_biobert_wip", "en", "clinical/models") \
        .setInputCols(["re_ner_chunk", "sentence"]) \
        .setOutputCol("re_oncobert")

    re_ade_model = RelationExtractionModel() \
        .pretrained("re_ade_clinical", "en", 'clinical/models') \
        .setInputCols(["embeddings", "pos_tags", "ner_chunk", "dependencies"]) \
        .setOutputCol("re_ade") \
        .setMaxSyntacticDistance(10) \
        .setPredictionThreshold(0.1) \
        .setRelationPairs(["ADE-Cancer_Therapy", "Cancer_Therapy-ADE"]) \
        .setRelationPairsCaseSensitive(False)
    re_ade_model.setCustomLabels({"1": "ADE_of", "0": "0"})

    annotation_merger = AnnotationMerger() \
        .setInputCols("re_biomarker", "re_temporal","re_location","re_pathology","re_oncobert","re_ade") \
        .setInputType("category") \
        .setOutputCol("all_relations")

    ner_stages = [document_assembler,
                  sentence_detector,
                  tokenizer,
                  word_embeddings,
                  ner_custom,
                  ner_chunk_custom,
                  embeddings_bert,
                  ner_bert,
                  ner_chunk_bert,
                  chunk_merger,
                  clinical_assertion,
                  pos_tagger,
                  dependency_parser,
                  re_biomarker,
                  re_location,
                  re_temporal,
                  re_pathology,
                  re_ner_chunk_filter,
                  re_oncobert,
                  re_ade_model,
                  annotation_merger
                  ]

    ner_pipeline = Pipeline(stages=ner_stages)
    empty_data = spark.createDataFrame([[""]]).toDF("text")
    ner_model = ner_pipeline.fit(empty_data)
    return ner_model

def get_pipe():
    spark = nlp.start()

    # passcode = input('Give new Passcode')
    documentAssembler = nlp.DocumentAssembler() \
        .setInputCol("text") \
        .setOutputCol("document")

    sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models") \
        .setInputCols(["document"]) \
        .setOutputCol("sentence")

    tokenizer = nlp.Tokenizer() \
        .setInputCols(["sentence"]) \
        .setOutputCol("token")

    word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models") \
        .setInputCols(["sentence", "token"]) \
        .setOutputCol("embeddings")

    ner = medical.NerModel.pretrained("ner_jsl","en","clinical/models") \
        .setInputCols(["sentence","token","embeddings"]) \
        .setOutputCol("ner") \
        .setLabelCasing("upper")

    ner_converter = medical.NerConverter() \
        .setInputCols(["sentence", "token", "ner"]) \
        .setOutputCol("ner_chunk")

    ner_pipeline = nlp.Pipeline(stages=[
        documentAssembler,
        sentenceDetector,
        tokenizer,
        word_embeddings,
        ner,
        ner_converter])

    empty_data = spark.createDataFrame([[""]]).toDF("text")
    ner_model = ner_pipeline.fit(empty_data)
    return ner_model

def test_create_service_udf_custom_pipe():

    # pipe = get_pipe()
    passcode = input('Give new Passcode')
    pipe = load_re_pipe()
    role_name, db_name, warehouse_name, schema_name, compute_pool_name, repo_url = nlp.snowflake_common_setup(
        secrets.snowflake_user, secrets.snowflake_account, secrets.snowflake_password,passcode=passcode
    )
    passcode = input('Give new Passcode')


    nlp.deploy_as_snowflake_udf(
                                custom_pipeline=pipe,
                                license_path=secrets.airgap_lic,
                                repo_url=repo_url,
                                role_name=role_name,
                                database_name=db_name,
                                warehouse_name=warehouse_name,
                                schema_name=schema_name,
                                compute_pool_name=compute_pool_name,
                                snowflake_user=secrets.snowflake_user,
                                snowflake_account=secrets.snowflake_account,
                                snowflake_password=secrets.snowflake_password,
                                passcode=passcode,
                                udf_name='re_udf'
                                )


def test_create_service_udf_open_source():
    # passcode = input('Give new Passcode')
    passcode = input('Give new Passcode')
    role_name, db_name, warehouse_name, schema_name, compute_pool_name, repo_url = nlp.snowflake_common_setup(
        secrets.snowflake_user, secrets.snowflake_account, secrets.snowflake_password,passcode=passcode
    )
    passcode = input('Give new Passcode')


    nlp.deploy_as_snowflake_udf(pipeline_name='explain_clinical_doc_oncology',
                                pipeline_bucket='clinical/models',
                                pipeline_language='en',
                                # license_path=secrets.airgap_lic,
                                repo_url=repo_url,
                                role_name=role_name,
                                database_name=db_name,
                                warehouse_name=warehouse_name,
                                schema_name=schema_name,
                                compute_pool_name=compute_pool_name,
                                snowflake_user=secrets.snowflake_user,
                                snowflake_account=secrets.snowflake_account,
                                snowflake_password=secrets.snowflake_password,
                                passcode=passcode,
                                udf_name='ner_udf12'
                                )


def test_query_udf():
    passcode = input('Give new Passcode')
    role_name, db_name, warehouse_name, schema_name, compute_pool_name, repo_url = nlp.snowflake_common_setup(
        secrets.snowflake_user, secrets.snowflake_account, secrets.snowflake_password,passcode=passcode
    )
    client = get_client(secrets.snowflake_user, secrets.snowflake_password, secrets.snowflake_account, warehouse_name, db_name,
                        schema_name, role_name, passcode, None)
    test_udf(client, 'ner_udf11')

def test_create_service_udf_healthcare():
    role_name, db_name, warehouse_name, schema_name, compute_pool_name, repo_url = nlp.snowflake_common_setup(
        secrets.snowflake_user, secrets.snowflake_account, secrets.snowflake_password,
        compute_pool_name='testpool6',
    )
    nlp.deploy_as_snowflake_udf('en.de_identify.clinical_pipeline',
                                                         repo_url=repo_url,
                                                         role_name=role_name,
                                                         database_name=db_name,
                                                         warehouse_name=warehouse_name,
                                                         schema_name=schema_name,
                                                         compute_pool_name=compute_pool_name,
                                                         snowflake_user=secrets.snowflake_user,
                                                         snowflake_account=secrets.snowflake_account,
                                                         snowflake_password=secrets.snowflake_password,
                                                         license_path=secrets.airgap_lic,
                                                         )


def test_create_service_udf_visual():
    nlp.deploy_as_snowflake_udf('todo', license_path=secrets.airgap_lic)
