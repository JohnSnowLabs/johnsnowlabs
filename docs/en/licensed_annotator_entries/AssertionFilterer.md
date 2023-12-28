{%- capture model -%}
model
{%- endcapture -%}

{%- capture title -%}
AssertionFilterer
{%- endcapture -%}

{%- capture model_description -%}
Filters entities coming from ASSERTION type annotations and returns the CHUNKS.
Filters can be set via a white list on the extracted chunk, the assertion or a regular expression.
White list for assertion is enabled by default. To use chunk white list, `criteria` has to be set to `"isin"`.
For regex, `criteria` has to be set to `"regex"`.

Parameters:

- `whiteList`: (list) If defined, list of entities to process. The rest will be ignored.

- `CaseSensitive`: (bool) Determines whether the definitions of the white listed entities are case sensitive.

- `regex`: (list) List of dash-separated pairs of named entities.

- `criteria`: (list)  Set tag representing what is the criteria to filter the chunks. possibles values (assertion,isIn,regex). *assertion*: Filter by the assertion, *isIn* : Filter by the chunk, *regex* : Filter using a regex.

- `entitiesConfidence`: (Str) Entity pairs to remove based on the confidence level.
{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, CHUNK, ASSERTION
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}


{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical 

# Annotator that transforms a text column from dataframe into an Annotation ready for NLP
documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

# Sentence Detector annotator, processes various sentences per line
sentenceDetector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

# Tokenizer splits words in a relevant format for NLP
tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

# Clinical word embeddings trained on PubMED dataset
word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_ner = medical.NerModel.pretrained("ner_clinical", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")\
    #.setIncludeAllConfidenceScores(False)

ner_converter = medical.NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")\
    .setWhiteList(["PROBLEM", "TEST","TREATMENT"])

clinical_assertion = medical.AssertionDLModel.pretrained("assertion_jsl", "en", "clinical/models") \
    .setInputCols(["sentence", "ner_chunk", "embeddings"]) \
    .setOutputCol("assertion")

assertion_filterer = medical.AssertionFilterer()\
    .setInputCols("sentence","ner_chunk","assertion")\
    .setOutputCol("assertion_filtered")\
    .setCaseSensitive(False)\
    .setWhiteList(["Present"])
#or .setBlackList([["absent"]])

nlpPipeline = nlp.Pipeline(stages=[
      documentAssembler,
      sentenceDetector,
      tokenizer,
      word_embeddings,
      clinical_ner,
      ner_converter,
      clinical_assertion,
      assertion_filterer
    ])

data = spark.createDataFrame([["Patient has a headache for the last 2 weeks, needs to get a head CT, and appears anxious when she walks fast. Alopecia noted. She denies pain."]]).toDF("text")

result = nlpPipeline.fit(data).transform(data)

# Show results:

result.selectExpr("ner_chunk.result as ner_chunk", "assertion.result as assertion").show(3, truncate=False)
+------------------------------------------------+--------------------------------------------------+
|ner_chunk                                       |assertion                                         |
+------------------------------------------------+--------------------------------------------------+
|[a headache, a head CT, anxious, Alopecia, pain]|[Present, Hypothetical, Possible, Present, Absent]|
+------------------------------------------------+--------------------------------------------------+

result.select("filtered.result").show(3, truncate=False)
+----------------------+
|result                |
+----------------------+
|[a headache, Alopecia]|
+----------------------+

{%- endcapture -%}

{%- capture model_python_legal -%}

from johnsnowlabs import nlp, legal 

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings_ner = nlp.RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base", "en") \
    .setInputCols("sentence", "token") \
    .setOutputCol("embeddings_ner")\

ner_model = legal.NerModel.pretrained('legner_contract_doc_parties', 'en', 'legal/models')\
    .setInputCols(["sentence", "token", "embeddings_ner"])\
    .setOutputCol("ner")

ner_converter = nlp.NerConverter()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DOC", "EFFDATE", "PARTY"])

embeddings_ass = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings_ass")

assertion = legal.AssertionDLModel.pretrained("legassertion_time", "en", "legal/models")\
    .setInputCols(["sentence", "ner_chunk", "embeddings_ass"]) \
    .setOutputCol("assertion")

assertion_filterer = legal.AssertionFilterer()\
    .setInputCols("sentence","ner_chunk","assertion")\
    .setOutputCol("assertion_filtered")\
    .setCaseSensitive(False)\
    .setWhiteList(["Present"])


nlpPipeline = nlp.Pipeline(stages=[
            document_assembler,
            sentence_detector,
            tokenizer,
            embeddings_ner,
            ner_model,
            ner_converter,
            embeddings_ass,
            assertion,
            assertion_filterer
            ])

data = spark.createDataFrame([["This is an Intellectual Property Agreement between Amazon Inc. and Atlantic Inc."]]).toDF("text")

# Show results

result = nlpPipeline.fit(data).transform(data)
result.selectExpr("ner_chunk.result as ner_chunk", "assertion.result as assertion").show(3, truncate=False)
+-----------------------------------------------------------+---------------------------+
|ner_chunk                                                  |assertion                  |
+-----------------------------------------------------------+---------------------------+
|[Intellectual Property Agreement, Amazon Inc, Atlantic Inc]|[PRESENT, PRESENT, PRESENT]|
+-----------------------------------------------------------+---------------------------+

result.select("assertion_filtered.result").show(3, truncate=False)
+-----------------------------------------------------------+
|result                                                     |
+-----------------------------------------------------------+
|[Intellectual Property Agreement, Amazon Inc, Atlantic Inc]|
+-----------------------------------------------------------+

{%- endcapture -%}

{%- capture model_python_finance -%}

from johnsnowlabs import nlp, finance 

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector =  nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer =  nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings =  nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

ner_model = finance.NerModel.pretrained("finner_orgs_prods_alias","en","finance/models")\
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")\

ner_converter = finance.NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")\

assertion = finance.AssertionDLModel.pretrained("finassertion_competitors", "en", "finance/models")\
    .setInputCols(["sentence", "ner_chunk", "embeddings"]) \
    .setOutputCol("assertion")

assertion_filterer = finance.AssertionFilterer()\
    .setInputCols("sentence","ner_chunk","assertion")\
    .setOutputCol("assertion_filtered")\
    .setCaseSensitive(False)\
    .setWhiteList(["Competitor"])

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    sentence_detector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter,
    assertion,
    assertion_filterer
    ])

data = spark.createDataFrame([["Our competitors include the following by general category: legacy antivirus product providers, such as McAfee LLC and Broadcom Inc."]]).toDF("text")

# Show results

result = pipeline.fit(data).transform(data)
result.selectExpr("ner_chunk.result as ner_chunk", "assertion.result as assertion").show(3, truncate=False)
+--------------------------+------------------------+
|ner_chunk                 |assertion               |
+--------------------------+------------------------+
|[McAfee LLC, Broadcom Inc]|[COMPETITOR, COMPETITOR]|
+--------------------------+------------------------+

result.select("assertion_filtered.result").show(3, truncate=False)
+--------------------------+
|result                    |
+--------------------------+
|[McAfee LLC, Broadcom Inc]|
+--------------------------+

{%- endcapture -%}

{%- capture model_scala_medical -%}
import spark.implicits._

// Annotator that transforms a text column from dataframe into an Annotation ready for NLP
val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

// Sentence Detector annotator, processes various sentences per line
val sentenceDetector = new SentenceDetector()
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

// Tokenizer splits words in a relevant format for NLP
val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

// Clinical word embeddings trained on PubMED dataset
val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val clinical_ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models") 
    .setInputCols(Array("sentence", "token", "embeddings")) 
    .setOutputCol("ner")
    //.setIncludeAllConfidenceScores(false)

val ner_converter = new NerConverterInternal() 
    .setInputCols(Array("sentence", "token", "ner")) 
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("PROBLEM", "TEST","TREATMENT"))

val clinical_assertion = AssertionDLModel.pretrained("assertion_jsl", "en", "clinical/models") 
    .setInputCols(Array("sentence", "ner_chunk", "embeddings")) 
    .setOutputCol("assertion")

val assertion_filterer = AssertionFilterer()
    .setInputCols("sentence","ner_chunk","assertion")
    .setOutputCol("assertion_filtered")
    .setCaseSensitive(false)
    .setWhiteList(Array("Present"))
//or .setBlackList(Array("absent"))

val nlpPipeline = new Pipeline().setStages(Array(
      documentAssembler,
      sentenceDetector,
      tokenizer,
      word_embeddings,
      clinical_ner,
      ner_converter,
      clinical_assertion,
      assertion_filterer
))

import spark.implicits._

val text ="""Patient has a headache for the last 2 weeks, needs to get a head CT, and appears anxious when she walks fast. Alopecia noted. She denies pain."""

val data = Seq(text).toDF("text")
val result = nlpPipeline.fit(data).transform(data)

// Show results:

+------------------------------------------------+--------------------------------------------------+
|ner_chunk                                       |assertion                                         |
+------------------------------------------------+--------------------------------------------------+
|[a headache, a head CT, anxious, Alopecia, pain]|[Present, Hypothetical, Possible, Present, Absent]|
+------------------------------------------------+--------------------------------------------------+

result.select("filtered.result").show(3, truncate=false)
+----------------------+
|result                |
+----------------------+
|[a headache, Alopecia]|
+----------------------+

{%- endcapture -%}

{%- capture model_scala_legal -%}
import spark.implicits._

// Annotator that transforms a text column from dataframe into an Annotation ready for NLP
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

// Sentence Detector annotator, processes various sentences per line
val sentence_detector = new SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

// Tokenizer splits words in a relevant format for NLP
val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

// Clinical word embeddings trained on PubMED dataset
val embeddings_ner = RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base", "en")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings_ner")

val ner_model = LegalNerModel.pretrained('legner_contract_doc_parties', 'en', 'legal/models') 
    .setInputCols(Array("sentence", "token", "embeddings_ner")) 
    .setOutputCol("ner")
    //.setIncludeAllConfidenceScores(false)

val ner_converter = new NerConverterInternal() 
    .setInputCols(Array("sentence", "token", "ner")) 
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("DOC", "EFFDATE", "PARTY"))

val embeddings_ass = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") 
    .setInputCols(Array("sentence", "token")) 
    .setOutputCol("embeddings_ass")

val assertion = AssertionDLModel.pretrained("assertion_jsl", "en", "clinical/models") 
    .setInputCols(Array("sentence", "ner_chunk", "embeddings_ass")) 
    .setOutputCol("assertion")

val assertion_filterer = AssertionFilterer()
    .setInputCols("sentence","ner_chunk","assertion")
    .setOutputCol("assertion_filtered")
    .setCaseSensitive(false)
    .setWhiteList(Array("Present"))


val nlpPipeline = new Pipeline().setStages(Array(
      document_assembler,
      sentence_detector,
      tokenizer,
      embeddings_ner,
      ner_model,
      ner_converter,
      embeddings_ass,
      assertion,
      assertion_filterer
))

import spark.implicits._

val text ="""This is an Intellectual Property Agreement between Amazon Inc. and Atlantic Inc."""

val data = Seq(text).toDF("text")
val result = nlpPipeline.fit(data).transform(data)

// Show results:
+-----------------------------------------------------------+---------------------------+
|ner_chunk                                                  |assertion                  |
+-----------------------------------------------------------+---------------------------+
|[Intellectual Property Agreement, Amazon Inc, Atlantic Inc]|[PRESENT, PRESENT, PRESENT]|
+-----------------------------------------------------------+---------------------------+

result.select("filtered.result").show(3, truncate=false)
+-----------------------------------------------------------+
|result                                                     |
+-----------------------------------------------------------+
|[Intellectual Property Agreement, Amazon Inc, Atlantic Inc]|
+-----------------------------------------------------------+

{%- endcapture -%}

{%- capture model_scala_finance -%}
import spark.implicits._

// Annotator that transforms a text column from dataframe into an Annotation ready for NLP
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

// Sentence Detector annotator, processes various sentences per line
val sentence_detector = new SentenceDetector()
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

// Tokenizer splits words in a relevant format for NLP
val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

// Clinical word embeddings trained on PubMED dataset
val embeddings = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = FinanceNerModel.pretrained("finner_orgs_prods_alias","en","finance/models") 
    .setInputCols(Array("sentence", "token", "embeddings")) 
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal() 
    .setInputCols(Array("sentence", "token", "ner")) 
    .setOutputCol("ner_chunk")

val assertion = AssertionDLModel.pretrained("finassertion_competitors", "en", "finance/models") 
    .setInputCols(Array("sentence", "ner_chunk", "embeddings")) 
    .setOutputCol("assertion")

val assertion_filterer = AssertionFilterer()
    .setInputCols("sentence","ner_chunk","assertion")
    .setOutputCol("assertion_filtered")
    .setCaseSensitive(false)
    .setWhiteList(Array("Competitor"))


val nlpPipeline = new Pipeline().setStages(Array(
        document_assembler,
        sentence_detector,
        tokenizer,
        embeddings,
        ner_model,
        ner_converter,
        assertion,
        assertion_filterer
))

import spark.implicits._

val text ="""Our competitors include the following by general category: legacy antivirus product providers, such as McAfee LLC and Broadcom Inc."""

val data = Seq(text).toDF("text")
val result = nlpPipeline.fit(data).transform(data)

// Show results:
+--------------------------+------------------------+
|ner_chunk                 |assertion               |
+--------------------------+------------------------+
|[McAfee LLC, Broadcom Inc]|[COMPETITOR, COMPETITOR]|
+--------------------------+------------------------+

result.select("filtered.result").show(3, truncate=false)
+--------------------------+
|result                    |
+--------------------------+
|[McAfee LLC, Broadcom Inc]|
+--------------------------+

{%- endcapture -%}

{%- capture model_api_link -%}
[AssertionFilterer](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/chunker/AssertionFilterer.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[AssertionFilterer](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/chunker/assertion_filterer/index.html#sparknlp_jsl.annotator.chunker.assertion_filterer.AssertionFilterer)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[AssertionFiltererNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/AssertionFilterer.ipynb)
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
