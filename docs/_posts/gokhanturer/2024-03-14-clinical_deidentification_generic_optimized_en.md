---
layout: model
title: Clinical Deidentification Pipeline Optimized Version (English - Generic)
author: John Snow Labs
name: clinical_deidentification_generic_optimized
date: 2024-03-14
tags: [deidentification, optimized, en, licensed, clinical, pipeline, obfuscation, mask]
task: [De-identification, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.3.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to de-identify PHI information from medical texts. The PHI information will be obfuscated in the resulting text and masked with entity labels in the metadata. The pipeline can obfuscate and mask `AGE`, `CONTACT`, `DATE`, `LOCATION`, `COUNTRY`, `NAME`, `PROFESSION`, `ID`, `MEDICALRECORD`, `PHONE`, `ZIP`, `ACCOUNT`, `LICENSE`, `VIN`, `SSN`, `DLN`, `PLATE` entities. This pipeline is built using the `ner_deid_generic_augmented` model, and `ContextualParser`, `RegexMatcher`, and `TextMatcher` and a single `Deidentification` stage for optimization.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_generic_optimized_en_5.3.0_3.0_1710410162844.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_generic_optimized_en_5.3.0_3.0_1710410162844.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification_generic_optimized", "en", "clinical/models")

text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR #719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com."""

deid_result = deid_pipeline.fullAnnotate(text)

print('\n'.join([i.metadata['masked'] for i in deid_result[0]['obfuscated']]))
print('\n'.join([i.result for i in deid_result[0]['obfuscated']]))
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("clinical_deidentification_generic_optimized", "en", "clinical/models")

val text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR #719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com."""

val deid_result = deid_pipeline.fullAnnotate(text)

println(deid_result(0)("obfuscated").map(_("metadata")("masked").toString).mkString("\n"))
println(deid_result(0)("obfuscated").map(_("result").toString).mkString("\n"))
```
</div>

## Results

```bash
Masked with entity labels
------------------------------
Name : <NAME>, Record date: <DATE>, MR <ID>.
Dr. <NAME>, ID: <ID>, IP <IPADDR>.
He is a <AGE>-year-old male was admitted to the <LOCATION> for cystectomy on <DATE>.
Patient's VIN : <VIN>, SSN <SSN>, Driver's license no: <DLN>.
Phone <PHONE>, <LOCATION>, <LOCATION>, E-MAIL: <EMAIL>.

Obfuscated
------------------------------
Name : Loleta Chance, Record date: 2093-02-14, MR #161096.
Dr. Vevelyn Pat, ID: 0454098119, IP 444.444.444.444.
He is a 70-year-old male was admitted to the 34 Maple St for cystectomy on 02/14/93.
Patient's VIN : 1YNWG95AOZH086578, SSN #469-62-9528, Driver's license no: U132440N.
Phone (027) 253-6644, 600 Elizabeth Street,Third Floor, 3500 East Frank Phillips Boulevard, E-MAIL: Ottilie@google.com.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification_generic_optimized|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- TextMatcherInternalModel
- ContextualParserModel
- RegexMatcherModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ChunkMergeModel
- ChunkMergeModel
- DeIdentificationModel
- Finisher
