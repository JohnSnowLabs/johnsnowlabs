{%- capture title -%}
ContextualEntityRuler
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
ContextualEntityRuler is an annotator that updates chunks based on contextual rules.
These rules are defined in the form of dictionaries and can include prefixes, suffixes, and the context within a specified scope window around the chunks.
This annotator modifies detected chunks by replacing their entity labels or content based on the patterns and rules if they match.
It is particularly useful for refining entity recognition results according to specific needs.

Parameters:

- `caseSensitive`: Whether to perform case-sensitive matching. Default is False.
- `allowPunctuationInBetween`: Whether to allow punctuation between prefix/suffix patterns and the entity. Default is True.
- `allowTokensInBetween`: Whether to allow tokens between prefix/suffix patterns and the entity. Default is False.
- `dropEmptyChunks`: If True, removes chunks with empty content after applying rules. Default is False.
- `mergeOverlapping`: If False, it returns both modified entities and the original entities at the same time. Default is True.
- `rules`: The updating rules. Each rule is a dictionary with the following keys:
  - `entity`: The target entity label to modify.  
        Example: `"AGE"`.
  - `prefixPatterns`: Array of patterns (words/phrases) to match **before the entity**.  
        Example: `["years", "old"]` matches entities preceded by "years" or "old."
  - `suffixPatterns`: Array of patterns (words/phrases) to match **after the entity**.  
        Example: `["years", "old"]` matches entities followed by "years" or "old."
  - `scopeWindowLevel`: Specifies the level of the scope window to consider.  
        Valid values: `"token"` or `"char"`. Default: `"token"`.
  - `scopeWindow`: A tuple defining the range of tokens or characters (based on `scopeWindowLevel`) to include in the scope.  
        Default for "token" level: `(2, 2)`.
        Default for "char" level: `(10,10)`
        Example: `(2, 3)` means 2 tokens/characters before and 3 after the entity are considered.
  - `prefixRegexes`: Array of regular expressions to match **before the entity**.  
        Example: `["\\b(years|months)\\b"]` matches words like "years" or "months" as prefixes.
  - `suffixRegexes`: Array of regular expressions to match **after the entity**.  
        Example: `["\\b(old|young)\\b"]` matches words like "old" or "young" as suffixes.
  - `replaceEntity`: Optional string specifying the new entity label to replace with the target entity label.  
        Example: `"MODIFIED_AGE"` replaces `"AGE"` with `"MODIFIED_AGE"` in matching cases.
  - `mode`: Specifies the operational mode for the rules. Options: `include`, `exclude`, or `replace_label_only`. Default is `include`.

  {%- endcapture -%}

{%- capture model_input_anno -%}


{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, TOKEN, CHUNK
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
    .setInputCols(["document"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models") \
    .setInputCols(["document", "token"])\
    .setOutputCol("embeddings")

jsl_ner = medical.NerModel.pretrained("ner_jsl", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("jsl_ner") 

jsl_ner_converter = medical.NerConverterInternal() \
    .setInputCols(["sentence", "token", "jsl_ner"]) \
    .setOutputCol("ner_chunks")

rules = [   {
                "entity" : "Age",
                "scopeWindow" : [15,15],
                "scopeWindowLevel"  : "char",
                "suffixPatterns" : ["years old", "year old", "months",],
                "replaceEntity" : "Modified_Age",
                "mode" : "exclude"
            },
            {
                "entity" : "Diabetes",
                "scopeWindow" : [3,3],
                "scopeWindowLevel"  : "token",
                "suffixPatterns" : ["with complications"],
                "replaceEntity" : "Modified_Diabetes",
                "mode" : "include"
            },
            {
                "entity" : "Date",
                "suffixRegexes" : ["\\d{4}"],
                "replaceEntity" : "Modified_Date",
                "mode" : "include"
            }
        ]

contextual_entity_ruler = medical.ContextualEntityRuler() \
    .setInputCols("sentence", "token", "ner_chunks") \
    .setOutputCol("ruled_ner_chunks") \
    .setRules(rules) \
    .setCaseSensitive(False)\
    .setDropEmptyChunks(True)\
    .setAllowPunctuationInBetween(True)

ruler_pipeline = nlp.Pipeline(
    stages=[
        documentAssembler,
        sentenceDetector,
        tokenizer,
        word_embeddings,
        jsl_ner,
        jsl_ner_converter,
        contextual_entity_ruler,
        flattener
    ])

empty_data = spark.createDataFrame([[""]]).toDF("text")
ruler_model = ruler_pipeline.fit(empty_data)

text ="""The Doctor assessed the 36 years old who has a history of the diabetes mellitus with complications in May, 2006"""
ruler_result = ruler_model.transform(data)
ruler_result.show(truncate = False)


# result

+-----------------+-----+---+------------------------------------+
|entity           |begin|end|ruled_ner_chunks_result             |
+-----------------+-----+---+------------------------------------+
|Modified_Age     |28   |29 |36                                  |
|Modified_Diabetes|66   |101|diabetes mellitus with complications|
|Modified_Date    |106  |114|May, 2006                           |
+-----------------+-----+---+------------------------------------+


{%- endcapture -%}


{%- capture model_scala_medical -%}

import spark.implicits._

val rules =
    """
    |[
    |  {
    |    "entity": "Age",
    |    "scopeWindow": [15, 15],
    |    "scopeWindowLevel": "char",
    |    "suffixPatterns": ["years old", "year old", "months"],
    |    "replaceEntity": "Modified_Age",
    |    "mode": "exclude"
    |  },
    |  {
    |    "entity": "Diabetes",
    |    "scopeWindow": [3, 3],
    |    "scopeWindowLevel": "token",
    |    "suffixPatterns": ["with complications"],
    |    "replaceEntity": "Modified_Diabetes",
    |    "mode": "include"
    |  },
    |  {
    |    "entity": "Date",
    |    "suffixRegexes": ["\\d{4}"],
    |    "replaceEntity": "Modified_Date",
    |    "mode": "include"
    |  }
    |]
    """.stripMargin


val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols("document", "token")
    .setOutputCol("embeddings")

val jslNer = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")
   .setInputCols("sentence", "token", "embeddings")
   .setOutputCol("jsl_ner")

val jslNerConverter = new NerConverterInternal()
    .setInputCols("sentence", "token", "jsl_ner")
    .setOutputCol("ner_chunks")

val  contextualEntityRuler = new ContextualEntityRuler()
    .setInputCols("sentence", "token", "ner_chunks")
    .setOutputCol("ruled_ner_chunks")
    .setRulesAsStr(rules)
    .setCaseSensitive(false)
    .setDropEmptyChunks(true)
    .setAllowPunctuationInBetween(true)

val ruler_pipeline = new Pipeline().setStages(
  Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    wordEmbeddings,
    jslNer,
    jslNerConverter,
    contextualEntityRuler
  ))

val text = "The Doctor assessed the 36 years old who has a history of the diabetes mellitus with complications in May, 2006"
val df = Seq(text).toDF("text")
val result = nlpPipeline.fit(df).transform(df)


# result
+-----------------+-----+---+------------------------------------+
|entity           |begin|end|ruled_ner_chunks_result             |
+-----------------+-----+---+------------------------------------+
|Modified_Age     |28   |30 |36                                  |
|Modified_Diabetes|66   |101|diabetes mellitus with complications|
|Modified_Date    |106  |114|May, 2006                           |
+-----------------+-----+---+------------------------------------+

{%- endcapture -%}

{%- capture model_api_link -%}
[ContextualEntityRuler](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/context/ContextualEntityRuler.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[ContextualEntityRuler](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/context/ContextualEntityRuler/index.html)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[ContextualEntityRuler](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ContextualEntityRuler.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical
model_api_link=model_api_link
model_python_api_link=model_python_api_link
model_notebook_link=model_notebook_link
%}
