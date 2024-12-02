{%- capture title -%}
ContextualEntityFilterer
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
ContextualEntityFilterer can filter chunks coming from CHUNK annotations based on entity(identifier,field) info in metadata and contextual cues.
Filters can be done via white list entities, black list entities, black list word and white list words.
The filter can be applied to the scope of the sentence or the document.

Parameters:

- `ruleScope`: The rule scope to apply the filter. Options: sentence, document.
- `caseSensitive`:  Whether to use case-sensitive when matching words. Default is `False`.
- `rules`: The filtering rules. Each rule is a dictionary with the following keys:
  - `entity`: The target entity field for filtering.
  - `scopeWindow`: A list of two integers [before, after], specifying how many tokens/chunks before and after the target to consider.
  - `whiteListEntities`: The white list of entities. If one of the entity from this list appears within the scope window, the chunk will be kept. Only one element is enough to keep the chunk.
  - `blackListEntities`: The black list of entities. If an entity from this list appears within the scope window, the chunk will be filtered out. All elements must be absent to keep the chunk.
  - `scopeWindowLevel`: Determines whether the `scopeWindow` is applied at the token or chunk level. Options: `token`, `chunk`.
  - `blackListWords`: The black list of words. If a word from this list appears within the scope window, the chunk will be filtered out.
  - `whiteListWords`: The white list of words. If a word from this list appears within the scope window, the chunk will be kept.
  - `confidenceThreshold`: The confidence threshold to filter the chunks. Filtering is only applied if the confidence of the chunk is below the threshold.
  
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

ner_deid = medical.NerModel.pretrained("ner_deid_subentity_docwise", "en", "clinical/models")  \
    .setInputCols(["document", "token", "embeddings"]) \
    .setOutputCol("ner_deid_subentity_docwise")

ner_deid_converter = medical.NerConverterInternal()\
    .setInputCols(["document", "token", "ner_deid_subentity_docwise"])\
    .setOutputCol("ner_chunk_subentity_docwise")

rules =[{   "entity": "STATE",
            "scopeWindow": [2, 2],
            "whiteListEntities": ["CITY"],
            "blackListEntities": ["NAME"],
            "scopeWindowLevel": "token"
        }]

contextual_entity_filterer = medical.ContextualEntityFilterer() \
    .setInputCols("document", "token", "ner_chunk_subentity_docwise") \
    .setOutputCol("filtered_ner_chunks") \
    .setRules(rules)\
    .setRuleScope("sentence") 

nlpPipeline = nlp.Pipeline(
  stages=[
      documentAssembler,
      tokenizer,
      word_embeddings,
      ner_deid,
      ner_deid_converter,
      contextual_entity_filterer
])

text = "NY, a 34-year-old woman, Dr. Michael Johnson cares wit her, at CarePlus Clinic, located at 456 Elm Street, NewYork, NY has recommended starting insulin therapy."
df = spark.createDataFrame([[text]]).toDF("text")
result = nlpPipeline.fit(df).transform(df)


# result

+---------------+-----+---+---------+----------+
|chunk          |begin|end|ner_label|confidence|
+---------------+-----+---+---------+----------+
|NY             |0    |1  |STATE    |0.9299    |
|34-year-old    |6    |16 |AGE      |0.7687    |
|Michael Johnson|29   |43 |DOCTOR   |0.89965   |
|CarePlus Clinic|63   |77 |HOSPITAL |0.9661    |
|456 Elm Street |91   |104|STREET   |0.7733667 |
|NewYork        |107  |113|CITY     |0.9302    |
|NY             |116  |117|STATE    |0.9991    |
+---------------+-----+---+---------+----------+
{%- endcapture -%}


{%- capture model_scala_medical -%}

import spark.implicits._

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols("document", "token")
    .setOutputCol("embeddings")

val ner_deid = MedicalNerModel.pretrained("ner_deid_subentity_docwise", "en", "clinical/models")
    .setInputCols("document", "token", "embeddings")
    .setOutputCol("ner_deid_subentity_docwise")

val ner_deid_converter = new NerConverterInternal()
    .setInputCols("document", "token", "ner_deid_subentity_docwise")
    .setOutputCol("ner_chunk_subentity_docwise")

val rules =
  """
    |[{
    |"entity": "STATE",
    |  "scopeWindow": [2, 2],
    |  "whiteListEntities": ["CITY"],
    |  "blackListEntities": ["NAME"],
    |  "scopeWindowLevel": "token"
    |
    | }
    | ]
    |
    |""".stripMargin

val contextual_entity_filterer = new ContextualEntityFilterer()
    .setInputCols("document", "token", "ner_chunk_subentity_docwise")
    .setOutputCol("filtered_ner_chunks")
    .setRulesAsStr(rules)
    .setRuleScope("sentence")

val nlpPipeline = new Pipeline().setStages(
  Array(
    documentAssembler,
    tokenizer,
    word_embeddings,
    ner_deid,
    ner_deid_converter,
    contextual_entity_filterer
  ))

val text = "NY, a 34-year-old woman, Dr. Michael Johnson cares wit her, at CarePlus Clinic, located at 456 Elm Street, NewYork, NY has recommended starting insulin therapy."
val df = Seq(text).toDF("text")
val result = nlpPipeline.fit(df).transform(df)


# result
+---------------+-----+---+---------+----------+
|chunk          |begin|end|ner_label|confidence|
+---------------+-----+---+---------+----------+
|NY             |0    |1  |STATE    |0.9299    |
|34-year-old    |6    |16 |AGE      |0.7687    |
|Michael Johnson|29   |43 |DOCTOR   |0.89965   |
|CarePlus Clinic|63   |77 |HOSPITAL |0.9661    |
|456 Elm Street |91   |104|STREET   |0.7733667 |
|NewYork        |107  |113|CITY     |0.9302    |
|NY             |116  |117|STATE    |0.9991    |
+---------------+-----+---+---------+----------+

{%- endcapture -%}

{%- capture model_api_link -%}
[ContextualEntityFilterer](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/context/ContextualEntityFilterer.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[ContextualEntityFilterer](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/context/ContextualEntityFilterer/index.html)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[ContextualEntityFilterer](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ContextualEntityFilterer.ipynb)
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
