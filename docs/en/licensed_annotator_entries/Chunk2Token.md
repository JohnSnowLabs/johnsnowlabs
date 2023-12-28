{%- capture title -%}
Chunk2Token
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
A feature transformer that converts the input array of strings (annotatorType CHUNK) into an
array of chunk-based tokens (annotatorType TOKEN).

When the input is empty, an empty array is returned.

This Annotator is specially convenient when using NGramGenerator annotations as inputs to WordEmbeddingsModels.

Parameters:

- `inputCols`: The name of the columns containing the input annotations. It can read either a String column or an Array.

- `outputCol`: The name of the column in Document type that is generated. We can specify only one column here.

All the parameters can be set using the corresponding set method in camel case. For example, `.setInputcols()`.
{%- endcapture -%}

{%- capture model_input_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
TOKEN
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical 
# Define a pipeline for generating n-grams
document = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

token = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

ngrammer = nlp.NGramGenerator() \
    .setN(2) \
    .setEnableCumulative(False) \
    .setInputCols(["token"]) \
    .setOutputCol("ngrams") \
    .setDelimiter("_")

# Stage to convert n-gram CHUNKS to TOKEN type
chunk2Token = medical.Chunk2Token()\
    .setInputCols(["ngrams"])\
    .setOutputCol("ngram_tokens")

trainingPipeline = nlp.Pipeline(stages=[
    document, 
    sentenceDetector, 
    token, 
    ngrammer, 
    chunk2Token])

data = spark.createDataFrame([["A 63-year-old man presents to the hospital ..."]]).toDF("text")
result = trainingPipeline.fit(data).transform(data).cache()
result.selectExpr("explode(ngram_tokens)").show(5, False)

+----------------------------------------------------------------+
|col                                                             |
+----------------------------------------------------------------+
|{token, 0, 12, A_63-year-old, {sentence -> 0, chunk -> 0}, []}  |
|{token, 2, 16, 63-year-old_man, {sentence -> 0, chunk -> 1}, []}|
|{token, 14, 25, man_presents, {sentence -> 0, chunk -> 2}, []}  |
|{token, 18, 28, presents_to, {sentence -> 0, chunk -> 3}, []}   |
|{token, 27, 32, to_the, {sentence -> 0, chunk -> 4}, []}        |
+----------------------------------------------------------------+
{%- endcapture -%}


{%- capture model_python_legal -%}
from johnsnowlabs import nlp, legal 
# Define a pipeline for generating n-grams
document = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

token = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

ngrammer = nlp.NGramGenerator() \
    .setN(2) \
    .setEnableCumulative(False) \
    .setInputCols(["token"]) \
    .setOutputCol("ngrams") 

# Stage to convert n-gram CHUNKS to TOKEN type
chunk2Token = legal.Chunk2Token()\
    .setInputCols(["ngrams"])\
    .setOutputCol("ngram_tokens")

trainingPipeline = nlp.Pipeline(stages=[
    document, 
    sentenceDetector, 
    token, 
    ngrammer, 
    chunk2Token])

data = spark.createDataFrame([["This is an Intellectual Property Agreement between Amazon Inc. and Atlantic Inc."]]).toDF("text")
result = trainingPipeline.fit(data).transform(data).cache()
result.selectExpr("explode(ngram_tokens)").show(5, False)

+-----------------------------------------------------------------------+
|col                                                                    |
+-----------------------------------------------------------------------+
|{token, 0, 6, This is, {sentence -> 0, chunk -> 0}, []}                |
|{token, 5, 9, is an, {sentence -> 0, chunk -> 1}, []}                  |
|{token, 8, 22, an Intellectual, {sentence -> 0, chunk -> 2}, []}       |
|{token, 11, 31, Intellectual Property, {sentence -> 0, chunk -> 3}, []}|
|{token, 24, 41, Property Agreement, {sentence -> 0, chunk -> 4}, []}   |
+-----------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_python_finance -%}
from johnsnowlabs import nlp, finance
# Define a pipeline for generating n-grams
document = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

token = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

ngrammer = nlp.NGramGenerator() \
    .setN(2) \
    .setEnableCumulative(False) \
    .setInputCols(["token"]) \
    .setOutputCol("ngrams") 

# Stage to convert n-gram CHUNKS to TOKEN type
chunk2Token = finance.Chunk2Token()\
    .setInputCols(["ngrams"])\
    .setOutputCol("ngram_tokens")

trainingPipeline = nlp.Pipeline(stages=[
    document, 
    sentenceDetector, 
    token, 
    ngrammer, 
    chunk2Token])

data = spark.createDataFrame([["Our competitors include the following by general category: legacy antivirus product providers, such as McAfee LLC and Broadcom Inc."]]).toDF("text")

result = trainingPipeline.fit(data).transform(data)
result.selectExpr("explode(ngram_tokens)").show(5, False)

+--------------------------------------------------------------------+
|col                                                                 |
+--------------------------------------------------------------------+
|{token, 0, 14, Our competitors, {sentence -> 0, chunk -> 0}, []}    |
|{token, 4, 22, competitors include, {sentence -> 0, chunk -> 1}, []}|
|{token, 16, 26, include the, {sentence -> 0, chunk -> 2}, []}       |
|{token, 24, 36, the following, {sentence -> 0, chunk -> 3}, []}     |
|{token, 28, 39, following by, {sentence -> 0, chunk -> 4}, []}      |
+--------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_scala_medical -%}

import spark.implicits._

// Define a pipeline for generating n-grams
val document = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val token = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val ngrammer = new NGramGenerator()
    .setN(2)
    .setEnableCumulative(false)
    .setInputCols("token")
    .setOutputCol("ngrams")
    .setDelimiter("_")

// Stage to convert n-gram CHUNKS to TOKEN type
val chunk2Token = new Chunk2Token()
    .setInputCols("ngrams")
    .setOutputCol("ngram_tokens")

val trainingPipeline = new Pipeline().setStages(Array(
    document, 
    sentenceDetector, 
    token, 
    ngrammer, 
    chunk2Token))

val data = Seq(("A 63-year-old man presents to the hospital ...")).toDF("text")

val result = trainingPipeline.fit(data).transform(data)

+----------------------------------------------------------------+
|col                                                             |
+----------------------------------------------------------------+
|{token, 3, 15, A_63-year-old, {sentence -> 0, chunk -> 0}, []}  |
|{token, 5, 19, 63-year-old_man, {sentence -> 0, chunk -> 1}, []}|
|{token, 17, 28, man_presents, {sentence -> 0, chunk -> 2}, []}  |
|{token, 21, 31, presents_to, {sentence -> 0, chunk -> 3}, []}   |
|{token, 30, 35, to_the, {sentence -> 0, chunk -> 4}, []}        |
+----------------------------------------------------------------+

{%- endcapture -%}

{%- capture model_scala_legal -%}

import spark.implicits._

// Define a pipeline for generating n-grams
val document = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val token = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val ngrammer = new NGramGenerator()
    .setN(2)
    .setEnableCumulative(false)
    .setInputCols("token")
    .setOutputCol("ngrams")

// Stage to convert n-gram CHUNKS to TOKEN type
val chunk2Token = new Chunk2Token()
    .setInputCols("ngrams")
    .setOutputCol("ngram_tokens")

val trainingPipeline = new Pipeline().setStages(Array(
    document, 
    sentenceDetector, 
    token, 
    ngrammer, 
    chunk2Token))

val data = Seq(("This is an Intellectual Property Agreement between Amazon Inc. and Atlantic Inc.")).toDF("text")

val result = trainingPipeline.fit(data).transform(data)

+-----------------------------------------------------------------------+
|col                                                                    |
+-----------------------------------------------------------------------+
|{token, 0, 6, This is, {sentence -> 0, chunk -> 0}, []}                |
|{token, 5, 9, is an, {sentence -> 0, chunk -> 1}, []}                  |
|{token, 8, 22, an Intellectual, {sentence -> 0, chunk -> 2}, []}       |
|{token, 11, 31, Intellectual Property, {sentence -> 0, chunk -> 3}, []}|
|{token, 24, 41, Property Agreement, {sentence -> 0, chunk -> 4}, []}   |
+-----------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_scala_finance -%}

import spark.implicits._

// Define a pipeline for generating n-grams
val document = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val token = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val ngrammer = new NGramGenerator()
    .setN(2)
    .setEnableCumulative(false)
    .setInputCols("token")
    .setOutputCol("ngrams")

// Stage to convert n-gram CHUNKS to TOKEN type
val chunk2Token = new Chunk2Token()
    .setInputCols("ngrams")
    .setOutputCol("ngram_tokens")

val trainingPipeline = new Pipeline().setStages(Array(
    document, 
    sentenceDetector, 
    token, 
    ngrammer, 
    chunk2Token))

val data = Seq(("Our competitors include the following by general category: legacy antivirus product providers, such as McAfee LLC and Broadcom Inc.")).toDF("text")

val result = trainingPipeline.fit(data).transform(data)

+--------------------------------------------------------------------+
|col                                                                 |
+--------------------------------------------------------------------+
|{token, 0, 14, Our competitors, {sentence -> 0, chunk -> 0}, []}    |
|{token, 4, 22, competitors include, {sentence -> 0, chunk -> 1}, []}|
|{token, 16, 26, include the, {sentence -> 0, chunk -> 2}, []}       |
|{token, 24, 36, the following, {sentence -> 0, chunk -> 3}, []}     |
|{token, 28, 39, following by, {sentence -> 0, chunk -> 4}, []}      |
+--------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_api_link -%}
[Chunk2Token](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/Chunk2Token.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[Chunk2Token](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/chunk2_token/index.html)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[Chunk2TokenNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/Chunk2Token.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_python_legal=model_python_legal
model_python_finance=model_python_finance
model_scala_medical=model_scala_medical
model_scala_legal=model_scala_legal
model_scala_finance=model_scala_finance
model_api_link=model_api_link
model_python_api_link=model_python_api_link
model_notebook_link=model_notebook_link
%}
