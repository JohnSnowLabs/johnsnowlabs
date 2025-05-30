---
layout: model
title: SDOH Insurance Status For Classification
author: John Snow Labs
name: genericclassifier_sdoh_insurance_status_sbiobert_cased_mli
date: 2023-04-27
tags: [en, licensed, sdoh, social_determinants, generic_classifier, biobert]
task: Text Classification
language: en
edition: Healthcare NLP 4.4.0
spark_version: 3.0
supported: true
annotator: GenericClassifierModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This Generic Classifier model is intended for detecting whether the patient has insurance or not. If the patient's insurance status is not mentioned or is unknown, it is regarded as "Unknown". The model is trained by using GenericClassifierApproach annotator.

`Insured`: The patient has insurance.

`Uninsured`: The patient has no insurance.

`Unknown`: Insurance status is not mentioned in the clinical notes or is unknown.

## Predicted Entities

`Insured`, `Uninsured`, `Unknown`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/SDOH/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/27.0.Social_Determinant_of_Health_Models.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/genericclassifier_sdoh_insurance_status_sbiobert_cased_mli_en_4.4.0_3.0_1682623268182.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/genericclassifier_sdoh_insurance_status_sbiobert_cased_mli_en_4.4.0_3.0_1682623268182.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")
        
sentence_embeddings = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", 'en','clinical/models')\
    .setInputCols(["document"])\
    .setOutputCol("sentence_embeddings")

features_asm = FeaturesAssembler()\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("features")

generic_classifier = GenericClassifierModel.pretrained("genericclassifier_sdoh_insurance_status_sbiobert_cased_mli", 'en', 'clinical/models')\
    .setInputCols(["features"])\
    .setOutputCol("prediction")

pipeline = Pipeline(stages=[
    document_assembler,
    sentence_embeddings,
    features_asm,
    generic_classifier    
])

text_list = ["The patient has VA insurance.", 
"She doesn't have any kind of insurance",
"""Patient: Mary H.

Background: Mary is a 40-year-old woman who has been diagnosed with asthma and allergies. She has been managing her conditions with medication and regular follow-up appointments with her healthcare provider. She lives in a rented apartment with her husband and two children and has been stably housed for the past five years.

Presenting problem: Mary presents to the clinic for a routine check-up and reports no significant changes in her health status or symptoms related to her asthma or allergies. However, she expresses concerns about the quality of the air in her apartment and potential environmental triggers that could impact her health.

Medical history: Mary has a medical history of asthma and allergies. She takes an inhaler and antihistamines to manage her conditions.

Social history: Mary is married with two children and lives in a rented apartment. She and her husband both work full-time jobs and have health insurance. They have savings and are able to cover basic expenses.

Assessment: The clinician assesses Mary's medical conditions and determines that her asthma and allergies are stable and well-controlled. The clinician also assesses Mary's housing situation and determines that her apartment building is in good condition and does not present any immediate environmental hazards.

Plan: The clinician advises Mary to continue to monitor her health conditions and to report any changes or concerns to her healthcare team. The clinician also prescribes a referral to an allergist who can provide additional evaluation and treatment for her allergies. The clinician recommends that Mary and her family take steps to minimize potential environmental triggers in their apartment, such as avoiding smoking and using air purifiers. The clinician advises Mary to continue to maintain her stable housing situation and to seek assistance if any financial or housing issues arise.
""",

"""Patient: Sarah L.

Background: Sarah is a 35-year-old woman who has been experiencing housing insecurity for the past year. She was evicted from her apartment due to an increase in rent, which she could not afford, and has been staying with friends and family members ever since. She works as a part-time sales associate at a retail store and has no medical insurance.

Presenting problem: Sarah presents to the clinic with complaints of increased stress and anxiety related to her housing insecurity. She reports feeling constantly on edge and worried about where she will sleep each night. She is also having difficulty concentrating at work and has been missing shifts due to her anxiety.

Medical history: Sarah has no significant medical history and takes no medications.

Social history: Sarah is currently single and has no children. She has a high school diploma but has not attended college. She has been working at her current job for three years and earns minimum wage. She has no savings and relies on her income to cover basic expenses.

Assessment: The clinician assesses Sarah's mental health and determines that she is experiencing symptoms of anxiety and depression related to her housing insecurity. The clinician also assesses Sarah's housing situation and determines that she is at risk for homelessness if she is unable to secure stable housing soon.

Plan: The clinician refers Sarah to a social worker who can help her connect with local housing resources, including subsidized housing programs and emergency shelters. The clinician also prescribes an antidepressant medication to help manage her symptoms of anxiety and depression. The clinician advises Sarah to continue to seek employment opportunities that may offer higher pay and stability."""]

df = spark.createDataFrame(text_list, StringType()).toDF("text")

result = pipeline.fit(df).transform(df)

result.select("text", "prediction.result").show(truncate=100)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
        
val sentence_embeddings = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence_embeddings")

val features_asm = new FeaturesAssembler()
    .setInputCols("sentence_embeddings")
    .setOutputCol("features")

val generic_classifier = GenericClassifierModel.pretrained("genericclassifier_sdoh_insurance_status_sbiobert_cased_mli", "en", "clinical/models")
    .setInputCols("features")
    .setOutputCol("prediction")

val pipeline = new PipelineModel().setStages(Array(
    document_assembler,
    sentence_embeddings,
    features_asm,
    generic_classifier))

val data = Seq(Array("The patient has VA insurance.", 
"She doesn't have any kind of insurance",
"""Patient: Mary H.

Background: Mary is a 40-year-old woman who has been diagnosed with asthma and allergies. She has been managing her conditions with medication and regular follow-up appointments with her healthcare provider. She lives in a rented apartment with her husband and two children and has been stably housed for the past five years.

Presenting problem: Mary presents to the clinic for a routine check-up and reports no significant changes in her health status or symptoms related to her asthma or allergies. However, she expresses concerns about the quality of the air in her apartment and potential environmental triggers that could impact her health.

Medical history: Mary has a medical history of asthma and allergies. She takes an inhaler and antihistamines to manage her conditions.

Social history: Mary is married with two children and lives in a rented apartment. She and her husband both work full-time jobs and have health insurance. They have savings and are able to cover basic expenses.

Assessment: The clinician assesses Mary's medical conditions and determines that her asthma and allergies are stable and well-controlled. The clinician also assesses Mary's housing situation and determines that her apartment building is in good condition and does not present any immediate environmental hazards.

Plan: The clinician advises Mary to continue to monitor her health conditions and to report any changes or concerns to her healthcare team. The clinician also prescribes a referral to an allergist who can provide additional evaluation and treatment for her allergies. The clinician recommends that Mary and her family take steps to minimize potential environmental triggers in their apartment, such as avoiding smoking and using air purifiers. The clinician advises Mary to continue to maintain her stable housing situation and to seek assistance if any financial or housing issues arise.
""",

"""Patient: Sarah L.

Background: Sarah is a 35-year-old woman who has been experiencing housing insecurity for the past year. She was evicted from her apartment due to an increase in rent, which she could not afford, and has been staying with friends and family members ever since. She works as a part-time sales associate at a retail store and has no medical insurance.

Presenting problem: Sarah presents to the clinic with complaints of increased stress and anxiety related to her housing insecurity. She reports feeling constantly on edge and worried about where she will sleep each night. She is also having difficulty concentrating at work and has been missing shifts due to her anxiety.

Medical history: Sarah has no significant medical history and takes no medications.

Social history: Sarah is currently single and has no children. She has a high school diploma but has not attended college. She has been working at her current job for three years and earns minimum wage. She has no savings and relies on her income to cover basic expenses.

Assessment: The clinician assesses Sarah's mental health and determines that she is experiencing symptoms of anxiety and depression related to her housing insecurity. The clinician also assesses Sarah's housing situation and determines that she is at risk for homelessness if she is unable to secure stable housing soon.

Plan: The clinician refers Sarah to a social worker who can help her connect with local housing resources, including subsidized housing programs and emergency shelters. The clinician also prescribes an antidepressant medication to help manage her symptoms of anxiety and depression. The clinician advises Sarah to continue to seek employment opportunities that may offer higher pay and stability.""")).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+-----------+
|                                                                                                text|     result|
+----------------------------------------------------------------------------------------------------+-----------+
|                                                                       The patient has VA insurance.|  [Insured]|
|                                                              She doesn't have any kind of insurance|[Uninsured]|
|Patient: Mary H.\n\nBackground: Mary is a 40-year-old woman who has been diagnosed with asthma an...|  [Insured]|
|Patient: Sarah L.\n\nBackground: Sarah is a 35-year-old woman who has been experiencing housing i...|[Uninsured]|
+----------------------------------------------------------------------------------------------------+-----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|genericclassifier_sdoh_insurance_status_sbiobert_cased_mli|
|Compatibility:|Healthcare NLP 4.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[features]|
|Output Labels:|[prediction]|
|Language:|en|
|Size:|3.4 MB|
|Dependencies:|sbiobert_base_cased_mli|

## References

SDOH internal project

## Benchmarking

```bash
        label  precision    recall  f1-score   support
     Insured       0.94      0.90      0.92       145
   Uninsured       0.84      0.89      0.86        36
     Unknown       0.72      0.82      0.77        38
    accuracy         -         -       0.88       219
   macro-avg       0.84      0.87      0.85       219
weighted-avg       0.89      0.88      0.88       219

```
