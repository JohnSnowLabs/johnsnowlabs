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

- `mode` *(str)*: Mode for Anonimizer ['mask','obfuscate']

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
entity_labels: Mask with the entity type of that chunk. (default)
same_length_chars: Mask the deid entities with same length of asterix ( * ) with brackets ( [ , ] ) on both end.
fixed_length_chars: Mask the deid entities with a fixed length of asterix ( * ). The length is setting up using the setFixedMaskLength() method.
same_length_chars_without_brackets: masks entities with asterisks of the same length without square brackets.
entity_labels_without_brackets: replaces entities with their label without square brackets.

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

- `keepYear`: (BooleanParam) Whether to keep the year intact when obfuscating date entities.
  If True, the year will remain unchanged during the obfuscation process.
  If False, the year will be modified along with the month and day.
  Default: False.

- `keepMonth` : Whether to keep the month intact when obfuscating date entities.
  If True, the month will remain unchanged during the obfuscation process.
  If False, the month will be modified along with the year and day.
  Default: False.

- `consistentAcrossNameParts` : Param that indicates whether consistency should be enforced across different parts of a name
  (e.g., first name, middle name, last name).

When set to `True`, the same transformation or obfuscation will be applied consistently to all parts
of the same name entity, even if those parts appear separately.

For example, if "John Smith" is obfuscated as "Liam Brown", then:
- When the full name "John Smith" appears, it will be replaced with "Liam Brown"
- When "John" or "Smith" appear individually, they will still be obfuscated as "Liam" and "Brown" respectively,
  ensuring consistency in name transformation.

Default: True

- `geoConsistency`: (BooleanParam) Sets whether to enforce consistent obfuscation across geographical entities:
state, city, street, zip and phone.
This parameter enables intelligent geographical entity obfuscation that maintains
realistic relationships between different geographic components.
When enabled, the system ensures that obfuscated addresses form coherent, valid combinations
rather than random replacements. Default: False

- `countryObfuscation`: (BooleanParam) Whether to obfuscate country entities or not. If True, the country entities will be obfuscated. Default: False.

- `additionalDateFormats`: (Param[String]) Additional date formats to be considered during date obfuscation.
  This allows users to specify custom date formats in addition to the default date formats. Default: [].

- `selectiveObfuscateRefSource`: Dict[str, str]
  A dictionary of entity names to their obfuscation modes.
  This is used to selectively apply different obfuscation methods to specific entities.
  The keys are entity names and the values are the obfuscation sources.
  If an entity is not specified in this map, the `obfuscateRefSource` param is used to determine the obfuscation source.
  Possible values in dict for the obfuscation source are: 'custom', 'faker', 'both', 'file'.

- `staticObfuscationPairs`: static obfuscation pairs is used to set static obfuscation pairs that will be used for de-identification.
  Each pair should contain three elements: original, entity type, and fake.
  The pairs must have exactly 3 elements: [original, entityType, fake].

- `obfuscationEquivalents` : used to define variant-to-canonical mappings to ensure consistent obfuscation.  
  Each pair should contain three elements: variant, entity type, and canonical.  
  The pairs must have exactly 3 elements: `[variant, entityType, canonical]`.

- `enableDefaultObfuscationEquivalents` : whether to enable default obfuscation equivalents for common entities.
  This parameter allows the system to automatically include a set of predefined common English name equivalents.
  Default is False.




{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
DOCUMENT
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
ner_subentity = medical.NerModel.pretrained("ner_deid_subentity_augmented", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner_subentity")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner_subentity"])\
    .setOutputCol("ner_chunk")

light_deidentification = medical.LightDeIdentification() \
    .setInputCols(["ner_chunk", "sentence"]) \
    .setOutputCol("obfuscated") \
    .setMode("obfuscate") \
    .setObfuscateDate(True)\
    .setDateFormats(["MM/dd/yyyy","yyyy-MM-dd", "MM/dd/yy"]) \
    .setDays(7) \
    .setObfuscateRefSource('custom') \
    .setCustomFakers({"Doctor": ["John", "Joe"],
                      "Patient": ["James", "Michael"],
                      "Hospital": ["Medical Center"],
                      "Street" : ["Main Street"],
                      "Age":["1","10", "20", "40","80"],
                      "PHONE":["555-555-0000"]}) \
    .setAgeRanges([1, 4, 12, 20, 40, 60, 80])\
    .setLanguage("en") \
    .setSeed(42) \
    .setDateEntities(["DATE", "DOB",  "DOD"]) \

flattener = medical.Flattener()\
    .setInputCols("obfuscated","sentence")\
    .setExplodeSelectedFields({"obfuscated": ["result"],  "sentence": ["result"]})

nlpPipeline = nlp.Pipeline(stages=[
                documentAssembler,
                sentenceDetector,
                tokenizer,
                word_embeddings,
                ner_subentity,
                ner_converter,
                light_deidentification,
                flattener
                ])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = nlpPipeline.fit(empty_data)

text ='''
    Record date : 2093-01-13 , David Hale , M.D . ,
    Name : Hendrickson Ora , MR # 7194334 Date : 01/13/93 .
    PCP : Oliveira , 95 years-old , Record date : 2079-11-09 .
    Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555.
    '''

result = model.transform(spark.createDataFrame([[text]]).toDF("text"))
result.show(truncate=False)

## Result

+----------------------------------------------------------------------+-----------------------------------------------------+
|sentence_result                                                       |obfuscated_result                                    |
+----------------------------------------------------------------------+-----------------------------------------------------+
|Record date : 2093-01-13 , David Hale , M.D .                         |Record date : 2093-01-20 , John , M.D .              |
|,\nName : Hendrickson Ora , MR # 7194334 Date : 01/13/93 .            |,\nName : Michael , MR # 1478295 Date : 01/20/93 .   |
|PCP : Oliveira , 95 years-old , Record date : 2079-11-09 .            |PCP : Joe , 95 years-old , Record date : 2079-11-16 .|
|Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555.|Medical Center , Main Street , Phone 62-130-8657.    |
+----------------------------------------------------------------------+-----------------------------------------------------+

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

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

val nerSubEntity = MedicalNerModel.pretrained("ner_deid_subentity_augmented", "en", "clinical/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner_subentity")

val nerConverter = new NerConverterInternal()
  .setInputCols(Array("sentence", "token", "ner_subentity"))
  .setOutputCol("ner_chunk")

val lightDeidentification = new LightDeIdentification()
  .setInputCols(Array("ner_chunk", "sentence"))
  .setOutputCol("obfuscated")
  .setMode("obfuscate")
  .setObfuscateDate(true)
  .setDateFormats(Array("MM/dd/yyyy", "yyyy-MM-dd", "MM/dd/yy"))
  .setDays(7)
  .setObfuscateRefSource("custom")
  .setCustomFakers(Map("Doctor" -> Array("John", "Joe"),
    "Patient" -> Array("James", "Michael"),
    "Hospital" -> Array("Medical Center"),
    "Street" -> Array("Main Street"),
    "Age" -> Array("1", "10", "20", "40", "80"),
    "PHONE" -> Array("555-555-0000")))
  .setAgeRanges(Array(1, 4, 12, 20, 40, 60, 80))
  .setLanguage("en")
  .setSeed(42)
  .setDateEntities(Array("DATE", "DOB", "DOD"))

val flattener = new Flattener()
  .setInputCols(Array("obfuscated", "sentence"))
  .setExplodeSelectedFields(Map("obfuscated" -> Array("result"), "sentence" -> Array("result")))

val nlpPipeline = new Pipeline().setStages(Array(
      documentAssembler,
      sentenceDetector,
      tokenizer,
      wordEmbeddings,
      nerSubEntity,
      nerConverter,
      lightDeidentification,
      flattener
))

val emptyData =Seq(("")).toDF("text")

val model = nlpPipeline.fit(emptyData)

// Result

+----------------------------------------------------------------------+-----------------------------------------------------+
|sentence_result                                                       |obfuscated_result                                    |
+----------------------------------------------------------------------+-----------------------------------------------------+
|Record date : 2093-01-13 , David Hale , M.D .                         |Record date : 2093-01-20 , John , M.D .              |
|,\nName : Hendrickson Ora , MR # 7194334 Date : 01/13/93 .            |,\nName : Michael , MR # 1478295 Date : 01/20/93 .   |
|PCP : Oliveira , 95 years-old , Record date : 2079-11-09 .            |PCP : Joe , 95 years-old , Record date : 2079-11-16 .|
|Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555.|Medical Center , Main Street , Phone 62-130-8657.    |
+----------------------------------------------------------------------+-----------------------------------------------------+

{%- endcapture -%}


{%- capture model_api_link -%}
[LightDeIdentification](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/deid/LightDeIdentification.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[LightDeIdentification](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/deid/LightDeIdentification/index.html)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[LightDeIdentification](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.6.Light_Deidentification.ipynb)
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
