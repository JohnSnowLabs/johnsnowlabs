{%- capture title -%}
GenericSVMClassifier
{%- endcapture -%}

{%- capture approach -%}
approach
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
Creates a generic single-label classifier which uses pre-generated Tensorflow graphs. The model operates on FEATURE_VECTOR annotations which can be produced using FeatureAssembler. Requires the FeaturesAssembler to create the input.

Parameters:

`featureScaling`: Feature scaling method. Possible values are 'zscore', 'minmax' or empty (no scaling) (default:'')

`multiClass`: Whether to return only the label with the highest confidence score or all labels (default: False)

`inputCols`: previous annotations columns, if renamed (default: ['features'])

`outputCol`: output annotation column. can be left default. (default: class)

{%- endcapture -%}

{%- capture model_input_anno -%}
FEATURE_VECTOR
{%- endcapture -%}

{%- capture model_output_anno -%}
CATEGORY
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = nlp.Tokenizer()\
    .setInputCols("document")\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("word_embeddings")

sentence_embeddings = nlp.SentenceEmbeddings() \
    .setInputCols(["document", "word_embeddings"]) \
    .setOutputCol("sentence_embeddings") \
    .setPoolingStrategy("AVERAGE")

features_asm = medical.FeaturesAssembler()\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("features")

generic_classifier = medical.GenericSVMClassifierModel.pretrained("generic_svm_classifier_ade", "en", "clinical/models")\
    .setInputCols(["features"])\
    .setOutputCol("class")

clf_Pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    word_embeddings,
    sentence_embeddings,
    features_asm,
    generic_classifier])

data = spark.createDataFrame([["""None of the patients required treatment for the overdose."""], 
 ["""I feel a bit drowsy & have a little blurred vision after taking an insulin"""]]).toDF("text")

result = clf_Pipeline.fit(data).transform(df)  # sample df

+----------------------------------------------------------------------------------------------------+-------+
|                                                                                                text| result|
+----------------------------------------------------------------------------------------------------+-------+
|                       Multicentric canine lymphoma in a 12-year-old keeshond: chemotherapy options.|[False]|
|                             Pyomyositis is a rare disease, encountered mainly in tropical climates.|[False]|
| Both patients subsequently developed markedly elevated EBV-DNA titers in association with monocl...|[False]|
|Bortezomib-induced paralytic ileus is a potential gastrointestinal side effect of this first-in-c...|[False]|
|However, given the clinically significant result to the interaction between tolazoline and cimeti...| [True]|
|                                              How much do novel antipsychotics benefit the patients?|[False]|
| We hypothesize that during interferon therapy, melanocytes may produce more melanin pigment in t...|[False]|
|They seemed to involve multiple aetiological factors, such as autoimmune thyroid disease, the tox...|[False]|
|               Two days after completing this regimen, the patient developed a rash with blistering.| [True]|
|A diagnosis of masked theophylline poisoning should be considered in similar situations involving...|[False]|
| The overall response rate of these 24 refractory lymphomas to gemcitabine-containing regimens wa...|[False]|
|Development of sarcoidosis during interferon alpha 2b and ribavirin combination therapy for chron...| [True]|
|A patient with coccidioidal meningitis was treated with intrathecally administered amphotericin B...|[False]|
|                                                Renal failure associated with the use of dextran-40.|[False]|
| However, with increased experience in applying BCG, the side effects now appear to be less promi...|[False]|
|                        Hepatotoxicity after high-dose methylprednisolone for demyelinating disease.| [True]|
| Histopathological findings included signs of orthokeratotic hyperkeratosis, moderate follicular ...| [True]|
| Acute spontaneous TLS is rare, and it has been described in leukemia and lymphoma and in some pa...|[False]|
|We present a fatal case of subacute methanol toxicity with associated diffuse brain involvement, ...| [True]|
| The reaction was thought to be triggered by the combination of radiation and epidermal growth fa...|[False]|
+----------------------------------------------------------------------------------------------------+-------+

{%- endcapture -%}


{%- capture model_scala_medical -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("token")

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("document", "token"))
  .setOutputCol("word_embeddings")

val sentenceEmbeddings = new SentenceEmbeddings()
  .setInputCols(Array("document", "word_embeddings"))
  .setOutputCol("sentence_embeddings")
  .setPoolingStrategy("AVERAGE")

val featuresAssembler = new FeaturesAssembler()
  .setInputCols(Array("sentence_embeddings"))
  .setOutputCol("features")

val genericClassifier = PretrainedPipeline("generic_svm_classifier_ade", lang = "en", remoteLoc = "clinical/models")
  .setInputCols("features")
  .setOutputCol("class")

val pipeline = new Pipeline()
  .setStages(Array(
  documentAssembler,
  tokenizer,
  wordEmbeddings,
  sentenceEmbeddings,
  featuresAssembler,
  genericClassifier))

val data = Seq(
  ("""None of the patients required treatment for the overdose."""),
  ("""I feel a bit drowsy & have a little blurred vision after taking an insulin""")
)

val df = data.toDF("text")

val result = pipeline.fit(df).transform(df)


+----------------------------------------------------------------------------------------------------+-------+
|                                                                                                text| result|
+----------------------------------------------------------------------------------------------------+-------+
|                       Multicentric canine lymphoma in a 12-year-old keeshond: chemotherapy options.|[False]|
|                             Pyomyositis is a rare disease, encountered mainly in tropical climates.|[False]|
| Both patients subsequently developed markedly elevated EBV-DNA titers in association with monocl...|[False]|
|Bortezomib-induced paralytic ileus is a potential gastrointestinal side effect of this first-in-c...|[False]|
|However, given the clinically significant result to the interaction between tolazoline and cimeti...| [True]|
|                                              How much do novel antipsychotics benefit the patients?|[False]|
| We hypothesize that during interferon therapy, melanocytes may produce more melanin pigment in t...|[False]|
|They seemed to involve multiple aetiological factors, such as autoimmune thyroid disease, the tox...|[False]|
|               Two days after completing this regimen, the patient developed a rash with blistering.| [True]|
|A diagnosis of masked theophylline poisoning should be considered in similar situations involving...|[False]|
| The overall response rate of these 24 refractory lymphomas to gemcitabine-containing regimens wa...|[False]|
|Development of sarcoidosis during interferon alpha 2b and ribavirin combination therapy for chron...| [True]|
|A patient with coccidioidal meningitis was treated with intrathecally administered amphotericin B...|[False]|
|                                                Renal failure associated with the use of dextran-40.|[False]|
| However, with increased experience in applying BCG, the side effects now appear to be less promi...|[False]|
|                        Hepatotoxicity after high-dose methylprednisolone for demyelinating disease.| [True]|
| Histopathological findings included signs of orthokeratotic hyperkeratosis, moderate follicular ...| [True]|
| Acute spontaneous TLS is rare, and it has been described in leukemia and lymphoma and in some pa...|[False]|
|We present a fatal case of subacute methanol toxicity with associated diffuse brain involvement, ...| [True]|
| The reaction was thought to be triggered by the combination of radiation and epidermal growth fa...|[False]|
+----------------------------------------------------------------------------------------------------+-------+

{%- endcapture -%}

{%- capture model_python_api_link -%}
[GenericSVMClassifier](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/classification/generic_svm_classifier/index.html#sparknlp_jsl.annotator.classification.generic_svm_classifier.GenericSVMClassifierModel)
{%- endcapture -%}

{%- capture model_api_link -%}
[GenericSVMClassifier](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/classification/GenericSVMClassifierModel.html)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[GenericSVMClassifierNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/GenericSVMClassifierModel.ipynb)
{%- endcapture -%}


{%- capture approach_description -%}
`GenericSVMClassifier` is a derivative of GenericClassifier which implements SVM (Support Vector Machine) classification. The input to the model is FeatureVector and the output is category annotations with labels and corresponding confidence scores. The scores are standardized using the logistic function so that they vary between 0 and 1.

Parameters:

- `batchSize`: (int) Batch size

- `dropout`: (float) Dropout coefficient

- `epochsNumber`: (int) Maximum number of epochs to train

- `featureScaling`: (str) Feature scaling method. Possible values are 'zscore', 'minmax' or empty (no scaling)

- `fixImbalance`: (boolean) Fix the imbalance in the training set by replicating examples of under represented categories

- `labelColumn`: (str) Column with label per each document

- `learningRate`: (float) Learning Rate

- `modelFile`: (str) Location of file of the model used for classification

- `multiClass`: (boolean) If multiClass is set, the model will return all the labels with corresponding scores. By default, multiClass is false.

- `outputLogsPath`: (str) Folder path to save training logs. If no path is specified, the logs won't be stored in disk. The path can be a local file path, a distributed file path (HDFS, DBFS), or a cloud storage (S3).

- `validationSplit`: (float) The proportion of training dataset to be used as validation set.The model will be validated against this dataset on each Epoch and will not be used for training. The value should be between 0.0 and 1.0.

{%- endcapture -%}

{%- capture approach_input_anno -%}
FEATURE_VECTOR
{%- endcapture -%}

{%- capture approach_output_anno -%}
CATEGORY
{%- endcapture -%}


{%- capture approach_python_medical -%}

from jojnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_healthcare_100d","en","clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("word_embeddings")

sentence_embeddings = nlp.SentenceEmbeddings() \
    .setInputCols(["document", "word_embeddings"]) \
    .setOutputCol("sentence_embeddings") \
    .setPoolingStrategy("AVERAGE")

embeddings_pipeline = nlp.Pipeline(stages = [
    document_assembler,
    tokenizer,
    word_embeddings,
    sentence_embeddings,
])

trainingData_with_embeddings = embeddings_pipeline.fit(trainingData).transform(trainingData)
trainingData_with_embeddings = trainingData_with_embeddings.select("text","category","sentence_embeddings")

graph_folder = "graph_folder"

gc_svm_graph_builder = medical.TFGraphBuilder()\
    .setModelName("svm_classifier")\
    .setInputCols(["feature_vector"]) \
    .setLabelColumn("category")\
    .setGraphFolder(graph_folder)\
    .setGraphFile("svm_graph.pb")

features_asm = medical.FeaturesAssembler()\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("feature_vector")

gen_clf = medical.GenericSVMClassifierApproach()\
    .setLabelColumn("category")\
    .setInputCols("feature_vector")\
    .setOutputCol("prediction")\
    .setModelFile(f"{graph_folder}/svm_graph.pb")\
    .setEpochsNumber(2)\
    .setBatchSize(128)\
    .setLearningRate(0.015)\
    .setOutputLogsPath(log_folder)\
    .setDropout(0.1)\
    .setFixImbalance(True)\
    # .setValidationSplit(0.1)

clf_Pipeline = nlp.Pipeline(stages=[
    features_asm,
    gc_svm_graph_builder,
    gen_clf])

model = clf_Pipeline.fit(trainingData_with_embeddings)
model.stages[-1].write().overwrite().save('/model_path/model_name')

#sample training data
    text	                                            category
0	Clioquinol intoxication occurring in the trea...	neg
1	"Retinoic acid syndrome" was prevented with s...	neg
2	BACKGROUND: External beam radiation therapy o...	neg
3	Although the enuresis ceased, she developed t...	neg
4	A 42-year-old woman had uneventful bilateral ...	neg

{%- endcapture -%}


{%- capture approach_scala_medical -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")
  
val sentenceEmbeddings = BertSentenceEmbeddings
  .pretrained()
  .setInputCols(Array("document"))
  .setOutputCol("sentence_embedding")

val featuresAssembler = new FeaturesAssembler()
  .setInputCols(Array("sentence_embedding"))
  .setOutputCol("feature_vector")

val svmClassifier = new GenericSVMClassifierApproach()
  .setInputCols("feature_vector")
  .setOutputCol("prediction")
  .setLabelColumn("label")
  .setModelFile("src/test/resources/classification/svm_graph.pb") 
  .setEpochsNumber(10)
  .setBatchSize(1)
  .setMultiClass(false)
  .setlearningRate(0.01f)

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceEmbeddings,
  featuresAssembler,
  svmClassifier,
))

val model = pipeline.fit(trainingData)

{%- endcapture -%}


{%- capture approach_python_api_link -%}
[GenericSVMClassifier](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/classification/generic_svm_classifier/index.html#sparknlp_jsl.annotator.classification.generic_svm_classifier.GenericSVMClassifierApproach)
{%- endcapture -%}

{%- capture approach_api_link -%}
[GenericSVMClassifier](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/classification/GenericSVMClassifierApproach.html)
{%- endcapture -%}

{%- capture approach_notebook_link -%}
[GenericSVMClassifierNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/GenericSVMClassifierApproach.ipynb)
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
model_api_link=model_api_link
model_python_api_link=model_python_api_link
model_notebook_link=model_notebook_link
approach_description=approach_description
approach_input_anno=approach_input_anno
approach_output_anno=approach_output_anno
approach_python_medical=approach_python_medical
approach_scala_medical=approach_scala_medical
approach_api_link=approach_api_link
approach_python_api_link=approach_python_api_link
approach_notebook_link=approach_notebook_link
%}
