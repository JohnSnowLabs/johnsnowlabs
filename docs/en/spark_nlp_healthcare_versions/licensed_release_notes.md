---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Spark NLP for Healthcare Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/licensed_release_notes
key: docs-licensed-release-notes
modify_date: 2023-05-02
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 4.4.1

#### Highlights

We are pleased to announce the latest enhancements and features for Spark NLP for Healthcare. This release showcases significant improvements and updates, including:

+ Introducing a new biogpt-chat-jsl model (LLM), fine-tuned for clinical conversations in healthcare settings.
+ A specialized medical summarizer model (LLM) designed specifically for radiology report analysis.
+ Eight new Voice of Patient (VOP) Named Entity Recognition (NER) models for detecting clinical terms expressed in patients' own words.
+ Advanced Chunk Mapper models for precise mapping of NDC and HCPCS codes.
+ Innovative Social Determinants of Health (SDOH) text classification models.
+ Enhanced NER profiling with updated pre-trained pipelines, enabling the simultaneous execution of 100 clinical NER models.
+ The implementation of a negative label feature for increased accuracy in the Zero Shot Relation Extraction Model.
+ Allowing users to select specific entity tags in NameChunkObfuscator, 
+ Multi-mode deidentification & obfuscation support in a single pass with the streamlined Deid module.
+ Core improvements and bug fixes:
    - Aligning ChunkMapperModel output metadata with `SentenceEntityResolverModel` metadata for seamless compatibility.
    - Resolving issues with the `MedicalNerApproach` `setTagsMapping` parameter.
    - Removing "non-sense" UNK tokens from text generators (e.g. BioGPt) for enhanced output quality.
+ New and updated notebooks
+ New and updated demos
+ 17 new clinical models and pipelines added & updated in total


We are committed to delivering exceptional tools and resources for healthcare professionals and researchers, and we look forward to your valuable feedback on these latest updates.

</div><div class="h3-box" markdown="1">

#### Introducing A New biogpt-chat-jsl Model (LLM), Fine-Tuned For Clinical Conversations In Healthcare Settings.

We are excited to present the `biogpt_chat_jsl_conversational` text generator model, an advanced adaptation of the BioGPT-JSL model, meticulously fine-tuned with authentic medical conversations from clinical environments. This model is adept at answering clinical queries related to symptoms, medications, diagnostic tests, and various diseases.

In comparison to its predecessor, the `biogpt_chat_jsl` model, the new `biogpt_chat_jsl_conversational` model generates more succinct and focused responses, significantly enhancing the efficiency and user experience of our software. This cutting-edge model is poised to revolutionize the way healthcare professionals and researchers engage with clinical information.

*Example*:

```python
gpt_qa = MedicalTextGenerator.pretrained("biogpt_chat_jsl_conversational", "en", "clinical/models")\
    .setInputCols("documents")\
    .setOutputCol("answer")\
    .setMaxNewTokens(100)

sample_text = "How to treat asthma?"
```

*Result*:

```bash
answer: You have to take montelukast + albuterol tablet once or twice in day according to severity of symptoms. Montelukast is used as a maintenance therapy to relieve symptoms of asthma. Albuterol is used as a rescue therapy when symptoms are severe. You can also use inhaled corticosteroids ( ICS ) like budesonide or fluticasone for long term treatment.
```


</div><div class="h3-box" markdown="1">

#### A Specialized Medical Summarizer Model (LLM) Designed Specifically For Radiology Report Analysis.

We are proud to unveil the `summarizer_radiology` model, a highly specialized tool engineered to efficiently distill radiology reports by pinpointing and retaining the most crucial information. This model enables users to rapidly access a succinct synopsis of a report's key findings without compromising on essential details.

The `summarizer_radiology` model represents a significant advancement in the field of medical text analysis, offering unparalleled support to healthcare professionals in swiftly grasping the salient points of complex radiology reports and ultimately enhancing patient care outcomes.

*Example*:

```python
summarizer = MedicalSummarizer.pretrained("summarizer_radiology", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("summary")\
    .setMaxTextLength(512)\
    .setMaxNewTokens(512)

sample_text = """INDICATIONS: Peripheral vascular disease with claudication.
RIGHT:
  1. Normal arterial imaging of right lower extremity.
  2. Peak systolic velocity is normal.
  3. Arterial waveform is triphasic.
  4. Ankle brachial index is 0.96.
LEFT:
  1. Normal arterial imaging of left lower extremity.
  2. Peak systolic velocity is normal.
  3. Arterial waveform is triphasic throughout except in posterior tibial artery where it is biphasic.
  4. Ankle brachial index is 1.06.
IMPRESSION:
  Normal arterial imaging of both lower lobes.
"""
```

*Result*:

```bash
The patient has peripheral vascular disease with claudication. The right lower extremity shows normal arterial imaging, but the peak systolic velocity is normal. The arterial waveform is triphasic throughout, except for the posterior tibial artery, which is biphasic. The ankle brachial index is 0.96. The impression is normal arterial imaging of both lower lobes.
```


</div><div class="h3-box" markdown="1">


#### Eight New Voice of Patient (VOP) Named Entity Recognition (NER) Models For Detecting Clinical Terms Expressed In Patients' Own Words.

We are thrilled to introduce eight innovative Voice of Patient (VOP) Named Entity Recognition (NER) models, meticulously crafted to extract clinical terms from patients' unique linguistic expressions. These models empower healthcare professionals to analyze patient data with enhanced accuracy and efficiency, paving the way for more precise diagnoses and tailored treatment plans.

By leveraging the capabilities of these VOP NER models, healthcare providers can better understand patients' perspectives, bridging the communication gap and fostering more effective patient-centered care.


| model name                                 | description                              |            predicted entities             |
|--------------------------------------------|------------------------------------------|-------------------------------------------|
| [`ner_vop_anatomy_wip`](https://nlp.johnsnowlabs.com/2023/04/20/ner_vop_anatomy_wip_en.html)                 | Detecting anatomical terms expressed in patients' own words. | `Laterality`, `BodyPart` |
| [`ner_vop_clinical_dept_wip`](https://nlp.johnsnowlabs.com/2023/04/20/ner_vop_clinical_dept_wip_en.html)     | Detecting medical devices and clinical department mentions terms expressed in patients' own words. | `MedicalDevice`, `AdmissionDischarge`, `ClinicalDept` |
| [`ner_vop_demographic_wip`](https://nlp.johnsnowlabs.com/2023/04/20/ner_vop_demographic_wip_en.html)         | Detecting demographic terms expressed in patients' own words. | `SubstanceQuantity`, `RaceEthnicity`, `RelationshipStatus`, `Substance`, `Age`, `Employment`, `Gender` |
| [`ner_vop_problem_reduced_wip`](https://nlp.johnsnowlabs.com/2023/04/20/ner_vop_problem_reduced_wip_en.html) | Detecting clinical condition terms expressed in patients' own words. | `Modifier`, `HealthStatus`, `Problem` |
| [`ner_vop_problem_wip`](https://nlp.johnsnowlabs.com/2023/04/20/ner_vop_problem_wip_en.html)                 | Detecting clinical condition terms expressed in patients' own words using a granular taxonomy. | `InjuryOrPoisoning`, `Modifier`, `HealthStatus`, `Symptom`, `Disease`, `PsychologicalCondition` |
| [`ner_vop_temporal_wip`](https://nlp.johnsnowlabs.com/2023/04/20/ner_vop_temporal_wip_en.html)               | Detecting temporal references terms expressed in patients' own words.| `Frequency`, `Duration`, `DateTime`|
| [`ner_vop_test_wip`](https://nlp.johnsnowlabs.com/2023/04/20/ner_vop_test_wip_en.html)                       | Detecting test mention terms expressed in patients' own words. | `Measurements`, `TestResult`, `Test`, `VitalTest`|
| [`ner_vop_treatment_wip`](https://nlp.johnsnowlabs.com/2023/04/20/ner_vop_treatment_wip_en.html)             | Detecting treatment terms expressed in patients' own words. | `Treatment`, `Frequency`, `Procedure`, `Route`, `Duration`, `Dosage`, `Drug`, `Form`|

*Example*:

```python
ner = MedicalNerModel.pretrained("ner_vop_problem_wip", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

sample_text = """I"ve been experiencing joint pain and fatigue lately, so I went to the rheumatology department. After some tests, they diagnosed me with rheumatoid arthritis and started me on a treatment plan to manage the symptoms."""
```

*Results*:

| chunk                | ner_label   |
|:---------------------|:------------|
| pain                 | Symptom     |
| fatigue              | Symptom     |
| rheumatoid arthritis | Disease     |




</div><div class="h3-box" markdown="1">

#### Advanced Chunk Mapper Models For Precise Mapping Of NDC And HCPCS Codes:

We are delighted to present our cutting-edge chunk mapper models, meticulously crafted for the accurate mapping of National Drug Code (NDC) and Healthcare Common Procedure Coding System (HCPCS) codes. These innovative models enable users to swiftly and effortlessly identify the relevant codes, optimizing the coding and billing process while bolstering accuracy.

The introduction of these advanced chunk mapper models demonstrates our commitment to delivering state-of-the-art solutions that streamline healthcare administration tasks, ultimately contributing to improved efficiency and patient care outcomes.

+ [hcpcs_ndc_mapper](https://nlp.johnsnowlabs.com/2023/04/13/hcpcs_ndc_mapper_en.html) model maps Healthcare Common Procedure Coding System (HCPCS) codes to their corresponding National Drug Codes (NDC) and their drug brand names.

*Example*:

```python
...
chunkerMapper = DocMapperModel.pretrained("hcpcs_ndc_mapper", "en", "clinical/models")\
      .setInputCols(["hcpcs_chunk"])\
      .setOutputCol("mappings")\
      .setRels(["ndc_code", "brand_name"])

text= ["Q5106", "J9211", "J7508"]
```

 *Result:*

| hcpcs_chunk | mappings                              | relation   |
|-------------|---------------------------------------|------------|
| Q5106       | 59353-0003-10                         | ndc_code   |
| Q5106       | RETACRIT (PF) 3000 U/1 ML             | brand_name |
| J9211       | 59762-2596-01                         | ndc_code   |
| J9211       | IDARUBICIN HYDROCHLORIDE (PF) 1 MG/ML | brand_name |
| J7508       | 00469-0687-73                         | ndc_code   |
| J7508       | ASTAGRAF XL 5 MG                      | brand_name |


+ [ndc_hcpcs_mapper](https://nlp.johnsnowlabs.com/2023/04/13/ndc_hcpcs_mapper_en.html) model maps NDC with their corresponding HCPCS codes and their descriptions.

*Example*:

```python
...
chunkerMapper = DocMapperModel.pretrained("ndc_hcpcs_mapper", "en", "clinical/models")\
      .setInputCols(["ndc_chunk"])\
      .setOutputCol("hcpcs")\
      .setRels(["hcpcs_code", "hcpcs_description"])

text= ["16714-0892-01", "00990-6138-03", "43598-0650-11"]
```

 *Result:*

| ndc_chunk     | mappings                     | relation          |
|---------------|------------------------------|-------------------|
| 16714-0892-01 | J0878                        | hcpcs_code        |
| 16714-0892-01 | INJECTION, DAPTOMYCIN, 1 MG  | hcpcs_description |
| 00990-6138-03 | A4217                        | hcpcs_code        |
| 00990-6138-03 | STERILE WATER/SALINE, 500 ML | hcpcs_description |
| 43598-0650-11 | J9340                        | hcpcs_code        |
| 43598-0650-11 | INJECTION, THIOTEPA, 15 MG   | hcpcs_description |


</div><div class="h3-box" markdown="1">


#### Innovative Social Determinants Of Health (SDOH) Text Classification Models.

We are excited to announce the release of three new Social Determinants of Health (SDOH) text classification models, specifically tailored to analyze and classify information related to insurance status, insurance coverage, and SDOH insurance type. These cutting-edge models enable healthcare professionals and researchers to better understand the nuanced interplay of insurance factors that influence health outcomes and access to care.

By leveraging these innovative SDOH classification models, stakeholders can gain valuable insights into the insurance landscape and its impact on health disparities, ultimately informing more targeted interventions and policies to improve patient care and well-being.


| model name                                 | description                              |            predicted entities             |
|--------------------------------------------|------------------------------------------|-------------------------------------------|
| [`genericclassifier_sdoh_insurance_status_sbiobert_cased_mli`](https://nlp.johnsnowlabs.com/2023/04/27/genericclassifier_sdoh_insurance_status_sbiobert_cased_mli_en.html) | Detecting whether the patient has insurance or not | `Insured`, `Uninsured`, `Unknown` |
| [`genericclassifier_sdoh_insurance_coverage_sbiobert_cased_mli`](https://nlp.johnsnowlabs.com/2023/04/28/genericclassifier_sdoh_insurance_coverage_sbiobert_cased_mli_en.html) | Detecting insurance coverage | `Good`, `Poor`, `Unknown` |
| [`genericclassifier_sdoh_insurance_type_sbiobert_cased_mli`](https://nlp.johnsnowlabs.com/2023/04/28/genericclassifier_sdoh_insurance_type_sbiobert_cased_mli_en.html)  | Detecting insurance type | `Employer`, `Medicaid`, `Medicare`, `Military`, `Private`, `Other` |

*Example*:

```python
features_asm = FeaturesAssembler()\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("features")

 generic_classifier = GenericClassifierModel.pretrained("genericclassifier_sdoh_insurance_type_sbiobert_cased_mli", 'en', 'clinical/models')\
    .setInputCols(["features"])\
    .setOutputCol("prediction")

text_list = [
"""The patient has VA insurance.""", 
"""She is under Medicare insurance""",
"""The patient has good coverage of Private insurance""",
"""Medical File for John Smith, Male, Age 42 Chief Complaint: Patient complains of nausea, vomiting, and shortness of breath...""",
"""Certainly, here is an example case study for a patient with private insurance: Case Study for Emily Chen, Female, Age 38 ...""",
"""Medical File for John Doe, Male, Age 72 Chief Complaint: Patient reports shortness of breath and fatigue. History of Pres..."""]
```


*Result*:

|                                                                                             text|    result|
|-------------------------------------------------------------------------------------------------|----------|
|                                                                    The patient has VA insurance.| Military |
|                                                                  She is under Medicare insurance| Medicare |
|Medical File for John Smith, Male, Age 42 Chief Complaint: Patient complains of nausea, vomiti...| Medicaid |
|Certainly, here is an example case study for a patient with private insurance: Case Study for ...|  Private |
|  Medical File for John Doe, Male, Age 72 Chief Complaint: Patient reports shortness of breath...| Medicare |


</div><div class="h3-box" markdown="1">



#### Updated NER Profiling Pretrained Pipelines With New NER Models to Allow Running 100 Clinical NER Models At Once

We are proud to announce the latest updates to our `ner_profiling_clinical` and `ner_profiling_biobert` pre-trained pipelines, which now feature the integration of new Named Entity Recognition (NER) models. When executing these pipelines on your text, you can now benefit from the predictions generated by an impressive 100 clinical NER models in `ner_profiling_clinical` and 22 clinical NER models in `ner_profiling_biobert`.

These enhancements to our pre-trained pipelines showcase our commitment to providing healthcare professionals and researchers with state-of-the-art tools, enabling more efficient and accurate analysis of clinical text to support data-driven decision-making and improved patient care outcomes.

You can check [ner_profiling_clinical](https://nlp.johnsnowlabs.com/2023/04/26/ner_profiling_clinical_en.html) and [ner_profiling_biobert](https://nlp.johnsnowlabs.com/2023/04/26/ner_profiling_biobert_en.html) Models Hub pages for more details and the NER model lists that these pipelines include.


</div><div class="h3-box" markdown="1">

#### The Implementation Of A Negative Label Feature For Increased Accuracy In The Zero Shot Relation Extraction Model

We are pleased to introduce the addition of a new `setNegativeRelationships` parameter to the `ZeroShotRelationExtractionModel` annotator, empowering users to exercise more effective control over the model's predictions for enhanced accuracy. This innovative parameter generates negative examples of relations and subsequently removes them, resulting in improved precision for positive labels.

This advanced feature demonstrates our ongoing commitment to delivering state-of-the-art solutions for healthcare professionals and researchers, facilitating more accurate analysis of complex relationships within clinical text and ultimately contributing to better patient care and outcomes.

*Example*:

```python
re_model = sparknlp_jsl.annotator.ZeroShotRelationExtractionModel \
    .pretrained() \
    .setRelationalCategories({
        "CURE": ["{TREATMENT} cures {PROBLEM}."],
        "IMPROVE": ["{TREATMENT} improves {PROBLEM}.", "{TREATMENT} cures {PROBLEM}."],
        "REVEAL": ["{TEST} reveals {PROBLEM}."]})\
    .setMultiLabel(False)\
    .setInputCols(["re_ner_chunks", "sentences"]) \
    .setOutputCol("relations")\
    .setNegativeRelationships(["IMPROVE"])

sample_text = "Paracetamol can alleviate headache or sickness. An MRI test can be used to find cancer."
```

*Without Setting setNegativeRelationships*:

|relation|     chunk1|  entity1|  chunk2|entity2|                    hypothesis|confidence|
|--------|-----------|---------|--------|-------|------------------------------|----------|
|  REVEAL|An MRI test|     TEST|  cancer|PROBLEM|   An MRI test reveals cancer.| 0.9760039|
| IMPROVE|Paracetamol|TREATMENT|sickness|PROBLEM|Paracetamol improves sickness.|0.98819494|
| IMPROVE|Paracetamol|TREATMENT|headache|PROBLEM|Paracetamol improves headache.| 0.9929625|


*After Setting setNegativeRelationships*:

|relation|     chunk1|entity1|chunk2|entity2|                 hypothesis|confidence|
|--------|-----------|-------|------|-------|---------------------------|----------|
|  REVEAL|An MRI test|   TEST|cancer|PROBLEM|An MRI test reveals cancer.| 0.9760039|


</div><div class="h3-box" markdown="1">

#### Allowing users To Select Specific Entity Tags In NameChunkObfuscator

We are excited to introduce the new `setNameEntities` parameter for the `NameChunkObfuscator` annotator, enabling users to specify the labels they wish to obfuscate using an array list. The default value is set to ["NAME"], offering greater flexibility and customization when working with sensitive information.

This enhancement to the `NameChunkObfuscator` reflects our dedication to providing user-centric tools that cater to the diverse needs of healthcare professionals and researchers, ensuring the protection of sensitive data while maintaining the utility of the information for analysis and decision-making.

*Example*:

```python
nameChunkObfuscator = NameChunkObfuscatorApproach()\
  .setInputCols("ner_chunk")\
  .setOutputCol("replacement")\
  .setNameEntities(["PATIENT","DOCTOR","NAME"])

sample_text = '''John Davies Hendrickson is a 62 y.o. patient admitted. 
Dr. Lorand was scheduled for emergency assessment. 
John Davies Hendrickson is a teacher and Dr. Lorand is a Doctor.
Olivera is 25 years-old.
Dr. Roland offered his patient Olivera a healthy diet.  
John Davies Hendrickson Lorand has biggest name'''

```

As can be seen in the table below, `DOCTOR` and `PATIENT` chunks are consistently replaced with the same obfuscation chunks.

|                     ner_chunk|  label|                   replacement|
|------------------------------|-------|------------------------------|
|       John Davies Hendrickson|PATIENT|       Aesculapius Amalasuntha|
|                        Lorand| DOCTOR|                        Fulvia|
|       John Davies Hendrickson|PATIENT|       Aesculapius Amalasuntha|
|                        Lorand| DOCTOR|                        Fulvia|
|                       Olivera|PATIENT|                       Killian|
|                        Roland| DOCTOR|                        Rudolf|
|                       Olivera| DOCTOR|                       Killian|
|John Davies Hendrickson Lorand|PATIENT|Deipnosophistae Hermaphroditus|


|    | Sentence                                                         | Obfuscated                                                       |
|---:|:-----------------------------------------------------------------|:-----------------------------------------------------------------|
|  0 | John Davies Hendrickson is a 62 y.o. patient admitted.           | Aesculapius Amalasuntha is a 62 y.o. patient admitted.           |
|  1 | Dr. Lorand was scheduled for emergency assessment.               | Dr. Fulvia was scheduled for emergency assessment.               |
|  2 | John Davies Hendrickson is a teacher and Dr. Lorand is a Doctor. | Aesculapius Amalasuntha is a teacher and Dr. Fulvia is a Doctor. |
|  3 | Olivera is 25 years-old.                                         | Killian is 25 years-old.                                         |
|  4 | Dr. Roland offered his patient Olivera a healthy diet.           | Dr. Rudolf offered his patient Killian a healthy diet.           |
|  5 | John Davies Hendrickson Lorand has biggest name                  | Deipnosophistae Hermaphroditus has biggest name                  |



</div><div class="h3-box" markdown="1">

#### Multi-mode Deidentification And Obfuscation Support In A Single Pass With The Streamlined Deid Module

We are proud to announce the enhancement of our Deid module with the introduction of a one-pass, multi-mode deidentification feature. This powerful new capability significantly improves the module's functionality, enabling users to deidentify their data with increased efficiency, accuracy, and flexibility.

To utilize this feature for a single column, simply set the `multi_mode_file_path` parameter with the JSON file path describing the desired multi-mode configuration. This streamlined approach demonstrates our commitment to providing state-of-the-art tools that cater to the evolving needs of healthcare professionals and researchers, ensuring the protection of sensitive information while maintaining data utility for analysis and decision-making.

*Example*:

```python
#json to choose deid mode
sample_json= {
	"obfuscate": ["NAME", "PHONE"] ,
	"mask_entity_labels": ["AGE"],
	"skip": ["SSN"],
	"mask_same_length_chars":["DATE"],
	"mask_fixed_length_chars":["ZIP", "LOCATION"]
}

import json
with open('sample_multi-mode.json', 'w', encoding='utf-8') as f:
    json.dump(sample_json, f, ensure_ascii=False, indent=4)

#Deidentification with multi mode for one column
deid_implementor= Deid(spark,
                       input_file_path="deid_data.csv",
                       output_file_path="deidentified.csv",
                       custom_pipeline=model,
                       multi_mode_file_path="sample_multi-mode.json")
                       
```


For multiple columns, we can set one specific JSON file path multi mode for each column.

*Example*:

```python
#json to choose deid mode for the 2nd column
sample_json_column2= {
	"obfuscate": ["SSN", "AGE"] ,
	"mask_entity_labels": ["DATE"],
	"skip": ["ID"],
	"mask_same_length_chars":["NAME"],
	"mask_fixed_length_chars":["ZIP", "LOCATION"]
}

import json
with open('sample_multi-mode_column2.json', 'w', encoding='utf-8') as f:
    json.dump(sample_json_column2, f, ensure_ascii=False, indent=4)

#Deidentification with multi mode for multiple columns
deid_implementor= Deid(spark,
                       input_file_path="deid_multiple_data.csv",
                       output_file_path="deidentified.csv",
                       custom_pipeline=model,
                       fields={"text": "sample_multi-mode.json", "text_1":"sample_multi-mode_column2.json"}, masking_policy="fixed_length_chars", 
                       fixed_mask_length=2, separator=",")
                       
```
For more detail please check [Clinical Deidentification Utility Module](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.5.Clinical_Deidentification_Utility_Module.ipynb)

</div><div class="h3-box" markdown="1">

#### Core Improvements and Bug Fixes

- Aligning ChunkMapperModel output metadata with `SentenceEntityResolverModel` metadata for seamless compatibility.
- Resolving issues with the `MedicalNerApproach` `setTagsMapping` parameter.
- Removing "non-sense" UNK tokens from text generators (e.g. BioGPt) for enhanced output quality



</div><div class="h3-box" markdown="1">

#### New and Updated Notebooks

- New [Comparison Medical Text Summarization Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/32.1.Comparison_Medical_Text_Summarization.ipynb) for summarization of clinical context can be used with new `MedicalSummarizer` annotator.
- New [Biogpt Chat JSL Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/33.Biogpt_Chat_JSL.ipynb) for test generation of clinical context can be used with new `MedicalTextGenerator` annotator.
- New [Text Classification with Contextual Window Splitting](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/30.2.Text_Classification_with_Contextual_Window_Splitting.ipynb) for text classification with contextual window splitting can be used with the new `WindowedSentenceModel` annotator.
- New [Review Functions of ALab Module Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Annotation_Lab/Review_Functions_of_ALab_Module_SparkNLP_JSL.ipynb) for ALAB module review functions.
- Updated [Clinical Deidentification Utility Module](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.5.Clinical_Deidentification_Utility_Module.ipynb) with the latest improvement.


</div><div class="h3-box" markdown="1">

#### New and Updated Demos

+ [Medical Large Language Modeling](https://demo.johnsnowlabs.com/healthcare/MEDICAL_LLM/) demo
+ [Medical Summarization Radiology](https://demo.johnsnowlabs.com/healthcare/MEDICAL_TEXT_SUMMARIZATION_RADIOLOGY/) demo
+ [BIOGPT CHAT JSL](https://demo.johnsnowlabs.com/healthcare/BIOGPT_CHAT_JSL/) demo
+ [MODELS](https://demo.johnsnowlabs.com/healthcare/MODELS/) demo

	- With MODELS demos, you can select all healthcare models as Task and Annotator based and you can see information about the models.

![image](https://user-images.githubusercontent.com/64752006/235436656-161ab6f4-11c5-4d56-80a4-b1b4c6f06865.png)



</div><div class="h3-box" markdown="1">

#### 17 New Clinical Models and Pipelines Added & Updated in Total


+ `biogpt_chat_jsl_conversational`
+ `summarizer_radiology`
+ `ner_profiling_biobert`
+ `ner_profiling_clinical`
+ `ner_vop_anatomy_wip`
+ `ner_vop_clinical_dept_wip`
+ `ner_vop_demographic_wip`
+ `ner_vop_problem_reduced_wip`
+ `ner_vop_problem_wip`
+ `ner_vop_temporal_wip`
+ `ner_vop_test_wip`
+ `ner_vop_treatment_wip`
+ `ndc_hcpcs_mapper`
+ `hcpcs_ndc_mapper`
+ `genericclassifier_sdoh_insurance_status_sbiobert_cased_mli`
+ `genericclassifier_sdoh_insurance_coverage_sbiobert_cased_mli`
+ `genericclassifier_sdoh_insurance_type_sbiobert_cased_mli`




</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)



<div class="prev_ver h3-box" markdown="1">

## Previous versions

</div>
{%- include docs-healthcare-pagination.html -%}
