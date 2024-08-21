---
layout: model
title: IP Regex Matcher
author: John Snow Labs
name: ip_matcher
date: 2024-08-21
tags: [en, clinical, licensed, ip, regexmatcher]
task: Contextual Parser
language: en
edition: Healthcare NLP 5.4.0
spark_version: 3.0
supported: true
annotator: RegexMatcherInternalModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts IPs  using rule-based RegexMatcherInternal annotator.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ip_matcher_en_5.4.0_3.0_1724235903374.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ip_matcher_en_5.4.0_3.0_1724235903374.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

ip_regex_matcher = RegexMatcherInternalModel.pretrained("ip_matcher","en","clinical/models") \
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
        Visit http://198.51.100.42 for more information. File transfers can be done via ftp://files.example.com.""").toDF("text")

val result = regex_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-------------+-----+---+-----+
|chunk        |begin|end|label|
+-------------+-----+---+-----+
|192.168.0.1  |131  |141|IP   |
|10.0.0.1     |180  |187|IP   |
|198.51.100.42|235  |247|IP   |
+-------------+-----+---+-----+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ip_matcher|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[IP]|
|Language:|en|
|Size:|2.3 KB|