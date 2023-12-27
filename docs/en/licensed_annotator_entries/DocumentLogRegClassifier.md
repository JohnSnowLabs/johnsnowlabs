{%- capture title -%}
DocumentLogRegClassifier
{%- endcapture -%}

{%- capture approach -%}
approach
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
Classifies documents with a Logarithmic Regression algorithm.
Currently there are no pretrained models available.
Please see DocumentLogRegClassifierApproach to train your own model.

Parameters:

- `setMergeChunks(merge)`: Sets whether to merge all chunks in a document or not (Default: false).

- `setLabels(value)`: Sets array to output the label in the original form.

- `setVectorizationModel(model)`: Sets a path to the classification model if it has been already trained.

- `setClassificationModel(model)`: Sets a path to the the classification model if it has been already trained.

Please check out the [Models Hub](https://nlp.johnsnowlabs.com/models) for available models in the future.
{%- endcapture -%}

{%- capture model_input_anno -%}
TOKEN
{%- endcapture -%}

{%- capture model_output_anno -%}
CATEGORY
{%- endcapture -%}

{%- capture model_api_link -%}
[DocumentLogRegClassifierModel](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/classification/DocumentLogRegClassifierModel.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[DocumentLogRegClassifierModel](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/classification/document_log_classifier/index.html#sparknlp_jsl.annotator.classification.document_log_classifier.DocumentLogRegClassifierModel)
{%- endcapture -%}

{%- capture approach_description -%}
Trains a model to classify documents with a Logarithmic Regression algorithm. Training data requires columns for
text and their label. The result is a trained DocumentLogRegClassifierModel.
{%- endcapture -%}

{%- capture approach_input_anno -%}
TOKEN
{%- endcapture -%}

{%- capture approach_output_anno -%}
CATEGORY
{%- endcapture -%}

{%- capture approach_python_medical -%}
from johnsnowlabs import nlp, medical
# Define pipeline stages to prepare the data
document_assembler = nlp.DocumentAssembler() \
  .setInputCol("text") \
  .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
  .setInputCols(["document"]) \
  .setOutputCol("token")

normalizer = nlp.Normalizer() \
  .setInputCols(["token"]) \
  .setOutputCol("normalized")

stopwords_cleaner = nlp.StopWordsCleaner() \
  .setInputCols(["normalized"]) \
  .setOutputCol("cleanTokens") \
  .setCaseSensitive(False)

stemmer = nlp.Stemmer() \
  .setInputCols(["cleanTokens"]) \
  .setOutputCol("stem")

# Define the document classifier and fit training data to it
logreg = medical.DocumentLogRegClassifierApproach() \
  .setInputCols(["stem"]) \
  .setLabelCol("category") \
  .setOutputCol("prediction")

pipeline = nlp.Pipeline(stages=[
  document_assembler,
  tokenizer,
  normalizer,
  stopwords_cleaner,
  stemmer,
  logreg
])

model = pipeline.fit(trainingData)
{%- endcapture -%}

{%- capture approach_python_legal -%}
from johnsnowlabs import nlp, legal
# Define pipeline stages to prepare the data
document_assembler = nlp.DocumentAssembler() \
  .setInputCol("text") \
  .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
  .setInputCols(["document"]) \
  .setOutputCol("token")

normalizer = nlp.Normalizer() \
  .setInputCols(["token"]) \
  .setOutputCol("normalized")

stopwords_cleaner = nlp.StopWordsCleaner() \
  .setInputCols(["normalized"]) \
  .setOutputCol("cleanTokens") \
  .setCaseSensitive(False)

stemmer = nlp.Stemmer() \
  .setInputCols(["cleanTokens"]) \
  .setOutputCol("stem")

# Define the document classifier and fit training data to it
logreg = legal.DocumentLogRegClassifierApproach() \
  .setInputCols(["stem"]) \
  .setLabelCol("category") \
  .setOutputCol("prediction")

pipeline = nlp.Pipeline(stages=[
  document_assembler,
  tokenizer,
  normalizer,
  stopwords_cleaner,
  stemmer,
  logreg
])

model = pipeline.fit(trainingData)
{%- endcapture -%}


{%- capture approach_python_finance -%}
from johnsnowlabs import nlp, finance
# Define pipeline stages to prepare the data
document_assembler = nlp.DocumentAssembler() \
  .setInputCol("text") \
  .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
  .setInputCols(["document"]) \
  .setOutputCol("token")

normalizer = nlp.Normalizer() \
  .setInputCols(["token"]) \
  .setOutputCol("normalized")

stopwords_cleaner = nlp.StopWordsCleaner() \
  .setInputCols(["normalized"]) \
  .setOutputCol("cleanTokens") \
  .setCaseSensitive(False)

stemmer = nlp.Stemmer() \
  .setInputCols(["cleanTokens"]) \
  .setOutputCol("stem")

# Define the document classifier and fit training data to it
logreg = finance.DocumentLogRegClassifierApproach() \
  .setInputCols(["stem"]) \
  .setLabelCol("category") \
  .setOutputCol("prediction")

pipeline = nlp.Pipeline(stages=[
  document_assembler,
  tokenizer,
  normalizer,
  stopwords_cleaner,
  stemmer,
  logreg
])

model = pipeline.fit(trainingData)
{%- endcapture -%}

{%- capture approach_scala_medical -%}
import spark.implicits._ 
// Define pipeline stages to prepare the data
val document_assembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("token")

val normalizer = new Normalizer()
  .setInputCols("token")
  .setOutputCol("normalized")

val stopwords_cleaner = new StopWordsCleaner()
  .setInputCols("normalized")
  .setOutputCol("cleanTokens")
  .setCaseSensitive(false)

val stemmer = new Stemmer()
  .setInputCols("cleanTokens")
  .setOutputCol("stem")

// Define the document classifier and fit training data to it
val logreg = new DocumentLogRegClassifierApproach()
  .setInputCols("stem")
  .setLabelCol("category")
  .setOutputCol("prediction")

val pipeline = new Pipeline().setStages(Array(
  document_assembler,
  tokenizer,
  normalizer,
  stopwords_cleaner,
  stemmer,
  logreg
))

val model = pipeline.fit(trainingData)
{%- endcapture -%}

{%- capture approach_scala_legal -%}
import spark.implicits._
// Define pipeline stages to prepare the data
val document_assembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("token")

val normalizer = new Normalizer()
  .setInputCols("token")
  .setOutputCol("normalized")

val stopwords_cleaner = new StopWordsCleaner()
  .setInputCols("normalized")
  .setOutputCol("cleanTokens")
  .setCaseSensitive(false)

val stemmer = new Stemmer()
  .setInputCols("cleanTokens")
  .setOutputCol("stem")

// Define the document classifier and fit training data to it
val logreg = new DocumentLogRegClassifierApproach()
  .setInputCols("stem")
  .setLabelCol("category")
  .setOutputCol("prediction")

val pipeline = new Pipeline().setStages(Array(
  document_assembler,
  tokenizer,
  normalizer,
  stopwords_cleaner,
  stemmer,
  logreg
))

val model = pipeline.fit(trainingData)
{%- endcapture -%}

{%- capture approach_scala_finance -%}
import spark.implicits._ 
// Define pipeline stages to prepare the data
val document_assembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("token")

val normalizer = new Normalizer()
  .setInputCols("token")
  .setOutputCol("normalized")

val stopwords_cleaner = new StopWordsCleaner()
  .setInputCols("normalized")
  .setOutputCol("cleanTokens")
  .setCaseSensitive(false)

val stemmer = new Stemmer()
  .setInputCols("cleanTokens")
  .setOutputCol("stem")

// Define the document classifier and fit training data to it
val logreg = new DocumentLogRegClassifierApproach()
  .setInputCols("stem")
  .setLabelCol("category")
  .setOutputCol("prediction")

val pipeline = new Pipeline().setStages(Array(
  document_assembler,
  tokenizer,
  normalizer,
  stopwords_cleaner,
  stemmer,
  logreg
))

val model = pipeline.fit(trainingData)
{%- endcapture -%}

{%- capture approach_api_link -%}
[DocumentLogRegClassifierApproach](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/classification/DocumentLogRegClassifierApproach.html)
{%- endcapture -%}

{%- capture approach_python_api_link -%}
[DocumentLogRegClassifierApproach](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/classification/document_log_classifier/index.html#sparknlp_jsl.annotator.classification.document_log_classifier.DocumentLogRegClassifierApproach)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
approach=approach
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_api_link=model_api_link
model_python_api_link=model_python_api_link
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
%}
