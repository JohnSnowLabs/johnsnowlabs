{%- capture title -%}
IOBTagger
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
The IOBTagger chunk tag (Chunk based) outputs, namely NerConverter and ChunkMerger, serve the purpose of converting token tags into Named Entity Recognition (NER) tags (token-based). These tags help to identify and categorize specific entities within a given text, enabling valuable information and context to be extracted from tokens.
For example output columns as inputs from
[NerConverter](/docs/en/annotators#nerconverter)
and [Tokenizer](/docs/en/annotators#tokenizer) can be used to merge.
{%- endcapture -%}

{%- capture model_input_anno -%}
TOKEN, CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
NAMED_ENTITY
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical 
# Pipeline stages are defined where NER is done. NER is converted to chunks.

docAssembler = nlp.DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
  .setInputCols(["sentence"])\
  .setOutputCol("token")

embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
  .setInputCols(["sentence", "token"])\
  .setOutputCol("embs")

nerModel = medical.NerModel.pretrained("ner_posology_greedy", "en", "clinical/models")\
  .setInputCols(["sentence", "token", "embs"])\
  .setOutputCol("ner")

nerConverter = nlp.NerConverter()\
  .setInputCols(["sentence", "token", "ner"])\
  .setOutputCol("ner_chunk")

# Define the IOB tagger, which needs tokens and chunks as input. Show results.
iobTagger = medical.IOBTagger()\
  .setInputCols(["token", "ner_chunk"])\
  .setOutputCol("ner_label")

pipeline = nlp.Pipeline(stages=[docAssembler,
                            sentenceDetector,
                            tokenizer,
                            embeddings,
                            nerModel,
                            nerConverter,
                            iobTagger])

text = "The patient was prescribed 1 capsule of Advil 10 mg for 5 days and magnesium hydroxide 100mg/1ml suspension PO."
df = spark.createDataFrame([[text]]).toDF("text")
result = pipeline.fit(df).transform(df)

# chunk level result
result.selectExpr("explode(ner_chunk) as a") \
  .selectExpr("a.begin",
              "a.end",
              "a.result as ner_chunk",
              "a.metadata.entity as ner_label").show(50, False)

+-----+---+-------------------------------------------+---------+
|begin|end|ner_chunk                                  |ner_label|
+-----+---+-------------------------------------------+---------+
|27   |50 |1 capsule of Advil 10 mg                   |DRUG     |
|52   |61 |for 5 days                                 |DURATION |
|67   |109|magnesium hydroxide 100mg/1ml suspension PO|DRUG     |
+-----+---+-------------------------------------------+---------+

# token level result
result.selectExpr("explode(ner_label) as a") \
  .selectExpr("a.begin",
              "a.end",
              "a.metadata.word as word",
              "a.result as chunk").show(50, False)

+-----+---+----------+----------+
|begin|end|word      |chunk     |
+-----+---+----------+----------+
|0    |2  |The       |0         |
|4    |10 |patient   |0         |
|12   |14 |was       |0         |
|16   |25 |prescribed|0         |
|27   |27 |1         |B-DRUG    |
|29   |35 |capsule   |I-DRUG    |
|37   |38 |of        |I-DRUG    |
|40   |44 |Advil     |I-DRUG    |
|46   |47 |10        |I-DRUG    |
|49   |50 |mg        |I-DRUG    |
|52   |54 |for       |B-DURATION|
|56   |56 |5         |I-DURATION|
|58   |61 |days      |I-DURATION|
|63   |65 |and       |0         |
|67   |75 |magnesium |B-DRUG    |
|77   |85 |hydroxide |I-DRUG    |
|87   |95 |100mg/1ml |I-DRUG    |
|97   |106|suspension|I-DRUG    |
|108  |109|PO        |I-DRUG    |
|110  |110|.         |0         |
+-----+---+----------+----------+

{%- endcapture -%}

{%- capture model_python_legal -%}
from johnsnowlabs import nlp, legal 
# Pipeline stages are defined where NER is done. NER is converted to chunks.

docAssembler = nlp.DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
  .setInputCols(["sentence"])\
  .setOutputCol("token")

embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en")\
  .setInputCols(["sentence", "token"])\
  .setOutputCol("embs")

ner_model = legal.NerModel.pretrained("legner_orgs_prods_alias", "en", "legal/models")\
  .setInputCols(["sentence", "token", "embs"])\
  .setOutputCol("ner")

nerConverter = nlp.NerConverter()\
  .setInputCols(["sentence", "token", "ner"])\
  .setOutputCol("ner_chunk")

# Define the IOB tagger, which needs tokens and chunks as input. Show results.
iobTagger = legal.IOBTagger()\
  .setInputCols(["token", "ner_chunk"])\
  .setOutputCol("ner_label")

pipeline = nlp.Pipeline(stages=[docAssembler, 
                            sentenceDetector, 
                            tokenizer, 
                            embeddings, 
                            ner_model, 
                            nerConverter, 
                            iobTagger])

text = """This INTELLECTUAL PROPERTY AGREEMENT (this "Agreement"), dated as of December 31, 2018 (the "Effective Date") is entered into by and between Armstrong Flooring, Inc., a Delaware corporation ("Seller") and AFI Licensing LLC, a Delaware limited liability company ("Licensing" and together with Seller, "Arizona") and AHF Holding, Inc. (formerly known as Tarzan HoldCo, Inc.), a Delaware corporation ("Buyer") and Armstrong Hardwood Flooring Company, a Tennessee corporation (the "Company" and together with Buyer the "Buyer Entities") (each of Arizona on the one hand and the Buyer Entities on the other hand, a "Party" and collectively, the "Parties").
"""

df = spark.createDataFrame([[text]]).toDF("text")
result = pipeline.fit(df).transform(df) 

# chunk level result
result.selectExpr("explode(ner_chunk) as a") \
  .selectExpr("a.begin",
              "a.end",
              "a.result as ner_chunk",
              "a.metadata.entity as ner_label").show(50, False)

+-----+---+-----------------------------------+---------+
|begin|end|ner_chunk                          |ner_label|
+-----+---+-----------------------------------+---------+
|141  |165|Armstrong Flooring, Inc.,          |ORG      |
|192  |197|Seller                             |ALIAS    |
|205  |221|AFI Licensing LLC                  |ORG      |
|263  |271|Licensing                          |ALIAS    |
|292  |297|Seller                             |ALIAS    |
|301  |307|Arizona                            |ALIAS    |
|315  |330|AHF Holding, Inc                   |ORG      |
|399  |403|Buyer                              |ALIAS    |
|411  |445|Armstrong Hardwood Flooring Company|ORG      |
|478  |484|Company                            |ALIAS    |
|505  |509|Buyer                              |ALIAS    |
|516  |529|Buyer Entities                     |ALIAS    |
|542  |548|Arizona                            |ALIAS    |
|574  |587|Buyer Entities                     |ALIAS    |
|611  |615|Party                              |ALIAS    |
|641  |647|Parties                            |ALIAS    |
+-----+---+-----------------------------------+---------+

# token level result
result.selectExpr("explode(ner_label) as a") \
  .selectExpr("a.begin",
              "a.end",
              "a.metadata.word as word",
              "a.result as chunk").show(50, False)

+-----+---+------------+-------+
|begin|end|word        |chunk  |
+-----+---+------------+-------+
|0    |3  |This        |0      |
|5    |16 |INTELLECTUAL|0      |
|18   |25 |PROPERTY    |0      |
|27   |35 |AGREEMENT   |0      |
|37   |37 |(           |0      |
|38   |41 |this        |0      |
|43   |43 |"           |0      |
|44   |52 |Agreement   |0      |
|53   |55 |"),         |0      |
|57   |61 |dated       |0      |
|63   |64 |as          |0      |
|66   |67 |of          |0      |
|69   |76 |December    |0      |
|78   |79 |31          |0      |
|80   |80 |,           |0      |
|82   |85 |2018        |0      |
|87   |87 |(           |0      |
|88   |90 |the         |0      |
|92   |92 |"           |0      |
|93   |101|Effective   |0      |
|103  |106|Date        |0      |
|107  |108|")          |0      |
|110  |111|is          |0      |
|113  |119|entered     |0      |
|121  |124|into        |0      |
|126  |127|by          |0      |
|129  |131|and         |0      |
|133  |139|between     |0      |
|141  |149|Armstrong   |B-ORG  |
|151  |158|Flooring    |I-ORG  |
|159  |159|,           |I-ORG  |
|161  |163|Inc         |I-ORG  |
|164  |165|.,          |I-ORG  |
|167  |167|a           |0      |
|169  |176|Delaware    |0      |
|178  |188|corporation |0      |
|190  |191|("          |0      |
|192  |197|Seller      |B-ALIAS|
|198  |199|")          |0      |
|201  |203|and         |0      |
|205  |207|AFI         |B-ORG  |
|209  |217|Licensing   |I-ORG  |
|219  |221|LLC         |I-ORG  |
|222  |222|,           |0      |
|224  |224|a           |0      |
|226  |233|Delaware    |0      |
|235  |241|limited     |0      |
|243  |251|liability   |0      |
|253  |259|company     |0      |
|261  |262|("          |0      |
+-----+---+------------+-------+
only showing top 50 rows              
{%- endcapture -%}

{%- capture model_python_finance -%}
from johnsnowlabs import nlp, finance
# Pipeline stages are defined where NER is done. NER is converted to chunks.

docAssembler = nlp.DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
  .setInputCols(["sentence"])\
  .setOutputCol("token")

embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") \
  .setInputCols(["sentence", "token"])\
  .setOutputCol("embs")

nerModel = finance.NerModel.pretrained("finner_orgs_prods_alias","en","finance/models")\
  .setInputCols(["sentence", "token", "embs"])\
  .setOutputCol("ner")

nerConverter = nlp.NerConverter()\
  .setInputCols(["sentence", "token", "ner"])\
  .setOutputCol("ner_chunk")

# Define the IOB tagger, which needs tokens and chunks as input. Show results.
iobTagger = finance.IOBTagger()\
  .setInputCols(["token", "ner_chunk"])\
  .setOutputCol("ner_label")

pipeline = nlp.Pipeline(stages=[docAssembler,
                            sentenceDetector,
                            tokenizer,
                            embeddings,
                            nerModel,
                            nerConverter,
                            iobTagger])

text = """In 2020, we acquired certain assets of Spell Security Private Limited (also known as "Spell Security"). More specifically, their Compliance product - Policy Compliance (PC)")."""
df = spark.createDataFrame([[text]]).toDF("text")
result = pipeline.fit(df).transform(df)  

# chunk level result
result.selectExpr("explode(ner_chunk) as a") \
  .selectExpr("a.begin",
              "a.end",
              "a.result as ner_chunk",
              "a.metadata.entity as ner_label").show(50, False)

+-----+---+------------------------------+---------+
|begin|end|ner_chunk                     |ner_label|
+-----+---+------------------------------+---------+
|39   |68 |Spell Security Private Limited|ORG      |
|86   |99 |Spell Security                |ALIAS    |
|129  |138|Compliance                    |PRODUCT  |
|150  |166|Policy Compliance             |PRODUCT  |
|169  |170|PC                            |ALIAS    |
+-----+---+------------------------------+---------+

# token level result
result.selectExpr("explode(ner_label) as a") \
  .selectExpr("a.begin",
              "a.end",
              "a.metadata.word as word",
              "a.result as chunk").show(50, False)

+-----+---+------------+---------+
|begin|end|word        |chunk    |
+-----+---+------------+---------+
|0    |1  |In          |0        |
|3    |6  |2020        |0        |
|7    |7  |,           |0        |
|9    |10 |we          |0        |
|12   |19 |acquired    |0        |
|21   |27 |certain     |0        |
|29   |34 |assets      |0        |
|36   |37 |of          |0        |
|39   |43 |Spell       |B-ORG    |
|45   |52 |Security    |I-ORG    |
|54   |60 |Private     |I-ORG    |
|62   |68 |Limited     |I-ORG    |
|70   |70 |(           |0        |
|71   |74 |also        |0        |
|76   |80 |known       |0        |
|82   |83 |as          |0        |
|85   |85 |"           |0        |
|86   |90 |Spell       |B-ALIAS  |
|92   |99 |Security    |I-ALIAS  |
|100  |102|").         |0        |
|104  |107|More        |0        |
|109  |120|specifically|0        |
|121  |121|,           |0        |
|123  |127|their       |0        |
|129  |138|Compliance  |B-PRODUCT|
|140  |146|product     |0        |
|148  |148|-           |0        |
|150  |155|Policy      |B-PRODUCT|
|157  |166|Compliance  |I-PRODUCT|
|168  |168|(           |0        |
|169  |170|PC          |B-ALIAS  |
|171  |174|)").        |0        |
+-----+---+------------+---------+            
{%- endcapture -%}



{%- capture model_scala_medical -%}
import spark.implicits._

// Pipeline stages are defined where NER is done. NER is converted to chunks. 
val docAssembler = new DocumentAssembler()
  .setInputCol("text") 
  .setOutputCol("document") 

val sentenceDetector = new SentenceDetector()
  .setInputCols("document") 
  .setOutputCol("sentence") 

val tokenizer = new Tokenizer()
  .setInputCols("sentence") 
  .setOutputCol("token") 

val embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
  .setInputCols(Array("sentence","token")) 
  .setOutputCol("embs") 

val nerModel = MedicalNerModel.pretrained("ner_posology_greedy","en","clinical/models")
  .setInputCols(Array("sentence","token","embs")) 
  .setOutputCol("ner") 

val nerConverter = new NerConverter()
  .setInputCols(Array("sentence","token","ner")) 
  .setOutputCol("ner_chunk") 
  
// Define the IOB tagger,which needs tokens and chunks as input. Show results. 
val iobTagger = new IOBTagger()
  .setInputCols(Array("token","ner_chunk")) 
  .setOutputCol("ner_label") 

val pipeline = new Pipeline().setStages(Array(
                                              docAssembler,
                                              sentenceDetector,
                                              tokenizer,
                                              embeddings, 
                                              nerModel,
                                              nerConverter,
                                              iobTagger)) 

val text = "The patient was prescribed 1 capsule of Advil 10 mg for 5 days and magnesium hydroxide 100mg/1ml suspension PO." 
val df = Seq(text) .toDF("text") 
val result = pipeline.fit(df) .transform(df) 

// chunk level result
+-----+---+-------------------------------------------+---------+
|begin|end|ner_chunk                                  |ner_label|
+-----+---+-------------------------------------------+---------+
|27   |50 |1 capsule of Advil 10 mg                   |DRUG     |
|52   |61 |for 5 days                                 |DURATION |
|67   |109|magnesium hydroxide 100mg/1ml suspension PO|DRUG     |
+-----+---+-------------------------------------------+---------+

// token level result
+-----+---+----------+----------+
|begin|end|word      |chunk     |
+-----+---+----------+----------+
|0    |2  |The       |0         |
|4    |10 |patient   |0         |
|12   |14 |was       |0         |
|16   |25 |prescribed|0         |
|27   |27 |1         |B-DRUG    |
|29   |35 |capsule   |I-DRUG    |
|37   |38 |of        |I-DRUG    |
|40   |44 |Advil     |I-DRUG    |
|46   |47 |10        |I-DRUG    |
|49   |50 |mg        |I-DRUG    |
|52   |54 |for       |B-DURATION|
|56   |56 |5         |I-DURATION|
|58   |61 |days      |I-DURATION|
|63   |65 |and       |0         |
|67   |75 |magnesium |B-DRUG    |
|77   |85 |hydroxide |I-DRUG    |
|87   |95 |100mg/1ml |I-DRUG    |
|97   |106|suspension|I-DRUG    |
|108  |109|PO        |I-DRUG    |
|110  |110|.         |0         |
+-----+---+----------+----------+              

{%- endcapture -%}


{%- capture model_scala_legal -%}
import spark.implicits._

// Pipeline stages are defined where NER is done. NER is converted to chunks. 
val docAssembler = new DocumentAssembler()
  .setInputCol("text") 
  .setOutputCol("document") 

val sentenceDetector = new SentenceDetector()
  .setInputCols("document") 
  .setOutputCol("sentence") 

val tokenizer = new Tokenizer()
  .setInputCols("sentence") 
  .setOutputCol("token") 

val embeddings = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en")
  .setInputCols(Array("sentence","token")) 
  .setOutputCol("embs") 

val ner_model = LegalNerModel.pretrained("legner_orgs_prods_alias","en","legal/models")
  .setInputCols(Array("sentence","token","embs")) 
  .setOutputCol("ner") 

val nerConverter = new NerConverter()
  .setInputCols(Array("sentence","token","ner")) 
  .setOutputCol("ner_chunk") 
  
// Define the IOB tagger,which needs tokens and chunks as input. Show results. 
val iobTagger = new IOBTagger()
  .setInputCols(Array("token","ner_chunk")) 
  .setOutputCol("ner_label") 

val pipeline = new Pipeline().setStages(Array(
                                              docAssembler,
                                              sentenceDetector,
                                              tokenizer,
                                              embeddings, 
                                              ner_model,
                                              nerConverter,
                                              iobTagger)) 

val text = """This
 INTELLECTUAL PROPERTY AGREEMENT (this "Agreement") ,dated as of December 31,2018 (the "Effective Date") is entered into by and between Armstrong Flooring,Inc.,a Delaware corporation ("Seller") and AFI Licensing LLC,a Delaware limited liability company ("Licensing" and together with Seller,"Arizona") and AHF Holding,Inc. (formerly known as Tarzan HoldCo,Inc.) ,a Delaware corporation ("Buyer") and Armstrong Hardwood Flooring Company,a Tennessee corporation (the "Company" and together with Buyer the "Buyer Entities") (each of Arizona on the one hand and the Buyer Entities on the other hand,a "Party" and collectively,the "Parties") .""" 
val df = Seq(text) .toDF("text") 
val result = pipeline.fit(df) .transform(df)

// chunk level result
+-----+---+-----------------------------------+---------+
|begin|end|ner_chunk                          |ner_label|
+-----+---+-----------------------------------+---------+
|141  |165|Armstrong Flooring, Inc.,          |ORG      |
|192  |197|Seller                             |ALIAS    |
|205  |221|AFI Licensing LLC                  |ORG      |
|263  |271|Licensing                          |ALIAS    |
|292  |297|Seller                             |ALIAS    |
|301  |307|Arizona                            |ALIAS    |
|315  |330|AHF Holding, Inc                   |ORG      |
|399  |403|Buyer                              |ALIAS    |
|411  |445|Armstrong Hardwood Flooring Company|ORG      |
|478  |484|Company                            |ALIAS    |
|505  |509|Buyer                              |ALIAS    |
|516  |529|Buyer Entities                     |ALIAS    |
|542  |548|Arizona                            |ALIAS    |
|574  |587|Buyer Entities                     |ALIAS    |
|611  |615|Party                              |ALIAS    |
|641  |647|Parties                            |ALIAS    |
+-----+---+-----------------------------------+---------+

// token level result
+-----+---+------------+-------+
|begin|end|word        |chunk  |
+-----+---+------------+-------+
|0    |3  |This        |0      |
|5    |16 |INTELLECTUAL|0      |
|18   |25 |PROPERTY    |0      |
|27   |35 |AGREEMENT   |0      |
|37   |37 |(           |0      |
|38   |41 |this        |0      |
|43   |43 |"           |0      |
|44   |52 |Agreement   |0      |
|53   |55 |"),         |0      |
|57   |61 |dated       |0      |
|63   |64 |as          |0      |
|66   |67 |of          |0      |
|69   |76 |December    |0      |
|78   |79 |31          |0      |
|80   |80 |,           |0      |
|82   |85 |2018        |0      |
|87   |87 |(           |0      |
|88   |90 |the         |0      |
|92   |92 |"           |0      |
|93   |101|Effective   |0      |
|103  |106|Date        |0      |
|107  |108|")          |0      |
|110  |111|is          |0      |
|113  |119|entered     |0      |
|121  |124|into        |0      |
|126  |127|by          |0      |
|129  |131|and         |0      |
|133  |139|between     |0      |
|141  |149|Armstrong   |B-ORG  |
|151  |158|Flooring    |I-ORG  |
|159  |159|,           |I-ORG  |
|161  |163|Inc         |I-ORG  |
|164  |165|.,          |I-ORG  |
|167  |167|a           |0      |
|169  |176|Delaware    |0      |
|178  |188|corporation |0      |
|190  |191|("          |0      |
|192  |197|Seller      |B-ALIAS|
|198  |199|")          |0      |
|201  |203|and         |0      |
|205  |207|AFI         |B-ORG  |
|209  |217|Licensing   |I-ORG  |
|219  |221|LLC         |I-ORG  |
|222  |222|,           |0      |
|224  |224|a           |0      |
|226  |233|Delaware    |0      |
|235  |241|limited     |0      |
|243  |251|liability   |0      |
|253  |259|company     |0      |
|261  |262|("          |0      |
+-----+---+------------+-------+
only showing top 50 rows   
{%- endcapture -%}


{%- capture model_scala_finance -%}
import spark.implicits._

// Pipeline stages are defined where NER is done. NER is converted to chunks. 
val docAssembler = new DocumentAssembler()
  .setInputCol("text") 
  .setOutputCol("document") 

val sentenceDetector = new SentenceDetector()
  .setInputCols("document") 
  .setOutputCol("sentence") 

val tokenizer = new Tokenizer()
  .setInputCols("sentence")
  .setOutputCol("token") 

val embeddings = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en")
  .setInputCols(Array("sentence","token")) 
  .setOutputCol("embs") 

val nerModel = FinanceNerModel.pretrained("finner_orgs_prods_alias","en","finance/models")
  .setInputCols(Array("sentence","token","embs")) 
  .setOutputCol("ner") 

val nerConverter = new NerConverter()
  .setInputCols(Array("sentence","token","ner"))
  .setOutputCol("ner_chunk") 

// Define the IOB tagger,which needs tokens and chunks as input. Show results. 
val iobTagger = new IOBTagger()
  .setInputCols(Array("token","ner_chunk")) 
  .setOutputCol("ner_label") 

val pipeline = new Pipeline().setStages(Array(
                                              docAssembler,
                                              sentenceDetector,
                                              tokenizer,
                                              embeddings, 
                                              nerModel, 
                                              nerConverter,
                                              iobTagger)) 

val text = """In 2020, we acquired certain assets of Spell Security Private Limited (also known as "Spell Security") . More specifically,their Compliance product - Policy Compliance (PC)).""" 
val df = Seq(text) .toDF("text") 
val result = pipeline.fit(df) .transform(df) 

// chunk level result
+-----+---+------------------------------+---------+
|begin|end|ner_chunk                     |ner_label|
+-----+---+------------------------------+---------+
|39   |68 |Spell Security Private Limited|ORG      |
|86   |99 |Spell Security                |ALIAS    |
|129  |138|Compliance                    |PRODUCT  |
|150  |166|Policy Compliance             |PRODUCT  |
|169  |170|PC                            |ALIAS    |
+-----+---+------------------------------+---------+

// token level result
+-----+---+------------+---------+
|begin|end|word        |chunk    |
+-----+---+------------+---------+
|0    |1  |In          |0        |
|3    |6  |2020        |0        |
|7    |7  |,           |0        |
|9    |10 |we          |0        |
|12   |19 |acquired    |0        |
|21   |27 |certain     |0        |
|29   |34 |assets      |0        |
|36   |37 |of          |0        |
|39   |43 |Spell       |B-ORG    |
|45   |52 |Security    |I-ORG    |
|54   |60 |Private     |I-ORG    |
|62   |68 |Limited     |I-ORG    |
|70   |70 |(           |0        |
|71   |74 |also        |0        |
|76   |80 |known       |0        |
|82   |83 |as          |0        |
|85   |85 |"           |0        |
|86   |90 |Spell       |B-ALIAS  |
|92   |99 |Security    |I-ALIAS  |
|100  |102|").         |0        |
|104  |107|More        |0        |
|109  |120|specifically|0        |
|121  |121|,           |0        |
|123  |127|their       |0        |
|129  |138|Compliance  |B-PRODUCT|
|140  |146|product     |0        |
|148  |148|-           |0        |
|150  |155|Policy      |B-PRODUCT|
|157  |166|Compliance  |I-PRODUCT|
|168  |168|(           |0        |
|169  |170|PC          |B-ALIAS  |
|171  |174|)").        |0        |
+-----+---+------------+---------+
{%- endcapture -%}



{%- capture model_api_link -%}
[IOBTagger](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/ner/IOBTagger.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[IOBTagger](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/ner/iob_tagger/index.html#sparknlp_jsl.annotator.ner.iob_tagger.IOBTagger)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[IOBTaggerNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/IOBTagger.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_python_legal=model_python_legal
model_python_finance=model_python_finance
model_scala_medical=model_scala_medical
model_scala_legal=model_scala_legal
model_scala_finance=model_scala_finance
model_api_link=model_api_link
model_python_api_link=model_python_api_link
model_notebook_link=model_notebook_link
%}
