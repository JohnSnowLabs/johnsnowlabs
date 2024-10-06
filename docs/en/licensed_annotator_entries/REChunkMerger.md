 n{%- capture title -%}
 REChunkMerger
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
`REChunkMerger` annotator merges relation chunks to create a new chunk.

Parameters:

- `separator`: Separator to add between the chunks. Default: " ".



{%- endcapture -%}

{%- capture model_input_anno -%}
CATEGORY
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

documenter = nlp.DocumentAssembler() \
    .setInputCol("sentence") \
    .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("tokens") \

words_embedder = nlp.WordEmbeddingsModel() \
    .pretrained("embeddings_clinical", "en", "clinical/models") \
    .setInputCols(["document", "tokens"]) \
    .setOutputCol("embeddings")

pos_tagger = nlp.PerceptronModel() \
    .pretrained("pos_clinical", "en", "clinical/models") \
    .setInputCols(["document", "tokens"]) \
    .setOutputCol("pos_tags")

ner_tagger = medical.NerModel() \
    .pretrained("ner_clinical", "en", "clinical/models") \
    .setInputCols(["document", "tokens", "embeddings"]) \
    .setOutputCol("ner_tags")

ner_converter = medical.NerConverter() \
    .setInputCols(["document", "tokens", "ner_tags"]) \
    .setOutputCol("ner_chunks")

depency_parser = nlp.DependencyParserModel() \
    .pretrained("dependency_conllu", "en") \
    .setInputCols(["document", "pos_tags", "tokens"]) \
    .setOutputCol("dependencies")

re_model = medical.RelationExtractionModel \
    .pretrained("re_clinical", "en", "clinical/models") \
    .setCustomLabels({"TeRP": "CustomLabel_TeRP", "TrWP": "CustomLabel_TeWP"}) \
    .setInputCols(["embeddings", "pos_tags", "ner_chunks", "dependencies"]) \
    .setOutputCol("re_chunk")

re_chunk_merger = medical.REChunkMerger() \
    .setInputCols(["re_chunk"]) \
    .setOutputCol("relation_chunks") \
    .setSeparator(" && ")

nlpPipeline = nlp.Pipeline(
    stages=[
      documenter,
      tokenizer,
      words_embedder,
      pos_tagger,
      ner_tagger,
      ner_converter,
      depency_parser,
      re_model,
      re_chunk_merger
    ])

empty_data = spark.createDataFrame([[""]]).toDF("sentence")

model = nlpPipeline.fit(empty_data)

text =''' 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to " +
"presentation and subsequent type two diabetes mellitus ( T2DM ). '''

result = model.transform(spark.createDataFrame([[text]]).toDF("sentence"))

# result
+----------------------------------------------------------------------+
|result                                                                |
+----------------------------------------------------------------------+
|gestational diabetes mellitus && subsequent type two diabetes mellitus|
|gestational diabetes mellitus && T2DM                                 |
|subsequent type two diabetes mellitus && T2DM                         |
+----------------------------------------------------------------------+
{%- endcapture -%}


{%- capture model_scala_medical -%}

import spark.implicits._

val documenter = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("tokens")

val words_embedder = WordEmbeddingsModel
    .pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols("document", "tokens")
    .setOutputCol("embeddings")

val pos_tagger = PerceptronModel
    .pretrained("pos_clinical", "en", "clinical/models")
    .setInputCols("document", "tokens")
    .setOutputCol("pos_tags")

val ner_tagger = MedicalNerModel
    .pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols("document", "tokens", "embeddings")
    .setOutputCol("ner_tags")

val ner_converter = new NerConverter()
    .setInputCols("document", "tokens", "ner_tags")
    .setOutputCol("ner_chunks")

val depency_parser = DependencyParserModel
    .pretrained("dependency_conllu", "en")
    .setInputCols("document", "pos_tags", "tokens")
    .setOutputCol("dependencies")

val re_model = RelationExtractionModel
    .pretrained("re_clinical", "en", "clinical/models")
    .setInputCols("embeddings", "pos_tags", "ner_chunks", "dependencies")
    .setOutputCol("re_chunk")

val re_chunk_merger = new REChunkMerger()
    .setInputCols("re_chunk")
    .setOutputCol("relation_chunks")
    .setSeparator(" && ")

val pipeline = new Pipeline()
  .setStages(Array(
        documenter,
        tokenizer,
        words_embedder,
        pos_tagger,
        ner_tagger,
        ner_converter,
        depency_parser,
        re_model,
        re_chunk_merger
  ))
val text = "28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to " +
  "presentation and subsequent type two diabetes mellitus ( T2DM ). "

val empty_data = Seq("").toDF("text")

val model = pipeline.fit(empty_data).transform(Seq(text).toDF("text"))

# result
+----------------------------------------------------------------------+
|result                                                                |
+----------------------------------------------------------------------+
|gestational diabetes mellitus && subsequent type two diabetes mellitus|
|gestational diabetes mellitus && T2DM                                 |
|subsequent type two diabetes mellitus && T2DM                         |
+----------------------------------------------------------------------+

{%- endcapture -%}

{%- capture model_api_link -%}
[REChunkMerger](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/merge/REChunkMerger.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[REChunkMerger](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/merge/REChunkMerger.html)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[REChunkMergerNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/REChunkMerger.ipynb)
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
