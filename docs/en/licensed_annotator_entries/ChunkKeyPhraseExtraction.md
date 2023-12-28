{%- capture title -%}
ChunkKeyPhraseExtraction
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
Chunk KeyPhrase Extraction uses Bert Sentence Embeddings to determine the most relevant key phrases describing a text. 
The input to the model consists of chunk annotations and sentence or document annotation. The model compares the chunks  against the corresponding sentences/documents and selects the chunks which are most representative of the broader text context (i.e. the document or the sentence they belong to). The key phrases candidates (i.e. the input chunks) can be  generated in various ways, e.g. by NGramGenerator, TextMatcher or NerConverter. The model operates either at sentence (selecting the most descriptive chunks from the sentence they belong to) or at document level. In the latter case, the key phrases are selected to represent all the input document annotations.

Parametres:

- `setConcatenateSentences(value: Boolean)`: Concatenate the input sentence/documentation annotations before computing their embedding Default value is 'true'.

- `setDivergence(value: Float)`: Set the level of divergence of the extracted key phrases.

- `setDocumentLevelProcessing(value: Boolean)`: Extract key phrases from the whole document (true) or from particular sentences which the chunks refer to (false) Default value is 'true'.

- `setDropPunctuation(value: Boolean)`: Remove punctuation marks from input chunks.

- `setSelectMostDifferent(value: Boolean)`: Let the model return the top N key phrases which are the most different from each other.

- `setTopN(value: Int)`: Set the number of key phrases to extract.

This model is a subclass of [[BertSentenceEmbeddings]] and shares all parameters with it. It can load any pretrained BertSentenceEmbeddings model. Available models can be found at the [Models Hub](https://nlp.johnsnowlabs.com/models?task=Sentence+Embeddings).

{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

documenter = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

sentencer = nlp.SentenceDetector() \
    .setInputCols(["document"])\
    .setOutputCol("sentences")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("tokens") \

embeddings = nlp.WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models") \
    .setInputCols(["document", "tokens"]) \
    .setOutputCol("embeddings")

ner_tagger = medical.NerModel().pretrained("ner_jsl_slim", "en", "clinical/models") \
    .setInputCols(["sentences", "tokens", "embeddings"]) \
    .setOutputCol("ner_tags")

ner_converter = nlp.NerConverter()\
    .setInputCols("sentences", "tokens", "ner_tags")\
    .setOutputCol("ner_chunks")

key_phrase_extractor = medical.ChunkKeyPhraseExtraction.pretrained()\
    .setTopN(1)\
    .setDocumentLevelProcessing(False)\
    .setDivergence(0.4)\
    .setInputCols(["sentences", "ner_chunks"])\
    .setOutputCol("ner_chunk_key_phrases")

pipeline = nlp.Pipeline(stages=[
    documenter, 
    sentencer, 
    tokenizer, 
    embeddings, 
    ner_tagger, 
    ner_converter,
    key_phrase_extractor])

data = spark.createDataFrame([["Her Diabetes has become type 2 in the last year with her Diabetes.He complains of swelling in his right forearm."]]).toDF("text")
results = pipeline.fit(data).transform(data)

results.selectExpr("explode(ner_chunk_key_phrases) AS key_phrase")\
       .selectExpr("key_phrase.result",
                   "key_phrase.metadata.entity",
                   "key_phrase.metadata.DocumentSimilarity",
                   "key_phrase.metadata.MMRScore").show(truncate=False)

+--------+-------------------------+------------------+-----------------+
|result  |entity                   |DocumentSimilarity|MMRScore         |
+--------+-------------------------+------------------+-----------------+
|Diabetes|Disease_Syndrome_Disorder|0.66827321499841  |0.400963944931921|
+--------+-------------------------+------------------+-----------------+
{%- endcapture -%}

{%- capture model_python_legal -%}
from johnsnowlabs import nlp, legal

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")
        
sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

ner_model = legal.NerModel.pretrained("legner_orgs_prods_alias","en","legal/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = nlp.NerConverter()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")

key_phrase_extractor = legal.ChunkKeyPhraseExtraction\
    .pretrained()\
    .setTopN(1)\
    .setDocumentLevelProcessing(False)\
    .setDivergence(0.4)\
    .setInputCols(["sentence", "ner_chunk"])\
    .setOutputCol("ner_chunk_key_phrases")

nlpPipeline = nlp.Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter,
    key_phrase_extractor])

text = ["""This INTELLECTUAL PROPERTY AGREEMENT (this "Agreement"), dated as of December 31, 2018 (the "Effective Date") is entered into by and between Armstrong Flooring, Inc., a Delaware corporation ("Seller") and AFI Licensing LLC, a Delaware limited liability company ("Licensing" and together with Seller, "Arizona") and AHF Holding, Inc. (formerly known as Tarzan HoldCo, Inc.), a Delaware corporation ("Buyer") and Armstrong Hardwood Flooring Company, a Tennessee corporation (the "Company" and together with Buyer the "Buyer Entities") (each of Arizona on the one hand and the Buyer Entities on the other hand, a "Party" and collectively, the "Parties").
"""]

data = spark.createDataFrame([text]).toDF("text")
result = nlpPipeline.fit(data).transform(data)

result.selectExpr("explode(ner_chunk_key_phrases) AS key_phrase")\
      .selectExpr("key_phrase.result",
                  "key_phrase.metadata.entity",
                  "key_phrase.metadata.DocumentSimilarity",
                  "key_phrase.metadata.MMRScore").show(truncate=False)

+--------------+------+------------------+-------------------+
|result        |entity|DocumentSimilarity|MMRScore           |
+--------------+------+------------------+-------------------+
|Buyer Entities|ALIAS |0.5680936022739617|0.34085617490878395|
+--------------+------+------------------+-------------------+
{%- endcapture -%}

{%- capture model_python_finance -%}
from johnsnowlabs import nlp, finance

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")
        
sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

ner_model = finance.NerModel.pretrained("finner_orgs_prods_alias","en","finance/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = nlp.NerConverter()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")

key_phrase_extractor = finance.ChunkKeyPhraseExtraction\
    .pretrained()\
    .setTopN(1)\
    .setDocumentLevelProcessing(False)\
    .setDivergence(0.4)\
    .setInputCols(["sentence", "ner_chunk"])\
    .setOutputCol("ner_chunk_key_phrases")

nlpPipeline = nlp.Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter,
    key_phrase_extractor])

text = ["""In 2020, we acquired certain assets of Spell Security Private Limited (also known as "Spell Security"). More specifically, their Compliance product - Policy Compliance (PC)")."""]

data = spark.createDataFrame([text]).toDF("text")
result = nlpPipeline.fit(data).transform(data)

result.selectExpr("explode(ner_chunk_key_phrases) AS key_phrase")\
      .selectExpr("key_phrase.result",
                  "key_phrase.metadata.entity",
                  "key_phrase.metadata.DocumentSimilarity",
                  "key_phrase.metadata.MMRScore").show(truncate=False)

+------------------------------+-------+------------------+-------------------+
|result                        |entity |DocumentSimilarity|MMRScore           |
+------------------------------+-------+------------------+-------------------+
|Policy Compliance             |PRODUCT|0.6446724461374882|0.38680348305268175|
|Spell Security Private Limited|ORG    |0.6282153013401193|0.3769291957818915 |
+------------------------------+-------+------------------+-------------------+
{%- endcapture -%}

{%- capture model_scala_medical -%}
import spark.implicits._

val documenter = new DocumentAssembler()
  .setInputCol("text") 
  .setOutputCol("document") 

val sentencer = new SentenceDetector()
  .setInputCols(Array("document")) 
  .setOutputCol("sentences") 

val tokenizer = new Tokenizer()
  .setInputCols(Array("document")) 
  .setOutputCol("tokens") 

val embeddings = WordEmbeddingsModel
  .pretrained("embeddings_clinical","en","clinical/models") 
  .setInputCols(Array("document","tokens")) 
  .setOutputCol("embeddings") 

val ner_tagger = MedicalNerModel.pretrained("ner_jsl_slim","en","clinical/models") 
  .setInputCols(Array("sentences","tokens","embeddings")) 
  .setOutputCol("ner_tags") 
 
val ner_converter = new NerConverter()
  .setInputCols("sentences","tokens","ner_tags") 
  .setOutputCol("ner_chunks") 

val key_phrase_extractor = ChunkKeyPhraseExtraction.pretrained()
  .setTopN(1) 
  .setDocumentLevelProcessing(false) 
  .setDivergence(0.4) 
  .setInputCols(Array("sentences","ner_chunks")) 
  .setOutputCol("ner_chunk_key_phrases") 

val pipeline = new Pipeline().setStages(Array( 
  documenter, 
  sentencer, 
  tokenizer, 
  embeddings, 
  ner_tagger, 
  ner_converter, 
  key_phrase_extractor)) 

val text ="""Her Diabetes has become type 2 in the last year with her Diabetes.He complains of swelling in his right forearm."""
val data = Seq(text).toDF("text")

val results = pipeline.fit(data).transform(data)

+--------+-------------------------+------------------+-----------------+
|result  |entity                   |DocumentSimilarity|MMRScore         |
+--------+-------------------------+------------------+-----------------+
|Diabetes|Disease_Syndrome_Disorder|0.66827321499841  |0.400963944931921|
+--------+-------------------------+------------------+-----------------+
{%- endcapture -%}

{%- capture model_scala_legal -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text") 
  .setOutputCol("document") 

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
  .setInputCols(Array("document") ) 
  .setOutputCol("sentence") 

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence")) 
  .setOutputCol("token") 

val embeddings = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en")
  .setInputCols(Array("sentence","token")) 
  .setOutputCol("embeddings") 

val ner_model = LegalNerModel.pretrained("legner_orgs_prods_alias","en","legal/models")
  .setInputCols(Array("sentence","token","embeddings")) 
  .setOutputCol("ner") 

val ner_converter = new NerConverter()
  .setInputCols(Array("sentence","token","ner")) 
  .setOutputCol("ner_chunk") 

val key_phrase_extractor = ChunkKeyPhraseExtraction.pretrained() 
  .setTopN(1) 
  .setDocumentLevelProcessing(false) 
  .setDivergence(0.4) 
  .setInputCols(Array("sentence","ner_chunk")) 
  .setOutputCol("ner_chunk_key_phrases")

val nlpPipeline = new Pipeline().setStages(Array( 
  documentAssembler, 
  sentenceDetector, 
  tokenizer, 
  embeddings, 
  ner_model, n
  er_converter, 
  key_phrase_extractor) ) 

val text ="""This INTELLECTUAL PROPERTY AGREEMENT (this "Agreement"), dated as of December 31, 2018 (the "Effective Date") is entered into by and between Armstrong Flooring, Inc., a Delaware corporation ("Seller") and AFI Licensing LLC, a Delaware limited liability company ("Licensing" and together with Seller, "Arizona") and AHF Holding, Inc. (formerly known as Tarzan HoldCo, Inc.), a Delaware corporation ("Buyer") and Armstrong Hardwood Flooring Company, a Tennessee corporation (the "Company" and together with Buyer the "Buyer Entities") (each of Arizona on the one hand and the Buyer Entities on the other hand, a "Party" and collectively, the "Parties")."""
val data = Seq(text).toDF("text")

val result = nlpPipeline.fit(data).transform(data)

+--------------+------+------------------+-------------------+
|result        |entity|DocumentSimilarity|MMRScore           |
+--------------+------+------------------+-------------------+
|Buyer Entities|ALIAS |0.5680936022739617|0.34085617490878395|
+--------------+------+------------------+-------------------+
{%- endcapture -%}

{%- capture model_scala_finance -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text") 
  .setOutputCol("document") 

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
  .setInputCols(Array("document") ) 
  .setOutputCol("sentence") 

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence")) 
  .setOutputCol("token") 

val embeddings = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en")
  .setInputCols(Array("sentence","token")) 
  .setOutputCol("embeddings") 

val ner_model = FinanceNerModel.pretrained("finner_orgs_prods_alias","en","finance/models")
  .setInputCols(Array("sentence","token","embeddings")) 
  .setOutputCol("ner") 

val ner_converter = new NerConverter()
  .setInputCols(Array("sentence","token","ner")) 
  .setOutputCol("ner_chunk") 

val key_phrase_extractor = ChunkKeyPhraseExtraction.pretrained() 
  .setTopN(1) 
  .setDocumentLevelProcessing(false) 
  .setDivergence(0.4) 
  .setInputCols(Array("sentence","ner_chunk")) 
  .setOutputCol("ner_chunk_key_phrases")

val nlpPipeline = new Pipeline().setStages(Array( 
  documentAssembler, 
  sentenceDetector, 
  tokenizer, 
  embeddings, 
  ner_model, n
  er_converter, 
  key_phrase_extractor) ) 

val text ="""In 2020, we acquired certain assets of Spell Security Private Limited (also known as "Spell Security"). More specifically, their Compliance product - Policy Compliance (PC)."""
val data = Seq(text).toDF("text")

val result = nlpPipeline.fit(data).transform(data)

+------------------------------+-------+------------------+-------------------+
|result                        |entity |DocumentSimilarity|MMRScore           |
+------------------------------+-------+------------------+-------------------+
|Policy Compliance             |PRODUCT|0.6446724461374882|0.38680348305268175|
|Spell Security Private Limited|ORG    |0.6282153013401193|0.3769291957818915 |
+------------------------------+-------+------------------+-------------------+
{%- endcapture -%}

{%- capture model_api_link -%}
[ChunkKeyPhraseExtraction](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/chunker/ChunkKeyPhraseExtraction.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[ChunkKeyPhraseExtraction](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/chunker/chunk_key_phrase_extraction/index.html#sparknlp_jsl.annotator.chunker.chunk_key_phrase_extraction.ChunkKeyPhraseExtraction)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[ChunkKeyPhraseExtractionNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ChunkKeyPhraseExtraction.ipynb)
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
