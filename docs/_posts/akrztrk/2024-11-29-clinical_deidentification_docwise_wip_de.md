---
layout: model
title: Clinical Deidentification Pipeline (German, Document Wise)
author: John Snow Labs
name: clinical_deidentification_docwise_wip
date: 2024-11-29
tags: [deidentification, deid, de, licensed, clinical, pipeline, docwise]
task: [De-identification, Pipeline Healthcare]
language: de
edition: Healthcare NLP 5.5.1
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to deidentify PHI information from medical texts in German language. The PHI information will be masked and obfuscated in the resulting text.
The pipeline can mask and obfuscate: `LOCATION`, `DATE`, `NAME`, `ID`, `AGE`, `PROFESSION`, `CONTACT`, `ORGANIZATION`, `DOCTOR`, `CITY`, `COUNTRY`, `STREET`, `PATIENT`, `PHONE`, `HOSPITAL`, `STATE`, `DLN`, `SSN`, `ZIP`, `ACCOUNT`, `LICENSE`, `PLATE`, `VIN`, `MEDICALRECORD`, `EMAIL`, `URL` entities.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_docwise_wip_de_5.5.1_3.0_1732886237933.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_docwise_wip_de_5.5.1_3.0_1732886237933.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python


from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification_docwise_wip", "de", "clinical/models")

text = """Sehr geehrter Herr Schmidt, bezüglich Ihrer Anfrage vom 15.03.2024 für Ihre Krankenakte 341123 möchte ich bestätigen, dass Ihre Sozialversicherungsnummer 13110587M565 und Ihre Versichertennummer T0110053F5D korrekt in unserem System hinterlegt sind. Ihr Fahrzeug mit dem Kennzeichen M-AB 1234 ist bereits registriert. Falls Sie Fragen haben, erreichen Sie uns unter +49 89 12345678 oder schreiben Sie an support@beispiel.de. Unsere Details finden Sie auch unter https://www.beispiel-behoerde.de. Für Ihre Bankgeschäfte nutzen Sie weiterhin das Konto DE89 3704 0044 0532 0130 00."""

deid_result = deid_pipeline.fullAnnotate(text)

print(''.join([i.result for i in deid_result[0]['document']]))
print(''.join([i.result for i in deid_result[0]['masked']]))
print(''.join([i.result for i in deid_result[0]['obfuscated']]))


```
```scala


import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("clinical_deidentification_docwise_wip", "de", "clinical/models")

val text = """Sehr geehrter Herr Schmidt, bezüglich Ihrer Anfrage vom 15.03.2024 für Ihre Krankenakte 341123 möchte ich bestätigen, dass Ihre Sozialversicherungsnummer 13110587M565 und Ihre Versichertennummer T0110053F5D korrekt in unserem System hinterlegt sind. Ihr Fahrzeug mit dem Kennzeichen M-AB 1234 ist bereits registriert. Falls Sie Fragen haben, erreichen Sie uns unter +49 89 12345678 oder schreiben Sie an support@beispiel.de. Unsere Details finden Sie auch unter https://www.beispiel-behoerde.de. Für Ihre Bankgeschäfte nutzen Sie weiterhin das Konto DE89 3704 0044 0532 0130 00."""

val deid_result = deid_pipeline.fullAnnotate(text)

println(deid_result(0)("document").map(_("result").toString).mkString(""))
println(deid_result(0)("masked").map(_("result").toString).mkString(""))
println(deid_result(0)("obfuscated").map(_("result").toString).mkString(""))


```
</div>

## Results

```bash

Sehr geehrter Herr Schmidt, bezüglich Ihrer Anfrage vom 15.03.2024 für Ihre Krankenakte 341123 möchte ich bestätigen, dass Ihre Sozialversicherungsnummer 13110587M565 und Ihre Versichertennummer T0110053F5D korrekt in unserem System hinterlegt sind. Ihr Fahrzeug mit dem Kennzeichen M-AB 1234 ist bereits registriert. Falls Sie Fragen haben, erreichen Sie uns unter +49 89 12345678 oder schreiben Sie an support@beispiel.de. Unsere Details finden Sie auch unter https://www.beispiel-behoerde.de. Für Ihre Bankgeschäfte nutzen Sie weiterhin das Konto DE89 3704 0044 0532 0130 00.
-------------MASKED------------
Sehr geehrter Herr <NAME>, bezüglich Ihrer Anfrage vom <DATE> für Ihre Krankenakte <MEDICALRECORD> möchte ich bestätigen, dass Ihre Sozialversicherungsnummer <SSN> und Ihre Versichertennummer <ID> korrekt in unserem System hinterlegt sind. Ihr Fahrzeug mit dem Kennzeichen <PLATE> ist bereits registriert. Falls Sie Fragen haben, erreichen Sie uns unter <PHONE> oder schreiben Sie an <EMAIL>. Unsere Details finden Sie auch unter <URL>. Für Ihre Bankgeschäfte nutzen Sie weiterhin das Konto <ACCOUNT>.
-------------OBFUSCATED-----------
Sehr geehrter Herr Johan, bezüglich Ihrer Anfrage vom 14.05.2024 für Ihre Krankenakte 149921 möchte ich bestätigen, dass Ihre Sozialversicherungsnummer 68667052J030und Ihre Versichertennummer C1001142Q4S korrekt in unserem System hinterlegt sind. Ihr Fahrzeug mit dem Kennzeichen L-PM 6981 ist bereits registriert. Falls Sie Fragen haben, erreichen Sie uns unter +81 21 36587092 oder schreiben Sie an Aeron@google.com. Unsere Details finden Sie auch unter PoliticalMakeover.com.ee. Für Ihre Bankgeschäfte nutzen Sie weiterhin das Konto IJ32 6059 5599 5867 5465 55.


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification_docwise_wip|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|de|
|Size:|1.3 GB|

## Included Models

- DocumentAssembler
- InternalDocumentSplitter
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- RegexMatcherInternalModel
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
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- TextMatcherInternalModel
- TextMatcherInternalModel
- TextMatcherInternalModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- RegexMatcherModel
- RegexMatcherModel
- RegexMatcherModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ChunkMergeModel
- ChunkMergeModel
- ChunkMergeModel
- ChunkMergeModel
- ChunkMergeModel
- ChunkFilterer
- LightDeIdentification
- LightDeIdentification