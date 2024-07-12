{%- capture title -%}
NerDisambiguator
{%- endcapture -%}

{%- capture approach -%}
approach
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
Links words of interest, such as names of persons, locations and companies, from an input text document to
a corresponding unique entity in a target Knowledge Base (KB). Words of interest are called Named Entities (NEs),
mentions, or surface forms.
Instantiated / pretrained model of the NerDisambiguator.
Links words of interest, such as names of persons, locations and companies, from an input text document to
a corresponding unique entity in a target Knowledge Base (KB). Words of interest are called Named Entities (NEs),
mentions, or surface forms.

Parameters:

- `embeddingTypeParam`: (String) ‘bow’ for word embeddings or ‘sentence’ for sentences.

- `numFirstChars`: (Int) number of characters to be considered for initial prefix search in the knowledge base.

- `tokenSearch`: (BooleanParam) mechanism of search - by token or by - chunk in knowledge base (token is recommended ==> Default value: True).

- `narrowWithApproximateMatching`: (BooleanParam) narrow down the prefix search results with Levenshtein distance based matching (True is recommended).

- `levenshteinDistanceThresholdParam`: (Float) value of the
Levenshtein distance threshold to narrow results from prefix search (default value: 0.1).

- `nearMatchingGapParam`: (Int) allows to define a limit on the string length (by trimming the candidate chunks) during Levenshtein distance-based narrowing,  {len(candidate) - len(entity chunk) > nearMatchingGap} (default value: 4).

- `predictionsLimit`: (BooleanParam) allows to limit the number of predictions N for top N predictions.

- `s3KnowledgeBaseName`: (String) the name of the Knowledge Base name in S3.

{%- endcapture -%}

{%- capture model_input_anno -%}
CHUNK, SENTENCE_EMBEDDINGS
{%- endcapture -%}

{%- capture model_output_anno -%}
DISAMBIGUATION
{%- endcapture -%}

{%- capture model_python_medical -%}

from johnsnowlabs import nlp,  medical

documentAssembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector() \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained() \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

sentence_embeddings = nlp.SentenceEmbeddings() \
    .setInputCols(["sentence","embeddings"]) \
    .setOutputCol("sentence_embeddings")

ner_model = medical.NerModel.pretrained() \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = nlp.NerConverter() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk") \
    .setWhiteList(["PER"])

disambiguator = medical.NerDisambiguator() \
    .setS3KnowledgeBaseName("i-per") \
    .setInputCols(["ner_chunk", "sentence_embeddings"]) \
    .setOutputCol("disambiguation") \
    .setTokenSearch(False)

pipeline = nlp.Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    word_embeddings,
    sentence_embeddings,
    ner_model,
    ner_converter,
    disambiguator])

text = """The show also had a contestant named Donald Trump who later defeated Christina Aguilera ..."""

df = spark.createDataFrame([[text]]).toDF("text")
result = pipeline.fit(df).transform(df)


# Result
result.selectExpr("explode(disambiguation)") \
    .selectExpr("col.metadata.chunk as chunk", "col.result as result").show(5, truncate=False)

+------------------+------------------------------------------------------------------------------------------------------------------------+
|chunk             |result                                                                                                                  |
+------------------+------------------------------------------------------------------------------------------------------------------------+
|Donald Trump      |http://en.wikipedia.org/?curid=55907961, http://en.wikipedia.org/?curid=31698421, http://en.wikipedia.org/?curid=4848272|
|Christina Aguilera|http://en.wikipedia.org/?curid=6636454, http://en.wikipedia.org/?curid=144171                                           |
+------------------+------------------------------------------------------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_scala_medical -%}

import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text") 
  .setOutputCol("document") 

val sentenceDetector = new SentenceDetector()
  .setInputCols("document")
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols("sentence") 
  .setOutputCol("token") 

val word_embeddings = WordEmbeddingsModel.pretrained()
  .setInputCols(Array("sentence","token")) 
  .setOutputCol("embeddings") 

val sentence_embeddings = new SentenceEmbeddings()
  .setInputCols(Array("sentence","embeddings")) 
  .setOutputCol("sentence_embeddings") 

val ner_model = MedicalNerModel.pretrained()
  .setInputCols(Array("sentence","token","embeddings")) 
  .setOutputCol("ner") 

val ner_converter = new NerConverter()
  .setInputCols(Array("sentence","token","ner")) 
  .setOutputCol("ner_chunk") 
  .setWhiteList(Array("PER")) 

val disambiguator = new NerDisambiguator()
  .setS3KnowledgeBaseName("i-per") 
  .setInputCols(Array("ner_chunk","sentence_embeddings")) 
  .setOutputCol("disambiguation") 
  .setTokenSearch(false)

val pipeline = new Pipeline().setStages(Array( 
                                              documentAssembler, 
                                              sentenceDetector, 
                                              tokenizer, 
                                              word_embeddings, 
                                              sentence_embeddings, 
                                              ner_model, 
                                              ner_converter, 
                                              disambiguator))
 
val text = "The show also had a contestant named Donald Trump who later defeated Christina Aguilera ..." 

val df = Seq(text) .toDF("text") 
val result = pipeline.fit(df) .transform(df) 

// Result 

+------------------+------------------------------------------------------------------------------------------------------------------------+
|chunk             |result                                                                                                                  |
+------------------+------------------------------------------------------------------------------------------------------------------------+
|Donald Trump      |http://en.wikipedia.org/?curid=55907961, http://en.wikipedia.org/?curid=31698421, http://en.wikipedia.org/?curid=4848272|
|Christina Aguilera|http://en.wikipedia.org/?curid=6636454, http://en.wikipedia.org/?curid=144171                                           |
+------------------+------------------------------------------------------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_api_link -%}
[NerDisambiguatorModel](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/disambiguation/NerDisambiguatorModel.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[NerDisambiguatorModel](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/disambiguation/ner_disambiguator/index.html#sparknlp_jsl.annotator.disambiguation.ner_disambiguator.NerDisambiguatorModel)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[NerDisambiguatorModelNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/NerDisambiguatorModel.ipynb)
{%- endcapture -%}

{%- capture approach_description -%}
Links words of interest, such as names of persons, locations and companies, from an input text document to
a corresponding unique entity in a target Knowledge Base (KB). Words of interest are called Named Entities (NEs),
mentions, or surface forms.
The model needs extracted CHUNKS and SENTENCE_EMBEDDINGS type input from e.g.
[SentenceEmbeddings](/docs/en/annotators#sentenceembeddings) and
[NerConverter](/docs/en/annotators#nerconverter).
{%- endcapture -%}

{%- capture approach_input_anno -%}
CHUNK, SENTENCE_EMBEDDINGS
{%- endcapture -%}

{%- capture approach_output_anno -%}
DISAMBIGUATION
{%- endcapture -%}

{%- capture approach_api_link -%}
[NerDisambiguator](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/disambiguation/NerDisambiguator.html)
{%- endcapture -%}

{%- capture approach_python_api_link -%}
[NerDisambiguator](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/disambiguation/ner_disambiguator/index.html#sparknlp_jsl.annotator.disambiguation.ner_disambiguator.NerDisambiguator)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
approach=approach
model=model
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
approach_api_link=approach_api_link
approach_python_api_link=approach_python_api_link
%}
