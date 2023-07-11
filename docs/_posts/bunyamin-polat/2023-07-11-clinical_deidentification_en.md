---
layout: model
title: Clinical Deidentification
author: John Snow Labs
name: clinical_deidentification
date: 2023-07-11
tags: [deidentification, deid, en, licensed, clinical, pipeline]
task: De-identification
language: en
edition: Healthcare NLP 5.0.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to deidentify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text. The pipeline can mask and obfuscate `AGE`, `CONTACT`, `DATE`, `ID`, `LOCATION`, `NAME`, `PROFESSION`, `CITY`, `COUNTRY`, `DOCTOR`, `HOSPITAL`, `IDNUM`, `MEDICALRECORD`, `ORGANIZATION`, `PATIENT`, `PHONE`, `PROFESSION`,  `STREET`, `USERNAME`, `ZIP`, `ACCOUNT`, `LICENSE`, `VIN`, `SSN`, `DLN`, `PLATE`, `IPADDR` entities.

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/DEID_PHI_TEXT_MULTI/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/DEID_PHI_TEXT_MULTI.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_en_5.0.0_3.0_1689070635933.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_en_5.0.0_3.0_1689070635933.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification", "en", "clinical/models")

deid_pipeline.annotate("""Record date : 2093-01-13, Name : Hendrickson, ORA, 25 years-old, #719435. IP: 203.120.223.13, the driver's license no:A334455B. The SSN: 324598674 and e-mail: hale@gmail.com. Patient's VIN : 1HGBH41JXMN109286. Date : 01/13/93, PCP : David Hale.""")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = PretrainedPipeline("clinical_deidentification", "en", "clinical/models")

val result = deid_pipeline.annotate("""Record date : 2093-01-13, Name : Hendrickson, ORA, 25 years-old, #719435. IP: 203.120.223.13, the driver's license no:A334455B. The SSN: 324598674 and e-mail: hale@gmail.com. Patient's VIN : 1HGBH41JXMN109286. Date : 01/13/93, PCP : David Hale.""")
```
</div>

## Results

```bash
{'masked': ['Record date : <DATE>, Name : <PATIENT>, <AGE> years-old, <MEDICALRECORD>.',
  "IP: <IPADDR>, the driver's license <DLN>.",
  'The SSN: <SSN> and e-mail: <EMAIL>.',
  "Patient's VIN : <VIN>.",
  'Date : <DATE>, PCP : <DOCTOR>.'],
 'obfuscated': ['Record date : 2093-02-25, Name : Albertine Grates, 30 years-old, #100581.',
  "IP: 003.003.003.003, the driver's license EL:I131599D.",
  'The SSN: 060014689 and e-mail: Tory@yahoo.com.',
  "Patient's VIN : 8JFSU78UTYV898505.",
  'Date : 02/25/93, PCP : Elvera Maria.'],
 'ner_chunk': ['2093-01-13',
  'Hendrickson, ORA',
  '25',
  '#719435',
  '203.120.223.13',
  'no:A334455B',
  '324598674',
  'hale@gmail.com',
  '1HGBH41JXMN109286',
  '01/13/93',
  'David Hale'],
 'masked_fixed_length_chars': ['Record date : ****, Name : ****, **** years-old, ****.',
  "IP: ****, the driver's license ****.",
  'The SSN: **** and e-mail: ****.',
  "Patient's VIN : ****.",
  'Date : ****, PCP : ****.'],
 'sentence': ['Record date : 2093-01-13, Name : Hendrickson, ORA, 25 years-old, #719435.',
  "IP: 203.120.223.13, the driver's license no:A334455B.",
  'The SSN: 324598674 and e-mail: hale@gmail.com.',
  "Patient's VIN : 1HGBH41JXMN109286.",
  'Date : 01/13/93, PCP : David Hale.'],
 'masked_with_chars': ['Record date : [********], Name : [**************], ** years-old, [*****].',
  "IP: [************], the driver's license [*********].",
  'The SSN: [*******] and e-mail: [************].',
  "Patient's VIN : [***************].",
  'Date : [******], PCP : [********].']}
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.0.0+|
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
- MedicalNerModel
- NerConverter
- ChunkMergeModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- TextMatcherModel
- ContextualParserModel
- RegexMatcherModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ChunkMergeModel
- ChunkMergeModel
- DeIdentificationModel
- DeIdentificationModel
- DeIdentificationModel
- DeIdentificationModel
- Finisher
