{%- capture title -%}
ChunkMapperFilterer
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}

`ChunkMapperFilterer` is an annotator to be used after `ChunkMapper` that allows to filter chunks based on the results of the mapping, whether it was successful or failed.

Parametres;

- `ReturnCriteria` *(String)*: Has two possible values: “success” or “fail”. If “fail” (default), returns the chunks that are not in the label dependencies; if “success”, returns the labels that were successfully mapped by the `ChunkMapperModel` annotator.

Example usage and more details can be found on Spark NLP Workshop repository accessible in GitHub, for example the notebook [Healthcare Chunk Mapping](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/26.Chunk_Mapping.ipynb).

{%- endcapture -%}

{%- capture model_input_anno -%}
CHUNK, LABEL_DEPENDENCY
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_python_medical -%}
document_assembler = nlp.DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

sentence_detector = nlp.SentenceDetector()\
      .setInputCols(["document"])\
      .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
      .setInputCols("sentence")\
      .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
      .setInputCols(["sentence", "token"])\
      .setOutputCol("embeddings")

ner_model = medical.NerModel.pretrained("ner_posology_greedy", "en", "clinical/models")\
      .setInputCols(["sentence", "token", "embeddings"])\
      .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
      .setInputCols("sentence", "token", "ner")\
      .setOutputCol("chunk")

chunkerMapper = medical.ChunkMapperModel.pretrained("rxnorm_mapper", "en", "clinical/models")\
      .setInputCols(["chunk"])\
      .setOutputCol("RxNorm_Mapper")\
      .setRels(["rxnorm_code"])

chunk_mapper_filterer = medical.ChunkMapperFilterer() \
      .setInputCols(["chunk", "RxNorm_Mapper"]) \
      .setOutputCol("chunks_fail") \
      .setReturnCriteria("fail")

mapper_pipeline = nlp.Pipeline(
      stages = [
          document_assembler,
          sentence_detector,
          tokenizer,
          word_embeddings,
          ner_model,
          ner_converter,
          chunkerMapper,
          chunkerMapper,
          chunk_mapper_filterer
      ])

samples = [["The patient was given Adapin 10 MG, coumadn 5 mg"],
           ["The patient was given Avandia 4 mg, Tegretol, zitiga"] ]
           
data = spark.createDataFrame(samples).toDF("text")

result = mapper_pipeline.fit(data).transform(data)

result.selectExpr("chunk.result as chunk", 
                  "RxNorm_Mapper.result as RxNorm_Mapper", 
                  "chunks_fail.result as chunks_fail").show(truncate = False)

+--------------------------------+----------------------+--------------+
|chunk                           |RxNorm_Mapper         |chunks_fail   |
+--------------------------------+----------------------+--------------+
|[Adapin 10 MG, coumadn 5 mg]    |[1000049, NONE]       |[coumadn 5 mg]|
|[Avandia 4 mg, Tegretol, zitiga]|[261242, 203029, NONE]|[zitiga]      |
+--------------------------------+----------------------+--------------+

{%- endcapture -%}

{%- capture model_scala_medical -%}
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
 
val sentence_detector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols("sentence", "token")
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_posology_greedy", "en", "clinical/models")
    .setInputCols("sentence", "token", "embeddings")
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols("sentence", "token", "ner")
    .setOutputCol("chunk")

val chunkerMapper = ChunkMapperModel.pretrained("rxnorm_mapper", "en", "clinical/models")
    .setInputCols("chunk")
    .setOutputCol("RxNorm_Mapper")
    .setRels(Array("rxnorm_code"))

val chunk_mapper_filterer = new ChunkMapperFilterer()
    .setInputCols("chunk", "RxNorm_Mapper")
    .setOutputCol("chunks_fail")
    .setReturnCriteria("fail")

val mapper_pipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_model,
    ner_converter,
    chunkerMapper,
    chunk_mapper_filterer
    ))

import spark.implicits._

val data = Seq("The patient was given Adapin 10 MG, coumadn 5 mg",
"The patient was given Avandia 4 mg, Tegretol, zitiga").toDF("text")

val result = mapper_pipeline.fit(data).transform(data)

result.selectExpr("chunk.result as chunk", 
                  "RxNorm_Mapper.result as RxNorm_Mapper", 
                  "chunks_fail.result as chunks_fail").show(truncate = False)

+--------------------------------+----------------------+--------------+
|chunk                           |RxNorm_Mapper         |chunks_fail   |
+--------------------------------+----------------------+--------------+
|[Adapin 10 MG, coumadn 5 mg]    |[1000049, NONE]       |[coumadn 5 mg]|
|[Avandia 4 mg, Tegretol, zitiga]|[261242, 203029, NONE]|[zitiga]      |
+--------------------------------+----------------------+--------------+

{%- endcapture -%}
{%- capture model_api_link -%}
[ChunkMapperFilterer](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/chunker/ChunkMapperFilterer.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[ChunkMapperFilterer](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/chunker/chunkmapper_filterer/index.html#sparknlp_jsl.annotator.chunker.chunkmapper_filterer.ChunkMapperFilterer)
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
%}
