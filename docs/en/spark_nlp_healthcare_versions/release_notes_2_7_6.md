---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Healthcare NLP v2.7.6 Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/release_notes_2_7_6
key: docs-licensed-release-notes
modify_date: 2021-07-14
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="prev_ver h3-box" markdown="1">

### 2.7.6

We are glad to announce that Spark NLP for Healthcare 2.7.6 has been released!

</div><div class="h3-box" markdown="1">

#### Highlights:

- New pretrained **Radiology Assertion Status** model to assign `Confirmed`, `Suspected`, `Negative` assertion scopes to imaging findings or any clinical tests.

- **Obfuscating** the same sensitive information (patient or doctor name) with the same fake names across the same clinical note.

- Version compatibility checker for the pretrained clinical models and builds to keep up with the latest development efforts in production.

- Adding more English names to faker module in **Deidentification**.

- Updated & improved clinical **SentenceDetectorDL** model.

- New upgrades on `ner_deid_large` and `ner_deid_enriched` NER models to cover more use cases with better resolutions.

- Adding more [examples](https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/scala/healthcare) to workshop repo for _Scala_ users to practice more on healthcare annotators.

- Bug fixes & general improvements.

</div><div class="h3-box" markdown="1">

#### 1. Radiology Assertion Status Model

We trained a new assertion model to assign `Confirmed`, `Suspected`, `Negative` assertion scopes to imaging findings or any clinical tests. It will try to assign these statuses to any named entity you would feed to the assertion annotater in the same pipeline.

     radiology_assertion = AssertionDLModel.pretrained("assertion_dl_radiology", "en", "clinical/models")\
     .setInputCols(["sentence", "ner_chunk", "embeddings"])\
     .setOutputCol("assertion")

`text = Blunting of the left costophrenic angle on the lateral view posteriorly suggests a small left pleural effusion. No right-sided pleural effusion or pneumothorax is definitively seen. There are mildly displaced fractures of the left lateral 8th and likely 9th ribs.`

{:.table-model-big}
|sentences |chunk | ner_label |sent_id|assertion|
|-----------:|:-----:|:---------:|:------:|:------|
|Blunting of the left costophrenic angle on the lateral view posteriorly suggests a small left pleural effusion.|Blunting           |ImagingFindings|0      |Confirmed|
|Blunting of the left costophrenic angle on the lateral view posteriorly suggests a small left pleural effusion.|effusion           |ImagingFindings|0      |Suspected|
|No right-sided pleural effusion or pneumothorax is definitively seen.                                          |effusion           |ImagingFindings|1      |Negative |
|No right-sided pleural effusion or pneumothorax is definitively seen.                                          |pneumothorax       |ImagingFindings|1      |Negative |
|There are mildly displaced fractures of the left lateral 8th and likely 9th ribs.                              |displaced fractures|ImagingFindings|2      |Confirmed|

You can also use this with `AssertionFilterer` to return clinical findings from a note only when it is i.e. `confirmed` or `suspected`.

     assertion_filterer = AssertionFilterer()\
     .setInputCols("sentence","ner_chunk","assertion")\
     .setOutputCol("assertion_filtered")\
     .setWhiteList(["confirmed","suspected"])

     >> ["displaced fractures", "effusion"]

</div><div class="h3-box" markdown="1">

#### 2. **Obfuscating** with the same fake name across the same note:

     obfuscation = DeIdentification()\
      .setInputCols(["sentence", "token", "ner_chunk"]) \
      .setOutputCol("deidentified") \
      .setMode("obfuscate")\
      .setObfuscateDate(True)\
      .setSameEntityThreshold(0.8)\
      .setObfuscateRefSource("faker")


    text =''' Provider: David Hale, M.D.
              Pt: Jessica Parker
              David told  Jessica that she will need to visit the clinic next month.'''


{:.table-model-big}
|    | sentence                                                               | obfuscated                                                          |
|---:|:-----------------------------------------------------------------------|:----------------------------------------------------------------------|
|  0 | Provider: `David Hale`, M.D.                                             | Provider: `Dennis Perez`, M.D.                                          |
|  1 | Pt: `Jessica Parker`                                                     | Pt: `Gerth Bayer`                                                       |
|  2 | `David` told  `Jessica` that she will need to visit the clinic next month. | `Dennis` told  `Gerth` that she will need to visit the clinic next month. |

</div><div class="h3-box" markdown="1">

#### 3. Library Version Compatibility Table :

We are releasing the version compatibility table to help users get to see which Spark NLP licensed version is built against which core (open source) version. We are going to release a detailed one after running some tests across the jars from each library.

{:.table-model-big}
| Healthcare| Public |
|-----------|--------|
| 2.7.6     | 2.7.4  |
| 2.7.5     | 2.7.4  |
| 2.7.4     | 2.7.3  |
| 2.7.3     | 2.7.3  |
| 2.7.2     | 2.6.5  |
| 2.7.1     | 2.6.4  |
| 2.7.0     | 2.6.3  |
| 2.6.2     | 2.6.2  |
| 2.6.0     | 2.6.0  |
| 2.5.5     | 2.5.5  |
| 2.5.3     | 2.5.3  |
| 2.5.2     | 2.5.2  |
| 2.5.0     | 2.5.0  |
| 2.4.7     | 2.4.5  |
| 2.4.6     | 2.4.5  |
| 2.4.5     | 2.4.5  |
| 2.4.2     | 2.4.2  |
| 2.4.1     | 2.4.1  |
| 2.4.0     | 2.4.0  |
| 2.3.6     | 2.3.6  |
| 2.3.5     | 2.3.5  |
| 2.3.4     | 2.3.4  |

</div><div class="h3-box" markdown="1">

#### 4. Pretrained Models Version Control :

Due to active release cycle, we are adding & training new pretrained models at each release and it might be tricky to maintain the backward compatibility or keep up with the latest models, especially for the users using our models locally in air-gapped networks.

We are releasing a new utility class to help you check your local & existing models with the latest version of everything we have up to date. This is an highly experimental feature of which we plan to improve and add more capability later on.


    from sparknlp_jsl.check_compatibility import Compatibility

     checker = sparknlp_jsl.Compatibility()

     result = checker.find_version(aws_access_key_id=license_keys['AWS_ACCESS_KEY_ID'],
                            aws_secret_access_key=license_keys['AWS_SECRET_ACCESS_KEY'],
                            metadata_path=None,
                            model = 'all' , # or a specific model name
                            target_version='all',
                            cache_pretrained_path='/home/ubuntu/cache_pretrained')

     >> result['outdated_models']

      [{'model_name': 'clinical_ner_assertion',
        'current_version': '2.4.0',
        'latest_version': '2.6.4'},
       {'model_name': 'jsl_rd_ner_wip_greedy_clinical',
        'current_version': '2.6.1',
        'latest_version': '2.6.2'},
       {'model_name': 'ner_anatomy',
        'current_version': '2.4.2',
        'latest_version': '2.6.4'},
       {'model_name': 'ner_aspect_based_sentiment',
        'current_version': '2.6.2',
        'latest_version': '2.7.2'},
       {'model_name': 'ner_bionlp',
        'current_version': '2.4.0',
        'latest_version': '2.7.0'},
       {'model_name': 'ner_cellular',
        'current_version': '2.4.2',
        'latest_version': '2.5.0'}]

      >> result['version_comparison_dict']

      [{'clinical_ner_assertion': {'current_version': '2.4.0', 'latest_version': '2.6.4'}}, {'jsl_ner_wip_clinical': {'current_version': '2.6.5', 'latest_version': '2.6.1'}}, {'jsl_ner_wip_greedy_clinical': {'current_version': '2.6.5', 'latest_version': '2.6.5'}}, {'jsl_ner_wip_modifier_clinical': {'current_version': '2.6.4', 'latest_version': '2.6.4'}}, {'jsl_rd_ner_wip_greedy_clinical': {'current_version': '2.6.1','latest_version': '2.6.2'}}]

</div><div class="h3-box" markdown="1">

#### 5. Updated Pretrained Models:

 (requires fresh `.pretraned()`)

- ner_deid_large
- ner_deid_enriched

</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

{%- include docs-healthcare-pagination.html -%}