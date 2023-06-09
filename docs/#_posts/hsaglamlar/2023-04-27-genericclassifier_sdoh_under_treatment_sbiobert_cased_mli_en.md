---
layout: model
title: SDOH Under Treatment For Classification
author: John Snow Labs
name: genericclassifier_sdoh_under_treatment_sbiobert_cased_mli
date: 2023-04-27
tags: [en, licensed, clinical, sdoh, generic_classifier, under_treatment, biobert]
task: Text Classification
language: en
edition: Healthcare NLP 4.3.2
spark_version: 3.0
supported: true
annotator: GenericClassifierModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This Generic Classifier model is intended for detecting if the patient is under treatment or not. If under treatment is not mentioned in the text, it is regarded as “not under treatment”. The model is trained by using GenericClassifierApproach annotator.

`Under_Treatment`: The patient is under treatment.

`Not_Under_Treatment_Or_Not_Mentioned`: The patient is not under treatment or it is not mentioned in the clinical notes.

## Predicted Entities

`Under_Treatment`, `Not_Under_Treatment_Or_Not_Mentioned`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/genericclassifier_sdoh_under_treatment_sbiobert_cased_mli_en_4.3.2_3.0_1682608513576.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/genericclassifier_sdoh_under_treatment_sbiobert_cased_mli_en_4.3.2_3.0_1682608513576.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

generic_classifier = GenericClassifierModel.pretrained("genericclassifier_sdoh_under_treatment_sbiobert_cased_mli", 'en', 'clinical/models')\
    .setInputCols(["features"])\
    .setOutputCol("prediction")

pipeline = Pipeline(stages=[
    document_assembler,
    sentence_embeddings,
    features_asm,
    generic_classifier    
])

text_list = ["""Sarah, a 55-year-old woman with a history of high cholesterol and a family history of heart disease, presented to her primary care physician with complaints of chest pain and shortness of breath. After a thorough evaluation, Sarah was diagnosed with coronary artery disease (CAD), a condition that can lead to heart attacks and other serious complications.

To manage her CAD, Sarah was started on a treatment plan that included medication to lower her cholesterol and blood pressure, as well as aspirin to prevent blood clots. In addition to medication, Sarah was advised to make lifestyle modifications such as improving her diet, quitting smoking, and increasing physical activity.

Over the course of several months, Sarah's symptoms improved, and follow-up tests showed that her cholesterol and blood pressure were within the target range. However, Sarah continued to experience occasional chest pain, and her medication regimen was adjusted accordingly.

With regular follow-up appointments and adherence to her treatment plan, Sarah's CAD remained under control, and she was able to resume her normal activities with improved quality of life.
""",

"""John, a 60-year-old man with a history of smoking and high blood pressure, presented to his primary care physician with complaints of chest pain and shortness of breath. Further tests revealed that John had a blockage in one of his coronary arteries, which required urgent intervention. However, John was hesitant to undergo treatment, citing concerns about potential complications and side effects of medications and procedures.

Despite the physician's recommendations and attempts to educate John about the risks of leaving the blockage untreated, John ultimately chose not to pursue any treatment. Over the next several months, John continued to experience symptoms, which progressively worsened, and he ultimately required hospitalization for a heart attack. The medical team attempted to intervene at that point, but the damage to John's heart was severe, and his prognosis was poor.
"""]

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

val generic_classifier = GenericClassifierModel.pretrained("genericclassifier_sdoh_under_treatment_sbiobert_cased_mli", "en", "clinical/models")
    .setInputCols("features")
    .setOutputCol("prediction")

val pipeline = new PipelineModel().setStages(Array(
    document_assembler,
    sentence_embeddings,
    features_asm,
    generic_classifier))

val data = Seq(Array("""Sarah, a 55-year-old woman with a history of high cholesterol and a family history of heart disease, presented to her primary care physician with complaints of chest pain and shortness of breath. After a thorough evaluation, Sarah was diagnosed with coronary artery disease (CAD), a condition that can lead to heart attacks and other serious complications.

To manage her CAD, Sarah was started on a treatment plan that included medication to lower her cholesterol and blood pressure, as well as aspirin to prevent blood clots. In addition to medication, Sarah was advised to make lifestyle modifications such as improving her diet, quitting smoking, and increasing physical activity.

Over the course of several months, Sarah's symptoms improved, and follow-up tests showed that her cholesterol and blood pressure were within the target range. However, Sarah continued to experience occasional chest pain, and her medication regimen was adjusted accordingly.

With regular follow-up appointments and adherence to her treatment plan, Sarah's CAD remained under control, and she was able to resume her normal activities with improved quality of life.
""",

"""John, a 60-year-old man with a history of smoking and high blood pressure, presented to his primary care physician with complaints of chest pain and shortness of breath. Further tests revealed that John had a blockage in one of his coronary arteries, which required urgent intervention. However, John was hesitant to undergo treatment, citing concerns about potential complications and side effects of medications and procedures.

Despite the physician's recommendations and attempts to educate John about the risks of leaving the blockage untreated, John ultimately chose not to pursue any treatment. Over the next several months, John continued to experience symptoms, which progressively worsened, and he ultimately required hospitalization for a heart attack. The medical team attempted to intervene at that point, but the damage to John's heart was severe, and his prognosis was poor.
""")).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+--------------------------------------+
|                                                                                                text|                                result|
+----------------------------------------------------------------------------------------------------+--------------------------------------+
|Sarah, a 55-year-old woman with a history of high cholesterol and a family history of heart disea...|                     [Under_Treatment]|
|John, a 60-year-old man with a history of smoking and high blood pressure, presented to his prima...|[Not_Under_Treatment_Or_Not_Mentioned]|
+----------------------------------------------------------------------------------------------------+--------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|genericclassifier_sdoh_under_treatment_sbiobert_cased_mli|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[features]|
|Output Labels:|[prediction]|
|Language:|en|
|Size:|3.4 MB|
|Dependencies:|sbiobert_base_cased_mli|

## References

Internal SDOH Project

## Benchmarking

```bash
                               label  precision    recall  f1-score   support
Not_Under_Treatment_Or_Not_Mentioned       0.86      0.68      0.76       222
                     Under_Treatment       0.86      0.94      0.90       450
                            accuracy         -         -       0.86       672
                           macro-avg       0.86      0.81      0.83       672
                        weighted-avg       0.86      0.86      0.85       672
```