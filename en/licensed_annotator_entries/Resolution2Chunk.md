{%- capture title -%}
Resolution2Chunk
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
This annotator is responsible for converting the annotations generated by entity resolver models (typically labeled as ENTITY) into a format compatible with subsequent stages of the pipeline, such as the ChunkMapperModel. It transforms these annotations into CHUNK annotations, allowing for seamless integration and processing of clinical terminologies and entities in the pipeline.

{%- endcapture -%}

{%- capture model_input_anno -%}
Resolution
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_python_medical -%}

from johnsnowlabs import medical, nlp

document_assembler = nlp.DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("ner_chunk")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en","clinical/models")\
      .setInputCols(["ner_chunk"])\
      .setOutputCol("sentence_embeddings")\
      .setCaseSensitive(False)

rxnorm_resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_rxnorm_augmented","en", "clinical/models") \
      .setInputCols(["sentence_embeddings"]) \
      .setOutputCol("rxnorm_code")\
      .setDistanceFunction("EUCLIDEAN")

resolver2chunk = medical.Resolution2Chunk()\
      .setInputCols(["rxnorm_code"]) \
      .setOutputCol("resolver2chunk")

chunkerMapper_action = medical.ChunkMapperModel.pretrained("rxnorm_action_treatment_mapper", "en", "clinical/models")\
      .setInputCols(["resolver2chunk"])\
      .setOutputCol("action_mapping")\
      .setRels(["action"]) #for treatment

pipeline = nlp.Pipeline().setStages([document_assembler,
                                 sbert_embedder,
                                 rxnorm_resolver,
                                 resolver2chunk,
                                 chunkerMapper_action
                                 ])

data= spark.createDataFrame([['Zonalon 50 mg']]).toDF('text')

res= pipeline.fit(data).transform(data)

# Example results

res.select(F.explode(F.arrays_zip(res.ner_chunk.result,
                                  res.rxnorm_code.result,
                                  res.action_mapping.result)).alias("col"))\
    .select(F.expr("col['0']").alias("document"),
            F.expr("col['1']").alias("rxnorm_code"),
            F.expr("col['2']").alias("Action Mapping")).show(truncate=False)

+-------------+-----------+--------------+
|document     |rxnorm_code|Action Mapping|
+-------------+-----------+--------------+
|Zonalon 50 mg|103971     |Analgesic     |
+-------------+-----------+--------------+


{%- endcapture -%}


{%- capture model_scala_medical -%}

import spark.implicits._

val document_assembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("ner_chunk")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
  .setInputCols("ner_chunk")
  .setOutputCol("sentence_embeddings")
  .setCaseSensitive(False)

val rxnorm_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_rxnorm_augmented","en","clinical/models")
  .setInputCols("sentence_embeddings")
  .setOutputCol("rxnorm_code")
  .setDistanceFunction("EUCLIDEAN")

val resolver2chunk = new Resolution2Chunk()
  .setInputCols("rxnorm_code")
  .setOutputCol("resolver2chunk")

val chunkerMapper_action = ChunkMapperModel.pretrained("rxnorm_action_treatment_mapper","en","clinical/models")
  .setInputCols("resolver2chunk")
  .setOutputCol("action_mapping")
  .setRels("action")

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sbert_embedder, 
    rxnorm_resolver, 
    resolver2chunk, 
    chunkerMapper_action )) 

val data = Seq("Zonalon 50 mg").toDF("text") 

val res = pipeline.fit(data).transform(data)

// Example results

+-------------+-----------+--------------+
|document     |rxnorm_code|Action Mapping|
+-------------+-----------+--------------+
|Zonalon 50 mg|103971     |Analgesic     |
+-------------+-----------+--------------+

{%- endcapture -%}


{%- capture model_api_link -%}
[Resolution2Chunk](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/resolution/Resolution2Chunk.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[Resolution2Chunk](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/resolution2_chunk/index.html#sparknlp_jsl.annotator.resolution2_chunk.Resolution2Chunk)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[Resolution2ChunkNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/Resolution2Chunk.ipynb)
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