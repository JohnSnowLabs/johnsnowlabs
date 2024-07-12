---
layout: model
title: Detect Cellular/Molecular Biology Entities (clinical_medium)
author: John Snow Labs
name: ner_cellular_emb_clinical_medium
date: 2023-05-24
tags: [ner, clinical, en, licensed, dna, rna, cell_type, cell_line, protein]
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

Pretrained named entity recognition deep learning model for molecular biology related terms. The SparkNLP deep learning model (MedicalNerModel) is inspired by a former state of the art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM-CNN.

## Predicted Entities

`DNA`, `RNA`, `Cell_type`, `Cell_line`, `Protein`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_CELLULAR/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_CELLULAR.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_cellular_emb_clinical_medium_en_4.4.2_3.0_1684919993889.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_cellular_emb_clinical_medium_en_4.4.2_3.0_1684919993889.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical_medium", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_cellular_emb_clinical_medium", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(['sentence', 'token', 'ner'])\
    .setOutputCol('ner_chunk')

pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter   
    ])

sample_df = spark.createDataFrame([["""Detection of various other intracellular signaling proteins is also described. Genetic characterization of transactivation of the human T-cell leukemia virus type 1 promoter: Binding of Tax to Tax-responsive element 1 is mediated by the cyclic AMP-responsive members of the CREB/ATF family of transcription factors. To achieve a better understanding of the mechanism of transactivation by Tax of human T-cell leukemia virus type 1 Tax-responsive element 1 (TRE-1), we developed a genetic approach with Saccharomyces cerevisiae. We constructed a yeast reporter strain containing the lacZ gene under the control of the CYC1 promoter associated with three copies of TRE-1. Expression of either the cyclic AMP response element-binding protein (CREB) or CREB fused to the GAL4 activation domain (GAD) in this strain did not modify the expression of the reporter gene. Tax alone was also inactive."""]]).toDF("text")

result = pipeline.fit(sample_df).transform(sample_df)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical_medium", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_cellular_emb_clinical_medium", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter))

val sample_data = Seq("""Detection of various other intracellular signaling proteins is also described. Genetic characterization of transactivation of the human T-cell leukemia virus type 1 promoter: Binding of Tax to Tax-responsive element 1 is mediated by the cyclic AMP-responsive members of the CREB/ATF family of transcription factors. To achieve a better understanding of the mechanism of transactivation by Tax of human T-cell leukemia virus type 1 Tax-responsive element 1 (TRE-1), we developed a genetic approach with Saccharomyces cerevisiae. We constructed a yeast reporter strain containing the lacZ gene under the control of the CYC1 promoter associated with three copies of TRE-1. Expression of either the cyclic AMP response element-binding protein (CREB) or CREB fused to the GAL4 activation domain (GAD) in this strain did not modify the expression of the reporter gene. Tax alone was also inactive.""").toDS.toDF("text")

val result = pipeline.fit(sample_data).transform(sample_data)
```
</div>

## Results

```bash
+-----------------------------------------------------------+-----+---+---------+
|chunk                                                      |begin|end|ner_label|
+-----------------------------------------------------------+-----+---+---------+
|intracellular signaling proteins                           |27   |58 |protein  |
|human T-cell leukemia virus type 1 promoter                |130  |172|DNA      |
|Tax                                                        |186  |188|protein  |
|Tax-responsive element 1                                   |193  |216|DNA      |
|cyclic AMP-responsive members                              |237  |265|protein  |
|CREB/ATF family                                            |274  |288|protein  |
|transcription factors                                      |293  |313|protein  |
|Tax                                                        |389  |391|protein  |
|human T-cell leukemia virus type 1 Tax-responsive element 1|396  |454|DNA      |
|TRE-1),                                                    |457  |463|DNA      |
|lacZ gene                                                  |582  |590|DNA      |
|CYC1 promoter                                              |617  |629|DNA      |
|TRE-1                                                      |663  |667|DNA      |
|cyclic AMP response element-binding protein                |695  |737|protein  |
|CREB                                                       |740  |743|protein  |
|CREB                                                       |749  |752|protein  |
|GAL4 activation domain                                     |767  |788|protein  |
|GAD                                                        |791  |793|protein  |
|reporter gene                                              |848  |860|DNA      |
|Tax                                                        |863  |865|protein  |
+-----------------------------------------------------------+-----+---+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_cellular_emb_clinical_medium|
|Compatibility:|Healthcare NLP 4.4.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|2.8 MB|

## References

Trained on the JNLPBA corpus containing more than 2.404 publication abstracts. [https://www.geniaproject.org/](https://www.geniaproject.org/)

## Benchmarking

```bash
       label  precision    recall  f1-score   support
   cell_line       0.59      0.80      0.68      1489
   cell_type       0.89      0.76      0.82      4912
     protein       0.80      0.90      0.85      9841
         RNA       0.79      0.83      0.81       305
         DNA       0.78      0.86      0.82      2845
   micro-avg       0.80      0.85      0.82     19392
   macro-avg       0.77      0.83      0.79     19392
weighted-avg       0.80      0.85      0.82     19392
```