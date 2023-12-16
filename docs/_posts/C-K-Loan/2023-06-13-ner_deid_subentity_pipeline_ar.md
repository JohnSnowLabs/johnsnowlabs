---
layout: model
title: Pipeline for Detect Subentity PHI for Deidentification (Arabic)
author: John Snow Labs
name: ner_deid_subentity_pipeline
date: 2023-06-13
tags: [licensed, clinical, deidentification, ar, pipeline]
task: [De-identification, Pipeline Healthcare]
language: ar
edition: Healthcare NLP 4.4.4
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [ner_deid_subentity](https://nlp.johnsnowlabs.com/2023/05/29/ner_deid_subentity_ar.html) model.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_pipeline_ar_4.4.4_3.2_1686666161768.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_pipeline_ar_4.4.4_3.2_1686666161768.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ner_deid_subentity_pipeline", "ar", "clinical/models")

text= '''
ملاحظات سريرية - مريض الربو. التاريخ: 16 أبريل 2000. اسم المريضة: ليلى حسن. العنوان: شارع المعرفة، مبنى رقم 789، حي الأمانة، جدة. الرمز البريدي: 54321. البلد: المملكة العربية السعودية. اسم المستشفى: مستشفى النور. اسم الطبيب: د. أميرة أحمد. تفاصيل الحالة: المريضة ليلى حسن، البالغة من العمر 35 عامًا، تعاني من مرض الربو المزمن. تشكو من ضيق التنفس والسعال المتكرر والشهيق الشديد. تم تشخيصها بمرض الربو بناءً على تاريخها الطبي واختبارات وظائف الرئة. الخطة: تم وصف مضادات الالتهاب غير الستيرويدية والموسعات القصبية لتحسين التنفس وتقليل التهيج. يجب على المريضة حمل معها جهاز الاستنشاق في حالة حدوث نوبة ربو حادة. يتعين على المريضة تجنب التحسس من العوامل المسببة للربو، مثل الدخان والغبار والحيوانات الأليفة. يجب مراقبة وظائف الرئة بانتظام ومتابعة التعليمات الطبية المتعلقة بمرض الربو. تعليم المريضة بشأن كيفية استخدام جهاز الاستنشاق بشكل صحيح وتقنيات التنفس الصحيح.
'''

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("ner_deid_subentity_pipeline", "ar", "clinical/models")


val text = "ملاحظات سريرية - مريض الربو. التاريخ: 16 أبريل 2000. اسم المريضة: ليلى حسن. العنوان: شارع المعرفة، مبنى رقم 789، حي الأمانة، جدة. الرمز البريدي: 54321. البلد: المملكة العربية السعودية. اسم المستشفى: مستشفى النور. اسم الطبيب: د. أميرة أحمد. تفاصيل الحالة: المريضة ليلى حسن، البالغة من العمر 35 عامًا، تعاني من مرض الربو المزمن. تشكو من ضيق التنفس والسعال المتكرر والشهيق الشديد. تم تشخيصها بمرض الربو بناءً على تاريخها الطبي واختبارات وظائف الرئة. الخطة: تم وصف مضادات الالتهاب غير الستيرويدية والموسعات القصبية لتحسين التنفس وتقليل التهيج. يجب على المريضة حمل معها جهاز الاستنشاق في حالة حدوث نوبة ربو حادة. يتعين على المريضة تجنب التحسس من العوامل المسببة للربو، مثل الدخان والغبار والحيوانات الأليفة. يجب مراقبة وظائف الرئة بانتظام ومتابعة التعليمات الطبية المتعلقة بمرض الربو. تعليم المريضة بشأن كيفية استخدام جهاز الاستنشاق بشكل صحيح وتقنيات التنفس الصحيح."

val result = pipeline.fullAnnotate(text)
```
</div>



## Results

```bash
+---------------+--------+
|chunks         |entities|
+---------------+--------+
|16 أبريل 2000  |DATE    |
|ليلى حسن       |PATIENT |
|789،           |ZIP     |
|جدة            |CITY    |
|54321          |ZIP     |
|المملكة العربية|CITY    |
|السعودية       |COUNTRY |
|النور          |HOSPITAL|
|أميرة أحمد     |DOCTOR  |
|ليلى           |PATIENT |
|35             |AGE     |
+---------------+--------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_subentity_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|ar|
|Size:|1.2 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter