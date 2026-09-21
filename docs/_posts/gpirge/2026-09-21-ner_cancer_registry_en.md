---
layout: model
title: Cancer Registry Model
author: John Snow Labs
name: ner_cancer_registry
date: 2026-09-21
tags: [en, licensed]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.4.0
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Run the pipeline

## Predicted Entities

`Lymph_Node`, `Histological_Type`, `Anatomical_Site`, `Staging`, `Imaging_Test`, `Tumor_Finding`, `Invasion`, `Response_To_Treatment`, `Adverse_Event`, `Tumor_Size`, `Biomarker_Result`, `Clinical_Condition`, `Chemotherapy`, `ICD10_Code`, `Targeted_Therapy`, `Radiotherapy`, `Performance_Status`, `Pathology_Test`, `Supportive_Care`, `Cancer_Surgery`, `Pathology_Result`, `Hormonal_Therapy`, `Biomarker`, `Immunotherapy`, `Metastasis`, `Cancer_Dx`, `Grade`, `Date`, `Treatment_Intent`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_cancer_registry_en_6.4.0_3.0_1790020084795.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_cancer_registry_en_6.4.0_3.0_1790020084795.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

ner = MedicalNerModel.pretrained("ner_cancer_registry", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")
    
pipeline = Pipeline(stages=[document_assembler,
                            sentence_detector,
                            tokenizer,
                            word_embeddings,
                            ner,
                            ner_converter])

data = spark.createDataFrame([[""]]).toDF("text")

model = pipeline.fit(data)
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_cancer_registry|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.8 MB|