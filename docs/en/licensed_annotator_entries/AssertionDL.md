{%- capture title -%}
AssertionDL
{%- endcapture -%}

{%- capture approach -%}
approach
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
AssertionDL is a deep Learning based approach used to extract Assertion Status
from extracted entities and text. AssertionDLModel requires DOCUMENT, CHUNK and WORD_EMBEDDINGS type
annotator inputs, which can be obtained by e.g a
[DocumentAssembler](/docs/en/annotators#documentassembler),
[NerConverter](/docs/en/annotators#nerconverter)
and [WordEmbeddingsModel](/docs/en/annotators#wordembeddings).
The result is an assertion status annotation for each recognized entity.
Possible values include `“present”,“absent”,“hypothetical”,“conditional”,“associated_with_other_person”` etc.

Parameters:
- `inputCols`: Gets current column names of input annotations.

- `outputCol`: Gets output column name of annotations.

- `ScopeWindow`: Sets the scope of the window of the assertion expression.

- `EntityAssertionCaseSensitive`: Sets the case sensitivity of entities and assertion labels.

- `DoExceptionHandling`: If it is set as True, the annotator tries to process as usual and ff exception-causing data (e.g. corrupted record/ document) is passed to the annotator, an exception warning is emitted which has the exception message.

For pretrained models please see the
[Models Hub](https://nlp.johnsnowlabs.com/models?task=Assertion+Status) for available models.
{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, CHUNK, WORD_EMBEDDINGS
{%- endcapture -%}

{%- capture model_output_anno -%}
ASSERTION
{%- endcapture -%}

{%- capture model_python_medical -%}

from johnsnowlabs import nlp, medical
# Define pipeline stages to extract NER chunks first
documentAssembler = nlp.DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
  .setInputCols(["sentence"])\
  .setOutputCol("token")

embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models") \
  .setInputCols(["sentence", "token"])\
  .setOutputCol("embeddings")

nerModel = medical.NerModel.pretrained("ner_clinical", "en", "clinical/models") \
  .setInputCols(["sentence", "token", "embeddings"])\
  .setOutputCol("ner")

nerConverter = nlp.NerConverter()\
  .setInputCols(["sentence", "token", "ner"])\
  .setOutputCol("ner_chunk")

# Then a pretrained AssertionDLModel is used to extract the assertion status
clinicalAssertion = medical.AssertionDLModel.pretrained("assertion_dl", "en", "clinical/models") \
  .setInputCols(["sentence", "ner_chunk", "embeddings"]) \
  .setOutputCol("assertion")

assertionPipeline = nlp.Pipeline(stages=[
  documentAssembler,
  sentenceDetector,
  tokenizer,
  embeddings,
  nerModel,
  nerConverter,
  clinicalAssertion
])

data = spark.createDataFrame([
  ["Patient with severe fever and sore throat"],
  ["Patient shows no stomach pain"],
  ["She was maintained on an epidural and PCA for pain control."]]).toDF("text")


# Show results
result = assertionPipeline.fit(data).transform(data)
result.selectExpr("ner_chunk.result as chunk_result", "assertion.result as assertion_result").show(3, truncate=False)

+--------------------------------+--------------------------------+
|chunk_result                    |assertion_result                |
+--------------------------------+--------------------------------+
|[severe fever, sore throat]     |[present, present]              |
|[stomach pain]                  |[absent]                        |
|[an epidural, PCA, pain control]|[present, present, hypothetical]|
+--------------------------------+--------------------------------+

{%- endcapture -%}

{%- capture model_python_finance -%}
from johnsnowlabs import nlp, finance

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector =  nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer =  nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings =  nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

ner_model = finance.NerModel.pretrained("finner_orgs_prods_alias","en","finance/models")\
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")\

ner_converter = finance.NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")\

assertion = finance.AssertionDLModel.pretrained("finassertion_competitors", "en", "finance/models")\
    .setInputCols(["sentence", "ner_chunk", "embeddings"]) \
    .setOutputCol("assertion")
    
pipeline = nlp.Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter,
    assertion
    ])

data = spark.createDataFrame([["Our competitors include the following by general category: legacy antivirus product providers, such as McAfee LLC and Broadcom Inc."]]).toDF("text")


# Show results
result = pipeline.fit(data).transform(data)
result.select(F.explode(F.arrays_zip(result.ner_chunk.result, result.ner_chunk.metadata, result.assertion.result)).alias("cols"))\
      .select(F.expr("cols['1']['sentence']").alias("sent_id"),
              F.expr("cols['0']").alias("chunk"),
              F.expr("cols['1']['entity']").alias("ner_label"),
              F.expr("cols['2']").alias("assertion")).show(truncate=False)

+-------+------------+---------+----------+
|sent_id|chunk       |ner_label|assertion |
+-------+------------+---------+----------+
|0      |McAfee LLC  |ORG      |COMPETITOR|
|0      |Broadcom Inc|ORG      |COMPETITOR|
+-------+------------+---------+----------+
{%- endcapture -%}

{%- capture model_python_legal -%}
from johnsnowlabs import nlp, legal

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings_ner = nlp.RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base", "en") \
    .setInputCols("sentence", "token") \
    .setOutputCol("embeddings_ner")\

ner_model = legal.NerModel.pretrained('legner_contract_doc_parties', 'en', 'legal/models')\
    .setInputCols(["sentence", "token", "embeddings_ner"])\
    .setOutputCol("ner")

ner_converter = nlp.NerConverter()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DOC", "EFFDATE", "PARTY"])

embeddings_ass = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings_ass")

assertion = legal.AssertionDLModel.pretrained("legassertion_time", "en", "legal/models")\
    .setInputCols(["sentence", "ner_chunk", "embeddings_ass"]) \
    .setOutputCol("assertion")

nlpPipeline = nlp.Pipeline(stages=[
            document_assembler, 
            sentence_detector,
            tokenizer,
            embeddings_ner,
            ner_model,
            ner_converter,
            embeddings_ass,
            assertion
            ])

data = spark.createDataFrame([["This is an Intellectual Property Agreement between Amazon Inc. and Atlantic Inc."]]).toDF("text")


# Show results
result = nlpPipeline.fit(data).transform(data)
result.select(F.explode(F.arrays_zip(result.ner_chunk.result,  
                                     result.ner_chunk.begin, 
                                     result.ner_chunk.end, 
                                     result.ner_chunk.metadata, 
                                     result.assertion.result)).alias("cols"))\
      .select(F.expr("cols['0']").alias("chunk"),
              F.expr("cols['1']").alias("begin"),
              F.expr("cols['2']").alias("end"),
              F.expr("cols['3']['entity']").alias("ner_label"),
              F.expr("cols['4']").alias("assertion")).show(truncate=False)

+-------------------------------+-----+---+---------+---------+
|chunk                          |begin|end|ner_label|assertion|
+-------------------------------+-----+---+---------+---------+
|Intellectual Property Agreement|11   |41 |DOC      |PRESENT  |
|Amazon Inc                     |51   |60 |PARTY    |PRESENT  |
|Atlantic Inc                   |67   |78 |PARTY    |PRESENT  |
+-------------------------------+-----+---+---------+---------+

{%- endcapture -%}

{%- capture model_scala_medical -%}

import spark.implicits._
// Define pipeline stages to extract NER chunks first

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val nerModel = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val nerConverter = new NerConverter()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

// Then a pretrained AssertionDLModel is used to extract the assertion status
val clinicalAssertion = AssertionDLModel.pretrained("assertion_dl", "en", "clinical/models")
    .setInputCols(Array("sentence", "ner_chunk", "embeddings"))
    .setOutputCol("assertion")

val assertionPipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  embeddings,
  nerModel,
  nerConverter,
  clinicalAssertion
))

val data = Seq(
  "Patient with severe fever and sore throat",
  "Patient shows no stomach pain",
  "She was maintained on an epidural and PCA for pain control.").toDF("text")
  

// Show results
val result = assertionPipeline.fit(data).transform(data)

+--------------------------------+--------------------------------+
|chunk_result                    |assertion_result                |
+--------------------------------+--------------------------------+
|[severe fever, sore throat]     |[present, present]              |
|[stomach pain]                  |[absent]                        |
|[an epidural, PCA, pain control]|[present, present, hypothetical]|
+--------------------------------+--------------------------------+

{%- endcapture -%}

{%- capture model_scala_finance -%}
import spark.implicits._

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector =  new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer =  new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val embeddings =  BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = FinanceNerModel.pretrained("finner_orgs_prods_alias","en","finance/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverter()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val assertion = AssertionDLModel.pretrained("finassertion_competitors", "en", "finance/models")
    .setInputCols(Array("sentence", "ner_chunk", "embeddings"))
    .setOutputCol("assertion")
    
val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter,
    assertion
    ))

val data = Seq("Our competitors include the following by general category: legacy antivirus product providers, such as McAfee LLC and Broadcom Inc.").toDF("text")


// Show results
val result = pipeline.fit(data).transform(data)

+-------+------------+---------+----------+
|sent_id|chunk       |ner_label|assertion |
+-------+------------+---------+----------+
|0      |McAfee LLC  |ORG      |COMPETITOR|
|0      |Broadcom Inc|ORG      |COMPETITOR|
+-------+------------+---------+----------+

{%- endcapture -%}


{%- capture model_scala_legal -%}
import spark.implicits._

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val embeddings_ner = RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base", "en")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings_ner")

val ner_model = LegalNerModel.pretrained('legner_contract_doc_parties', 'en', 'legal/models')
    .setInputCols(Array("sentence", "token", "embeddings_ner"))
    .setOutputCol("ner")

val ner_converter = new NerConverter()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("DOC", "EFFDATE", "PARTY"))

val embeddings_ass = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings_ass")

val assertion = AssertionDLModel.pretrained("legassertion_time", "en", "legal/models")
    .setInputCols(Array("sentence", "ner_chunk", "embeddings_ass"))
    .setOutputCol("assertion")
    
val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector,
    tokenizer,
    embeddings_ner,
    ner_model,
    ner_converter,
    embeddings_ass,
    assertion
    ))

val data = Seq("This is an Intellectual Property Agreement between Amazon Inc. and Atlantic Inc.").toDF("text")


// Show results
val result = pipeline.fit(data).transform(data)

+-------------------------------+-----+---+---------+---------+
|chunk                          |begin|end|ner_label|assertion|
+-------------------------------+-----+---+---------+---------+
|Intellectual Property Agreement|11   |41 |DOC      |PRESENT  |
|Amazon Inc                     |51   |60 |PARTY    |PRESENT  |
|Atlantic Inc                   |67   |78 |PARTY    |PRESENT  |
+-------------------------------+-----+---+---------+---------+

{%- endcapture -%}




{%- capture model_api_link -%}
[AssertionDLModel](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/assertion/dl/AssertionDLModel.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[AssertionDLModel](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/assertion/assertionDL/index.html#sparknlp_jsl.annotator.assertion.assertionDL.AssertionDLModel)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[AssertionDLModelNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/AssertionDLModel.ipynb)
{%- endcapture -%}

{%- capture approach_description -%}
Trains AssertionDL, a deep Learning based approach used to extract Assertion Status
from extracted entities and text.
Contains all the methods for training an AssertionDLModel.
For pretrained models please use AssertionDLModel and see the
[Models Hub](https://nlp.johnsnowlabs.com/models?task=Assertion+Status) for available models.

Parameters:

- `inputCols`: Gets current column names of input annotations.

- `outputCol`: Gets output column name of annotations.

- `ScopeWindow`: Sets the scope of the window of the assertion expression.

- `StartCol`: Set a column that contains the token number for the start of the target.

{%- endcapture -%}

{%- capture approach_input_anno -%}
DOCUMENT, CHUNK, WORD_EMBEDDINGS
{%- endcapture -%}

{%- capture approach_output_anno -%}
ASSERTION
{%- endcapture -%}

{%- capture approach_python_medical -%}
from johnsnowlabs import nlp, medical

# First, pipeline stages for pre-processing the dataset (containing columns for text and label) are defined.
document = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

chunk = nlp.Doc2Chunk() \
    .setInputCols(["document"]) \
    .setOutputCol("chunk") \
    .setChunkCol("target")\
    .setStartCol("start")\
    .setStartColByTokenIndex(True)\
    .setFailOnMissing(False)\
    .setLowerCase(True)

token = nlp.Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("embeddings")

# Define AssertionDLApproach with parameters and start training
assertionStatus = medical.AssertionDLApproach() \
    .setLabelCol("label") \
    .setInputCols(["document", "chunk", "embeddings"]) \
    .setOutputCol("assertion") \
    .setBatchSize(128) \
    .setDropout(0.012) \
    .setLearningRate(0.015) \
    .setEpochs(1) \
    .setStartCol("start") \
    .setEndCol("end") \
    .setMaxSentLen(250)

trainingPipeline = nlp.Pipeline().setStages([
    document,
    chunk,
    token,
    embeddings,
    assertionStatus
])

assertionResults = trainingPipeline.fit(data).transform(data).cache()
{%- endcapture -%}

{%- capture approach_python_legal -%}
from johnsnowlabs import nlp, legal

# First, pipeline stages for pre-processing the dataset (containing columns for text and label) are defined.
document = nlp.DocumentAssembler()\
    .setInputCol("sentence")\
    .setOutputCol("document")

chunk = nlp.Doc2Chunk()\
    .setInputCols("document")\
    .setOutputCol("doc_chunk")

token = nlp.Tokenizer()\
    .setInputCols(['document'])\
    .setOutputCol('token')

roberta_embeddings = nlp.RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base","en") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("embeddings") \
    .setMaxSentenceLength(512)

# Define AssertionDLApproach with parameters and start training
assertionStatus = legal.AssertionDLApproach()\
    .setLabelCol("assertion_label")\
    .setInputCols(["document", "doc_chunk", "embeddings"])\
    .setOutputCol("assertion")\
    .setBatchSize(128)\
    .setLearningRate(0.001)\
    .setEpochs(2)\
    .setStartCol("tkn_start")\
    .setEndCol("tkn_end")\
    .setMaxSentLen(1200)\
    .setEnableOutputLogs(True)\
    .setOutputLogsPath('training_logs/')\
    .setGraphFolder(graph_folder)\
    .setGraphFile(f"{graph_folder}/assertion_graph.pb")\
    .setTestDataset(path="test_data.parquet", read_as='SPARK', options={'format': 'parquet'})\
    .setScopeWindow(scope_window)
    #.setValidationSplit(0.2)\    
    #.setDropout(0.1)\    

trainingPipeline = nlp.Pipeline().setStages([
    document,
    chunk,
    token,
    roberta_embeddings,
    assertionStatus
])

assertionResults = trainingPipeline.fit(data).transform(data).cache()
{%- endcapture -%}

{%- capture approach_python_finance -%}
from johnsnowlabs import nlp, finance

# First, pipeline stages for pre-processing the dataset (containing columns for text and label) are defined.
document = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

chunk = nlp.Doc2Chunk() \
    .setInputCols(["document"]) \
    .setOutputCol("chunk")

token = nlp.Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("embeddings")

# Define AssertionDLApproach with parameters and start training
assertionStatus = finance.AssertionDLApproach() \
    .setLabelCol("label") \
    .setInputCols(["document", "chunk", "embeddings"]) \
    .setOutputCol("assertion") \
    .setBatchSize(128) \
    .setDropout(0.012) \
    .setLearningRate(0.015) \
    .setEpochs(1) \
    .setStartCol("start") \
    .setEndCol("end") \
    .setMaxSentLen(250)

trainingPipeline = nlp.Pipeline().setStages([
    document,
    chunk,
    token,
    embeddings,
    assertionStatus
])

assertionResults = trainingPipeline.fit(data).transform(data).cache()
{%- endcapture -%}

{%- capture approach_scala_medical -%}
import spark.implicits._

// First, pipeline stages for pre-processing the dataset (containing columns for text and label) are defined.
val document = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val chunk = new Doc2Chunk()
  .setInputCols(Array("document"))
  .setOutputCol("chunk")

val token = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("token")

val embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("document", "token"))
  .setOutputCol("embeddings")

// Define AssertionDLApproach with parameters and start training
val assertionStatus = new AssertionDLApproach()
  .setLabelCol("label")
  .setInputCols(Array("document", "chunk", "embeddings"))
  .setOutputCol("assertion")
  .setBatchSize(128)
  .setDropout(0.012)
  .setLearningRate(0.015)
  .setEpochs(1)
  .setStartCol("start")
  .setEndCol("end")
  .setMaxSentLen(250)

val trainingPipeline = new Pipeline().setStages(Array(
  document,
  chunk,
  token,
  embeddings,
  assertionStatus
))

val assertionResults = trainingPipeline.fit(data).transform(data).cache()
{%- endcapture -%}

{%- capture approach_scala_legal -%}
import spark.implicits._

val document = new DocumentAssembler()
    .setInputCol("sentence")
    .setOutputCol("document")

val chunk = new Doc2Chunk()
    .setInputCols(Array("document"))
    .setOutputCol("doc_chunk")
    .setChunkCol("chunk")
    .setStartCol("tkn_start")
    .setStartColByTokenIndex(true)
    .setFailOnMissing(false)
    .setLowerCase(false)

val token = new Tokenizer()
    .setInputCols(Array('document'))
    .setOutputCol('token')

val roberta_embeddings = RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base","en") 
    .setInputCols(Array("document", "token")) 
    .setOutputCol("embeddings") 
    .setMaxSentenceLength(512)

# Define AssertionDLApproach with parameters and start training
val assertionStatus = new AssertionDLApproach()
    .setLabelCol("assertion_label")
    .setInputCols(Array("document", "doc_chunk", "embeddings"))
    .setOutputCol("assertion")
    .setBatchSize(128)
    .setLearningRate(0.001)
    .setEpochs(2)
    .setStartCol("tkn_start")
    .setEndCol("tkn_end")
    .setMaxSentLen(1200)
    .setEnableOutputLogs(true)
    .setOutputLogsPath('training_logs/')
    .setGraphFolder(graph_folder)
    .setGraphFile(f"{graph_folder}/assertion_graph.pb")
    .setTestDataset(path="test_data.parquet", read_as='SPARK', options={'format': 'parquet'})
    .setScopeWindow(scope_window)
    #.setValidationSplit(0.2) 
    #.setDropout(0.1) 

val trainingPipeline = new Pipeline().setStages(Array(
  document,
  chunk,
  token,
  roberta_embeddings,
  assertionStatus
))

val assertionResults = trainingPipeline.fit(data).transform(data).cache()
{%- endcapture -%}

{%- capture approach_scala_finance -%}
import spark.implicits._
// First, pipeline stages for pre-processing the dataset (containing columns for text and label) are defined.

val document = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val chunk = new Doc2Chunk()
  .setInputCols(Array("document"))
  .setOutputCol("chunk")

val token = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("token")

val embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("document", "token"))
  .setOutputCol("embeddings")

// Define AssertionDLApproach with parameters and start training
val assertionStatus = new AssertionDLApproach()
  .setLabelCol("label")
  .setInputCols(Array("document", "chunk", "embeddings"))
  .setOutputCol("assertion")
  .setBatchSize(128)
  .setDropout(0.012)
  .setLearningRate(0.015)
  .setEpochs(1)
  .setStartCol("start")
  .setEndCol("end")
  .setMaxSentLen(250)

val trainingPipeline = new Pipeline().setStages(Array(
  document,
  chunk,
  token,
  embeddings,
  assertionStatus
))

val assertionResults = trainingPipeline.fit(data).transform(data).cache()
{%- endcapture -%}


{%- capture approach_api_link -%}
[AssertionDLApproach](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/assertion/dl/AssertionDLApproach.html)
{%- endcapture -%}

{%- capture approach_python_api_link -%}
[AssertionDLApproach](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/assertion/assertionDL/index.html#sparknlp_jsl.annotator.assertion.assertionDL.AssertionDLApproach)
{%- endcapture -%}

{%- capture approach_notebook_link -%}
[AssertionDLApproachNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/AssertionDLApproach.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
approach=approach
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_python_finance=model_python_finance
model_python_legal=model_python_legal
model_scala_medical=model_scala_medical
model_scala_finance=model_scala_finance
model_scala_legal=model_scala_legal
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
