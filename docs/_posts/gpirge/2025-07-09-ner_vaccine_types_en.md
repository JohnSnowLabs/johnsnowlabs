---
layout: model
title: Vaccinations and Infectious Diseases
author: John Snow Labs
name: ner_vaccine_types
date: 2025-07-09
tags: [licensed, en, clinical, ner, vaccines, infectious_diseases]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.0.3
spark_version: 3.4
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is trained to extract vaccine and related disease/symptom entities from clinical/medical texts.

This project has been funded in whole or in part with Federal funds from the National Institute of 
Allergy and Infectious Diseases, National Institutes of Health, Department of Health and Human 
Services, under Contract No. 75N93024C00010"

## Predicted Entities

`Bacterial_Vax`, `Viral_Vax`, `Cancer_Vax`, `Bac_Vir_Comb`, `Other_Vax`, `Vax_Dose`, `Infectious_Disease`, `Other_Disease_Disorder`, `Sign_Symptom`, `Toxoid`, `Adaptive_Immunity`, `Inactivated`, `Date`, `Age`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_vaccine_types_en_6.0.3_3.4_1752075858996.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_vaccine_types_en_6.0.3_3.4_1752075858996.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = MedicalNerModel.pretrained('ner_cancer_names', "en", "clinical/models")\
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

sample_texts = ["""
On May 14, 2023, a 57-year-old female presented with fever, joint pain, and fatigue three days after receiving her third dose of the Shingrix vaccine.
Her history includes rheumatoid arthritis, managed with immunosuppressants, and prior breast cancer in remission. 
She previously received Gardasil 9, an HPV vaccine, and the hepatitis B recombinant vaccine series in 2020. 
Notably, she developed mild aches following her annual influenza shot, which is an inactivated vaccine. 
The patient reported receiving the DTaP vaccine (a toxoid vaccine) as a child. 
She also had tuberculosis as a teenager and had COVID-19 twice during the pandemic. 
In 2022, she was enrolled in a clinical trial for Stimuvax, a cancer vaccine targeting MUC1-expressing tumors. 
The team is assessing whether the patient's symptoms are due to a flare in her autoimmune disease or a delayed viral vaccine reaction. 
"""]

data = spark.createDataFrame(sample_texts, StringType()).toDF("text")

result = pipeline.fit(data).transform(data)
```

{:.jsl-block}
```python
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

clinical_embeddings = nlp.WordEmbeddingsModel.pretrained('embeddings_clinical', "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = medical.NerModel.pretrained('ner_cancer_names', "en", "clinical/models")\
    .setInputCols(["sentence", "token","embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(['sentence', 'token', 'ner'])\
    .setOutputCol('ner_chunk')

pipeline = nlp.Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter   
    ])

sample_texts = ["""
On May 14, 2023, a 57-year-old female presented with fever, joint pain, and fatigue three days after receiving her third dose of the Shingrix vaccine.
Her history includes rheumatoid arthritis, managed with immunosuppressants, and prior breast cancer in remission. 
She previously received Gardasil 9, an HPV vaccine, and the hepatitis B recombinant vaccine series in 2020. 
Notably, she developed mild aches following her annual influenza shot, which is an inactivated vaccine. 
The patient reported receiving the DTaP vaccine (a toxoid vaccine) as a child. 
She also had tuberculosis as a teenager and had COVID-19 twice during the pandemic. 
In 2022, she was enrolled in a clinical trial for Stimuvax, a cancer vaccine targeting MUC1-expressing tumors. 
The team is assessing whether the patient's symptoms are due to a flare in her autoimmune disease or a delayed viral vaccine reaction. 
"""]

data = spark.createDataFrame(sample_texts, StringType()).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_vaccine_names", "en", "clinical/models")
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

val sample_texts = Seq("""On May 14, 2023, a 57-year-old female presented with fever, joint pain, and fatigue three days after receiving her third dose of the Shingrix vaccine.
Her history includes rheumatoid arthritis, managed with immunosuppressants, and prior breast cancer in remission. 
She previously received Gardasil 9, an HPV vaccine, and the hepatitis B recombinant vaccine series in 2020. 
Notably, she developed mild aches following her annual influenza shot, which is an inactivated vaccine. 
The patient reported receiving the DTaP vaccine (a toxoid vaccine) as a child. 
She also had tuberculosis as a teenager and had COVID-19 twice during the pandemic. 
In 2022, she was enrolled in a clinical trial for Stimuvax, a cancer vaccine targeting MUC1-expressing tumors. 
The team is assessing whether the patient's symptoms are due to a flare in her autoimmune disease or a delayed viral vaccine reaction. .
""").toDF("text")

val result = pipeline.fit(sample_texts).transform(sample_texts)
```
</div>

## Results

```bash
+-----------+--------------------+-----+---+----------------------+
|sentence_id|chunk               |begin|end|entities              |
+-----------+--------------------+-----+---+----------------------+
|0          |May 14, 2023        |4    |15 |Date                  |
|0          |57-year-old         |20   |30 |Age                   |
|0          |fever               |54   |58 |Sign_Symptom          |
|0          |joint pain          |61   |70 |Sign_Symptom          |
|0          |fatigue             |77   |83 |Sign_Symptom          |
|0          |third dose          |116  |125|Vax_Dose              |
|0          |Shingrix            |134  |141|Viral_Vax             |
|0          |vaccine             |143  |149|Adaptive_Immunity     |
|1          |rheumatoid arthritis|174  |193|Other_Disease_Disorder|
|1          |breast cancer       |239  |251|Other_Disease_Disorder|
|2          |Gardasil            |292  |301|Viral_Vax             |
|2          |HPV                 |307  |309|Infectious_Disease    |
|2          |vaccine             |311  |317|Adaptive_Immunity     |
|2          |hepatitis B         |328  |338|Infectious_Disease    |
|2          |recombinant         |340  |350|Other_Vax             |
|2          |vaccine             |352  |358|Adaptive_Immunity     |
|2          |2020                |370  |373|Date                  |
|3          |aches               |405  |409|Sign_Symptom          |
|3          |influenza           |432  |440|Infectious_Disease    |
|3          |inactivated         |460  |470|Inactivated           |
|3          |vaccine             |472  |478|Adaptive_Immunity     |
|4          |DTaP                |517  |520|Bacterial_Vax         |
|4          |vaccine             |522  |528|Adaptive_Immunity     |
|4          |toxoid              |533  |538|Toxoid                |
|4          |vaccine             |540  |546|Adaptive_Immunity     |
|4          |child               |554  |558|Age                   |
|5          |tuberculosis        |575  |586|Infectious_Disease    |
|5          |COVID-19            |610  |617|Infectious_Disease    |
|6          |2022                |650  |653|Date                  |
|6          |Stimuvax            |697  |704|Cancer_Vax            |
|6          |cancer              |709  |714|Other_Disease_Disorder|
|6          |vaccine             |716  |722|Adaptive_Immunity     |
|6          |tumors              |750  |755|Other_Disease_Disorder|
|7          |vaccine             |876  |882|Adaptive_Immunity     |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_vaccine_types|
|Compatibility:|Healthcare NLP 6.0.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|4.9 MB|

## References

In-house annotated case reports.

## Benchmarking

```bash
                  label  precision    recall  f1-score   support

      Adaptive_Immunity       0.96      0.98      0.97       659
                    Age       0.87      0.91      0.89       379
           Bac_Vir_Comb       0.94      0.97      0.96        66
          Bacterial_Vax       0.94      0.73      0.82       129
             Cancer_Vax       0.92      0.96      0.94       112
                   Date       0.93      0.92      0.92        99
            Inactivated       0.93      0.78      0.85        32
     Infectious_Disease       0.96      0.98      0.97       772
 Other_Disease_Disorder       0.87      0.90      0.89       441
              Other_Vax       0.77      1.00      0.87        17
           Sign_Symptom       0.87      0.86      0.87       197
                 Toxoid       0.94      1.00      0.97        15
               Vax_Dose       0.78      0.95      0.86       169
              Viral_Vax       0.94      0.94      0.94       186


              micro_avg       0.92      0.93      0.92      3273
              macro avg       0.90      0.92      0.91      3273
           weighted avg       0.92      0.93      0.92      3273
```
