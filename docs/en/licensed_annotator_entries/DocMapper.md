{%- capture title -%}
DocMapper
{%- endcapture -%}

{%- capture approach -%}
approach
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}

`DocMapper` uses the text representation of document annotations to map clinical codes to other codes or relevant information. 

Parametres:

- `setRels` *(List[str])*: Relations that we are going to use to map the document

- `setLowerCase` *(Boolean)*: Set if we want to map the documents in lower case or not (Default: True)

- `setAllowMultiTokenChunk` *(Boolean)*: Whether to skip relations with multitokens (Default: True)

- `setMultivaluesRelations` *(Boolean)*:  Whether to decide to return all values in a relation together or separately (Default: False)


{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_output_anno -%}
LABEL_DEPENDENCY
{%- endcapture -%}

{%- capture model_python_medical -%}

from johnsnowlabs import nlp, medical

#ChunkMapper Pipeline
document_assembler = nlp.DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

#drug_action_treatment_mapper 
docMapper= medical.DocMapperModel().pretrained("drug_action_treatment_mapper", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("mappings")\
    .setRels(["action", "treatment"])

mapperPipeline = nlp.Pipeline().setStages([
    document_assembler,
    docMapper])

test_data = spark.createDataFrame([["Dermovate"], ["Aspagin"]]).toDF("text")

res = mapperPipeline.fit(test_data).transform(test_data)

# Show results
res.select(F.explode(F.arrays_zip(res.mappings.result, 
                                  res.mappings.metadata)).alias("col"))\
    .select(F.expr("col['1']['entity']").alias("ner_chunk"),
            F.expr("col['0']").alias("mapping_result"),
            F.expr("col['1']['relation']").alias("relation"),
            F.expr("col['1']['all_relations']").alias("all_mappings")).show(truncate=False)

+---------+----------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|ner_chunk|mapping_result        |relation |all_mappings                                                                                                                                                                                                           |
+---------+----------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|Dermovate|anti-inflammatory     |action   |corticosteroids::: dermatological preparations:::very strong                                                                                                                                                           |
|Dermovate|lupus                 |treatment|discoid lupus erythematosus:::empeines:::psoriasis:::eczema                                                                                                                                                            |
|Aspagin  |analgesic             |action   |anti-inflammatory:::antipyretic                                                                                                                                                                                        |
|Aspagin  |ankylosing spondylitis|treatment|arthralgia:::pain:::bursitis:::headache:::migraine:::myositis:::neuralgia:::osteoarthritis:::gout:::rheumatoid arthritis:::spondylitis:::spondyloarthritis:::tendinitis:::tenosynovitis:::crush injury:::golfer's elbow|
+---------+----------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


{%- endcapture -%}


{%- capture model_scala_medical -%}

import spark.implicits._

#ChunkMapper Pipeline
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

#drug_action_treatment_mapper 
val docMapper= DocMapperModel().pretrained("drug_action_treatment_mapper", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("mappings")
    .setRels(Array("action", "treatment"))

val mapperPipeline = new Pipeline().setStages(Array(
    document_assembler,
    docMapper))


val test_data = Seq(("Dermovate", "Aspagin")).toDF("text")

val res = mapperPipeline.fit(test_data).transform(test_data)

// Show results

+---------+----------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|ner_chunk|mapping_result        |relation |all_mappings                                                                                                                                                                                                           |
+---------+----------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|Dermovate|anti-inflammatory     |action   |corticosteroids::: dermatological preparations:::very strong                                                                                                                                                           |
|Dermovate|lupus                 |treatment|discoid lupus erythematosus:::empeines:::psoriasis:::eczema                                                                                                                                                            |
|Aspagin  |analgesic             |action   |anti-inflammatory:::antipyretic                                                                                                                                                                                        |
|Aspagin  |ankylosing spondylitis|treatment|arthralgia:::pain:::bursitis:::headache:::migraine:::myositis:::neuralgia:::osteoarthritis:::gout:::rheumatoid arthritis:::spondylitis:::spondyloarthritis:::tendinitis:::tenosynovitis:::crush injury:::golfer's elbow|
+---------+----------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}

{%- capture model_api_link -%}
[DocMapperModel](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/chunker/DocMapperModel.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[DocMapperModel](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/chunker/docmapper/index.html#sparknlp_jsl.annotator.chunker.docmapper.DocMapperModel)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[DocMapperModelNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/DocMapperModel.ipynb)
{%- endcapture -%}

{%- capture approach_description -%}

`DocMapper` that can be used to map short strings via DocumentAssembler without using any other annotator between to convert strings to Chunk type that ChunkMapperModel expects.

Parameters:

- `setDictionary` *(Str)*: Dictionary path where is the JsonDictionary that contains the mappings columns

- `setRels` *(Boolean)*: Relations that we are going to use to map the document

- `setLowerCase` *(Boolean)*: Set if we want to map the documents in lower case or not (Default: True)

- `setAllowMultiTokenChunk` *(Boolean)*: Whether to skip relations with multitokens (Default: True)

- `setMultivaluesRelations` *(Boolean)*:  Whether to decide to return all values in a relation together or separately (Default: False)
{%- endcapture -%}

{%- capture approach_input_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture approach_output_anno -%}
LABEL_DEPENDENCY
{%- endcapture -%}

{%- capture approach_python_medical -%}

from johnsnowlabs import nlp,  medical

data_set= {
  "mappings": [
    {
      "key": "metformin",
      "relations": [
        {
          "key": "action",
          "values" : ["hypoglycemic", "Drugs Used In Diabetes"]
        },
        {
          "key": "treatment",
          "values" : ["diabetes", "t2dm"]
        }
      ]
    }
  ]
}

import json
with open('sample_drug.json', 'w', encoding='utf-8') as f:
    json.dump(data_set, f, ensure_ascii=False, indent=4)

document_assembler = nlp.DocumentAssembler()\
      .setInputCol('text')\
      .setOutputCol('document')

chunkerMapper = medical.DocMapperApproach()\
      .setInputCols(["document"])\
      .setOutputCol("mappings")\
      .setDictionary("./sample_drug.json")\
      .setRels(["action"])

pipeline = nlp.Pipeline().setStages([document_assembler,
                                     chunkerMapper])

test_data = spark.createDataFrame([["metformin"]]).toDF("text")

res = pipeline.fit(test_data).transform(test_data)


## Results
res.select(F.explode(F.arrays_zip(res.mappings.result,
                                  res.mappings.metadata)).alias("col"))\
    .select(F.expr("col['1']['entity']").alias("document"),
            F.expr("col['0']").alias("mapping_result"),
            F.expr("col['1']['relation']").alias("relation"),
            F.expr("col['1']['all_relations']").alias("all_mappings")).show(truncate=False)

+---------+--------------+--------+----------------------+
|document |mapping_result|relation|all_mappings          |
+---------+--------------+--------+----------------------+
|metformin|hypoglycemic  |action  |Drugs Used In Diabetes|
+---------+--------------+--------+----------------------+
{%- endcapture -%}


{%- capture approach_scala_medical -%}

import spark.implicits._

/* sample_drug.json file
{
  "mappings": [
    {
      "key": "metformin",
      "relations": [
        {
          "key": "action",
          "values" : ["hypoglycemic", "Drugs Used In Diabetes"]
        },
        {
          "key": "treatment",
          "values" : ["diabetes", "t2dm"]
        }
      ]
    }
  ]
}
*/

val document_assembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document") 

val chunkerMapper = new DocMapperApproach()
  .setInputCols("document")
  .setOutputCol("mappings")
  .setDictionary("./sample_drug.json")
  .setRels("action")

val pipeline = new Pipeline().setStages(Array(document_assembler, chunkerMapper))

val test_data = Seq("metformin").toDF("text") 

val res = pipeline.fit(test_data).transform(test_data)


// Results 

+---------+--------------+--------+----------------------+
|document |mapping_result|relation|all_mappings          |
+---------+--------------+--------+----------------------+
|metformin|hypoglycemic  |action  |Drugs Used In Diabetes|
+---------+--------------+--------+----------------------+
{%- endcapture -%}


{%- capture approach_api_link -%}
[DocMapperApproach](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/chunker/DocMapperApproach.html)
{%- endcapture -%}

{%- capture approach_python_api_link -%}
[DocMapperApproach](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/chunker/docmapper/index.html#sparknlp_jsl.annotator.chunker.docmapper.DocMapperApproach.name)
{%- endcapture -%}

{%- capture approach_notebook_link -%}
[DocMapperApproachNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/DocMapperApproach.ipynb)
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
model_api_link=model_api_link
model_python_api_link=model_python_api_link
approach_description=approach_description
approach_input_anno=approach_input_anno
approach_output_anno=approach_output_anno
approach_python_medical=approach_python_medical
approach_scala_medical=approach_scala_medical
approach_api_link=approach_api_link
approach_python_api_link=approach_python_api_link
model_notebook_link=model_notebook_link
approach_notebook_link=approach_notebook_link
%}
