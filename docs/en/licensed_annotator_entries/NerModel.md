{%- capture title -%}
NerModel
{%- endcapture -%}

{%- capture approach -%}
approach
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
`NerModel` is the Named Entity Recognition (NER) annotator that allows to train generic NER model based on Neural Networks. The architecture of the neural network is a Char CNNs - BiLSTM - CRF that achieves state-of-the-art in most datasets.

Note that some pre-trained models require specific types of embeddings, depending on which they were trained.

Parameters:

- `setBatchSize`: (int) number of samples used in one iteration of training (Default: `32`).

- `setIncludeConfidence`: (Boolean) whether to include confidence scores in annotation metadata (`Default`: False). 

- `setConfigProtoBytes`: (int) ConfigProto from tensorflow, serialized into byte array.

- `setIncludeAllConfidenceScores`: (Boolean) whether to include confidence scores for all tags rather than just for the predicted one.

- `setMinProbability` (Float) define the minimum probability value.

For available pretrained models please see the [Models Hub](https://nlp.johnsnowlabs.com/models?task=Named+Entity+Recognition).
Additionally, pretrained pipelines are available for this module, see the [Pipelines](https://nlp.johnsnowlabs.com/docs/en/pipelines).
For extended examples of usage, see the [Spark NLP Workshop](https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master)
{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, TOKEN, WORD_EMBEDDINGS
{%- endcapture -%}

{%- capture model_output_anno -%}
NAMED_ENTITY
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models") \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

jsl_ner = medical.NerModel.pretrained("ner_jsl", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("jsl_ner")

jsl_ner_converter = medical.NerConverterInternal() \
    .setInputCols(["sentence", "token", "jsl_ner"]) \
    .setOutputCol("ner_chunk")

jsl_ner_pipeline = nlp.Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    word_embeddings,
    jsl_ner,
    jsl_ner_converter])

text = '''
A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, and associated with an acute hepatitis, presented with a one-week history of polyuria, poor appetite, and vomiting.
She was on metformin, glipizide, and dapagliflozin for T2DM and atorvastatin and gemfibrozil for HTG. She had been on dapagliflozin for six months at the time of presentation.
Physical examination on presentation was significant for dry oral mucosa ; significantly , her abdominal examination was benign with no tenderness, guarding, or rigidity. Pertinent laboratory findings on admission were: serum glucose 111 mg/dl,  creatinine 0.4 mg/dL, triglycerides 508 mg/dL, total cholesterol 122 mg/dL, and venous pH 7.27.
'''
data = spark.createDataFrame([[text]]).toDF("text")

result = jsl_ner_pipeline.fit(data).transform(data)

result.select(F.explode(F.arrays_zip(result.ner_chunk.result, result.ner_chunk.metadata)).alias("cols"))\
      .select(F.expr("cols['0']").alias("chunk"),
              F.expr("cols['1']['entity']").alias("ner_label")).show(100, truncate=False)

+-----------------------------+----------------------------+
|chunk                        |ner_label                   |
+-----------------------------+----------------------------+
|28-year-old                  |Age                         |
|female                       |Gender                      |
|gestational diabetes mellitus|Diabetes                    |
|eight years prior            |RelativeDate                |
|type two diabetes mellitus   |Diabetes                    |
|T2DM                         |Diabetes                    |
|HTG-induced pancreatitis     |Disease_Syndrome_Disorder   |
|three years prior            |RelativeDate                |
|acute                        |Modifier                    |
|hepatitis                    |Disease_Syndrome_Disorder   |
|one-week                     |Duration                    |
|polyuria                     |Symptom                     |
|poor appetite                |Symptom                     |
|vomiting                     |Symptom                     |
|She                          |Gender                      |
|metformin                    |Drug_Ingredient             |
|glipizide                    |Drug_Ingredient             |
|dapagliflozin                |Drug_Ingredient             |
|T2DM                         |Diabetes                    |
|atorvastatin                 |Drug_Ingredient             |
|gemfibrozil                  |Drug_Ingredient             |
|HTG                          |Hyperlipidemia              |
|She                          |Gender                      |
|dapagliflozin                |Drug_Ingredient             |
|for six months               |Duration                    |
|dry oral mucosa              |Symptom                     |
|her                          |Gender                      |
|abdominal                    |External_body_part_or_region|
|tenderness                   |Symptom                     |
|guarding                     |Symptom                     |
|rigidity                     |Symptom                     |
|admission                    |Admission_Discharge         |
|serum glucose                |Test                        |
|111 mg/dl                    |Test_Result                 |
|creatinine                   |Test                        |
|0.4 mg/dL                    |Test_Result                 |
|triglycerides                |Triglycerides               |
|508 mg/dL                    |Test_Result                 |
|total cholesterol 122 mg/dL  |Total_Cholesterol           |
|venous pH                    |Test                        |
|7.27                         |Test_Result                 |
+-----------------------------+----------------------------+
{%- endcapture -%}

{%- capture model_scala_medical -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = SentenceDetector.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

val jslNer = NerModel.pretrained("ner_jsl", "en", "clinical/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("jsl_ner")

val jslNerConverter = new NerConverter()
  .setInputCols(Array("sentence", "token", "jsl_ner"))
  .setOutputCol("ner_chunk")

val jslNerPipeline = new Pipeline()
  .setStages(Array(documentAssembler, 
                   sentenceDetector, 
                   tokenizer, 
                   wordEmbeddings, 
                   jslNer, 
                   jslNerConverter))

val text = "A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, and associated with an acute hepatitis, presented with a one-week history of polyuria, poor appetite, and vomiting.
She was on metformin, glipizide, and dapagliflozin for T2DM and atorvastatin and gemfibrozil for HTG. She had been on dapagliflozin for six months at the time of presentation.
Physical examination on presentation was significant for dry oral mucosa ; significantly , her abdominal examination was benign with no tenderness, guarding, or rigidity. Pertinent laboratory findings on admission were: serum glucose 111 mg/dl,  creatinine 0.4 mg/dL, triglycerides 508 mg/dL, total cholesterol 122 mg/dL, and venous pH 7.27."

val data = Seq(text).toDF("text")

val result = jslNerPipeline.fit(data).transform(data)

+-----------------------------+----------------------------+
|chunk                        |ner_label                   |
+-----------------------------+----------------------------+
|28-year-old                  |Age                         |
|female                       |Gender                      |
|gestational diabetes mellitus|Diabetes                    |
|eight years prior            |RelativeDate                |
|type two diabetes mellitus   |Diabetes                    |
|T2DM                         |Diabetes                    |
|HTG-induced pancreatitis     |Disease_Syndrome_Disorder   |
|three years prior            |RelativeDate                |
|acute                        |Modifier                    |
|hepatitis                    |Disease_Syndrome_Disorder   |
|one-week                     |Duration                    |
|polyuria                     |Symptom                     |
|poor appetite                |Symptom                     |
|vomiting                     |Symptom                     |
|She                          |Gender                      |
|metformin                    |Drug_Ingredient             |
|glipizide                    |Drug_Ingredient             |
|dapagliflozin                |Drug_Ingredient             |
|T2DM                         |Diabetes                    |
|atorvastatin                 |Drug_Ingredient             |
|gemfibrozil                  |Drug_Ingredient             |
|HTG                          |Hyperlipidemia              |
|She                          |Gender                      |
|dapagliflozin                |Drug_Ingredient             |
|for six months               |Duration                    |
|dry oral mucosa              |Symptom                     |
|her                          |Gender                      |
|abdominal                    |External_body_part_or_region|
|tenderness                   |Symptom                     |
|guarding                     |Symptom                     |
|rigidity                     |Symptom                     |
|admission                    |Admission_Discharge         |
|serum glucose                |Test                        |
|111 mg/dl                    |Test_Result                 |
|creatinine                   |Test                        |
|0.4 mg/dL                    |Test_Result                 |
|triglycerides                |Triglycerides               |
|508 mg/dL                    |Test_Result                 |
|total cholesterol 122 mg/dL  |Total_Cholesterol           |
|venous pH                    |Test                        |
|7.27                         |Test_Result                 |
+-----------------------------+----------------------------+
{%- endcapture -%}

{%- capture model_python_legal -%}
from johnsnowlabs import nlp, legal

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = nlp.RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base", "en") \
    .setInputCols("sentence", "token") \
    .setOutputCol("embeddings")\

ner_model = legal.NerModel.pretrained("legner_contract_doc_parties", "en", "legal/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = nlp.NerConverter()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")

pipeline = nlp.Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter])
  
text = """EXCLUSIVE DISTRIBUTOR AGREEMENT (" Agreement ") dated as April 15, 1994 by and between IMRS OPERATIONS INC., a Delaware corporation with its principal place of business at 777 Long Ridge Road, Stamford, Connecticut 06902, U.S.A. (hereinafter referred to as " Developer ") and Delteq Pte Ltd, a Singapore company (and a subsidiary of Wuthelam Industries (S) Pte LTD ) with its principal place of business at 215 Henderson Road , #101-03 Henderson Industrial Park , Singapore 0315 ( hereinafter referred to as " Distributor ")."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

result.select(F.explode(F.arrays_zip(result.ner_chunk.result, result.ner_chunk.metadata)).alias("cols"))\
      .select(F.expr("cols['0']").alias("chunk"),
              F.expr("cols['1']['entity']").alias("ner_label")).show(100, truncate=False)

+-------------------------------+---------+
|chunk                          |ner_label|
+-------------------------------+---------+
|EXCLUSIVE DISTRIBUTOR AGREEMENT|DOC      |
|April 15, 1994                 |EFFDATE  |
|IMRS OPERATIONS INC            |PARTY    |
|Developer                      |ALIAS    |
|Delteq Pte Ltd                 |PARTY    |
|Distributor                    |ALIAS    |
+-------------------------------+---------+
{%- endcapture -%}

{%- capture model_scala_legal -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val embeddings = RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base", "en")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

val nerModel = NerModel.pretrained("legner_contract_doc_parties", "en", "legal/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner")

val nerConverter = new NerConverter()
  .setInputCols(Array("sentence", "token", "ner"))
  .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  embeddings,
  nerModel,
  nerConverter))

val text = """EXCLUSIVE DISTRIBUTOR AGREEMENT ("Agreement") dated as April 15, 1994 by and between IMRS OPERATIONS INC., a Delaware corporation with its principal place of business at 777 Long Ridge Road, Stamford, Connecticut 06902, U.S.A. (hereinafter referred to as "Developer") and Delteq Pte Ltd, a Singapore company (and a subsidiary of Wuthelam Industries (S) Pte LTD) with its principal place of business at 215 Henderson Road, #101-03 Henderson Industrial Park, Singapore 0315 (hereinafter referred to as "Distributor")."""

val data = Seq(text).toDF("text")

val result = pipeline.fit(data).transform(data)

+-------------------------------+---------+
|chunk                          |ner_label|
+-------------------------------+---------+
|EXCLUSIVE DISTRIBUTOR AGREEMENT|DOC      |
|April 15, 1994                 |EFFDATE  |
|IMRS OPERATIONS INC            |PARTY    |
|Developer                      |ALIAS    |
|Delteq Pte Ltd                 |PARTY    |
|Distributor                    |ALIAS    |
+-------------------------------+---------+
{%- endcapture -%}

{%- capture model_python_finance -%}
from johnsnowlabs import nlp, finance

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")
    
sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_legal_bert_base_uncased","en")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = finance.NerModel.pretrained("finner_sec_conll", "en", "finance/models") \
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = finance.NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")

pipeline = nlp.Pipeline(stages=[
    documentAssembler,
    sentence_detector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter])

text = '''December 2007 SUBORDINATED LOAN AGREEMENT. THIS LOAN AGREEMENT is made on 7th December, 2007 BETWEEN: (1) SILICIUM DE PROVENCE S.A.S., a private company with limited liability, incorporated under the laws of France, whose registered office is situated at Usine de Saint Auban, France, represented by Mr.Frank Wouters, hereinafter referred to as the "Borrower", and ( 2 ) EVERGREEN SOLAR INC., a company incorporated in Delaware, U.S.A., with registered number 2426798, whose registered office is situated at Bartlett Street, Marlboro, Massachusetts, U.S.A. represented by Richard Chleboski, hereinafter referred to as "Lender" '''

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

result.select(F.explode(F.arrays_zip(result.ner_chunk.result, result.ner_chunk.metadata)).alias("cols"))\
      .select(F.expr("cols['0']").alias("chunk"),
              F.expr("cols['1']['entity']").alias("ner_label")).show(100, truncate=False)
+--------------------------+---------+
|chunk                     |ner_label|
+--------------------------+---------+
|SILICIUM DE PROVENCE S.A.S|ORG      |
|France                    |LOC      |
|Usine de Saint Auban      |LOC      |
|France                    |LOC      |
|Mr.Frank Wouters          |PER      |
|Borrower                  |PER      |
|EVERGREEN SOLAR INC       |ORG      |
|Delaware                  |LOC      |
|U.S.A                     |LOC      |
|Bartlett Street           |LOC      |
|Marlboro                  |LOC      |
|Massachusetts             |LOC      |
|U.S.A                     |LOC      |
|Richard Chleboski         |PER      |
|Lender                    |PER      |
+--------------------------+---------+
{%- endcapture -%}

{%- capture model_scala_finance -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val embeddings = BertEmbeddings.pretrained("bert_embeddings_legal_bert_base_uncased", "en")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

val nerModel = NerModel.pretrained("finner_sec_conll", "en", "finance/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner")

val nerConverter = new NerConverterInternal()
  .setInputCols(Array("sentence", "token", "ner"))
  .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  embeddings,
  nerModel,
  nerConverter))

val text = '''December 2007 SUBORDINATED LOAN AGREEMENT. THIS LOAN AGREEMENT is made on 7th December, 2007 BETWEEN: (1) SILICIUM DE PROVENCE S.A.S., a private company with limited liability, incorporated under the laws of France, whose registered office is situated at Usine de Saint Auban, France, represented by Mr.Frank Wouters, hereinafter referred to as the "Borrower", and ( 2 ) EVERGREEN SOLAR INC., a company incorporated in Delaware, U.S.A., with registered number 2426798, whose registered office is situated at Bartlett Street, Marlboro, Massachusetts, U.S.A. represented by Richard Chleboski, hereinafter referred to as "Lender" '''

val data = Seq((text)).toDF("text")

val result = pipeline.fit(data).transform(data)

+--------------------------+---------+
|chunk                     |ner_label|
+--------------------------+---------+
|SILICIUM DE PROVENCE S.A.S|ORG      |
|France                    |LOC      |
|Usine de Saint Auban      |LOC      |
|France                    |LOC      |
|Mr.Frank Wouters          |PER      |
|Borrower                  |PER      |
|EVERGREEN SOLAR INC       |ORG      |
|Delaware                  |LOC      |
|U.S.A                     |LOC      |
|Bartlett Street           |LOC      |
|Marlboro                  |LOC      |
|Massachusetts             |LOC      |
|U.S.A                     |LOC      |
|Richard Chleboski         |PER      |
|Lender                    |PER      |
+--------------------------+---------+
{%- endcapture -%}

{%- capture model_api_link -%}
[MedicalNerModel](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/ner/MedicalNerModel.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[MedicalNerModel](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/ner/medical_ner/index.html#sparknlp_jsl.annotator.ner.medical_ner.MedicalNerModel)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[MedicalNerModelNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/MedicalNerModel.ipynb)
{%- endcapture -%}

{%- capture approach_description -%}
This Named Entity recognition annotator allows to train generic NER model based on Neural Networks.

The architecture of the neural network is a Char CNNs - BiLSTM - CRF that achieves state-of-the-art in most datasets.

For instantiated/pretrained models, see NerDLModel.

The training data should be a labeled Spark Dataset, in the format of [CoNLL](/docs/en/training#conll-dataset)
2003 IOB with `Annotation` type columns. The data should have columns of type `DOCUMENT, TOKEN, WORD_EMBEDDINGS` and an
additional label column of annotator type `NAMED_ENTITY`.
Excluding the label, this can be done with for example
- a [SentenceDetector](/docs/en/annotators#sentencedetector),
- a [Tokenizer](/docs/en/annotators#tokenizer) and
- a [WordEmbeddingsModel](/docs/en/annotators#wordembeddings) with clinical embeddings
  (any [clinical word embeddings](https://nlp.johnsnowlabs.com/models?task=Embeddings) can be chosen).

For extended examples of usage, see the [Spark NLP Workshop](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb)
(sections starting with `Training a Clinical NER`)

{%- endcapture -%}

{%- capture approach_input_anno -%}
DOCUMENT, TOKEN, WORD_EMBEDDINGS
{%- endcapture -%}

{%- capture approach_output_anno -%}
NAMED_ENTITY
{%- endcapture -%}

{%- capture approach_python_medical -%}
from johnsnowlabs import nlp, medical 

# First extract the prerequisites for the NerDLApproach
documentAssembler = nlp.DocumentAssembler() \
.setInputCol("text") \
.setOutputCol("document")

sentence = nlp.SentenceDetector() \
.setInputCols(["document"]) \
.setOutputCol("sentence")

tokenizer = nlp.Tokenizer() \
.setInputCols(["sentence"]) \
.setOutputCol("token")

clinical_embeddings = nlp.WordEmbeddingsModel.pretrained('embeddings_clinical', "en", "clinical/models")\
.setInputCols(["sentence", "token"])\
.setOutputCol("embeddings")

# Then the training can start
nerTagger = medical.NerApproach()\
.setInputCols(["sentence", "token", "embeddings"])\
.setLabelColumn("label")\
.setOutputCol("ner")\
.setMaxEpochs(2)\
.setBatchSize(64)\
.setRandomSeed(0)\
.setVerbose(1)\
.setValidationSplit(0.2)\
.setEvaluationLogExtended(True) \
.setEnableOutputLogs(True)\
.setIncludeConfidence(True)\
.setOutputLogsPath('ner_logs')\
.setGraphFolder('medical_ner_graphs')\
.setEnableMemoryOptimizer(True) #>> if you have a limited memory and a large conll file, you can set this True to train batch by batch

pipeline = nlp.Pipeline().setStages([
documentAssembler,
sentence,
tokenizer,
clinical_embeddings,
nerTagger
])

# We use the text and labels from the CoNLL dataset
conll = CoNLL()
trainingData = conll.readDataset(spark, "src/test/resources/conll2003/eng.train")

pipelineModel = pipeline.fit(trainingData)

{%- endcapture -%}

{%- capture approach_python_legal -%}
from johnsnowlabs import nlp, legal

# First extract the prerequisites for the NerDLApproach
documentAssembler = nlp.DocumentAssembler() \
.setInputCol("text") \
.setOutputCol("document")

sentence = nlp.SentenceDetector() \
.setInputCols(["document"]) \
.setOutputCol("sentence")

tokenizer = nlp.Tokenizer() \
.setInputCols(["sentence"]) \
.setOutputCol("token")

clinical_embeddings = nlp.WordEmbeddingsModel.pretrained('embeddings_clinical', "en", "clinical/models")\
.setInputCols(["sentence", "token"])\
.setOutputCol("embeddings")

# Then the training can start
nerTagger = legal.NerApproach()\
.setInputCols(["sentence", "token", "embeddings"])\
.setLabelColumn("label")\
.setOutputCol("ner")\
.setMaxEpochs(2)\
.setBatchSize(64)\
.setRandomSeed(0)\
.setVerbose(1)\
.setValidationSplit(0.2)\
.setEvaluationLogExtended(True) \
.setEnableOutputLogs(True)\
.setIncludeConfidence(True)\
.setOutputLogsPath('ner_logs')\
.setGraphFolder('medical_ner_graphs')\
.setEnableMemoryOptimizer(True) #>> if you have a limited memory and a large conll file, you can set this True to train batch by batch

pipeline = nlp.Pipeline().setStages([
documentAssembler,
sentence,
tokenizer,
clinical_embeddings,
nerTagger
])
{%- endcapture -%}

{%- capture approach_python_finance -%}
from johnsnowlabs import nlp, finance

# First extract the prerequisites for the NerDLApproach
documentAssembler = nlp.DocumentAssembler() \
.setInputCol("text") \
.setOutputCol("document")

sentence = nlp.SentenceDetector() \
.setInputCols(["document"]) \
.setOutputCol("sentence")

tokenizer = nlp.Tokenizer() \
.setInputCols(["sentence"]) \
.setOutputCol("token")

clinical_embeddings = nlp.WordEmbeddingsModel.pretrained('embeddings_clinical', "en", "clinical/models")\
.setInputCols(["sentence", "token"])\
.setOutputCol("embeddings")

# Then the training can start
nerTagger = finance.NerApproach()\
.setInputCols(["sentence", "token", "embeddings"])\
.setLabelColumn("label")\
.setOutputCol("ner")\
.setMaxEpochs(2)\
.setBatchSize(64)\
.setRandomSeed(0)\
.setVerbose(1)\
.setValidationSplit(0.2)\
.setEvaluationLogExtended(True) \
.setEnableOutputLogs(True)\
.setIncludeConfidence(True)\
.setOutputLogsPath('ner_logs')\
.setGraphFolder('medical_ner_graphs')\
.setEnableMemoryOptimizer(True) #>> if you have a limited memory and a large conll file, you can set this True to train batch by batch

pipeline = nlp.Pipeline().setStages([
documentAssembler,
sentence,
tokenizer,
clinical_embeddings,
nerTagger
])
{%- endcapture -%}



{%- capture approach_scala_medical -%}
import spark.implicits._

// First extract the prerequisites for the NerDLApproach
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentence = new SentenceDetector()
  .setInputCols("document")
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols("sentence")
  .setOutputCol("token")

val embeddings = WordEmbeddingsModel
  .pretrained('embeddings_clinical', "en", "clinical/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

// Then the training can start
val nerTagger =new MedicalNerApproach()
.setInputCols(Array("sentence", "token", "embeddings"))
.setLabelColumn("label")
.setOutputCol("ner")
.setMaxEpochs(5)
.setLr(0.003f)
.setBatchSize(8)
.setRandomSeed(0)
.setVerbose(1)
.setEvaluationLogExtended(false)
.setEnableOutputLogs(false)
.setIncludeConfidence(true)

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentence,
  tokenizer,
  embeddings,
  nerTagger
))

// We use the text and labels from the CoNLL dataset
val conll = CoNLL()
val trainingData = conll.readDataset(spark, "src/test/resources/conll2003/eng.train")

val pipelineModel = pipeline.fit(trainingData)

{%- endcapture -%}


{%- capture approach_scala_legal -%}
import spark.implicits._

// First extract the prerequisites for the NerDLApproach
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentence = new SentenceDetector()
  .setInputCols("document")
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols("sentence")
  .setOutputCol("token")

val embeddings = WordEmbeddingsModel
  .pretrained('embeddings_clinical', "en", "clinical/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

// Then the training can start
val nerTagger =new LegalNerApproach()
.setInputCols(Array("sentence", "token", "embeddings"))
.setLabelColumn("label")
.setOutputCol("ner")
.setMaxEpochs(5)
.setLr(0.003f)
.setBatchSize(8)
.setRandomSeed(0)
.setVerbose(1)
.setEvaluationLogExtended(false)
.setEnableOutputLogs(false)
.setIncludeConfidence(true)

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentence,
  tokenizer,
  embeddings,
  nerTagger
))
{%- endcapture -%}

{%- capture approach_scala_finance -%}
import spark.implicits._

// First extract the prerequisites for the NerDLApproach
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentence = new SentenceDetector()
  .setInputCols("document")
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols("sentence")
  .setOutputCol("token")

val embeddings = WordEmbeddingsModel
  .pretrained('embeddings_clinical', "en", "clinical/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

// Then the training can start
val nerTagger =new FinanceNerApproach()
.setInputCols(Array("sentence", "token", "embeddings"))
.setLabelColumn("label")
.setOutputCol("ner")
.setMaxEpochs(5)
.setLr(0.003f)
.setBatchSize(8)
.setRandomSeed(0)
.setVerbose(1)
.setEvaluationLogExtended(false)
.setEnableOutputLogs(false)
.setIncludeConfidence(true)

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentence,
  tokenizer,
  embeddings,
  nerTagger
))
{%- endcapture -%}


{%- capture approach_api_link -%}
[MedicalNerApproach](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/ner/MedicalNerApproach.html)
{%- endcapture -%}

{%- capture approach_python_api_link -%}
[MedicalNerApproach](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/ner/medical_ner/index.html#sparknlp_jsl.annotator.ner.medical_ner.MedicalNerApproach)
{%- endcapture -%}

{%- capture approach_notebook_link -%}
[MedicalNerApproachNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/MedicalNerApproach.ipynb)
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
