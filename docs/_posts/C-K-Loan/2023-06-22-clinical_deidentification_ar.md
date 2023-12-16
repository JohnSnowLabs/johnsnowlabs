---
layout: model
title: Clinical Deidentification Pipeline (Arabic)
author: John Snow Labs
name: clinical_deidentification
date: 2023-06-22
tags: [licensed, deidentification, clinical, ar, pipeline]
task: [De-identification, Pipeline Healthcare]
language: ar
edition: Healthcare NLP 4.4.4
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to deidentify Arabic PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text. The pipeline can mask and obfuscate CONTACT, NAME, DATE, ID, LOCATION, AGE, PATIENT, HOSPITAL, ORGANIZATION, CITY, STREET, USERNAME, SEX, IDNUM, EMAIL, ZIP, MEDICALRECORD, PROFESSION, PHONE, COUNTRY, DOCTOR, SSN, ACCOUNT, LICENSE, DLN and VIN

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_ar_4.4.4_3.4_1687412427565.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_ar_4.4.4_3.4_1687412427565.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification", "ar", "clinical/models")

text = '''

ملاحظات سريرية - مريض الربو:

التاريخ: 30 مايو 2023
اسم المريضة: ليلى حسن

تم تسجيل المريض في النظام باستخدام رقم الضمان الاجتماعي 123456789012.

العنوان: شارع المعرفة، مبنى رقم 789، حي الأمانة، جدة
الرمز البريدي: 54321
البلد: المملكة العربية السعودية
اسم المستشفى: مستشفى النور
اسم الطبيب: د. أميرة أحمد

تفاصيل الحالة:
المريضة ليلى حسن، البالغة من العمر 35 عامًا، تعاني من مرض الربو المزمن. تشكو من ضيق التنفس والسعال المتكرر والشهيق الشديد. تم تشخيصها بمرض الربو بناءً على تاريخها الطبي واختبارات وظائف الرئة.

الخطة:

تم وصف مضادات الالتهاب غير الستيرويدية والموسعات القصبية لتحسين التنفس وتقليل التهيج.
يجب على المريضة حمل معها جهاز الاستنشاق في حالة حدوث نوبة ربو حادة.
يتعين على المريضة تجنب التحسس من العوامل المسببة للربو، مثل الدخان والغبار والحيوانات الأليفة.
يجب مراقبة وظائف الرئة بانتظام ومتابعة التعليمات الطبية المتعلقة بمرض الربو.
تعليم المريضة بشأن كيفية استخدام جهاز الاستنشاق بشكل صحيح وتقنيات التنفس الصحيح

'''
result = deid_pipeline.annotate(text)

print("\nMasked with entity labels")
print("-"*30)
print("\n".join(result['masked_with_entity']))
print("\nMasked with chars")
print("-"*30)
print("\n".join(result['masked_with_chars']))
print("\nMasked with fixed length chars")
print("-"*30)
print("\n".join(result['masked_fixed_length_chars']))
print("\nObfuscated")
print("-"*30)
print("\n".join(result['obfuscated']))
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = new PretrainedPipeline("clinical_deidentification","ar","clinical/models")

val text = '''

ملاحظات سريرية - مريض الربو:

التاريخ: 30 مايو 2023
اسم المريضة: ليلى حسن

تم تسجيل المريض في النظام باستخدام رقم الضمان الاجتماعي 123456789012.

العنوان: شارع المعرفة، مبنى رقم 789، حي الأمانة، جدة
الرمز البريدي: 54321
البلد: المملكة العربية السعودية
اسم المستشفى: مستشفى النور
اسم الطبيب: د. أميرة أحمد

تفاصيل الحالة:
المريضة ليلى حسن، البالغة من العمر 35 عامًا، تعاني من مرض الربو المزمن. تشكو من ضيق التنفس والسعال المتكرر والشهيق الشديد. تم تشخيصها بمرض الربو بناءً على تاريخها الطبي واختبارات وظائف الرئة.

الخطة:

تم وصف مضادات الالتهاب غير الستيرويدية والموسعات القصبية لتحسين التنفس وتقليل التهيج.
يجب على المريضة حمل معها جهاز الاستنشاق في حالة حدوث نوبة ربو حادة.
يتعين على المريضة تجنب التحسس من العوامل المسببة للربو، مثل الدخان والغبار والحيوانات الأليفة.
يجب مراقبة وظائف الرئة بانتظام ومتابعة التعليمات الطبية المتعلقة بمرض الربو.
تعليم المريضة بشأن كيفية استخدام جهاز الاستنشاق بشكل صحيح وتقنيات التنفس الصحيح

'''

val result = deid_pipeline.annotate(text)
```
</div>

## Results

```bash
Masked with entity labels
------------------------------
ملاحظات سريرية - مريض الربو:

التاريخ: [تاريخ] [تاريخ]
اسم المريضة: [المريض]
تم تسجيل المريض في النظام باستخدام رقم الضمان الاجتماعي [هاتف].
العنوان: شارع المعرفة، مبنى رقم [الرمز البريدي] حي [الموقع]
الرمز البريدي: [الرمز البريدي]
البلد: [المدينة] [البلد]
اسم المستشفى: [الموقع]
اسم الطبيب: د. [دكتور]
تفاصيل الحالة:
المريضة [المريض] حسن، البالغة من العمر [العمر]عامًا، تعاني من مرض الربو المزمن.
تشكو من ضيق التنفس والسعال المتكرر والشهيق الشديد.
تم تشخيصها بمرض الربو بناءً على تاريخها الطبي واختبارات وظائف الرئة.
الخطة:

تم وصف مضادات الالتهاب غير الستيرويدية والموسعات القصبية لتحسين التنفس وتقليل التهيج.
يجب على المريضة حمل معها جهاز الاستنشاق في حالة حدوث نوبة ربو حادة.
يتعين على المريضة تجنب التحسس من العوامل المسببة للربو، مثل الدخان والغبار والحيوانات الأليفة.
يجب مراقبة وظائف الرئة بانتظام ومتابعة التعليمات الطبية المتعلقة بمرض الربو.
تعليم المريضة بشأن كيفية استخدام جهاز الاستنشاق بشكل صحيح وتقنيات التنفس الصحيح

Masked with chars
------------------------------
ملاحظات سريرية - مريض الربو:

التاريخ: [٭٭٭٭٭] [٭٭]
اسم المريضة: [٭٭٭٭٭٭]
تم تسجيل المريض في النظام باستخدام رقم الضمان الاجتماعي [٭٭٭٭٭٭٭٭٭٭].
العنوان: شارع المعرفة، مبنى رقم [٭٭] حي [٭٭٭٭٭٭٭٭٭٭]
الرمز البريدي: [٭٭٭]
البلد: [٭٭٭٭٭٭٭٭٭٭٭٭٭] [٭٭٭٭٭٭]
اسم المستشفى: [٭٭٭٭٭٭٭٭٭٭]
اسم الطبيب: د. [٭٭٭٭٭٭٭٭]
تفاصيل الحالة:
المريضة [٭٭] حسن، البالغة من العمر ٭٭عامًا، تعاني من مرض الربو المزمن.
تشكو من ضيق التنفس والسعال المتكرر والشهيق الشديد.
تم تشخيصها بمرض الربو بناءً على تاريخها الطبي واختبارات وظائف الرئة.
الخطة:

تم وصف مضادات الالتهاب غير الستيرويدية والموسعات القصبية لتحسين التنفس وتقليل التهيج.
يجب على المريضة حمل معها جهاز الاستنشاق في حالة حدوث نوبة ربو حادة.
يتعين على المريضة تجنب التحسس من العوامل المسببة للربو، مثل الدخان والغبار والحيوانات الأليفة.
يجب مراقبة وظائف الرئة بانتظام ومتابعة التعليمات الطبية المتعلقة بمرض الربو.
تعليم المريضة بشأن كيفية استخدام جهاز الاستنشاق بشكل صحيح وتقنيات التنفس الصحيح

Masked with fixed length chars
------------------------------
ملاحظات سريرية - مريض الربو:

التاريخ: ٭٭٭٭ ٭٭٭٭
اسم المريضة: ٭٭٭٭
تم تسجيل المريض في النظام باستخدام رقم الضمان الاجتماعي ٭٭٭٭.
العنوان: شارع المعرفة، مبنى رقم ٭٭٭٭ حي ٭٭٭٭
الرمز البريدي: ٭٭٭٭
البلد: ٭٭٭٭ ٭٭٭٭
اسم المستشفى: ٭٭٭٭
اسم الطبيب: د. ٭٭٭٭
تفاصيل الحالة:
المريضة ٭٭٭٭ حسن، البالغة من العمر ٭٭٭٭عامًا، تعاني من مرض الربو المزمن.
تشكو من ضيق التنفس والسعال المتكرر والشهيق الشديد.
تم تشخيصها بمرض الربو بناءً على تاريخها الطبي واختبارات وظائف الرئة.
الخطة:

تم وصف مضادات الالتهاب غير الستيرويدية والموسعات القصبية لتحسين التنفس وتقليل التهيج.
يجب على المريضة حمل معها جهاز الاستنشاق في حالة حدوث نوبة ربو حادة.
يتعين على المريضة تجنب التحسس من العوامل المسببة للربو، مثل الدخان والغبار والحيوانات الأليفة.
يجب مراقبة وظائف الرئة بانتظام ومتابعة التعليمات الطبية المتعلقة بمرض الربو.
تعليم المريضة بشأن كيفية استخدام جهاز الاستنشاق بشكل صحيح وتقنيات التنفس الصحيح

Obfuscated
------------------------------
ملاحظات سريرية - مريض الربو:

التاريخ: 30 يونيو 2024
اسم المريضة: رياض حسيبي
تم تسجيل المريض في النظام باستخدام رقم الضمان الاجتماعي 217492240818.
العنوان: شارع المعرفة، مبنى رقم 616، حي شارع الحرية
الرمز البريدي: 32681
البلد: تاونات موريشيوس
اسم المستشفى: شارع الجزر الموريسية
اسم الطبيب: د. ميرا نورة
تفاصيل الحالة:
المريضة ربى شحاتة حسن، البالغة من العمر 26عامًا، تعاني من مرض الربو المزمن.
تشكو من ضيق التنفس والسعال المتكرر والشهيق الشديد.
تم تشخيصها بمرض الربو بناءً على تاريخها الطبي واختبارات وظائف الرئة.
الخطة:

تم وصف مضادات الالتهاب غير الستيرويدية والموسعات القصبية لتحسين التنفس وتقليل التهيج.
يجب على المريضة حمل معها جهاز الاستنشاق في حالة حدوث نوبة ربو حادة.
يتعين على المريضة تجنب التحسس من العوامل المسببة للربو، مثل الدخان والغبار والحيوانات الأليفة.
يجب مراقبة وظائف الرئة بانتظام ومتابعة التعليمات الطبية المتعلقة بمرض الربو.
تعليم المريضة بشأن كيفية استخدام جهاز الاستنشاق بشكل صحيح وتقنيات التنفس الصحيح
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|ar|
|Size:|1.3 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- ChunkMergeModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ChunkMergeModel
- DeIdentificationModel
- DeIdentificationModel
- DeIdentificationModel
- DeIdentificationModel
- Finisher