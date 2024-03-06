---
layout: model
title: Biomarker Text Matcher
author: John Snow Labs
name: biomarker_matcher
date: 2024-03-06
tags: [en, licensed, biomarker, textmatcher]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.3.0
spark_version: 3.0
supported: true
annotator: TextMatcherInternalModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Extracts biomarker entities using rule based `TextMatcherInternal` annotator.

## Predicted Entities

`Biomarker`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biomarker_matcher_en_5.3.0_3.0_1709748724355.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biomarker_matcher_en_5.3.0_3.0_1709748724355.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

text_matcher = TextMatcherInternalModel.pretrained("biomarker_matcher","en","clinical/models") \
    .setInputCols(["document", "token"])\
    .setOutputCol("matched_text")\

mathcer_pipeline = Pipeline().setStages([
                  documentAssembler,
                  tokenizer,
                  text_matcher])

data = spark.createDataFrame([["In the bone- marrow (BM) aspiration, blasts accounted for 88.1% of ANCs, which were positive for CD20, CD34, CD38, CD58, CD66c, CD123, HLA-DR, cCD79a, and TdT on flow cytometry. Measurements of serum tumor markers showed elevated level of cytokeratin 19 fragment (Cyfra21-1: 4.77 ng/mL), neuron-specific enolase (NSE: 19.60 ng/mL), and squamous cell carcinoma antigen (SCCA: 2.58 ng/mL)."]]).toDF("text")

matcher_model = mathcer_pipeline.fit(data)
result = matcher_model.transform(data)
```
```scala
val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
	
val tokenizer = new Tokenizer()
    .setInputCols(Array("document"))
    .setOutputCol("token")
	
val text_matcher = TextMatcherInternalModel.pretrained("biomarker_matcher","en","clinical/models")
    .setInputCols(Array("document","token"))
    .setOutputCol("matched_text")
	
val mathcer_pipeline = new Pipeline()
    .setStages(Array(documentAssembler,
	             tokenizer,
 	             text_matcher))
	
val data = Seq("In the bone- marrow (BM) aspiration, blasts accounted for 88.1% of ANCs, which were positive for CD20, CD34, CD38, CD58, CD66c, CD123, HLA-DR, cCD79a, and TdT on flow cytometry. Measurements of serum tumor markers showed elevated level of cytokeratin 19 fragment (Cyfra21-1: 4.77 ng/mL), neuron-specific enolase (NSE: 19.60 ng/mL), and squamous cell carcinoma antigen (SCCA: 2.58 ng/mL).") .toDF("text")
	
val matcher_model = mathcer_pipeline.fit(data)
	
val result = matcher_model.transform(data)
```
</div>

## Results

```bash
+-------------------------------+-----+---+---------+
|                          chunk|begin|end|    label|
+-------------------------------+-----+---+---------+
|                           CD20|   97|100|Biomarker|
|                           CD34|  103|106|Biomarker|
|                           CD38|  109|112|Biomarker|
|                           CD58|  115|118|Biomarker|
|                          CD66c|  121|125|Biomarker|
|                          CD123|  128|132|Biomarker|
|                         HLA-DR|  135|140|Biomarker|
|                         cCD79a|  143|148|Biomarker|
|                            TdT|  155|157|Biomarker|
|        cytokeratin 19 fragment|  239|261|Biomarker|
|                      Cyfra21-1|  264|272|Biomarker|
|        neuron-specific enolase|  288|310|Biomarker|
|                            NSE|  313|315|Biomarker|
|squamous cell carcinoma antigen|  336|366|Biomarker|
|                           SCCA|  369|372|Biomarker|
+-------------------------------+-----+---+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biomarker_matcher|
|Compatibility:|Healthcare NLP 5.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[matched_text]|
|Language:|en|
|Size:|26.2 KB|
|Case sensitive:|false|