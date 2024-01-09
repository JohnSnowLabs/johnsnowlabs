{%- capture title -%}
NerChunker
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
Extracts phrases that fits into a known pattern using the NER tags. Useful for entity groups with neighboring tokens
when there is no pretrained NER model to address certain issues. A Regex needs to be provided to extract the tokens
between entities.

Parameter:

- `setRegexParsers`: Array of grammar based chunk parsers.   
{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, NAMED_ENTITY
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical
# Defining pipeline stages for NER

documentAssembler= nlp.DocumentAssembler() \
  .setInputCol("text") \
  .setOutputCol("document")

sentenceDetector= nlp.SentenceDetector() \
  .setInputCols(["document"]) \
  .setOutputCol("sentence") \
  .setUseAbbreviations(False)

tokenizer= nlp.Tokenizer() \
  .setInputCols(["sentence"]) \
  .setOutputCol("token")

embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models") \
  .setInputCols(["sentence","token"]) \
  .setOutputCol("embeddings") \
  .setCaseSensitive(False)

ner = medical.NerModel.pretrained("ner_radiology", "en", "clinical/models") \
  .setInputCols(["sentence","token","embeddings"]) \
  .setOutputCol("ner") \
  .setIncludeConfidence(True)

# Define the NerChunker to combine to chunks
chunker = medical.NerChunker() \
  .setInputCols(["sentence","ner"]) \
  .setOutputCol("ner_chunk") \
  .setRegexParsers(["<ImagingFindings>.*<BodyPart>"])

pipeline= nlp.Pipeline(stages=[
  documentAssembler,
  sentenceDetector,
  tokenizer,
  embeddings,
  ner,
  chunker
])

data= spark.createDataFrame([["She has cystic cyst on her kidney."]]).toDF("text")
result = pipeline.fit(data).transform(data)

# Show results:
result.selectExpr("explode(arrays_zip(ner.metadata , ner.result))")\
      .selectExpr("col['0'].word as word" , "col['1'] as ner").show(truncate=False)
+------+-----------------+
|word  |ner              |
+------+-----------------+
|She   |O                |
|has   |O                |
|cystic|B-ImagingFindings|
|cyst  |I-ImagingFindings|
|on    |O                |
|her   |O                |
|kidney|B-BodyPart       |
|.     |O                |
+------+-----------------+

result.select("ner_chunk.result").show(truncate=False)
+---------------------------+
|result                     |
+---------------------------+
|[cystic cyst on her kidney]|
+---------------------------+
{%- endcapture -%}


{%- capture model_python_legal -%}
from johnsnowlabs import nlp, legal 
# Defining pipeline stages for NER

documentAssembler= nlp.DocumentAssembler() \
  .setInputCol("text") \
  .setOutputCol("document")

sentenceDetector= nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

tokenizer= nlp.Tokenizer() \
  .setInputCols(["sentence"]) \
  .setOutputCol("token")

embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") \
  .setInputCols(["sentence", "token"]) \
  .setOutputCol("embeddings")

ner_model = legal.NerModel.pretrained("legner_org_per_role_date", "en", "legal/models")\
  .setInputCols(["sentence", "token", "embeddings"])\
  .setOutputCol("ner")

# Define the NerChunker to combine to chunks
chunker = legal.NerChunker() \
  .setInputCols(["sentence","ner"]) \
  .setOutputCol("ner_chunk") \
  .setRegexParsers(["<PERSON>.*<ROLE>"])

pipeline= nlp.Pipeline(stages=[
  documentAssembler,
  sentenceDetector,
  tokenizer,
  embeddings,
  ner_model,
  chunker
])

data= spark.createDataFrame([["""Jeffrey Preston Bezos is an American entrepreneur, founder and CEO of Amazon"""]]).toDF("text")

result = pipeline.fit(data).transform(data)

# Show results:
result.selectExpr("explode(arrays_zip(ner.metadata , ner.result))")\
      .selectExpr("col['0'].word as word" , "col['1'] as ner").show(truncate=False)

+------------+--------+
|word        |ner     |
+------------+--------+
|Jeffrey     |B-PERSON|
|Preston     |I-PERSON|
|Bezos       |I-PERSON|
|is          |O       |
|an          |O       |
|American    |O       |
|entrepreneur|O       |
|,           |O       |
|founder     |B-ROLE  |
|and         |O       |
|CEO         |B-ROLE  |
|of          |O       |
|Amazon      |B-ORG   |
+------------+--------+

result.select("ner_chunk.result").show(truncate=False)

+--------------------------------------------------------------------+
|result                                                              |
+--------------------------------------------------------------------+
|[Jeffrey Preston Bezos is an American entrepreneur, founder and CEO]|
+--------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_python_finance -%}
from johnsnowlabs import nlp, finance 
# Defining pipeline stages for NER

documentAssembler= nlp.DocumentAssembler() \
  .setInputCol("text") \
  .setOutputCol("document")

sentenceDetector= nlp.SentenceDetector() \
  .setInputCols(["document"]) \
  .setOutputCol("sentence") 

tokenizer= nlp.Tokenizer() \
  .setInputCols(["sentence"]) \
  .setOutputCol("token")\
  .setContextChars(['.', ',', ';', ':', '!', '?', '*', '-', '(', ')', '"', "'", '%', '&'])

embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base", "en") \
  .setInputCols("sentence", "token") \
  .setOutputCol("embeddings")\
  .setMaxSentenceLength(512)\
  .setCaseSensitive(True)

ner_model = finance.NerModel.pretrained("finner_responsibility_reports_md", "en", "finance/models")\
  .setInputCols(["sentence", "token", "embeddings"])\
  .setOutputCol("ner")

# Define the NerChunker to combine to chunks
chunker = finance.NerChunker() \
  .setInputCols(["sentence","ner"]) \
  .setOutputCol("ner_chunk") \
  .setRegexParsers(["<ENVIRONMENTAL_KPI>.*<AMOUNT>"])

pipeline= nlp.Pipeline(stages=[
  documentAssembler,
  sentenceDetector,
  tokenizer,
  embeddings,
  ner_model,
  chunker
])

data= spark.createDataFrame([["""The company has reduced its direct GHG emissions from 12,135 million tonnes of CO2e in 2017 to 4 million tonnes of CO2e in 2021. The indirect GHG emissions (scope 2) are mainly from imported energy, including electricity, heat, steam, and cooling, and the company has reduced its scope 2 emissions from 3 million tonnes of CO2e in 2017-2018 to 4 million tonnes of CO2e in 2020-2021. The scope 3 emissions are mainly from the use of sold products, and the emissions have increased from 377 million tonnes of CO2e in 2017 to 408 million tonnes of CO2e in 2021."""]]).toDF("text")

result = pipeline.fit(data).transform(data)

# Show results:
result.selectExpr("explode(arrays_zip(ner.metadata , ner.result))")\
      .selectExpr("col['0'].word as word" , "col['1'] as ner").show(truncate=False)

+---------+--------------------+
|word     |ner                 |
+---------+--------------------+
|The      |O                   |
|company  |O                   |
|has      |O                   |
|reduced  |O                   |
|its      |O                   |
|direct   |B-ENVIRONMENTAL_KPI |
|GHG      |I-ENVIRONMENTAL_KPI |
|emissions|I-ENVIRONMENTAL_KPI |
|from     |O                   |
|12,135   |B-AMOUNT            |
|million  |I-AMOUNT            |
|tonnes   |B-ENVIRONMENTAL_UNIT|
|of       |I-ENVIRONMENTAL_UNIT|
|CO2e     |I-ENVIRONMENTAL_UNIT|
|in       |O                   |
|2017     |B-DATE_PERIOD       |
|to       |O                   |
|4        |B-AMOUNT            |
|million  |I-AMOUNT            |
|tonnes   |B-ENVIRONMENTAL_UNIT|
+---------+--------------------+

result.select("ner_chunk.result").show(truncate=False)

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[direct GHG emissions from 12,135 million tonnes of CO2e in 2017 to 4 million, indirect GHG emissions (scope 2) are mainly from imported energy, including electricity, heat, steam, and cooling, and the company has reduced its scope 2 emissions from 3 million tonnes of CO2e in 2017-2018 to 4 million, scope 3 emissions are mainly from the use of sold products, and the emissions have increased from 377 million tonnes of CO2e in 2017 to 408 million]|
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}


{%- capture model_scala_medical -%}
import spark.implicits._

// Defining pipeline stages for NER
val data= Seq("She has cystic cyst on her kidney.").toDF("text")

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
  .setInputCols("document")
  .setOutputCol("sentence")
  .setUseAbbreviations(false)

val tokenizer = new Tokenizer()
  .setInputCols("sentence")
  .setOutputCol("token")

val embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("sentence","token"))
  .setOutputCol("embeddings")
  .setCaseSensitive(False)

val ner = MedicalNerModel.pretrained("ner_radiology", "en", "clinical/models")
  .setInputCols(Array("sentence","token","embeddings"))
  .setOutputCol("ner")
  .setIncludeConfidence(True)

// Define the NerChunker to combine to chunks
val chunker = new NerChunker()
  .setInputCols(Array("sentence","ner"))
  .setOutputCol("ner_chunk")
  .setRegexParsers(Array("<ImagingFindings>.<BodyPart>"))

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  embeddings,
  ner,
  chunker
))

val data = Seq(
  """She has cystic cyst on her kidney."""
).toDF("text")
val result = pipeline.fit(data).transform(data)

// Show results:

+------+-----------------+
|word  |ner              |
+------+-----------------+
|She   |O                |
|has   |O                |
|cystic|B-ImagingFindings|
|cyst  |I-ImagingFindings|
|on    |O                |
|her   |O                |
|kidney|B-BodyPart       |
|.     |O                |
+------+-----------------+

+---------------------------+
|result                     |
+---------------------------+
|[cystic cyst on her kidney]|
+---------------------------+
{%- endcapture -%}


{%- capture model_scala_legal -%}
import spark.implicits._
// Defining pipeline stages for NER

val documentAssembler= new DocumentAssembler() 
  .setInputCol("text") 
  .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
  .setInputCols("document")
  .setOutputCol("sentence")

val tokenizer= new Tokenizer() 
  .setInputCols("sentence") 
  .setOutputCol("token")

val embeddings = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") 
  .setInputCols(Array("sentence", "token")) 
  .setOutputCol("embeddings")

val ner_model = LegalNerModel.pretrained("legner_org_per_role_date", "en", "legal/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner")

// Define the NerChunker to combine to chunks
val chunker = new NerChunker() 
  .setInputCols(Array("sentence","ner")) 
  .setOutputCol("ner_chunk") 
  .setRegexParsers(Array("<PERSON>.*<ROLE>"))

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  embeddings,
  ner,
  chunker
))

val data = Seq(
  """Jeffrey Preston Bezos is an American entrepreneur, founder and CEO of Amazon"""
).toDF("text")
val result = pipeline.fit(data).transform(data)

// Show results:

+------------+--------+
|word        |ner     |
+------------+--------+
|Jeffrey     |B-PERSON|
|Preston     |I-PERSON|
|Bezos       |I-PERSON|
|is          |O       |
|an          |O       |
|American    |O       |
|entrepreneur|O       |
|,           |O       |
|founder     |B-ROLE  |
|and         |O       |
|CEO         |B-ROLE  |
|of          |O       |
|Amazon      |B-ORG   |
+------------+--------+


+--------------------------------------------------------------------+
|result                                                              |
+--------------------------------------------------------------------+
|[Jeffrey Preston Bezos is an American entrepreneur, founder and CEO]|
+--------------------------------------------------------------------+

{%- endcapture -%}


{%- capture model_scala_finance -%}
import spark.implicits._

// Defining pipeline stages for NER
val documentAssembler= new DocumentAssembler() 
  .setInputCol("text") 
  .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
  .setInputCols("document")
  .setOutputCol("sentence")

val tokenizer= new Tokenizer() 
  .setInputCols("sentence")
  .setOutputCol("token")

val embeddings = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") 
  .setInputCols(Array("sentence", "token")) 
  .setOutputCol("embeddings")

val ner_model = FinanceNerModel.pretrained("finner_responsibility_reports_md", "en", "finance/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner")

// Define the NerChunker to combine to chunks
val chunker = new NerChunker() 
  .setInputCols(Array("sentence","ner")) 
  .setOutputCol("ner_chunk") 
  .setRegexParsers(Array("<ENVIRONMENTAL_KPI>.*<AMOUNT>"))

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  embeddings,
  ner,
  chunker
))

val data = Seq(
  """The company has reduced its direct GHG emissions from 12,135 million tonnes of CO2e in 2017 to 4 million tonnes of CO2e in 2021. The indirect GHG emissions (scope 2) are mainly from imported energy, including electricity, heat, steam, and cooling, and the company has reduced its scope 2 emissions from 3 million tonnes of CO2e in 2017-2018 to 4 million tonnes of CO2e in 2020-2021. The scope 3 emissions are mainly from the use of sold products, and the emissions have increased from 377 million tonnes of CO2e in 2017 to 408 million tonnes of CO2e in 2021."""
).toDF("text")
val result = pipeline.fit(data).transform(data)

// Show results:

+---------+--------------------+
|word     |ner                 |
+---------+--------------------+
|The      |O                   |
|company  |O                   |
|has      |O                   |
|reduced  |O                   |
|its      |O                   |
|direct   |B-ENVIRONMENTAL_KPI |
|GHG      |I-ENVIRONMENTAL_KPI |
|emissions|I-ENVIRONMENTAL_KPI |
|from     |O                   |
|12,135   |B-AMOUNT            |
|million  |I-AMOUNT            |
|tonnes   |B-ENVIRONMENTAL_UNIT|
|of       |I-ENVIRONMENTAL_UNIT|
|CO2e     |I-ENVIRONMENTAL_UNIT|
|in       |O                   |
|2017     |B-DATE_PERIOD       |
|to       |O                   |
|4        |B-AMOUNT            |
|million  |I-AMOUNT            |
|tonnes   |B-ENVIRONMENTAL_UNIT|
+---------+--------------------+


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[direct GHG emissions from 12,135 million tonnes of CO2e in 2017 to 4 million, indirect GHG emissions (scope 2) are mainly from imported energy, including electricity, heat, steam, and cooling, and the company has reduced its scope 2 emissions from 3 million tonnes of CO2e in 2017-2018 to 4 million, scope 3 emissions are mainly from the use of sold products, and the emissions have increased from 377 million tonnes of CO2e in 2017 to 408 million]|
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}

{%- capture model_api_link -%}
[NerChunker](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/ner/NerChunker.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[NerChunker](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/ner/ner_chunker/index.html#sparknlp_jsl.annotator.ner.ner_chunker.NerChunker)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[NerChunkerNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/NerChunker.ipynb)
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
