---
layout: model
title: Explain Clinical Document Radiology - Light
author: John Snow Labs
name: explain_clinical_doc_radiology_light
date: 2025-06-27
tags: [licensed, en, clinical, pipeline, ner, radiology]
task: [Pipeline Healthcare, Named Entity Recognition]
language: en
edition: Healthcare NLP 6.0.2
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to extract radiology-related clinical/medical entities. In this pipeline, 3 NER models are used to extract the clinical entity labels.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_radiology_light_en_6.0.2_3.4_1751033464998.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_radiology_light_en_6.0.2_3.4_1751033464998.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_radiology_light", "en", "clinical/models")

result = ner_pipeline.annotate("""A 65-year-old woman had a history of debulking surgery, bilateral oophorectomy with omentectomy,
 total anterior hysterectomy with radical pelvic lymph nodes dissection due to ovarian carcinoma (mucinous-type carcinoma, stage Ic) 1 year ago.
 Bilateral breast ultrasound was subsequently performed, which demonstrated an ovoid mass measuring approximately 0.5 x 0.5 x 0.4 cm in diameter located within the anteromedial aspect of the left shoulder. 
 This mass demonstrates isoechoic echotexture to the adjacent muscle, with no evidence of internal color flow. 
 This may represent benign fibrous tissue or a lipoma.
 """)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_radiology_light", "en", "clinical/models")

val result = ner_pipeline.annotate("""A 65-year-old woman had a history of debulking surgery, bilateral oophorectomy with omentectomy,
 total anterior hysterectomy with radical pelvic lymph nodes dissection due to ovarian carcinoma (mucinous-type carcinoma, stage Ic) 1 year ago.
 Bilateral breast ultrasound was subsequently performed, which demonstrated an ovoid mass measuring approximately 0.5 x 0.5 x 0.4 cm in diameter located within the anteromedial aspect of the left shoulder. 
 This mass demonstrates isoechoic echotexture to the adjacent muscle, with no evidence of internal color flow. 
 This may represent benign fibrous tissue or a lipoma.
 """)

```
</div>

## Results

```bash
|    | chunks                                   |   begin |   end | entities                  |
|---:|:-----------------------------------------|--------:|------:|:--------------------------|
|  0 | woman                                    |      14 |    18 | Gender                    |
|  1 | debulking surgery                        |      37 |    53 | Procedure                 |
|  2 | bilateral oophorectomy                   |      56 |    77 | Procedure                 |
|  3 | omentectomy                              |      84 |    94 | Procedure                 |
|  4 | total anterior hysterectomy              |      98 |   124 | Procedure                 |
|  5 | radical pelvic lymph nodes dissection    |     131 |   167 | Procedure                 |
|  6 | ovarian                                  |     176 |   182 | BodyPart                  |
|  7 | carcinoma                                |     184 |   192 | Disease_Syndrome_Disorder |
|  8 | mucinous-type carcinoma                  |     195 |   217 | Disease_Syndrome_Disorder |
|  9 | stage Ic                                 |     220 |   227 | Disease_Syndrome_Disorder |
| 10 | Bilateral                                |     243 |   251 | Direction                 |
| 11 | breast ultrasound                        |     253 |   269 | Imaging_Test              |
| 12 | ovoid mass                               |     321 |   330 | ImagingFindings           |
| 13 | 0.5 x 0.5 x 0.4 cm                       |     356 |   373 | Measurements              |
| 14 | anteromedial aspect of the left shoulder |     406 |   445 | BodyPart                  |
| 15 | mass                                     |     455 |   458 | ImagingFindings           |
| 16 | isoechoic echotexture                    |     473 |   493 | ImagingFindings           |
| 17 | adjacent muscle                          |     502 |   516 | BodyPart                  |
| 18 | internal color flow                      |     539 |   557 | ImagingFindings           |
| 19 | benign fibrous tissue                    |     581 |   601 | ImagingFindings           |
| 20 | lipoma                                   |     608 |   613 | Disease_Syndrome_Disorder |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_radiology_light|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.8 GB|

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
- ChunkMergeModel