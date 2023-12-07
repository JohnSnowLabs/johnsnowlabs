{%- capture title -%}
Router
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
`Router` provides the ability to split an output of an annotator for a selected metadata field and the value for that field. 

When we need to use multiple sentence entity resolver models in the same pipeline, we typically had to run the `BertSentenceEmbeddings` annotator multiple times based on the number of resolver models. This meant that the heavy process of generating sentence embeddings using BERT was repeated multiple times.

To address this issue, Spark NLP Healthcare Library has introduced a solution using the `Router` annotator. With this new approach, we can provide all the named entity recognition (NER) chunks to the `BertSentenceEmbeddings` annotator at once. The annotator generates the sentence embeddings for all the chunks together. Then, the output of the sentence embeddings is routed to the specific resolver models that are required for further processing.

This solution eliminates the need to run `BertSentenceEmbeddings` multiple times, reducing the computational overhead and improving the efficiency of the pipeline.

Parametres:

- `inputCols`: The name of the columns containing the input annotations. It can read an Array of strings.
- `outputCol`: The name of the column in the Document type that is generated. We can specify only one column here.
- `inputType`: The type of entity that you want to filter (by default `sentence_embeddings`). Possible values; `document|token|wordpiece|word_embeddings|sentence_embeddings|category|date|sentiment|pos|chunk|named_entity|regex|dependency|labeled_dependency|language|keyword`
- `metadataField`: The key in the metadata dictionary that you want to filter (by default `entity`)
- `filterFieldsElements`: The `filterfieldsElements` are the allowed values for the metadata field that is being used.

All the parameters can be set using the corresponding set method in the camel case. For example, `.setInputcols()`. 

{%- endcapture -%}

{%- capture model_input_anno -%}
ENTITY, LABEL_DEPENDENCY
{%- endcapture -%}

{%- capture model_output_anno -%}
ENTITY
{%- endcapture -%}

{%- capture model_python_medical -%}

from johnsnowlabs import nlp, medical

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
    .setInputCols("document")\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols("sentence")\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols("sentence", "token")\
    .setOutputCol("word_embeddings")

# to get PROBLEM entitis
clinical_ner = medical.NerModel().pretrained("ner_clinical", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "word_embeddings"]) \
    .setOutputCol("clinical_ner")

clinical_ner_chunk = medical.NerConverterInternal()\
    .setInputCols("sentence","token","clinical_ner")\
    .setOutputCol("clinical_ner_chunk")\
    .setWhiteList(["PROBLEM"])

# to get DRUG entities
posology_ner = medical.NerModel().pretrained("ner_posology", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "word_embeddings"]) \
    .setOutputCol("posology_ner")

posology_ner_chunk = medical.NerConverterInternal()\
    .setInputCols("sentence","token","posology_ner")\
    .setOutputCol("posology_ner_chunk")\
    .setWhiteList(["DRUG"])

# merge the chunks into a single ner_chunk
chunk_merger = medical.ChunkMergeApproach()\
    .setInputCols("clinical_ner_chunk","posology_ner_chunk")\
    .setOutputCol("final_ner_chunk")\
    .setMergeOverlapping(False)

# convert chunks to doc to get sentence embeddings of them
chunk2doc = nlp.Chunk2Doc().setInputCols("final_ner_chunk").setOutputCol("doc_final_chunk")

sbiobert_embeddings = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
    .setInputCols(["doc_final_chunk"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

# filter PROBLEM entity embeddings
router_sentence_icd10 = medical.Router() \
    .setInputCols("sbert_embeddings") \
    .setFilterFieldsElements(["PROBLEM"]) \
    .setOutputCol("problem_embeddings")

# filter DRUG entity embeddings
router_sentence_rxnorm = medical.Router() \
    .setInputCols("sbert_embeddings") \
    .setFilterFieldsElements(["DRUG"]) \
    .setOutputCol("drug_embeddings")

# use problem_embeddings only
icd_resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_slim_billable_hcc","en", "clinical/models") \
    .setInputCols(["problem_embeddings"]) \
    .setOutputCol("icd10cm_code")\
    .setDistanceFunction("EUCLIDEAN")

# use drug_embeddings only
rxnorm_resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_rxnorm_augmented","en", "clinical/models") \
    .setInputCols(["drug_embeddings"]) \
    .setOutputCol("rxnorm_code")\
    .setDistanceFunction("EUCLIDEAN")


pipeline = nlp.Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    word_embeddings,
    clinical_ner,
    clinical_ner_chunk,
    posology_ner,
    posology_ner_chunk,
    chunk_merger,
    chunk2doc,
    sbiobert_embeddings,
    router_sentence_icd10,
    router_sentence_rxnorm,
    icd_resolver,
    rxnorm_resolver
])

clinical_note = """The patient is a 41-year-old Vietnamese female with a cough that started last week.
She has had right-sided chest pain radiating to her back with fever starting yesterday.
She has a history of pericarditis in May 2006 and developed cough with right-sided chest pain.
MEDICATIONS
1. Coumadin 1 mg daily. Last INR was on Tuesday, August 14, 2007, and her INR was 2.3.
2. Amiodarone 100 mg p.o. daily.
"""

data = spark.createDataFrame([[clinical_note]]).toDF("text")

result = pipeline.fit(data).transform(data)

## Result

result.selectExpr(
    "final_ner_chunk.result as chunk",
    "posology_ner_chunk.result as posology_chunk",
    "rxnorm_code.result as rxnorm_code",
    "clinical_ner_chunk.result as clinical_chunk",
    "icd10cm_code.result as icd10cm_code",
).show(truncate=False)

+-----------------------------------------------------------------------------------------------------------+----------------------+-------------+-------------------------------------------------------------------------------------+--------------------------------------+
|chunk                                                                                                      |posology_chunk        |rxnorm_code  |clinical_chunk                                                                       |icd10cm_code                          |
+-----------------------------------------------------------------------------------------------------------+----------------------+-------------+-------------------------------------------------------------------------------------+--------------------------------------+
|[a cough, right-sided chest pain, fever, pericarditis, cough, right-sided chest pain, Coumadin, Amiodarone]|[Coumadin, Amiodarone]|[202421, 703]|[a cough, right-sided chest pain, fever, pericarditis, cough, right-sided chest pain]|[R05, R10.11, A68, I30.1, R05, R10.11]|
+-----------------------------------------------------------------------------------------------------------+----------------------+-------------+-------------------------------------------------------------------------------------+--------------------------------------+


{%- endcapture -%}


{%- capture model_scala_medical -%}

import spark.implicits._

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence","token"))
    .setOutputCol("word_embeddings")
    
// to get PROBLEM entitis 
val clinical_ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence","token","word_embeddings"))
    .setOutputCol("clinical_ner")

val clinical_ner_chunk = new NerConverterInternal()
    .setInputCols("sentence","token","clinical_ner")
    .setOutputCol("clinical_ner_chunk")
    .setWhiteList("PROBLEM")

// to get DRUG entities 
val posology_ner = MedicalNerModel.pretrained("ner_posology", "en", "clinical/models")
    .setInputCols(Array("sentence","token","word_embeddings"))
    .setOutputCol("posology_ner")

val posology_ner_chunk = new NerConverterInternal()
    .setInputCols("sentence","token","posology_ner")
    .setOutputCol("posology_ner_chunk")
    .setWhiteList("DRUG")

// merge the chunks into a single ner_chunk 
val chunk_merger = new ChunkMergeApproach()
    .setInputCols(Array("clinical_ner_chunk","posology_ner_chunk"))
    .setOutputCol("final_ner_chunk")
    .setMergeOverlapping(false)

// convert chunks to doc to get sentence embeddings of them 
val chunk2doc = new Chunk2Doc()
    .setInputCols("final_ner_chunk")
    .setOutputCol("doc_final_chunk")

val sbiobert_embeddings = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
    .setInputCols("doc_final_chunk")
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(false)

// filter PROBLEM entity embeddings 
val router_sentence_icd10 = new Router()
    .setInputCols("sbert_embeddings")
    .setFilterFieldsElements("PROBLEM")
    .setOutputCol("problem_embeddings")
    
// filter DRUG entity embeddings 
val router_sentence_rxnorm = new Router()
    .setInputCols("sbert_embeddings")
    .setFilterFieldsElements("DRUG")
    .setOutputCol("drug_embeddings")
    
// use problem_embeddings only 
val icd_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_slim_billable_hcc", "en", "clinical/models")
    .setInputCols("problem_embeddings")
    .setOutputCol("icd10cm_code")
    .setDistanceFunction("EUCLIDEAN")
    
// use drug_embeddings only 
val rxnorm_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_rxnorm_augmented", "en", "clinical/models")
    .setInputCols("drug_embeddings")
    .setOutputCol("rxnorm_code")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, 
    sentenceDetector, 
    tokenizer, 
    word_embeddings, 
    clinical_ner, 
    clinical_ner_chunk, 
    posology_ner, 
    posology_ner_chunk, 
    chunk_merger, 
    chunk2doc, 
    sbiobert_embeddings, 
    router_sentence_icd10, 
    router_sentence_rxnorm, 
    icd_resolver, 
    rxnorm_resolver))


val data = Seq("""The patient is a 41-year-old Vietnamese female with a cough that started last week.
She has had right-sided chest pain radiating to her back with fever starting yesterday.
She has a history of pericarditis in May 2006 and developed cough with right-sided chest pain.
MEDICATIONS
1. Coumadin 1 mg daily. Last INR was on Tuesday, August 14, 2007, and her INR was 2.3.
2. Amiodarone 100 mg p.o. daily.""").toDF("text")

val res = mapperPipeline.fit(data).transform(data)

// Show results

+-----------------------------------------------------------------------------------------------------------+----------------------+-------------+-------------------------------------------------------------------------------------+--------------------------------------+
|chunk                                                                                                      |posology_chunk        |rxnorm_code  |clinical_chunk                                                                       |icd10cm_code                          |
+-----------------------------------------------------------------------------------------------------------+----------------------+-------------+-------------------------------------------------------------------------------------+--------------------------------------+
|[a cough, right-sided chest pain, fever, pericarditis, cough, right-sided chest pain, Coumadin, Amiodarone]|[Coumadin, Amiodarone]|[202421, 703]|[a cough, right-sided chest pain, fever, pericarditis, cough, right-sided chest pain]|[R05, R10.11, A68, I30.1, R05, R10.11]|
+-----------------------------------------------------------------------------------------------------------+----------------------+-------------+-------------------------------------------------------------------------------------+--------------------------------------+

{%- endcapture -%}

{%- capture model_api_link -%}
[Router](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/annotator/Router.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[Router](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/router/index.html#module-sparknlp_jsl.annotator.router)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[RouterNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/Router.ipynb)
{%- endcapture -%}


{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical
model_api_link=model_api_link
model_python_api_link=model_python_api_link
model_notebook_link=model_notebook_link
%}
