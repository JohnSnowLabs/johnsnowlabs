{%- capture title -%}
ChunkMerge
{%- endcapture -%}

{%- capture approach -%}
approach
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
Merges entities coming from different CHUNK annotations
{%- endcapture -%}

{%- capture model_input_anno -%}
CHUNK, CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_api_link -%}
[ChunkMergeModel](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/merge/ChunkMergeModel.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[ChunkMergeModel](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/merge/chunk_merge/index.html#sparknlp_jsl.annotator.merge.chunk_merge.ChunkMergeModel)
{%- endcapture -%}

{%- capture model_description -%}
Merges two chunk columns coming from two annotators(NER, ContextualParser or any other annotator producing
chunks). The merger of the two chunk columns is made by selecting one chunk from one of the columns according
to certain criteria.
The decision on which chunk to select is made according to the chunk indices in the source document.
(chunks with longer lengths and highest information will be kept from each source)
Labels can be changed by setReplaceDictResource.

`ChunkMergeModel` has the same parameters as `ChunkMergeApproach` except for `setFalsePositivesResource` and `setReplaceDictResource` parameters.
- `inputCols`: The name of the columns containing the input annotations. It can read either a String column or an Array.
- `outputCol`: The name of the column in Document type that is generated. We can specify only one column here.v
- `mergeOverlapping`: (Boolean) Sets whether to merge overlapping matched chunks. Default `True`.
- `blackList`: (String List) If defined, list of entities to ignore. The rest will be processed.
- `whiteList`: (String List) If defined, list of entities to accept.
- `selectionStrategy`: (String) Sets Whether to select annotations sequentially based on annotation order `Sequential` or using any other available strategy; currently only `Sequential` and `DiverseLonger` are available. Default `DiverseLonger`.
- `orderingFeatures`: (String List) The ordering features to use for overlapping entities. Possible values are `ChunkBegin, ChunkLength, ChunkPrecedence, ChunkConfidence.`
- `defaultConfidence`: (Float) Sets when ChunkConfidence ordering feature is included and a given annotation does not have any confidence. The value of this param will be used as confidence score for annotations without a confidence score.
- `chunkPrecedence`: (String List) Sets the precedence order when a chunk is labeled by two models.
- `chunkPrecedenceValuePrioritization`: (String List) Sets when ChunkPrecedence ordering feature is used. This param contains an Array of comma-separated values representing the desired order of prioritization for the values in the metadata fields included from chunkPrecedence.

All the parameters can be set using the corresponding set method in camel case. For example, `.setInputcols()`.
{%- endcapture -%}

{%- capture model_input_anno -%}
CHUNK, CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import *
# Annotator that transforms a text column from dataframe into an Annotation ready for NLP
documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

# Sentence Detector annotator, processes various sentences per line
sentenceDetector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

# Tokenizer splits words in a relevant format for NLP
tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

# Clinical word embeddings trained on PubMED dataset
word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")


# 1- ner_clinical model
clinical_ner = medical.NerModel.pretrained("ner_clinical", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("clinical_ner")

clinical_ner_converter = medical.NerConverterInternal() \
    .setInputCols(["sentence", "token", "clinical_ner"]) \
    .setOutputCol("clinical_ner_chunk")


# 2- posology ner model
posology_ner = medical.NerModel.pretrained("ner_posology", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("posology_ner")

posology_ner_converter = medical.NerConverterInternal() \
    .setInputCols(["sentence", "token", "posology_ner"]) \
    .setOutputCol("posology_ner_chunk")


# 3- generate a text matcher annotator that extracts female related entities
entities = ['she', 'her', 'girl', 'woman', 'women', 'womanish', 'womanlike', 'womanly', 'madam', 'madame', 'senora', 'lady', 'miss', 'girlfriend', 'wife', 'bride', 'misses', 'mrs.', 'female']
with open ('female_entities.txt', 'w') as f:
    for i in entities:
        f.write(i+'\n')

# Find female entities using TextMatcher
female_entity_extractor = nlp.TextMatcher() \
    .setInputCols(["sentence",'token'])\
    .setOutputCol("female_entities")\
    .setEntities("female_entities.txt")\
    .setCaseSensitive(False)\
    .setEntityValue('female_entity')

from sparknlp.common.read_as import ReadAs

# Chunk Merge annotator is used to merge columns
chunk_merger = medical.ChunkMergeModel()\
    .setInputCols("posology_ner_chunk", 'clinical_ner_chunk', "female_entities")\
    .setOutputCol('merged_ner_chunk')\
    .setMergeOverlapping(True) \
    .setOrderingFeatures(["ChunkConfidence"])\
    .setSelectionStrategy("Sequential")\
    .setDefaultConfidence(0.8)\
    .setBlackList(["DURATION"])

nlpPipeline = nlp.Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    word_embeddings,
    clinical_ner,
    clinical_ner_converter,
    posology_ner,
    posology_ner_converter,
    female_entity_extractor,
    chunk_merger])

sample_text = """A 28 year old female with a history of gestational diabetes mellitus diagnosed eight years prior to
presentation and subsequent type two diabetes mellitus ( T2DM ), one prior episode of HTG-induced pancreatitis
three years prior to presentation , associated with an acute hepatitis , and obesity with a body mass index
( BMI ) of 33.5 kg/m2 , presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting.
Two weeks prior to presentation , The lady was treated with a five-day course of amoxicillin for a respiratory tract infection .
She was on metformin , glipizide , and dapagliflozin for T2DM and atorvastatin and gemfibrozil for HTG .
The woman had been on dapagliflozin for six months at the time of presentation ."""

data = spark.createDataFrame([[sample_text]]).toDF("text")

model = nlpPipeline.fit(data).transform(data)

# Show results
model.selectExpr("explode(merged_ner_chunk) as a") \
  .selectExpr("a.begin","a.end","a.result as chunk","a.metadata.entity as entity") \
  .show(5, False)

+-----+---+-------------------------------------+-------------+
|begin|end|chunk                                |entity       |
+-----+---+-------------------------------------+-------------+
|14   |19 |female                               |female_entity|
|39   |67 |gestational diabetes mellitus        |PROBLEM      |
|117  |153|subsequent type two diabetes mellitus|PROBLEM      |
|157  |160|T2DM                                 |PROBLEM      |
|186  |209|HTG-induced pancreatitis             |PROBLEM      |
+-----+---+-------------------------------------+-------------+
{%- endcapture -%}

{%- capture model_python_finance -%}
from johnsnowlabs import *

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = nlp.RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base","en") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

bert_embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("bert_embeddings")

fin_ner = finance.NerModel.pretrained('finner_deid', "en", "finance/models")\
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner") 
    #.setLabelCasing("upper")

ner_converter =  finance.NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setReplaceLabels({"ORG": "PARTY"}) # Replace "ORG" entity as "PARTY"

ner_finner = finance.NerModel.pretrained("finner_org_per_role_date", "en", "finance/models")\
    .setInputCols(["sentence", "token", "bert_embeddings"]) \
    .setOutputCol("ner_finner") 
    #.setLabelCasing("upper")

ner_converter_finner = nlp.NerConverter() \
    .setInputCols(["sentence", "token", "ner_finner"]) \
    .setOutputCol("ner_finner_chunk") \
    .setWhiteList(['ROLE']) # Just use "ROLE" entity from this NER

chunk_merge =  finance.ChunkMergeModel()\
    .setInputCols("ner_finner_chunk", "ner_chunk")\
    .setOutputCol("deid_merged_chunk")

nlpPipeline = nlp.Pipeline(stages=[
      documentAssembler, 
      sentenceDetector,
      tokenizer,
      embeddings,
      bert_embeddings,
      fin_ner,
      ner_converter,
      ner_finner,
      ner_converter_finner,
      chunk_merge])

data = spark.createDataFrame([["Jeffrey Preston Bezos is an American entrepreneur, founder and CEO of Amazon"]]).toDF("text")

# Show results
result = nlpPipeline.fit(data).transform(data).cache()
result.select(F.explode(F.arrays_zip(result.deid_merged_chunk.result, 
                                     result.deid_merged_chunk.metadata)).alias("cols")) \
      .select(F.expr("cols['0']").alias("chunk"),
              F.expr("cols['1']['entity']").alias("ner_label")).show(truncate=False)

+---------------------+---------+
|chunk                |ner_label|
+---------------------+---------+
|Jeffrey Preston Bezos|PERSON   |
|American             |COUNTRY  |
|founder              |ROLE     |
|CEO                  |ROLE     |
|Amazon               |PARTY    |
+---------------------+---------+
{%- endcapture -%}

{%- capture model_python_legal -%}
from johnsnowlabs import *

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = nlp.RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base","en") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

legal_ner = legal.NerModel.pretrained("legner_contract_doc_parties", "en", "legal/models")\
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner") 
    #.setLabelCasing("upper")

ner_converter = legal.NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setReplaceLabels({"ALIAS": "PARTY"})

ner_signers = legal.NerModel.pretrained("legner_signers", "en", "legal/models")\
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner_signers") 
    #.setLabelCasing("upper")

ner_converter_signers = nlp.NerConverter() \
    .setInputCols(["sentence", "token", "ner_signers"]) \
    .setOutputCol("ner_signer_chunk")

chunk_merge = legal.ChunkMergeModel()\
    .setInputCols("ner_signer_chunk", "ner_chunk")\
    .setOutputCol("deid_merged_chunk")

nlpPipeline = nlp.Pipeline(stages=[
      documentAssembler, 
      sentenceDetector,
      tokenizer,
      embeddings,
      legal_ner,
      ner_converter,
      ner_signers,
      ner_converter_signers,
      chunk_merge])

data = spark.createDataFrame([["""ENTIRE AGREEMENT.  This Agreement contains the entire understanding of the parties hereto with respect to the transactions and matters contemplated hereby, supersedes all previous Agreements between i-Escrow and 2TheMart concerning the subject matter.

2THEMART.COM, INC.:                         I-ESCROW, INC.:

By:Dominic J. Magliarditi                By:Sanjay Bajaj Name: Dominic J. Magliarditi                Name: Sanjay Bajaj Title: President                            Title: VP Business Development Date: 6/21/99                               Date: 6/11/99 """]]).toDF("text")

# Show results
result = nlpPipeline.fit(data).transform(data).cache()
result.select(F.explode(F.arrays_zip(result.deid_merged_chunk.result, 
                                     result.deid_merged_chunk.metadata)).alias("cols")) \
      .select(F.expr("cols['0']").alias("chunk"),
              F.expr("cols['1']['entity']").alias("ner_label")).show(truncate=False)

+-----------------------+--------------+
|chunk                  |ner_label     |
+-----------------------+--------------+
|ENTIRE AGREEMENT       |DOC           |
|INC                    |PARTY         |
|INC                    |PARTY         |
|J. Magliarditi         |SIGNING_PERSON|
|Bajaj                  |SIGNING_PERSON|
|Dominic J. Magliarditi |SIGNING_PERSON|
|Sanjay Bajaj           |SIGNING_PERSON|
|President              |SIGNING_TITLE |
|VP Business Development|SIGNING_TITLE |
+-----------------------+--------------+
{%- endcapture -%}

{%- capture model_scala_medical -%}
import spark.implicits._

// Annotator that transforms a text column from dataframe into an Annotation ready for NLP 
val documentAssembler = new DocumentAssembler()
 .setInputCol("text") 
 .setOutputCol("document") 
 
// Sentence Detector annotator,processes various sentences per line 
val sentenceDetector = new SentenceDetector()
 .setInputCols(Array("document")) 
 .setOutputCol("sentence") 
 
// Tokenizer splits words in a relevant format for NLP 
val tokenizer = new Tokenizer()
 .setInputCols(Array("sentence")) 
 .setOutputCol("token") 
 
// Clinical word embeddings trained on PubMED dataset 
val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
 .setInputCols(Array("sentence","token")) 
 .setOutputCol("embeddings") 
 
// 1- ner_clinical model 
val clinical_ner = MedicalNerModel.pretrained("ner_clinical","en","clinical/models")
 .setInputCols(Array("sentence","token","embeddings")) 
 .setOutputCol("clinical_ner") 

val clinical_ner_converter = new NerConverterInternal()
 .setInputCols(Array("sentence","token","clinical_ner")) 
 .setOutputCol("clinical_ner_chunk") 
 
// 2- posology ner model 
val posology_ner = MedicalNerModel.pretrained("ner_posology","en","clinical/models")
 .setInputCols(Array("sentence","token","embeddings")) 
 .setOutputCol("posology_ner") 

val posology_ner_converter = new NerConverterInternal()
 .setInputCols(Array("sentence","token","posology_ner")) 
 .setOutputCol("posology_ner_chunk") 
 
// 3- generate a text matcher annotator that extracts female related entities 
val entities = new Array("she","her","girl","woman","women","womanish","womanlike","womanly","madam","madame","senora","lady","miss","girlfriend","wife","bride","misses","mrs.","female")

with open ('female_entities.txt', 'w') as f:
    for i in entities:
        f.write(i+'\n')
 
// Find female entities using TextMatcher 
val female_entity_extractor = new TextMatcher()
 .setInputCols(Array("sentence","token")) 
 .setOutputCol("female_entities") 
 .setEntities("female_entities.txt") 
 .setCaseSensitive(false) 
 .setEntityValue("female_entity") 
 

// Chunk Merge annotator is used to merge columns 
val chunk_merger = new ChunkMergeModel()
 .setInputCols("posology_ner_chunk","clinical_ner_chunk","female_entities") 
 .setOutputCol("merged_ner_chunk") 
 .setMergeOverlapping(true) 
 .setOrderingFeatures(Array("ChunkConfidence")) 
 .setSelectionStrategy("Sequential") 
 .setDefaultConfidence(0.8) 
 .setBlackList(Array("DURATION")) 

val nlpPipeline = new Pipeline().setStages(Array( 
    documentAssembler, 
    sentenceDetector, 
    tokenizer, 
    word_embeddings, 
    clinical_ner, 
    clinical_ner_converter, 
    posology_ner, 
    posology_ner_converter, 
    female_entity_extractor, 
    chunk_merger)) 

val text ="""A 28 year old female with a history of gestational diabetes mellitus diagnosed eight years prior to
presentation and subsequent type two diabetes mellitus ( T2DM ), one prior episode of HTG-induced pancreatitis
three years prior to presentation , associated with an acute hepatitis , and obesity with a body mass index
( BMI ) of 33.5 kg/m2 , presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting.
Two weeks prior to presentation , The lady was treated with a five-day course of amoxicillin for a respiratory tract infection .
She was on metformin , glipizide , and dapagliflozin for T2DM and atorvastatin and gemfibrozil for HTG .
The woman had been on dapagliflozin for six months at the time of presentation ."""
val data = Seq(text).toDF("text")

val model = nlpPipeline.fit(data).transform(data) 

model.selectExpr("explode(merged_ner_chunk) as a") \
  .selectExpr("a.begin","a.end","a.result as chunk","a.metadata.entity as entity") \
  .show(5, False)

+-----+---+-------------------------------------+----------------+
|begin|end|chunk                                |entity          |
+-----+---+-------------------------------------+----------------+
|14   |19 |female                               |FEMALE_GENDER   |
|39   |67 |gestational diabetes mellitus        |CLINICAL_PROBLEM|
|117  |153|subsequent type two diabetes mellitus|CLINICAL_PROBLEM|
|157  |160|T2DM                                 |CLINICAL_PROBLEM|
|186  |209|HTG-induced pancreatitis             |CLINICAL_PROBLEM|
+-----+---+-------------------------------------+----------------+

{%- endcapture -%}

{%- capture model_scala_finance -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
 .setInputCol("text") 
 .setOutputCol("document") 

val sentenceDetector = new SentenceDetector()
 .setInputCols(Array("document")) 
 .setOutputCol("sentence") 

val tokenizer = new Tokenizer()
 .setInputCols(Array("sentence")) 
 .setOutputCol("token") 

val embeddings = RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base","en")
 .setInputCols(Array("sentence","token")) 
 .setOutputCol("embeddings") 

val bert_embeddings = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en")
 .setInputCols(Array("sentence","token")) 
 .setOutputCol("bert_embeddings") 

val fin_ner = FinanceNerModel.pretrained("finner_deid","en","finance/models")
 .setInputCols(Array("sentence","token","embeddings")) 
 .setOutputCol("ner") 
 //.setLabelCasing("upper") 

val ner_converter = new NerConverterInternal()
 .setInputCols(Array("sentence","token","ner")) 
 .setOutputCol("ner_chunk") 
 .setReplaceLabels(Map("ORG" -> "PARTY") ) // Replace "ORG" entity as "PARTY" 

val ner_finner = FinanceNerModel.pretrained("finner_org_per_role_date","en","finance/models")
 .setInputCols(Array("sentence","token","bert_embeddings")) 
 .setOutputCol("ner_finner") 
 //.setLabelCasing("upper") 

val ner_converter_finner = new NerConverter()
 .setInputCols(Array("sentence","token","ner_finner")) 
 .setOutputCol("ner_finner_chunk") 
 .setWhiteList(Array("ROLE")) // Just use "ROLE" entity from this NER 

val chunk_merge = new ChunkMergeModel()
 .setInputCols("ner_finner_chunk","ner_chunk") 
 .setOutputCol("deid_merged_chunk") 

val nlpPipeline = new Pipeline().setStages(Array(
      documentAssembler, 
      sentenceDetector,
      tokenizer,
      embeddings,
      bert_embeddings,
      fin_ner,
      ner_converter,
      ner_finner,
      ner_converter_finner,
      chunk_merge))

val text ="""Jeffrey Preston Bezos is an American entrepreneur, founder and CEO of Amazon"""
val data = Seq(text).toDF("text")

val result = nlpPipeline.fit(data).transform(data) 

# Show results
result.select(F.explode(F.arrays_zip(result.deid_merged_chunk.result, 
                                     result.deid_merged_chunk.metadata)).alias("cols")) \
      .select(F.expr("cols['0']").alias("chunk"),
              F.expr("cols['1']['entity']").alias("ner_label")).show(truncate=False)

+---------------------+---------+
|chunk                |ner_label|
+---------------------+---------+
|Jeffrey Preston Bezos|PERSON   |
|American             |COUNTRY  |
|founder              |ROLE     |
|CEO                  |ROLE     |
|Amazon               |PARTY    |
+---------------------+---------+

{%- endcapture -%}

{%- capture model_scala_legal -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
 .setInputCol("text") 
 .setOutputCol("document") 

val sentenceDetector = new SentenceDetector()
 .setInputCols(Array("document")) 
 .setOutputCol("sentence") 

val tokenizer = new Tokenizer()
 .setInputCols(Array("sentence")) 
 .setOutputCol("token") 

val embeddings = RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base","en")
 .setInputCols(Array("sentence","token")) 
 .setOutputCol("embeddings") 

val legal_ner = LegalNerModel.pretrained("legner_contract_doc_parties","en","legal/models")
 .setInputCols(Array("sentence","token","embeddings")) 
 .setOutputCol("ner") 
 //.setLabelCasing("upper") 

val ner_converter = new NerConverterInternal()
 .setInputCols(Array("sentence","token","ner")) 
 .setOutputCol("ner_chunk") 
 .setReplaceLabels(Map("ALIAS" -> "PARTY") ) 

val ner_signers = LegalNerModel.pretrained("legner_signers","en","legal/models")
 .setInputCols(Array("sentence","token","embeddings")) 
 .setOutputCol("ner_signers") 
 //.setLabelCasing("upper") 

val ner_converter_signers = new NerConverter()
 .setInputCols(Array("sentence","token","ner_signers")) 
 .setOutputCol("ner_signer_chunk") 

val chunk_merge = new ChunkMergeModel()
 .setInputCols("ner_signer_chunk","ner_chunk") 
 .setOutputCol("deid_merged_chunk") 

val nlpPipeline = new Pipeline().setStages(Array( 
    documentAssembler, 
    sentenceDetector, 
    tokenizer, 
    embeddings, 
    legal_ner, 
    ner_converter, 
    ner_signers,
    ner_converter_signers, 
    chunk_merge)) 

val data = Seq(("ENTIRE AGREEMENT.  This Agreement contains the entire understanding of the parties hereto with respect to the transactions and matters contemplated hereby, supersedes all previous Agreements between i-Escrow and 2TheMart concerning the subject matter.

2THEMART.COM, INC.:                         I-ESCROW, INC.:

By:Dominic J. Magliarditi                By:Sanjay Bajaj Name: Dominic J. Magliarditi                Name: Sanjay Bajaj Title: President                            Title: VP Business Development Date: 6/21/99                               Date: 6/11/99 ")).toDF("text")

# Show results
result = nlpPipeline.fit(data).transform(data).cache()
result.select(F.explode(F.arrays_zip(result.deid_merged_chunk.result, 
                                     result.deid_merged_chunk.metadata)).alias("cols")) \
      .select(F.expr("cols['0']").alias("chunk"),
              F.expr("cols['1']['entity']").alias("ner_label")).show(truncate=False)

+-----------------------+--------------+
|chunk                  |ner_label     |
+-----------------------+--------------+
|ENTIRE AGREEMENT       |DOC           |
|INC                    |PARTY         |
|INC                    |PARTY         |
|J. Magliarditi         |SIGNING_PERSON|
|Bajaj                  |SIGNING_PERSON|
|Dominic J. Magliarditi |SIGNING_PERSON|
|Sanjay Bajaj           |SIGNING_PERSON|
|President              |SIGNING_TITLE |
|VP Business Development|SIGNING_TITLE |
+-----------------------+--------------+
{%- endcapture -%}

{%- capture model_api_link -%}
[ChunkMergeModel](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/merge/ChunkMergeModel.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[ChunkMergeModel](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/merge/chunk_merge/index.html#sparknlp_jsl.annotator.merge.chunk_merge.ChunkMergeModel)
{%- endcapture -%}

{%- capture model_description -%}
Merges two chunk columns coming from two annotators(NER, ContextualParser or any other annotator producing
chunks)

- `inputCols`: The name of the columns containing the input annotations. It can read either a String column or an Array.
- `outputCol`: The name of the column in Document type that is generated. We can specify only one column here.
- `mergeOverlapping`: (Boolean) Sets whether to merge overlapping matched chunks. Default `True`.
- `falsePositivesResource`: Sets file with false positive pairs
- `replaceDictResource`: Sets replace dictionary pairs for NER labels
- `blackList`: (String List) If defined, list of entities to ignore. The rest will be processed.
- `whiteList`: (String List) If defined, list of entities to accept.
- `selectionStrategy`: (String) Sets Whether to select annotations sequentially based on annotation order `Sequential` or using any other available strategy; currently only `Sequential` and `DiverseLonger` are available. Default `Sequential`.
- `orderingFeatures`: (String List) The ordering features to use for overlapping entities. Possible values are `ChunkBegin, ChunkLength, ChunkPrecedence, ChunkConfidence.`
- `defaultConfidence`: (Float) Sets when ChunkConfidence ordering feature is included and a given annotation does not have any confidence. The value of this param will be used as a confidence score for annotations without a confidence score.
- `chunkPrecedence`: (String List) Sets what is the precedence order when a chunk labeled by two models.
- `chunkPrecedenceValuePrioritization`: (String List) Sets when ChunkPrecedence ordering feature is used. This param contains an Array of comma-separated values representing the desired order of prioritization for the values in the metadata fields included from chunkPrecedence.

All the parameters can be set using the corresponding set method in camel case. For example, `.setInputcols()`.
{%- endcapture -%}

{%- capture model_input_anno -%}
CHUNK, CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}



{%- capture approach_python_medical -%}
from johnsnowlabs import *
# Annotator that transforms a text column from dataframe into an Annotation ready for NLP
documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

# Sentence Detector annotator, processes various sentences per line
sentenceDetector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

# Tokenizer splits words in a relevant format for NLP
tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

# Clinical word embeddings trained on PubMED dataset
word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")


# 1- ner_clinical model
clinical_ner = medical.NerModel.pretrained("ner_clinical", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("clinical_ner")

clinical_ner_converter = medical.NerConverterInternal() \
    .setInputCols(["sentence", "token", "clinical_ner"]) \
    .setOutputCol("clinical_ner_chunk")

# 2- posology ner model
posology_ner = medical.NerModel.pretrained("ner_posology", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("posology_ner")

posology_ner_converter = medical.NerConverterInternal() \
    .setInputCols(["sentence", "token", "posology_ner"]) \
    .setOutputCol("posology_ner_chunk")

# 3- generate a text matcher annotator that extracts female related entities
entities = ['she', 'her', 'girl', 'woman', 'women', 'womanish', 'womanlike', 'womanly', 'madam', 'madame', 'senora', 'lady', 'miss', 'girlfriend', 'wife', 'bride', 'misses', 'mrs.', 'female']
with open ('female_entities.txt', 'w') as f:
    for i in entities:
        f.write(i+'\n')

# Find female entities using TextMatcher
female_entity_extractor = nlp.TextMatcher() \
    .setInputCols(["sentence",'token'])\
    .setOutputCol("female_entities")\
    .setEntities("female_entities.txt")\
    .setCaseSensitive(False)\
    .setEntityValue('female_entity')

# Chunk Merge annotator is used to merge columns
chunk_merger = medical.ChunkMergeApproach()\
    .setInputCols("posology_ner_chunk", 'clinical_ner_chunk', "female_entities")\
    .setOutputCol('merged_ner_chunk')

nlpPipeline = nlp.Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    word_embeddings,
    clinical_ner,
    clinical_ner_converter,
    posology_ner,
    posology_ner_converter,
    female_entity_extractor,
    chunk_merger])

sample_text = """A 28 year old female with a history of gestational diabetes mellitus diagnosed eight years prior to
presentation and subsequent type two diabetes mellitus ( T2DM ), one prior episode of HTG-induced pancreatitis
three years prior to presentation , associated with an acute hepatitis , and obesity with a body mass index
( BMI ) of 33.5 kg/m2 , presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting.
Two weeks prior to presentation , The lady was treated with a five-day course of amoxicillin for a respiratory tract infection .
She was on metformin , glipizide , and dapagliflozin for T2DM and atorvastatin and gemfibrozil for HTG .
The woman had been on dapagliflozin for six months at the time of presentation ."""


data = spark.createDataFrame([[sample_text]]).toDF("text")

model = nlpPipeline.fit(data).transform(data)

# Show results
model.selectExpr("explode(merged_ner_chunk) as a") \
  .selectExpr("a.begin","a.end","a.result as chunk","a.metadata.entity as entity") \
  .show(5, False)
+-----+---+-------------------------------------+-------------+
|begin|end|chunk                                |entity       |
+-----+---+-------------------------------------+-------------+
|14   |19 |female                               |female_entity|
|39   |67 |gestational diabetes mellitus        |PROBLEM      |
|117  |153|subsequent type two diabetes mellitus|PROBLEM      |
|157  |160|T2DM                                 |PROBLEM      |
|186  |209|HTG-induced pancreatitis             |PROBLEM      |
+-----+---+-------------------------------------+-------------+
{%- endcapture -%}

{%- capture approach_python_finance -%}
from johnsnowlabs import *

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = nlp.RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base","en") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

bert_embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("bert_embeddings")

fin_ner = finance.NerModel.pretrained('finner_deid', "en", "finance/models")\
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner") 
    #.setLabelCasing("upper")

ner_converter =  finance.NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setReplaceLabels({"ORG": "PARTY"}) # Replace "ORG" entity as "PARTY"

ner_finner = finance.NerModel.pretrained("finner_org_per_role_date", "en", "finance/models")\
    .setInputCols(["sentence", "token", "bert_embeddings"]) \
    .setOutputCol("ner_finner") 
    #.setLabelCasing("upper")

ner_converter_finner = nlp.NerConverter() \
    .setInputCols(["sentence", "token", "ner_finner"]) \
    .setOutputCol("ner_finner_chunk") \
    .setWhiteList(['ROLE']) # Just use "ROLE" entity from this NER

chunk_merge =  finance.ChunkMergeApproach()\
    .setInputCols("ner_finner_chunk", "ner_chunk")\
    .setOutputCol("deid_merged_chunk")

nlpPipeline = Pipeline(stages=[
      documentAssembler, 
      sentenceDetector,
      tokenizer,
      embeddings,
      bert_embeddings,
      fin_ner,
      ner_converter,
      ner_finner,
      ner_converter_finner,
      chunk_merge])

data = spark.createDataFrame([["Jeffrey Preston Bezos is an American entrepreneur, founder and CEO of Amazon"]]).toDF("text")

# Show results
result = nlpPipeline.fit(data).transform(data).cache()
result.select(F.explode(F.arrays_zip(result.deid_merged_chunk.result, 
                                     result.deid_merged_chunk.metadata)).alias("cols")) \
      .select(F.expr("cols['0']").alias("chunk"),
              F.expr("cols['1']['entity']").alias("ner_label")).show(truncate=False)
+---------------------+---------+
|chunk                |ner_label|
+---------------------+---------+
|Jeffrey Preston Bezos|PERSON   |
|founder              |ROLE     |
|CEO                  |ROLE     |
|Amazon               |PARTY    |
+---------------------+---------+
{%- endcapture -%}

{%- capture approach_python_legal -%}
from johnsnowlabs import *

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = nlp.RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base","en") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

legal_ner = legal.NerModel.pretrained("legner_contract_doc_parties", "en", "legal/models")\
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner") 
    #.setLabelCasing("upper")

ner_converter = legal.NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setReplaceLabels({"ALIAS": "PARTY"})

ner_signers = legal.NerModel.pretrained("legner_signers", "en", "legal/models")\
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner_signers") 
    #.setLabelCasing("upper")

ner_converter_signers = nlp.NerConverter() \
    .setInputCols(["sentence", "token", "ner_signers"]) \
    .setOutputCol("ner_signer_chunk")

chunk_merge = legal.ChunkMergeApproach()\
    .setInputCols("ner_signer_chunk", "ner_chunk")\
    .setOutputCol("deid_merged_chunk")

nlpPipeline = Pipeline(stages=[
      documentAssembler, 
      sentenceDetector,
      tokenizer,
      embeddings,
      legal_ner,
      ner_converter,
      ner_signers,
      ner_converter_signers,
      chunk_merge])


data = spark.createDataFrame([["ENTIRE AGREEMENT.  This Agreement contains the entire understanding of the parties hereto with respect to the transactions and matters contemplated hereby, supersedes all previous Agreements between i-Escrow and 2TheMart concerning the subject matter.

2THEMART.COM, INC.:                         I-ESCROW, INC.:

By:Dominic J. Magliarditi                By:Sanjay Bajaj Name: Dominic J. Magliarditi                Name: Sanjay Bajaj Title: President                            Title: VP Business Development Date: 6/21/99                               Date: 6/11/99 "]]).toDF("text")

# Show results
result = nlpPipeline.fit(data).transform(data).cache()
result.select(F.explode(F.arrays_zip(result.deid_merged_chunk.result, 
                                     result.deid_merged_chunk.metadata)).alias("cols")) \
      .select(F.expr("cols['0']").alias("chunk"),
              F.expr("cols['1']['entity']").alias("ner_label")).show(truncate=False)
+-----------------------+--------------+
|chunk                  |ner_label     |
+-----------------------+--------------+
|ENTIRE AGREEMENT       |DOC           |
|INC                    |PARTY         |
|J. Magliarditi         |SIGNING_PERSON|
|Bajaj                  |SIGNING_PERSON|
|Dominic J. Magliarditi |SIGNING_PERSON|
|Sanjay Bajaj           |SIGNING_PERSON|
|President              |SIGNING_TITLE |
|VP Business Development|SIGNING_TITLE |
+-----------------------+--------------+
{%- endcapture -%}

{%- capture approach_scala_medical -%}
import spark.implicits._

// Annotator that transforms a text column from dataframe into an Annotation ready for NLP 
val documentAssembler = new DocumentAssembler()
 .setInputCol("text") 
 .setOutputCol("document") 
 
// Sentence Detector annotator,processes various sentences per line 
val sentenceDetector = new SentenceDetector()
 .setInputCols(Array("document")) 
 .setOutputCol("sentence") 
 
// Tokenizer splits words in a relevant format for NLP 
val tokenizer = new Tokenizer()
 .setInputCols(Array("sentence")) 
 .setOutputCol("token") 
 
// Clinical word embeddings trained on PubMED dataset 
val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
 .setInputCols(Array("sentence","token")) 
 .setOutputCol("embeddings") 
 
// 1- ner_clinical model 
val clinical_ner = MedicalNerModel.pretrained("ner_clinical","en","clinical/models")
 .setInputCols(Array("sentence","token","embeddings")) 
 .setOutputCol("clinical_ner") 

val clinical_ner_converter = new NerConverterInternal()
 .setInputCols(Array("sentence","token","clinical_ner")) 
 .setOutputCol("clinical_ner_chunk") 
 
// 2- posology ner model 
val posology_ner = MedicalNerModel.pretrained("ner_posology","en","clinical/models")
 .setInputCols(Array("sentence","token","embeddings")) 
 .setOutputCol("posology_ner") 

val posology_ner_converter = new NerConverterInternal()
 .setInputCols(Array("sentence","token","posology_ner")) 
 .setOutputCol("posology_ner_chunk") 
 
// 3- generate a text matcher annotator that extracts female related entities 
val entities = new Array("she","her","girl","woman","women","womanish","womanlike","womanly","madam","madame","senora","lady","miss","girlfriend","wife","bride","misses","mrs.","female")

with open ('female_entities.txt', 'w') as f:
    for i in entities:
        f.write(i+'\n')
 
// Find female entities using TextMatcher 
val female_entity_extractor = new TextMatcher()
 .setInputCols(Array("sentence","token")) 
 .setOutputCol("female_entities") 
 .setEntities("female_entities.txt") 
 .setCaseSensitive(false) 
 .setEntityValue("female_entity") 
 
// Chunk Merge annotator is used to merge columns 
val chunk_merger = new ChunkMergeApproach()
 .setInputCols("posology_ner_chunk","clinical_ner_chunk","female_entities") 
 .setOutputCol("merged_ner_chunk") 

val nlpPipeline = new Pipeline().setStages(Array( 
    documentAssembler, 
    sentenceDetector, 
    tokenizer, 
    word_embeddings, 
    clinical_ner, 
    clinical_ner_converter, 
    posology_ner, 
    posology_ner_converter, 
    female_entity_extractor, 
    chunk_merger)) 

val text ="""A 28 year old female with a history of gestational diabetes mellitus diagnosed eight years prior to
presentation and subsequent type two diabetes mellitus ( T2DM ), one prior episode of HTG-induced pancreatitis
three years prior to presentation , associated with an acute hepatitis , and obesity with a body mass index
( BMI ) of 33.5 kg/m2 , presented with a one-week history of polyuria , polydipsia , poor appetite , and vomiting.
Two weeks prior to presentation , The lady was treated with a five-day course of amoxicillin for a respiratory tract infection .
She was on metformin , glipizide , and dapagliflozin for T2DM and atorvastatin and gemfibrozil for HTG .
The woman had been on dapagliflozin for six months at the time of presentation ."""
val data = Seq(text).toDF("text")

val model = nlpPipeline.fit(data).transform(data) 

model.selectExpr("explode(merged_ner_chunk) as a") \
  .selectExpr("a.begin","a.end","a.result as chunk","a.metadata.entity as entity") \
  .show(5, False)

+-----+---+-------------------------------------+----------------+
|begin|end|chunk                                |entity          |
+-----+---+-------------------------------------+----------------+
|14   |19 |female                               |FEMALE_GENDER   |
|39   |67 |gestational diabetes mellitus        |CLINICAL_PROBLEM|
|117  |153|subsequent type two diabetes mellitus|CLINICAL_PROBLEM|
|157  |160|T2DM                                 |CLINICAL_PROBLEM|
|186  |209|HTG-induced pancreatitis             |CLINICAL_PROBLEM|
+-----+---+-------------------------------------+----------------+
{%- endcapture -%}

{%- capture approach_scala_finance -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
    .setInputCol("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCol("sentence")
    .setOutputCol("token")

val embeddings = RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base","en")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val bert_embeddings = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("bert_embeddings")

val fin_ner = FinanceNerModel.pretrained('finner_deid', "en", "finance/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner") 
    #.setLabelCasing("upper")

val ner_converter =  new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")\
    .setReplaceLabels({"ORG": "PARTY"}) # Replace "ORG" entity as "PARTY"

val ner_finner = FinanceNerModel.pretrained("finner_org_per_role_date", "en", "finance/models")\
    .setInputCols(Array("sentence", "token", "bert_embeddings"))
    .setOutputCol("ner_finner") 
    #.setLabelCasing("upper")

val ner_converter_finner = new NerConverter()
    .setInputCols(Array("sentence", "token", "ner_finner"))
    .setOutputCol("ner_finner_chunk")
    .setWhiteList(['ROLE']) # Just use "ROLE" entity from this NER

val chunk_merge =  new ChunkMergeApproach()
    .setInputCols(Array("ner_finner_chunk", "ner_chunk"))
    .setOutputCol("deid_merged_chunk")

val nlpPipeline = new Pipeline().setStages(Array(
      documentAssembler, 
      sentenceDetector,
      tokenizer,
      embeddings,
      bert_embeddings,
      fin_ner,
      ner_converter,
      ner_finner,
      ner_converter_finner,
      chunk_merge))

val data = Seq(("Jeffrey Preston Bezos is an American entrepreneur, founder and CEO of Amazon")).toDF("text")

# Show results
result = nlpPipeline.fit(data).transform(data).cache()
result.select(F.explode(F.arrays_zip(result.deid_merged_chunk.result, 
                                     result.deid_merged_chunk.metadata)).alias("cols")) \
      .select(F.expr("cols['0']").alias("chunk"),
              F.expr("cols['1']['entity']").alias("ner_label")).show(truncate=False)
+---------------------+---------+
|chunk                |ner_label|
+---------------------+---------+
|Jeffrey Preston Bezos|PERSON   |
|founder              |ROLE     |
|CEO                  |ROLE     |
|Amazon               |PARTY    |
+---------------------+---------+
{%- endcapture -%}

{%- capture approach_scala_legal -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
    .setInputCol("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCol("sentence")
    .setOutputCol("token")

val embeddings = RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base","en")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val legal_ner = LegalNerModel.pretrained("legner_contract_doc_parties", "en", "legal/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner") 
    #.setLabelCasing("upper")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")\
    .setReplaceLabels({"ALIAS": "PARTY"})

val ner_signers = LegalNerModel.pretrained("legner_signers", "en", "legal/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner_signers") 
    #.setLabelCasing("upper")

val ner_converter_signers = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner_signers"))
    .setOutputCol("ner_signer_chunk")

val chunk_merge = new ChunkMergeApproach()
    .setInputCols(Array("ner_signer_chunk", "ner_chunk"))
    .setOutputCol("deid_merged_chunk")

val nlpPipeline = new Pipeline().setStages(Array(
      documentAssembler, 
      sentenceDetector,
      tokenizer,
      embeddings,
      legal_ner,
      ner_converter,
      ner_signers,
      ner_converter_signers,
      chunk_merge))

val data = Seq(("ENTIRE AGREEMENT.  This Agreement contains the entire understanding of the parties hereto with respect to the transactions and matters contemplated hereby, supersedes all previous Agreements between i-Escrow and 2TheMart concerning the subject matter.

2THEMART.COM, INC.:                         I-ESCROW, INC.:

By:Dominic J. Magliarditi                By:Sanjay Bajaj Name: Dominic J. Magliarditi                Name: Sanjay Bajaj Title: President                            Title: VP Business Development Date: 6/21/99                               Date: 6/11/99 ")).toDF("text")

# Show results
result = nlpPipeline.fit(data).transform(data).cache()
result.select(F.explode(F.arrays_zip(result.deid_merged_chunk.result, 
                                     result.deid_merged_chunk.metadata)).alias("cols")) \
      .select(F.expr("cols['0']").alias("chunk"),
              F.expr("cols['1']['entity']").alias("ner_label")).show(truncate=False)
+-----------------------+--------------+
|chunk                  |ner_label     |
+-----------------------+--------------+
|ENTIRE AGREEMENT       |DOC           |
|INC                    |PARTY         |
|J. Magliarditi         |SIGNING_PERSON|
|Bajaj                  |SIGNING_PERSON|
|Dominic J. Magliarditi |SIGNING_PERSON|
|Sanjay Bajaj           |SIGNING_PERSON|
|President              |SIGNING_TITLE |
|VP Business Development|SIGNING_TITLE |
+-----------------------+--------------+
{%- endcapture -%}

{%- capture approach_api_link -%}
[ChunkMergeApproach](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/merge/ChunkMergeApproach.html)
{%- endcapture -%}

{%- capture approach_python_api_link -%}
[ChunkMergeApproach](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/merge/chunk_merge/index.html#sparknlp_jsl.annotator.merge.chunk_merge.ChunkMergeApproach)
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
%}