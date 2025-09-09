---
layout: model
title: Vaccinations and Infectious Diseases
author: John Snow Labs
name: ner_vaccine_types_pipeline
date: 2025-07-14
tags: [licensed, en, clinical, pipeline, ner, vaccines, infectious_diseases]
task: [Pipeline Healthcare, Named Entity Recognition]
language: en
edition: Healthcare NLP 6.0.3
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to extract types of vaccines and related disease/symptom entities from clinical/medical texts.

This project has been funded in whole or in part with Federal funds from the National Institute of Allergy and Infectious Diseases, National Institutes of Health, Department of Health and Human Services, under Contract No. 75N93024C00010.

## Predicted Entities

`Bacterial_Vax`, `Viral_Vax`, `Cancer_Vax`, `Bac_Vir_Comb`, `Other_Vax`, `Vax_Dose`, `Infectious_Disease`, `Other_Disease_Disorder`, `Sign_Symptom`, `Toxoid`, `Adaptive_Immunity`, `Inactivated`, `Date`, `Age`


{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_vaccine_types_pipeline_en_6.0.3_3.4_1752516272515.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_vaccine_types_pipeline_en_6.0.3_3.4_1752516272515.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_vaccine_types_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""
On May 14, 2023, a 57-year-old female presented with fever, joint pain, and fatigue three days after receiving her third dose of the Shingrix vaccine.
Her history includes rheumatoid arthritis, managed with immunosuppressants, and prior breast cancer in remission.
She previously received Gardasil 9, an HPV vaccine, and the hepatitis B recombinant vaccine series in 2020.
Notably, she developed mild aches following her annual influenza shot, which is an inactivated vaccine.
The patient reported receiving the DTaP vaccine (a toxoid vaccine) as a child. She also had tuberculosis as a teenager and had COVID-19 twice during the pandemic.
In 2022, she was enrolled in a clinical trial for Stimuvax, a cancer vaccine targeting MUC1-expressing tumors.
The team is assessing whether the patient's symptoms are due to a flare in her autoimmune disease or a delayed viral vaccine reaction.
""")
```

{:.jsl-block}
```python
ner_pipeline = nlp.PretrainedPipeline("ner_vaccine_types_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""
On May 14, 2023, a 57-year-old female presented with fever, joint pain, and fatigue three days after receiving her third dose of the Shingrix vaccine.
Her history includes rheumatoid arthritis, managed with immunosuppressants, and prior breast cancer in remission.
She previously received Gardasil 9, an HPV vaccine, and the hepatitis B recombinant vaccine series in 2020.
Notably, she developed mild aches following her annual influenza shot, which is an inactivated vaccine.
The patient reported receiving the DTaP vaccine (a toxoid vaccine) as a child. She also had tuberculosis as a teenager and had COVID-19 twice during the pandemic.
In 2022, she was enrolled in a clinical trial for Stimuvax, a cancer vaccine targeting MUC1-expressing tumors.
The team is assessing whether the patient's symptoms are due to a flare in her autoimmune disease or a delayed viral vaccine reaction.
""")
```

```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_vaccine_types_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""
On May 14, 2023, a 57-year-old female presented with fever, joint pain, and fatigue three days after receiving her third dose of the Shingrix vaccine.
Her history includes rheumatoid arthritis, managed with immunosuppressants, and prior breast cancer in remission.
She previously received Gardasil 9, an HPV vaccine, and the hepatitis B recombinant vaccine series in 2020.
Notably, she developed mild aches following her annual influenza shot, which is an inactivated vaccine.
The patient reported receiving the DTaP vaccine (a toxoid vaccine) as a child. She also had tuberculosis as a teenager and had COVID-19 twice during the pandemic.
In 2022, she was enrolled in a clinical trial for Stimuvax, a cancer vaccine targeting MUC1-expressing tumors.
The team is assessing whether the patient's symptoms are due to a flare in her autoimmune disease or a delayed viral vaccine reaction.
""")
```
</div>

## Results

```bash
|    | chunks               |   begin |   end | entities               |
|---:|:---------------------|--------:|------:|:-----------------------|
|  0 | May 14, 2023         |       4 |    15 | Date                   |
|  1 | 57-year-old          |      20 |    30 | Age                    |
|  2 | fever                |      54 |    58 | Sign_Symptom           |
|  3 | joint pain           |      61 |    70 | Sign_Symptom           |
|  4 | fatigue              |      77 |    83 | Sign_Symptom           |
|  5 | third dose           |     116 |   125 | Vax_Dose               |
|  6 | Shingrix             |     134 |   141 | Viral_Vax              |
|  7 | vaccine              |     143 |   149 | Adaptive_Immunity      |
|  8 | rheumatoid arthritis |     173 |   192 | Other_Disease_Disorder |
|  9 | breast cancer        |     238 |   250 | Other_Disease_Disorder |
| 10 | Gardasil 9           |     290 |   299 | Viral_Vax              |
| 11 | HPV                  |     305 |   307 | Infectious_Disease     |
| 12 | vaccine              |     309 |   315 | Adaptive_Immunity      |
| 13 | hepatitis B          |     326 |   336 | Infectious_Disease     |
| 14 | recombinant          |     338 |   348 | Other_Vax              |
| 15 | vaccine              |     350 |   356 | Adaptive_Immunity      |
| 16 | 2020                 |     368 |   371 | Date                   |
| 17 | aches                |     402 |   406 | Sign_Symptom           |
| 18 | influenza            |     429 |   437 | Infectious_Disease     |
| 19 | inactivated          |     457 |   467 | Inactivated            |
| 20 | vaccine              |     469 |   475 | Adaptive_Immunity      |
| 21 | DTaP                 |     513 |   516 | Bacterial_Vax          |
| 22 | vaccine              |     518 |   524 | Adaptive_Immunity      |
| 23 | toxoid               |     529 |   534 | Toxoid                 |
| 24 | vaccine              |     536 |   542 | Adaptive_Immunity      |
| 25 | child                |     550 |   554 | Age                    |
| 26 | tuberculosis         |     570 |   581 | Infectious_Disease     |
| 27 | COVID-19             |     605 |   612 | Infectious_Disease     |
| 28 | 2022                 |     644 |   647 | Date                   |
| 29 | Stimuvax             |     691 |   698 | Cancer_Vax             |
| 30 | cancer               |     703 |   708 | Other_Disease_Disorder |
| 31 | vaccine              |     710 |   716 | Adaptive_Immunity      |
| 32 | tumors               |     744 |   749 | Other_Disease_Disorder |
| 33 | vaccine              |     869 |   875 | Adaptive_Immunity      |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_vaccine_types_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.3+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|


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
              micro-avg       0.92      0.93      0.92      3273
              macro-avg       0.90      0.92      0.91      3273
           weighted-avg       0.92      0.93      0.92      3273

```

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- TextMatcherInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
