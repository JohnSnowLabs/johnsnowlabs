---
layout: model
title: Clinical Deidentification Pipeline (Arabic-Enriched)
author: John Snow Labs
name: clinical_deidentification_subentity_enriched
date: 2025-03-13
tags: [deidentification, deid, ar, enriched, licensed, clinical, pipeline, subentity]
task: [De-identification, Pipeline Healthcare]
language: ar
edition: Healthcare NLP 5.5.3
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to deidentify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text.
The pipeline can mask and obfuscate `MEDICALRECORD`, `ORGANIZATION`, `PROFESSION`, `DOCTOR`, `USERNAME`, `URL`, `DEVICE`, `CITY`, `DATE`,
`ZIP`, `STATE`, `PATIENT`, `COUNTRY`, `STREET`, `PHONE`, `HOSPITAL`, `EMAIL`, `IDNUM`, `AGE`, `LOCATION`, `DLN`, `SSN`, `PLATE`, `VIN`, `LICENSE`, `IP`, `ACCOUNT` and `DOB`  entities.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_subentity_enriched_ar_5.5.3_3.2_1741884403147.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_subentity_enriched_ar_5.5.3_3.2_1741884403147.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification_subentity_enriched_ar", "ar", "clinical/models")

text = """الملاحظات السريرية - مريض السكري
تم تسجيل المريض في النظام باستخدام رقم الضمان الاجتماعي 123456789012.

رقم الجهاز: 356789012345678.

التاريخ: 11 مايو 1999
اسم المريض: فاطمة علي.
تاريخ الميلاد: 12 مايو.

العنوان: شارع الحرية، حي السلام، القاهرة
دولة: مصر
اسم المستشفى: مستشفى الشفاء
اسم الطبيب: د.محمد صلاح

البريد الإلكتروني: fatima.ali@example.com
الموقع الإلكتروني: https://hospital-alshifa.com
عنوان IP: 192.168.1.100"""

result = deid_pipeline.annotate(text)
print("
Masked with entity labels")
print("-"*30)
print("
".join(result['masked_with_entity']))
print("
Masked with chars")
print("-"*30)
print("
".join(result['masked_with_chars']))
print("
Masked with fixed length chars")
print("-"*30)
print("
".join(result['masked_fixed_length_chars']))
print("
Obfuscated")
print("-"*30)
print("
".join(result['obfuscated']))


```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("clinical_deidentification_subentity_enriched_ar", "ar", "clinical/models")

val text = """الملاحظات السريرية - مريض السكري
تم تسجيل المريض في النظام باستخدام رقم الضمان الاجتماعي 123456789012.

رقم الجهاز: 356789012345678.

التاريخ: 11 مايو 1999
اسم المريض: فاطمة علي.
تاريخ الميلاد: 12 مايو.

العنوان: شارع الحرية، حي السلام، القاهرة
دولة: مصر
اسم المستشفى: مستشفى الشفاء
اسم الطبيب: د.محمد صلاح

البريد الإلكتروني: fatima.ali@example.com
الموقع الإلكتروني: https://hospital-alshifa.com
عنوان IP: 192.168.1.100"""

val result = deid_pipeline.annotate(text)

println("
Masked with entity labels")
println("-" * 30)
println(result("masked_with_entity").mkString("
"))
println("
Masked with chars")
println("-" * 30)
println(result("masked_with_chars").mkString("
"))
println("
Masked with fixed length chars")
println("-" * 30)
println(result("masked_fixed_length_chars").mkString("
"))
println("
Obfuscated")
println("-" * 30)
println(result("obfuscated").mkString("
"))

```
</div>

## Results

```bash
Masked with entity labels
------------------------------
الملاحظات السريرية - مريض السكري
تم تسجيل المريض في النظام باستخدام رقم الضمان الاجتماعي [رقم الضمان الاجتماعي].
رقم الجهاز: [الجهاز].
التاريخ: [تاريخ]
اسم المريض: [المريض].
تاريخ الميلاد: [تاريخ].
العنوان: [مستشفى] حي السلام، [المدينة]
[البلد]: [البلد]
اسم المستشفى: مستشفى الشفاء
اسم الطبيب: [دكتور] [دكتور]
البريد الإلكتروني: [البريد الإلكتروني]
الموقع الإلكتروني: [عنوان الرابط]
عنوان IP: [بروتوكول الإنترنت]


Masked with chars
------------------------------
الملاحظات السريرية - مريض السكري
تم تسجيل المريض في النظام باستخدام رقم الضمان الاجتماعي [٭٭٭٭٭٭٭٭٭٭].
رقم الجهاز: [٭٭٭٭٭٭٭٭٭٭٭٭٭].
التاريخ: [٭٭٭٭٭٭٭٭٭٭]
اسم المريض: [٭٭٭٭٭٭٭].
تاريخ الميلاد: [٭٭٭٭٭].
العنوان: [٭٭٭٭٭٭٭٭٭٭] حي السلام، [٭٭٭٭٭]
[٭٭]: [٭]
اسم المستشفى: مستشفى الشفاء
اسم الطبيب: [٭٭٭٭] [٭٭]
البريد الإلكتروني: [٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭]
الموقع الإلكتروني: [٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭٭]
عنوان IP: [٭٭٭٭٭٭٭٭٭٭٭]


Masked with fixed length chars
------------------------------
الملاحظات السريرية - مريض السكري
تم تسجيل المريض في النظام باستخدام رقم الضمان الاجتماعي ٭٭٭٭.
رقم الجهاز: ٭٭٭٭.
التاريخ: ٭٭٭٭
اسم المريض: ٭٭٭٭.
تاريخ الميلاد: ٭٭٭٭.
العنوان: ٭٭٭٭ حي السلام، ٭٭٭٭
٭٭٭٭: ٭٭٭٭
اسم المستشفى: مستشفى الشفاء
اسم الطبيب: ٭٭٭٭ ٭٭٭٭
البريد الإلكتروني: ٭٭٭٭
الموقع الإلكتروني: ٭٭٭٭
عنوان IP: ٭٭٭٭

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification_subentity_enriched|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.3+|
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
- ContextualEntityRuler
- RegexMatcherModel
- RegexMatcherModel
- RegexMatcherModel
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
- ContextualParserModel
- ChunkConverter
- ContextualParserModel
- ChunkConverter
- ContextualParserModel
- ChunkConverter
- ChunkMergeModel
- DeIdentificationModel
- DeIdentificationModel
- DeIdentificationModel
- DeIdentificationModel
- Finisher