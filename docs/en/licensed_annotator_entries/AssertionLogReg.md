{%- capture title -%}
AssertionLogReg
{%- endcapture -%}

{%- capture approach -%}
approach
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
This is a main class in AssertionLogReg family. Logarithmic Regression is used to extract Assertion Status from extracted entities and text. AssertionLogRegModel requires DOCUMENT, CHUNK and WORD_EMBEDDINGS type annotator inputs, which can be obtained by e.g a [DocumentAssembler](/docs/en/annotators#documentassembler), [NerConverter](/docs/en/annotators#nerconverter) and [WordEmbeddingsModel](/docs/en/annotators#wordembeddings). The result is an assertion status annotation for each recognized entity.
Possible values are `"Negated", "Affirmed" and "Historical"`.

Unlike the DL Model, this class does not extend AnnotatorModel. Instead it extends the RawAnnotator, that's why the main point of interest is method transform().

At the moment there are no pretrained models available for this class. Please refer to AssertionLogRegApproach to train your own model.

Parametres:
- `setAfter(Int)`: Length of the context after the target (Default: 13)

- `setBefore(Int)`: Length of the context before the target (Default: 11)

- `setEndCol(String)`: Column that contains the token number for the end of the target

- `setStartCol(String)`: Column that contains the token number for the start of the target
{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, CHUNK, WORD_EMBEDDINGS
{%- endcapture -%}

{%- capture model_output_anno -%}
ASSERTION
{%- endcapture -%}

{%- capture model_api_link -%}
[AssertionLogRegModel](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/assertion/logreg/AssertionLogRegModel.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[AssertionLogRegModel](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/assertion/assertion_dl_reg/index.html#sparknlp_jsl.annotator.assertion.assertion_dl_reg.AssertionLogRegModel)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[AssertionLogRegModelNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/AssertionLogRegModel.ipynb)
{%- endcapture -%}

{%- capture approach_description -%}
Trains a classification method, which uses the Logarithmic Regression Algorithm. It is used to extract Assertion Status
from extracted entities and text.
Contains all the methods for training a AssertionLogRegModel, together with trainWithChunk, trainWithStartEnd.

Parameters:

- `label` : Column with label per each token

- `maxIter`: This specifies the maximum number of iterations to be performed in the model's training, default: 26

- `regParam` : This specifies the regularization parameter. Regularization helps to control the complexity of the model, aiding in preventing the issue of overfitting.

- `eNetParam` : Elastic net parameter

- `beforeParam` : Length of the context before the target

- `afterParam` : Length of the context after the target

- `startCol` : Column that contains the token number for the start of the target

- `endCol` : Column that contains the token number for the end of the target
{%- endcapture -%}

{%- capture approach_input_anno -%}
DOCUMENT, CHUNK, WORD_EMBEDDINGS
{%- endcapture -%}

{%- capture approach_output_anno -%}
ASSERTION
{%- endcapture -%}

{%- capture approach_python_medical -%}
from johnsnowlabs import nlp, medical

# First define pipeline stages to extract embeddings and text chunks
documentAssembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

glove = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("word_embeddings") \
    .setCaseSensitive(False)

chunkAssembler = nlp.Doc2Chunk() \
    .setInputCols(["document"]) \
    .setChunkCol("target") \
    .setOutputCol("chunk")

# Then the AssertionLogRegApproach model is defined. Label column is needed in the dataset for training.
assertion = medical.AssertionLogRegApproach() \
    .setLabelCol("label") \
    .setInputCols(["document", "chunk", "word_embeddings"]) \
    .setOutputCol("assertion") \
    .setReg(0.01) \
    .setBefore(11) \
    .setAfter(13) \
    .setStartCol("start") \
    .setEndCol("end")

assertionPipeline = nlp.Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    embeddings,
    nerModel,
    nerConverter,
    assertion
])

assertionModel = assertionPipeline.fit(dataset)
{%- endcapture -%}

{%- capture approach_python_legal -%}
from johnsnowlabs import nlp, legal

# First define pipeline stages to extract embeddings and text chunks
documentAssembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

glove = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("word_embeddings") \
    .setCaseSensitive(False)

chunkAssembler = nlp.Doc2Chunk() \
    .setInputCols(["document"]) \
    .setChunkCol("target") \
    .setOutputCol("chunk")

# Then the AssertionLogRegApproach model is defined. Label column is needed in the dataset for training.
assertion = legal.AssertionLogRegApproach() \
    .setLabelCol("label") \
    .setInputCols(["document", "chunk", "word_embeddings"]) \
    .setOutputCol("assertion") \
    .setReg(0.01) \
    .setBefore(11) \
    .setAfter(13) \
    .setStartCol("start") \
    .setEndCol("end")

assertionPipeline = nlp.Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    embeddings,
    nerModel,
    nerConverter,
    assertion
])

assertionModel = assertionPipeline.fit(dataset)
{%- endcapture -%}

{%- capture approach_python_finance -%}
from johnsnowlabs import nlp, finance

# First define pipeline stages to extract embeddings and text chunks
documentAssembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

glove = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("word_embeddings") \
    .setCaseSensitive(False)

chunkAssembler = nlp.Doc2Chunk() \
    .setInputCols(["document"]) \
    .setChunkCol("target") \
    .setOutputCol("chunk")

# Then the AssertionLogRegApproach model is defined. Label column is needed in the dataset for training.
assertion = finance.AssertionLogRegApproach() \
    .setLabelCol("label") \
    .setInputCols(["document", "chunk", "word_embeddings"]) \
    .setOutputCol("assertion") \
    .setReg(0.01) \
    .setBefore(11) \
    .setAfter(13) \
    .setStartCol("start") \
    .setEndCol("end")

assertionPipeline = nlp.Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    embeddings,
    nerModel,
    nerConverter,
    assertion
])

assertionModel = assertionPipeline.fit(dataset)
{%- endcapture -%}

{%- capture approach_scala_medical -%}
 
import spark.implicits._

// First define pipeline stages to extract embeddings and text chunks
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("token")

val glove = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("document", "token"))
  .setOutputCol("word_embeddings")
  .setCaseSensitive(false)

val chunkAssembler = new Doc2Chunk()
  .setInputCols("document")
  .setChunkCol("target")
  .setOutputCol("chunk")

// Then the AssertionLogRegApproach model is defined. Label column is needed in the dataset for training.
val assertion = new AssertionLogRegApproach()
  .setLabelCol("label")
  .setInputCols(Array("document", "chunk", "word_embeddings"))
  .setOutputCol("assertion")
  .setReg(0.01)
  .setBefore(11)
  .setAfter(13)
  .setStartCol("start")
  .setEndCol("end")

val assertionPipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  embeddings,
  nerModel,
  nerConverter,
  assertion
))

val assertionModel = assertionPipeline.fit(dataset)
{%- endcapture -%}

{%- capture approach_scala_legal -%}

import spark.implicits._

// First define pipeline stages to extract embeddings and text chunks
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("token")

val glove = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("document", "token"))
  .setOutputCol("word_embeddings")
  .setCaseSensitive(false)

val chunkAssembler = new Doc2Chunk()
  .setInputCols("document")
  .setChunkCol("target")
  .setOutputCol("chunk")

// Then the AssertionLogRegApproach model is defined. Label column is needed in the dataset for training.
val assertion = new AssertionLogRegApproach()
  .setLabelCol("label")
  .setInputCols(Array("document", "chunk", "word_embeddings"))
  .setOutputCol("assertion")
  .setReg(0.01)
  .setBefore(11)
  .setAfter(13)
  .setStartCol("start")
  .setEndCol("end")

val assertionPipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  embeddings,
  nerModel,
  nerConverter,
  assertion
))

val assertionModel = assertionPipeline.fit(dataset)
{%- endcapture -%}

{%- capture approach_scala_finance -%}

import spark.implicits._

// First define pipeline stages to extract embeddings and text chunks
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("token")

val glove = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("document", "token"))
  .setOutputCol("word_embeddings")
  .setCaseSensitive(false)

val chunkAssembler = new Doc2Chunk()
  .setInputCols("document")
  .setChunkCol("target")
  .setOutputCol("chunk")

// Then the AssertionLogRegApproach model is defined. Label column is needed in the dataset for training.
val assertion = new AssertionLogRegApproach()
  .setLabelCol("label")
  .setInputCols(Array("document", "chunk", "word_embeddings"))
  .setOutputCol("assertion")
  .setReg(0.01)
  .setBefore(11)
  .setAfter(13)
  .setStartCol("start")
  .setEndCol("end")

val assertionPipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  embeddings,
  nerModel,
  nerConverter,
  assertion
))

val assertionModel = assertionPipeline.fit(dataset)
{%- endcapture -%}

{%- capture approach_api_link -%}
[AssertionLogRegApproach](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/assertion/logreg/AssertionLogRegApproach.html)
{%- endcapture -%}

{%- capture approach_python_api_link -%}
[AssertionLogRegApproach](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/assertion/assertion_dl_reg/index.html#sparknlp_jsl.annotator.assertion.assertion_dl_reg.AssertionLogRegApproach)
{%- endcapture -%}

{%- capture approach_notebook_link -%}
[AssertionLogRegApproachNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/AssertionLogRegApproach.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
approach=approach
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
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
