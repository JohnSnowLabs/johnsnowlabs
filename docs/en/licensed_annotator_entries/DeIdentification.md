{%- capture title -%}
DeIdentification
{%- endcapture -%}

{%- capture approach -%}
approach
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
Deidentification is a critical and important technology to facilitate the use of structured or unstructured clinical text while protecting patient privacy and confidentiality. John Snow Labs teams has invested great efforts in developing methods and corpora for deidentification of clinical text, PDF, image, DICOM, containing Protected Health Information (PHI):

*   individual’s past, present, or future physical or mental health or condition.
*   provision of health care to the individual.
*   past, present, or future payment for the health care.

Protected health information includes many common identifiers (e.g., name, address, birth date, Social Security Number) when they can be associated with the health information.

Spark NLP for Healthcare proposes several techniques and strategies for deidentification, the principal ones are:


*   **Mask**:

          *   entity_labels: Mask with the entity type of that chunk. (default)
          *   same_length_chars: Mask the deid entities with same length of asterix ( * ) with brackets ( [ , ] ) on both end.
          *   fixed_length_chars: Mask the deid entities with a fixed length of asterix ( * ). The length is setting up using the setFixedMaskLength() method.


*   **Obfuscation**: replace sensetive entities with random values of the same type.

*   **Faker**:  allows the user to use a set of fake entities that are in the memory of spark-nlp-internal

Also there is an advanced option allowing to deidentify with multiple modes at the same time. (Multi-Mode Deididentification).
Deidentifies Input Annotations of types DOCUMENT, TOKEN and CHUNK, by either masking or obfuscating the given CHUNKS.

- `ageRanges`: (IntArrayParam)
List of integers specifying limits of the age groups to preserve during obfuscation

- `blackList`: (StringArrayParam)
List of entities that will be ignored to in the regex file.

- `consistentObfuscation`: (BooleanParam)
Whether to replace very similar entities in a document with the same randomized term (default: true) The similarity is based on the Levenshtein Distance between the words.

- `dateFormats`: (StringArrayParam)
Format of dates to displace

- `dateTag`: (Param[String])
Tag representing what are the NER entity (default: DATE)

- `dateToYear`: (BooleanParam)
true if dates must be converted to years, false otherwise

- `days`: (IntParam)
Number of days to obfuscate the dates by displacement.

- `fixedMaskLength`: (IntParam)
Select the fixed mask length: this is the length of the masking sequence that will be used when the 'fixed_length_chars' masking policy is selected.

- `ignoreRegex`: (BooleanParam)
Select if you want to use regex file loaded in the model.

- `isRandomDateDisplacement`: (BooleanParam)
Use a random displacement days in dates entities,that random number is based on the DeIdentificationParams.seed If true use random displacement days in dates entities,if false use the DeIdentificationParams.days The default value is false.

- `language`: (Param[String])
The language used to select the regex file and some faker entities.'en'(english),'de'(German), 'es'(Spanish), 'fr'(French) or 'ro'(Romanian)

- `mappingsColumn`: (Param[String])
This is the mapping column that will return the Annotations chunks with the fake entities

- `maskingPolicy`: (Param[String])
Select the masking policy:
same_length_chars: Replace the obfuscated entity with a masking sequence composed of asterisks and surrounding squared brackets, being the total length of the masking sequence of the same length as the original sequence. Example, Smith -> [***]. If the entity is less than 3 chars (like Jo, or 5), asterisks without brackets will be returned. entity_labels: Replace the values with the corresponding entity labels. fixed_length_chars: Replace the obfuscated entity with a masking sequence composed of a fixed number of asterisks.

- `minYear`: (IntParam)
Minimum year to use when converting date to year

- `mode`: (Param[String])
Mode for Anonymizer ['mask'|'obfuscate'] Given the following text

- `obfuscateDate`: (BooleanParam)
When mode=="obfuscate" whether to obfuscate dates or not.

- `obfuscateRefFile`: (Param[String])
File with the terms to be used for Obfuscation

- `obfuscateRefSource`: (Param[String])
The source of obfuscation of to obfuscate the entities.For dates entities doesnt apply tha method.

- `outputAsDocument`: (BooleanParam)
Whether to return all sentences joined into a single document

- `refFileFormat`: (Param[String])
Format of the reference file for Obfuscation the default value for that is "csv"

- `refSep`: (Param[String])
Separator character for the csv reference file for Obfuscation de default value is "#"

- `regexOverride`: (BooleanParam)
If is true prioritize the regex entities, if is false prioritize the ner.

- `regexPatternsDictionary`: (ExternalResourceParam)
dictionary with regular expression patterns that match some protected entity if the dictionary in not setting up we will use the default regex file.

- `region`: (Param[String])
Usa or eu

- `returnEntityMappings`: (BooleanParam)
With this property you select if you want to return mapping column

- `sameEntityThreshold`: (DoubleParam)
Similarity threshold [0.0-1.0] to consider two appearances of an entity as the same (default: 0.9) For date entities this method doesn't apply.

- `sameLengthFormattedEntities`: (StringArrayParam)
List of formatted entities to generate the same length outputs as original ones during obfuscation.

- `seed`: (IntParam)
It is the seed to select the entities on obfuscate mode.With the seed you can reply a execution several times with the same ouptut.

- `selectiveObfuscationModesPath`: (Param[String])
Dictionary path where is the json that contains the selective obfuscation modes

- `unnormalizedDateMode`: (Param[String])
The mode to use if the date is not formatted.

- `zipCodeTag`: (Param[String])
Tag representing zip codes in the obfuscate reference file (default: ZIP).


To create a configured DeIdentificationModel, please see the example of DeIdentification.
{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, TOKEN, CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_api_link -%}
[DeIdentificationModel](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/deid/DeIdentificationModel.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[DeIdentificationModel](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/deid/deIdentification/index.html#sparknlp_jsl.annotator.deid.deIdentification.DeIdentificationModel)
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

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

# NER model trained on n2c2 (de-identification and Heart Disease Risk Factors Challenge) datasets)
clinical_ner = medical.NerModel.pretrained("ner_deid_generic_augmented", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

#deid model with "entity_labels"
deid_entity_labels= medical.DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"])\
    .setOutputCol("deid_entity_label")\
    .setMode("mask")\
    .setReturnEntityMappings(True)\
    .setMaskingPolicy("entity_labels")

obs_lines = """Marvin MARSHALL#PATIENT
Hubert GROGAN#PATIENT
ALTHEA COLBURN#PATIENT
Kalil AMIN#PATIENT
Inci FOUNTAIN#PATIENT
Ekaterina Rosa#DOCTOR
Rudiger Chao#DOCTOR
COLLETTE KOHLER#NAME
Mufi HIGGS#NAME"""

with open ('obfuscation.txt', 'w') as f:
  f.write(obs_lines)

obfuscation = medical.DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"]) \
    .setOutputCol("deidentified") \
    .setMode("obfuscate")\
    .setObfuscateDate(True)\
    .setObfuscateRefFile('obfuscation.txt')\
    .setObfuscateRefSource("both")\  #file or faker
    .setGenderAwareness(True)\
    .setLanguage("en")\
    .setUnnormalizedDateMode("obfuscate")  #mask or skip

deidPipeline = nlp.Pipeline(stages=[
      documentAssembler,
      sentenceDetector,
      tokenizer,
      word_embeddings,
      clinical_ner,
      ner_converter,
      deid_entity_labels,
      obfuscation
      ])


empty_data = spark.createDataFrame([[""]]).toDF("text")


model = deidPipeline.fit(empty_data)

#sample data
text ='''
Record date : 2093-01-13 , David Hale , M.D . , Name : Hendrickson Ora , MR # 7194334 Date : 01/13/93 . PCP : Oliveira , 25 years-old , Record date : 2079-11-09 . Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 .
'''

result = model.transform(spark.createDataFrame([[text]]).toDF("text"))

result.select(F.explode(F.arrays_zip(result.sentence.result,
                                     result.deid_entity_label.result,
                                     result.deidentified.result,
                                     )).alias("cols")) \
      .select(F.expr("cols['0']").alias("sentence"),
              F.expr("cols['1']").alias("deid_entity_label"),
              F.expr("cols['2']").alias("deidentified"),
              ).toPandas()

|index|sentence|deid\_entity\_label|deidentified|
|---|---|---|---|
|0|Record date : 2093-01-13 , David Hale , M\.D \.|Record date : \<DATE\> , \<NAME\> , M\.D \.|Record date : 2093-02-13 , Wolf Hermes , M\.D \.|
|1|, Name : Hendrickson Ora , MR \# 7194334 Date : 01/13/93 \.|, Name : \<NAME\> , MR \# \<ID\> Date : \<DATE\> \.|, Name : Engel Rainier , MR \# 5822805 Date : 02/13/93 \.|
|2|PCP : Oliveira , 25 years-old , Record date : 2079-11-09 \.|PCP : \<NAME\> , \<AGE\> years-old , Record date : \<DATE\> \.|PCP : Damián Lango , 21 years-old , Record date : 2079-12-10 \.|
|3|Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 \.|\<LOCATION\> , \<LOCATION\> , Phone \<CONTACT\> \.|103 North Street , 2500 Bellevue Medical Center Dr , Phone 051-096-883 \.|


{%- endcapture -%}

{%- capture model_scala_medical -%}

val documentAssembler = new DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

// Sentence Detector annotator, processes various sentences per line
val sentenceDetector = new SentenceDetector()\
    .setInputCols(Array("document"))\
    .setOutputCol("sentence")

// Tokenizer splits words in a relevant format for NLP
val tokenizer = new Tokenizer()\
    .setInputCols(Array("sentence"))\
    .setOutputCol("token")

// Clinical word embeddings trained on PubMED dataset
val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(Array("sentence", "token")) \
    .setOutputCol("embeddings")

// NER model trained on n2c2 (de-identification and Heart Disease Risk Factors Challenge) datasets)
val clinical_ner = NerModel.pretrained("ner_deid_generic_augmented", "en", "clinical/models") \
    .setInputCols(Array("sentence", "token", "embeddings")) \
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()\
    .setInputCols(Array("sentence", "token", "ner"))\
    .setOutputCol("ner_chunk")

//deid model with "entity_labels"
val deid_entity_labels= new DeIdentification()
    .setInputCols(Array("ner_chunk", "token", "sentence")) \
    .setOutputCol("deid_entity_label")\
    .setMode("mask")\
    .setReturnEntityMappings(true)\
    .setMaskingPolicy("entity_labels")

import java.io.PrintWriter

val obs_lines = """Marvin MARSHALL#PATIENT
Hubert GROGAN#PATIENT
ALTHEA COLBURN#PATIENT
Kalil AMIN#PATIENT
Inci FOUNTAIN#PATIENT
Ekaterina Rosa#DOCTOR
Rudiger Chao#DOCTOR
COLLETTE KOHLER#NAME
Mufi HIGGS#NAME"""

val filename = "obfuscation.txt"
val writer = new PrintWriter(filename)
writer.write(obs_lines)
writer.close()

val obfuscation =  new DeIdentification()
    .setInputCols(Array("ner_chunk", "token", "sentence")) \
    .setOutputCol("deidentified") \
    .setMode("obfuscate")\
    .setObfuscateDate(true)\
    .setObfuscateRefFile('obfuscation.txt')\
    .setObfuscateRefSource("both")\        //file or faker  
    .setGenderAwareness(true)\
    .setLanguage("en")\
    .setUnnormalizedDateMode("obfuscate") //mask or skip



val deidPipeline = new Pipeline().setStages(Array(
                                                  documentAssembler,
                                                  sentenceDetector,
                                                  tokenizer,
                                                  word_embeddings,
                                                  clinical_ner,
                                                  ner_converter,
                                                  deid_entity_labels,
                                                  obfuscation
                                                ))




//sample data

val text =
          '''
          Record date : 2093-01-13 , David Hale , M.D . , Name : Hendrickson Ora , MR # 7194334 Date : 01/13/93 . PCP : Oliveira , 25 years-old , Record date : 2079-11-09 . Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 .
          '''

val data = Seq(text).toDF("text")

val result = new deidPipeline.fit(data).transform(data)

|index|sentence|deid\_entity\_label|deidentified|
|---|---|---|---|
|0|Record date : 2093-01-13 , David Hale , M\.D \.|Record date : \<DATE\> , \<NAME\> , M\.D \.|Record date : 2093-02-13 , Wolf Hermes , M\.D \.|
|1|, Name : Hendrickson Ora , MR \# 7194334 Date : 01/13/93 \.|, Name : \<NAME\> , MR \# \<ID\> Date : \<DATE\> \.|, Name : Engel Rainier , MR \# 5822805 Date : 02/13/93 \.|
|2|PCP : Oliveira , 25 years-old , Record date : 2079-11-09 \.|PCP : \<NAME\> , \<AGE\> years-old , Record date : \<DATE\> \.|PCP : Damián Lango , 21 years-old , Record date : 2079-12-10 \.|
|3|Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 \.|\<LOCATION\> , \<LOCATION\> , Phone \<CONTACT\> \.|103 North Street , 2500 Bellevue Medical Center Dr , Phone 051-096-883 \.|

{%- endcapture -%}

{%- capture model_scala_finance -%}
 
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")
val sentenceDetector = new SentenceDetector()
  .setInputCols(Array("document"))
  .setOutputCol("sentence")
val tokenizer = new Tokenizer()
  .setInputCols("sentence")
.setOutputCol("token")
val embeddings = RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base","en")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")
val bert_embeddings = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("bert_embeddings")
val fin_ner = FinanceNerModel.pretrained("finner_deid", "en", "finance/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner")
  .setLabelCasing("upper")
val ner_converter =  new NerConverterInternal()
  .setInputCols(Array("sentence", "token", "ner"))
  .setOutputCol("ner_chunk")
  .setReplaceLabels(Map("ORG" -> "PARTY")) 
// Replace "ORG" entity as "PARTY"
val ner_finner = FinanceNerModel.pretrained("finner_org_per_role_date", "en", "finance/models")
  .setInputCols(Array("sentence", "token", "bert_embeddings"))
  .setOutputCol("ner_finner")
  .setLabelCasing("upper")
val ner_converter_finner = new NerConverterInternal()
  .setInputCols(Array("sentence", "token", "ner_finner"))
  .setOutputCol("ner_finner_chunk")
  .setWhiteList(Array("ROLE")) 
// Just use "ROLE" entity from this NER
val chunk_merge =  new ChunkMergeApproach()
  .setInputCols(Array("ner_finner_chunk", "ner_chunk"))
  .setOutputCol("deid_merged_chunk")
val deidentification =  new DeIdentification()
  .setInputCols(Array("sentence", "token", "deid_merged_chunk"))
  .setOutputCol("deidentified")
  .setMode("mask")
  .setIgnoreRegex(true)
// Pipeline
val data = Seq("Jeffrey Preston Bezos is an American entrepreneur, founder and CEO of Amazon").toDF("text")
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
  chunk_merge,
  deidentification))
val result = nlpPipeline.fit(data).transform(data)

result.select("sentence.result", "deidentified.result").show()

|index|result|result|
|---|---|---|
|0|Jeffrey Preston Bezos is an American entrepreneur, founder and CEO of Amazon|\<PERSON\> is an \<COUNTRY\> entrepreneur, \<ROLE\> and \<ROLE\> of \<PARTY\>|


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

val embeddings = RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base","en")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val legal_ner = LegalNerModel.pretrained("legner_contract_doc_parties", "en", "legal/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner") 
    //.setLabelCasing("upper")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")\
    .setReplaceLabels(Map("ALIAS" -> "PARTY")) 

val ner_signers = LegalNerModel.pretrained("legner_signers", "en", "legal/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner_signers") 
    //.setLabelCasing("upper")

val ner_converter_signers = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner_signers"))
    .setOutputCol("ner_signer_chunk")

val chunk_merge = new ChunkMergeApproach()
    .setInputCols(Array("ner_signer_chunk", "ner_chunk"))
    .setOutputCol("deid_merged_chunk")

val deidentification = new DeIdentification()
    .setInputCols(Array("sentence", "token", "deid_merged_chunk"))
    .setOutputCol("deidentified") \
    .setMode("mask")\
    .setIgnoreRegex(true)

# Pipeline
val data = Seq("ENTIRE AGREEMENT.  This Agreement contains the entire understanding of the parties hereto with respect to the transactions and matters contemplated hereby, supersedes all previous Agreements between i-Escrow and 2TheMart concerning the subject matter.

2THEMART.COM, INC.:                         I-ESCROW, INC.:

By:Dominic J. Magliarditi                By:Sanjay Bajaj Name: Dominic J. Magliarditi                Name: Sanjay Bajaj Title: President                            Title: VP Business Development Date: 6/21/99                               Date: 6/11/99 ").toDF("text")

val nlpPipeline = new Pipeline().setStages(Array(
      documentAssembler, 
      sentenceDetector,
      tokenizer,
      embeddings,
      legal_ner,
      ner_converter,
      ner_signers,
      ner_converter_signers,
      chunk_merge,
      deidentification))

val result = nlpPipeline.fit(data).transform(data)
{%- endcapture -%}


{%- capture approach_description -%}
Contains all the methods for training a DeIdentificationModel model.
This module can obfuscate or mask the entities that contains personal information. These can be set with a file of
regex patterns with setRegexPatternsDictionary, where each line is a mapping of
entity to regex.
```
DATE \d{4}
AID \d{6,7}
```

Additionally, obfuscation strings can be defined with setObfuscateRefFile, where each line
is a mapping of string to entity. The format and seperator can be speficied with
setRefFileFormat and setRefSep.
```
Dr. Gregory House#DOCTOR
01010101#MEDICALRECORD
```

Ideally this annotator works in conjunction with Demographic Named EntityRecognizers that can be trained either using
[TextMatchers](/docs/en/annotators#textmatcher),
[RegexMatchers](/docs/en/annotators#regexmatcher),
[DateMatchers](/docs/en/annotators#datematcher),
[NerCRFs](/docs/en/annotators#nercrf) or
[NerDLs](/docs/en/annotators#nerdl)
{%- endcapture -%}

{%- capture approach_input_anno -%}
DOCUMENT, TOKEN, CHUNK
{%- endcapture -%}

{%- capture approach_output_anno -%}
DOCUMENT
{%- endcapture -%}


{%- capture approach_python_medical -%}

from johnsnowlabs import nlp, medical

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

# NER model trained on n2c2 (de-identification and Heart Disease Risk Factors Challenge) datasets)
clinical_ner = medical.NerModel.pretrained("ner_deid_generic_augmented", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

#deid model with "entity_labels"
deid_entity_labels= medical.DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"])\
    .setOutputCol("deid_entity_label")\
    .setMode("mask")\
    .setReturnEntityMappings(True)\
    .setMaskingPolicy("entity_labels")

obs_lines = """Marvin MARSHALL#PATIENT
Hubert GROGAN#PATIENT
ALTHEA COLBURN#PATIENT
Kalil AMIN#PATIENT
Inci FOUNTAIN#PATIENT
Ekaterina Rosa#DOCTOR
Rudiger Chao#DOCTOR
COLLETTE KOHLER#NAME
Mufi HIGGS#NAME"""

with open ('obfuscation.txt', 'w') as f:
  f.write(obs_lines)

obfuscation = medical.DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"]) \
    .setOutputCol("deidentified") \
    .setMode("obfuscate")\
    .setObfuscateDate(True)\
    .setObfuscateRefFile('obfuscation.txt')\
    .setObfuscateRefSource("both")\  #file or faker
    .setGenderAwareness(True)\
    .setLanguage("en")\
    .setUnnormalizedDateMode("obfuscate")  #mask or skip

deidPipeline = nlp.Pipeline(stages=[
      documentAssembler,
      sentenceDetector,
      tokenizer,
      word_embeddings,
      clinical_ner,
      ner_converter,
      deid_entity_labels,
      obfuscation
      ])


empty_data = spark.createDataFrame([[""]]).toDF("text")


model = deidPipeline.fit(empty_data)

#sample data
text ='''
Record date : 2093-01-13 , David Hale , M.D . , Name : Hendrickson Ora , MR # 7194334 Date : 01/13/93 . PCP : Oliveira , 25 years-old , Record date : 2079-11-09 . Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 .
'''

result = model.transform(spark.createDataFrame([[text]]).toDF("text"))

result.select(F.explode(F.arrays_zip(result.sentence.result,
                                     result.deid_entity_label.result,
                                     result.deidentified.result,
                                     )).alias("cols")) \
      .select(F.expr("cols['0']").alias("sentence"),
              F.expr("cols['1']").alias("deid_entity_label"),
              F.expr("cols['2']").alias("deidentified"),
              ).toPandas()

|index|sentence|deid\_entity\_label|deidentified|
|---|---|---|---|
|0|Record date : 2093-01-13 , David Hale , M\.D \.|Record date : \<DATE\> , \<NAME\> , M\.D \.|Record date : 2093-02-13 , Wolf Hermes , M\.D \.|
|1|, Name : Hendrickson Ora , MR \# 7194334 Date : 01/13/93 \.|, Name : \<NAME\> , MR \# \<ID\> Date : \<DATE\> \.|, Name : Engel Rainier , MR \# 5822805 Date : 02/13/93 \.|
|2|PCP : Oliveira , 25 years-old , Record date : 2079-11-09 \.|PCP : \<NAME\> , \<AGE\> years-old , Record date : \<DATE\> \.|PCP : Damián Lango , 21 years-old , Record date : 2079-12-10 \.|
|3|Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 \.|\<LOCATION\> , \<LOCATION\> , Phone \<CONTACT\> \.|103 North Street , 2500 Bellevue Medical Center Dr , Phone 051-096-883 \.|



{%- endcapture -%}

{%- capture approach_python_legal -%}
from johnsnowlabs import *

documentAssembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

 sentenceDetector = nlp.SentenceDetector() \
    .setInputCols(["document"]) \
    .setOutputCol("sentence") \
    .setUseAbbreviations(True)

tokenizer = nlp.Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

embeddings = nlp.WordEmbeddingsModel \
    .pretrained("embeddings_clinical", "en", "clinical/models") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

# Ner entities
ner_model = legal.NerModel.pretrained("legner_orgs_prods_alias", "en", "legal/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

nerConverter = nlp.NerConverter() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_con")

# Deidentification
deIdentification = legal.DeIdentification() \
    .setInputCols(["ner_chunk", "token", "sentence"]) \
    .setOutputCol("dei") \
    # file with custom regex pattern for custom entities
    .setRegexPatternsDictionary("path/to/dic_regex_patterns_main_categories.txt") \
    # file with custom obfuscator names for the entities
    .setObfuscateRefFile("path/to/obfuscate_fixed_entities.txt") \
    .setRefFileFormat("csv") \
    .setRefSep("#") \
    .setMode("obfuscate") \
    .setDateFormats(Array("MM/dd/yy","yyyy-MM-dd")) \
    .setObfuscateDate(True) \
    .setDateTag("DATE") \
    .setDays(5) \
    .setObfuscateRefSource("file")

# Pipeline
pipeline = Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    embeddings,
    ner_model,
    nerConverter,
    deIdentification
])
{%- endcapture -%}

{%- capture approach_python_finance -%}
from johnsnowlabs import *

documentAssembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

 sentenceDetector = nlp.SentenceDetector() \
    .setInputCols(["document"]) \
    .setOutputCol("sentence") \
    .setUseAbbreviations(True)

tokenizer = nlp.Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

embeddings = nlp.WordEmbeddingsModel \
    .pretrained("embeddings_clinical", "en", "clinical/models") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

# Ner entities
ner_model = finance.NerModel.pretrained("finner_orgs_prods_alias","en","finance/models")\
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

nerConverter = nlp.NerConverter() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_con")

# Deidentification
deIdentification = finance.DeIdentification() \
    .setInputCols(["ner_chunk", "token", "sentence"]) \
    .setOutputCol("dei") \
    # file with custom regex pattern for custom entities
    .setRegexPatternsDictionary("path/to/dic_regex_patterns_main_categories.txt") \
    # file with custom obfuscator names for the entities
    .setObfuscateRefFile("path/to/obfuscate_fixed_entities.txt") \
    .setRefFileFormat("csv") \
    .setRefSep("#") \
    .setMode("obfuscate") \
    .setDateFormats(Array("MM/dd/yy","yyyy-MM-dd")) \
    .setObfuscateDate(True) \
    .setDateTag("DATE") \
    .setDays(5) \
    .setObfuscateRefSource("file")

# Pipeline
pipeline = Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    embeddings,
    ner_model,
    nerConverter,
    deIdentification
])
{%- endcapture -%}


{%- capture approach_scala_medical -%}
val documentAssembler = new DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

// Sentence Detector annotator, processes various sentences per line
val sentenceDetector = new SentenceDetector()\
    .setInputCols(Array("document"))\
    .setOutputCol("sentence")

// Tokenizer splits words in a relevant format for NLP
val tokenizer = new Tokenizer()\
    .setInputCols(Array("sentence"))\
    .setOutputCol("token")

// Clinical word embeddings trained on PubMED dataset
val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(Array("sentence", "token")) \
    .setOutputCol("embeddings")

// NER model trained on n2c2 (de-identification and Heart Disease Risk Factors Challenge) datasets)
val clinical_ner = NerModel.pretrained("ner_deid_generic_augmented", "en", "clinical/models") \
    .setInputCols(Array("sentence", "token", "embeddings")) \
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()\
    .setInputCols(Array("sentence", "token", "ner"))\
    .setOutputCol("ner_chunk")

//deid model with "entity_labels"
val deid_entity_labels= new DeIdentification()
    .setInputCols(Array("ner_chunk", "token", "sentence")) \
    .setOutputCol("deid_entity_label")\
    .setMode("mask")\
    .setReturnEntityMappings(true)\
    .setMaskingPolicy("entity_labels")

import java.io.PrintWriter

val obs_lines = """Marvin MARSHALL#PATIENT
Hubert GROGAN#PATIENT
ALTHEA COLBURN#PATIENT
Kalil AMIN#PATIENT
Inci FOUNTAIN#PATIENT
Ekaterina Rosa#DOCTOR
Rudiger Chao#DOCTOR
COLLETTE KOHLER#NAME
Mufi HIGGS#NAME"""

val filename = "obfuscation.txt"
val writer = new PrintWriter(filename)
writer.write(obs_lines)
writer.close()

val obfuscation =  new DeIdentification()
    .setInputCols(Array("ner_chunk", "token", "sentence")) \
    .setOutputCol("deidentified") \
    .setMode("obfuscate")\
    .setObfuscateDate(true)\
    .setObfuscateRefFile('obfuscation.txt')\
    .setObfuscateRefSource("both")\        //file or faker  
    .setGenderAwareness(true)\
    .setLanguage("en")\
    .setUnnormalizedDateMode("obfuscate") //mask or skip



val deidPipeline = new Pipeline().setStages(Array(
                                                  documentAssembler,
                                                  sentenceDetector,
                                                  tokenizer,
                                                  word_embeddings,
                                                  clinical_ner,
                                                  ner_converter,
                                                  deid_entity_labels,
                                                  obfuscation
                                                ))




//sample data

val text =
          '''
          Record date : 2093-01-13 , David Hale , M.D . , Name : Hendrickson Ora , MR # 7194334 Date : 01/13/93 . PCP : Oliveira , 25 years-old , Record date : 2079-11-09 . Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 .
          '''

val data = Seq(text).toDF("text")

val result = new deidPipeline.fit(data).transform(data)

|index|sentence|deid\_entity\_label|deidentified|
|---|---|---|---|
|0|Record date : 2093-01-13 , David Hale , M\.D \.|Record date : \<DATE\> , \<NAME\> , M\.D \.|Record date : 2093-02-13 , Wolf Hermes , M\.D \.|
|1|, Name : Hendrickson Ora , MR \# 7194334 Date : 01/13/93 \.|, Name : \<NAME\> , MR \# \<ID\> Date : \<DATE\> \.|, Name : Engel Rainier , MR \# 5822805 Date : 02/13/93 \.|
|2|PCP : Oliveira , 25 years-old , Record date : 2079-11-09 \.|PCP : \<NAME\> , \<AGE\> years-old , Record date : \<DATE\> \.|PCP : Damián Lango , 21 years-old , Record date : 2079-12-10 \.|
|3|Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 \.|\<LOCATION\> , \<LOCATION\> , Phone \<CONTACT\> \.|103 North Street , 2500 Bellevue Medical Center Dr , Phone 051-096-883 \.|

{%- endcapture -%}

{%- capture approach_scala_legal -%}
  
val documentAssembler = new nlp.DocumentAssembler()
     .setInputCol("text")
     .setOutputCol("document")

 val sentenceDetector = new nlp.SentenceDetector()
     .setInputCols(Array("document"))
     .setOutputCol("sentence")
     .setUseAbbreviations(true)

 val tokenizer = new nlp.Tokenizer()
     .setInputCols(Array("sentence"))
     .setOutputCol("token")

 val embeddings = nlp.WordEmbeddingsModel
     .pretrained("embeddings_clinical", "en", "clinical/models")
     .setInputCols(Array("sentence", "token"))
     .setOutputCol("embeddings")

// Ner entities
val ner_model = legal.NerModel.pretrained("legner_orgs_prods_alias", "en", "legal/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

 val nerConverter = new nlp.NerConverter()
     .setInputCols(Array("sentence", "token", "ner"))
     .setOutputCol("ner_con")

// Deidentification
val deIdentification = new legal.DeIdentification()
     .setInputCols(Array("ner_chunk", "token", "sentence"))
     .setOutputCol("dei")
     // file with custom regex patterns for custom entities
     .setRegexPatternsDictionary("path/to/dic_regex_patterns_main_categories.txt")
     // file with custom obfuscator names for the entities
     .setObfuscateRefFile("path/to/obfuscate_fixed_entities.txt")
     .setRefFileFormat("csv")
     .setRefSep("#")
     .setMode("obfuscate")
     .setDateFormats(Array("MM/dd/yy","yyyy-MM-dd"))
     .setObfuscateDate(true)
     .setDateTag("DATE")
     .setDays(5)
     .setObfuscateRefSource("file")

// Pipeline

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  embeddings,
  ner_model,
  nerConverter,
  deIdentification
))


{%- endcapture -%}

{%- capture approach_scala_finance -%}
from johnsnowlabs import * 
val documentAssembler = new nlp.DocumentAssembler()
     .setInputCol("text")
     .setOutputCol("document")

 val sentenceDetector = new nlp.SentenceDetector()
     .setInputCols(Array("document"))
     .setOutputCol("sentence")
     .setUseAbbreviations(true)

 val tokenizer = new nlp.Tokenizer()
     .setInputCols(Array("sentence"))
     .setOutputCol("token")

 val embeddings = nlp.WordEmbeddingsModel
     .pretrained("embeddings_clinical", "en", "clinical/models")
     .setInputCols(Array("sentence", "token"))
     .setOutputCol("embeddings")

// Ner entities
val ner_model = finance.NerModel.pretrained("finner_orgs_prods_alias","en","finance/models")
     .setInputCols(Array("sentence", "token", "embeddings"))
     .setOutputCol("ner")

 val nerConverter = new nlp.NerConverter()
     .setInputCols(Array("sentence", "token", "ner"))
     .setOutputCol("ner_con")

// Deidentification
val deIdentification = new finance.DeIdentification()
     .setInputCols(Array("ner_chunk", "token", "sentence"))
     .setOutputCol("dei")
     // file with custom regex patterns for custom entities
     .setRegexPatternsDictionary("path/to/dic_regex_patterns_main_categories.txt")
     // file with custom obfuscator names for the entities
     .setObfuscateRefFile("path/to/obfuscate_fixed_entities.txt")
     .setRefFileFormat("csv")
     .setRefSep("#")
     .setMode("obfuscate")
     .setDateFormats(Array("MM/dd/yy","yyyy-MM-dd"))
     .setObfuscateDate(true)
     .setDateTag("DATE")
     .setDays(5)
     .setObfuscateRefSource("file")

// Pipeline

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  embeddings,
  ner_model,
  nerConverter,
  deIdentification
))
{%- endcapture -%}

{%- capture approach_api_link -%}
[DeIdentification](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/deid/DeIdentification.html)
{%- endcapture -%}

{%- capture approach_python_api_link -%}
[DeIdentification](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/deid/deIdentification/index.html#sparknlp_jsl.annotator.deid.deIdentification.DeIdentification)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
approach=approach
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_api_link=model_api_link
model_python_api_link=model_python_api_link
model_python_medical=model_python_medical
model_python_finance=model_python_finance
model_python_legal=model_python_legal
model_scala_medical=model_scala_medical
model_scala_finance=model_scala_finance
model_scala_legal=model_scala_legal
approach_description=approach_description
approach_input_anno=approach_input_anno
approach_output_anno=approach_output_anno
approach_python_medical=approach_python_medical
approach_python_legal=approach_python_legal
approach_python_finance=approach_python_finance
approach_scala_medical=approach_scala_medical
approach_scala_legal=approach_scala_legal
approach_scala_finance=approach_scala_finance
approach_api_link=approach_api_link
approach_python_api_link=approach_python_api_link
%}
