---
layout: model
title: Pipeline to Detect Chemical Compounds and Genes (BertForTokenClassifier)
author: John Snow Labs
name: bert_token_classifier_ner_chemprot_pipeline
date: 2023-06-16
tags: [berfortokenclassification, chemprot, licensed, en]
task: Named Entity Recognition
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

This pretrained pipeline is built on the top of [bert_token_classifier_ner_chemprot](https://nlp.johnsnowlabs.com/2022/01/06/bert_token_classifier_ner_chemprot_en.html) model.

## Predicted Entities

`CHEMICAL`, `GENE-N`, `GENE-Y`



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_chemprot_pipeline_en_4.4.4_3.4_1686922205651.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_chemprot_pipeline_en_4.4.4_3.4_1686922205651.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("bert_token_classifier_ner_chemprot_pipeline", "en", "clinical/models")

text = '''Keratinocyte growth factor and acidic fibroblast growth factor are mitogens for primary cultures of mammary epithelium.'''

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("bert_token_classifier_ner_chemprot_pipeline", "en", "clinical/models")

val text = "Keratinocyte growth factor and acidic fibroblast growth factor are mitogens for primary cultures of mammary epithelium."

val result = pipeline.fullAnnotate(text)
```


{:.nlu-block}
```python
import nlu
nlu.load("en.classify.token_bert.chemprot_pipeline").predict("""Keratinocyte growth factor and acidic fibroblast growth factor are mitogens for primary cultures of mammary epithelium.""")
```

</div>



## Results

```bash
|    | ner_chunk    |   begin |   end | ner_label   |   confidence |
|---:|:-------------|--------:|------:|:------------|-------------:|
|  0 | Keratinocyte |       0 |    11 | GENE-Y      |     0.999147 |
|  1 | growth       |      13 |    18 | GENE-Y      |     0.999752 |
|  2 | factor       |      20 |    25 | GENE-Y      |     0.999685 |
|  3 | acidic       |      31 |    36 | GENE-Y      |     0.999661 |
|  4 | fibroblast   |      38 |    47 | GENE-Y      |     0.999753 |
|  5 | growth       |      49 |    54 | GENE-Y      |     0.999771 |
|  6 | factor       |      56 |    61 | GENE-Y      |     0.999742 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_token_classifier_ner_chemprot_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|404.7 MB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- MedicalBertForTokenClassifier
- NerConverter