---
layout: model
title: PDF Obfuscation Multi Model Context
author: John Snow Labs
name: pdf_obfuscation_multi_model_context_pipeline
date: 2025-05-09
tags: [en, licensed]
task: De-identification
language: en
edition: Healthcare NLP 6.0.0
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to mask PHI information in PDFs. Masked entities include 'AGE', 'CITY', 'COUNTRY', 'DATE', 'DOCTOR', 'EMAIL', 'HOSPITAL', 'IDNUM', 'ORGANIZATION', 'PATIENT', 'PHONE', 'PROFESSION', 'STATE', 'STREET', 'USERNAME', 'ZIP'.
The output is a PDF document, similar to the one at the input, but with fake obfuscated text on top of the targeted entities. 

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/pdf_obfuscation_multi_model_context_pipeline_en_6.0.0_3.0_1746699526000.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/pdf_obfuscation_multi_model_context_pipeline_en_6.0.0_3.0_1746699526000.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline
deid_pipeline = PretrainedPipeline("pdf_obfuscation_multi_model_context_pipeline", "en", "clinical/ocr")
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|pdf_obfuscation_multi_model_context_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|4.4 GB|

## Included Models

- PdfToImage
- ImageToText
- DocumentAssembler
- SentenceDetectorDLModel
- Regex
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- EntityExtractor
- ContextualParserModel
- RegexMatcher
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- RegexMatcher
- ChunkMergeModel
- ChunkMergeModel
- XLMRobertaEmbeddings
- MedicalNerModel
- NerConverter 
- PretrainedZeroShotNER
- NerConverter
- PretrainedZeroShotNER
- NerConverter
- ChunkMergeModel
- PositionFinder
- ImageDrawRegions
- ImageToPdf 