---
layout: model
title: Summarize Clinical Notes (PubMed)
author: John Snow Labs
name: summarizer_biomedical_pubmed
date: 2023-04-03
tags: [licensed, en, clinical, summarization, tensorflow]
task: Summarization
language: en
edition: Healthcare NLP 4.3.2
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MedicalSummarizer
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is a Flan-T5 (LLM) based summarization model that is finetuned with biomedical datasets (Pubmed abstracts) by John Snow Labs.  It can generate summaries up to 512 tokens given an input text (max 1024 tokens).

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/summarizer_biomedical_pubmed_en_4.3.2_3.0_1680523127672.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/summarizer_biomedical_pubmed_en_4.3.2_3.0_1680523127672.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

summarizer = MedicalSummarizer.pretrained("summarizer_biomedical_pubmed", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("summary")\
    .setMaxTextLength(512)\
    .setMaxNewTokens(512)

pipeline = sparknlp.base.Pipeline(stages=[
    document_assembler,
    summarizer  
])

text = """Residual disease after initial surgery for ovarian cancer is the strongest prognostic factor for survival. However, the extent of surgical resection required to achieve optimal cytoreduction is controversial. Our goal was to estimate the effect of aggressive surgical resection on ovarian cancer patient survival.\\n A retrospective cohort study of consecutive patients with International Federation of Gynecology and Obstetrics stage IIIC ovarian cancer undergoing primary surgery was conducted between January 1, 1994, and December 31, 1998. The main outcome measures were residual disease after cytoreduction, frequency of radical surgical resection, and 5-year disease-specific survival.\\n The study comprised 194 patients, including 144 with carcinomatosis. The mean patient age and follow-up time were 64.4 and 3.5 years, respectively. After surgery, 131 (67.5%) of the 194 patients had less than 1 cm of residual disease (definition of optimal cytoreduction). Considering all patients, residual disease was the only independent predictor of survival; the need to perform radical procedures to achieve optimal cytoreduction was not associated with a decrease in survival. For the subgroup of patients with carcinomatosis, residual disease and the performance of radical surgical procedures were the only independent predictors. Disease-specific survival was markedly improved for patients with carcinomatosis operated on by surgeons who most frequently used radical procedures compared with those least likely to use radical procedures (44% versus 17%, P < .001).\\n Overall, residual disease was the only independent predictor of survival. Minimizing residual disease through aggressive surgical resection was beneficial, especially in patients with carcinomatosis."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val summarizer  = MedicalSummarizer.pretrained("summarizer_biomedical_pubmed", "en", "clinical/models")
    .setInputCols("document_prompt")
    .setOutputCol("answer")
    .setMaxTextLength(512)
    .setMaxNewTokens(512)

val pipeline = new Pipeline().setStages(Array(document_assembler, summarizer))

val text = """Residual disease after initial surgery for ovarian cancer is the strongest prognostic factor for survival. However, the extent of surgical resection required to achieve optimal cytoreduction is controversial. Our goal was to estimate the effect of aggressive surgical resection on ovarian cancer patient survival.\\n A retrospective cohort study of consecutive patients with International Federation of Gynecology and Obstetrics stage IIIC ovarian cancer undergoing primary surgery was conducted between January 1, 1994, and December 31, 1998. The main outcome measures were residual disease after cytoreduction, frequency of radical surgical resection, and 5-year disease-specific survival.\\n The study comprised 194 patients, including 144 with carcinomatosis. The mean patient age and follow-up time were 64.4 and 3.5 years, respectively. After surgery, 131 (67.5%) of the 194 patients had less than 1 cm of residual disease (definition of optimal cytoreduction). Considering all patients, residual disease was the only independent predictor of survival; the need to perform radical procedures to achieve optimal cytoreduction was not associated with a decrease in survival. For the subgroup of patients with carcinomatosis, residual disease and the performance of radical surgical procedures were the only independent predictors. Disease-specific survival was markedly improved for patients with carcinomatosis operated on by surgeons who most frequently used radical procedures compared with those least likely to use radical procedures (44% versus 17%, P < .001).\\n Overall, residual disease was the only independent predictor of survival. Minimizing residual disease through aggressive surgical resection was beneficial, especially in patients with carcinomatosis."""

val data = Seq(Array(text)).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

['The results of this review suggest that aggressive ovarian cancer surgery is associated with a significant reduction in the risk of recurrence and a reduction in the number of radical versus conservative surgical resections. However, the results of this review are based on only one small trial. Further research is needed to determine the role of aggressive ovarian cancer surgery in women with stage IIIC ovarian cancer.']
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|summarizer_biomedical_pubmed|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|920.0 MB|
