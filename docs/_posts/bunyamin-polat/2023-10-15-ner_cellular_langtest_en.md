---
layout: model
title: Detect Cellular/Molecular Biology Entities (LangTest)
author: John Snow Labs
name: ner_cellular_langtest
date: 2023-10-15
tags: [en, ner, licensed, clinical, cellular, langtest]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.1.1
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for molecular biology-related terms. It is the version of [ner_cellular](https://nlp.johnsnowlabs.com/2021/03/31/ner_cellular_en.html) model augmented with `langtest` library.

| **test_type**        | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|----------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_ocr_typo**     | 1240                  | 311                  | 738                   | 1667                 | 70%                   | 37%                  | 84%                 |
| **lowercase**        | 840                   | 437                  | 1153                  | 1556                 | 70%                   | 58%                  | 78%                 |
| **titlecase**        | 1404                  | 466                  | 589                   | 1527                 | 70%                   | 30%                  | 77%                 |
| **uppercase**        | 1788                  | 575                  | 205                   | 1418                 | 70%                   | 10%                  | 71%                 |
| **weighted average** | **5272**              | **1789**             | **2685**              | **6168**             | **70%**               | **33.74%**           | **77.52%**          |

## Predicted Entities

`DNA`, `Cell_type`, `Cell_line`, `RNA`, `Protein`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_cellular_langtest_en_5.1.1_3.0_1697371325344.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_cellular_langtest_en_5.1.1_3.0_1697371325344.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")
         
sentence_detector = SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

cellular_ner = MedicalNerModel.pretrained("ner_cellular_langtest", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter()\
 	.setInputCols(["sentence", "token", "ner"])\
 	.setOutputCol("ner_chunk")

nlpPipeline = Pipeline(stages=[document_assembler, sentence_detector, tokenizer, word_embeddings, cellular_ner, ner_converter])

model = nlpPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

result = model.transform(spark.createDataFrame([['Detection of various other intracellular signaling proteins is also described. Genetic characterization of transactivation of the human T-cell leukemia virus type 1 promoter: Binding of Tax to Tax-responsive element 1 is mediated by the cyclic AMP-responsive members of the CREB/ATF family of transcription factors. To achieve a better understanding of the mechanism of transactivation by Tax of human T-cell leukemia virus type 1 Tax-responsive element 1 (TRE-1), we developed a genetic approach with Saccharomyces cerevisiae. We constructed a yeast reporter strain containing the lacZ gene under the control of the CYC1 promoter associated with three copies of TRE-1. Expression of either the cyclic AMP response element-binding protein (CREB) or CREB fused to the GAL4 activation domain (GAD) in this strain did not modify the expression of the reporter gene. Tax alone was also inactive.']]).toDF("text"))

```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
         
val sentence_detector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val celular_ner = MedicalNerModel.pretrained("ner_cellular_langtest", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverter()
 	.setInputCols(Array("sentence", "token", "ner"))
 	.setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(document_assembler, sentence_detector, tokenizer, word_embeddings, cellular_ner, ner_converter))

val data = Seq("""Detection of various other intracellular signaling proteins is also described. Genetic characterization of transactivation of the human T-cell leukemia virus type 1 promoter: Binding of Tax to Tax-responsive element 1 is mediated by the cyclic AMP-responsive members of the CREB/ATF family of transcription factors. To achieve a better understanding of the mechanism of transactivation by Tax of human T-cell leukemia virus type 1 Tax-responsive element 1 (TRE-1), we developed a genetic approach with Saccharomyces cerevisiae. We constructed a yeast reporter strain containing the lacZ gene under the control of the CYC1 promoter associated with three copies of TRE-1. Expression of either the cyclic AMP response element-binding protein (CREB) or CREB fused to the GAL4 activation domain (GAD) in this strain did not modify the expression of the reporter gene. Tax alone was also inactive.""").toDS().toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-------------------------------------------+---------+
|chunk                                      |ner_label|
+-------------------------------------------+---------+
|intracellular signaling proteins           |protein  |
|human T-cell leukemia virus type 1 promoter|DNA      |
|Tax                                        |protein  |
|Tax-responsive element 1                   |DNA      |
|cyclic AMP-responsive members              |protein  |
|CREB/ATF family                            |protein  |
|transcription factors                      |protein  |
|Tax                                        |protein  |
|Tax-responsive element 1                   |DNA      |
|TRE-1                                      |DNA      |
|lacZ gene                                  |DNA      |
|CYC1 promoter                              |DNA      |
|TRE-1                                      |DNA      |
|cyclic AMP response element-binding protein|protein  |
|CREB                                       |protein  |
|CREB                                       |protein  |
|GAL4 activation domain                     |protein  |
|GAD                                        |protein  |
|reporter gene                              |DNA      |
|Tax                                        |protein  |
+-------------------------------------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_cellular_langtest|
|Compatibility:|Healthcare NLP 5.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.5 MB|

## References

Trained on the [JNLPBA corpus](https://www.geniaproject.org/) containing more than 2.404 publication abstracts with 'embeddings_clinical'.

## Benchmarking

```bash
label         precision  recall  f1-score  support 
B-DNA         0.81       0.79    0.80      1026    
B-RNA         0.79       0.90    0.84      87      
B-cell_line   0.79       0.74    0.77      457     
B-cell_type   0.77       0.81    0.79      843     
B-protein     0.86       0.90    0.88      3630    
I-DNA         0.88       0.87    0.87      1776    
I-RNA         0.76       0.99    0.86      127     
I-cell_line   0.80       0.75    0.78      819     
I-cell_type   0.76       0.86    0.81      1185    
I-protein     0.85       0.86    0.85      3069    
micro-avg     0.83       0.85    0.84      13019   
macro-avg     0.81       0.85    0.82      13019   
weighted-avg  0.83       0.85    0.84      13019   
```
