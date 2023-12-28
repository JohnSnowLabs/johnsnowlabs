{%- capture title -%}
SentenceEntityResolver
{%- endcapture -%}

{%- capture approach -%}
approach
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
The model transforms a dataset with Input Annotation type SENTENCE_EMBEDDINGS, coming from e.g.
[BertSentenceEmbeddings](/docs/en/transformers#bertsentenceembeddings)
and returns the normalized entity for a particular trained ontology / curated dataset (e.g. ICD-10, RxNorm, SNOMED etc.).

Parametres:

- `distanceFunction`: Determines how the distance between different entities will be calculated. Either `COSINE` or `EUCLIDEAN`.

- `neighbours`: The number of neighbours to consider when computing the distances.

- `caseSensitive`: WWhether to consider text casing or not.

- `threshold`: Threshold of the distance between nodes to consider.

All the parameters can be set using the corresponding set method in camel case. For example, `.setInputcols()`.

For a list of pretrained models, please see the
[Models Hub](https://nlp.johnsnowlabs.com/models?task=Entity+Resolution).
{%- endcapture -%}

{%- capture model_input_anno -%}
SENTENCE_EMBEDDINGS
{%- endcapture -%}

{%- capture model_output_anno -%}
ENTITY
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical 

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetectorDLModel.pretrained()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_ner = medical.NerModel.pretrained("jsl_ner_wip_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = nlp.NerConverter()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Test","Procedure"])

c2doc = nlp.Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings\
    .pretrained("sbiobert_base_cased_mli","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")

# Then the resolver is defined on the extracted entities and sentence embeddings
cpt_resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_cpt_procedures_augmented","en", "clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("cpt_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline().setStages([
    documentAssembler,
    sentenceDetector,
    tokenizer,
    word_embeddings,
    clinical_ner,
    ner_converter,
    c2doc,
    sbert_embedder,
    cpt_resolver])

text = """She was admitted to the hospital with chest pain and found to have bilateral pleural effusion, the right greater than the left. CT scan of the chest also revealed a large mediastinal lymph node.
We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma.
At this time, chest tube placement for drainage of the fluid occurred and thoracoscopy, which were performed, which revealed epithelioid malignant mesothelioma."""

df = spark.createDataFrame([[text]]).toDF("text")
result = pipeline.fit(df).transform(df)

# Show Results
+--------------------+---------+-----+----------+--------------------+--------------------+
|               chunk|   entity| code|confidence|       all_k_results|   all_k_resolutions|
+--------------------+---------+-----+----------+--------------------+--------------------+
|CT scan of the chest|     Test|62284|    0.2028|62284:::76497:::7...|Computed tomograp...|
|      pericardectomy|Procedure|33031|    0.3329|33031:::33025:::3...|Pericardectomy [P...|
|chest tube placement|Procedure|39503|    0.9343|39503:::32036:::3...|Insertion of ches...|
|drainage of the f...|Procedure|49405|    0.2476|49405:::49407:::4...|Drainage procedur...|
|        thoracoscopy|Procedure|32660|    0.1422|32660:::32667:::1...|Thoracoscopy [Tho...|
+--------------------+---------+-----+----------+--------------------+--------------------+

{%- endcapture -%}

{%- capture model_scala_medical -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text") 
  .setOutputCol("document") 

val sentenceDetector = SentenceDetectorDLModel.pretrained()
  .setInputCols(Array("document")) 
  .setOutputCol("sentence") 

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence")) 
  .setOutputCol("token") 

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
  .setInputCols(Array("sentence","token")) 
  .setOutputCol("embeddings") 

val clinical_ner = MedicalNerModel.pretrained("jsl_ner_wip_clinical","en","clinical/models")
  .setInputCols(Array("sentence","token","embeddings")) 
  .setOutputCol("ner") 

val ner_converter = new NerConverter()
  .setInputCols(Array("sentence","token","ner")) 
  .setOutputCol("ner_chunk") 
  .setWhiteList(Array("Test","Procedure")) 

val c2doc = new Chunk2Doc()
  .setInputCols(Array("ner_chunk")) 
  .setOutputCol("ner_chunk_doc") 

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models") 
  .setInputCols(Array("ner_chunk_doc"))
  .setOutputCol("sbert_embeddings") 

// Then the resolver is defined on the extracted entities and sentence embeddings 

val cpt_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_cpt_procedures_augmented","en","clinical/models")
  .setInputCols(Array("sbert_embeddings")) 
  .setOutputCol("cpt_code") 
  .setDistanceFunction("EUCLIDEAN") 

val pipeline = new Pipeline().setStages(Array( 
                                              documentAssembler, 
                                              sentenceDetector, 
                                              tokenizer,
                                              word_embeddings, 
                                              clinical_ner, 
                                              ner_converter, 
                                              c2doc, 
                                              sbert_embedder, 
                                              cpt_resolver)) 


val text = "She was admitted to the hospital with chest pain and found to have bilateral pleural effusion,the right greater than the left. CT scan of the chest also revealed a large mediastinal lymph node. We reviewed the pathology obtained from the pericardectomy in March 2006,which was diagnostic of mesothelioma. At this time,chest tube placement for drainage of the fluid occurred and thoracoscopy,which were performed,which revealed epithelioid malignant mesothelioma." 

val df = Seq(text) .toDF("text") 
val result = pipeline.fit(df) .transform(df) 
{%- endcapture -%}



{%- capture model_python_legal -%}
from johnsnowlabs import nlp, legal 

documentAssembler = nlp.DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("ner_chunk")

embeddings = nlp.UniversalSentenceEncoder.pretrained("tfhub_use", "en")\
      .setInputCols("ner_chunk")\
      .setOutputCol("sentence_embeddings")
    
resolver = legal.SentenceEntityResolverModel.pretrained("legel_edgar_company_name", "en", "legal/models")\
      .setInputCols(["ner_chunk", "sentence_embeddings"])\
      .setOutputCol("irs_code")\
      .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(
      stages = [
          documentAssembler,
          embeddings,
          resolver])

text = """CONTACT GOLD"""

df = spark.createDataFrame([[text]]).toDF("text")
result = pipeline.fit(df).transform(df)

# Show Results
+------------+------------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|chunk       |result            |code                                                                                         |all_k_results                                                                                                                                                                                                                                  |all_k_resolutions                                                                                                                                                                                                                              |
+------------+------------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|CONTACT GOLD|Contact Gold Corp.|981369960:::0:::208273426:::204092640:::0:::0:::270531073:::261918920:::0:::271989147:::0:::0|Contact Gold Corp.:::ISHARES GOLD TRUST:::Minatura Gold:::Mexus Gold US:::BESRA GOLD INC.:::ALAMOS GOLD INC:::JOSHUA GOLD RESOURCES INC:::MIDEX GOLD CORP.:::Gold Mark Stephen:::Guskin Gold Corp.:::CMX GOLD & SILVER CORP.:::Permal Gold Ltd.|Contact Gold Corp.:::ISHARES GOLD TRUST:::Minatura Gold:::Mexus Gold US:::BESRA GOLD INC.:::ALAMOS GOLD INC:::JOSHUA GOLD RESOURCES INC:::MIDEX GOLD CORP.:::Gold Mark Stephen:::Guskin Gold Corp.:::CMX GOLD & SILVER CORP.:::Permal Gold Ltd.|
+------------+------------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}

{%- capture model_scala_legal -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text") 
  .setOutputCol("ner_chunk") 

val embeddings = UniversalSentenceEncoder.pretrained("tfhub_use","en")
  .setInputCols("ner_chunk") 
  .setOutputCol("sentence_embeddings") 

val resolver = SentenceEntityResolverModel.pretrained("legel_edgar_company_name","en","legal/models")
  .setInputCols(Array("ner_chunk","sentence_embeddings")) 
  .setOutputCol("irs_code") .setDistanceFunction("EUCLIDEAN") 

val pipeline = new Pipeline().setStages(Array(
                                            documentAssembler, 
                                            embeddings, 
                                            resolver)) 

val text = "CONTACT GOLD" 

val df = Seq(text) .toDF("text") 
val result = pipeline.fit(df) .transform(df)

{%- endcapture -%}


{%- capture model_python_finance -%}
from johnsnowlabs import nlp, finance 

documentAssembler = nlp.DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("ner_chunk")

embeddings = nlp.UniversalSentenceEncoder.pretrained("tfhub_use", "en") \
      .setInputCols("ner_chunk") \
      .setOutputCol("sentence_embeddings")

resolver = finance.SentenceEntityResolverModel.pretrained("finel_edgar_company_name", "en", "finance/models")\
      .setInputCols(["ner_chunk", "sentence_embeddings"]) \
      .setOutputCol("normalized")\
      .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(
      stages = [
          documentAssembler,
          embeddings,
          resolver])

text = """CONTACT GOLD"""

df = spark.createDataFrame([[text]]).toDF("text")
result = pipeline.fit(df).transform(df)

# Show Results
+------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|chunk       |result            |all_k_results                                                                                                                                                                                                                                  |all_k_resolutions                                                                                                                                                                                                                              |
+------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|CONTACT GOLD|Contact Gold Corp.|Contact Gold Corp.:::ISHARES GOLD TRUST:::Minatura Gold:::Mexus Gold US:::BESRA GOLD INC.:::ALAMOS GOLD INC:::JOSHUA GOLD RESOURCES INC:::MIDEX GOLD CORP.:::Gold Mark Stephen:::Guskin Gold Corp.:::CMX GOLD & SILVER CORP.:::Permal Gold Ltd.|Contact Gold Corp.:::ISHARES GOLD TRUST:::Minatura Gold:::Mexus Gold US:::BESRA GOLD INC.:::ALAMOS GOLD INC:::JOSHUA GOLD RESOURCES INC:::MIDEX GOLD CORP.:::Gold Mark Stephen:::Guskin Gold Corp.:::CMX GOLD & SILVER CORP.:::Permal Gold Ltd.|
+------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


{%- endcapture -%}

{%- capture model_scala_finance -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text") 
  .setOutputCol("ner_chunk") 

val embeddings = UniversalSentenceEncoder.pretrained("tfhub_use","en")
  .setInputCols("ner_chunk") 
  .setOutputCol("sentence_embeddings") 

val resolver = SentenceEntityResolverModel.pretrained("finel_edgar_company_name","en","finance/models")
  .setInputCols(Array("ner_chunk","sentence_embeddings")) 
  .setOutputCol("normalized") 
  .setDistanceFunction("EUCLIDEAN") 

val pipeline = new Pipeline().setStages(Array(
                                            documentAssembler, 
                                            embeddings, 
                                            resolver)) 

val text = "CONTACT GOLD" 
val df = Seq(text) .toDF("text") 
val result = pipeline.fit(df) .transform(df) 
{%- endcapture -%}


{%- capture model_api_link -%}
[SentenceEntityResolverModel](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/resolution/SentenceEntityResolverModel.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[SentenceEntityResolverModel](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/resolution/sentence_entity_resolver/index.html#sparknlp_jsl.annotator.resolution.sentence_entity_resolver.SentenceEntityResolverModel)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[SentenceEntityResolverModelNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/SentenceEntityResolverApproach_SentenceEntityResolverModel.ipynb)
{%- endcapture -%}

{%- capture approach_description -%}
Trains a SentenceEntityResolverModel that maps sentence embeddings to entities in a knowledge base.

General parameters:

- `labelCol` : Column name for the value we are trying to resolve. Usually this contains the entity ID in the knowledge base (e.g., the ICD-10 code).

- `normalizedCol`: Column name for the original, normalized description

- `aux_label_col`: Auxiliary label which maps resolved entities to additional labels

- `useAuxLabel`: Whether to use the auxiliary column or not. Default value is False.

- `distanceFunction`: Determines how the distance between different entities will be calculated.

- `confidenceFunction`: What function to use to calculate confidence: Either ` `INVERSE` or `SOFTMAX`.

- `caseSensitive`: whether to ignore case in tokens for embeddings matching (Default: `False`)

- `threshold`: Threshold value for the last distance calculated (default: 5.0)

- `missAsEmpty`: whether or not to return an empty annotation on unmatched chunks (default: `True`)


When finetuning an existing model, there are additional parameters:

- `pretrainedModelPath`: Path to an already trained SentenceEntityResolverModel.This pretrained model will be used as a starting point for training the new one. The path can be a local file path, a distributed file path (HDFS, DBFS), or a cloud storage (S3).

- `overrideExistingCodes`: Whether to override the existing codes with new data while continue the training from a pretrained model. Default value is `False` (keep all the codes).

- `dropCodesList`: A list of codes in a pretrained model that will be omitted when the training process begins with a pretrained model.

You can find pretrained Sentence Embeddings (using BERT or other architecgture) in the
`NLP Models Hub <https://nlp.johnsnowlabs.com/models?task=Embeddings>`_.
{%- endcapture -%}

{%- capture approach_input_anno -%}
SENTENCE_EMBEDDINGS
{%- endcapture -%}

{%- capture approach_output_anno -%}
ENTITY
{%- endcapture -%}

{%- capture approach_python_medical -%}
from johnsnowlabs import nlp, medical 

# Training a SNOMED resolution model using BERT sentence embeddings
# Define pre-processing pipeline for training data. It needs consists of columns for the normalized training data and their labels.
documentAssembler = nlp.DocumentAssembler() \
  .setInputCol("normalized_text") \
  .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

bertEmbeddings = nlp.BertSentenceEmbeddings.pretrained("sent_biobert_pubmed_base_cased") \
  .setInputCols(["sentence"]) \
  .setOutputCol("bert_embeddings")

snomedTrainingPipeline = nlp.Pipeline(stages=[
  documentAssembler,
  sentenceDetector,
  bertEmbeddings
])
snomedTrainingModel = snomedTrainingPipeline.fit(data)
snomedData = snomedTrainingModel.transform(data).cache()

# Then the Resolver can be trained with
bertExtractor = medical.SentenceEntityResolverApproach() \
  .setNeighbours(25) \
  .setThreshold(1000) \
  .setInputCols(["bert_embeddings"]) \
  .setNormalizedCol("normalized_text") \
  .setLabelCol("label") \
  .setOutputCol("snomed_code") \
  .setDistanceFunction("EUCLIDIAN") \
  .setCaseSensitive(False)

snomedModel = bertExtractor.fit(snomedData)

{%- endcapture -%}

{%- capture approach_python_legal -%}
from johnsnowlabs import nlp, legal

# Define pre-processing pipeline for training data. It needs consists of columns for the normalized training data and their labels.
documentAssembler = nlp.DocumentAssembler() \
  .setInputCol("normalized_text") \
  .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

bertEmbeddings = nlp.BertSentenceEmbeddings.pretrained("sent_bert_base_uncased_legal") \
  .setInputCols(["sentence"]) \
  .setOutputCol("bert_embeddings")

preprocessing_pipeline = nlp.Pipeline(stages=[
  documentAssembler,
  sentenceDetector,
  bertEmbeddings
])
data_preprocessing_model = preprocessing_pipeline.fit(data)
processed_data = data_preprocessing_model.transform(data).cache()

# Then the Resolver can be trained with
bertExtractor = legal.SentenceEntityResolverApproach() \
  .setNeighbours(25) \
  .setThreshold(1000) \
  .setInputCols(["bert_embeddings"]) \
  .setNormalizedCol("normalized_text") \
  .setLabelCol("label") \
  .setOutputCol("snomed_code") \
  .setDistanceFunction("EUCLIDIAN") \
  .setCaseSensitive(False)

model = bertExtractor.fit(processed_data)

{%- endcapture -%}

{%- capture approach_python_finance -%}
from johnsnowlabs import nlp, finance

# Define pre-processing pipeline for training data. It needs consists of columns for the normalized training data and their labels.
documentAssembler = nlp.DocumentAssembler() \
  .setInputCol("normalized_text") \
  .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

bertEmbeddings = nlp.BertSentenceEmbeddings.pretrained("sent_bert_large_cased") \
  .setInputCols(["sentence"]) \
  .setOutputCol("bert_embeddings")

preprocessing_pipeline = nlp.Pipeline(stages=[
  documentAssembler,
  sentenceDetector,
  bertEmbeddings
])
preprocessing_model = preprocessing_pipeline.fit(data)
processed_data = preprocessing_model.transform(data).cache()

# Then the Resolver can be trained with
bertExtractor = finance.SentenceEntityResolverApproach() \
  .setNeighbours(25) \
  .setThreshold(1000) \
  .setInputCols(["bert_embeddings"]) \
  .setNormalizedCol("normalized_text") \
  .setLabelCol("label") \
  .setOutputCol("snomed_code") \
  .setDistanceFunction("EUCLIDIAN") \
  .setCaseSensitive(False)

model = bertExtractor.fit(processed_data)

{%- endcapture -%}

{%- capture approach_scala_medical -%}
import spark.implicits._

// Training a SNOMED resolution model using BERT sentence embeddings
// Define pre-processing pipeline for training data. It needs consists of columns for the normalized training data and their labels.
val documentAssembler = new DocumentAssembler()
   .setInputCol("normalized_text")
   .setOutputCol("document")

val sentenceDetector = SentenceDetector()
  .setInputCols("document")
  .setOutputCol("sentence")

 val bertEmbeddings = BertSentenceEmbeddings.pretrained("sent_biobert_pubmed_base_cased")
   .setInputCols("sentence")
   .setOutputCol("bert_embeddings")

 val snomedTrainingPipeline = new Pipeline().setStages(Array(
   documentAssembler,
   sentenceDetector,
   bertEmbeddings
 ))

 val snomedTrainingModel = snomedTrainingPipeline.fit(data)
 val snomedData = snomedTrainingModel.transform(data).cache()

// Then the Resolver can be trained with
val bertExtractor = new SentenceEntityResolverApproach()
  .setNeighbours(25)
  .setThreshold(1000)
  .setInputCols("bert_embeddings")
  .setNormalizedCol("normalized_text")
  .setLabelCol("label")
  .setOutputCol("snomed_code")
  .setDistanceFunction("EUCLIDIAN")
  .setCaseSensitive(false)

val snomedModel = bertExtractor.fit(snomedData)

{%- endcapture -%}

{%- capture approach_scala_legal -%}
import spark.implicits._

// Training a SNOMED resolution model using BERT sentence embeddings
// Define pre-processing pipeline for training data. It needs consists of columns for the normalized training data and their labels.
val documentAssembler = new DocumentAssembler()
   .setInputCol("normalized_text")
   .setOutputCol("document")

val sentenceDetector = SentenceDetector()
  .setInputCols("document")
  .setOutputCol("sentence")

 val bertEmbeddings = BertSentenceEmbeddings.pretrained("sent_biobert_pubmed_base_cased")
   .setInputCols("sentence")
   .setOutputCol("bert_embeddings")

 val snomedTrainingPipeline = new Pipeline().setStages(Array(
   documentAssembler,
   sentenceDetector,
   bertEmbeddings
 ))
 val snomedTrainingModel = snomedTrainingPipeline.fit(data)
 val snomedData = snomedTrainingModel.transform(data).cache()

// Then the Resolver can be trained with
val bertExtractor = new SentenceEntityResolverApproach()
  .setNeighbours(25)
  .setThreshold(1000)
  .setInputCols("bert_embeddings")
  .setNormalizedCol("normalized_text")
  .setLabelCol("label")
  .setOutputCol("snomed_code")
  .setDistanceFunction("EUCLIDIAN")
  .setCaseSensitive(false)

val snomedModel = bertExtractor.fit(snomedData)

{%- endcapture -%}

{%- capture approach_scala_finance -%}
import spark.implicits._

// Training a SNOMED resolution model using BERT sentence embeddings
// Define pre-processing pipeline for training data. It needs consists of columns for the normalized training data and their labels.
val documentAssembler = new DocumentAssembler()
   .setInputCol("normalized_text")
   .setOutputCol("document")

val sentenceDetector = SentenceDetector()
  .setInputCols("document")
  .setOutputCol("sentence")

 val bertEmbeddings = BertSentenceEmbeddings.pretrained("sent_biobert_pubmed_base_cased")
   .setInputCols("sentence")
   .setOutputCol("bert_embeddings")
   
 val snomedTrainingPipeline = new Pipeline().setStages(Array(
   documentAssembler,
   sentenceDetector,
   bertEmbeddings
 ))
 val snomedTrainingModel = snomedTrainingPipeline.fit(data)
 val snomedData = snomedTrainingModel.transform(data).cache()

// Then the Resolver can be trained with
val bertExtractor = new SentenceEntityResolverApproach()
  .setNeighbours(25)
  .setThreshold(1000)
  .setInputCols("bert_embeddings")
  .setNormalizedCol("normalized_text")
  .setLabelCol("label")
  .setOutputCol("snomed_code")
  .setDistanceFunction("EUCLIDIAN")
  .setCaseSensitive(false)

val snomedModel = bertExtractor.fit(snomedData)

{%- endcapture -%}

{%- capture approach_api_link -%}
[SentenceEntityResolverApproach](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/resolution/SentenceEntityResolverApproach.html)
{%- endcapture -%}

{%- capture approach_python_api_link -%}
[SentenceEntityResolverApproach](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/resolution/sentence_entity_resolver/index.html#sparknlp_jsl.annotator.resolution.sentence_entity_resolver.SentenceEntityResolverApproach)
{%- endcapture -%}

{%- capture approach_notebook_link -%}
[SentenceEntityResolverApproachNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/SentenceEntityResolverApproach_SentenceEntityResolverModel.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
approach=approach
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical
model_python_legal=model_python_legal
model_scala_legal=model_scala_legal
model_python_finance=model_python_finance
model_scala_finance=model_scala_finance
model_api_link=model_api_link
model_python_api_link=model_python_api_link
model_notebook_link=model_notebook_link
approach_description=approach_description
approach_input_anno=approach_input_anno
approach_output_anno=approach_output_anno
approach_python_medical=approach_python_medical
approach_python_legal=approach_python_legal
approach_python_finance=approach_python_finance
approach_scala_medical=approach_scala_medical
approach_scala_legal=approach_scala_legal
approach_scala_finance=approach_scala_finance
approach_api_link=approach_api_link
approach_python_api_link=approach_python_api_link
approach_notebook_link=approach_notebook_link
%}
