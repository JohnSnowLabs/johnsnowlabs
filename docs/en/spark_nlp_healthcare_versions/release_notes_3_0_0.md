---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Healthcare NLP v3.0.0 Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/release_notes_3_0_0
key: docs-licensed-release-notes
modify_date: 2021-07-14
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="prev_ver h3-box" markdown="1">

### 3.0.0

We are very excited to announce that **Spark NLP for Healthcare 3.0.0** has been released! This has been one of the biggest releases we have ever done and we are so proud to share this with our customers.

</div><div class="h3-box" markdown="1">

#### Highlights:

Spark NLP for Healthcare 3.0.0 extends the support for Apache Spark 3.0.x and 3.1.x major releases on Scala 2.12 with both Hadoop 2.7. and 3.2. We now support all 4 major Apache Spark and PySpark releases of 2.3.x, 2.4.x, 3.0.x, and 3.1.x helping the customers to migrate from earlier Apache Spark versions to newer releases without being worried about Spark NLP support.

</div><div class="h3-box" markdown="1">

#### Highlights:
* Support for Apache Spark and PySpark 3.0.x on Scala 2.12
* Support for Apache Spark and PySpark 3.1.x on Scala 2.12
* Migrate to TensorFlow v2.3.1 with native support for Java to take advantage of many optimizations for CPU/GPU and new features/models introduced in TF v2.x
* A brand new `MedicalNerModel` annotator to train & load the licensed clinical NER models.
*  **Two times faster NER and Entity Resolution** due to new batch annotation technique.
* Welcoming 9x new Databricks runtimes to our Spark NLP family:
  * Databricks 7.3
  * Databricks 7.3 ML GPU
  * Databricks 7.4
  * Databricks 7.4 ML GPU
  * Databricks 7.5
  * Databricks 7.5 ML GPU
  * Databricks 7.6
  * Databricks 7.6 ML GPU
  * Databricks 8.0
  * Databricks 8.0 ML (there is no GPU in 8.0)
  * Databricks 8.1 Beta
* Welcoming 2x new EMR 6.x series to our Spark NLP family:
  * EMR 6.1.0 (Apache Spark 3.0.0 / Hadoop 3.2.1)
  * EMR 6.2.0 (Apache Spark 3.0.1 / Hadoop 3.2.1)
* Starting Spark NLP for Healthcare 3.0.0 the default packages  for CPU and GPU will be based on Apache Spark 3.x and Scala 2.12.

</div><div class="h3-box" markdown="1">

##### Deprecated

Text2SQL annotator is deprecated and will not be maintained going forward. We are working on a better and faster version of Text2SQL at the moment and will announce soon.

</div><div class="h3-box" markdown="1">

#### 1. MedicalNerModel Annotator

Starting Spark NLP for Healthcare 3.0.0, the licensed clinical and biomedical pretrained NER models will only work with this brand new annotator called `MedicalNerModel` and will not work with `NerDLModel` in open source version.

In order to make this happen, we retrained all the clinical NER models (more than 80) and uploaded to models hub.

Example:


    clinical_ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

</div><div class="h3-box" markdown="1">

#### 2. Speed Improvements

A new batch annotation technique implemented in Spark NLP 3.0.0 for `NerDLModel`,`BertEmbeddings`, and `BertSentenceEmbeddings` annotators will be reflected in `MedicalNerModel` and it improves prediction/inferencing performance radically. From now on the `batchSize` for these annotators means the number of rows that can be fed into the models for prediction instead of sentences per row. You can control the throughput when you are on accelerated hardware such as GPU to fully utilise it. Here are the overall speed comparison:

Now, NER inference and Entity Resolution are **two times faster** on CPU and three times faster on GPU.

</div><div class="h3-box" markdown="1">

#### 3. JSL Clinical NER Model

We are releasing the richest clinical NER model ever, spanning over 80 entities. It has been under development for the last 6 months and we manually annotated more than 4000 clinical notes to cover such a high number of entities in a single model. It has 4 variants at the moment:

- `jsl_ner_wip_clinical`
- `jsl_ner_wip_greedy_clinical`
- `jsl_ner_wip_modifier_clinical`
- `jsl_rd_ner_wip_greedy_clinical`

</div><div class="h3-box" markdown="1">

##### Entities:

`Kidney_Disease`, `HDL`, `Diet`, `Test`, `Imaging_Technique`, `Triglycerides`, `Obesity`, `Duration`, `Weight`, `Social_History_Header`, `ImagingTest`, `Labour_Delivery`, `Disease_Syndrome_Disorder`, `Communicable_Disease`, `Overweight`, `Units`, `Smoking`, `Score`, `Substance_Quantity`, `Form`, `Race_Ethnicity`, `Modifier`, `Hyperlipidemia`, `ImagingFindings`, `Psychological_Condition`, `OtherFindings`, `Cerebrovascular_Disease`, `Date`, `Test_Result`, `VS_Finding`, `Employment`, `Death_Entity`, `Gender`, `Oncological`, `Heart_Disease`, `Medical_Device`, `Total_Cholesterol`, `ManualFix`, `Time`, `Route`, `Pulse`, `Admission_Discharge`, `RelativeDate`, `O2_Saturation`, `Frequency`, `RelativeTime`, `Hypertension`, `Alcohol`, `Allergen`, `Fetus_NewBorn`, `Birth_Entity`, `Age`, `Respiration`, `Medical_History_Header`, `Oxygen_Therapy`, `Section_Header`, `LDL`, `Treatment`, `Vital_Signs_Header`, `Direction`, `BMI`, `Pregnancy`, `Sexually_Active_or_Sexual_Orientation`, `Symptom`, `Clinical_Dept`, `Measurements`, `Height`, `Family_History_Header`, `Substance`, `Strength`, `Injury_or_Poisoning`, `Relationship_Status`, `Blood_Pressure`, `Drug`, `Temperature`, `EKG_Findings`, `Diabetes`, `BodyPart`, `Vaccine`, `Procedure`, `Dosage`

</div><div class="h3-box" markdown="1">

#### 4. JSL Clinical Assertion Model

We are releasing a brand new clinical assertion model, supporting 8 assertion statuses.

- `jsl_assertion_wip`

</div><div class="h3-box" markdown="1">

##### Assertion Labels :

`Present`, `Absent`, `Possible`, `Planned`, `Someoneelse`, `Past`, `Family`, `Hypotetical`

</div><div class="h3-box" markdown="1">

#### 5. Library Version Compatibility Table :

Spark NLP for Healthcare 3.0.0 is compatible with Spark NLP 3.0.1

</div><div class="h3-box" markdown="1">

#### 6. Pretrained Models Version Control (Beta):

Due to active release cycle, we are adding & training new pretrained models at each release and it might be tricky to maintain the backward compatibility or keep up with the latest models, especially for the users using our models locally in air-gapped networks.

We are releasing a new utility class to help you check your local & existing models with the latest version of everything we have up to date. You will not need to specify your AWS credentials from now on. This is the second version of the model checker we released with 2.7.6 and will replace that soon.

    from sparknlp_jsl.compatibility_beta import CompatibilityBeta

    compatibility = CompatibilityBeta(spark)

    print(compatibility.findVersion("ner_deid"))

</div><div class="h3-box" markdown="1">

#### 7. Updated Pretrained Models:

 (requires fresh `.pretraned()`)

None

</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>
{%- include docs-healthcare-pagination.html -%}