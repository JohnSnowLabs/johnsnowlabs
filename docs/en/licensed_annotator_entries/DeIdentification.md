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
import pandas as pd
from pyspark.sql import SparkSession
from sparknlp.annotator import *
from sparknlp_jsl.annotator import *
from sparknlp.base import *
import sparknlp_jsl
import sparknlp
import pandas as pd
from array import array
spark = nlp.start()

# ==============pipeline ==============

documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_deid_generic_augmented", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

***deid model with "entity_labels"***

deid_entity_labels= DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"])\
    .setOutputCol("deid_entity_label")\
    .setMode("mask")\
    .setReturnEntityMappings(True)\
    .setMaskingPolicy("entity_labels")

***#deid model with "same_length_chars"***

deid_same_length= DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"])\
    .setOutputCol("deid_same_length")\
    .setMode("mask")\
    .setReturnEntityMappings(True)\
    .setMaskingPolicy("same_length_chars")

***#deid model with "fixed_length_chars"***

deid_fixed_length= DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"])\
    .setOutputCol("deid_fixed_length")\
    .setMode("mask")\
    .setReturnEntityMappings(True)\
    .setMaskingPolicy("fixed_length_chars")\
    .setFixedMaskLength(4)


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

obfuscation = DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"]) \
    .setOutputCol("deidentified") \
    .setMode("obfuscate")\
    .setObfuscateDate(True)\
    .setObfuscateRefFile('obfuscation.txt')\
    .setObfuscateRefSource("file")



faker = DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"]) \
    .setOutputCol("deidentified_by_faker") \
    .setMode("obfuscate")\
    .setObfuscateDate(True)\
    .setObfuscateRefSource("faker")


deidPipeline = Pipeline(stages=[
      documentAssembler,
      sentenceDetector,
      tokenizer,
      word_embeddings,
      clinical_ner,
      ner_converter,
      deid_entity_labels,
      deid_same_length,
      deid_fixed_length,
      obfuscation,
      faker])


empty_data = spark.createDataFrame([[""]]).toDF("text")


model = deidPipeline.fit(empty_data)

#sample data
text ='''
Record date : 2093-01-13 , David Hale , M.D . , Name : Hendrickson Ora , MR # 7194334 Date : 01/13/93 . PCP : Oliveira , 25 years-old , Record date : 2079-11-09 . Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 .
'''

result = model.transform(spark.createDataFrame([[text]]).toDF("text"))

result.select(F.explode(F.arrays_zip(result.sentence.result,
                                a     result.deid_entity_label.result,
                                     result.deid_same_length.result,
                                     result.deid_fixed_length.result,
                                     result.deidentified.result,
                                     result.deidentified_by_faker.result,
                                     )).alias("cols")) \
      .select(F.expr("cols['0']").alias("sentence"), 
              F.expr("cols['1']").alias("deid_entity_label"),
              F.expr("cols['2']").alias("deid_same_length"),
              F.expr("cols['3']").alias("deid_fixed_length"),
              F.expr("cols['4']").alias("deidentified"),
              F.expr("cols['5']").alias("deidentified_by_faker"),
              ).toPandas()


|index|sentence|deid\_entity\_label|deid\_same\_length|deid\_fixed\_length|deidentified|deidentified\_by\_faker|
|---|---|---|---|---|---|---|
|0|Record date : 2093-01-13 , David Hale , M\.D \.|Record date : \<DATE\> , \<NAME\> , M\.D \.|Record date : \[\*\*\*\*\*\*\*\*\] , \[\*\*\*\*\*\*\*\*\] , M\.D \.|Record date : \*\*\*\* , \*\*\*\* , M\.D \.|Record date : 2093-01-21 , COLLETTE KOHLER , M\.D \.|Record date : 2093-01-18 , Jacelyn Grip , M\.D \.|
|1|, Name : Hendrickson Ora , MR \# 7194334 Date : 01/13/93 \.|, Name : \<NAME\> , MR \# \<ID\> Date : \<DATE\> \.|, Name : \[\*\*\*\*\*\*\*\*\*\*\*\*\*\] , MR \# \[\*\*\*\*\*\] Date : \[\*\*\*\*\*\*\] \.|, Name : \*\*\*\* , MR \# \*\*\*\* Date : \*\*\*\* \.|, Name : Mufi HIGGS , MR \# 8296535 Date : 01/21/93 \.|, Name : Gillian Shields , MR \# 0327020 Date : 01/18/93 \.|
|2|PCP : Oliveira , 25 years-old , Record date : 2079-11-09 \.|PCP : \<NAME\> , \<AGE\> years-old , Record date : \<DATE\> \.|PCP : \[\*\*\*\*\*\*\] , \*\* years-old , Record date : \[\*\*\*\*\*\*\*\*\] \.|PCP : \*\*\*\* , \*\*\*\* years-old , Record date : \*\*\*\* \.|PCP : COLLETTE KOHLER , \<AGE\> years-old , Record date : 2079-11-17 \.|PCP : Wynona Neat , 23 years-old , Record date : 2079-11-14 \.|
|3|Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 \.|\<LOCATION\> , \<LOCATION\> , Phone \<CONTACT\> \.|\[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\] , \[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\] , Phone \[\*\*\*\*\*\*\*\*\*\] \.|\*\*\*\* , \*\*\*\* , Phone \*\*\*\* \.|\<LOCATION\> , \<LOCATION\> , Phone \<CONTACT\> \.|1065 East Broad Street , 410 West 16Th Avenue , Phone 564 472 379 \.|

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

chunk_merge =  finance.ChunkMergeApproach()\
    .setInputCols("ner_finner_chunk", "ner_chunk")\
    .setOutputCol("deid_merged_chunk")

deidentification =  finance.DeIdentification() \
    .setInputCols(["sentence", "token", "deid_merged_chunk"]) \
    .setOutputCol("deidentified") \
    .setMode("mask")\
    .setIgnoreRegex(True)

# Pipeline
data = spark.createDataFrame([
    ["Jeffrey Preston Bezos is an American entrepreneur, founder and CEO of Amazon"]
]).toDF("text")

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
      chunk_merge,
      deidentification])

result = nlpPipeline.fit(data).transform(data)

|index|result|result|
|---|---|---|
|0|Jeffrey Preston Bezos is an American entrepreneur, founder and CEO of Amazon|\<PERSON\> is an \<COUNTRY\> entrepreneur, \<ROLE\> and \<ROLE\> of \<PARTY\>|

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

chunk_merge = legal.ChunkMergeApproach()\
    .setInputCols("ner_signer_chunk", "ner_chunk")\
    .setOutputCol("deid_merged_chunk")

deidentification = legal.DeIdentification() \
    .setInputCols(["sentence", "token", "deid_merged_chunk"]) \
    .setOutputCol("deidentified") \
    .setMode("mask")\
    .setIgnoreRegex(True)

# Pipeline
data = spark.createDataFrame([
    ["ENTIRE AGREEMENT.  This Agreement contains the entire understanding of the parties hereto with respect to the transactions and matters contemplated hereby, supersedes all previous Agreements between i-Escrow and 2TheMart concerning the subject matter.

2THEMART.COM, INC.:                         I-ESCROW, INC.:

By:Dominic J. Magliarditi                By:Sanjay Bajaj Name: Dominic J. Magliarditi                Name: Sanjay Bajaj Title: President                            Title: VP Business Development Date: 6/21/99                               Date: 6/11/99 "]
]).toDF("text")

nlpPipeline = Pipeline(stages=[
      documentAssembler, 
      sentenceDetector,
      tokenizer,
      embeddings,
      legal_ner,
      ner_converter,
      ner_signers,
      ner_converter_signers,
      chunk_merge,
      deidentification])

result = nlpPipeline.fit(data).transform(data)

|index|result|result|
|---|---|---|
|0|ENTIRE AGREEMENT\.,This Agreement contains the entire understanding of the parties hereto with respect to the transactions and matters contemplated hereby, supersedes all previous Agreements between i-Escrow and 2TheMart concerning the subject matter\.,THE MART\.COM, INC\.:                         I-ESCROW, INC\.: By:Dominic J\. Magliarditi                 By:Sanjay Bajaj Name: Dominic J\. Magliarditi                Name: Sanjay Bajaj Title: President                            Title: VP Business Development Date: 6/21/99                                 Date: 6/11/99|\<DOC\>\.,This Agreement contains the entire understanding of the parties hereto with respect to the transactions and matters contemplated hereby, supersedes all previous Agreements between i-Escrow and 2TheMart concerning the subject matter\.,\<PARTY\>\.:                         \<PARTY\>\.: By:Dominic \<SIGNING\_PERSON\>                 By:Sanjay \<SIGNING\_PERSON\> Name: \<SIGNING\_PERSON\>                Name: \<SIGNING\_PERSON\> Title: \<SIGNING\_TITLE\>                            Title: \<SIGNING\_TITLE\> Date: 6/21/99                                 Date: 6/11/99|

{%- endcapture -%}

{%- capture model_scala_medical -%}

from johnsnowlabs import * spark = nlp.start()

==============pipeline ==============
val documentAssembler = new DocumentAssembler()
.setInputCol("text")
.setOutputCol("document")

val sentenceDetector = new SentenceDetector()
.setInputCols(Array("document"))
.setOutputCol("sentence")

val tokenizer = new Tokenizer()
.setInputCols(Array("sentence"))
.setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
.setInputCols(Array("sentence", "token"))
.setOutputCol("embeddings")

val clinical_ner = MedicalNerModel.pretrained("ner_deid_generic_augmented", "en", "clinical/models")
.setInputCols(Array("sentence", "token", "embeddings"))
.setOutputCol("ner")

val ner_converter = new NerConverterInternal()
.setInputCols(Array("sentence", "token", "ner"))
.setOutputCol("ner_chunk")

deid model with "entity_labels"

val deid_entity_labels= DeIdentification()
.setInputCols(Array("sentence", "token", "ner_chunk"))
.setOutputCol("deid_entity_label")
.setMode("mask")
.setReturnEntityMappings(True)
.setMaskingPolicy("entity_labels")

#deid model with "same_length_chars"

val deid_same_length= DeIdentification()
.setInputCols(Array("sentence", "token", "ner_chunk"))
.setOutputCol("deid_same_length")
.setMode("mask")
.setReturnEntityMappings(True)
.setMaskingPolicy("same_length_chars")

#deid model with "fixed_length_chars"

val deid_fixed_length= DeIdentification()
.setInputCols(Array("sentence", "token", "ner_chunk"))
.setOutputCol("deid_fixed_length")
.setMode("mask")
.setReturnEntityMappings(True)
.setMaskingPolicy("fixed_length_chars")
.setFixedMaskLength(4)

import java.io.PrintWriter

object Main { def main(args: Array[String]): Unit = { val obsLines = """Marvin MARSHALL#PATIENT Hubert GROGAN#PATIENT ALTHEA COLBURN#PATIENT Kalil AMIN#PATIENT Inci FOUNTAIN#PATIENT Ekaterina Rosa#DOCTOR Rudiger Chao#DOCTOR COLLETTE KOHLER#NAME Mufi HIGGS#NAME"""

val filename = "obfuscation.txt"
val writer = new PrintWriter(filename)
writer.write(obsLines)
writer.close()
} }

val obfuscation = new DeIdentification()
.setInputCols(Array("sentence", "token", "ner_chunk"))
.setOutputCol("deidentified")
.setMode("obfuscate")
.setObfuscateDate(True)
.setObfuscateRefFile('obfuscation.txt')
.setObfuscateRefSource("file")

fval aker = new DeIdentification()
.setInputCols(Array("sentence", "token", "ner_chunk"))
.setOutputCol("deidentified_by_faker")
.setMode("obfuscate")
.setObfuscateDate(True)
.setObfuscateRefSource("faker")

val deidPipeline = new Pipeline(stages=Array(documentAssembler, sentenceDetector, tokenizer, word_embeddings, clinical_ner, ner_converter, deid_entity_labels, deid_same_length, deid_fixed_length, obfuscation, faker))

empty_data = spark.createDataFrame([[""]]).toDF("text")

#sample data

val data = Seq( "Record date : 2093-01-13 , David Hale , M.D . , Name : Hendrickson Ora , MR # 7194334 Date : 01/13/93 . PCP : Oliveira , 25 years-old , Record date : 2079-11-09 . Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 ." ).toDF("text")

val model = new deidPipeline.fit(data)

val result = new model.transform(data).toDF("text"))

result.select(F.explode(F.arrays_zip(result.sentence.result, a result.deid_entity_label.result, result.deid_same_length.result, result.deid_fixed_length.result, result.deidentified.result, result.deidentified_by_faker.result, )).alias("cols"))
.select(F.expr("cols['0']").alias("sentence"), F.expr("cols['1']").alias("deid_entity_label"), F.expr("cols['2']").alias("deid_same_length"), F.expr("cols['3']").alias("deid_fixed_length"), F.expr("cols['4']").alias("deidentified"), F.expr("cols['5']").alias("deidentified_by_faker"), ).toPandas()

index	sentence	deid_entity_label	deid_same_length	deid_fixed_length	deidentified	deidentified_by_faker
0	Record date : 2093-01-13 , David Hale , M.D .	Record date : <DATE> , <NAME> , M.D .	Record date : [********] , [********] , M.D .	Record date : **** , **** , M.D .	Record date : 2093-01-21 , COLLETTE KOHLER , M.D .	Record date : 2093-01-18 , Jacelyn Grip , M.D .
1	, Name : Hendrickson Ora , MR # 7194334 Date : 01/13/93 .	, Name : <NAME> , MR # <ID> Date : <DATE> .	, Name : [*************] , MR # [*****] Date : [******] .	, Name : **** , MR # **** Date : **** .	, Name : Mufi HIGGS , MR # 8296535 Date : 01/21/93 .	, Name : Gillian Shields , MR # 0327020 Date : 01/18/93 .
2	PCP : Oliveira , 25 years-old , Record date : 2079-11-09 .	PCP : <NAME> , <AGE> years-old , Record date : <DATE> .	PCP : [******] , ** years-old , Record date : [********] .	PCP : **** , **** years-old , Record date : **** .	PCP : COLLETTE KOHLER , <AGE> years-old , Record date : 2079-11-17 .	PCP : Wynona Neat , 23 years-old , Record date : 2079-11-14 .
3	Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 .	<LOCATION> , <LOCATION> , Phone <CONTACT> .	[***************************] , [***************] , Phone [*********] .	**** , **** , Phone **** .	<LOCATION> , <LOCATION> , Phone <CONTACT> .	1065 East Broad Street , 410 West 16Th Avenue , Phone 564 472 379 .
{%- endcapture -%}

{%- capture model_scala_finance -%}
from johnsnowlabs import * 
val documentAssembler = new nlp.DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new nlp.SentenceDetector()
    .setInputCols(["document"])
    .setOutputCol("sentence")

val tokenizer = new nlp.Tokenizer()
    .setInputCols(["sentence"])
    .setOutputCol("token")

val embeddings = nlp.RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base","en")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val bert_embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("bert_embeddings")

val fin_ner = finance.NerModel.pretrained('finner_deid', "en", "finance/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner") 
    #.setLabelCasing("upper")

val ner_converter =  finance.NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setReplaceLabels({"ORG": "PARTY"}) # Replace "ORG" entity as "PARTY"

val ner_finner = finance.NerModel.pretrained("finner_org_per_role_date", "en", "finance/models")
    .setInputCols(Array("sentence", "token", "bert_embeddings"))
    .setOutputCol("ner_finner") 
    #.setLabelCasing("upper")

val ner_converter_finner = new nlp.NerConverter()
    .setInputCols(Array("sentence", "token", "ner_finner"))
    .setOutputCol("ner_finner_chunk")
    .setWhiteList(['ROLE']) # Just use "ROLE" entity from this NER

val chunk_merge =  new finance.ChunkMergeApproach()
    .setInputCols(Array("ner_finner_chunk", "ner_chunk"))
    .setOutputCol("deid_merged_chunk")

val deidentification =  new finance.DeIdentification()
    .setInputCols(Array("sentence", "token", "deid_merged_chunk"))
    .setOutputCol("deidentified")
    .setMode("mask")
    .setIgnoreRegex(True)

# Pipeline
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
{%- endcapture -%}

{%- capture model_scala_legal -%}
from johnsnowlabs import * 
val documentAssembler = new nlp.DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new nlp.SentenceDetector()
    .setInputCols(["document"])
    .setOutputCol("sentence")

val tokenizer = new nlp.Tokenizer()
    .setInputCols(["sentence"])
    .setOutputCol("token")

val embeddings = nlp.RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base","en")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val legal_ner = legal.NerModel.pretrained("legner_contract_doc_parties", "en", "legal/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner") 
    #.setLabelCasing("upper")

val ner_converter = new legal.NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")\
    .setReplaceLabels({"ALIAS": "PARTY"})

val ner_signers = legal.NerModel.pretrained("legner_signers", "en", "legal/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner_signers") 
    #.setLabelCasing("upper")

val ner_converter_signers = new nlp.NerConverter()
    .setInputCols(Array("sentence", "token", "ner_signers"))
    .setOutputCol("ner_signer_chunk")

val chunk_merge = new legal.ChunkMergeApproach()
    .setInputCols(Array("ner_signer_chunk", "ner_chunk"))
    .setOutputCol("deid_merged_chunk")

val deidentification = new legal.DeIdentification()
    .setInputCols(Array("sentence", "token", "deid_merged_chunk"))
    .setOutputCol("deidentified") \
    .setMode("mask")\
    .setIgnoreRegex(True)

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
import pandas as pd
from pyspark.sql import SparkSession
from sparknlp.annotator import *
from sparknlp_jsl.annotator import *
from sparknlp.base import *
import sparknlp_jsl
import sparknlp
import pandas as pd
from array import array
spark = nlp.start()

# ==============pipeline ==============

documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_deid_generic_augmented", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

***deid model with "entity_labels"***

deid_entity_labels= DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"])\
    .setOutputCol("deid_entity_label")\
    .setMode("mask")\
    .setReturnEntityMappings(True)\
    .setMaskingPolicy("entity_labels")

***#deid model with "same_length_chars"***

deid_same_length= DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"])\
    .setOutputCol("deid_same_length")\
    .setMode("mask")\
    .setReturnEntityMappings(True)\
    .setMaskingPolicy("same_length_chars")

***#deid model with "fixed_length_chars"***

deid_fixed_length= DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"])\
    .setOutputCol("deid_fixed_length")\
    .setMode("mask")\
    .setReturnEntityMappings(True)\
    .setMaskingPolicy("fixed_length_chars")\
    .setFixedMaskLength(4)


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

obfuscation = DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"]) \
    .setOutputCol("deidentified") \
    .setMode("obfuscate")\
    .setObfuscateDate(True)\
    .setObfuscateRefFile('obfuscation.txt')\
    .setObfuscateRefSource("file")



faker = DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"]) \
    .setOutputCol("deidentified_by_faker") \
    .setMode("obfuscate")\
    .setObfuscateDate(True)\
    .setObfuscateRefSource("faker")


deidPipeline = Pipeline(stages=[
      documentAssembler,
      sentenceDetector,
      tokenizer,
      word_embeddings,
      clinical_ner,
      ner_converter,
      deid_entity_labels,
      deid_same_length,
      deid_fixed_length,
      obfuscation,
      faker])


empty_data = spark.createDataFrame([[""]]).toDF("text")


model = deidPipeline.fit(empty_data)

#sample data
text ='''
Record date : 2093-01-13 , David Hale , M.D . , Name : Hendrickson Ora , MR # 7194334 Date : 01/13/93 . PCP : Oliveira , 25 years-old , Record date : 2079-11-09 . Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 .
'''

result = model.transform(spark.createDataFrame([[text]]).toDF("text"))

result.select(F.explode(F.arrays_zip(result.sentence.result,
                                a     result.deid_entity_label.result,
                                     result.deid_same_length.result,
                                     result.deid_fixed_length.result,
                                     result.deidentified.result,
                                     result.deidentified_by_faker.result,
                                     )).alias("cols")) \
      .select(F.expr("cols['0']").alias("sentence"), 
              F.expr("cols['1']").alias("deid_entity_label"),
              F.expr("cols['2']").alias("deid_same_length"),
              F.expr("cols['3']").alias("deid_fixed_length"),
              F.expr("cols['4']").alias("deidentified"),
              F.expr("cols['5']").alias("deidentified_by_faker"),
              ).toPandas()


|index|sentence|deid\_entity\_label|deid\_same\_length|deid\_fixed\_length|deidentified|deidentified\_by\_faker|
|---|---|---|---|---|---|---|
|0|Record date : 2093-01-13 , David Hale , M\.D \.|Record date : \<DATE\> , \<NAME\> , M\.D \.|Record date : \[\*\*\*\*\*\*\*\*\] , \[\*\*\*\*\*\*\*\*\] , M\.D \.|Record date : \*\*\*\* , \*\*\*\* , M\.D \.|Record date : 2093-01-21 , COLLETTE KOHLER , M\.D \.|Record date : 2093-01-18 , Jacelyn Grip , M\.D \.|
|1|, Name : Hendrickson Ora , MR \# 7194334 Date : 01/13/93 \.|, Name : \<NAME\> , MR \# \<ID\> Date : \<DATE\> \.|, Name : \[\*\*\*\*\*\*\*\*\*\*\*\*\*\] , MR \# \[\*\*\*\*\*\] Date : \[\*\*\*\*\*\*\] \.|, Name : \*\*\*\* , MR \# \*\*\*\* Date : \*\*\*\* \.|, Name : Mufi HIGGS , MR \# 8296535 Date : 01/21/93 \.|, Name : Gillian Shields , MR \# 0327020 Date : 01/18/93 \.|
|2|PCP : Oliveira , 25 years-old , Record date : 2079-11-09 \.|PCP : \<NAME\> , \<AGE\> years-old , Record date : \<DATE\> \.|PCP : \[\*\*\*\*\*\*\] , \*\* years-old , Record date : \[\*\*\*\*\*\*\*\*\] \.|PCP : \*\*\*\* , \*\*\*\* years-old , Record date : \*\*\*\* \.|PCP : COLLETTE KOHLER , \<AGE\> years-old , Record date : 2079-11-17 \.|PCP : Wynona Neat , 23 years-old , Record date : 2079-11-14 \.|
|3|Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 \.|\<LOCATION\> , \<LOCATION\> , Phone \<CONTACT\> \.|\[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\] , \[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\] , Phone \[\*\*\*\*\*\*\*\*\*\] \.|\*\*\*\* , \*\*\*\* , Phone \*\*\*\* \.|\<LOCATION\> , \<LOCATION\> , Phone \<CONTACT\> \.|1065 East Broad Street , 410 West 16Th Avenue , Phone 564 472 379 \.|
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
from johnsnowlabs import *
spark = nlp.start()

# ==============pipeline ==============

val documentAssembler = new DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

val clinical_ner = MedicalNerModel.pretrained("ner_deid_generic_augmented", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

***deid model with "entity_labels"***

val deid_entity_labels= DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"])\
    .setOutputCol("deid_entity_label")\
    .setMode("mask")\
    .setReturnEntityMappings(True)\
    .setMaskingPolicy("entity_labels")

***#deid model with "same_length_chars"***

val deid_same_length= DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"])\
    .setOutputCol("deid_same_length")\
    .setMode("mask")\
    .setReturnEntityMappings(True)\
    .setMaskingPolicy("same_length_chars")

***#deid model with "fixed_length_chars"***

val deid_fixed_length= DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"])\
    .setOutputCol("deid_fixed_length")\
    .setMode("mask")\
    .setReturnEntityMappings(True)\
    .setMaskingPolicy("fixed_length_chars")\
    .setFixedMaskLength(4)


import java.io.PrintWriter

object Main {
  def main(args: Array[String]): Unit = {
    val obsLines = """Marvin MARSHALL#PATIENT
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
    writer.write(obsLines)
    writer.close()
  }
}


val obfuscation = new DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"]) \
    .setOutputCol("deidentified") \
    .setMode("obfuscate")\
    .setObfuscateDate(True)\
    .setObfuscateRefFile('obfuscation.txt')\
    .setObfuscateRefSource("file")



fval aker = new DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"]) \
    .setOutputCol("deidentified_by_faker") \
    .setMode("obfuscate")\
    .setObfuscateDate(True)\
    .setObfuscateRefSource("faker")


val deidPipeline = new Pipeline(stages=[
      documentAssembler,
      sentenceDetector,
      tokenizer,
      word_embeddings,
      clinical_ner,
      ner_converter,
      deid_entity_labels,
      deid_same_length,
      deid_fixed_length,
      obfuscation,
      faker])


empty_data = spark.createDataFrame([[""]]).toDF("text")



#sample data

val data = Seq(
  "Record date : 2093-01-13 , David Hale , M.D . , Name : Hendrickson Ora , MR # 7194334 Date : 01/13/93 . PCP : Oliveira , 25 years-old , Record date : 2079-11-09 . Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 ."
).toDF("text")

val model = new deidPipeline.fit(data)

val result = new model.transform(data).toDF("text"))

result.select(F.explode(F.arrays_zip(result.sentence.result,
                                a     result.deid_entity_label.result,
                                     result.deid_same_length.result,
                                     result.deid_fixed_length.result,
                                     result.deidentified.result,
                                     result.deidentified_by_faker.result,
                                     )).alias("cols")) \
      .select(F.expr("cols['0']").alias("sentence"), 
              F.expr("cols['1']").alias("deid_entity_label"),
              F.expr("cols['2']").alias("deid_same_length"),
              F.expr("cols['3']").alias("deid_fixed_length"),
              F.expr("cols['4']").alias("deidentified"),
              F.expr("cols['5']").alias("deidentified_by_faker"),
              ).toPandas()


|index|sentence|deid\_entity\_label|deid\_same\_length|deid\_fixed\_length|deidentified|deidentified\_by\_faker|
|---|---|---|---|---|---|---|
|0|Record date : 2093-01-13 , David Hale , M\.D \.|Record date : \<DATE\> , \<NAME\> , M\.D \.|Record date : \[\*\*\*\*\*\*\*\*\] , \[\*\*\*\*\*\*\*\*\] , M\.D \.|Record date : \*\*\*\* , \*\*\*\* , M\.D \.|Record date : 2093-01-21 , COLLETTE KOHLER , M\.D \.|Record date : 2093-01-18 , Jacelyn Grip , M\.D \.|
|1|, Name : Hendrickson Ora , MR \# 7194334 Date : 01/13/93 \.|, Name : \<NAME\> , MR \# \<ID\> Date : \<DATE\> \.|, Name : \[\*\*\*\*\*\*\*\*\*\*\*\*\*\] , MR \# \[\*\*\*\*\*\] Date : \[\*\*\*\*\*\*\] \.|, Name : \*\*\*\* , MR \# \*\*\*\* Date : \*\*\*\* \.|, Name : Mufi HIGGS , MR \# 8296535 Date : 01/21/93 \.|, Name : Gillian Shields , MR \# 0327020 Date : 01/18/93 \.|
|2|PCP : Oliveira , 25 years-old , Record date : 2079-11-09 \.|PCP : \<NAME\> , \<AGE\> years-old , Record date : \<DATE\> \.|PCP : \[\*\*\*\*\*\*\] , \*\* years-old , Record date : \[\*\*\*\*\*\*\*\*\] \.|PCP : \*\*\*\* , \*\*\*\* years-old , Record date : \*\*\*\* \.|PCP : COLLETTE KOHLER , \<AGE\> years-old , Record date : 2079-11-17 \.|PCP : Wynona Neat , 23 years-old , Record date : 2079-11-14 \.|
|3|Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 \.|\<LOCATION\> , \<LOCATION\> , Phone \<CONTACT\> \.|\[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\] , \[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\] , Phone \[\*\*\*\*\*\*\*\*\*\] \.|\*\*\*\* , \*\*\*\* , Phone \*\*\*\* \.|\<LOCATION\> , \<LOCATION\> , Phone \<CONTACT\> \.|1065 East Broad Street , 410 West 16Th Avenue , Phone 564 472 379 \.|

{%- endcapture -%}

{%- capture approach_scala_legal -%}
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
