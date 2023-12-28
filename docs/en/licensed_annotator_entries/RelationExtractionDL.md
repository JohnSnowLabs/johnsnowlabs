{%- capture title -%}
RelationExtractionDL
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
This Relation Extraction annotator extracts and classifies instances of relations between named entities. In contrast with `RelationExtractionModel`, `RelationExtractionDLModel` is based on BERT. 

Parametres:

- `predictionThreshold` *(Float)*: Sets minimal activation of the target unit to encode a new relation instance.

- `customLabels` *(dict[str, str])*: Custom relation labels.

- `DoExceptionHandling`: If it is set as True, the annotator tries to process as usual and ff exception-causing data (e.g. corrupted record/ document) is passed to the annotator, an exception warning is emitted which has the exception message.

Available models can be found at the [Models Hub](https://nlp.johnsnowlabs.com/models?task=Relation+Extraction).

For more extended examples on document pre-processing see the [Spark NLP Workshop](https://github.com/JohnSnowLabs/spark-nlp-workshop)
{%- endcapture -%}

{%- capture model_input_anno -%}
CHUNK, DOCUMENT
{%- endcapture -%}

{%- capture model_output_anno -%}
CATEGORY
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

documenter = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentencer = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

words_embedder = nlp.WordEmbeddingsModel()\
    .pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

pos_tagger = nlp.PerceptronModel()\
    .pretrained("pos_clinical", "en", "clinical/models") \
    .setInputCols(["sentence", "token"])\
    .setOutputCol("pos_tags")

ner_tagger = medical.NerModel.pretrained("ner_ade_clinical", "en", "clinical/models")\
    .setInputCols("sentence", "token", "embeddings")\
    .setOutputCol("ner_tags")

ner_chunker = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner_tags"])\
    .setOutputCol("ner_chunks")

dependency_parser = nlp.DependencyParserModel()\
    .pretrained("dependency_conllu", "en")\
    .setInputCols(["sentence", "pos_tags", "token"])\
    .setOutputCol("dependencies")

ade_re_ner_chunk_filter = medical.RENerChunksFilter() \
    .setInputCols(["ner_chunks", "dependencies"])\
    .setOutputCol("re_ner_chunks")\
    .setMaxSyntacticDistance(10)\
    .setRelationPairs(["drug-ade, ade-drug"])

ade_re_model = medical.RelationExtractionDLModel()\
    .pretrained('redl_ade_biobert', 'en', "clinical/models") \
    .setInputCols(["re_ner_chunks", "sentences"]) \
    .setPredictionThreshold(0.5)\
    .setOutputCol("relations")

pipeline = nlp.Pipeline(stages=[
    documenter,
    sentencer,
    tokenizer,
    words_embedder,
    pos_tagger,
    ner_tagger,
    ner_chunker,
    dependency_parser,
    ade_re_ner_chunk_filter,
    ade_re_model
])

text = """A 44-year-old man taking naproxen for chronic low back pain and a 20-year-old woman on oxaprozin for rheumatoid arthritis presented with tense bullae and cutaneous fragility on the face and the back of the hands."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

from pyspark.sql import functions as F

results.select(
    F.explode(F.arrays_zip(results.relations.metadata, results.relations.result)).alias("cols")).select(
    F.expr("cols['0']['sentence']").alias("sentence"),
    F.expr("cols['0']['entity1_begin']").alias("entity1_begin"),
    F.expr("cols['0']['entity1_end']").alias("entity1_end"),
    F.expr("cols['0']['chunk1']").alias("chunk1"),
    F.expr("cols['0']['entity1']").alias("entity1"),
    F.expr("cols['0']['entity2_begin']").alias("entity2_begin"),
    F.expr("cols['0']['entity2_end']").alias("entity2_end"),
    F.expr("cols['0']['chunk2']").alias("chunk2"),
    F.expr("cols['0']['entity2']").alias("entity2"),
    F.expr("cols['1']").alias("relation"),
    F.expr("cols['0']['confidence']").alias("confidence"),
).show(truncate=70)

+--------+-------------+-----------+---------+-------+-------------+-----------+---------------------------------------------------------+-------+--------+----------+
|sentence|entity1_begin|entity1_end|   chunk1|entity1|entity2_begin|entity2_end|                                                   chunk2|entity2|relation|confidence|
+--------+-------------+-----------+---------+-------+-------------+-----------+---------------------------------------------------------+-------+--------+----------+
|       0|           25|         32| naproxen|   DRUG|          137|        148|                                             tense bullae|    ADE|       1| 0.9989047|
|       0|           25|         32| naproxen|   DRUG|          154|        210|cutaneous fragility on the face and the back of the hands|    ADE|       1| 0.9989704|
|       0|           87|         95|oxaprozin|   DRUG|          137|        148|                                             tense bullae|    ADE|       1|0.99895453|
|       0|           87|         95|oxaprozin|   DRUG|          154|        210|cutaneous fragility on the face and the back of the hands|    ADE|       1|0.99900633|
+--------+-------------+-----------+---------+-------+-------------+-----------+---------------------------------------------------------+-------+--------+----------+
{%- endcapture -%}

{%- capture model_scala_medical -%}
import spark.implicits._

val documenter = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentencer = new SentenceDetector()
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val wordsEmbedder = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

val posTagger = PerceptronModel.pretrained("pos_clinical", "en", "clinical/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("pos_tags")

val nerTagger = MedicalNerModel.pretrained("ner_ade_clinical", "en", "clinical/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner_tags")

val nerChunker = new NerConverterInternal()
  .setInputCols(Array("sentence", "token", "ner_tags"))
  .setOutputCol("ner_chunks")

val dependencyParser = DependencyParserModel.pretrained("dependency_conllu", "en")
  .setInputCols(Array("sentence", "pos_tags", "token"))
  .setOutputCol("dependencies")

val adeReNerChunkFilter = new RENerChunksFilter()
  .setInputCols(Array("ner_chunks", "dependencies"))
  .setOutputCol("re_ner_chunks")
  .setMaxSyntacticDistance(10)
  .setRelationPairs(Array("drug-ade", "ade-drug"))

val adeReModel = RelationExtractionDLModel.pretrained("redl_ade_biobert", "en", "clinical/models")
  .setInputCols(Array("re_ner_chunks", "sentences"))
  .setPredictionThreshold(0.5)
  .setOutputCol("relations")

val pipeline = new Pipeline()
  .setStages(Array(
    documenter,
    sentencer,
    tokenizer,
    wordsEmbedder,
    posTagger,
    nerTagger,
    nerChunker,
    dependencyParser,
    adeReNerChunkFilter,
    adeReModel
  ))

val text = """A 44-year-old man taking naproxen for chronic low back pain and a 20-year-old woman on oxaprozin for rheumatoid arthritis presented with tense bullae and cutaneous fragility on the face and the back of the hands."""

val data = Seq(text).toDF("text")

val result = pipeline.fit(data).transform(data)

+--------+-------------+-----------+---------+-------+-------------+-----------+---------------------------------------------------------+-------+--------+----------+
|sentence|entity1_begin|entity1_end|   chunk1|entity1|entity2_begin|entity2_end|                                                   chunk2|entity2|relation|confidence|
+--------+-------------+-----------+---------+-------+-------------+-----------+---------------------------------------------------------+-------+--------+----------+
|       0|           25|         32| naproxen|   DRUG|          137|        148|                                             tense bullae|    ADE|       1| 0.9989047|
|       0|           25|         32| naproxen|   DRUG|          154|        210|cutaneous fragility on the face and the back of the hands|    ADE|       1| 0.9989704|
|       0|           87|         95|oxaprozin|   DRUG|          137|        148|                                             tense bullae|    ADE|       1|0.99895453|
|       0|           87|         95|oxaprozin|   DRUG|          154|        210|cutaneous fragility on the face and the back of the hands|    ADE|       1|0.99900633|
+--------+-------------+-----------+---------+-------+-------------+-----------+---------------------------------------------------------+-------+--------+----------+
{%- endcapture -%}

{%- capture model_python_legal -%}
from johnsnowlabs import nlp, legal

document_assembler = nlp.DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

text_splitter = legal.TextSplitter()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = nlp.RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base", "en") \
    .setInputCols("sentence", "token") \
    .setOutputCol("embeddings")\
    .setMaxSentenceLength(512)

ner_model = legal.NerModel.pretrained("legner_contract_doc_parties", "en", "legal/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = legal.NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")

re_model = legal.RelationExtractionDLModel.pretrained("legre_contract_doc_parties", "en", "legal/models")\
    .setPredictionThreshold(0.1)\
    .setInputCols(["ner_chunk", "sentence"])\
    .setOutputCol("relation")

pipeline = nlp.Pipeline(stages=[
        document_assembler,
        text_splitter,
        tokenizer,
        embeddings,
        ner_model,
        ner_converter,
        re_model
        ])

text = """This INTELLECTUAL PROPERTY AGREEMENT (this "Agreement"), dated as of December 31, 2018 (the "Effective Date") is entered into by and between Armstrong Flooring, Inc., a Delaware corporation ("Seller") and AFI Licensing LLC, a Delaware limited liability company ("Licensing" and together with Seller, "Arizona") and AHF Holding, Inc. (formerly known as Tarzan HoldCo, Inc.), a Delaware corporation ("Buyer") and Armstrong Hardwood Flooring Company, a Tennessee corporation (the "Company" and together with Buyer the "Buyer Entities") (each of Arizona on the one hand and the Buyer Entities on the other hand, a "Party" and collectively, the "Parties")."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

from pyspark.sql import functions as F

result.select(
    F.explode(F.arrays_zip(result.relation.metadata, result.relation.result)).alias("cols")).select(
    F.expr("cols['0']['sentence']").alias("sentence"),
    F.expr("cols['0']['entity1_begin']").alias("entity1_begin"),
    F.expr("cols['0']['entity1_end']").alias("entity1_end"),
    F.expr("cols['0']['chunk1']").alias("chunk1"),
    F.expr("cols['0']['entity1']").alias("entity1"),
    F.expr("cols['0']['entity2_begin']").alias("entity2_begin"),
    F.expr("cols['0']['entity2_end']").alias("entity2_end"),
    F.expr("cols['0']['chunk2']").alias("chunk2"),
    F.expr("cols['0']['entity2']").alias("entity2"),
    F.expr("cols['1']").alias("relation"),
    F.expr("cols['0']['confidence']").alias("confidence"),
).filter("relation != 'no_rel'").show(truncate=70)

+--------+-------------+-----------+-----------------------------------+-------+-------------+-----------+-----------------------+-------+--------------------+----------+
|sentence|entity1_begin|entity1_end|                             chunk1|entity1|entity2_begin|entity2_end|                 chunk2|entity2|            relation|confidence|
+--------+-------------+-----------+-----------------------------------+-------+-------------+-----------+-----------------------+-------+--------------------+----------+
|       0|            5|         35|    INTELLECTUAL PROPERTY AGREEMENT|    DOC|           69|         85|      December 31, 2018|EFFDATE|            dated_as| 0.9856822|
|       0|            5|         35|    INTELLECTUAL PROPERTY AGREEMENT|    DOC|          141|        163|Armstrong Flooring, Inc|  PARTY|           signed_by| 0.7816506|
|       0|            5|         35|    INTELLECTUAL PROPERTY AGREEMENT|    DOC|          205|        221|      AFI Licensing LLC|  PARTY|           signed_by|0.53521496|
|       0|          141|        163|            Armstrong Flooring, Inc|  PARTY|          192|        197|                 Seller|  ALIAS|           has_alias| 0.8962001|
|       0|          205|        221|                  AFI Licensing LLC|  PARTY|          263|        271|              Licensing|  ALIAS|           has_alias|0.95189077|
|       0|          292|        297|                             Seller|  ALIAS|          301|        307|                Arizona|  ALIAS|has_collective_alias| 0.8934925|
|       1|          411|        445|Armstrong Hardwood Flooring Company|  PARTY|          478|        484|                Company|  ALIAS|           has_alias|0.98353034|
|       1|          505|        509|                              Buyer|  ALIAS|          516|        529|         Buyer Entities|  ALIAS|has_collective_alias| 0.7217146|
|       1|          611|        615|                              Party|  ALIAS|          641|        647|                Parties|  ALIAS|has_collective_alias| 0.5040909|
+--------+-------------+-----------+-----------------------------------+-------+-------------+-----------+-----------------------+-------+--------------------+----------+
{%- endcapture -%}

{%- capture model_scala_legal -%}
import spark.implicits._

val document_assembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val text_splitter = new TextSplitter()
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val embeddings = RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base", "en", "clinical/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")
  .setMaxSentenceLength(512)

val ner_model = LegalNerModel.pretrained("legner_contract_doc_parties", "en", "legal/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner")

val ner_converter = new NerConverter()
  .setInputCols(Array("sentence", "token", "ner"))
  .setOutputCol("ner_chunk")

val re_model = RelationExtractionDLModel.pretrained("legre_contract_doc_parties", "en", "legal/models")
  .setPredictionThreshold(0.1)
  .setInputCols(Array("ner_chunk", "sentence"))
  .setOutputCol("relation")

val pipeline = new Pipeline()
  .setStages(Array(
    document_assembler,
    text_splitter,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter,
    re_model
  ))

text = """This INTELLECTUAL PROPERTY AGREEMENT (this "Agreement"), dated as of December 31, 2018 (the "Effective Date") is entered into by and between Armstrong Flooring, Inc., a Delaware corporation ("Seller") and AFI Licensing LLC, a Delaware limited liability company ("Licensing" and together with Seller, "Arizona") and AHF Holding, Inc. (formerly known as Tarzan HoldCo, Inc.), a Delaware corporation ("Buyer") and Armstrong Hardwood Flooring Company, a Tennessee corporation (the "Company" and together with Buyer the "Buyer Entities") (each of Arizona on the one hand and the Buyer Entities on the other hand, a "Party" and collectively, the "Parties")."""

val data = Seq(text).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)

+--------+-------------+-----------+-----------------------------------+-------+-------------+-----------+-----------------------+-------+--------------------+----------+
|sentence|entity1_begin|entity1_end|                             chunk1|entity1|entity2_begin|entity2_end|                 chunk2|entity2|            relation|confidence|
+--------+-------------+-----------+-----------------------------------+-------+-------------+-----------+-----------------------+-------+--------------------+----------+
|       0|            5|         35|    INTELLECTUAL PROPERTY AGREEMENT|    DOC|           69|         85|      December 31, 2018|EFFDATE|            dated_as| 0.9856822|
|       0|            5|         35|    INTELLECTUAL PROPERTY AGREEMENT|    DOC|          141|        163|Armstrong Flooring, Inc|  PARTY|           signed_by| 0.7816506|
|       0|            5|         35|    INTELLECTUAL PROPERTY AGREEMENT|    DOC|          205|        221|      AFI Licensing LLC|  PARTY|           signed_by|0.53521496|
|       0|          141|        163|            Armstrong Flooring, Inc|  PARTY|          192|        197|                 Seller|  ALIAS|           has_alias| 0.8962001|
|       0|          205|        221|                  AFI Licensing LLC|  PARTY|          263|        271|              Licensing|  ALIAS|           has_alias|0.95189077|
|       0|          292|        297|                             Seller|  ALIAS|          301|        307|                Arizona|  ALIAS|has_collective_alias| 0.8934925|
|       1|          411|        445|Armstrong Hardwood Flooring Company|  PARTY|          478|        484|                Company|  ALIAS|           has_alias|0.98353034|
|       1|          505|        509|                              Buyer|  ALIAS|          516|        529|         Buyer Entities|  ALIAS|has_collective_alias| 0.7217146|
|       1|          611|        615|                              Party|  ALIAS|          641|        647|                Parties|  ALIAS|has_collective_alias| 0.5040909|
+--------+-------------+-----------+-----------------------------------+-------+-------------+-----------+-----------------------+-------+--------------------+----------+
{%- endcapture -%}

{%- capture model_python_finance -%}
from johnsnowlabs import nlp, finance
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

text_splitter = finance.TextSplitter()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") \
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model_date = finance.NerModel.pretrained("finner_sec_dates", "en", "finance/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner_dates")

ner_converter_date = finance.NerConverterInternal()\
    .setInputCols(["sentence","token","ner_dates"])\
    .setOutputCol("ner_chunk_date")

ner_model_org= finance.NerModel.pretrained("finner_orgs_prods_alias", "en", "finance/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner_orgs")

ner_converter_org = finance.NerConverterInternal()\
    .setInputCols(["sentence","token","ner_orgs"])\
    .setOutputCol("ner_chunk_org")\

chunk_merger = finance.ChunkMergeApproach()\
    .setInputCols('ner_chunk_org', "ner_chunk_date")\
    .setOutputCol('ner_chunk')

pos = nlp.PerceptronModel.pretrained()\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("pos")

dependency_parser = nlp.DependencyParserModel().pretrained("dependency_conllu", "en")\
    .setInputCols(["sentence", "pos", "token"])\
    .setOutputCol("dependencies")

re_filter = finance.RENerChunksFilter()\
    .setInputCols(["ner_chunk", "dependencies"])\
    .setOutputCol("re_ner_chunk")\
    .setRelationPairs(["ORG-ORG", "ORG-DATE"])\
    .setMaxSyntacticDistance(10)

reDL = finance.RelationExtractionDLModel().pretrained('finre_acquisitions_subsidiaries_md', 'en', 'finance/models')\
    .setInputCols(["re_ner_chunk", "sentence"])\
    .setOutputCol("relation")\
    .setPredictionThreshold(0.1)

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    text_splitter,
    tokenizer,
    embeddings,
    ner_model_date,
    ner_converter_date,
    ner_model_org,
    ner_converter_org,
    chunk_merger,
    pos,
    dependency_parser,
    re_filter,
    reDL])

text = """In fiscal 2020, Cadence acquired all of the outstanding equity of AWR Corporation (“AWR”) and Integrand Software, Inc. (“Integrand”)."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

from pyspark.sql import functions as F

result.select(
    F.explode(F.arrays_zip(result.relation.metadata, result.relation.result)).alias("cols")).select(
    F.expr("cols['0']['sentence']").alias("sentence"),
    F.expr("cols['0']['entity1_begin']").alias("entity1_begin"),
    F.expr("cols['0']['entity1_end']").alias("entity1_end"),
    F.expr("cols['0']['chunk1']").alias("chunk1"),
    F.expr("cols['0']['entity1']").alias("entity1"),
    F.expr("cols['0']['entity2_begin']").alias("entity2_begin"),
    F.expr("cols['0']['entity2_end']").alias("entity2_end"),
    F.expr("cols['0']['chunk2']").alias("chunk2"),
    F.expr("cols['0']['entity2']").alias("entity2"),
    F.expr("cols['1']").alias("relation"),
    F.expr("cols['0']['confidence']").alias("confidence"),
).filter("relation != 'no_rel'").show(truncate=70)

+--------+-------------+-----------+-----------------------+-------+-------------+-----------+---------------+-------+--------------------+----------+
|sentence|entity1_begin|entity1_end|                 chunk1|entity1|entity2_begin|entity2_end|         chunk2|entity2|            relation|confidence|
+--------+-------------+-----------+-----------------------+-------+-------------+-----------+---------------+-------+--------------------+----------+
|       0|           16|         22|                Cadence|    ORG|            3|         13|    fiscal 2020|   DATE|has_acquisition_date|0.99687237|
|       0|           66|         80|        AWR Corporation|    ORG|            3|         13|    fiscal 2020|   DATE|has_acquisition_date|  0.993112|
|       0|           94|        116|Integrand Software, Inc|    ORG|            3|         13|    fiscal 2020|   DATE|has_acquisition_date| 0.9741451|
|       0|           66|         80|        AWR Corporation|    ORG|           16|         22|        Cadence|    ORG|     was_acquired_by|  0.997124|
|       0|           94|        116|Integrand Software, Inc|    ORG|           16|         22|        Cadence|    ORG|     was_acquired_by|0.99910504|
|       0|           94|        116|Integrand Software, Inc|    ORG|           66|         80|AWR Corporation|    ORG|     was_acquired_by|0.93245244|
+--------+-------------+-----------+-----------------------+-------+-------------+-----------+---------------+-------+--------------------+----------+
{%- endcapture -%}

{%- capture model_scala_finance -%}
import spark.implicits._

val document_assembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val text_splitter = new TextSplitter() 
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val embeddings = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base", "en", "finance/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

val ner_model_date = NerModel.pretrained("finner_sec_dates", "en", "finance/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner_dates")

val ner_converter_date = new NerConverterInternal()
  .setInputCols(Array("sentence", "token", "ner_dates"))
  .setOutputCol("ner_chunk_date")

val ner_model_org = FinanceNerModel.pretrained("finner_orgs_prods_alias", "en", "finance/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner_orgs")

val ner_converter_org = new NerConverterInternal()
  .setInputCols(Array("sentence", "token", "ner_orgs"))
  .setOutputCol("ner_chunk_org")

val chunk_merger = new ChunkMergeApproach()
  .setInputCols(Array("ner_chunk_org", "ner_chunk_date"))
  .setOutputCol("ner_chunk")

val pos = PerceptronModel.pretrained()
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("pos")

val dependency_parser = DependencyParserModel.pretrained("dependency_conllu", "en")
  .setInputCols(Array("sentence", "pos", "token"))
  .setOutputCol("dependencies")

val re_filter = new RENerChunksFilter()
  .setInputCols(Array("ner_chunk", "dependencies"))
  .setOutputCol("re_ner_chunk")
  .setRelationPairs(Array("ORG-ORG", "ORG-DATE"))
  .setMaxSyntacticDistance(10)

val reDL = RelationExtractionDLModel.pretrained("finre_acquisitions_subsidiaries_md", "en", "finance/models")
  .setInputCols(Array("re_ner_chunk", "sentence"))
  .setOutputCol("relation")
  .setPredictionThreshold(0.1)

val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    text_splitter,
    tokenizer,
    embeddings,
    ner_model_date,
    ner_converter_date,
    ner_model_org,
    ner_converter_org,
    chunk_merger,
    pos,
    dependency_parser,
    re_filter,
    reDL
  ))

text = """In fiscal 2020, Cadence acquired all of the outstanding equity of AWR Corporation (“AWR”) and Integrand Software, Inc. (“Integrand”)."""

val data = Seq(text).toDF("text")

val result = pipeline.fit(data).transform(data)

+--------+-------------+-----------+-----------------------+-------+-------------+-----------+---------------+-------+--------------------+----------+
|sentence|entity1_begin|entity1_end|                 chunk1|entity1|entity2_begin|entity2_end|         chunk2|entity2|            relation|confidence|
+--------+-------------+-----------+-----------------------+-------+-------------+-----------+---------------+-------+--------------------+----------+
|       0|           16|         22|                Cadence|    ORG|            3|         13|    fiscal 2020|   DATE|has_acquisition_date|0.99687237|
|       0|           66|         80|        AWR Corporation|    ORG|            3|         13|    fiscal 2020|   DATE|has_acquisition_date|  0.993112|
|       0|           94|        116|Integrand Software, Inc|    ORG|            3|         13|    fiscal 2020|   DATE|has_acquisition_date| 0.9741451|
|       0|           66|         80|        AWR Corporation|    ORG|           16|         22|        Cadence|    ORG|     was_acquired_by|  0.997124|
|       0|           94|        116|Integrand Software, Inc|    ORG|           16|         22|        Cadence|    ORG|     was_acquired_by|0.99910504|
|       0|           94|        116|Integrand Software, Inc|    ORG|           66|         80|AWR Corporation|    ORG|     was_acquired_by|0.93245244|
+--------+-------------+-----------+-----------------------+-------+-------------+-----------+---------------+-------+--------------------+----------+
{%- endcapture -%}

{%- capture model_api_link -%}
[RelationExtractionDLModel](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/re/RelationExtractionDLModel.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[RelationExtractionDLModel](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/re/relation_extraction_dl/index.html#sparknlp_jsl.annotator.re.relation_extraction_dl.RelationExtractionDLModel)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[RelationExtractionDLModelNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/RelationExtractionDLModel.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical
model_python_legal=model_python_legal
model_scala_legal=model_scala_legal
model_python_finance=model_python_finance
model_scala_finance=model_scala_finance
model_api_link=model_api_link
model_python_api_link=model_python_api_link
model_notebook_link=model_notebook_link%}
