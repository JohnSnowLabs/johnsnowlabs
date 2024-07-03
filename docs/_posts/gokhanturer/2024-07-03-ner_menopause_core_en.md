---
layout: model
title: Detect Menopause Specific Entities
author: John Snow Labs
name: ner_menopause_core
date: 2024-07-03
tags: [licensed, en, clinical, ner, menopause, core]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.3.2
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Menopause Core model is designed to detect and label core entities related to menopause and associated conditions within text data. Menopause-related terms and conditions are crucial factors that influence individuals’ health outcomes, especially among women undergoing the menopausal transition. The model has been trained using advanced machine learning techniques on a diverse range of text sources. It can accurately recognize and classify a wide range of menopause-related entities. The model’s accuracy and precision have been carefully validated against expert-labeled data to ensure reliable and consistent results. Here are the labels of the Menopause Core model with their description:

`Perimenopause` : The transition period before menopause, which can last from a few months to several years. “Perimenopausal symptoms include hot flashes and irregular menstrual cycles.”
`Menopause` : The permanent end of menstrual cycles for at least 12 consecutive months. “She has been experiencing menopausal symptoms such as hot flashes and night sweats.”
`Gynecological_Symptom` : Symptoms related to the female reproductive system. “Heavy menstrual bleeding and pelvic pain are common gynecological symptoms.”
`Gynecological_Disease` : Diseases affecting the female reproductive system. “Conditions like fibroids and polycystic ovary syndrome are considered gynecological diseases.”
`Other_Symptom` : Symptoms not specifically categorized under other defined labels. “General symptoms such as fatigue and headaches.”
`Irregular_Menstruation` : Variations in the menstrual cycle. “Irregular menstrual cycles can be a sign of perimenopause.”
`G_P` : Information about the patient's gynecological history, including gravida (number of pregnancies) and para (number of births). “The patient's G2P1 status indicates two pregnancies and one live birth.”
`Hypertension` : Persistently elevated blood pressure. “She has a history of hypertension and takes medication to manage it.”
`Osteoporosis` : A condition characterized by weak and brittle bones. “Osteoporosis increases the risk of fractures in postmenopausal women.”
`Oncological` : Conditions related to cancer. “Breast cancer is a common oncological concern for menopausal women.”
`Fracture` : Breaks in bones due to mechanical forces. “Osteoporosis can lead to an increased risk of fractures.”
`Hormone_Replacement_Therapy` (HRT) : Hormone therapy to relieve menopausal symptoms. “Hormone replacement therapy can help manage hot flashes and other menopausal symptoms.”
`Osteoporosis_Therapy` : Treatments aimed at improving bone density and strength. “Medications like bisphosphonates are used in osteoporosis therapy.”
`Antidepressants` : Medications used to treat depression and related conditions. “SSRIs are commonly prescribed antidepressants for menopausal women experiencing depression.”
`Procedure` : Medical procedures related to menopausal care. “Hysterectomy is a procedure that may be performed for certain gynecological conditions.”
`Hormone_Testing` : Tests to measure hormone levels in the body. “Hormone testing can help diagnose menopausal status.”
`Vaginal_Swab` : A diagnostic test involving a swab from the vaginal area. “Vaginal swabs are used to detect infections or other conditions.”
`Age` : The age of the patient. “Menopausal symptoms commonly begin around the age of 50.”
`Test_Result` : Results from various medical tests. “The test results indicated low bone density, suggestive of osteoporosis.”

## Predicted Entities

`Perimenopause`, `Menopause`, `Gynecological_Symptom`, `Gynecological_Disease`, `Other_Symptom`, `Irregular_Menstruation`, `G_P`, `Hypertension`, `Osteoporosis`, `Oncological`, `Fracture`, `Hormone_Replacement_Therapy`, `Osteporosis_Therapy`, `Antidepressants`, `Procedure`, `Hormone_Testing`, `Vaginal_Swab`, `Age`, `Test_Result`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_menopause_core_en_5.3.2_3.0_1720018938030.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_menopause_core_en_5.3.2_3.0_1720018938030.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

clinical_embeddings = WordEmbeddingsModel.pretrained('embeddings_clinical', "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_menopause_core", "en", "clinical/models"))\
    .setInputCols(["sentence", "token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(['sentence', 'token', 'ner'])\
    .setOutputCol('ner_chunk')

pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter   
    ])

sample_texts = ["""The patient is a 52-year-old female, G3P2, who presents with complaints of irregular menstruation and symptoms suggestive of perimenopause. She reports experiencing hot flashes, night sweats, and vaginal dryness. Her medical history includes polycystic ovary syndrome (PCOS), fatigue, mood swings, hypertension diagnosed 5 years ago and currently managed with medication, and osteoporosis diagnosed 2 years ago with ongoing treatment. 
Current medications include estradiol for hormone replacement therapy, alendronate for osteoporosis therapy, and fluoxetine for depressive symptoms related to menopause. Recent tests and procedures include a bone density scan to monitor osteoporosis, blood tests for estradiol and follicle-stimulating hormone (FSH) levels, and a vaginal swab collected for routine infection screening. Test results showed elevated FSH levels indicating menopause.
The patient's family history includes breast cancer in her mother and a hip fracture in her mother at the age of 60. The plan is to continue current hormone replacement therapy and osteoporosis therapy, with follow-up appointments every 6 months to monitor symptoms and treatment efficacy."""]

data = spark.createDataFrame(sample_texts, StringType()).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_menopause_core", "en", "clinical/models")
    .setInputCols(Array("sentence", "token","embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentenceDetector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter   
))

val sample_texts = Seq("""The patient is a 52-year-old female, G3P2, who presents with complaints of irregular menstruation and symptoms suggestive of perimenopause. She reports experiencing hot flashes, night sweats, and vaginal dryness. Her medical history includes polycystic ovary syndrome (PCOS), fatigue, mood swings, hypertension diagnosed 5 years ago and currently managed with medication, and osteoporosis diagnosed 2 years ago with ongoing treatment. 
Current medications include estradiol for hormone replacement therapy, alendronate for osteoporosis therapy, and fluoxetine for depressive symptoms related to menopause. Recent tests and procedures include a bone density scan to monitor osteoporosis, blood tests for estradiol and follicle-stimulating hormone (FSH) levels, and a vaginal swab collected for routine infection screening. Test results showed elevated FSH levels indicating menopause.
The patient's family history includes breast cancer in her mother and a hip fracture in her mother at the age of 60. The plan is to continue current hormone replacement therapy and osteoporosis therapy, with follow-up appointments every 6 months to monitor symptoms and treatment efficacy.""").toDF("text")

val result = pipeline.fit(sample_texts).transform(sample_texts)
```
</div>

## Results

```bash
+----------------------------+-----+----+---------------------------+
|chunk                       |begin|end |ner_label                  |
+----------------------------+-----+----+---------------------------+
|irregular menstruation      |76   |97  |Irregular_Menstruation     |
|perimenopause               |126  |138 |Perimenopause              |
|hot flashes                 |166  |176 |Other_Symptom              |
|night sweats                |179  |190 |Other_Symptom              |
|vaginal dryness             |197  |211 |Gynecological_Symptom      |
|polycystic ovary syndrome   |243  |267 |Gynecological_Disease      |
|PCOS                        |270  |273 |Gynecological_Disease      |
|fatigue                     |277  |283 |Other_Symptom              |
|hypertension                |299  |310 |Hypertension               |
|osteoporosis                |377  |388 |Osteoporosis               |
|estradiol                   |466  |474 |Hormone_Replacement_Therapy|
|hormone replacement therapy |480  |506 |Hormone_Replacement_Therapy|
|alendronate                 |509  |519 |Osteporosis_Therapy        |
|osteoporosis                |525  |536 |Osteoporosis               |
|fluoxetine                  |551  |560 |Antidepressants            |
|menopause                   |597  |605 |Menopause                  |
|osteoporosis                |675  |686 |Osteoporosis               |
|estradiol                   |705  |713 |Hormone_Testing            |
|follicle-stimulating hormone|719  |746 |Hormone_Testing            |
|FSH                         |749  |751 |Hormone_Testing            |
|vaginal swab                |768  |779 |Vaginal_Swab               |
|elevated                    |844  |851 |Test_Result                |
|FSH                         |853  |855 |Hormone_Testing            |
|menopause                   |875  |883 |Menopause                  |
|breast cancer               |925  |937 |Oncological                |
|hip fracture                |959  |970 |Fracture                   |
|age of 60                   |993  |1001|Age                        |
|hormone replacement therapy |1036 |1062|Hormone_Replacement_Therapy|
|osteoporosis                |1068 |1079|Osteoporosis               |
+----------------------------+-----+----+---------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_menopause_core|
|Compatibility:|Healthcare NLP 5.3.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|2.8 MB|

## References

The datasets employed in training this model were meticulously curated and annotated using our in-house capabilities.

## Benchmarking

```bash
                      label  precision    recall  f1-score   support
                        Age       0.94      0.88      0.91       217
            Antidepressants       1.00      1.00      1.00         9
                   Fracture       0.98      0.99      0.99       269
                        G_P       1.00      0.79      0.89        39
      Gynecological_Disease       0.90      0.74      0.82       429
      Gynecological_Symptom       0.98      1.00      0.99        62
Hormone_Replacement_Therapy       0.95      0.99      0.97        87
            Hormone_Testing       0.94      0.83      0.88       175
               Hypertension       1.00      1.00      1.00        15
     Irregular_Menstruation       0.99      0.97      0.98        79
                  Menopause       0.99      1.00      1.00       144
                Oncological       0.95      0.87      0.91       211
               Osteoporosis       0.73      1.00      0.84        90
        Osteporosis_Therapy       0.96      0.98      0.97        52
              Other_Symptom       0.88      0.89      0.89       225
              Perimenopause       1.00      0.97      0.98        63
                  Procedure       0.92      0.85      0.89       270
                Test_Result       0.96      0.78      0.86       218
               Vaginal_Swab       1.00      1.00      1.00        11
                  micro-avg       0.93      0.88      0.91      2665
                  macro-avg       0.95      0.92      0.93      2665
               weighted-avg       0.94      0.88      0.90      2665
```