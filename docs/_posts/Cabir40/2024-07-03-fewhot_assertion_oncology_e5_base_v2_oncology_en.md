---
layout: model
title: Few-Shot Assertion Model ( Oncology )
author: John Snow Labs
name: fewhot_assertion_oncology_e5_base_v2_oncology
date: 2024-07-03
tags: [assertion, en, licensed, clinical, e5, medical, oncology, fewshot]
task: Assertion Status
language: en
edition: Healthcare NLP 5.3.3
spark_version: 3.0
supported: true
annotator: FewShotAssertionClassifierModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Assign assertion status to clinical entities extracted by NER based on their context in the text. Also this model is trained on a list of clinical and biomedical datasets curated in-house

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/fewhot_assertion_oncology_e5_base_v2_oncology_en_5.3.3_3.0_1720013627652.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/fewhot_assertion_oncology_e5_base_v2_oncology_en_5.3.3_3.0_1720013627652.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")\
    .setSplitChars(["-", "\/"])

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

# ner_oncology
ner_oncology = MedicalNerModel.pretrained("ner_oncology","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner_oncology")

ner_oncology_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner_oncology"])\
    .setOutputCol("ner_oncology_chunk")

few_shot_assertion_converter = FewShotAssertionSentenceConverter()\
    .setInputCols(["sentence", "ner_oncology_chunk"])\
    .setOutputCol("assertion_sentence")

e5_embeddings = E5Embeddings.pretrained("e5_base_v2_embeddings_medical_assertion_oncology", "en", "clinical/models")\
    .setInputCols(["assertion_sentence"])\
    .setOutputCol("assertion_embedding")

few_shot_assertion_classifier = FewShotAssertionClassifierModel()\
    .pretrained("fewhot_assertion_oncology_e5_base_v2_oncology", "en", "clinical/models")\
    .setInputCols(["assertion_embedding"])\
    .setOutputCol("assertion")
 
assertion_pipeline = Pipeline(stages=[
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_oncology,
    ner_oncology_converter,
    few_shot_assertion_converter,
    e5_embeddings,
    few_shot_assertion_classifier
])

sample_text= [
"""The patient is suspected to have colorectal cancer. Her family history is positive for other cancers. The result of the biopsy was positive. A CT scan was ordered to rule out metastases."""
]

data = spark.createDataFrame([sample_text]).toDF("text")

result = assertion_pipeline.fit(data).transform(data)

```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")
    .setSplitChars(Array("-", "\/"))

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
    .setInputCols(Array("sentence","token"))
    .setOutputCol("embeddings")

# ner_oncology
val ner_oncology = MedicalNerModel.pretrained("ner_oncology","en","clinical/models")
    .setInputCols(Array("sentence","token","embeddings"))
    .setOutputCol("ner_oncology")

val ner_oncology_converter = new NerConverterInternal()
    .setInputCols(Array("sentence","token","ner_oncology"))
    .setOutputCol("ner_chunk")

val few_shot_assertion_converter = new FewShotAssertionSentenceConverter()
    .setInputCols(Array("sentence", "ner_chunk"))
    .setOutputCol("assertion_sentence")

val e5_embeddings = E5Embeddings.pretrained("e5_base_v2_embeddings_medical_assertion_oncology", "en", "clinical/models")
    .setInputCols(Array("assertion_sentence"))
    .setOutputCol("assertion_embedding")

val few_shot_assertion_classifier = FewShotAssertionClassifierModel()
    .pretrained("fewhot_assertion_oncology_e5_base_v2_oncology", "en", "clinical/models")
    .setInputCols(Array("assertion_embedding"))
    .setOutputCol("assertion")

val pipeline = new Pipeline().setStages(Array(    
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_oncology,
    ner_oncology_converter,
    few_shot_assertion_converter,
    e5_embeddings,
    few_shot_assertion_classifier))

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

|    | chunks            |   begin |   end | entities         | assertion   |   confidence |
|---:|:------------------|--------:|------:|:-----------------|:------------|-------------:|
|  0 | colorectal cancer |      33 |    49 | Cancer_Dx        | Possible    |     0.581282 |
|  1 | Her               |      52 |    54 | Gender           | Present     |     0.9563   |
|  2 | cancers           |      93 |    99 | Cancer_Dx        | Family      |     0.234656 |
|  3 | biopsy            |     120 |   125 | Pathology_Test   | Past        |     0.957321 |
|  4 | positive          |     131 |   138 | Pathology_Result | Present     |     0.956439 |
|  5 | CT scan           |     143 |   149 | Imaging_Test     | Past        |     0.95717  |
|  6 | metastases        |     175 |   184 | Metastasis       | Possible    |     0.549866 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|fewhot_assertion_oncology_e5_base_v2_oncology|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[assertion_embedding]|
|Output Labels:|[assertion]|
|Language:|en|
|Size:|25.4 KB|
