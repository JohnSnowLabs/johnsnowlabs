{%- capture title -%}
Mapper2Chunk
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
This annotator converts 'LABELED_DEPENDENCY' type annotations coming from [[ChunkMapper]] into 'CHUNK' type to create new chunk-type column, compatible with annotators that use chunk type as input.

Parameters:

- `filterNoneValues`: (Bool) Filter 'NONE' values

{%- endcapture -%}

{%- capture model_input_anno -%}
LABELED_DEPENDENCY
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

# Annotator that transforms a text column from dataframe into an Annotation ready for NLP
documentAssembler = nlp.DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("sentence")\

# Tokenizer splits words in a relevant format for NLP
tokenizer = nlp.Tokenizer()\
  .setInputCols("sentence")\
  .setOutputCol("token")\

# Clinical word embeddings trained on PubMED dataset
word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

# NER model trained on n2c2 (de-identification and Heart Disease Risk Factors Challenge) datasets
clinical_ner = medical.NerModel.pretrained("ner_jsl", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter_name = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

chunkMapper = medical.ChunkMapperModel.pretrained("drug_action_treatment_mapper", "en", "clinical/models") \
    .setInputCols(["ner_chunk"]) \
    .setOutputCol("relations") \
    .setRels(["action"])

mapper2chunk = medical.Mapper2Chunk() \
    .setInputCols(["relations"]) \
    .setOutputCol("chunk") \
    .setFilterNoneValues(True)

nlpPipeline = nlp.Pipeline(stages=[
    documentAssembler, 
    tokenizer,
    word_embeddings,
    clinical_ner,
    ner_converter_name,
    chunkMapper,
    mapper2chunk
    ])

sample_text = "Patient resting in bed. Patient given azithromycin without any difficulty. Patient denies nausea at this time. zofran declined. Patient is also having intermittent sweating"

data = spark.createDataFrame([[sample_text]]).toDF("text")
result = nlpPipeline.fit(data).transform(data)

## Result

+--------------------------+--------------+
|result                    |annotatorType |
+--------------------------+--------------+
|[bactericidal, antiemetic]|[chunk, chunk]|
+--------------------------+--------------+

{%- endcapture -%}


{%- capture model_scala_medical -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
    .setInputCols(Array("sentence","token"))
    .setOutputCol("embeddings")

val clinical_ner = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")
    .setInputCols(Array("sentence","token","embeddings"))
    .setOutputCol("ner")

val ner_converter_name = new NerConverterInternal()
    .setInputCols(Array("sentence","token","ner"))
    .setOutputCol("ner_chunk")

val chunkMapper = ChunkMapperModel.pretrained("drug_action_treatment_mapper", "en", "clinical/models")
    .setInputCols("ner_chunk")
    .setOutputCol("relations")
    .setRels("action")

val mapper2chunk = new Mapper2Chunk()
    .setInputCols("relations")
    .setOutputCol("chunk")
    .setFilterNoneValues(True)

val nlpPipeline = new Pipeline().setStages(Array(
    documentAssembler, 
    tokenizer, 
    word_embeddings, 
    clinical_ner, 
    ner_converter_name, 
    chunkMapper, 
    mapper2chunk))


val test_data = Seq("""Patient resting in bed. Patient given azithromycin without any difficulty. Patient denies nausea at this time. zofran declined. Patient is also having intermittent sweating""").toDF("text")

val res = mapperPipeline.fit(test_data).transform(test_data)

// Show results

+--------------------------+--------------+
|result                    |annotatorType |
+--------------------------+--------------+
|[bactericidal, antiemetic]|[chunk, chunk]|
+--------------------------+--------------+

{%- endcapture -%}

{%- capture model_api_link -%}
[Mapper2Chunk](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/chunker/Mapper2Chunk.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[Mapper2Chunk](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/chunker/mapper2_chunk/index.html#)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[Mapper2Chunk](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/Mapper2Chunk.ipynb)
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
