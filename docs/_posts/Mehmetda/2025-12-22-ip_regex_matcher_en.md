---
layout: model
title: URL Regex Matcher
author: John Snow Labs
name: ip_regex_matcher
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ip_regex_matcher_en_6.2.2_3.4_1766408163989.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ip_regex_matcher_en_6.2.2_3.4_1766408163989.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

documentAssembler = DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

ip_regex_matcher = RegexMatcherInternalModel.pretrained("ip_matcher","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("IP")\

ip_regex_matcher_pipeline = Pipeline(
    stages=[
        documentAssembler,
        ip_regex_matcher
        ])

data = spark.createDataFrame([
    ["""Name: ID: 1231511863, Driver's License No: A334455B, SSN: 324-59-8674. E-mail: hale@gmail.com.
        Access the router at http://192.168.0.1 for configuration. Please connect to 10.0.0.1 to access the database..
        Visit http://198.51.100.42 for more information. File transfers can be done via ftp://files.example.com.
        The backup server is located at 172.16.254.1 and the monitoring system can be reached at 203.0.113.0.
"""]]).toDF("text")


result = ip_regex_matcher_pipeline.fit(data).transform(data)


```

{:.jsl-block}
```python

documentAssembler = nlp.DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

ip_regex_matcher = medical.RegexMatcherInternalModel.pretrained("ip_matcher","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("IP")\

ip_regex_matcher_pipeline = nlp.Pipeline(
    stages=[
        documentAssembler,
        ip_regex_matcher
        ])

data = spark.createDataFrame([
    ["""Name: ID: 1231511863, Driver's License No: A334455B, SSN: 324-59-8674. E-mail: hale@gmail.com.
        Access the router at http://192.168.0.1 for configuration. Please connect to 10.0.0.1 to access the database..
        Visit http://198.51.100.42 for more information. File transfers can be done via ftp://files.example.com.
        The backup server is located at 172.16.254.1 and the monitoring system can be reached at 203.0.113.0.
"""]]).toDF("text")


result = ip_regex_matcher_pipeline.fit(data).transform(data)



```
```scala

val documentAssembler = new DocumentAssembler()
	.setInputCol("text")
	.setOutputCol("document")

val ip_regex_matcher = RegexMatcherInternalModel.pretrained("ip_matcher","en","clinical/models")
	.setInputCols(Array("document"))
	.setOutputCol("IP")

val regex_pipeline = new Pipeline().setStages(Array(
		documentAssembler,
		ip_regex_matcher
  ))

val data = Seq("""Name: ID: 1231511863, Driver's License No: A334455B, SSN: 324-59-8674. E-mail: hale@gmail.com.
        Access the router at http://192.168.0.1 for configuration. Please connect to 10.0.0.1 to access the database..
        Visit http://198.51.100.42 for more information. File transfers can be done via ftp://files.example.com.
        The backup server is located at 172.16.254.1 and the monitoring system can be reached at 203.0.113.0.
""").toDF("text")

val result = regex_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

| chunk         |   begin |   end | label   |
|:--------------|--------:|------:|:--------|
| 192.168.0.1   |     131 |   141 | IP      |
| 10.0.0.1      |     180 |   187 | IP      |
| 198.51.100.42 |     235 |   247 | IP      |
| 172.16.254.1  |     367 |   378 | IP      |
| 203.0.113.0   |     424 |   434 | IP      |


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ip_regex_matcher|
|Compatibility:|Healthcare NLP 6.2.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[entity_ip]|
|Language:|en|
|Size:|2.2 KB|