{%- capture title -%}
DocumentMLClassifier
{%- endcapture -%}

{%- capture approach -%}
approach
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
`DocumentMLClassifier` classifies documents with a Logarithmic Regression algorithm.
{%- endcapture -%}

{%- capture model_input_anno -%}
TOKEN
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

classifier_ml = medical.DocumentMLClassifierModel.pretrained("classifierml_ade", "en", "clinical/models")\
    .setInputCols("token")\
    .setOutputCol("prediction")

clf_Pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    classifier_ml])

data = spark.createDataFrame([["""I feel great after taking tylenol."""], ["""Detection of activated eosinophils in nasal polyps of an aspirin-induced asthma patient."""]]).toDF("text")

result = clf_Pipeline.fit(data).transform(data)


# Show results
result.select('text','prediction.result').show(truncate=False)

+----------------------------------------------------------------------------------------+-------+
|text                                                                                    |result |
+----------------------------------------------------------------------------------------+-------+
|Detection of activated eosinophils in nasal polyps of an aspirin-induced asthma patient.|[False]|
|I feel great after taking tylenol.                                                      |[False]|
+----------------------------------------------------------------------------------------+-------+

{%- endcapture -%}


{%- capture model_scala_medical -%}

import spark.implicits._

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val classifier_ml = DocumentMLClassifierModel.pretrained("classifierml_ade", "en", "clinical/models")
    .setInputCols("token")
    .setOutputCol("prediction")

val clf_Pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    tokenizer, 
    classifier_ml))

val data = Seq(
  "I feel great after taking tylenol.",
  "Detection of activated eosinophils in nasal polyps of an aspirin-induced asthma patient.").toDF("text")
  
val result = clf_Pipeline.fit(data).transform(data)

// Show results

+----------------------------------------------------------------------------------------+-------+
|text                                                                                    |result |
+----------------------------------------------------------------------------------------+-------+
|Detection of activated eosinophils in nasal polyps of an aspirin-induced asthma patient.|[False]|
|I feel great after taking tylenol.                                                      |[False]|
+----------------------------------------------------------------------------------------+-------+

{%- endcapture -%}


{%- capture model_api_link -%}
[DocumentMLClassifierModel](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/classification/DocumentMLClassifierModel.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[DocumentMLClassifierModel](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/classification/document_ml_classifier/index.html#sparknlp_jsl.annotator.classification.document_ml_classifier.DocumentMLClassifierModel)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[DocumentMLClassifierModelNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/DocumentMLClassifierApproach_DocumentMLClassifierModel.ipynb)
{%- endcapture -%}


{%- capture approach_description -%}

Trains a model to classify documents with a Logarithmic Regression algorithm. Training data requires columns for text and their label. The result is a trained DocumentMLClassifierModel.

Parametres:

- `labelCol`: (str) Sets column with the value result we are trying to predict.
- `maxIter`: (Int) Sets maximum number of iterations.
- `tol`: (float) Sets convergence tolerance after each iteration.
- `fitIntercept`: (str) Sets whether to fit an intercept term, default is true.
- `vectorizationModelPath`: (str) Sets a path to the classification model if it has been already trained.
- `classificationModelPath`: (str) Sets a path to the classification model if it has been already trained.
- `classificationModelClass`: (str) Sets a the classification model class from SparkML to use; possible values are: logreg, svm.
- `minTokenNgram`: (int) Sets minimum number of tokens for Ngrams.
- `maxTokenNgram`: (int) Sets maximum number of tokens for Ngrams.
- `mergeChunks`: (boolean) whether to merge all chunks in a document or not (Default: false)

{%- endcapture -%}

{%- capture approach_input_anno -%}
TOKEN
{%- endcapture -%}

{%- capture approach_output_anno -%}
CATEGORY
{%- endcapture -%}

{%- capture approach_python_medical -%}

from johnsnowlabs import nlp, medical 

document = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

token = nlp.Tokenizer()\
    .setInputCols("document")\
    .setOutputCol("token")

classifier_logreg = medical.DocumentMLClassifierApproach() \
    .setInputCols("token") \
    .setLabelCol("category") \
    .setOutputCol("prediction") \
    .setClassificationModelClass("logreg")\
    .setFitIntercept(True)

pipeline = nlp.Pipeline(stages=[
    document, 
    token, 
    classifier_logreg])

result_logreg = pipeline.fit(train_data).transform(test_data).cache()

{%- endcapture -%}


{%- capture approach_scala_medical -%}

import spark.implicits._

val document = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val token = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val classifier_logreg = new DocumentMLClassifierApproach()
    .setInputCols("token")
    .setLabelCol("category")
    .setOutputCol("prediction")
    .setClassificationModelClass("logreg")
    .setFitIntercept(true) 

val pipeline = new Pipeline().setStages(Array(
    document,
    token,
    classifier_logreg)) 

val result_logreg = pipeline.fit(train_data).transform(test_data).cache()
{%- endcapture -%}


{%- capture approach_api_link -%}
[DocumentMLClassifierApproach](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/classification/DocumentMLClassifierApproach.html)
{%- endcapture -%}

{%- capture approach_python_api_link -%}
[DocumentMLClassifierApproach](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/classification/document_ml_classifier/index.html#sparknlp_jsl.annotator.classification.document_ml_classifier.DocumentMLClassifierApproach)
{%- endcapture -%}

{%- capture approach_notebook_link -%}
[DocumentMLClassifierApproachNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/DocumentMLClassifierApproach_DocumentMLClassifierModel.ipynb)
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
