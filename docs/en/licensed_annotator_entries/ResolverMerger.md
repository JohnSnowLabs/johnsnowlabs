{%- capture title -%}
ResolverMerger
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
`ResolverMerger` provides the ability to merge sentence enitity resolver and chunk mapper model output columns. 

To convert a sentence or document into a vector for tasks like semantic search or recommendation systems, a common approach is to utilize transformer models like BERT. These models provide embeddings for each token in the text. One option is to extract the embedding vector of the CLS token, which represents the overall meaning of the text. Another option is to average the embeddings of all tokens.

Alternatively, we can use fine-tuned Siamese network variants like SBERT, which are specifically designed to generate embeddings that bring similar sentences or documents closer together in the embedding space while separating dissimilar ones. These embeddings can be applied in "Sentence Entity Resolver Models" to perform entity mapping.

However, for a more straightforward approach, we can use a chunk mapper method to extract entities from the text. In addition, by combining resolver models and mapper models using the `ResolverMerger` annotator, we can further enhance the performance and accuracy of the resolver system.

Parametres:

- `inputCols`: The name of the columns containing the input annotations. It can read an Array of strings.

- `outputCol`: The name of the column in Document type that is generated. We can specify only one column here.

All the parameters can be set using the corresponding set method in camel case. For example, `.setInputcols()`.   

{%- endcapture -%}

{%- capture model_input_anno -%}
ENTITY, LABEL_DEPENDENCY
{%- endcapture -%}

{%- capture model_output_anno -%}
ENTITY
{%- endcapture -%}

{%- capture model_python_medical -%}

from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler()\
    .setInputCol('text')\
    .setOutputCol('document')

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
    .setRel("rxnorm_code")

cfModel = medical.ChunkMapperFilterer() \
    .setInputCols(["chunk", "RxNorm_Mapper"]) \
    .setOutputCol("chunks_fail") \
    .setReturnCriteria("fail")

chunk2doc = nlp.Chunk2Doc() \
    .setInputCols("chunks_fail") \
    .setOutputCol("doc_chunk")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained('sbiobert_base_cased_mli', 'en','clinical/models')\
    .setInputCols(["doc_chunk"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_rxnorm_augmented", "en", "clinical/models") \
    .setInputCols(["sentence_embeddings"]) \
    .setOutputCol("resolver_code") \
    .setDistanceFunction("EUCLIDEAN")

resolverMerger = medical.ResolverMerger()\
    .setInputCols(["resolver_code","RxNorm_Mapper"])\
    .setOutputCol("RxNorm")

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
        cfModel,
        chunk2doc,
        sbert_embedder,
        resolver,
        resolverMerger
    ])

sample_text = [
    ["The patient was given Adapin 10 MG, coumadn 5 mg"],
    ["The patient was given Avandia 4 mg, Tegretol, zitiga"],
]

data = spark.createDataFrame(sample_text).toDF("text")

result = mapper_pipeline.fit(data).transform(data)

result.selectExpr(
    "chunk.result as chunk",
    "RxNorm_Mapper.result as RxNorm_Mapper",
    "chunks_fail.result as chunks_fail",
    "resolver_code.result as resolver_code",
    "RxNorm.result as RxNorm",
).show(truncate=False)


## Result

+--------------------------------+----------------------+--------------+-------------+------------------------+
|chunk                           |RxNorm_Mapper         |chunks_fail   |resolver_code|RxNorm                  |
+--------------------------------+----------------------+--------------+-------------+------------------------+
|[Adapin 10 MG, coumadn 5 mg]    |[1000049, NONE]       |[coumadn 5 mg]|[200883]     |[1000049, 200883]       |
|[Avandia 4 mg, Tegretol, zitiga]|[261242, 203029, NONE]|[zitiga]      |[220989]     |[261242, 203029, 220989]|
+--------------------------------+----------------------+--------------+-------------+------------------------+

{%- endcapture -%}


{%- capture model_scala_medical -%}

import spark.implicits._

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
    .setInputCols(Array("sentence","token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_posology_greedy","en","clinical/models")
    .setInputCols(Array("sentence","token","embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence","token","ner"))
    .setOutputCol("chunk")

val chunkerMapper = ChunkMapperModel.pretrained("rxnorm_mapper","en","clinical/models")
    .setInputCols("chunk")
    .setOutputCol("RxNorm_Mapper")
    .setRel("rxnorm_code")

val cfModel = new ChunkMapperFilterer()
    .setInputCols(Array("chunk","RxNorm_Mapper"))
    .setOutputCol("chunks_fail")
    .setReturnCriteria("fail")

val chunk2doc = new Chunk2Doc()
    .setInputCols("chunks_fail")
    .setOutputCol("doc_chunk")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
    .setInputCols("doc_chunk")
    .setOutputCol("sentence_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_rxnorm_augmented","en","clinical/models")
    .setInputCols("sentence_embeddings")
    .setOutputCol("resolver_code")
    .setDistanceFunction("EUCLIDEAN")

val resolverMerger = new ResolverMerger()
    .setInputCols(Array("resolver_code","RxNorm_Mapper"))
    .setOutputCol("RxNorm")

val mapper_pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector, 
    tokenizer, 
    word_embeddings, 
    ner_model, 
    ner_converter, 
    chunkerMapper, 
    chunkerMapper, 
    cfModel, 
    chunk2doc, 
    sbert_embedder, 
    resolver, 
    resolverMerger))


val data = Seq(("""The patient was given Adapin 10 MG, coumadn 5 mg"""),("""The patient was given Avandia 4 mg, Tegretol, zitiga""")).toDF("text")

val res = mapperPipeline.fit(data).transform(data)

// Show results

+--------------------------------+----------------------+--------------+-------------+------------------------+
|chunk                           |RxNorm_Mapper         |chunks_fail   |resolver_code|RxNorm                  |
+--------------------------------+----------------------+--------------+-------------+------------------------+
|[Adapin 10 MG, coumadn 5 mg]    |[1000049, NONE]       |[coumadn 5 mg]|[200883]     |[1000049, 200883]       |
|[Avandia 4 mg, Tegretol, zitiga]|[261242, 203029, NONE]|[zitiga]      |[220989]     |[261242, 203029, 220989]|
+--------------------------------+----------------------+--------------+-------------+------------------------+

{%- endcapture -%}

{%- capture model_api_link -%}
[ResolverMerger](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/resolution/ResolverMerger.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[ResolverMerger](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/resolution/resolver_merger/index.html#module-sparknlp_jsl.annotator.resolution.resolver_merger)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[ResolverMergerNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ResolverMerger.ipynb)
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
