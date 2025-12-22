---
layout: model
title: URL Regex Matcher
author: John Snow Labs
name: url_regex_matcher
date: 2025-12-22
tags: [en, regexmatcher, licensed, clinical, url]
task: Contextual Parser
language: en
edition: Healthcare NLP 6.2.2
spark_version: 3.4
supported: true
annotator: RegexMatcherInternalModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts URLs in clinical notes using rule-based RegexMatcherInternal annotator.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/url_regex_matcher_en_6.2.2_3.4_1766402348958.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/url_regex_matcher_en_6.2.2_3.4_1766402348958.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

documentAssembler = DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

url_regex_matcher = RegexMatcherInternalModel.pretrained("url_matcher","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("URL")\

url_regex_matcher_pipeline = Pipeline(
    stages=[
        documentAssembler,
        url_regex_matcher
        ])

data = spark.createDataFrame([
    ["""Name: ID: 1231511863, Driver's License No: A334455B, SSN: 324-59-8674. E-mail: hale@gmail.com.
        For more details, visit our website at www.johnsnowlabs.com or check out http://example.com for general info.
        For secure access, go to https://secure.example.com. File transfers can be done via ftp://files.example.com.
"""]]).toDF("text")


result = url_regex_matcher_pipeline.fit(data).transform(data)


```

{:.jsl-block}
```python

documentAssembler = nlp.DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

url_regex_matcher = medical.RegexMatcherInternalModel.pretrained("url_matcher","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("URL")\

url_regex_matcher_pipeline = nlp.Pipeline(
    stages=[
        documentAssembler,
        url_regex_matcher
        ])

data = spark.createDataFrame([
    ["""Name: ID: 1231511863, Driver's License No: A334455B, SSN: 324-59-8674. E-mail: hale@gmail.com.
        For more details, visit our website at www.johnsnowlabs.com or check out http://example.com for general info.
        For secure access, go to https://secure.example.com. File transfers can be done via ftp://files.example.com.
"""]]).toDF("text")


result = url_regex_matcher_pipeline.fit(data).transform(data)



```
```scala

val documentAssembler = new DocumentAssembler()
	.setInputCol("text")
	.setOutputCol("document")

val url_regex_matcher = RegexMatcherInternalModel.pretrained("url_matcher","en","clinical/models")
	.setInputCols(Array("document"))
	.setOutputCol("URL")

val regex_pipeline = new Pipeline().setStages(Array(
		documentAssembler,
		url_regex_matcher
  ))

val data = Seq("""Name: ID: 1231511863, Driver's License No: A334455B, SSN: 324-59-8674. E-mail: hale@gmail.com.
        For more details, visit our website at www.johnsnowlabs.com or check out http://example.com for general info.
        For secure access, go to https://secure.example.com. File transfers can be done via ftp://files.example.com.
        """).toDF("text")

val result = regex_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

| chunk                      |   begin |   end | label   |
|:---------------------------|--------:|------:|:--------|
| www.johnsnowlabs.com       |     142 |   161 | URL     |
| http://example.com         |     176 |   193 | URL     |
| https://secure.example.com |     246 |   271 | URL     |
| ftp://files.example.com    |     305 |   327 | URL     |



```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|url_regex_matcher|
|Compatibility:|Healthcare NLP 6.2.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[entity_url]|
|Language:|en|
|Size:|2.2 KB|