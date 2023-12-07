{%- capture title -%}
ReIdentification
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
 This annotator can reidentifies obfuscated entities by DeIdentification. It requires the outputs from the deidentification as input. Input columns need to be the deidentified document and the deidentification mappings set with `DeIdentification.setMappingsColumn`.
{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT,CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_ner = medical.NerModel.pretrained("ner_deid_generic_augmented", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

deidentification = medical.DeIdentification() \
    .setInputCols(["sentence", "token", "ner_chunk"]) \
    .setOutputCol("deidentified") \
    .setMode("mask")\
    .setReturnEntityMappings(True) #  return a new column to save the mappings between the mask/obfuscated entities and original entities.
    #.setMappingsColumn("MappingCol") # change the name of the column, 'aux' is default

pipeline = nlp.Pipeline(stages=[
      documentAssembler,
      sentenceDetector,
      tokenizer,
      word_embeddings,
      clinical_ner,
      ner_converter,
      deidentification])

text = """
Record date : 2093-01-13 , David Hale , M.D . , Name : Hendrickson Ora ,
MR # 7194334 Date : 01/13/93 . PCP : Oliveira , 25 years-old , Record date : 2079-11-09 .
Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 .
"""
data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

result.select(F.explode(F.arrays_zip(result.sentence.result, 
                                     result.deidentified.result)).alias("cols"))\
      .select(F.expr("cols['0']").alias("sentence"), 
              F.expr("cols['1']").alias("deidentified")).show(truncate = False)

+-----------------------------------------------------------------------+-------------------------------------------------------+
|sentence                                                               |deidentified                                           |
+-----------------------------------------------------------------------+-------------------------------------------------------+
|Record date : 2093-01-13 , David Hale , M.D .                          |Record date : <DATE> , <NAME> , M.D .                  |
|, Name : Hendrickson Ora , MR # 7194334 Date : 01/13/93 .              |, Name : <NAME> , MR # <ID> Date : <DATE> .            |
|PCP : Oliveira , 25 years-old , Record date : 2079-11-09 .             |PCP : <NAME> , <AGE> years-old , Record date : <DATE> .|
|Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 .|<LOCATION> , <LOCATION> , Phone <CONTACT> .            |
+-----------------------------------------------------------------------+-------------------------------------------------------+

reIdentification = medical.ReIdentification()\
    .setInputCols(["aux","deidentified"])\
    .setOutputCol("original")

reid_result = reIdentification.transform(result)

reid_result.select('original.result').show(truncate=False)

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[Record date : 2093-01-13 , David Hale , M.D ., , Name : Hendrickson Ora ,MR # 7194334 Date : 01/13/93 ., PCP : Oliveira , 25 years-old , Record date : 2079-11-09 ., Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 .] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_scala_medical -%}
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

val clinicalNer = MedicalNerModel.pretrained("ner_deid_generic_augmented", "en", "clinical/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner")

val nerConverter = new NerConverter()
  .setInputCols(Array("sentence", "token", "ner"))
  .setOutputCol("ner_chunk")

val deidentification = new DeIdentification()
  .setInputCols(Array("sentence", "token", "ner_chunk"))
  .setOutputCol("deidentified")
  .setMode("mask")
  .setReturnEntityMappings(true)

val pipeline = new Pipeline()
  .setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    wordEmbeddings,
    clinicalNer,
    nerConverter,
    deidentification
  ))

val text = """
Record date : 2093-01-13 , David Hale , M.D . , Name : Hendrickson Ora ,
MR # 7194334 Date : 01/13/93 . PCP : Oliveira , 25 years-old , Record date : 2079-11-09 .
Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 .
"""

val data = Seq((text)).toDF("text")

val result = pipeline.fit(data).transform(data)

result.selectExpr("explode(arrays_zip(sentence.result, deidentified.metadata)) as cols")
      .selectExpr("cols['0'] as sentence", "cols['1']['entity'] as deidentified").show(false)

+-----------------------------------------------------------------------+-------------------------------------------------------+
|sentence                                                               |deidentified                                           |
+-----------------------------------------------------------------------+-------------------------------------------------------+
|Record date : 2093-01-13 , David Hale , M.D .                          |Record date : <DATE> , <NAME> , M.D .                  |
|, Name : Hendrickson Ora , MR # 7194334 Date : 01/13/93 .              |, Name : <NAME> , MR # <ID> Date : <DATE> .            |
|PCP : Oliveira , 25 years-old , Record date : 2079-11-09 .             |PCP : <NAME> , <AGE> years-old , Record date : <DATE> .|
|Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 .|<LOCATION> , <LOCATION> , Phone <CONTACT> .            |
+-----------------------------------------------------------------------+-------------------------------------------------------+

val reIdentification = new ReIdentification()
  .setInputCols(Array("aux", "deidentified"))
  .setOutputCol("original")

val reidResult = reIdentification.transform(result)

reidResult.selectExpr("original.result").show(false)

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[Record date : 2093-01-13 , David Hale , M.D ., , Name : Hendrickson Ora ,MR # 7194334 Date : 01/13/93 ., PCP : Oliveira , 25 years-old , Record date : 2079-11-09 ., Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 .] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_python_legal -%}
from johnsnowlabs import nlp, legal

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

legal_ner = legal.NerModel.pretrained("legner_contract_doc_parties_lg", "en", "legal/models")\
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner") 

ner_converter = legal.NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setReplaceLabels({"ALIAS": "PARTY"}) # "ALIAS" are secondary names of companies, so let's extract them also as PARTY

deidentification = legal.DeIdentification() \
    .setInputCols(["sentence", "token", "ner_chunk"]) \
    .setOutputCol("deidentified") \
    .setMode("mask")\
    .setReturnEntityMappings(True) #  return a new column to save the mappings between the mask/obfuscated entities and original entities. REquired for "ReIdentification"
    #.setMappingsColumn("MappingCol") # change the name of the column, 'aux' is default

pipeline = nlp.Pipeline(stages=[
      documentAssembler, 
      sentenceDetector,
      tokenizer,
      embeddings,
      legal_ner,
      ner_converter,
      deidentification])

text = """THIS STRATEGIC ALLIANCE AGREEMENT ("Agreement") is made and entered into as of December 14, 2016 , by and between Hyatt Franchising Latin America, L.L.C. a limited liability company organized and existing under the laws of the State of Delaware"""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

result.select("deidentified.result").show(truncate = False)

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[THIS <DOC> ("Agreement") is made and entered into as of <EFFDATE> , by and between <PARTY>. a limited liability company organized and existing under the laws of the State of Delaware]|
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

reIdentification = legal.ReIdentification()\
    .setInputCols(["aux","deidentified"])\
    .setOutputCol("original")

reid_result = reIdentification.transform(result)

reid_result.select('original.result').show(truncate=False)

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[THIS STRATEGIC ALLIANCE AGREEMENT ("Agreement") is made and entered into as of December 14, 2016 , by and between Hyatt Franchising Latin America, L.L.C. a limited liability company organized and existing under the laws of the State of Delaware]|
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_scala_legal -%}
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val embeddings = RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base", "en")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

val legalNer = LegalNerModel.pretrained("legner_contract_doc_parties_lg", "en", "legal/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner")

val nerConverter = new NerConverterInternal()
  .setInputCols(Array("sentence", "token", "ner"))
  .setOutputCol("ner_chunk")
  .setReplaceLabels(Map("ALIAS" -> "PARTY"))

val deidentification = new DeIdentification()
  .setInputCols(Array("sentence", "token", "ner_chunk"))
  .setOutputCol("deidentified")
  .setMode("mask")
  .setReturnEntityMappings(true)

val pipeline = new Pipeline()
  .setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    embeddings,
    legalNer,
    nerConverter,
    deidentification
  ))

val text = "THIS STRATEGIC ALLIANCE AGREEMENT (\"Agreement\") is made and entered into as of December 14, 2016, by and between Hyatt Franchising Latin America, L.L.C. a limited liability company organized and existing under the laws of the State of Delaware"

val data = Seq(text).toDF("text")

val result = pipeline.fit(data).transform(data)

result.selectExpr("deidentified.result").show(false)

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[THIS <DOC> ("Agreement") is made and entered into as of <EFFDATE> , by and between <PARTY>. a limited liability company organized and existing under the laws of the State of Delaware]|
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

val reIdentification = new ReIdentification()
  .setInputCols(Array("aux", "deidentified"))
  .setOutputCol("original")

val reidResult = reIdentification.transform(result)

reidResult.selectExpr("original.result").show(false)

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[THIS STRATEGIC ALLIANCE AGREEMENT ("Agreement") is made and entered into as of December 14, 2016 , by and between Hyatt Franchising Latin America, L.L.C. a limited liability company organized and existing under the laws of the State of Delaware]|
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_python_finance -%}
from johnsnowlabs import nlp, finance

documentAssembler = nlp.DocumentAssembler()\
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
    .setOutputCol("embeddings")

ner_model = finance.NerModel.pretrained('finner_sec_10k_summary', 'en', 'finance/models')\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = finance.NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

deidentification = finance.DeIdentification() \
    .setInputCols(["sentence", "token", "ner_chunk"]) \
    .setOutputCol("deidentified") \
    .setMode("mask")\
    .setReturnEntityMappings(True) #  return a new column to save the mappings between the mask/obfuscated entities and original entities. REquired for "ReIdentification"
    #.setMappingsColumn("MappingCol") # change the name of the column, 'aux' is default

pipeline = nlp.Pipeline(stages=[
      documentAssembler, 
      sentenceDetector,
      tokenizer,
      embeddings,
      ner_model,
      ner_converter,
      deidentification])

text= """
Commission file number 000-15867 
_____________________________________
 
CADENCE DESIGN SYSTEMS, INC. 
(Exact name of registrant as specified in its charter)
____________________________________ 
Delaware
 
00-0000000
(State or Other Jurisdiction ofIncorporation or Organization)
 
(I.R.S. EmployerIdentification No.)
2655 Seely Avenue, Building 5,
San Jose,
California
 
95134
(Address of Principal Executive Offices)
 
(Zip Code)
(408)
-943-1234 
(Registrant’s Telephone Number, including Area Code) 
Securities registered pursuant to Section 12(b) of the Act:
Title of Each Class
Trading Symbol(s)
Names of Each Exchange on which Registered
Common Stock, $0.01 par value per share
CDNS
Nasdaq Global Select Market
Securities registered pursuant to Section 12(g) of the Act:"""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

result.select("deidentified.result").show(truncate = False)

+-------------------------------------------------------------------------------------------------------------+
|result                                                                                                       |
+-------------------------------------------------------------------------------------------------------------+
|[Commission file number <CFN> 
_____________________________________
 
<ORG>., (Exact name of registrant as specified in its charter)
____________________________________ 
<STATE>
 
<IRS>
(State or Other Jurisdiction ofIncorporation or Organization)
 
(I.R.S., EmployerIdentification No., )
<ADDRESS>
 
95134
(Address of Principal Executive Offices)
 
(Zip Code)
<PHONE> 
(Registrant’s Telephone Number, including Area Code) 
Securities registered pursuant to Section 12, (b) of the Act:
Title of Each Class
Trading Symbol, (s)
Names of Each Exchange on which Registered
<TITLE_CLASS>, <TITLE_CLASS_VALUE> par value per share
<TICKER>
<STOCK_EXCHANGE>
Securities registered pursuant to Section 12, (g) of the Act:]|
+-------------------------------------------------------------------------------------------------------------+

reIdentification = finance.ReIdentification()\
    .setInputCols(["aux","deidentified"])\
    .setOutputCol("original")

reid_result = reIdentification.transform(result)

reid_result.select('original.result').show(truncate=False)

+---------------------------------------------------------------------------------------------------+
|result                                                                                             |
+---------------------------------------------------------------------------------------------------+
|[Commission file number 000-15867 
_____________________________________
 
CADENCE DESIGN SYSTEMS, INC., (Exact name of registrant as specified in its charter)
____________________________________ 
Delaware
 
00-0000000
(State or Other Jurisdiction ofIncorporation or Organization)
 
(I.R.S., EmployerIdentification No., )
2655 Seely Avenue, Building 5,
San Jose,
California
 
95134
(Address of Principal Executive Offices)
 
(Zip Code)<(408)
-943-1234
(Registrant’s Telephone Number, including Area Code) 
Securities registered pursuant to Section 12, (b) of the Act:
Title of Each Class
Trading Symbol, (s)
Names of Each Exchange on which Registered
Common Stock, $0.01 par value per share
CDNS
Nasdaq Global Select Market
Securities registered pursuant to Section 12, (g) of the Act:]|
+---------------------------------------------------------------------------------------------------+

{%- endcapture -%}

{%- capture model_scala_finance -%}
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val embeddings = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base", "en")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

val nerModel = FinanceNerModel.pretrained("finner_sec_10k_summary", "en", "finance/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner")

val nerConverter = new NerConverter()
  .setInputCols(Array("sentence", "token", "ner"))
  .setOutputCol("ner_chunk")

val deidentification = new DeIdentification()
  .setInputCols(Array("sentence", "token", "ner_chunk"))
  .setOutputCol("deidentified")
  .setMode("mask")
  .setReturnEntityMappings(true)

val pipeline = new Pipeline()
  .setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    embeddings,
    nerModel,
    nerConverter,
    deidentification
  ))

val text = "Commission file number 000-15867 
_____________________________________
 
CADENCE DESIGN SYSTEMS, INC. 
(Exact name of registrant as specified in its charter)
____________________________________ 
Delaware
 
00-0000000
(State or Other Jurisdiction ofIncorporation or Organization)
 
(I.R.S. EmployerIdentification No.)
2655 Seely Avenue, Building 5,
San Jose,
California
 
95134
(Address of Principal Executive Offices)
 
(Zip Code)
(408)
-943-1234 
(Registrant’s Telephone Number, including Area Code) 
Securities registered pursuant to Section 12(b) of the Act:
Title of Each Class
Trading Symbol(s)
Names of Each Exchange on which Registered
Common Stock, $0.01 par value per share
CDNS
Nasdaq Global Select Market
Securities registered pursuant to Section 12(g) of the Act:"

val data = Seq(text).toDF("text")

val result = pipeline.fit(data).transform(data)

result.selectExpr("deidentified.result").show(false)

+-------------------------------------------------------------------------------------------------------------+
|result                                                                                                       |
+-------------------------------------------------------------------------------------------------------------+
|[Commission file number <CFN> 
_____________________________________
 
<ORG>., (Exact name of registrant as specified in its charter)
____________________________________ 
<STATE>
 
<IRS>
(State or Other Jurisdiction ofIncorporation or Organization)
 
(I.R.S., EmployerIdentification No., )
<ADDRESS>
 
95134
(Address of Principal Executive Offices)
 
(Zip Code)
<PHONE> 
(Registrant’s Telephone Number, including Area Code) 
Securities registered pursuant to Section 12, (b) of the Act:
Title of Each Class
Trading Symbol, (s)
Names of Each Exchange on which Registered
<TITLE_CLASS>, <TITLE_CLASS_VALUE> par value per share
<TICKER>
<STOCK_EXCHANGE>
Securities registered pursuant to Section 12, (g) of the Act:]|
+-------------------------------------------------------------------------------------------------------------+

val reIdentification = new ReIdentification()
  .setInputCols(Array("aux", "deidentified"))
  .setOutputCol("original")

val reidResult = reIdentification.transform(result)

reidResult.selectExpr("original.result").show(false)

+---------------------------------------------------------------------------------------------------+
|result                                                                                             |
+---------------------------------------------------------------------------------------------------+
|[Commission file number 000-15867 
_____________________________________
 
CADENCE DESIGN SYSTEMS, INC., (Exact name of registrant as specified in its charter)
____________________________________ 
Delaware
 
00-0000000
(State or Other Jurisdiction ofIncorporation or Organization)
 
(I.R.S., EmployerIdentification No., )
2655 Seely Avenue, Building 5,
San Jose,
California
 
95134
(Address of Principal Executive Offices)
 
(Zip Code)<(408)
-943-1234
(Registrant’s Telephone Number, including Area Code) 
Securities registered pursuant to Section 12, (b) of the Act:
Title of Each Class
Trading Symbol, (s)
Names of Each Exchange on which Registered
Common Stock, $0.01 par value per share
CDNS
Nasdaq Global Select Market
Securities registered pursuant to Section 12, (g) of the Act:]|
+---------------------------------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_api_link -%}
[ReIdentification](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/deid/ReIdentification.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[ReIdentification](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/deid/reIdentification/index.html#sparknlp_jsl.annotator.deid.reIdentification.ReIdentification)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[ReIdentification](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ReIdentification.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical
model_python_finance=model_python_finance
model_scala_finance=model_scala_finance
model_python_legal=model_python_legal
model_scala_legal=model_scala_legal
model_api_link=model_api_link
model_python_api_link=model_python_api_link
model_notebook_link=model_notebook_link
%}
