{%- capture title -%}
ChunkFilterer
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
Filters entities coming from CHUNK annotations. Filters can be set via a white list of terms or a regular expression.
White list criteria is enabled by default. To use regex, `criteria` has to be set to `regex`.

Parametres:

- `inputCols`: The name of the columns containing the input annotations. It can read either a String column or an Array.

- `outputCol`: The name of the column in Document type that is generated. We can specify only one column here.

- `criteria`: Tag representing what is the criteria to filter the chunks. Possibles values are: - isIn: Filter by the chunk - regex: Filter using a regex

- `whiteList`: If defined, list of entities to process. The rest will be ignored.

- `blackList`: If defined, list of entities to ignore. The rest will be processed.

- `regex`: If defined, list of regex to process the chunks (Default: []).

- `filterEntity`: If equal to “entity”, use the ner label to filter. If set to “result”, use the result attribute of the annotation to filter.

- `entitiesConfidence`: Path to csv with pairs (entity,confidenceThreshold). Filter the chunks with entities which have confidence lower than the confidence threshold.

All the parameters can be set using the corresponding set method in camel case. For example, `.setInputcols()`.
{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT,CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

# Filtering POS tags
# First pipeline stages to extract the POS tags are defined

docAssembler = nlp.DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
  .setInputCols(["sentence"])\
  .setOutputCol("token")

posTagger = nlp.PerceptronModel.pretrained() \
  .setInputCols(["sentence", "token"]) \
  .setOutputCol("pos")

chunker = nlp.Chunker() \
  .setInputCols(["pos", "sentence"]) \
  .setOutputCol("chunk") \
  .setRegexParsers(["(<NN>)+"])

# Then the chunks can be filtered via a white list. Here only terms with "gastroenteritis" remain.
chunkerFilter = medical.ChunkFilterer() \
  .setInputCols(["sentence","chunk"]) \
  .setOutputCol("filtered") \
  .setCriteria("isin") \
  .setWhiteList(["gastroenteritis"])

pipeline = nlp.Pipeline(stages=[
  docAssembler,
  sentenceDetector,
  tokenizer,
  posTagger,
  chunker,
  chunkerFilter])

data = spark.createDataFrame([["Has a past history of gastroenteritis and stomach pain, however patient ..."]]).toDF("text")

result = pipeline.fit(data).transform(data)
result.selectExpr("explode(chunk)").show(truncate=False)
+---------------------------------------------------------------------------------+
|col                                                                              |
+---------------------------------------------------------------------------------+
|{chunk, 11, 17, history, {sentence -> 0, chunk -> 0}, []}                        |
|{chunk, 22, 36, gastroenteritis, {sentence -> 0, chunk -> 1}, []}                |
|{chunk, 42, 53, stomach pain, {sentence -> 0, chunk -> 2}, []}                   |
|{chunk, 64, 70, patient, {sentence -> 0, chunk -> 3}, []}                        |
|{chunk, 81, 110, stomach pain now.We don't care, {sentence -> 0, chunk -> 4}, []}|
|{chunk, 118, 132, gastroenteritis, {sentence -> 0, chunk -> 5}, []}              |
+---------------------------------------------------------------------------------+

result.selectExpr("explode(filtered)").show(truncate=False)
+-------------------------------------------------------------------+
|col                                                                |
+-------------------------------------------------------------------+
|{chunk, 22, 36, gastroenteritis, {sentence -> 0, chunk -> 1}, []}  |
|{chunk, 118, 132, gastroenteritis, {sentence -> 0, chunk -> 5}, []}|
+-------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_python_legal -%}
from johnsnowlabs import nlp, legal

# Filtering POS tags
# First pipeline stages to extract the POS tags are defined

docAssembler = nlp.DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
  .setInputCols(["sentence"])\
  .setOutputCol("token")

posTagger = nlp.PerceptronModel.pretrained() \
  .setInputCols(["sentence", "token"]) \
  .setOutputCol("pos")

chunker = nlp.Chunker() \
  .setInputCols(["pos", "sentence"]) \
  .setOutputCol("chunk") \
  .setRegexParsers(["(<NN>)+"])

# Then the chunks can be filtered via a white list. Here only terms with "gastroenteritis" remain.
chunkerFilter = legal.ChunkFilterer() \
  .setInputCols(["sentence","chunk"]) \
  .setOutputCol("filtered") \
  .setCriteria("isin") \
  .setWhiteList(["rate"])

pipeline = nlp.Pipeline(stages=[
  docAssembler,
  sentenceDetector,
  tokenizer,
  posTagger,
  chunker,
  chunkerFilter])

data = spark.createDataFrame([["AWA Group LP intends to pay dividends on the Common Units on a quarterly basis at an annual rate of 8.00% of the Offering Price."]]).toDF("text")

result = pipeline.fit(data).transform(data)
result.selectExpr("explode(chunk)").show(truncate=False)
+-------------------------------------------------------+
|col                                                    |
+-------------------------------------------------------+
|{chunk, 73, 77, basis, {sentence -> 0, chunk -> 0}, []}|
|{chunk, 92, 95, rate, {sentence -> 0, chunk -> 1}, []} |
+-------------------------------------------------------+

result.selectExpr("explode(filtered)").show(truncate=False)
+-------------------------------------------------------+
|col                                                    |
+-------------------------------------------------------+
|{chunk, 92, 95, rate, {sentence -> 0, chunk -> 1}, []} |
+-------------------------------------------------------+

{%- endcapture -%}

{%- capture model_python_finance -%}
from johnsnowlabs import nlp, finance

# Filtering POS tags
# First pipeline stages to extract the POS tags are defined

docAssembler = nlp.DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
  .setInputCols(["sentence"])\
  .setOutputCol("token")

posTagger = nlp.PerceptronModel.pretrained() \
  .setInputCols(["sentence", "token"]) \
  .setOutputCol("pos")

chunker = nlp.Chunker() \
  .setInputCols(["pos", "sentence"]) \
  .setOutputCol("chunk") \
  .setRegexParsers(["(<NN>)+"])

# Then the chunks can be filtered via a white list. Here only terms with "gastroenteritis" remain.
chunkerFilter = finance.ChunkFilterer() \
  .setInputCols(["sentence","chunk"]) \
  .setOutputCol("filtered") \
  .setCriteria("isin") \
  .setWhiteList(["rate"])

pipeline = nlp.Pipeline(stages=[
  docAssembler,
  sentenceDetector,
  tokenizer,
  posTagger,
  chunker,
  chunkerFilter])

data = spark.createDataFrame([["AWA Group LP intends to pay dividends on the Common Units on a quarterly basis at an annual rate of 8.00% of the Offering Price."]]).toDF("text")

result = pipeline.fit(data).transform(data)
result.selectExpr("explode(chunk)").show(truncate=False)
+-------------------------------------------------------+
|col                                                    |
+-------------------------------------------------------+
|{chunk, 73, 77, basis, {sentence -> 0, chunk -> 0}, []}|
|{chunk, 92, 95, rate, {sentence -> 0, chunk -> 1}, []} |
+-------------------------------------------------------+

result.selectExpr("explode(filtered)").show(truncate=False)
+-------------------------------------------------------+
|col                                                    |
+-------------------------------------------------------+
|{chunk, 92, 95, rate, {sentence -> 0, chunk -> 1}, []} |
+-------------------------------------------------------+
{%- endcapture -%}


{%- capture model_scala_medical -%}
// Filtering POS tags
// First pipeline stages to extract the POS tags are defined

import spark.implicits._

val docAssembler = new DocumentAssembler()
 .setInputCol("text") 
 .setOutputCol("document") 

val sentenceDetector = new SentenceDetector()
 .setInputCols(Array("document")) 
 .setOutputCol("sentence") 

val tokenizer = new Tokenizer()
 .setInputCols(Array("sentence")) 
 .setOutputCol("token") 

val posTagger = PerceptronModel.pretrained()
 .setInputCols(Array("sentence","token")) 
 .setOutputCol("pos") 

val chunker = new Chunker()
 .setInputCols(Array("pos","sentence")) 
 .setOutputCol("chunk") 
 .setRegexParsers(Array("(<NN>) +")) 

val chunkerFilter = new ChunkFilterer()
 .setInputCols(Array("sentence","chunk")) 
 .setOutputCol("filtered") 
 .setCriteria("isin") 
 .setWhiteList(Array("gastroenteritis"))

val pipeline = new Pipeline().setStages(Array(
  docAssembler, 
  sentenceDetector, 
  tokenizer, 
  posTagger, 
  chunker, 
  chunkerFilter)) 

val text ="""Has a past history of gastroenteritis and stomach pain, however patient ..."""

val data = Seq(text).toDF("text")
val result = pipeline.fit(data).transform(data)

// result.selectExpr("explode(chunk)").show(truncate=false)
+---------------------------------------------------------------------------------+
|col                                                                              |
+---------------------------------------------------------------------------------+
|{chunk, 11, 17, history, {sentence -> 0, chunk -> 0}, []}                        |
|{chunk, 22, 36, gastroenteritis, {sentence -> 0, chunk -> 1}, []}                |
|{chunk, 42, 53, stomach pain, {sentence -> 0, chunk -> 2}, []}                   |
|{chunk, 64, 70, patient, {sentence -> 0, chunk -> 3}, []}                        |
|{chunk, 81, 110, stomach pain now.We don't care, {sentence -> 0, chunk -> 4}, []}|
|{chunk, 118, 132, gastroenteritis, {sentence -> 0, chunk -> 5}, []}              |
+---------------------------------------------------------------------------------+

// result.selectExpr("explode(filtered)").show(truncate=false)
+-------------------------------------------------------------------+
|col                                                                |
+-------------------------------------------------------------------+
|{chunk, 22, 36, gastroenteritis, {sentence -> 0, chunk -> 1}, []}  |
|{chunk, 118, 132, gastroenteritis, {sentence -> 0, chunk -> 5}, []}|
+-------------------------------------------------------------------+
{%- endcapture -%}


{%- capture model_scala_legal -%}
import spark.implicits._

val docAssembler = new DocumentAssembler()
 .setInputCol("text") 
 .setOutputCol("document") 

val sentenceDetector = new SentenceDetector()
 .setInputCols(Array("document")) 
 .setOutputCol("sentence") 

val tokenizer = new Tokenizer()
 .setInputCols(Array("sentence")) 
 .setOutputCol("token") 

val posTagger = PerceptronModel.pretrained()
 .setInputCols(Array("sentence","token")) 
 .setOutputCol("pos") 

val chunker = new Chunker()
 .setInputCols(Array("pos","sentence")) 
 .setOutputCol("chunk") 
 .setRegexParsers(Array("(<NN>) +")) 

val chunkerFilter = new ChunkFilterer()
 .setInputCols(Array("sentence","chunk")) 
 .setOutputCol("filtered") 
 .setCriteria("isin") 

val pipeline = new Pipeline().setStages(Array(
  docAssembler, 
  sentenceDetector, 
  tokenizer, 
  posTagger, 
  chunker, 
  chunkerFilter)) 

val text ="""AWA Group LP intends to pay dividends on the Common Units on a quarterly basis at an annual rate of 8.00% of the Offering Price."""

val data = Seq(text).toDF("text")
val result = pipeline.fit(data).transform(data)

// result.selectExpr("explode(chunk)").show(truncate=false)
+-------------------------------------------------------+
|col                                                    |
+-------------------------------------------------------+
|{chunk, 73, 77, basis, {sentence -> 0, chunk -> 0}, []}|
|{chunk, 92, 95, rate, {sentence -> 0, chunk -> 1}, []} |
+-------------------------------------------------------+

// result.selectExpr("explode(filtered)").show(truncate=False)
+-------------------------------------------------------+
|col                                                    |
+-------------------------------------------------------+
|{chunk, 92, 95, rate, {sentence -> 0, chunk -> 1}, []} |
+-------------------------------------------------------+
{%- endcapture -%}

{%- capture model_scala_finance -%}
import spark.implicits._

val docAssembler = new DocumentAssembler()
 .setInputCol("text") 
 .setOutputCol("document") 

val sentenceDetector = new SentenceDetector()
 .setInputCols(Array("document")) 
 .setOutputCol("sentence") 

val tokenizer = new Tokenizer()
 .setInputCols(Array("sentence")) 
 .setOutputCol("token") 

val posTagger = PerceptronModel.pretrained()
 .setInputCols(Array("sentence","token")) 
 .setOutputCol("pos") 

val chunker = new Chunker()
 .setInputCols(Array("pos","sentence")) 
 .setOutputCol("chunk") 
 .setRegexParsers(Array("(<NN>) +")) 

val chunkerFilter = new ChunkFilterer()
 .setInputCols(Array("sentence","chunk")) 
 .setOutputCol("filtered") 
 .setCriteria("isin") 

val pipeline = new Pipeline().setStages(Array(
  docAssembler, 
  sentenceDetector, 
  tokenizer, 
  posTagger, 
  chunker, 
  chunkerFilter)) 

val text ="""AWA Group LP intends to pay dividends on the Common Units on a quarterly basis at an annual rate of 8.00% of the Offering Price."""

val data = Seq(text).toDF("text")
val result = pipeline.fit(data).transform(data)

// result.selectExpr("explode(chunk)").show(truncate=false)
+-------------------------------------------------------+
|col                                                    |
+-------------------------------------------------------+
|{chunk, 73, 77, basis, {sentence -> 0, chunk -> 0}, []}|
|{chunk, 92, 95, rate, {sentence -> 0, chunk -> 1}, []} |
+-------------------------------------------------------+

// result.selectExpr("explode(filtered)").show(truncate=False)
+-------------------------------------------------------+
|col                                                    |
+-------------------------------------------------------+
|{chunk, 92, 95, rate, {sentence -> 0, chunk -> 1}, []} |
+-------------------------------------------------------+
{%- endcapture -%}

{%- capture model_api_link -%}
[ChunkFilterer](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/chunker/ChunkFilterer.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[ChunkFilterer](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/chunker/chunker_filterer/index.html#sparknlp_jsl.annotator.chunker.chunker_filterer.ChunkFilterer)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[ChunkFiltererNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ChunkFilterer.ipynb)
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
