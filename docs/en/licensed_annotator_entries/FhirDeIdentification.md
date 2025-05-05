{%- capture title -%}
FhirDeIdentification
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
A Spark Transformer for de-identifying FHIR resources according to configurable privacy rules.

Performs field-level obfuscation on FHIR JSON documents using FHIR Path expressions.
Supports R4, R5, and DSTU3 FHIR versions with type-aware de-identification strategies.
Additionally, supports different parser types (JSON, XML) for FHIR resources.

**Note: FhirDeIdentification Module Availability**  
The `FhirDeIdentification` module is not enabled by default in your current package.  
To use this module, please set `fhir_deid=True` in the `start()` function.  
If you need help or access, feel free to contact us at [support@johnsnowlabs.com](mailto:support@johnsnowlabs.com).

Parameters:

- `fhirVersion`: (Param[String]) The FHIR version to use for de-identification. Options: ['R4', 'R5', 'DSTU3']

- `parserType`: (Param[String]) The parser type to use for de-identification. Options: ['JSON', 'XML']

- `mode`: (Param[String]) Mode for Anonymizer. Options: ['mask', 'obfuscate']

- `dateEntities`: (StringArrayParam) List of date entities. Default: ['DATE', 'DOB', 'DOD']

- `obfuscateDate`: (BooleanParam) When `mode == "obfuscate"`, whether to obfuscate dates or not. If `True` and obfuscation fails, `unnormalizedDateMode` will be used.

- `unnormalizedDateMode`: (Param[String]) The mode to use if the date is not formatted. Options: ['mask', 'obfuscate', 'skip']. Default: 'obfuscate'

- `days`: (IntParam) Number of days to displace dates for obfuscation. If not set, a random value between 1 and 60 will be used.

- `dateFormats`: (StringArrayParam) List of date formats to automatically displace if parsed.

- `obfuscateRefSource`: (Param[String]) The source to use for obfuscating entities (not applicable to date entities). Options: ['custom', 'faker', 'both']

- `language`: (Param[String]) Language for regex and faker data. Options: ['en', 'de', 'es', 'fr', 'ar', 'ro']. Default: 'en'

- `seed`: (IntParam) Seed for deterministic obfuscation results

- `maskingPolicy`: (Param[String]) Select the masking policy. Options: ['same_length_chars', 'entity_labels', 'fixed_length_chars']

- `fixedMaskLength`: (IntParam) Length of masking sequence when using 'fixed_length_chars' masking policy

- `sameLengthFormattedEntities`: (StringArrayParam) List of formatted entities to keep same-length during obfuscation. Supported: PHONE, FAX, ID, IDNUM, BIOID, MEDICALRECORD, ZIP, VIN, SSN, DLN, LICENSE, PLATE

- `genderAwareness`: (BooleanParam) Whether to use gender-aware names during obfuscation. Default: False

- `ageRanges`: (IntArrayParam) List of integers specifying limits of age groups to preserve during obfuscation

- `selectiveObfuscationModes`: (MapParam[String, StringArrayParam]) Dictionary of entity-wise obfuscation modes. Example: {'NAME': ['mask_entity_labels'], 'PHONE': ['obfuscate']}

- `customFakers`: (MapParam[String, StringArrayParam]) Custom dictionary of faker terms to be used for specific entities

- `keepYear`: (BooleanParam) Whether to keep the year intact during date obfuscation. Default: False

- `keepMonth`: (BooleanParam) Whether to keep the month intact during date obfuscation. Default: False


{%- endcapture -%}


{%- capture model_input_anno -%}
TEXT
{%- endcapture -%}

{%- capture model_output_anno -%}
TEXT
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical



rules = {
  "Patient.birthDate" : "DATE",
  "Patient.name.given" : "FIRST_NAME",
  "Patient.name.family" : "LAST_NAME",
  "Patient.telecom.value" : "EMAIL",
  "Patient.gender" : "GENDER"
}

fhir = (
    FhirDeIdentification()
      .setInputCol("text")
      .setOutputCol("deid")
      .setMode("obfuscate")
      .setMappingRules(rules)
      .setFhirVersion("R4")
      .setParserType("JSON")
      .setDays(20)
      .setSeed(88)
      .setCustomFakers(
          {
              "GENDER": ["female", "other"]
          }
      )
      .setObfuscateRefSource("both")
)

john_doe = """{
  "resourceType": "Patient",
  "id": "example",
  "name": [
    {
      "use": "official",
      "family": "Doe",
      "given": [
        "John",
        "Michael"
      ]
    }
  ],
  "telecom": [
    {
      "system": "email",
      "value": "john.doe@example.com"
    },
    {
      "system": "url",
      "value": "http://johndoe.com"
    }
  ],
  "birthDate": "1970-01-01",
  "gender": "male"
}"""



# result

{
    'resourceType': 'Patient',
    'id': 'example',
    'name': [
        {
            'use': 'official',
            'family': 'Cease',
            'given': [
                'Mylene',
                'Anola'
            ]
        }
    ],
    'telecom': [
        {
            'system': 'email',
            'value': 'Bryton@yahoo.com'
        },
        {
            'system': 'url',
            'value': 'https://aurora.com'
        }
    ],
    'birthDate': '1970-01-21',
    'gender': 'other'
}


{%- endcapture -%}


{%- capture model_api_link -%}
[FhirDeIdentification](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/deid/fhir/FhirDeIdentification.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}

[FhirDeIdentification](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/fhir/fhir_deIdentification/index.html)


{%- endcapture -%}

{%- capture model_notebook_link -%}
[FhirDeIdentification](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.10.Fhir_DeIdentification.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_api_link=model_api_link
model_python_api_link=model_python_api_link
model_notebook_link=model_notebook_link
%}
