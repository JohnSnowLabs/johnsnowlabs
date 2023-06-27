---
layout: model
title: Named Entity Recognition Profiling (Oncology)
author: John Snow Labs
name: ner_profiling_oncology
date: 2023-06-27
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_profiling_oncology_en_4.4.4_3.4_1687833370996.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_profiling_oncology_en_4.4.4_3.4_1687833370996.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_profiling_pipeline = PretrainedPipeline("ner_profiling_oncology", 'en', 'clinical/models')

result = ner_profiling_pipeline.annotate("""The had previously undergone a left mastectomy and an axillary lymph node dissection for a left breast cancer twenty years ago.
The tumor was positive for ER and PR. Postoperatively, radiotherapy was administered to the residual breast.
The cancer recurred as a right lung metastasis 13 years later. The patient underwent a regimen consisting of adriamycin (60 mg/m2) and cyclophosphamide (600 mg/m2) over six courses, as first line therapy.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_profiling_pipeline = PretrainedPipeline("ner_profiling_oncology", "en", "clinical/models")

val result = ner_profiling_pipeline.annotate("""The had previously undergone a left mastectomy and an axillary lymph node dissection for a left breast cancer twenty years ago.
The tumor was positive for ER and PR. Postoperatively, radiotherapy was administered to the residual breast.
The cancer recurred as a right lung metastasis 13 years later. The patient underwent a regimen consisting of adriamycin (60 mg/m2) and cyclophosphamide (600 mg/m2) over six courses, as first line therapy.""")

```
</div>

## Results

```bash
 
 ******************** ner_oncology Model Results ******************** 

[('The', 'O'), ('had', 'O'), ('previously', 'O'), ('undergone', 'O'), ('a', 'O'), ('left', 'B-Direction'), ('mastectomy', 'B-Cancer_Surgery'), ('and', 'O'), ('an', 'O'), ('axillary', 'B-Cancer_Surgery'), ('lymph', 'I-Cancer_Surgery'), ('node', 'I-Cancer_Surgery'), ('dissection', 'I-Cancer_Surgery'), ('for', 'O'), ('a', 'O'), ('left', 'B-Direction'), ('breast', 'B-Cancer_Dx'), ('cancer', 'I-Cancer_Dx'), ('twenty', 'B-Relative_Date'), ('years', 'I-Relative_Date'), ('ago', 'I-Relative_Date'), ('.', 'O'), ('The', 'O'), ('tumor', 'B-Tumor_Finding'), ('was', 'O'), ('positive', 'B-Biomarker_Result'), ('for', 'O'), ('ER', 'B-Biomarker'), ('and', 'O'), ('PR', 'B-Biomarker'), ('.', 'O'), ('Postoperatively', 'O'), (',', 'O'), ('radiotherapy', 'B-Radiotherapy'), ('was', 'O'), ('administered', 'O'), ('to', 'O'), ('the', 'O'), ('residual', 'O'), ('breast', 'B-Site_Breast'), ('.', 'O'), ('The', 'O'), ('cancer', 'B-Cancer_Dx'), ('recurred', 'B-Response_To_Treatment'), ('as', 'O'), ('a', 'O'), ('right', 'B-Direction'), ('lung', 'B-Site_Lung'), ('metastasis', 'B-Metastasis'), ('13', 'B-Relative_Date'), ('years', 'I-Relative_Date'), ('later', 'I-Relative_Date'), ('.', 'O'), ('The', 'O'), ('patient', 'O'), ('underwent', 'O'), ('a', 'O'), ('regimen', 'O'), ('consisting', 'O'), ('of', 'O'), ('adriamycin', 'B-Chemotherapy'), ('(', 'O'), ('60', 'B-Dosage'), ('mg/m2', 'I-Dosage'), (')', 'O'), ('and', 'O'), ('cyclophosphamide', 'B-Chemotherapy'), ('(', 'O'), ('600', 'B-Dosage'), ('mg/m2', 'I-Dosage'), (')', 'O'), ('over', 'O'), ('six', 'B-Cycle_Count'), ('courses', 'I-Cycle_Count'), (',', 'O'), ('as', 'O'), ('first', 'B-Line_Of_Therapy'), ('line', 'I-Line_Of_Therapy'), ('therapy', 'O'), ('.', 'O')]

 
 ******************** ner_oncology_anatomy_general Model Results ******************** 

[('The', 'O'), ('had', 'O'), ('previously', 'O'), ('undergone', 'O'), ('a', 'O'), ('left', 'B-Direction'), ('mastectomy', 'O'), ('and', 'O'), ('an', 'O'), ('axillary', 'O'), ('lymph', 'O'), ('node', 'O'), ('dissection', 'O'), ('for', 'O'), ('a', 'O'), ('left', 'B-Direction'), ('breast', 'O'), ('cancer', 'O'), ('twenty', 'O'), ('years', 'O'), ('ago', 'O'), ('.', 'O'), ('The', 'O'), ('tumor', 'O'), ('was', 'O'), ('positive', 'O'), ('for', 'O'), ('ER', 'O'), ('and', 'O'), ('PR', 'O'), ('.', 'O'), ('Postoperatively', 'O'), (',', 'O'), ('radiotherapy', 'O'), ('was', 'O'), ('administered', 'O'), ('to', 'O'), ('the', 'O'), ('residual', 'O'), ('breast', 'B-Anatomical_Site'), ('.', 'O'), ('The', 'O'), ('cancer', 'O'), ('recurred', 'O'), ('as', 'O'), ('a', 'O'), ('right', 'B-Direction'), ('lung', 'B-Anatomical_Site'), ('metastasis', 'O'), ('13', 'O'), ('years', 'O'), ('later', 'O'), ('.', 'O'), ('The', 'O'), ('patient', 'O'), ('underwent', 'O'), ('a', 'O'), ('regimen', 'O'), ('consisting', 'O'), ('of', 'O'), ('adriamycin', 'O'), ('(', 'O'), ('60', 'O'), ('mg/m2', 'O'), (')', 'O'), ('and', 'O'), ('cyclophosphamide', 'O'), ('(', 'O'), ('600', 'O'), ('mg/m2', 'O'), (')', 'O'), ('over', 'O'), ('six', 'O'), ('courses', 'O'), (',', 'O'), ('as', 'O'), ('first', 'O'), ('line', 'O'), ('therapy', 'O'), ('.', 'O')]

 
 ******************** ner_oncology_biomarker Model Results ******************** 

[('The', 'O'), ('had', 'O'), ('previously', 'O'), ('undergone', 'O'), ('a', 'O'), ('left', 'O'), ('mastectomy', 'O'), ('and', 'O'), ('an', 'O'), ('axillary', 'O'), ('lymph', 'O'), ('node', 'O'), ('dissection', 'O'), ('for', 'O'), ('a', 'O'), ('left', 'O'), ('breast', 'O'), ('cancer', 'O'), ('twenty', 'O'), ('years', 'O'), ('ago', 'O'), ('.', 'O'), ('The', 'O'), ('tumor', 'O'), ('was', 'O'), ('positive', 'B-Biomarker_Result'), ('for', 'O'), ('ER', 'B-Biomarker'), ('and', 'O'), ('PR', 'B-Biomarker'), ('.', 'O'), ('Postoperatively', 'O'), (',', 'O'), ('radiotherapy', 'O'), ('was', 'O'), ('administered', 'O'), ('to', 'O'), ('the', 'O'), ('residual', 'O'), ('breast', 'O'), ('.', 'O'), ('The', 'O'), ('cancer', 'O'), ('recurred', 'O'), ('as', 'O'), ('a', 'O'), ('right', 'O'), ('lung', 'O'), ('metastasis', 'O'), ('13', 'O'), ('years', 'O'), ('later', 'O'), ('.', 'O'), ('The', 'O'), ('patient', 'O'), ('underwent', 'O'), ('a', 'O'), ('regimen', 'O'), ('consisting', 'O'), ('of', 'O'), ('adriamycin', 'O'), ('(', 'O'), ('60', 'O'), ('mg/m2', 'O'), (')', 'O'), ('and', 'O'), ('cyclophosphamide', 'O'), ('(', 'O'), ('600', 'O'), ('mg/m2', 'O'), (')', 'O'), ('over', 'O'), ('six', 'O'), ('courses', 'O'), (',', 'O'), ('as', 'O'), ('first', 'O'), ('line', 'O'), ('therapy', 'O'), ('.', 'O')]

 
 ******************** ner_oncology_test Model Results ******************** 

[('The', 'O'), ('had', 'O'), ('previously', 'O'), ('undergone', 'O'), ('a', 'O'), ('left', 'O'), ('mastectomy', 'O'), ('and', 'O'), ('an', 'O'), ('axillary', 'O'), ('lymph', 'O'), ('node', 'O'), ('dissection', 'O'), ('for', 'O'), ('a', 'O'), ('left', 'O'), ('breast', 'O'), ('cancer', 'O'), ('twenty', 'O'), ('years', 'O'), ('ago', 'O'), ('.', 'O'), ('The', 'O'), ('tumor', 'O'), ('was', 'O'), ('positive', 'B-Biomarker_Result'), ('for', 'O'), ('ER', 'B-Biomarker'), ('and', 'O'), ('PR', 'B-Biomarker'), ('.', 'O'), ('Postoperatively', 'O'), (',', 'O'), ('radiotherapy', 'O'), ('was', 'O'), ('administered', 'O'), ('to', 'O'), ('the', 'O'), ('residual', 'O'), ('breast', 'O'), ('.', 'O'), ('The', 'O'), ('cancer', 'O'), ('recurred', 'O'), ('as', 'O'), ('a', 'O'), ('right', 'O'), ('lung', 'O'), ('metastasis', 'O'), ('13', 'O'), ('years', 'O'), ('later', 'O'), ('.', 'O'), ('The', 'O'), ('patient', 'O'), ('underwent', 'O'), ('a', 'O'), ('regimen', 'O'), ('consisting', 'O'), ('of', 'O'), ('adriamycin', 'O'), ('(', 'O'), ('60', 'O'), ('mg/m2', 'O'), (')', 'O'), ('and', 'O'), ('cyclophosphamide', 'O'), ('(', 'O'), ('600', 'O'), ('mg/m2', 'O'), (')', 'O'), ('over', 'O'), ('six', 'O'), ('courses', 'O'), (',', 'O'), ('as', 'O'), ('first', 'O'), ('line', 'O'), ('therapy', 'O'), ('.', 'O')]

 
 ******************** ner_oncology_response_to_treatment Model Results ******************** 

[('The', 'O'), ('had', 'O'), ('previously', 'O'), ('undergone', 'O'), ('a', 'O'), ('left', 'O'), ('mastectomy', 'O'), ('and', 'O'), ('an', 'O'), ('axillary', 'O'), ('lymph', 'O'), ('node', 'O'), ('dissection', 'O'), ('for', 'O'), ('a', 'O'), ('left', 'O'), ('breast', 'O'), ('cancer', 'O'), ('twenty', 'O'), ('years', 'O'), ('ago', 'O'), ('.', 'O'), ('The', 'O'), ('tumor', 'O'), ('was', 'O'), ('positive', 'O'), ('for', 'O'), ('ER', 'O'), ('and', 'O'), ('PR', 'O'), ('.', 'O'), ('Postoperatively', 'O'), (',', 'O'), ('radiotherapy', 'O'), ('was', 'O'), ('administered', 'O'), ('to', 'O'), ('the', 'O'), ('residual', 'O'), ('breast', 'O'), ('.', 'O'), ('The', 'O'), ('cancer', 'O'), ('recurred', 'B-Response_To_Treatment'), ('as', 'O'), ('a', 'O'), ('right', 'O'), ('lung', 'O'), ('metastasis', 'O'), ('13', 'O'), ('years', 'O'), ('later', 'O'), ('.', 'O'), ('The', 'O'), ('patient', 'O'), ('underwent', 'O'), ('a', 'O'), ('regimen', 'O'), ('consisting', 'O'), ('of', 'O'), ('adriamycin', 'O'), ('(', 'O'), ('60', 'O'), ('mg/m2', 'O'), (')', 'O'), ('and', 'O'), ('cyclophosphamide', 'O'), ('(', 'O'), ('600', 'O'), ('mg/m2', 'O'), (')', 'O'), ('over', 'O'), ('six', 'O'), ('courses', 'O'), (',', 'O'), ('as', 'O'), ('first', 'B-Line_Of_Therapy'), ('line', 'I-Line_Of_Therapy'), ('therapy', 'O'), ('.', 'O')]

 
 ******************** ner_oncology_anatomy_granular Model Results ******************** 

[('The', 'O'), ('had', 'O'), ('previously', 'O'), ('undergone', 'O'), ('a', 'O'), ('left', 'B-Direction'), ('mastectomy', 'O'), ('and', 'O'), ('an', 'O'), ('axillary', 'O'), ('lymph', 'O'), ('node', 'O'), ('dissection', 'O'), ('for', 'O'), ('a', 'O'), ('left', 'B-Direction'), ('breast', 'O'), ('cancer', 'O'), ('twenty', 'O'), ('years', 'O'), ('ago', 'O'), ('.', 'O'), ('The', 'O'), ('tumor', 'O'), ('was', 'O'), ('positive', 'O'), ('for', 'O'), ('ER', 'O'), ('and', 'O'), ('PR', 'O'), ('.', 'O'), ('Postoperatively', 'O'), (',', 'O'), ('radiotherapy', 'O'), ('was', 'O'), ('administered', 'O'), ('to', 'O'), ('the', 'O'), ('residual', 'O'), ('breast', 'B-Site_Breast'), ('.', 'O'), ('The', 'O'), ('cancer', 'O'), ('recurred', 'O'), ('as', 'O'), ('a', 'O'), ('right', 'B-Direction'), ('lung', 'B-Site_Lung'), ('metastasis', 'O'), ('13', 'O'), ('years', 'O'), ('later', 'O'), ('.', 'O'), ('The', 'O'), ('patient', 'O'), ('underwent', 'O'), ('a', 'O'), ('regimen', 'O'), ('consisting', 'O'), ('of', 'O'), ('adriamycin', 'O'), ('(', 'O'), ('60', 'O'), ('mg/m2', 'O'), (')', 'O'), ('and', 'O'), ('cyclophosphamide', 'O'), ('(', 'O'), ('600', 'O'), ('mg/m2', 'O'), (')', 'O'), ('over', 'O'), ('six', 'O'), ('courses', 'O'), (',', 'O'), ('as', 'O'), ('first', 'O'), ('line', 'O'), ('therapy', 'O'), ('.', 'O')]

 
 ******************** ner_oncology_therapy Model Results ******************** 

[('The', 'O'), ('had', 'O'), ('previously', 'O'), ('undergone', 'O'), ('a', 'O'), ('left', 'O'), ('mastectomy', 'B-Cancer_Surgery'), ('and', 'O'), ('an', 'O'), ('axillary', 'B-Cancer_Surgery'), ('lymph', 'I-Cancer_Surgery'), ('node', 'I-Cancer_Surgery'), ('dissection', 'I-Cancer_Surgery'), ('for', 'O'), ('a', 'O'), ('left', 'O'), ('breast', 'O'), ('cancer', 'O'), ('twenty', 'O'), ('years', 'O'), ('ago', 'O'), ('.', 'O'), ('The', 'O'), ('tumor', 'O'), ('was', 'O'), ('positive', 'O'), ('for', 'O'), ('ER', 'O'), ('and', 'O'), ('PR', 'O'), ('.', 'O'), ('Postoperatively', 'O'), (',', 'O'), ('radiotherapy', 'B-Radiotherapy'), ('was', 'O'), ('administered', 'O'), ('to', 'O'), ('the', 'O'), ('residual', 'O'), ('breast', 'O'), ('.', 'O'), ('The', 'O'), ('cancer', 'O'), ('recurred', 'B-Response_To_Treatment'), ('as', 'O'), ('a', 'O'), ('right', 'O'), ('lung', 'O'), ('metastasis', 'O'), ('13', 'O'), ('years', 'O'), ('later', 'O'), ('.', 'O'), ('The', 'O'), ('patient', 'O'), ('underwent', 'O'), ('a', 'O'), ('regimen', 'O'), ('consisting', 'O'), ('of', 'O'), ('adriamycin', 'B-Chemotherapy'), ('(', 'O'), ('60', 'B-Dosage'), ('mg/m2', 'I-Dosage'), (')', 'O'), ('and', 'O'), ('cyclophosphamide', 'B-Chemotherapy'), ('(', 'O'), ('600', 'B-Dosage'), ('mg/m2', 'I-Dosage'), (')', 'O'), ('over', 'O'), ('six', 'B-Cycle_Count'), ('courses', 'I-Cycle_Count'), (',', 'O'), ('as', 'O'), ('first', 'B-Line_Of_Therapy'), ('line', 'I-Line_Of_Therapy'), ('therapy', 'O'), ('.', 'O')]

 
 ******************** ner_oncology_demographics Model Results ******************** 

[('The', 'O'), ('had', 'O'), ('previously', 'O'), ('undergone', 'O'), ('a', 'O'), ('left', 'O'), ('mastectomy', 'O'), ('and', 'O'), ('an', 'O'), ('axillary', 'O'), ('lymph', 'O'), ('node', 'O'), ('dissection', 'O'), ('for', 'O'), ('a', 'O'), ('left', 'O'), ('breast', 'O'), ('cancer', 'O'), ('twenty', 'O'), ('years', 'O'), ('ago', 'O'), ('.', 'O'), ('The', 'O'), ('tumor', 'O'), ('was', 'O'), ('positive', 'O'), ('for', 'O'), ('ER', 'O'), ('and', 'O'), ('PR', 'O'), ('.', 'O'), ('Postoperatively', 'O'), (',', 'O'), ('radiotherapy', 'O'), ('was', 'O'), ('administered', 'O'), ('to', 'O'), ('the', 'O'), ('residual', 'O'), ('breast', 'O'), ('.', 'O'), ('The', 'O'), ('cancer', 'O'), ('recurred', 'O'), ('as', 'O'), ('a', 'O'), ('right', 'O'), ('lung', 'O'), ('metastasis', 'O'), ('13', 'O'), ('years', 'O'), ('later', 'O'), ('.', 'O'), ('The', 'O'), ('patient', 'O'), ('underwent', 'O'), ('a', 'O'), ('regimen', 'O'), ('consisting', 'O'), ('of', 'O'), ('adriamycin', 'O'), ('(', 'O'), ('60', 'O'), ('mg/m2', 'O'), (')', 'O'), ('and', 'O'), ('cyclophosphamide', 'O'), ('(', 'O'), ('600', 'O'), ('mg/m2', 'O'), (')', 'O'), ('over', 'O'), ('six', 'O'), ('courses', 'O'), (',', 'O'), ('as', 'O'), ('first', 'O'), ('line', 'O'), ('therapy', 'O'), ('.', 'O')]

 
 ******************** ner_oncology_diagnosis Model Results ******************** 

[('The', 'O'), ('had', 'O'), ('previously', 'O'), ('undergone', 'O'), ('a', 'O'), ('left', 'O'), ('mastectomy', 'O'), ('and', 'O'), ('an', 'O'), ('axillary', 'O'), ('lymph', 'O'), ('node', 'O'), ('dissection', 'O'), ('for', 'O'), ('a', 'O'), ('left', 'O'), ('breast', 'B-Cancer_Dx'), ('cancer', 'I-Cancer_Dx'), ('twenty', 'O'), ('years', 'O'), ('ago', 'O'), ('.', 'O'), ('The', 'O'), ('tumor', 'B-Tumor_Finding'), ('was', 'O'), ('positive', 'O'), ('for', 'O'), ('ER', 'O'), ('and', 'O'), ('PR', 'O'), ('.', 'O'), ('Postoperatively', 'O'), (',', 'O'), ('radiotherapy', 'O'), ('was', 'O'), ('administered', 'O'), ('to', 'O'), ('the', 'O'), ('residual', 'O'), ('breast', 'O'), ('.', 'O'), ('The', 'O'), ('cancer', 'B-Cancer_Dx'), ('recurred', 'O'), ('as', 'O'), ('a', 'O'), ('right', 'O'), ('lung', 'O'), ('metastasis', 'B-Metastasis'), ('13', 'O'), ('years', 'O'), ('later', 'O'), ('.', 'O'), ('The', 'O'), ('patient', 'O'), ('underwent', 'O'), ('a', 'O'), ('regimen', 'O'), ('consisting', 'O'), ('of', 'O'), ('adriamycin', 'O'), ('(', 'O'), ('60', 'O'), ('mg/m2', 'O'), (')', 'O'), ('and', 'O'), ('cyclophosphamide', 'O'), ('(', 'O'), ('600', 'O'), ('mg/m2', 'O'), (')', 'O'), ('over', 'O'), ('six', 'O'), ('courses', 'O'), (',', 'O'), ('as', 'O'), ('first', 'O'), ('line', 'O'), ('therapy', 'O'), ('.', 'O')]

 
 ******************** ner_oncology_limited_80p_for_benchmarks Model Results ******************** 

[('The', 'O'), ('had', 'O'), ('previously', 'O'), ('undergone', 'O'), ('a', 'O'), ('left', 'B-Direction'), ('mastectomy', 'B-Cancer_Surgery'), ('and', 'O'), ('an', 'O'), ('axillary', 'B-Cancer_Surgery'), ('lymph', 'I-Cancer_Surgery'), ('node', 'I-Cancer_Surgery'), ('dissection', 'I-Cancer_Surgery'), ('for', 'O'), ('a', 'O'), ('left', 'B-Direction'), ('breast', 'B-Cancer_Dx'), ('cancer', 'I-Cancer_Dx'), ('twenty', 'B-Relative_Date'), ('years', 'I-Relative_Date'), ('ago', 'I-Relative_Date'), ('.', 'O'), ('The', 'O'), ('tumor', 'B-Tumor_Finding'), ('was', 'O'), ('positive', 'B-Biomarker_Result'), ('for', 'O'), ('ER', 'B-Biomarker'), ('and', 'O'), ('PR', 'B-Biomarker'), ('.', 'O'), ('Postoperatively', 'O'), (',', 'O'), ('radiotherapy', 'B-Radiotherapy'), ('was', 'O'), ('administered', 'O'), ('to', 'O'), ('the', 'O'), ('residual', 'O'), ('breast', 'B-Site_Breast'), ('.', 'O'), ('The', 'O'), ('cancer', 'B-Cancer_Dx'), ('recurred', 'B-Response_To_Treatment'), ('as', 'O'), ('a', 'O'), ('right', 'B-Direction'), ('lung', 'B-Site_Lung'), ('metastasis', 'B-Metastasis'), ('13', 'B-Relative_Date'), ('years', 'I-Relative_Date'), ('later', 'I-Relative_Date'), ('.', 'O'), ('The', 'O'), ('patient', 'O'), ('underwent', 'O'), ('a', 'O'), ('regimen', 'O'), ('consisting', 'O'), ('of', 'O'), ('adriamycin', 'B-Chemotherapy'), ('(', 'O'), ('60', 'B-Dosage'), ('mg/m2', 'I-Dosage'), (')', 'O'), ('and', 'O'), ('cyclophosphamide', 'B-Chemotherapy'), ('(', 'O'), ('600', 'B-Dosage'), ('mg/m2', 'I-Dosage'), (')', 'O'), ('over', 'O'), ('six', 'B-Cycle_Count'), ('courses', 'I-Cycle_Count'), (',', 'O'), ('as', 'O'), ('first', 'B-Line_Of_Therapy'), ('line', 'I-Line_Of_Therapy'), ('therapy', 'O'), ('.', 'O')]


 ******************** ner_oncology_tnm Model Results ******************** 

[('The', 'O'), ('had', 'O'), ('previously', 'O'), ('undergone', 'O'), ('a', 'O'), ('left', 'O'), ('mastectomy', 'O'), ('and', 'O'), ('an', 'O'), ('axillary', 'O'), ('lymph', 'O'), ('node', 'O'), ('dissection', 'O'), ('for', 'O'), ('a', 'O'), ('left', 'O'), ('breast', 'B-Cancer_Dx'), ('cancer', 'I-Cancer_Dx'), ('twenty', 'O'), ('years', 'O'), ('ago', 'O'), ('.', 'O'), ('The', 'O'), ('tumor', 'B-Tumor'), ('was', 'O'), ('positive', 'O'), ('for', 'O'), ('ER', 'O'), ('and', 'O'), ('PR', 'O'), ('.', 'O'), ('Postoperatively', 'O'), (',', 'O'), ('radiotherapy', 'O'), ('was', 'O'), ('administered', 'O'), ('to', 'O'), ('the', 'O'), ('residual', 'O'), ('breast', 'O'), ('.', 'O'), ('The', 'O'), ('cancer', 'B-Cancer_Dx'), ('recurred', 'O'), ('as', 'O'), ('a', 'O'), ('right', 'O'), ('lung', 'O'), ('metastasis', 'B-Metastasis'), ('13', 'O'), ('years', 'O'), ('later', 'O'), ('.', 'O'), ('The', 'O'), ('patient', 'O'), ('underwent', 'O'), ('a', 'O'), ('regimen', 'O'), ('consisting', 'O'), ('of', 'O'), ('adriamycin', 'O'), ('(', 'O'), ('60', 'O'), ('mg/m2', 'O'), (')', 'O'), ('and', 'O'), ('cyclophosphamide', 'O'), ('(', 'O'), ('600', 'O'), ('mg/m2', 'O'), (')', 'O'), ('over', 'O'), ('six', 'O'), ('courses', 'O'), (',', 'O'), ('as', 'O'), ('first', 'O'), ('line', 'O'), ('therapy', 'O'), ('.', 'O')]

 
 ******************** ner_oncology_unspecific_posology Model Results ******************** 

[('The', 'O'), ('had', 'O'), ('previously', 'O'), ('undergone', 'O'), ('a', 'O'), ('left', 'O'), ('mastectomy', 'B-Cancer_Therapy'), ('and', 'O'), ('an', 'O'), ('axillary', 'B-Cancer_Therapy'), ('lymph', 'I-Cancer_Therapy'), ('node', 'I-Cancer_Therapy'), ('dissection', 'I-Cancer_Therapy'), ('for', 'O'), ('a', 'O'), ('left', 'O'), ('breast', 'O'), ('cancer', 'O'), ('twenty', 'O'), ('years', 'O'), ('ago', 'O'), ('.', 'O'), ('The', 'O'), ('tumor', 'O'), ('was', 'O'), ('positive', 'O'), ('for', 'O'), ('ER', 'O'), ('and', 'O'), ('PR', 'O'), ('.', 'O'), ('Postoperatively', 'O'), (',', 'O'), ('radiotherapy', 'B-Cancer_Therapy'), ('was', 'O'), ('administered', 'O'), ('to', 'O'), ('the', 'O'), ('residual', 'O'), ('breast', 'O'), ('.', 'O'), ('The', 'O'), ('cancer', 'O'), ('recurred', 'O'), ('as', 'O'), ('a', 'O'), ('right', 'O'), ('lung', 'O'), ('metastasis', 'O'), ('13', 'O'), ('years', 'O'), ('later', 'O'), ('.', 'O'), ('The', 'O'), ('patient', 'O'), ('underwent', 'O'), ('a', 'O'), ('regimen', 'O'), ('consisting', 'O'), ('of', 'O'), ('adriamycin', 'B-Cancer_Therapy'), ('(', 'O'), ('60', 'B-Posology_Information'), ('mg/m2', 'I-Posology_Information'), (')', 'O'), ('and', 'O'), ('cyclophosphamide', 'B-Cancer_Therapy'), ('(', 'O'), ('600', 'B-Posology_Information'), ('mg/m2', 'I-Posology_Information'), (')', 'O'), ('over', 'O'), ('six', 'B-Posology_Information'), ('courses', 'I-Posology_Information'), (',', 'O'), ('as', 'O'), ('first', 'O'), ('line', 'O'), ('therapy', 'O'), ('.', 'O')]

 
 ******************** ner_oncology_posology Model Results ******************** 

[('The', 'O'), ('had', 'O'), ('previously', 'O'), ('undergone', 'O'), ('a', 'O'), ('left', 'O'), ('mastectomy', 'B-Cancer_Surgery'), ('and', 'O'), ('an', 'O'), ('axillary', 'B-Cancer_Surgery'), ('lymph', 'I-Cancer_Surgery'), ('node', 'I-Cancer_Surgery'), ('dissection', 'I-Cancer_Surgery'), ('for', 'O'), ('a', 'O'), ('left', 'O'), ('breast', 'O'), ('cancer', 'O'), ('twenty', 'O'), ('years', 'O'), ('ago', 'O'), ('.', 'O'), ('The', 'O'), ('tumor', 'O'), ('was', 'O'), ('positive', 'O'), ('for', 'O'), ('ER', 'O'), ('and', 'O'), ('PR', 'O'), ('.', 'O'), ('Postoperatively', 'O'), (',', 'O'), ('radiotherapy', 'B-Radiotherapy'), ('was', 'O'), ('administered', 'O'), ('to', 'O'), ('the', 'O'), ('residual', 'O'), ('breast', 'O'), ('.', 'O'), ('The', 'O'), ('cancer', 'O'), ('recurred', 'O'), ('as', 'O'), ('a', 'O'), ('right', 'O'), ('lung', 'O'), ('metastasis', 'O'), ('13', 'O'), ('years', 'O'), ('later', 'O'), ('.', 'O'), ('The', 'O'), ('patient', 'O'), ('underwent', 'O'), ('a', 'O'), ('regimen', 'O'), ('consisting', 'O'), ('of', 'O'), ('adriamycin', 'B-Cancer_Therapy'), ('(', 'O'), ('60', 'B-Dosage'), ('mg/m2', 'I-Dosage'), (')', 'O'), ('and', 'O'), ('cyclophosphamide', 'B-Cancer_Therapy'), ('(', 'O'), ('600', 'B-Dosage'), ('mg/m2', 'I-Dosage'), (')', 'O'), ('over', 'O'), ('six', 'B-Cycle_Count'), ('courses', 'I-Cycle_Count'), (',', 'O'), ('as', 'O'), ('first', 'O'), ('line', 'O'), ('therapy', 'O'), ('.', 'O')]
 
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
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter