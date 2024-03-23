{%- capture title -%}
AnnotationMerger
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
Merge annotations from different pipeline steps that have the same annotation type into a unified annotation. Possible annotations that can be merged include:
- document (e.g., output of `DocumentAssembler` annotator)
- token (e.g., output of `Tokenizer` annotator)
- word_embeddings (e.g., output of `WordEmbeddingsModel` annotator)
- sentence_embeddings (e.g., output of `BertSentenceEmbeddings` annotator)
- category (e.g., output of `RelationExtractionModel` annotator)
- date (e.g., output of `DateMatcher` annotator)
- sentiment (e.g., output of `SentimentDLModel` annotator)
- pos (e.g., output of `PerceptronModel` annotator)
- chunk (e.g., output of `NerConverter` annotator)
- named_entity (e.g., output of `NerDLModel` annotator)
- regex (e.g., output of `RegexTokenizer` annotator)
- dependency (e.g., output of `DependencyParserModel` annotator)
- language (e.g., output of `LanguageDetectorDL` annotator)
- keyword (e.g., output of `YakeModel` annotator)

Parameters:

- `inputType`: The type of the annotations that you want to merge. Possible values.

{%- capture model_api_link -%}
[AnnotationMerger](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/annotator/AnnotationMerger.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[AnnotationMerger](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/annotation_merger/index.html#sparknlp_jsl.annotator.annotation_merger.AnnotationMerger)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[AnnotationMerger](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/AnnotationMerger.ipynb)
{%- endcapture -%}

{%- endcapture -%}

{%- capture model_input_anno -%}
ANY
{%- endcapture -%}

{%- capture model_output_anno -%}
ANY
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

# Create the pipeline with two RE models
documenter = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentencer = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentences")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentences"])\
    .setOutputCol("tokens")

words_embedder = nlp.WordEmbeddingsModel()\
    .pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentences", "tokens"])\
    .setOutputCol("embeddings")

pos_tagger = nlp.PerceptronModel()\
    .pretrained("pos_clinical", "en", "clinical/models") \
    .setInputCols(["sentences", "tokens"])\
    .setOutputCol("pos_tags")

pos_ner_tagger = medical.NerModel()\
    .pretrained("ner_posology", "en", "clinical/models")\
    .setInputCols("sentences", "tokens", "embeddings")\
    .setOutputCol("ner_pos")

pos_ner_chunker = medical.NerConverterInternal()\
    .setInputCols(["sentences", "tokens", "ner_pos"])\
    .setOutputCol("pos_ner_chunks")

dependency_parser = nlp.DependencyParserModel()\
    .pretrained("dependency_conllu", "en")\
    .setInputCols(["sentences", "pos_tags", "tokens"])\
    .setOutputCol("dependencies")

pos_reModel = medical.RelationExtractionModel()\
    .pretrained("posology_re")\
    .setInputCols(["embeddings", "pos_tags", "pos_ner_chunks", "dependencies"])\
    .setOutputCol("pos_relations")\
    .setMaxSyntacticDistance(4)

ade_ner_tagger = medical.NerModel.pretrained("ner_ade_clinical", "en", "clinical/models")\
    .setInputCols("sentences", "tokens", "embeddings")\
    .setOutputCol("ade_ner_tags")  

ade_ner_chunker = medical.NerConverterInternal()\
    .setInputCols(["sentences", "tokens", "ade_ner_tags"])\
    .setOutputCol("ade_ner_chunks")

ade_reModel = medical.RelationExtractionModel()\
    .pretrained("re_ade_clinical", "en", 'clinical/models')\
    .setInputCols(["embeddings", "pos_tags", "ade_ner_chunks", "dependencies"])\
    .setOutputCol("ade_relations")\
    .setMaxSyntacticDistance(10)\
    .setRelationPairs(["drug-ade, ade-drug"])

annotation_merger = medical.AnnotationMerger()\
    .setInputCols("ade_relations", "pos_relations")\
    .setInputType("category")\
    .setOutputCol("all_relations")

merger_pipeline = nlp.Pipeline(stages=[
    documenter,
    sentencer,
    tokenizer, 
    words_embedder, 
    pos_tagger, 
    pos_ner_tagger,
    pos_ner_chunker,
    dependency_parser,
    pos_reModel,
    ade_ner_tagger,
    ade_ner_chunker,
    ade_reModel,
    annotation_merger
])

# Show example result
text = """
The patient was prescribed 1 unit of naproxen for 5 days after meals for chronic low back pain. The patient was also given 1 unit of oxaprozin daily for rheumatoid arthritis presented with tense bullae and cutaneous fragility on the face and the back of the hands.. 
"""
data = spark.createDataFrame([[text]]).toDF("text")

result = merger_pipeline.fit(data).transform(data)
result.selectExpr("pos_relations.result as PosologyRelation", 
                  "ade_relations.result as AdeRelation", 
                  "all_relations.result as MergedRelation").show(truncate=False)

+---------------------------------------------------------+-----------+---------------------------------------------------------------+
|PosologyRelation                                         |AdeRelation|MergedRelation                                                 |
+---------------------------------------------------------+-----------+---------------------------------------------------------------+
|[DOSAGE-DRUG, DRUG-DURATION, DOSAGE-DRUG, DRUG-FREQUENCY]|[1, 1]     |[1, 1, DOSAGE-DRUG, DRUG-DURATION, DOSAGE-DRUG, DRUG-FREQUENCY]|
+---------------------------------------------------------+-----------+---------------------------------------------------------------+



{%- endcapture -%}

{%- capture model_scala_medical -%}
import spark.implicits._

// Create the pipeline with two RE models
val documenter = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentencer = new SentenceDetector()
  .setInputCols(Array("document"))
  .setOutputCol("sentences")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentences"))
  .setOutputCol("tokens")

val words_embedder = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("sentences", "tokens"))
  .setOutputCol("embeddings")

val pos_tagger = PerceptronModel.pretrained("pos_clinical", "en", "clinical/models")
  .setInputCols(Array("sentences", "tokens"))
  .setOutputCol("pos_tags")

val pos_ner_tagger = MedicalNerModel.pretrained("ner_posology", "en", "clinical/models")
  .setInputCols(Array("sentences", "tokens", "embeddings"))
  .setOutputCol("ner_pos")

val pos_ner_chunker = new NerConverterInternal()
  .setInputCols(Array("sentences", "tokens", "ner_pos"))
  .setOutputCol("pos_ner_chunks")

val dependency_parser = DependencyParserModel.pretrained("dependency_conllu", "en")
  .setInputCols(Array("sentences", "pos_tags", "tokens"))
  .setOutputCol("dependencies")

val pos_reModel = RelationExtractionModel.pretrained("posology_re")
  .setInputCols(Array("embeddings", "pos_tags", "pos_ner_chunks", "dependencies"))
  .setOutputCol("pos_relations")
  .setMaxSyntacticDistance(4)

val ade_ner_tagger = MedicalNerModel.pretrained("ner_ade_clinical", "en", "clinical/models")
  .setInputCols(Array("sentences", "tokens", "embeddings"))
  .setOutputCol("ade_ner_tags")

val ade_ner_chunker = new NerConverterInternal()
  .setInputCols(Array("sentences", "tokens", "ade_ner_tags"))
  .setOutputCol("ade_ner_chunks")

val ade_reModel = RelationExtractionModel.pretrained("re_ade_clinical", "en", "clinical/models")
  .setInputCols(Array("embeddings", "pos_tags", "ade_ner_chunks", "dependencies"))
  .setOutputCol("ade_relations")
  .setMaxSyntacticDistance(10)
  .setRelationPairs(Array("drug-ade", "ade-drug"))

val annotation_merger = new AnnotationMerger()
  .setInputCols(Array("ade_relations", "pos_relations"))
  .setInputType("category")
  .setOutputCol("all_relations")

val merger_pipeline = new Pipeline().setStages(Array(
  documenter,
  sentencer,
  tokenizer,
  words_embedder,
  pos_tagger,
  pos_ner_tagger,
  pos_ner_chunker,
  dependency_parser,
  pos_reModel,
  ade_ner_tagger,
  ade_ner_chunker,
  ade_reModel,
  annotation_merger
))


// Show example result

val text =
  """
The patient was prescribed 1 unit of naproxen for 5 days after meals for chronic low back pain. The patient was also given 1 unit of oxaprozin daily for rheumatoid arthritis presented with tense bullae and cutaneous fragility on the face and the back of the hands..
"""

val data = Seq(text).toDF("text")
val result = merger_pipeline.fit(data).transform(data)

+---------------------------------------------------------+-----------+---------------------------------------------------------------+
|PosologyRelation                                         |AdeRelation|MergedRelation                                                 |
+---------------------------------------------------------+-----------+---------------------------------------------------------------+
|[DOSAGE-DRUG, DRUG-DURATION, DOSAGE-DRUG, DRUG-FREQUENCY]|[1, 1]     |[1, 1, DOSAGE-DRUG, DRUG-DURATION, DOSAGE-DRUG, DRUG-FREQUENCY]|
+---------------------------------------------------------+-----------+---------------------------------------------------------------+


{%- endcapture -%}

{%- capture model_python_finance -%}
from johnsnowlabs import nlp, finance

# Create the pipeline with two RE models
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

text_splitter = finance.TextSplitter()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") \
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model_date = finance.NerModel.pretrained("finner_sec_dates", "en", "finance/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner_dates")

ner_converter_date = nlp.NerConverter()\
    .setInputCols(["sentence","token","ner_dates"])\
    .setOutputCol("ner_chunk_date")

ner_model_org= finance.NerModel.pretrained("finner_orgs_prods_alias", "en", "finance/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner_orgs")

ner_converter_org = nlp.NerConverter()\
    .setInputCols(["sentence","token","ner_orgs"])\
    .setOutputCol("ner_chunk_org")\

chunk_merger = finance.ChunkMergeApproach()\
    .setInputCols('ner_chunk_org', "ner_chunk_date")\
    .setOutputCol('ner_chunk')

pos = nlp.PerceptronModel.pretrained()\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("pos")

dependency_parser = nlp.DependencyParserModel().pretrained("dependency_conllu", "en")\
    .setInputCols(["sentence", "pos", "token"])\
    .setOutputCol("dependencies")

re_filter = finance.RENerChunksFilter()\
    .setInputCols(["ner_chunk", "dependencies"])\
    .setOutputCol("re_ner_chunk")\
    .setRelationPairs(["ORG-ORG", "ORG-DATE"])\
    .setMaxSyntacticDistance(10)

reDL = finance.RelationExtractionDLModel().pretrained('finre_acquisitions_subsidiaries_md', 'en', 'finance/models')\
    .setInputCols(["re_ner_chunk", "sentence"])\
    .setOutputCol("relations_acq")\
    .setPredictionThreshold(0.1)

reDL_alias = finance.RelationExtractionDLModel().pretrained('finre_org_prod_alias', 'en', 'finance/models')\
    .setInputCols(["re_ner_chunk", "sentence"])\
    .setOutputCol("relations_alias")\
    .setPredictionThreshold(0.1)

annotation_merger = finance.AnnotationMerger()\
    .setInputCols("relations_acq", "relations_alias")\
    .setOutputCol("relations")\
    .setInputType("category")

nlpPipeline = nlp.Pipeline(stages=[
        document_assembler,
        text_splitter,
        tokenizer,
        embeddings,
        ner_model_date,
        ner_converter_date,
        ner_model_org,
        ner_converter_org,
        chunk_merger,
        pos,
        dependency_parser,
        re_filter,
        reDL,
        reDL_alias,
        annotation_merger])


# Show example result
text ="""Definite-lived intangible assets acquired with Cadence’s fiscal 2021 acquisitions were as follows:
 
Acquisition Date Fair Value
Weighted Average Amortization Period
 
(In thousands)
 (in years)
Existing technology
$
59,100 
13.7 years
Agreements and relationships
28,900 
13.7 years
Tradenames, trademarks and patents
4,600 
14.3 years
Total acquired intangibles with definite lives
$
92,600 
13.7 years
2020 Acquisitions
In fiscal 2020, Cadence acquired all of the outstanding equity of AWR Corporation ("AWR") and Integrand Software, Inc. ("Integrand"). These acquisitions enhanced Cadence’s technology portfolio to address growing radio frequency design activity, driven by expanding use of 5G communications.
The aggregate cash consideration for these acquisitions was $195.6 million, after taking into account cash acquired of $1.5 million. The total purchase consideration was allocated to the assets acquired and liabilities assumed based on their respective estimated fair values on the acquisition dates. Cadence will also make payments to certain employees, subject to continued employment and other performance-based conditions, through the first quarter of fiscal 2023.
 With its acquisitions of AWR and Integrand, Cadence recorded $101.3 million of definite-lived intangible assets with a weighted average amortization period of approximately nine years. The definite-lived intangible assets related primarily to existing technology and customer agreements and relationships. Cadence also recorded $119.4 million of goodwill and $25.1 million of net liabilities, consisting primarily of deferred tax liabilities, assumed deferred revenue and trade accounts receivable. The recorded goodwill was primarily related to the acquired assembled workforce and expected synergies from combining operations of the acquired companies with Cadence. None of the goodwill related to the acquisitions of AWR and Integrand is deductible for tax purposes.
Cadence completed one additional acquisition during fiscal 2020 that was not material to the consolidated financial statements. 
Pro Forma Financial Information
Cadence has not presented pro forma financial information for any of the businesses it acquired during fiscal 2021 and fiscal 2020 because the results of operations for these businesses are not material to Cadence’s consolidated financial statements.
Acquisition-Related Transaction Costs
Transaction costs associated with acquisitions, which consist of professional fees and administrative costs, were not material during fiscal 2021, 2020 or 2019 and were expensed as incurred in Cadence’s consolidated income statements.
NOTE 7. GOODWILL AND ACQUIRED INTANGIBLES
Goodwill
The changes in the carrying amount of goodwill during fiscal 2021 and 2020 were as follows:
 
Gross CarryingAmount
 
(In thousands)
Balance as of December 28, 2019
$
661,856 
Goodwill resulting from acquisitions
120,564 
Effect of foreign currency translation
(333)
Balance as of January 2, 2021
782,087 
Goodwill resulting from acquisitions
154,362 
Effect of foreign currency translation
(8,091)
Balance as of January 1, 2022
$
928,358 
Cadence completed its annual goodwill impairment test during the third quarter of fiscal 2021 and determined that the fair value of Cadence’s single reporting unit exceeded the carrying amount of its net assets and that no impairment existed.
65"""

data = spark.createDataFrame([[text]]).toDF("text")
result = nlpPipeline.fit(data).transform(data)


# Show the results 
result.selectExpr("relations_acq.result as AcqRelation", 
                  "relations_alias.result as AliasRelation", 
                  "relations.result as MergedRelation").show(truncate=False)

+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|AcqRelation                                                                                     |AliasRelation                                                                           |MergedRelation                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[has_acquisition_date, was_acquired_by, other, other, other, has_acquisition_date, other, other]|[has_alias, has_alias, has_alias, has_alias, has_alias, has_alias, has_alias, has_alias]|[has_acquisition_date, was_acquired_by, other, other, other, has_acquisition_date, other, other, has_alias, has_alias, has_alias, has_alias, has_alias, has_alias, has_alias, has_alias]|
+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


{%- endcapture -%}

{%- capture model_scala_finance -%}
import spark.implicits._

// Create the pipeline with two RE models
val document_assembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val text_splitter = new TextSplitter()
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val embeddings = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base", "en")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

val ner_model_date = FinanceNerModel.pretrained("finner_sec_dates", "en", "finance/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner_dates")

val ner_converter_date = new NerConverter()
  .setInputCols(Array("sentence", "token", "ner_dates"))
  .setOutputCol("ner_chunk_date")

val ner_model_org = FinanceNerModel.pretrained("finner_orgs_prods_alias", "en", "finance/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner_orgs")

val ner_converter_org = new NerConverter()
  .setInputCols(Array("sentence", "token", "ner_orgs"))
  .setOutputCol("ner_chunk_org")

val chunk_merger = new Chunker()
  .setInputCols(Array("ner_chunk_org", "ner_chunk_date"))
  .setOutputCol("ner_chunk")

val pos = new PerceptronModel()
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("pos")

val dependency_parser = new DependencyParserModel()
  .pretrained("dependency_conllu", "en")
  .setInputCols(Array("sentence", "pos", "token"))
  .setOutputCol("dependencies")

val re_filter = new RelationExtractionModel()
  .setInputCols(Array("ner_chunk", "dependencies"))
  .setOutputCol("re_ner_chunk")
  .setRelationPairs(Array("ORG-ORG", "ORG-DATE"))
  .setMaxSyntacticDistance(10)

val reDL = new RelationExtractionModel()
  .pretrained("finre_acquisitions_subsidiaries_md", "en", "finance/models")
  .setInputCols(Array("re_ner_chunk", "sentence"))
  .setOutputCol("relations_acq")
  .setPredictionThreshold(0.1)

val reDL_alias = new RelationExtractionModel()
  .pretrained("finre_org_prod_alias", "en", "finance/models")
  .setInputCols(Array("re_ner_chunk", "sentence"))
  .setOutputCol("relations_alias")
  .setPredictionThreshold(0.1)

val annotation_merger = new AnnotationMerger()
  .setInputCols("relations_acq", "relations_alias")
  .setOutputCol("relations")
  .setInputType("category")

val nlpPipeline = new Pipeline().setStages(Array(
  document_assembler,
  text_splitter,
  tokenizer,
  embeddings,
  ner_model_date,
  ner_converter_date,
  ner_model_org,
  ner_converter_org,
  chunk_merger,
  pos,
  dependency_parser,
  re_filter,
  reDL,
  reDL_alias,
  annotation_merger
))

// Show example result
val text = """
Definite-lived intangible assets acquired with Cadence’s fiscal 2021 acquisitions were as follows:
 
Acquisition Date Fair Value
Weighted Average Amortization Period
 
(In thousands)
 (in years)
Existing technology
$
59,100 
13.7 years
Agreements and relationships
28,900 
13.7 years
Tradenames, trademarks and patents
4,600 
14.3 years
Total acquired intangibles with definite lives
$
92,600 
13.7 years
2020 Acquisitions
In fiscal 2020, Cadence acquired all of the outstanding equity of AWR Corporation ("AWR") and Integrand Software, Inc. ("Integrand"). These acquisitions enhanced Cadence’s technology portfolio to address growing radio frequency design activity, driven by expanding use of 5G communications.
The aggregate cash consideration for these acquisitions was $195.6 million, after taking into account cash acquired of $1.5 million. The total purchase consideration was allocated to the assets acquired and liabilities assumed based on their respective estimated fair values on the acquisition dates. Cadence will also make payments to certain employees, subject to continued employment and other performance-based conditions, through the first quarter of fiscal 2023.
 With its acquisitions of AWR and Integrand, Cadence recorded $101.3 million of definite-lived intangible assets with a weighted average amortization period of approximately nine years. The definite-lived intangible assets related primarily to existing technology and customer agreements and relationships. Cadence also recorded $119.4 million of goodwill and $25.1 million of net liabilities, consisting primarily of deferred tax liabilities, assumed deferred revenue and trade accounts receivable. The recorded goodwill was primarily related to the acquired assembled workforce and expected synergies from combining operations of the acquired companies with Cadence. None of the goodwill related to the acquisitions of AWR and Integrand is deductible for tax purposes.
Cadence completed one additional acquisition during fiscal 2020 that was not material to the consolidated financial statements. 
Pro Forma Financial Information
Cadence has not presented pro forma financial information for any of the businesses it acquired during fiscal 2021 and fiscal 2020 because the results of operations for these businesses are not material to Cadence’s consolidated financial statements.
Acquisition-Related Transaction Costs
Transaction costs associated with acquisitions, which consist of professional fees and administrative costs, were not material during fiscal 2021, 2020 or 2019 and were expensed as incurred in Cadence’s consolidated income statements.
NOTE 7. GOODWILL AND ACQUIRED INTANGIBLES
Goodwill
The changes in the carrying amount of goodwill during fiscal 2021 and 2020 were as follows:
 
Gross CarryingAmount
 
(In thousands)
Balance as of December 28, 2019
$
661,856 
Goodwill resulting from acquisitions
120,564 
Effect of foreign currency translation
(333)
Balance as of January 2, 2021
782,087 
Goodwill resulting from acquisitions
154,362 
Effect of foreign currency translation
(8,091)
Balance as of January 1, 2022
$
928,358 
Cadence completed its annual goodwill impairment test during the third quarter of fiscal 2021 and determined that the fair value of Cadence’s single reporting unit exceeded the carrying amount of its net assets and that no impairment existed.
65
"""

val data = Seq(text).toDF("text")
val result = nlpPipeline.fit(data).transform(data)

+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|AcqRelation                                                                                     |AliasRelation                                                                           |MergedRelation                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[has_acquisition_date, was_acquired_by, other, other, other, has_acquisition_date, other, other]|[has_alias, has_alias, has_alias, has_alias, has_alias, has_alias, has_alias, has_alias]|[has_acquisition_date, was_acquired_by, other, other, other, has_acquisition_date, other, other, has_alias, has_alias, has_alias, has_alias, has_alias, has_alias, has_alias, has_alias]|
+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}

{%- capture model_python_legal -%}
from johnsnowlabs import nlp, legal

# Create the pipeline with two RE models
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

text_splitter = legal.TextSplitter()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings =nlp.RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base", "en") \
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model_date = legal.NerModel.pretrained("legner_contract_doc_parties", "en", "legal/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner_parties")

ner_converter_date = nlp.NerConverter()\
    .setInputCols(["sentence","token","ner_parties"])\
    .setOutputCol("ner_chunk_parties")

ner_model_org= legal.NerModel.pretrained("legner_whereas_md", "en", "legal/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner_whereas")

ner_converter_org = nlp.NerConverter()\
    .setInputCols(["sentence","token","ner_whereas"])\
    .setOutputCol("ner_chunk_whereas")\

chunk_merger = legal.ChunkMergeApproach()\
    .setInputCols('ner_chunk_whereas', "ner_chunk_parties")\
    .setOutputCol('ner_chunk')

pos = nlp.PerceptronModel.pretrained()\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("pos")

dependency_parser = nlp.DependencyParserModel().pretrained("dependency_conllu", "en")\
    .setInputCols(["sentence", "pos", "token"])\
    .setOutputCol("dependencies")

re_filter = legal.RENerChunksFilter()\
    .setInputCols(["ner_chunk", "dependencies"])\
    .setOutputCol("re_ner_chunk")\
    .setMaxSyntacticDistance(10)

reDL = legal.RelationExtractionDLModel().pretrained("legre_contract_doc_parties_md", "en", "legal/models")\
    .setInputCols(["re_ner_chunk", "sentence"])\
    .setOutputCol("relations_parties")\
    .setPredictionThreshold(0.1)

reDL_alias = legal.RelationExtractionDLModel().pretrained("legre_whereas", "en", "legal/models")\
    .setInputCols(["re_ner_chunk", "sentence"])\
    .setOutputCol("relations_whereas")\
    .setPredictionThreshold(0.1)

annotation_merger = legal.AnnotationMerger()\
    .setInputCols("relations_parties", "relations_whereas")\
    .setOutputCol("relations")\
    .setInputType("category")

nlpPipeline = nlp.Pipeline(stages=[
        document_assembler,
        text_splitter,
        tokenizer,
        embeddings,
        ner_model_date,
        ner_converter_date,
        ner_model_org,
        ner_converter_org,
        chunk_merger,
        pos,
        dependency_parser,
        re_filter,
        reDL,
        reDL_alias,
        annotation_merger])


# Show example result
text = """
WHEREAS, the Company Entities own certain Copyrights and Know-How which may be used in the Arizona Field, and in connection with the transactions contemplated by the Stock Purchase Agreement, Arizona desires to obtain a license from the Company Entities to use such Intellectual Property on the terms and subject to the conditions set forth herein.
"""
data = spark.createDataFrame([[text]]).toDF("text")
result = nlpPipeline.fit(data).transform(data)

# Show the results 
result.selectExpr("relations_parties.result as PartiesRelation", 
                  "relations_whereas.result as WhereasRelation", 
                  "relations.result as MergedRelation").show(truncate=False)

+-----------------------------+--------------------------------------+-------------------------------------------------------------------+
|PartiesRelation              |WhereasRelation                       |MergedRelation                                                     |
+-----------------------------+--------------------------------------+-------------------------------------------------------------------+
|[signed_by, other, signed_by]|[has_subject, has_subject, has_object]|[signed_by, other, signed_by, has_subject, has_subject, has_object]|
+-----------------------------+--------------------------------------+-------------------------------------------------------------------+


{%- endcapture -%}

{%- capture model_scala_legal -%}
import spark.implicits._

// Create the pipeline with two RE models
val document_assembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val text_splitter = new TextSplitter()
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val embeddings = RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base", "en")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

val ner_model_date = LegalNerModel.pretrained("legner_contract_doc_parties", "en", "legal/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner_parties")

val ner_converter_date = new NerConverter()
  .setInputCols(Array("sentence", "token", "ner_parties"))
  .setOutputCol("ner_chunk_parties")

val ner_model_org = LegalNerModel.pretrained("legner_whereas_md", "en", "legal/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner_whereas")

val ner_converter_org = new NerConverter()
  .setInputCols(Array("sentence", "token", "ner_whereas"))
  .setOutputCol("ner_chunk_whereas")

val chunk_merger = new Chunker()
  .setInputCols(Array("ner_chunk_whereas", "ner_chunk_parties"))
  .setOutputCol("ner_chunk")

val pos = new PerceptronModel()
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("pos")

val dependency_parser = new DependencyParserModel()
  .pretrained("dependency_conllu", "en")
  .setInputCols(Array("sentence", "pos", "token"))
  .setOutputCol("dependencies")

val re_filter = new RelationExtractionModel()
  .setInputCols(Array("ner_chunk", "dependencies"))
  .setOutputCol("re_ner_chunk")
  .setMaxSyntacticDistance(10)

val reDL = new RelationExtractionModel()
  .pretrained("legre_contract_doc_parties_md", "en", "legal/models")
  .setInputCols(Array("re_ner_chunk", "sentence"))
  .setOutputCol("relations_parties")
  .setPredictionThreshold(0.1)

val reDL_alias = new RelationExtractionModel()
  .pretrained("legre_whereas", "en", "legal/models")
  .setInputCols(Array("re_ner_chunk", "sentence"))
  .setOutputCol("relations_whereas")
  .setPredictionThreshold(0.1)

val annotation_merger = new AnnotationMerger()
  .setInputCols("relations_parties", "relations_whereas")
  .setOutputCol("relations")
  .setInputType("category")

val nlpPipeline = new Pipeline().setStages(Array(
  document_assembler,
  text_splitter,
  tokenizer,
  embeddings,
  ner_model_date,
  ner_converter_date,
  ner_model_org,
  ner_converter_org,
  chunk_merger,
  pos,
  dependency_parser,
  re_filter,
  reDL,
  reDL_alias,
  annotation_merger
))

// Show example result

val text = """WHEREAS, the Company Entities own certain Copyrights and Know-How which may be used in the Arizona Field, and in connection with the transactions contemplated by the Stock Purchase Agreement, Arizona desires to obtain a license from the Company Entities to use such Intellectual Property on the terms and subject to the conditions set forth herein.
"""

val data = Seq(text).toDF("text")
val result = nlpPipeline.fit(data).transform(data)

+-----------------------------+--------------------------------------+-------------------------------------------------------------------+
|PartiesRelation              |WhereasRelation                       |MergedRelation                                                     |
+-----------------------------+--------------------------------------+-------------------------------------------------------------------+
|[signed_by, other, signed_by]|[has_subject, has_subject, has_object]|[signed_by, other, signed_by, has_subject, has_subject, has_object]|
+-----------------------------+--------------------------------------+-------------------------------------------------------------------+

{%- endcapture -%}




{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_api_link=model_api_link
model_python_api_link=model_python_api_link
model_notebook_link=model_notebook_link
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical
model_python_finance=model_python_finance
model_scala_finance=model_scala_finance
model_python_legal=model_python_legal
model_scala_legal=model_scala_legal
%}
