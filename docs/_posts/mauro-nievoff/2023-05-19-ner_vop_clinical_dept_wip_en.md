---
layout: model
title: Extract medical devices and clinical department mentions (Voice of the Patients)
author: John Snow Labs
name: ner_vop_clinical_dept_wip
date: 2023-05-19
tags: [licensed, clinical, en, ner, vop, patient]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.4.2
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts medical devices and clinical department mentions terms from the documents transferred from the patient’s own sentences.

Note: ‘wip’ suffix indicates that the model development is work-in-progress and will be finalised and the model performance will improved in the upcoming releases.

## Predicted Entities

`AdmissionDischarge`, `ClinicalDept`, `MedicalDevice`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/VOICE_OF_THE_PATIENTS/){:.button.button-orange}
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_vop_clinical_dept_wip_en_4.4.2_3.0_1684512218256.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_vop_clinical_dept_wip_en_4.4.2_3.0_1684512218256.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel.pretrained("ner_vop_clinical_dept_wip", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")
pipeline = Pipeline(stages=[document_assembler,
                            sentence_detector,
                            tokenizer,
                            word_embeddings,
                            ner,
                            ner_converter])

data = spark.createDataFrame([["My little brother is having surgery tomorrow in the orthopedic department. He is getting a titanium plate put in his leg to help it heal faster. Wishing him a speedy recovery!"]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
    
val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")
    
val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")
    
val word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")                
    
val ner = MedicalNerModel.pretrained("ner_vop_clinical_dept_wip", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")
    
val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

        
val pipeline = new Pipeline().setStages(Array(document_assembler,
                            sentence_detector,
                            tokenizer,
                            word_embeddings,
                            ner,
                            ner_converter))    

val data = Seq("My little brother is having surgery tomorrow in the orthopedic department. He is getting a titanium plate put in his leg to help it heal faster. Wishing him a speedy recovery!").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
| chunk                 | ner_label     |
|:----------------------|:--------------|
| orthopedic department | ClinicalDept  |
| titanium plate        | MedicalDevice |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_vop_clinical_dept_wip|
|Compatibility:|Healthcare NLP 4.4.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|3.8 MB|
|Dependencies:|embeddings_clinical|

## References

In-house annotated health-related text in colloquial language.

## Benchmarking

```bash
             label  tp  fp  fn  total  precision  recall   f1
AdmissionDischarge  29   1   5     34       0.97    0.85 0.91
      ClinicalDept 292  41  34    326       0.88    0.90 0.89
     MedicalDevice 244  72  88    332       0.77    0.73 0.75
         macro_avg 565 114 127    692       0.87    0.83 0.85
         micro_avg 565 114 127    692       0.83    0.82 0.82
```