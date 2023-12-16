{%- capture title -%}
AssertionChunkConverter
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}

This annotator creates a `CHUNK` column with metadata useful for training an Assertion Status Detection model (see [AssertionDL](https://nlp.johnsnowlabs.com/docs/en/licensed_annotators#assertiondl)).

In some cases, there may be issues while creating the chunk column when using token indices that can lead to loss of data to train assertion status models.

The `AssertionChunkConverter` annotator uses both the begin and end indices of the tokens as input to add more robust metadata to the chunk column in a way that improves the reliability of the indices and avoids loss of data.

AssertionChunkConverter Parameters:

- `chunkBeginCol`: (Str) The column containing the start index of the chunk.

- `chunkEndCol`: (Str) The column containing the end index of the chunk.

- `chunkTextCol`: (Str) The column containing the text chunk.

- `outputTokenBeginCol`: (Str)  The column containing the selected token start.

- `outputTokenEndCol`: (Str) The column containing the selected token end index.

> *NOTE*: Chunk begin and end indices in the assertion status model training dataframe can be populated using the new version of the ALAB module.

{%- endcapture -%}

{%- capture model_input_anno -%}
TOKEN
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_python_medical -%}

document_assembler = nlp.DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
  .setInputCols(["sentence"])\
  .setOutputCol("tokens")

converter = medical.AssertionChunkConverter()\
  .setInputCols("tokens")\
  .setChunkTextCol("target")\
  .setChunkBeginCol("char_begin")\
  .setChunkEndCol("char_end")\
  .setOutputTokenBeginCol("token_begin")\
  .setOutputTokenEndCol("token_end")\
  .setOutputCol("chunk")


pipeline = nlp.Pipeline().setStages(
    [document_assembler, 
     sentenceDetector, 
     tokenizer, 
     converter]
)

data = spark.createDataFrame([
    ["An angiography showed bleeding in two vessels off of the Minnie supplying the sigmoid that were succesfully embolized.","Minnie", 57, 64,],
    ["After discussing this with his PCP, Leon was clear that the patient had had recurrent DVTs and ultimately a PE and his PCP felt strongly that he required long-term anticoagulation","PCP",31,34,],
]).toDF("text", "target", "char_begin", "char_end")

results = pipeline.fit(data).transform(data)

results.selectExpr(
    "target",
    "char_begin",
    "char_end",
    "token_begin",
    "token_end",
    "tokens[token_begin].result",
    "tokens[token_end].result",
    "target",
    "chunk",
).show(truncate=False)

+------+----------+--------+-----------+---------+--------------------------+------------------------+------+----------------------------------------------+
|target|char_begin|char_end|token_begin|token_end|tokens[token_begin].result|tokens[token_end].result|target|chunk                                         |
+------+----------+--------+-----------+---------+--------------------------+------------------------+------+----------------------------------------------+
|Minnie|57        |64      |10         |10       |Minnie                    |Minnie                  |Minnie|[{chunk, 57, 62, Minnie, {sentence -> 0}, []}]|
|PCP   |31        |34      |5          |5        |PCP                       |PCP                     |PCP   |[{chunk, 31, 33, PCP, {sentence -> 0}, []}]   |
+------+----------+--------+-----------+---------+--------------------------+------------------------+------+----------------------------------------------+

{%- endcapture -%}

{%- capture model_scala_medical -%}
 
val document_assembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("tokens")

val converter = new AssertionChunkConverter()
  .setInputCols("tokens")
  .setOutputCol("chunk")
  .setChunkTextCol("target")
  .setChunkBeginCol("char_begin")
  .setChunkEndCol("char_end")
  .setOutputTokenBeginCol("token_begin")
  .setOutputTokenEndCol("token_end")

val pipeline = new Pipeline().setStages(Array(document_assembler, sentenceDetector, tokenizer, converter))

val data = Seq(Array(
    ("An angiography showed bleeding in two vessels off of the Minnie supplying the sigmoid that were succesfully embolized.", "Minnie",57,64,),
    ("After discussing this with his PCP, Leon was clear that the patient had had recurrent DVTs and ultimately a PE and his PCP felt strongly that he required long-term anticoagulation", "PCP", 31, 34,)
)).toDF("text", "target", "char_begin", "char_end")

val results = pipeline.fit(data).transform(data)

results.selectExpr(
  "target",
  "char_begin",
  "char_end",
  "token_begin",
  "token_end",
  "chunk.begin",
  "chunk.end",
  "tokens[token_begin].result as begin_result",
  "tokens[token_end].result as end_result",
  "chunk.result"
).show(false)

+------+----------+--------+-----------+---------+--------------------------+------------------------+------+----------------------------------------------+
|target|char_begin|char_end|token_begin|token_end|tokens[token_begin].result|tokens[token_end].result|target|chunk                                         |
+------+----------+--------+-----------+---------+--------------------------+------------------------+------+----------------------------------------------+
|Minnie|57        |64      |10         |10       |Minnie                    |Minnie                  |Minnie|[{chunk, 57, 62, Minnie, {sentence -> 0}, []}]|
|PCP   |31        |34      |5          |5        |PCP                       |PCP                     |PCP   |[{chunk, 31, 33, PCP, {sentence -> 0}, []}]   |
+------+----------+--------+-----------+---------+--------------------------+------------------------+------+----------------------------------------------+

{%- endcapture -%}

{%- capture model_python_finance -%}

document_assembler = nlp.DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
  .setInputCols(["sentence"])\
  .setOutputCol("tokens")

converter = finance.AssertionChunkConverter()\
  .setInputCols("tokens")\
  .setChunkTextCol("target")\
  .setChunkBeginCol("char_begin")\
  .setChunkEndCol("char_end")\
  .setOutputTokenBeginCol("token_begin")\
  .setOutputTokenEndCol("token_end")\
  .setOutputCol("chunk")


pipeline = nlp.Pipeline().setStages(
    [document_assembler, 
     sentenceDetector, 
     tokenizer, 
     converter]
)

data = spark.createDataFrame([
    ["Tom Martin worked as Cadence's CTO until 2010","Cadence's CTO",21,33],
    ["Mrs. Charles was before Managing Director at a big consultancy company","Managing Director",24,40],
]).toDF("text", "target", "char_begin", "char_end")

results = pipeline.fit(data).transform(data)

results.selectExpr(
    "target",
    "char_begin",
    "char_end",
    "token_begin",
    "token_end",
    "tokens[token_begin].result",
    "tokens[token_end].result",
    "target",
    "chunk",
).show(truncate=False)

+-----------------+----------+--------+-----------+---------+--------------------------+------------------------+-----------------+---------------------------------------------------------+
|target           |char_begin|char_end|token_begin|token_end|tokens[token_begin].result|tokens[token_end].result|target           |chunk                                                    |
+-----------------+----------+--------+-----------+---------+--------------------------+------------------------+-----------------+---------------------------------------------------------+
|Cadence's CTO    |21        |33      |4          |4        |Cadence's                 |Cadence's               |Cadence's CTO    |[{chunk, 21, 29, Cadence's CTO, {sentence -> 0}, []}]    |
|Managing Director|24        |40      |5          |5        |Managing                  |Managing                |Managing Director|[{chunk, 24, 31, Managing Director, {sentence -> 0}, []}]|
+-----------------+----------+--------+-----------+---------+--------------------------+------------------------+-----------------+---------------------------------------------------------+

{%- endcapture -%}

{%- capture model_scala_finance -%}
 
val document_assembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("tokens")

val converter = new AssertionChunkConverter()
  .setInputCols("tokens")
  .setOutputCol("chunk")
  .setChunkTextCol("target")
  .setChunkBeginCol("char_begin")
  .setChunkEndCol("char_end")
  .setOutputTokenBeginCol("token_begin")
  .setOutputTokenEndCol("token_end")

val pipeline = new Pipeline().setStages(Array(document_assembler, sentenceDetector, tokenizer, converter))

val data = Seq(Array(
    ("Tom Martin worked as Cadence's CTO until 2010","Cadence's CTO",21,33,),
    ("Mrs. Charles was before Managing Director at a big consultancy company", "Managing Director",24, 40,)
)).toDF("text", "target", "char_begin", "char_end")

val results = pipeline.fit(data).transform(data)

results.selectExpr(
  "target",
  "char_begin",
  "char_end",
  "token_begin",
  "token_end",
  "chunk.begin",
  "chunk.end",
  "tokens[token_begin].result as begin_result",
  "tokens[token_end].result as end_result",
  "chunk.result"
).show(false)

+-----------------+----------+--------+-----------+---------+-----+----+------------+----------+-------------------+
|target           |char_begin|char_end|token_begin|token_end|begin|end |begin_result|end_result|result             |
+-----------------+----------+--------+-----------+---------+-----+----+------------+----------+-------------------+
|Cadence's CTO    |21        |33      |4          |4        |[21] |[29]|Cadence's   |Cadence's |[Cadence's CTO]    |
|Managing Director|24        |40      |5          |5        |[24] |[31]|Managing    |Managing  |[Managing Director]|
+-----------------+----------+--------+-----------+---------+-----+----+------------+----------+-------------------+

{%- endcapture -%}

{%- capture model_python_legal -%}

document_assembler = nlp.DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
  .setInputCols(["sentence"])\
  .setOutputCol("tokens")

converter = legal.AssertionChunkConverter()\
  .setInputCols("tokens")\
  .setChunkTextCol("target")\
  .setChunkBeginCol("char_begin")\
  .setChunkEndCol("char_end")\
  .setOutputTokenBeginCol("token_begin")\
  .setOutputTokenEndCol("token_end")\
  .setOutputCol("chunk")


pipeline = nlp.Pipeline().setStages(
    [document_assembler,
     sentenceDetector,
     tokenizer, 
     converter]
)

data = spark.createDataFrame([
    ["This Agreement may be executed by different parties hereto","parties",44,50,],
    ["The Administrative Agent will determine the Dollar Equivalent amount","Agent",19,23,],
]).toDF("text", "target", "char_begin", "char_end")

results = pipeline.fit(data).transform(data)

results.selectExpr(
    "target",
    "char_begin",
    "char_end",
    "token_begin",
    "token_end",
    "tokens[token_begin].result",
    "tokens[token_end].result",
    "target",
    "chunk",
).show(truncate=False)

+-------+----------+--------+-----------+---------+--------------------------+------------------------+-------+-----------------------------------------------+
|target |char_begin|char_end|token_begin|token_end|tokens[token_begin].result|tokens[token_end].result|target |chunk                                          |
+-------+----------+--------+-----------+---------+--------------------------+------------------------+-------+-----------------------------------------------+
|parties|44        |50      |7          |6        |parties                   |different               |parties|[{chunk, 44, 42, parties, {sentence -> 0}, []}]|
|Agent  |19        |23      |2          |1        |Agent                     |Administrative          |Agent  |[{chunk, 19, 17, Agent, {sentence -> 0}, []}]  |
+-------+----------+--------+-----------+---------+--------------------------+------------------------+-------+-----------------------------------------------+

{%- endcapture -%}

{%- capture model_scala_legal -%}

val document_assembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("tokens")

val converter = new AssertionChunkConverter()
  .setInputCols("tokens")
  .setOutputCol("chunk")
  .setChunkTextCol("target")
  .setChunkBeginCol("char_begin")
  .setChunkEndCol("char_end")
  .setOutputTokenBeginCol("token_begin")
  .setOutputTokenEndCol("token_end")

val pipeline = new Pipeline().setStages(Array(document_assembler, sentenceDetector, tokenizer, converter))

val data = Seq(Array(
    ("Tom Martin worked as Cadence's CTO until 2010","Cadence's CTO", 21,33,),
    ("Mrs. Charles was before Managing Director at a big consultancy company","Managing Director",24,40,)
)).toDF("text", "target", "char_begin", "char_end")
 
val results = pipeline.fit(data).transform(data)

results.selectExpr(
  "target",
  "char_begin",
  "char_end",
  "token_begin",
  "token_end",
  "chunk.begin",
  "chunk.end",
  "tokens[token_begin].result as begin_result",
  "tokens[token_end].result as end_result",
  "chunk.result"
).show(false)

+-------+----------+--------+-----------+---------+--------------------------+------------------------+-------+-----------------------------------------------+
|target |char_begin|char_end|token_begin|token_end|tokens[token_begin].result|tokens[token_end].result|target |chunk                                          |
+-------+----------+--------+-----------+---------+--------------------------+------------------------+-------+-----------------------------------------------+
|parties|44        |50      |7          |6        |parties                   |different               |parties|[{chunk, 44, 42, parties, {sentence -> 0}, []}]|
|Agent  |19        |23      |2          |1        |Agent                     |Administrative          |Agent  |[{chunk, 19, 17, Agent, {sentence -> 0}, []}]  |
+-------+----------+--------+-----------+---------+--------------------------+------------------------+-------+-----------------------------------------------+

{%- endcapture -%}

{%- capture model_api_link -%}
[AssertionChunkConverter](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/assertion/AssertionChunkConverter.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[AssertionChunkConverter](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/assertion/assertion_chunk_converter/index.html#sparknlp_jsl.annotator.assertion.assertion_chunk_converter.AssertionChunkConverter)
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
model_python_finance=model_python_finance
model_scala_finance=model_scala_finance
model_python_legal=model_python_legal
model_scala_legal=model_scala_legal
model_api_link=model_api_link
model_python_api_link=model_python_api_link
%}
