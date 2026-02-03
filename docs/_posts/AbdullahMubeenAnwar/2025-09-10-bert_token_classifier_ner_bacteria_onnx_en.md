---
layout: model
title: Detect Bacterial Species (MedicalBertForTokenClassifier - ONNX)
author: John Snow Labs
name: bert_token_classifier_ner_bacteria_onnx
date: 2025-09-10
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

`bert_token_classifier_ner_bacteria` is a **BERT-based token classification model** fine-tuned for **Named Entity Recognition (NER) of bacterial species**.  
It identifies mentions of bacterial species in biomedical and clinical text, making it useful for literature mining, microbiology research, and healthcare applications.  

- **Architecture**: BERT Token Classifier  
- **Entities**:
  - `B-SPECIES`: Beginning of a bacterial species name  
  - `I-SPECIES`: Inside a bacterial species name  
  - `O`: Outside any entity  
  - `PAD`: Padding token (used internally, not during inference)

## Predicted Entities

`B-SPECIES`, `I-SPECIES`, `O`, `PAD`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_bacteria_onnx_en_6.1.1_3.0_1757522585145.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_bacteria_onnx_en_6.1.1_3.0_1757522585145.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.base import DocumentAssembler
from sparknlp_jsl.annotator import MedicalBertForTokenClassifier
from sparknlp.annotator import Tokenizer, NerConverter
from pyspark.ml import Pipeline

document_assembler = (
    DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
)

tokenizer = (
    Tokenizer()
    .setInputCols(["document"])
    .setOutputCol("token")
)

token_classifier = (
    MedicalBertForTokenClassifier.pretrained(
        "bert_token_classifier_ner_bacteria_onnx",
        "en",
        "clinical/models"
    )
    .setInputCols(["token", "document"])
    .setOutputCol("ner")
    .setCaseSensitive(True)
)

ner_converter = (
     NerConverterInternal()
    .setInputCols(["document", "token", "ner"])
    .setOutputCol("ner_chunk")
)

pipeline = Pipeline(stages=[
    document_assembler,
    tokenizer,
    token_classifier,
    ner_converter
])

test_sentence = "In recent years, infections caused by Escherichia coli have become increasingly resistant to antibiotics, especially in hospital environments. Another common pathogen is Staphylococcus aureus, which is notorious for methicillin-resistant strains (MRSA) that pose significant treatment challenges. In cases of pneumonia, Klebsiella pneumoniae is frequently isolated, while Pseudomonas aeruginosa is a leading cause of chronic lung infections in patients with cystic fibrosis. Foodborne outbreaks are often linked to Salmonella enterica and Listeria monocytogenes, both of which can contaminate improperly handled food products. In addition, Clostridium difficile has been associated with severe diarrhea following prolonged antibiotic use. Other important pathogens include Mycobacterium tuberculosis, the causative agent of tuberculosis, and Helicobacter pylori, which colonizes the stomach lining and is associated with peptic ulcers. Opportunistic infections are also observed with Enterococcus faecalis and Bacteroides fragilis in immunocompromised patients."
data = spark.createDataFrame([[test_sentence]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)
```
{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")


tokenizer = nlp.Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")


token_classifier = medical.BertForTokenClassifier.pretrained(
        "bert_token_classifier_ner_bacteria_onnx",
        "en",
        "clinical/models"
    )\
    .setInputCols(["token", "document"])\
    .setOutputCol("ner")\
    .setCaseSensitive(True)


ner_converter = medical.NerConverterInternal()\
    .setInputCols(["document", "token", "ner"])\
    .setOutputCol("ner_chunk")


pipeline = Pipeline(stages=[
    document_assembler,
    tokenizer,
    token_classifier,
    ner_converter
])

test_sentence = "In recent years, infections caused by Escherichia coli have become increasingly resistant to antibiotics, especially in hospital environments. Another common pathogen is Staphylococcus aureus, which is notorious for methicillin-resistant strains (MRSA) that pose significant treatment challenges. In cases of pneumonia, Klebsiella pneumoniae is frequently isolated, while Pseudomonas aeruginosa is a leading cause of chronic lung infections in patients with cystic fibrosis. Foodborne outbreaks are often linked to Salmonella enterica and Listeria monocytogenes, both of which can contaminate improperly handled food products. In addition, Clostridium difficile has been associated with severe diarrhea following prolonged antibiotic use. Other important pathogens include Mycobacterium tuberculosis, the causative agent of tuberculosis, and Helicobacter pylori, which colonizes the stomach lining and is associated with peptic ulcers. Opportunistic infections are also observed with Enterococcus faecalis and Bacteroides fragilis in immunocompromised patients."
data = spark.createDataFrame([[test_sentence]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)
```

```scala
import com.johnsnowlabs.nlp.base.DocumentAssembler
import com.johnsnowlabs.nlp.annotators.Tokenizer
import com.johnsnowlabs.nlp.annotators.ner.NerConverter
import com.johnsnowlabs.nlp.annotators.classifier.dl.MedicalBertForTokenClassifier
import org.apache.spark.ml.Pipeline

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("token")

val tokenClassifier = MedicalBertForTokenClassifier
  .pretrained("bert_token_classifier_ner_bacteria_onnx", "en", "clinical/models")
  .setInputCols(Array("token", "document"))
  .setOutputCol("ner")
  .setCaseSensitive(true)

val nerConverter = new  NerConverterInternal()
  .setInputCols(Array("document", "token", "ner"))
  .setOutputCol("ner_chunk")

val pipeline = new Pipeline()
  .setStages(Array(
    documentAssembler,
    tokenizer,
    tokenClassifier,
    nerConverter
  ))

val testSentence = "In recent years, infections caused by Escherichia coli have become increasingly resistant to antibiotics, especially in hospital environments. Another common pathogen is Staphylococcus aureus, which is notorious for methicillin-resistant strains (MRSA) that pose significant treatment challenges. In cases of pneumonia, Klebsiella pneumoniae is frequently isolated, while Pseudomonas aeruginosa is a leading cause of chronic lung infections in patients with cystic fibrosis. Foodborne outbreaks are often linked to Salmonella enterica and Listeria monocytogenes, both of which can contaminate improperly handled food products. In addition, Clostridium difficile has been associated with severe diarrhea following prolonged antibiotic use. Other important pathogens include Mycobacterium tuberculosis, the causative agent of tuberculosis, and Helicobacter pylori, which colonizes the stomach lining and is associated with peptic ulcers. Opportunistic infections are also observed with Enterococcus faecalis and Bacteroides fragilis in immunocompromised patients."
val data = Seq(testSentence).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+----------------------+-------+
|text                  |entity |
+----------------------+-------+
|Escherichia coli      |SPECIES|
|Staphylococcus aureus |SPECIES|
|MRSA                  |SPECIES|
|Klebsiella pneumoniae |SPECIES|
|Pseudomonas aeruginosa|SPECIES|
|Salmonella enterica   |SPECIES|
|Listeria monocytogenes|SPECIES|
+----------------------+-------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_token_classifier_ner_bacteria_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|403.7 MB|
|Case sensitive:|true|
|Max sentence length:|128|
