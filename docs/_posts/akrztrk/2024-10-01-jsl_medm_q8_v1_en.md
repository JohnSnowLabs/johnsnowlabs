---
layout: model
title: JSL_MedM (LLM - q8)
author: John Snow Labs
name: jsl_medm_q8_v1
date: 2024-10-01
tags: [licensed, clinical, en, llm, rag, qa, chat, tensorflow]
task: [Summarization, Question Answering]
language: en
edition: Healthcare NLP 5.5.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MedicalLLM
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This LLM model is trained to perform Q&A, Summarization, RAG, and Chat.

NOTE: "This model's size is 8B and is available to Healthcare NLP license owners for free. However, this is not the model most capable medical LLM that John Snow has to Labs offer. For the larger and better versions, please try out the models we have in [marketplaces](https://aws.amazon.com/marketplace/pp/prodview-z4jqmczvwgtby)."


{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_medm_q8_v1_en_5.5.0_3.0_1727809959050.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_medm_q8_v1_en_5.5.0_3.0_1727809959050.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

medical_llm = MedicalLLM.pretrained("jsl_medm_q8_v1", "en", "clinical/models")\
    .setInputCols("document")\
    .setOutputCol("completions")\
    .setBatchSize(1)\
    .setNPredict(100)\
    .setUseChatTemplate(True)\
    .setTemperature(0)


pipeline = Pipeline(
    stages = [
        document_assembler,
        medical_llm
])

medm_prompt = """
summarize the following content.

 content:
 ---------------------------- INDICATIONS AND USAGE ---------------------------
 KISUNLA is an amyloid beta-directed antibody indicated for the
 treatment of Alzheimer’s disease. Treatment with KISUNLA should be
 initiated in patients with mild cognitive impairment or mild dementia
 stage of disease, the population in which treatment was initiated in the
 clinical trials. (1)
 ------------------------DOSAGE AND ADMINISTRATION-----------------------
 • Confirm the presence of amyloid beta pathology prior to initiating
 treatment. (2.1)
 • The recommended dosage of KISUNLA is 700 mg administered as
 an intravenous infusion over approximately 30 minutes every four
 weeks for the first three doses, followed by 1400 mg every four
 weeks. (2.2)
 • Consider stopping dosing with KISUNLA based on reduction of
 amyloid plaques to minimal levels on amyloid PET imaging. (2.2)
 • Obtain a recent baseline brain MRI prior to initiating treatment.
 (2.3, 5.1)
 • Obtain an MRI prior to the 2nd, 3rd, 4th, and 7th infusions. If
 radiographically observed ARIA occurs, treatment
 recommendations are based on type, severity, and presence of
 symptoms. (2.3, 5.1)
 • Dilution to a final concentration of 4 mg/mL to 10 mg/mL with 0.9%
 Sodium Chloride Injection, is required prior to administration. (2.4)
 ----------------------DOSAGE FORMS AND STRENGTHS---------------------
 Injection: 350 mg/20 mL (17.5 mg/mL) in a single-dose vial. (3)
 ------------------------------- CONTRAINDICATIONS ------------------------------
 KISUNLA is contraindicated in patients with known serious
 hypersensitivity to donanemab-azbt or to any of the excipients. (4, 5.2)
 ------------------------WARNINGS AND PRECAUTIONS-----------------------
 • Amyloid Related Imaging Abnormalities (ARIA): Enhanced clinical
 vigilance for ARIA is recommended during the first 24 weeks of
 treatment with KISUNLA. Risk of ARIA, including symptomatic
 ARIA, was increased in apolipoprotein E ε4 (ApoE ε4)
 homozygotes compared to heterozygotes and noncarriers. The risk
 of ARIA-E and ARIA-H is increased in KISUNLA-treated patients
 with pretreatment microhemorrhages and/or superficial siderosis. If
 a patient experiences symptoms suggestive of ARIA, clinical
 evaluation should be performed, including MRI scanning if
 indicated. (2.3, 5.1)
 • Infusion-Related Reactions: The infusion rate may be reduced, or
 the infusion may be discontinued, and appropriate therapy initiated
 as clinically indicated. Consider pre-treatment with antihistamines,
 acetaminophen, or corticosteroids prior to subsequent dosing. (5.3)
 -------------------------------ADVERSE REACTIONS------------------------------
 Most common adverse reactions (at least 10% and higher incidence
 compared to placebo): ARIA-E, ARIA-H microhemorrhage, ARIA-H
 superficial siderosis, and headache. (6.1)
"""

data = spark.createDataFrame([[medm_prompt]]).toDF("text")

results = pipeline.fit(data).transform(data)

results.select("completions").show(truncate=False)

```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val medical_llm = MedicalLLM.pretrained("jsl_medm_q8_v1", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("completions")
    .setBatchSize(1)
    .setNPredict(100)
    .setUseChatTemplate(True)
    .setTemperature(0)


val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    medical_llm
))

val  medm_prompt = """
summarize the following content.

 content:
 ---------------------------- INDICATIONS AND USAGE ---------------------------
 KISUNLA is an amyloid beta-directed antibody indicated for the
 treatment of Alzheimer’s disease. Treatment with KISUNLA should be
 initiated in patients with mild cognitive impairment or mild dementia
 stage of disease, the population in which treatment was initiated in the
 clinical trials. (1)
 ------------------------DOSAGE AND ADMINISTRATION-----------------------
 • Confirm the presence of amyloid beta pathology prior to initiating
 treatment. (2.1)
 • The recommended dosage of KISUNLA is 700 mg administered as
 an intravenous infusion over approximately 30 minutes every four
 weeks for the first three doses, followed by 1400 mg every four
 weeks. (2.2)
 • Consider stopping dosing with KISUNLA based on reduction of
 amyloid plaques to minimal levels on amyloid PET imaging. (2.2)
 • Obtain a recent baseline brain MRI prior to initiating treatment.
 (2.3, 5.1)
 • Obtain an MRI prior to the 2nd, 3rd, 4th, and 7th infusions. If
 radiographically observed ARIA occurs, treatment
 recommendations are based on type, severity, and presence of
 symptoms. (2.3, 5.1)
 • Dilution to a final concentration of 4 mg/mL to 10 mg/mL with 0.9%
 Sodium Chloride Injection, is required prior to administration. (2.4)
 ----------------------DOSAGE FORMS AND STRENGTHS---------------------
 Injection: 350 mg/20 mL (17.5 mg/mL) in a single-dose vial. (3)
 ------------------------------- CONTRAINDICATIONS ------------------------------
 KISUNLA is contraindicated in patients with known serious
 hypersensitivity to donanemab-azbt or to any of the excipients. (4, 5.2)
 ------------------------WARNINGS AND PRECAUTIONS-----------------------
 • Amyloid Related Imaging Abnormalities (ARIA): Enhanced clinical
 vigilance for ARIA is recommended during the first 24 weeks of
 treatment with KISUNLA. Risk of ARIA, including symptomatic
 ARIA, was increased in apolipoprotein E ε4 (ApoE ε4)
 homozygotes compared to heterozygotes and noncarriers. The risk
 of ARIA-E and ARIA-H is increased in KISUNLA-treated patients
 with pretreatment microhemorrhages and/or superficial siderosis. If
 a patient experiences symptoms suggestive of ARIA, clinical
 evaluation should be performed, including MRI scanning if
 indicated. (2.3, 5.1)
 • Infusion-Related Reactions: The infusion rate may be reduced, or
 the infusion may be discontinued, and appropriate therapy initiated
 as clinically indicated. Consider pre-treatment with antihistamines,
 acetaminophen, or corticosteroids prior to subsequent dosing. (5.3)
 -------------------------------ADVERSE REACTIONS------------------------------
 Most common adverse reactions (at least 10% and higher incidence
 compared to placebo): ARIA-E, ARIA-H microhemorrhage, ARIA-H
 superficial siderosis, and headache. (6.1)
"""

val data = Seq(medm_prompt).toDF("text")

val results = pipeline.fit(data).transform(data)

results.select("completions").show(truncate=False)

```
</div>

## Results

```bash

KISUNLA is an amyloid beta-directed antibody indicated for the treatment of Alzheimer's disease. It is recommended to initiate treatment in patients with mild cognitive impairment or mild dementia stage of disease. The recommended dosage is 700 mg administered as an intravenous infusion over approximately 30 minutes every four weeks for the first three doses, followed by 1400 mg every four weeks. Patients should have a recent baseline brain MRI prior to initiating treatment and obtain an MRI prior to the 2nd,

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_medm_q8_v1|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|8.2 GB|



## Benchmarking

We have generated a total of 400 questions, 100 from each category. These questions were labeled and reviewed by 3 physician annotators. `%` indicates the preference rate.
Please see the more benchmark information [here](https://nlp.johnsnowlabs.com/docs/en/benchmark-llm).

```bash
## Overall
| Model    | Factuality % | Clinical Relevancy % | Conciseness % |
|----------|--------------|----------------------|---------------|
| JSL-MedM | 0.29         | 0.25                 | 0.50          |
| ChatGPT  | 0.21         | 0.30                 | 0.26          |
| Neutral  | 0.43         | 0.38                 | 0.17          |
| None     | 0.07         | 0.07                 | 0.08          |
| total    | 1.00         | 1.00                 | 1.00          |

## Summary 
| Model    | Factuality % | Clinical Relevancy % | Conciseness % |
|----------|--------------|----------------------|---------------|
| JSL-MedM | 0.42         | 0.42                 | 0.50          |
| GPT4o    | 0.33         | 0.33                 | 0.28          |
| Neutral  | 0.17         | 0.17                 | 0.12          |
| None     | 0.08         | 0.08                 | 0.10          |
| Total    | 1.00         | 1.00                 | 1.00          |

## QA

| Model    | Factuality % | Clinical Relevancy % | Conciseness % |
|----------|--------------|----------------------|---------------|
| JSL-MedM | 0.40         | 0.36                 | 0.60          |
| GPT4o    | 0.15         | 0.19                 | 0.19          |
| Neutral  | 0.38         | 0.38                 | 0.11          |
| None     | 0.08         | 0.08                 | 0.09          |
| Total    | 1.00         | 1.00                 | 1.00          |


## BioMedical

| Model    | Factuality % | Clinical Relevancy % | Conciseness % |
|----------|--------------|----------------------|---------------|
| JSL-MedM | 0.22         | 0.14                 | 0.55          |
| GPT4o    | 0.21         | 0.36                 | 0.23          |
| Neutral  | 0.49         | 0.44                 | 0.14          |
| None     | 0.07         | 0.06                 | 0.07          |
| Total    | 1.00         | 1.00                 | 1.00          |

## OpenEnded

| Model    | Factuality % | Clinical Relevancy % | Conciseness % |
|----------|--------------|----------------------|---------------|
| JSL-MedM | 0.21         | 0.19                 | 0.38          |
| GPT4o    | 0.18         | 0.30                 | 0.31          |
| Neutral  | 0.55         | 0.46                 | 0.26          |
| None     | 0.05         | 0.05                 | 0.06          |
| Total    | 1.00         | 1.00                 | 1.00          |

```
