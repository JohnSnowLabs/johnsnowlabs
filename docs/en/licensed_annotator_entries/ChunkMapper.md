{%- capture title -%}
ChunkMapper
{%- endcapture -%}

{%- capture approach -%}
approach
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}

We can use ChunkMapper to map entities with their associated code/reference based on pre-defined dictionaries. 

This is the AnnotatorModel of the ChunkMapper, which can be used to access pretrained models with the `.pretrained()` or `.load()` methods. To train a new model, check the documentation of the [ChunkMapperApproach](https://nlp.johnsnowlabs.com/docs/en/licensed_annotators#chunkmapperapproach) annotator. 

The annotator also allows using fuzzy matching, which can take into consideration parts of the tokens tha can map even when word order is different, char ngrams that can map even when thre are typos, and using fuzzy distance metric (Jaccard, Levenshtein, etc.).

Parametres:

- `setRels` *(List[str])*: Relations that we are going to use to map the chunk

- `setLowerCase` *(Boolean)*: Set if we want to map the chunks in lower case or not (Default: True)

- `setAllowMultiTokenChunk` *(Boolean)*: Whether to skip relations with multitokens (Default: True)

- `setMultivaluesRelations` *(Boolean)*:  Whether to decide to return all values in a relation together or separately (Default: False)


Example usage and more details can be found on Spark NLP Workshop repository accessible in GitHub, for example the notebook [Healthcare Chunk Mapping](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/26.Chunk_Mapping.ipynb).

{%- endcapture -%}

{%- capture model_input_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
LABEL_DEPENDENCY
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

documenter = nlp.DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

sentencer = nlp.SentenceDetector()\
  .setInputCols(["document"])\
  .setOutputCol("sentences")

tokenizer = nlp.Tokenizer()\
  .setInputCols(["sentences"])\
  .setOutputCol("tokens")

words_embedder = nlp.WordEmbeddingsModel()\
  .pretrained("embeddings_clinical", "en", "clinical/models")\
  .setInputCols(["sentences", "tokens"])\
  .setOutputCol("embeddings")

ner_tagger = medical.NerModel()\
  .pretrained("ner_posology", "en", "clinical/models")\
  .setInputCols("sentences", "tokens", "embeddings")\
  .setOutputCol("ner_tags")

ner_converter = medical.NerConverterInternal()\
  .setInputCols(["sentences", "tokens", "ner_tags"])\
  .setOutputCol("ner_chunks")\
  .setWhiteList(["DRUG"])

chunkToDoc = nlp.Chunk2Doc()\
  .setInputCols("ner_chunks")\
  .setOutputCol("ner_chunks_doc")

sbert_embedder = nlp.BertSentenceEmbeddings\
  .pretrained("sbiobert_base_cased_mli", "en","clinical/models")\
  .setInputCols(["ner_chunks_doc"])\
  .setOutputCol("sbert_embeddings")\
  .setCaseSensitive(False)

rxnorm_resolver = medical.SentenceEntityResolverModel\
  .pretrained("sbiobertresolve_rxnorm_augmented", "en", "clinical/models")\
  .setInputCols(["sbert_embeddings"])\
  .setOutputCol("rxnorm_code")\
  .setDistanceFunction("EUCLIDEAN")\

resolver2chunk = medical.Resolution2Chunk()\
  .setInputCols(["rxnorm_code"]) \
  .setOutputCol("rxnorm_chunk")\

chunkerMapper = medical.ChunkMapperModel.pretrained("rxnorm_drug_brandname_mapper", "en", "clinical/models")\
  .setInputCols(["rxnorm_chunk"])\
  .setOutputCol("rxnorm_drug_brandname_mapper")\
  .setRels(["rxnorm_brandname"])

pipeline = nlp.Pipeline(
    stages = [
        documenter,
        sentencer,
        tokenizer,
        words_embedder,
        ner_tagger,
        ner_converter,
        chunkToDoc,
        sbert_embedder,
        rxnorm_resolver,
        resolver2chunk,
        chunkerMapper
        ])


data = spark.createDataFrame([["The doctor prescribed Sinequan 150 MG for depression and Zonalon 50 mg for managing skin itching"]]).toDF("text")

result= pipeline.fit(data).transform(data)

result.select(F.explode(F.arrays_zip(result.ner_chunks.result,
                                     result.rxnorm_code.result)).alias("cols"))\
                  .select(F.expr("cols['0']").alias("ner_chunks"),
                          F.expr("cols['1']").alias("rxnorm_code")).show(15, truncate=100)

+----------+-----------+----------------------------+
|ner_chunks|rxnorm_code|rxnorm_drug_brandname_mapper|
+----------+-----------+----------------------------+
|  Sinequan|     224915|         Sinequan (Sinequan)|
|   Zonalon|       9801|           Zonalon (Zonalon)|
+----------+-----------+----------------------------+
{%- endcapture -%}

{%- capture model_python_finance -%}
from johnsnowlabs import nlp, finance

document_assembler = nlp.DocumentAssembler()\
  .setInputCol('text')\
  .setOutputCol('document')

tokenizer = nlp.Tokenizer()\
  .setInputCols("document")\
  .setOutputCol("token")

embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") \
  .setInputCols(["document", "token"]) \
  .setOutputCol("embeddings")

ner_model = finance.NerModel.pretrained("finner_ticker", "en", "finance/models")\
  .setInputCols(["document", "token", "embeddings"])\
  .setOutputCol("ner")

ner_converter = nlp.NerConverter()\
  .setInputCols(["document", "token", "ner"])\
  .setOutputCol("ner_chunk")

CM = finance.ChunkMapperModel.pretrained('finmapper_nasdaq_ticker_stock_screener', 'en', 'finance/models')\
  .setInputCols(["ner_chunk"])\
  .setOutputCol("mappings")

pipeline = nlp.Pipeline().setStages([
  document_assembler,
  tokenizer, 
  embeddings,
  ner_model, 
  ner_converter, 
  CM])
                                 
text = ["""There are some serious purchases and sales of AMZN stock today."""]

data = spark.createDataFrame([text]).toDF("text")

result = pipeline.fit(data).transform(data)

+------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result|result                                                                                                                                                             |
+------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[AMZN]|[AMZN, Amazon.com Inc. Common Stock, $98.12, 2.85, 2.991%, 9.98556270184E11, United States, 1997, 85412563, Consumer Discretionary, Catalog/Specialty Distribution]|
+------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_python_legal -%}
from johnsnowlabs import nlp, legal

document_assembler = nlp.DocumentAssembler()\
  .setInputCol('text')\
  .setOutputCol('document')

tokenizer = nlp.Tokenizer()\
  .setInputCols("document")\
  .setOutputCol("token")

embeddings = nlp.WordEmbeddingsModel.pretrained('glove_100d') \
  .setInputCols(['document', 'token']) \
  .setOutputCol('embeddings')

ner_model = nlp.NerDLModel.pretrained("onto_100", "en") \
  .setInputCols(["document", "token", "embeddings"]) \
  .setOutputCol("ner")
 
ner_converter = nlp.NerConverter()\
  .setInputCols(["document", "token", "ner"])\
  .setOutputCol("ner_chunk")\
  .setWhiteList(["CARDINAL"])

CM = legal.ChunkMapperModel().pretrained("legmapper_edgar_irs", "en", "legal/models")\
  .setInputCols(["ner_chunk"])\
  .setOutputCol("mappings")

pipeline = nlp.Pipeline().setStages([
  document_assembler,
  tokenizer, 
  embeddings,
  ner_model, 
  ner_converter, 
  CM])

text = ["""873474341 is an American multinational corporation that is engaged in the design, development, manufacturing, and worldwide marketing and sales of footwear, apparel, equipment, accessories, and services"""]

data = spark.createDataFrame([text]).toDF("text")

result= pipeline.fit(data).transform(data)

+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result     |result                                                                                                                                                               |
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[873474341]|[Masterworks 096, LLC, RETAIL-RETAIL STORES, NEC [5990], 5990, 873474341, 1231, NY, DE, 225 LIBERTY STREET, NEW YORK, NY, 10281, 2035185172, , , 2022-01-10, 1894064]|
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_scala_medical -%}

import spark.implicits._

val documenter = new DocumentAssembler()
 .setInputCol("text") 
 .setOutputCol("document") 

val sentencer = new SentenceDetector()
 .setInputCols("document")
 .setOutputCol("sentences") 

val tokenizer = new Tokenizer()
 .setInputCols("sentences")
 .setOutputCol("tokens") 

val words_embedder = WordEmbeddingsModel
 .pretrained("embeddings_clinical","en","clinical/models") 
 .setInputCols(Array("sentences","tokens")) 
 .setOutputCol("embeddings") 

val ner_tagger = MedicalNerModel
 .pretrained("ner_posology","en","clinical/models") 
 .setInputCols(Array("sentences","tokens","embeddings"))
 .setOutputCol("ner_tags") 

val ner_converter = new NerConverterInternal()
 .setInputCols(Array("sentences","tokens","ner_tags")) 
 .setOutputCol("ner_chunks") 
 .setWhiteList("DRUG") 

val chunkToDoc = new Chunk2Doc()
 .setInputCols("ner_chunks") 
 .setOutputCol("ner_chunks_doc") 

val sbert_embedder = BertSentenceEmbeddings
 .pretrained("sbiobert_base_cased_mli","en","clinical/models") 
 .setInputCols("ner_chunks_doc")
 .setOutputCol("sbert_embeddings") 
 .setCaseSensitive(false) 

val rxnorm_resolver = SentenceEntityResolverModel
 .pretrained("sbiobertresolve_rxnorm_augmented","en","clinical/models") 
 .setInputCols("sbert_embeddings")
 .setOutputCol("rxnorm_code") 
 .setDistanceFunction("EUCLIDEAN") 

val resolver2chunk = new Resolution2Chunk()
 .setInputCols("rxnorm_code")
 .setOutputCol("rxnorm_chunk") 

val chunkerMapper = ChunkMapperModel.pretrained("rxnorm_drug_brandname_mapper","en","clinical/models")
 .setInputCols("rxnorm_chunk")
 .setOutputCol("rxnorm_drug_brandname_mapper") 
 .setRels(Array("rxnorm_brandname")) 

val pipeline = new Pipeline().setStages(Array(
 documenter, 
 sentencer, 
 tokenizer, 
 words_embedder, 
 ner_tagger, 
 ner_converter, 
 chunkToDoc, 
 sbert_embedder, 
 rxnorm_resolver, 
 resolver2chunk,
  chunkerMapper )) 

val text ="""The doctor prescribed Sinequan 150 MG for depression and Zonalon 50 mg for managing skin itching"""
val data = Seq(text).toDF("text")

val result= mapper_pipeline.fit(data).transform(data)

+----------+-----------+----------------------------+
|ner_chunks|rxnorm_code|rxnorm_drug_brandname_mapper|
+----------+-----------+----------------------------+
|  Sinequan|     224915|         Sinequan (Sinequan)|
|   Zonalon|       9801|           Zonalon (Zonalon)|
+----------+-----------+----------------------------+

{%- endcapture -%}

{%- capture model_scala_finance -%}
import spark.implicits._

val document_assembler = new DocumentAssembler()
 .setInputCol("text") 
 .setOutputCol("document") 

val tokenizer = new Tokenizer()
 .setInputCols("document") 
 .setOutputCol("token") 

val embeddings = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en")
 .setInputCols(Array("document","token")) 
 .setOutputCol("embeddings") 

val ner_model = FinanceNerModel.pretrained("finner_ticker","en","finance/models")
 .setInputCols(Array("document","token","embeddings")) 
 .setOutputCol("ner") 

val ner_converter = new NerConverter()
 .setInputCols(Array("document","token","ner")) 
 .setOutputCol("ner_chunk") 

val CM = ChunkMapperModel.pretrained("finmapper_nasdaq_ticker_stock_screener","en","finance/models")
 .setInputCols("ner_chunk")
 .setOutputCol("mappings") 

val pipeline = new Pipeline().setStages(Array( 
  document_assembler, 
  tokenizer, 
  embeddings, 
  ner_model, 
  ner_converter, 
  CM) ) 
 
val text ="""There are some serious purchases and sales of AMZN stock today."""
val data = Seq(text).toDF("text")

val result = pipeline.fit(data).transform(data)

+------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result|result                                                                                                                                                             |
+------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[AMZN]|[AMZN, Amazon.com Inc. Common Stock, $98.12, 2.85, 2.991%, 9.98556270184E11, United States, 1997, 85412563, Consumer Discretionary, Catalog/Specialty Distribution]|
+------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}

{%- capture model_scala_legal -%}
import spark.implicits._

val document_assembler = new DocumentAssembler()
 .setInputCol("text") 
 .setOutputCol("document") 

val tokenizer = new Tokenizer()
 .setInputCols("document") 
 .setOutputCol("token") 

val embeddings = WordEmbeddingsModel.pretrained("glove_100d")
 .setInputCols(Array("document","token")) 
 .setOutputCol("embeddings") 

val ner_model = NerDLModel.pretrained("onto_100","en")
 .setInputCols(Array("document","token","embeddings")) 
 .setOutputCol("ner") 

val ner_converter = new NerConverter()
 .setInputCols(Array("document","token","ner")) 
 .setOutputCol("ner_chunk") 
 .setWhiteList(Array("CARDINAL")) 

val CM = ChunkMapperModel.pretrained("legmapper_edgar_irs","en","legal/models") 
.setInputCols("ner_chunk")
.setOutputCol("mappings") 

val pipeline = new Pipeline().setStages(Array( 
  document_assembler, 
  tokenizer, 
  embeddings, 
  ner_model, 
  ner_converter, 
  CM) ) 

val text ="""873474341 is an American multinational corporation that is engaged in the design,development,manufacturing,and worldwide marketing and sales of footwear,apparel,equipment,accessories,and services"""
val data = Seq(text).toDF("text")

val result= pipeline.fit(data).transform(data)

+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result     |result                                                                                                                                                               |
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[873474341]|[Masterworks 096, LLC, RETAIL-RETAIL STORES, NEC [5990], 5990, 873474341, 1231, NY, DE, 225 LIBERTY STREET, NEW YORK, NY, 10281, 2035185172, , , 2022-01-10, 1894064]|
+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}

{%- capture model_api_link -%}
[ChunkMapperModel](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/finance/chunk_classification/resolution/ChunkMapperModel.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[ChunkMapperModel](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/chunker/chunkmapper/index.html#sparknlp_jsl.annotator.chunker.chunkmapper.ChunkMapperModel)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[ChunkMapperModelNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ChunkMapperModel.ipynb)
{%- endcapture -%}

{%- capture approach_description -%}

We can use ChunkMapper to map entities with their associated code/reference based on pre-defined dictionaries. 

This is the AnnotatorApproach of the ChunkMapper, which can be used to train ChunkMapper models by giving a custom mapping dictionary. To use pretriained models, check the documentation of the [ChunkMapperModel](https://nlp.johnsnowlabs.com/docs/en/licensed_annotators#chunkmappermodel) annotator.

The annotator also allows using fuzzy matching, which can take into consideration parts of the tokens tha can map even when word order is different, char ngrams that can map even when thre are typos, and using fuzzy distance metric (Jaccard, Levenshtein, etc.).

Example usage and more details can be found on Spark NLP Workshop repository accessible in GitHub, for example the notebook [Healthcare Chunk Mapping](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/26.Chunk_Mapping.ipynb).

{%- endcapture -%}

{%- capture approach_input_anno -%}
CHUNK
{%- endcapture -%}

{%- capture approach_output_anno -%}
LABEL_DEPENDENCY
{%- endcapture -%}

{%- capture approach_python_medical -%}
from johnsnowlabs import nlp, medical

# First, create a dictionay in JSON format following this schema:
import json
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

with open('sample_drug.json', 'w', encoding='utf-8') as f:
    json.dump(data_set, f, ensure_ascii=False, indent=4)


# Create a pipeline
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

#NER model to detect drug in the text
clinical_ner =  medical.NerModel.pretrained("ner_posology_small","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner")\
    .setLabelCasing("upper")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DRUG"])

chunkerMapper =  medical.ChunkMapperApproach()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setDictionary("/content/sample_drug.json")\
    .setRels(["action"]) #or treatment

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    clinical_ner,
    ner_converter,
    chunkerMapper])

text = ["The patient was given 1 unit of metformin daily."]

test_data = spark.createDataFrame([text]).toDF("text")

model = pipeline.fit(test_data)
res= model.transform(test_data)

model.stages[-1].write().save("models/drug_mapper")

{%- endcapture -%}

{%- capture approach_python_finance -%}
from johnsnowlabs import nlp, finance

# First, create a dictionay in JSON format following this schema:
import json

data_set= {
  "mappings": [
    {
      "key": "Rayton Solar Inc.",
      "relations": [
        {
          "key": "name",
          "values" : ['Rayton Solar Inc.']
        },
        {
          "key": "sic",
          "values" : ['SEMICONDUCTORS & RELATED DEVICES [3674]']
        }]
    }]
}

with open('sample_finance.json', 'w', encoding='utf-8') as f:
    json.dump(data_set, f, ensure_ascii=False, indent=4)

# Create a pipeline
document_assembler = nlp.DocumentAssembler()\
  .setInputCol('text')\
  .setOutputCol('document')

sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
  .setInputCols("sentence")\
  .setOutputCol("token")

word_embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") \
  .setInputCols(["sentence", "token"]) \
  .setOutputCol("embeddings")

finance_ner = finance.NerModel.pretrained("finner_orgs_prods_alias", "en", "finance/models")\
  .setInputCols(["sentence", "token", "embeddings"])\
  .setOutputCol("ner")

ner_converter = nlp.NerConverter()\
  .setInputCols(["sentence","token","ner"])\
  .setOutputCol("ner_chunk")\
  .setWhiteList(["ORG"]) # Return only ORG entities

chunkerMapper =  finance.ChunkMapperApproach()\
  .setInputCols(["ner_chunk"])\
  .setOutputCol("mappings")\
  .setDictionary("/content/sample_finance.json")\
  .setRels(all_rels)

pipeline = nlp.Pipeline().setStages([
  document_assembler,
  sentence_detector,
  tokenizer,
  word_embeddings,
  finance_ner,
  ner_converter,
  chunkerMapper])

text = ["AWA Group LP intends to pay dividends on the Common Units on a quarterly basis at an annual rate of 8.00% of the Offering Price. "]

test_data = spark.createDataFrame([text]).toDF("text")

model = pipeline.fit(test_data)
res= model.transform(test_data)

model.stages[-1].write().save("models/finance_mapper")

{%- endcapture -%}

{%- capture approach_python_legal -%}
from johnsnowlabs import nlp, legal

# First, create a dictionay in JSON format following this schema:
import json

data_set= {
  "mappings": [
    {
      "key": "Rayton Solar Inc.",
      "relations": [
        {
          "key": "name",
          "values" : ['Rayton Solar Inc.']
        },
        {
          "key": "sic",
          "values" : ['SEMICONDUCTORS & RELATED DEVICES [3674]']
        }]
    }]
}

with open('sample_legal.json', 'w', encoding='utf-8') as f:
    json.dump(data_set, f, ensure_ascii=False, indent=4)

# Create a pipeline
document_assembler = nlp.DocumentAssembler()\
  .setInputCol('text')\
  .setOutputCol('document')

sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
  .setInputCols("sentence")\
  .setOutputCol("token")

word_embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") \
  .setInputCols(["sentence", "token"]) \
  .setOutputCol("embeddings")

legal_ner = legal.NerModel.pretrained("legner_org_per_role_date", "en", "legal/models")\
  .setInputCols(["sentence", "token", "embeddings"])\
  .setOutputCol("ner")

ner_converter = nlp.NerConverter()\
  .setInputCols(["sentence","token","ner"])\
  .setOutputCol("ner_chunk")\
  .setWhiteList(["ORG"]) # Return only ORG entities

chunkerMapper =  legal.ChunkMapperApproach()\
  .setInputCols(["ner_chunk"])\
  .setOutputCol("mappings")\
  .setDictionary("/content/sample_legal.json")\
  .setRels(all_rels)

pipeline = nlp.Pipeline().setStages([
  document_assembler,
  sentence_detector,
  tokenizer,
  word_embeddings,
  legal_ner,
  ner_converter,
  chunkerMapper])

text = ["AWA Group LP intends to pay dividends on the Common Units on a quarterly basis at an annual rate of 8.00% of the Offering Price. "]

test_data = spark.createDataFrame([text]).toDF("text")

model = pipeline.fit(test_data)
res= model.transform(test_data)

model.stages[-1].write().save("models/legal_mapper")

{%- endcapture -%}

{%- capture approach_scala_medical -%}
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
 .setOutputCol("embeddings") //NER model to detect drug in the text 

val clinical_ner = MedicalNerModel.pretrained("ner_posology_small","en","clinical/models")
 .setInputCols(Array("sentence","token","embeddings")) 
 .setOutputCol("ner") 
 .setLabelCasing("upper") 

val ner_converter = new NerConverterInternal()
 .setInputCols(Array("sentence","token","ner")) 
 .setOutputCol("ner_chunk") 
 .setWhiteList(Array("DRUG")) 

val chunkerMapper = new ChunkMapperApproach()
 .setInputCols("ner_chunk") 
 .setOutputCol("mappings") 
 .setDictionary("/content/sample_drug.json") 
 .setRels(Array("action") ) //or treatment 

val pipeline = new Pipeline()
 .setStages(Array(
  document_assembler, 
  sentence_detector, 
  tokenizer, 
  word_embeddings, 
  clinical_ner, 
  ner_converter, 
  chunkerMapper) ) 
val text = new Array("The patient was given 1 unit of metformin daily.") 

val test_data = seq(Array(text)) .toDF("text") 
val model = pipeline.fit(test_data) 

res= model.transform(test_data) 
model.stagesArray(-1) .write() .save("models/drug_mapper") 
{%- endcapture -%}

{%- capture approach_scala_finance -%}
import spark.implicits._

val document_assembler = new DocumentAssembler()
 .setInputCol("text") 
 .setOutputCol("document") 

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
 .setInputCols("document")
 .setOutputCol("sentence") 

val tokenizer = new Tokenizer()
 .setInputCols("sentence") 
 .setOutputCol("token") 

val word_embeddings = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en")
 .setInputCols(Array("sentence","token") ) 
 .setOutputCol("embeddings") 

val finance_ner = FinanceNerModel.pretrained("finner_orgs_prods_alias","en","finance/models")
 .setInputCols(Array("sentence","token","embeddings") ) 
 .setOutputCol("ner") 

val ner_converter = new NerConverter()
 .setInputCols(Array("sentence","token","ner") ) 
 .setOutputCol("ner_chunk") 
 .setWhiteList(Array("ORG") ) // Return only ORG entities 

val chunkerMapper = new ChunkMapperApproach()
 .setInputCols("ner_chunk")
 .setOutputCol("mappings") 
 .setDictionary("/content/sample_json") 
 .setRels(all_rels) 

val pipeline = new Pipeline()
 .setStages(Array( 
  document_assembler, 
  sentence_detector, 
  tokenizer, 
  word_embeddings, 
  finance_ner, 
  ner_converter, 
  chunkerMapper) ) 

val text = new Array("AWA Group LP intends to pay dividends on the Common Units on a quarterly basis at an annual rate of 8.00% of the Offering Price. ") 

val test_data = seq(Array(text)).toDF("text") 

val model = pipeline.fit(test_data) 
res= model.transform(test_data) 

model.stagesArray(-1) .write() .save("models/finance_mapper") 
{%- endcapture -%}

{%- capture approach_scala_legal -%}
import spark.implicits._
 
val document_assembler = new DocumentAssembler()
 .setInputCol("text") 
 .setOutputCol("document") 

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
 .setInputCols("document")
 .setOutputCol("sentence") 

val tokenizer = new Tokenizer()
 .setInputCols("sentence") 
 .setOutputCol("token") 

val word_embeddings = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en")
 .setInputCols(Array("sentence","token")) 
 .setOutputCol("embeddings") 

val legal_ner = LegalNerModel.pretrained("legner_org_per_role_date","en","legal/models")
 .setInputCols(Array("sentence","token","embeddings")) 
 .setOutputCol("ner") 

val ner_converter = new NerConverter()
 .setInputCols(Array("sentence","token","ner")) 
 .setOutputCol("ner_chunk") 
 .setWhiteList("ORG") // Return only ORG entities 

val chunkerMapper = new ChunkMapperApproach()
 .setInputCols("ner_chunk")
 .setOutputCol("mappings") 
 .setDictionary("/content/sample_json") 
 .setRels(all_rels) 

val pipeline = new Pipeline()
 .setStages(Array( 
  document_assembler, 
  sentence_detector, 
  tokenizer, 
  word_embeddings, 
  legal_ner, 
  ner_converter, 
  chunkerMapper) ) 

val text = new Array("AWA Group LP intends to pay dividends on the Common Units on a quarterly basis at an annual rate of 8.00% of the Offering Price. ") 
val test_data = seq(Array(text) ) .toDF("text") 
val model = pipeline.fit(test_data) 

res= model.transform(test_data) 
model.stagesArray(-1) .write() .save("models/legal_mapper")
{%- endcapture -%}

{%- capture approach_api_link -%}
[ChunkMapperApproach](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/finance/chunk_classification/resolution/ChunkMapperApproach.html)
{%- endcapture -%}

{%- capture approach_python_api_link -%}
[ChunkMapperApproach](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/chunker/chunkmapper/index.html#sparknlp_jsl.annotator.chunker.chunkmapper.ChunkMapperApproach)
{%- endcapture -%}

{%- capture approach_notebook_link -%}
[ChunkMapperApproachModelNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ChunkMapperApproach.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
approach=approach
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_python_finance=model_python_finance
model_python_legal=model_python_legal
model_scala_medical=model_scala_medical
model_scala_finance=model_scala_finance
model_scala_legal=model_scala_legal
model_api_link=model_api_link
model_python_api_link=model_python_api_link
model_notebook_link=model_notebook_link
approach_description=approach_description
approach_input_anno=approach_input_anno
approach_output_anno=approach_output_anno
approach_python_medical=approach_python_medical
approach_python_finance=approach_python_finance
approach_python_legal=approach_python_legal
approach_scala_medical=approach_scala_medical
approach_scala_finance=approach_scala_finance
approach_scala_legal=approach_scala_legal
approach_api_link=approach_api_link
approach_python_api_link=approach_python_api_link
approach_notebook_link=approach_notebook_link
%}
