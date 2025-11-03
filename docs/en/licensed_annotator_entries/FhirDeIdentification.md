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

- `inputCol`: Name of the input column containing FHIR resources.

- `outputCol`: Name of the output column that will contain de-identified FHIR resources.

- `fhirVersion`: FHIR version to use for de-identification. Options: ['R4', 'R5', 'DSTU3'].

- `parserType`: Parser type for FHIR resources. Options: ['JSON', 'XML'].

- `mode`: De-identification mode. Options: ['mask', 'obfuscate'].

- `mappingRules`: Dictionary mapping FHIR field paths to entity types for de-identification (e.g., `{"Patient.name.given": "FIRST_NAME"}`).

- `dateEntities`: List of date entity labels to de-identify (default: ['DATE', 'DOB', 'DOD']).

- `obfuscateDate`: Whether to obfuscate or mask dates in obfuscation mode (default: False).

- `unnormalizedDateMode`: Behavior for unformatted dates. Options: ['mask', 'obfuscate', 'skip'] (default: 'obfuscate').

- `days`: Number of days to displace date entities for obfuscation.

- `dateFormats`: List of supported date formats for obfuscation.

- `obfuscateRefSource`: Source for obfuscation data. Options: ['custom', 'faker', 'both'].

- `language`: Language for regex and faker entities. Options: ['en', 'de', 'es', 'fr', 'ar', 'ro'] (default: 'en').

- `seed`: Randomization seed for reproducible obfuscation.

- `maskingPolicy`: Masking policy for entity replacement. Options: ['same_length_chars', 'entity_labels', 'fixed_length_chars', 'entity_labels_without_brackets', 'same_length_chars_without_brackets'].

- `fixedMaskLength`: Length of masking when using `fixed_length_chars` policy.

- `sameLengthFormattedEntities`: List of entities to preserve length during obfuscation (e.g., PHONE, ZIP, SSN).

- `genderAwareness`: Use gender-aware name replacement during obfuscation (default: False).

- `ageRanges`: Integer list defining age brackets to preserve.

- `selectiveObfuscationModes`: Dictionary defining custom obfuscation modes for specific entities (e.g., `{'obfuscate': ['PHONE'], 'mask_entity_labels': ['NAME'], 'skip': ['id']}`).

- `customFakers`: Dictionary defining custom fake values for entities (e.g., `{'NAME': ['John', 'Jane'], 'CITY': ['Paris', 'London']}`).

- `keepYear`: Keep year unchanged when obfuscating dates (default: False).

- `keepMonth`: Keep month unchanged when obfuscating dates (default: False).

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
