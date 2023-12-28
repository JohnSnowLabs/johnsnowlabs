{%- capture title -%}
GenericClassifier
{%- endcapture -%}

{%- capture approach -%}
approach
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
Creates a generic single-label classifier which uses pre-generated Tensorflow graphs.
The model operates on FEATURE_VECTOR annotations which can be produced using FeatureAssembler.
Requires the FeaturesAssembler to create the input.

Parametres:

- `multiClass` *(Boolean)*: Whether to return all clases or only the one with highest score (Default: False)

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

sentence_embeddings = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", 'en','clinical/models')\
    .setInputCols(["document"])\
    .setOutputCol("sentence_embeddings")

features_asm = medical.FeaturesAssembler()\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("features")

generic_classifier = medical.GenericClassifierModel.pretrained("genericclassifier_sdoh_economics_binary_sbiobert_cased_mli", 'en', 'clinical/models')\
    .setInputCols(["features"])\
    .setOutputCol("classes")

pipeline = nlp.Pipeline(
    stages=[
        document_assembler,
        sentence_embeddings,
        features_asm,
        generic_classifier
])

text = """Patient works as a building inspector and remodeler. Married with 2 children. He is a current smoker, 1PPD for 25years. He drinks to beers/night, but has not had any alcohol in past 4 days. No IVDU."""

df = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(df).transform(df)
result.select("text", "classes.result").show(truncate=False)

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------+
|text                                                                                                                                                                                                  |result|
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------+
|Patient works as a building inspector and remodeler. Married with 2 children. He is a current smoker, 1PPD for 25years. He drinks to beers/night, but has not had any alcohol in past 4 days. No IVDU.|[True]|
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------+
{%- endcapture -%}

{%- capture model_scala_medical -%}

import spark.implicits._

val document_assembler = new DocumentAssembler()
  .setInputCol("text") 
  .setOutputCol("document")

val sentence_embeddings = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
  .setInputCols("document") 
  .setOutputCol("sentence_embeddings") 

val features_asm = new FeaturesAssembler()
  .setInputCols("sentence_embeddings")
  .setOutputCol("features") 

val generic_classifier = GenericClassifierModel.pretrained("genericclassifier_sdoh_economics_binary_sbiobert_cased_mli","en","clinical/models")
  .setInputCols(Array("features")) 
  .setOutputCol("classes") 

val pipeline = new Pipeline().setStages(Array( 
                                            document_assembler, 
                                            sentence_embeddings, 
                                            features_asm, 
                                            generic_classifier )) 

val text = "Patient works as a building inspector and remodeler. Married with 2 children. He is a current smoker,1PPD for 25years. He drinks to beers/night,but has not had any alcohol in past 4 days. No IVDU." 

val df = Seq(text) .toDF("text") 
val result = pipeline.fit(df) .transform(df) result.select("text","classes.result") .show(truncate=false)   

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------+
|text                                                                                                                                                                                                  |result|
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------+
|Patient works as a building inspector and remodeler. Married with 2 children. He is a current smoker, 1PPD for 25years. He drinks to beers/night, but has not had any alcohol in past 4 days. No IVDU.|[True]|
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------+

{%- endcapture -%}

{%- capture model_api_link -%}
[GenericClassifierModel](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/generic_classifier/GenericClassifierModel.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[GenericClassifierModel](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/generic_classifier/generic_classifier/index.html#sparknlp_jsl.annotator.generic_classifier.generic_classifier.GenericClassifierModel)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[GenericClassifierModelNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/GenericClassifierModel.ipynb)
{%- endcapture -%}

{%- capture approach_description -%}
Trains a TensorFlow model for generic classification of feature vectors. It takes FEATURE_VECTOR annotations from
`FeaturesAssembler` as input, classifies them and outputs CATEGORY annotations.
Please see the Parameters section for required training parameters.

Parametres:

- `batchSize`: (int) Batch size

- `dropout`: (float) Dropout coefficient

- `epochsN`: (int) Maximum number of epochs to train

- `featureScaling`: (str) Feature scaling method. Possible values are 'zscore', 'minmax' or empty (no scaling)

- `fixImbalance`: (boolean) Fix the imbalance in the training set by replicating examples of under represented categories

- `labelColumn`: (str) Column with label per each document

- `learningRate`: (float) Learning Rate

- `modelFile`: (str) Location of file of the model used for classification

- `multiClass`: (boolean) If multiClass is set, the model will return all the labels with corresponding scores. By default, multiClass is false.

- `outputLogsPath`: (str) Folder path to save training logs. If no path is specified, the logs won't be stored in disk. The path can be a local file path, a distributed file path (HDFS, DBFS), or a cloud storage (S3).

- `validationSplit`: (float) The proportion of training dataset to be used as validation set.The model will be validated against this dataset on each Epoch and will not be used for training. The value should be between 0.0 and 1.0.

For a more extensive example please see the
[Spark NLP Workshop](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/8.Generic_Classifier.ipynb).
{%- endcapture -%}

{%- capture approach_input_anno -%}
FEATURE_VECTOR
{%- endcapture -%}

{%- capture approach_output_anno -%}
CATEGORY
{%- endcapture -%}

{%- capture approach_python_medical -%}
from johnsnowlabs import nlp, medical

features_asm = medical.FeaturesAssembler() \
    .setInputCols(["feature_1", "feature_2", "...", "feature_n"]) \
    .setOutputCol("features")

gen_clf = medical.GenericClassifierApproach() \
    .setLabelColumn("target") \
    .setInputCols(["features"]) \
    .setOutputCol("prediction") \
    .setModelFile("/path/to/graph_file.pb") \
    .setEpochsNumber(50) \
    .setBatchSize(100) \
    .setFeatureScaling("zscore") \
    .setlearningRate(0.001) \
    .setFixImbalance(True) \
    .setOutputLogsPath("logs") \
    .setValidationSplit(0.2) # keep 20% of the data for validation purposes

pipeline = nlp.Pipeline().setStages([
    features_asm,
    gen_clf
])

clf_model = pipeline.fit(data)

{%- endcapture -%}

{%- capture approach_python_legal -%}
from johnsnowlabs import nlp, legal

features_asm = legal.FeaturesAssembler() \
    .setInputCols(["feature_1", "feature_2", "...", "feature_n"]) \
    .setOutputCol("features")

gen_clf = legal.GenericClassifierApproach() \
    .setLabelColumn("target") \
    .setInputCols(["features"]) \
    .setOutputCol("prediction") \
    .setModelFile("/path/to/graph_file.pb") \
    .setEpochsNumber(50) \
    .setBatchSize(100) \
    .setFeatureScaling("zscore") \
    .setlearningRate(0.001) \
    .setFixImbalance(True) \
    .setOutputLogsPath("logs") \
    .setValidationSplit(0.2) # keep 20% of the data for validation purposes

pipeline = nlp.Pipeline().setStages([
    features_asm,
    gen_clf
])

clf_model = pipeline.fit(data)

{%- endcapture -%}


{%- capture approach_python_finance -%}
from johnsnowlabs import nlp, finance

features_asm = finance.FeaturesAssembler() \
    .setInputCols(["feature_1", "feature_2", "...", "feature_n"]) \
    .setOutputCol("features")

gen_clf = finance.GenericClassifierApproach() \
    .setLabelColumn("target") \
    .setInputCols(["features"]) \
    .setOutputCol("prediction") \
    .setModelFile("/path/to/graph_file.pb") \
    .setEpochsNumber(50) \
    .setBatchSize(100) \
    .setFeatureScaling("zscore") \
    .setlearningRate(0.001) \
    .setFixImbalance(True) \
    .setOutputLogsPath("logs") \
    .setValidationSplit(0.2) # keep 20% of the data for validation purposes

pipeline = nlp.Pipeline().setStages([
    features_asm,
    gen_clf
])

clf_model = pipeline.fit(data)

{%- endcapture -%}

{%- capture approach_scala_medical -%}
import spark.implicits._

val features_asm = new FeaturesAssembler()
  .setInputCols(Array("feature_1", "feature_2", "...", "feature_n"))
  .setOutputCol("features")

val gen_clf = new GenericClassifierApproach()
  .setLabelColumn("target")
  .setInputCols("features")
  .setOutputCol("prediction")
  .setModelFile("/path/to/graph_file.pb")
  .setEpochsNumber(50)
  .setBatchSize(100)
  .setFeatureScaling("zscore")
  .setlearningRate(0.001f)
  .setFixImbalance(true)
  .setOutputLogsPath("logs")
  .setValidationSplit(0.2f) // keep 20% of the data for validation purposes

val pipeline = new Pipeline().setStages(Array(
  features_asm,
  gen_clf
))

val clf_model = pipeline.fit(data)

{%- endcapture -%}


{%- capture approach_scala_legal -%}
import spark.implicits._

val features_asm = new FeaturesAssembler()
  .setInputCols(Array("feature_1", "feature_2", "...", "feature_n"))
  .setOutputCol("features")

val gen_clf = new GenericClassifierApproach()
  .setLabelColumn("target")
  .setInputCols("features")
  .setOutputCol("prediction")
  .setModelFile("/path/to/graph_file.pb")
  .setEpochsNumber(50)
  .setBatchSize(100)
  .setFeatureScaling("zscore")
  .setlearningRate(0.001f)
  .setFixImbalance(true)
  .setOutputLogsPath("logs")
  .setValidationSplit(0.2f) // keep 20% of the data for validation purposes

val pipeline = new Pipeline().setStages(Array(
  features_asm,
  gen_clf
))

val clf_model = pipeline.fit(data)

{%- endcapture -%}


{%- capture approach_scala_finance -%}
import spark.implicits._

val features_asm = new FeaturesAssembler()
  .setInputCols(Array("feature_1", "feature_2", "...", "feature_n"))
  .setOutputCol("features")

val gen_clf = new GenericClassifierApproach()
  .setLabelColumn("target")
  .setInputCols("features")
  .setOutputCol("prediction")
  .setModelFile("/path/to/graph_file.pb")
  .setEpochsNumber(50)
  .setBatchSize(100)
  .setFeatureScaling("zscore")
  .setlearningRate(0.001f)
  .setFixImbalance(true)
  .setOutputLogsPath("logs")
  .setValidationSplit(0.2f) // keep 20% of the data for validation purposes

val pipeline = new Pipeline().setStages(Array(
  features_asm,
  gen_clf
))

val clf_model = pipeline.fit(data)

{%- endcapture -%}

{%- capture approach_api_link -%}
[GenericClassifierApproach](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/generic_classifier/GenericClassifierApproach.html)
{%- endcapture -%}

{%- capture approach_python_api_link -%}
[GenericClassifierApproach](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/generic_classifier/generic_classifier/index.html#sparknlp_jsl.annotator.generic_classifier.generic_classifier.GenericClassifierApproach)
{%- endcapture -%}

{%- capture approach_notebook_link -%}
[GenericClassifierApproachNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/GenericClassifierApproach.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
approach=approach
model=model
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
approach_python_legal=approach_python_legal
approach_python_finance=approach_python_finance
approach_scala_medical=approach_scala_medical
approach_scala_legal=approach_scala_legal
approach_scala_finance=approach_scala_finance
approach_api_link=approach_api_link
approach_python_api_link=approach_python_api_link
approach_notebook_link=approach_notebook_link
%}
