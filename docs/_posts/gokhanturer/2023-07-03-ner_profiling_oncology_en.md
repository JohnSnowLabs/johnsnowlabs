---
layout: model
title: Named Entity Recognition Profiling (Oncology)
author: John Snow Labs
name: ner_profiling_oncology
date: 2023-07-03
tags: [licensed, en, clinical, profiling, ner_profiling, ner, oncology]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to explore all the available pretrained NER models at once for Oncology. When you run this pipeline over your text, you will end up with the predictions coming out of each pretrained clinical NER model trained with `embeddings_clinical`.

Here are the NER models that this pretrained pipeline includes:

`ner_oncology_unspecific_posology`, `ner_oncology_tnm`, `ner_oncology_therapy`, `ner_oncology_test`, `ner_oncology_response_to_treatment`, `ner_oncology_posology`, `ner_oncology`, `ner_oncology_limited_80p_for_benchmarks`, `ner_oncology_diagnosis`, `ner_oncology_demographics`, `ner_oncology_biomarker`, `ner_oncology_anatomy_granular`, `ner_oncology_anatomy_general`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_profiling_oncology_en_4.4.4_3.4_1688357446065.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_profiling_oncology_en_4.4.4_3.4_1688357446065.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_profiling_pipeline = PretrainedPipeline("ner_profiling_oncology", 'en', 'clinical/models')

result = ner_profiling_pipeline.annotate("""The had previously undergone a left mastectomy and an axillary lymph node dissection for a left breast cancer twenty years ago.
The tumor was positive for ER and PR. Postoperatively, radiotherapy was administered to the residual breast.
The cancer recurred as a right lung metastasis 13 years later. He underwent a regimen consisting of adriamycin (60 mg/m2) and cyclophosphamide (600 mg/m2) over six courses, as first line therapy.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_profiling_pipeline = PretrainedPipeline("ner_profiling_oncology", "en", "clinical/models")

val result = ner_profiling_pipeline.annotate("""The had previously undergone a left mastectomy and an axillary lymph node dissection for a left breast cancer twenty years ago.
The tumor was positive for ER and PR. Postoperatively, radiotherapy was administered to the residual breast.
The cancer recurred as a right lung metastasis 13 years later. He underwent a regimen consisting of adriamycin (60 mg/m2) and cyclophosphamide (600 mg/m2) over six courses, as first line therapy.""")

```
</div>

## Results

```bash
 
 ******************** ner_oncology Model Results ******************** 

[('left', 'B-Direction'), ('mastectomy', 'B-Cancer_Surgery'), ('axillary', 'B-Cancer_Surgery'), ('lymph', 'I-Cancer_Surgery'), ('node', 'I-Cancer_Surgery'), ('dissection', 'I-Cancer_Surgery'), ('left', 'B-Direction'), ('breast', 'B-Cancer_Dx'), ('cancer', 'I-Cancer_Dx'), ('twenty', 'B-Relative_Date'), ('years', 'I-Relative_Date'), ('ago', 'I-Relative_Date'), ('tumor', 'B-Tumor_Finding'), ('positive', 'B-Biomarker_Result'), ('ER', 'B-Biomarker'), ('PR', 'B-Biomarker'), ('radiotherapy', 'B-Radiotherapy'), ('breast', 'B-Site_Breast'), ('cancer', 'B-Cancer_Dx'), ('recurred', 'B-Response_To_Treatment'), ('right', 'B-Direction'), ('lung', 'B-Site_Lung'), ('metastasis', 'B-Metastasis'), ('13', 'B-Relative_Date'), ('years', 'I-Relative_Date'), ('later', 'I-Relative_Date'), ('He', 'B-Gender'), ('adriamycin', 'B-Chemotherapy'), ('60', 'B-Dosage'), ('mg/m2', 'I-Dosage'), ('cyclophosphamide', 'B-Chemotherapy'), ('600', 'B-Dosage'), ('mg/m2', 'I-Dosage'), ('six', 'B-Cycle_Count'), ('courses', 'I-Cycle_Count'), ('first', 'B-Line_Of_Therapy'), ('line', 'I-Line_Of_Therapy')]

 
 ******************** ner_oncology_anatomy_general Model Results ******************** 

[('left', 'B-Direction'), ('left', 'B-Direction'), ('breast', 'B-Anatomical_Site'), ('right', 'B-Direction'), ('lung', 'B-Anatomical_Site')]

 
 ******************** ner_oncology_biomarker Model Results ******************** 

[('positive', 'B-Biomarker_Result'), ('ER', 'B-Biomarker'), ('PR', 'B-Biomarker')]

 
 ******************** ner_oncology_test Model Results ******************** 

[('positive', 'B-Biomarker_Result'), ('ER', 'B-Biomarker'), ('PR', 'B-Biomarker')]

 
 ******************** ner_oncology_response_to_treatment Model Results ******************** 

[('recurred', 'B-Response_To_Treatment'), ('first', 'B-Line_Of_Therapy'), ('line', 'I-Line_Of_Therapy')]


 ******************** ner_oncology_anatomy_granular Model Results ******************** 

[('left', 'B-Direction'), ('left', 'B-Direction'), ('breast', 'B-Site_Breast'), ('right', 'B-Direction'), ('lung', 'B-Site_Lung')]

 
 ******************** ner_oncology_therapy Model Results ******************** 

[('mastectomy', 'B-Cancer_Surgery'), ('axillary', 'B-Cancer_Surgery'), ('lymph', 'I-Cancer_Surgery'), ('node', 'I-Cancer_Surgery'), ('dissection', 'I-Cancer_Surgery'), ('radiotherapy', 'B-Radiotherapy'), ('recurred', 'B-Response_To_Treatment'), ('adriamycin', 'B-Chemotherapy'), ('60', 'B-Dosage'), ('mg/m2', 'I-Dosage'), ('cyclophosphamide', 'B-Chemotherapy'), ('600', 'B-Dosage'), ('mg/m2', 'I-Dosage'), ('six', 'B-Cycle_Count'), ('courses', 'I-Cycle_Count'), ('first', 'B-Line_Of_Therapy'), ('line', 'I-Line_Of_Therapy')]


 ******************** ner_oncology_demographics Model Results ******************** 

[('He', 'B-Gender')]

 
 ******************** ner_oncology_diagnosis Model Results ******************** 

[('breast', 'B-Cancer_Dx'), ('cancer', 'I-Cancer_Dx'), ('tumor', 'B-Tumor_Finding'), ('cancer', 'B-Cancer_Dx'), ('metastasis', 'B-Metastasis')]

 
 ******************** ner_oncology_limited_80p_for_benchmarks Model Results ******************** 

[('left', 'B-Direction'), ('mastectomy', 'B-Cancer_Surgery'), ('axillary', 'B-Cancer_Surgery'), ('lymph', 'I-Cancer_Surgery'), ('node', 'I-Cancer_Surgery'), ('dissection', 'I-Cancer_Surgery'), ('left', 'B-Direction'), ('breast', 'B-Cancer_Dx'), ('cancer', 'I-Cancer_Dx'), ('twenty', 'B-Relative_Date'), ('years', 'I-Relative_Date'), ('ago', 'I-Relative_Date'), ('tumor', 'B-Tumor_Finding'), ('positive', 'B-Biomarker_Result'), ('ER', 'B-Biomarker'), ('PR', 'B-Biomarker'), ('radiotherapy', 'B-Radiotherapy'), ('breast', 'B-Site_Breast'), ('cancer', 'B-Cancer_Dx'), ('recurred', 'B-Response_To_Treatment'), ('right', 'B-Direction'), ('lung', 'B-Site_Lung'), ('metastasis', 'B-Metastasis'), ('13', 'B-Relative_Date'), ('years', 'I-Relative_Date'), ('later', 'I-Relative_Date'), ('He', 'B-Gender'), ('adriamycin', 'B-Chemotherapy'), ('60', 'B-Dosage'), ('mg/m2', 'I-Dosage'), ('cyclophosphamide', 'B-Chemotherapy'), ('600', 'B-Dosage'), ('mg/m2', 'I-Dosage'), ('six', 'B-Cycle_Count'), ('courses', 'I-Cycle_Count'), ('first', 'B-Line_Of_Therapy'), ('line', 'I-Line_Of_Therapy')]


 ******************** ner_oncology_tnm Model Results ******************** 

[('breast', 'B-Cancer_Dx'), ('cancer', 'I-Cancer_Dx'), ('tumor', 'B-Tumor'), ('cancer', 'B-Cancer_Dx'), ('metastasis', 'B-Metastasis')]

 
 ******************** ner_oncology_unspecific_posology Model Results ******************** 

[('mastectomy', 'B-Cancer_Therapy'), ('axillary', 'B-Cancer_Therapy'), ('lymph', 'I-Cancer_Therapy'), ('node', 'I-Cancer_Therapy'), ('dissection', 'I-Cancer_Therapy'), ('radiotherapy', 'B-Cancer_Therapy'), ('adriamycin', 'B-Cancer_Therapy'), ('60', 'B-Posology_Information'), ('mg/m2', 'I-Posology_Information'), ('cyclophosphamide', 'B-Cancer_Therapy'), ('600', 'B-Posology_Information'), ('mg/m2', 'I-Posology_Information'), ('six', 'B-Posology_Information'), ('courses', 'I-Posology_Information')]

 
 ******************** ner_oncology_posology Model Results ******************** 

[('mastectomy', 'B-Cancer_Surgery'), ('axillary', 'B-Cancer_Surgery'), ('lymph', 'I-Cancer_Surgery'), ('node', 'I-Cancer_Surgery'), ('dissection', 'I-Cancer_Surgery'), ('radiotherapy', 'B-Radiotherapy'), ('adriamycin', 'B-Cancer_Therapy'), ('60', 'B-Dosage'), ('mg/m2', 'I-Dosage'), ('cyclophosphamide', 'B-Cancer_Therapy'), ('600', 'B-Dosage'), ('mg/m2', 'I-Dosage'), ('six', 'B-Cycle_Count'), ('courses', 'I-Cycle_Count')]

 
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_profiling_oncology|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.1 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel