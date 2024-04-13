{%- capture title -%}
LightDeIdentification
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}

Light DeIdentification is a light version of DeIdentification. It replaces sensitive information
in a text with obfuscated or masked fakers. It is designed to work with healthcare data,
and it can be used to de-identify patient names, dates, and other sensitive information.
It can also be used to obfuscate or mask any other type of sensitive information, such as doctor names, hospital
names, and other types of sensitive information.
Additionally, it supports millions of embedded fakers
and If desired, custom external fakers can be set with setCustomFakers function.
It also supports multiple languages such as English, Spanish, French, German, and Arabic.
And it supports multi-mode de-Identification with setSelectiveObfuscationModes function at the same time.

Parameters:

- `mode` *(str)*: Mode for Anonimizer ['mask'|'obfuscate']

- `dateEntities` *(list[str])*: List of date entities. Default: ['DATE', 'DOB', 'DOD']

- `obfuscateDate` *(Bool)*: When mode=='obfuscate' whether to obfuscate dates or not. This param helps in consistency to make dateFormats more visible.
  When setting to ``True``, make sure dateFormats param fits the needs.
  If the value is True and obfuscation is failed, then unnormalizedDateMode param will be activated.
  When setting to 'False', then the date will be masked to <DATE>.
  Default: False

- `unnormalizedDateMode` *(str)*: The mode to use if the date is not formatted. Options: [mask, obfuscate, skip]. Default: obfuscate.

- `days` (IntParam): Number of days to obfuscate the dates by displacement.If not provided a random integer between 1 and 60 will be used.

- `useShiftDays` *(Bool)*: Whether to use the random shift day when the document has this in its metadata. Default: False

- `dateFormats` (list[str]): List of date formats to automatically displace if parsed.

- `region` *(str)*:  The region to use for date parsing. This property is especially used when obfuscating dates.
  You can decide whether the first part of 11/11/2023 is a day or the second part is a day when obfuscating dates.
  Options: 'eu' for European Union, 'us' for the USA, Default: 'eu'

- `obfuscateRefSource` *(str)*: The source of obfuscation of to obfuscate the entities. For dates entities, This property is invalid.
  The values ar the following:
  custom: Takes the entities from the setCustomFakers function.
  faker: Takes the entities from the Faker module
  both : Takes the entities from the setCustomFakers function and the faker module randomly

- `language` *(str)*:   The language used to select the regex file and some faker entities.
  The values are the following:
  'en'(English), 'de'(German), 'es'(Spanish), 'fr'(French), 'ar'(Arabic) or 'ro'(Romanian). Default:'en'.

- `seed` *(Int)*:  It is the seed to select the entities on obfuscate mode. With the seed,
  you can reply to an execution several times with the same output.

- `maskingPolicy` *(str)*:  Select the masking policy:
  same_length_chars: Replace the obfuscated entity with a masking sequence composed of asterisks and surrounding squared brackets, being the total length of the masking sequence of the same length as the original sequence.
  Example, Smith -> [***].
  If the entity is less than 3 chars (like Jo, or 5), asterisks without brackets will be returned.
  entity_labels: Replace the values with the corresponding entity labels.
  fixed_length_chars: Replace the obfuscated entity with a masking sequence composed of a fixed number of asterisk.

- `fixedMaskLength` *(Int)*:  The length of the masking sequence in case of fixed_length_chars masking policy.

- `sameLengthFormattedEntities` (list[str]):  List of formatted entities to generate the same length outputs as original ones during obfuscation.
  The supported and default formatted entities are: PHONE, FAX, ID, IDNUM, BIOID, MEDICALRECORD, ZIP, VIN, SSN, DLN, LICENSE, PLATE.

- `genderAwareness` *(Bool)*:  Whether to use gender-aware names or not during obfuscation. This param effects only names.
  If the value is true, it might decrease performance. Default: False

- `ageRanges` (list[str]):   list of integer specifying limits of the age groups to preserve during obfuscation.

- `selectiveObfuscationModes` *(dict[str, dict[str]])*:   The dictionary of modes to enable multi-mode deIdentification.
  'obfuscate': Replace the values with random values.
  'mask_same_length_chars': Replace the name with the asterisks with same length minus two plus brackets on both end.
  'mask_entity_labels': Replace the values with the entity value.
  'mask_fixed_length_chars': Replace the name with the asterisks with fixed length. You can also invoke "setFixedMaskLength()"
  'skip': Skip the values (intact)
  The entities which have not been given in dictionary will deidentify according to :param:`mode`

- `customFakers` *(dict[str, dict[str]])*:   The dictionary of custom fakers to specify the obfuscation terms for the entities.
  You can specify the entity and the terms to be used for obfuscation.



{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_python_medical -%}

from johnsnowlabs import nlp, medical

sentences = [
['Record date: 01/01/1980'],
['Johnson, M.D.'],
['Gastby Hospital.'],
['Camel Street.'],
['My name is George.']
]

input_df = spark.createDataFrame(sentences).toDF("text")

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

ner_tagger = nlp.NerDLModel.pretrained("deidentify_dl", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

light_de_identification = medical.LightDeIdentification() \
    .setInputCols(["ner_chunk", "sentence"]) \
    .setOutputCol("dei") \
    .setMode("obfuscate") \
    .setObfuscateDate(True) \
    .setDateFormats(["MM/dd/yyyy"]) \
    .setDays(5) \
    .setObfuscateRefSource('custom') \
    .setCustomFakers({"DOCTOR": ["John"], "HOSPITAL": ["MEDICAL"], "STREET": ["Main Road"]}) \
    .setLanguage("en") \
    .setSeed(10) \
    .setDateEntities(["DATE"]) \

flattener = Flattener()\
    .setInputCols("dei")

pipeline = nlp.Pipeline() \
        .setStages([
        document_assembler,
        sentence_detector,
        tokenizer,
        word_embeddings,
        ner_tagger,
        ner_converter,
        light_de_identification,
        flattener
    ])

pipeline_model = pipeline.fit(input_df)
output = pipeline_model.transform(input_df)
output.show(truncate=False)

## Result

+-----------------------+---------+-------+---------------------+--------------------------+
|dei_result             |dei_begin|dei_end|dei_metadata_sentence|dei_metadata_originalIndex|
+-----------------------+---------+-------+---------------------+--------------------------+
|Record date: 01/06/1980|0        |22     |0                    |0                         |
|John, M.D.             |0        |9      |0                    |0                         |
|MEDICAL.               |0        |7      |0                    |0                         |
|Main Road.             |0        |9      |0                    |0                         |
|My name is <PATIENT>.  |0        |20     |0                    |0                         |
+-----------------------+---------+-------+---------------------+--------------------------+

{%- endcapture -%}

{%- capture model_scala_medical -%}
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

val embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val clinical_sensitive_entities = MedicalNerModel.pretrained("ner_deid_enriched", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val nerConverter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("chunk")

val deIdentification = new LightDeIdentification()
  .setInputCols(Array("chunk", "sentence")).setOutputCol("dei")
  .setMode("obfuscate")
  .setObfuscateDate(true)
  .setDays(5)
  .setObfuscateRefSource("custom")
  .setCustomFakers(Map(
    "DOCTOR" -> Array("John"),
    "HOSPITAL" -> Array("MEDICAL"),
    "STREET" -> Array("Main Road")))
  .setLanguage("en")
  .setSeed(10)
  .setDateEntities(Array("DATE"))


val flattener = new Flattener()
    .setInputCols("dei")

val data = Seq("""
  |Record date: 2093-01-13, David Hale, M.D., Name: Hendrickson Ora.
  | MR # 7194334 Date: 01/13/93. PCP: Oliveira, 25 years-old, Record date: 2079-11-09.
  |Cocke County Baptist Hospital, 0295 Keats Street, Phone 55-555-5555.""".stripMargin
).toDF("text")

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  embeddings,
  clinical_sensitive_entities,
  nerConverter,
  deIdentification,
  flattener
))

val result = pipeline.fit(data).transform(data)
result.show(truncate = false)

// Result

+----------------------------------------------------+---------+-------+---------------------+--------------------------+
|dei_result                                          |dei_begin|dei_end|dei_metadata_sentence|dei_metadata_originalIndex|
+----------------------------------------------------+---------+-------+---------------------+--------------------------+
|Record date: 2093-01-18, John, M.D., Name: John.    |0        |47     |0                    |1                         |
|MR # 4358590 Date: 01/18/93.                        |48       |75     |1                    |68                        |
|PCP: John, <AGE> years-old, Record date: 2079-11-14.|76       |127    |2                    |97                        |
|MEDICAL, Main Road, Phone 91-483-8495.              |128      |165    |3                    |151                       |
+----------------------------------------------------+---------+-------+---------------------+--------------------------+

{%- endcapture -%}


{%- capture model_api_link -%}
[LightDeIdentification](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/deid/LightDeIdentification.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[LightDeIdentification](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/deid/LightDeIdentification/index.html)
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
