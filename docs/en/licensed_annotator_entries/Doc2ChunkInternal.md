{%- capture title -%}
Doc2ChunkInternal
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}

Converts `DOCUMENT`, `TOKEN` typed annotations into `CHUNK` type with the contents of a `chunkCol`. Chunk text must be contained within input `DOCUMENT`. May be either `StringType` or `ArrayType[StringType]` (using `setIsArray`). Useful for annotators that require a CHUNK type input.

Parameters:

- `inputCols`: The name of the columns containing the input annotations. It can read either a String column or an Array.

- `outputCol`: The name of the column in Document type that is generated. We can specify only one column here.


All the parameters can be set using the corresponding set method in camel case. For example, `.setInputcols()`.

For more extended examples on document pre-processing see the [Spark NLP Workshop](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Public/2.Text_Preprocessing_with_SparkNLP_Annotators_Transformers.ipynb).


{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, TOKEN
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_python_medical -%}

from johnsnowlabs import nlp, medical

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = nlp.Tokenizer()\
    .setInputCols("document")\
    .setOutputCol("token")

chunkAssembler = medical.Doc2ChunkInternal()\
    .setInputCols("document", "token")\
    .setChunkCol("target")\
    .setOutputCol("chunk")\
    .setIsArray(True)

pipeline = nlp.Pipeline().setStages([documentAssembler, tokenizer, chunkAssembler])

data = spark.createDataFrame(
    [
        [
            "Spark NLP is an open-source text processing library for advanced natural language processing.",
            ["Spark NLP", "text processing library", "natural language processing"],
        ]
    ]
).toDF("text", "target")


result = pipeline.fit(data).transform(data)
result.selectExpr("chunk.result", "chunk.annotatorType").show(truncate=False)

+-----------------------------------------------------------------+---------------------+
|result                                                           |annotatorType        |
+-----------------------------------------------------------------+---------------------+
|[Spark NLP, text processing library, natural language processing]|[chunk, chunk, chunk]|
+-----------------------------------------------------------------+---------------------+

{%- endcapture -%}

{%- capture model_scala_medical -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val chunkAssembler = new Doc2ChunkInternal()
    .setInputCols(Array("document", "token"))
    .setChunkCol("target")
    .setOutputCol("chunk")
    .setIsArray(true)

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, 
    tokenizer, 
    chunkAssembler
))

val data = Seq(("Spark NLP is an open-source text processing library for advanced natural language processing.",
               "Spark NLP", "text processing library", "natural language processing")).toDF("text", "target")

val result = pipeline.fit(data).transform(data)

+-----------------------------------------------------------------+---------------------+
|result                                                           |annotatorType        |
+-----------------------------------------------------------------+---------------------+
|[Spark NLP, text processing library, natural language processing]|[chunk, chunk, chunk]|
+-----------------------------------------------------------------+---------------------+

{%- endcapture -%}

{%- capture model_python_legal -%}

from johnsnowlabs import nlp, legal

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = nlp.Tokenizer()\
    .setInputCols("document")\
    .setOutputCol("token")

chunkAssembler = legal.Doc2ChunkInternal()\
    .setInputCols("document", "token")\
    .setChunkCol("target")\
    .setOutputCol("chunk")\
    .setIsArray(True)

pipeline = nlp.Pipeline().setStages([documentAssembler, tokenizer, chunkAssembler])

data = spark.createDataFrame(
    [
        [
            "Spark NLP is an open-source text processing library for advanced natural language processing.",
            ["Spark NLP", "text processing library", "natural language processing"],
        ]
    ]
).toDF("text", "target")


result = pipeline.fit(data).transform(data)
result.selectExpr("chunk.result", "chunk.annotatorType").show(truncate=False)

+-----------------------------------------------------------------+---------------------+
|result                                                           |annotatorType        |
+-----------------------------------------------------------------+---------------------+
|[Spark NLP, text processing library, natural language processing]|[chunk, chunk, chunk]|
+-----------------------------------------------------------------+---------------------+

{%- endcapture -%}

{%- capture model_scala_legal -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val chunkAssembler = new Doc2ChunkInternal()
    .setInputCols(Array("document", "token"))
    .setChunkCol("target")
    .setOutputCol("chunk")
    .setIsArray(true)

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, 
    tokenizer, 
    chunkAssembler
))

val data = Seq(("Spark NLP is an open-source text processing library for advanced natural language processing.",
               "Spark NLP", "text processing library", "natural language processing")).toDF("text", "target")

val result = pipeline.fit(data).transform(data)

+-----------------------------------------------------------------+---------------------+
|result                                                           |annotatorType        |
+-----------------------------------------------------------------+---------------------+
|[Spark NLP, text processing library, natural language processing]|[chunk, chunk, chunk]|
+-----------------------------------------------------------------+---------------------+

{%- endcapture -%}

{%- capture model_python_finance -%}
from johnsnowlabs import nlp, finance

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = nlp.Tokenizer()\
    .setInputCols("document")\
    .setOutputCol("token")

chunkAssembler = finance.Doc2ChunkInternal()\
    .setInputCols("document", "token")\
    .setChunkCol("target")\
    .setOutputCol("chunk")\
    .setIsArray(True)

pipeline = nlp.Pipeline().setStages([documentAssembler, tokenizer, chunkAssembler])

data = spark.createDataFrame(
    [
        [
            "Spark NLP is an open-source text processing library for advanced natural language processing.",
            ["Spark NLP", "text processing library", "natural language processing"],
        ]
    ]
).toDF("text", "target")


result = pipeline.fit(data).transform(data)
result.selectExpr("chunk.result", "chunk.annotatorType").show(truncate=False)

+-----------------------------------------------------------------+---------------------+
|result                                                           |annotatorType        |
+-----------------------------------------------------------------+---------------------+
|[Spark NLP, text processing library, natural language processing]|[chunk, chunk, chunk]|
+-----------------------------------------------------------------+---------------------+

{%- endcapture -%}

{%- capture model_scala_finance -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val chunkAssembler = new Doc2ChunkInternal()
    .setInputCols(Array("document", "token"))
    .setChunkCol("target")
    .setOutputCol("chunk")
    .setIsArray(true)

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, 
    tokenizer, 
    chunkAssembler
))

val data = Seq(("Spark NLP is an open-source text processing library for advanced natural language processing.",
               "Spark NLP", "text processing library", "natural language processing")).toDF("text", "target")

val result = pipeline.fit(data).transform(data)

+-----------------------------------------------------------------+---------------------+
|result                                                           |annotatorType        |
+-----------------------------------------------------------------+---------------------+
|[Spark NLP, text processing library, natural language processing]|[chunk, chunk, chunk]|
+-----------------------------------------------------------------+---------------------+

{%- endcapture -%}

{%- capture model_api_link -%}
[Doc2ChunkInternal](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/annotator/Doc2ChunkInternal.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[Doc2ChunkInternal](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/doc2_chunk_internal/index.html#sparknlp_jsl.annotator.doc2_chunk_internal.Doc2ChunkInternal)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[Doc2ChunkInternalNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/Doc2ChunkInternal.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical
model_python_legal=model_python_legal
model_scala_legal=model_scala_legal
model_python_medical=model_python_finance
model_scala_finance=model_scala_finance
model_api_link=model_api_link
model_python_api_link=model_python_api_link
model_notebook_link=model_notebook_link
%}
