---
layout: model
title: Detect Cellular/Molecular Biology Entities - ONNX
author: John Snow Labs
name: bert_token_classifier_ner_jnlpba_cellular_onnx
date: 2025-09-11
tags: [medical, clinical, ner, en, licensed, onnx]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.1.1
spark_version: 3.0
supported: true
engine: onnx
annotator: MedicalBertForTokenClassifier
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model detects molecular biology-related terms in medical texts. The model is trained with the BertForTokenClassification method from the transformers library and imported into Spark NLP.

## Predicted Entities

`O`, `B-cell_type`, `B-RNA`, `B-protein`, `I-protein`, `I-cell_line`, `I-RNA`, `I-DNA`, `B-cell_line`, `I-cell_type`, `B-DNA`, `PAD`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_jnlpba_cellular_onnx_en_6.1.1_3.0_1757556992398.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_jnlpba_cellular_onnx_en_6.1.1_3.0_1757556992398.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.base import DocumentAssembler
from sparknlp_jsl.annotator import SentenceDetectorDLModel, MedicalBertForTokenClassifier
from sparknlp.annotator import Tokenizer, NerConverter
from pyspark.ml import Pipeline

document_assembler = (
    DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
)

sentenceDetector = (
    SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
    .setInputCols(["document"])
    .setOutputCol("sentence")
)

tokenizer = (
    Tokenizer()
    .setInputCols(["sentence"])
    .setOutputCol("token")
)

token_classifier = (
    MedicalBertForTokenClassifier.pretrained(
        "bert_token_classifier_ner_jnlpba_cellular_onnx",
        "en",
        "clinical/models"
    )
    .setInputCols(["token", "sentence"])
    .setOutputCol("ner")
    .setCaseSensitive(True)
)

ner_converter = (
     NerConverterInternal()
    .setInputCols(["sentence", "token", "ner"])
    .setOutputCol("ner_chunk")
)

pipeline = Pipeline(stages=[
    document_assembler,
    sentenceDetector,
    tokenizer,
    token_classifier,
    ner_converter
])

test_sentence = "The results suggest that activation of protein kinase C, but not new protein synthesis, is required for IL-2 induction of IFN-gamma and GM-CSF cytoplasmic mRNA. It also was observed that suppression of cytokine gene expression by these agents was independent of the inhibition of proliferation. These data indicate that IL-2 and IL-12 may have distinct signaling pathways leading to the induction of IFN-gammaand GM-CSFgene expression, andthatthe NK3.3 cell line may serve as a novel model for dissecting the biochemical and molecular events involved in these pathways. A functional T-cell receptor signaling pathway is required for p95vav activity. Stimulation of the T-cell antigen receptor ( TCR ) induces activation of multiple tyrosine kinases, resulting in phosphorylation of numerous intracellular substrates. One substrate is p95vav, which is expressed exclusively in hematopoietic and trophoblast cells."
data = spark.createDataFrame([[test_sentence]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)
```
{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

document_assembler =  nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")


sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")


tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")


token_classifier = medical.BertForTokenClassifier.pretrained(
        "bert_token_classifier_ner_jnlpba_cellular_onnx",
        "en",
        "clinical/models"
    )\
    .setInputCols(["token", "sentence"])\
    .setOutputCol("ner")\
    .setCaseSensitive(True)


ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")


pipeline = nlp.Pipeline(stages=[
    document_assembler,
    sentenceDetector,
    tokenizer,
    token_classifier,
    ner_converter
])

test_sentence = "The results suggest that activation of protein kinase C, but not new protein synthesis, is required for IL-2 induction of IFN-gamma and GM-CSF cytoplasmic mRNA. It also was observed that suppression of cytokine gene expression by these agents was independent of the inhibition of proliferation. These data indicate that IL-2 and IL-12 may have distinct signaling pathways leading to the induction of IFN-gammaand GM-CSFgene expression, andthatthe NK3.3 cell line may serve as a novel model for dissecting the biochemical and molecular events involved in these pathways. A functional T-cell receptor signaling pathway is required for p95vav activity. Stimulation of the T-cell antigen receptor ( TCR ) induces activation of multiple tyrosine kinases, resulting in phosphorylation of numerous intracellular substrates. One substrate is p95vav, which is expressed exclusively in hematopoietic and trophoblast cells."
data = spark.createDataFrame([[test_sentence]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)
```

```scala
import com.johnsnowlabs.nlp.base.DocumentAssembler
import com.johnsnowlabs.nlp.annotators.Tokenizer
import com.johnsnowlabs.nlp.annotators.ner.NerConverter
import com.johnsnowlabs.nlp.annotators.classifier.dl.MedicalBertForTokenClassifier
import com.johnsnowlabs.nlp.annotators.sentence_detector_dl.SentenceDetectorDLApproach
import org.apache.spark.ml.Pipeline

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = new SentenceDetectorDLModel()
  .pretrained("sentence_detector_dl","xx")
  .setInputCols("document")
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("token")

val tokenClassifier = MedicalBertForTokenClassifier
  .pretrained("bert_token_classifier_ner_jnlpba_cellular_onnx", "en", "clinical/models")
  .setInputCols(Array("token", "document"))
  .setOutputCol("ner")
  .setCaseSensitive(true)

val nerConverter = new  NerConverterInternal()
  .setInputCols(Array("document", "token", "ner"))
  .setOutputCol("ner_chunk")

val pipeline = new Pipeline()
  .setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    tokenClassifier,
    nerConverter
  ))

val testSentence = "The results suggest that activation of protein kinase C, but not new protein synthesis, is required for IL-2 induction of IFN-gamma and GM-CSF cytoplasmic mRNA. It also was observed that suppression of cytokine gene expression by these agents was independent of the inhibition of proliferation. These data indicate that IL-2 and IL-12 may have distinct signaling pathways leading to the induction of IFN-gammaand GM-CSFgene expression, andthatthe NK3.3 cell line may serve as a novel model for dissecting the biochemical and molecular events involved in these pathways. A functional T-cell receptor signaling pathway is required for p95vav activity. Stimulation of the T-cell antigen receptor ( TCR ) induces activation of multiple tyrosine kinases, resulting in phosphorylation of numerous intracellular substrates. One substrate is p95vav, which is expressed exclusively in hematopoietic and trophoblast cells."
val data = Seq(testSentence).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+-------------------------------------+---------+
|text                                 |entity   |
+-------------------------------------+---------+
|protein kinase C                     |protein  |
|IL-2                                 |protein  |
|IFN-gamma and GM-CSF cytoplasmic mRNA|RNA      |
|cytokine gene                        |DNA      |
|IL-2                                 |protein  |
|IL-12                                |protein  |
|IFN-gammaand                         |protein  |
|GM-CSFgene                           |protein  |
|NK3.3 cell line                      |cell_line|
|T-cell receptor                      |protein  |
|p95vav                               |protein  |
|T-cell antigen receptor              |protein  |
|TCR                                  |protein  |
|tyrosine kinases                     |protein  |
|p95vav                               |protein  |
|hematopoietic and trophoblast cells  |cell_type|
+-------------------------------------+---------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_token_classifier_ner_jnlpba_cellular_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|403.7 MB|
|Case sensitive:|true|
|Max sentence length:|128|