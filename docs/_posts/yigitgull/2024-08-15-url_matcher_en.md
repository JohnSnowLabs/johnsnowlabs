---
layout: model
title: URL Regex Matcher
author: John Snow Labs
name: url_matcher
date: 2024-08-15
tags: [en, clinical, licensed, url, regexmatcher]
task: Contextual Parser
language: en
edition: Healthcare NLP 5.4.0
spark_version: 3.4
supported: true
annotator: RegexMatcherInternal
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts URLs in clinical notes using rule-based RegexMatcherInternal annotator.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/url_matcher_en_5.4.0_3.4_1723708721036.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/url_matcher_en_5.4.0_3.4_1723708721036.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

url_regex_matcher = RegexMatcherInternalModel.pretrained("url_matcher","en","clinical/models") \
    .setInputCols(["document"])\
    .setOutputCol("URL")\

flattener = Flattener() \
    .setInputCols("URL") \
    .setExplodeSelectedFields({"URL":["result as chunk",
                                            "begin as begin",
                                            "end as end",
                                            "metadata.entity as label"
                                            ]})

url_regex_matcher_pipeline = Pipeline(
    stages=[
        documentAssembler,
        url_regex_matcher,
        flattener
        ])

data = spark.createDataFrame([
    ["""Name: ID: 1231511863, Driver's License No: A334455B, SSN: 324-59-8674. E-mail: hale@gmail.com.
        For more details, visit our website at www.johnsnowlabs.com or check out http://example.com for general info.
        For secure access, go to https://secure.example.com. File transfers can be done via ftp://files.example.com.
"""]]).toDF("text")


url_regex_matcher_model = url_regex_matcher_pipeline.fit(data)
result = url_regex_matcher_model.transform(data)

```
```scala
val documentAssembler = new DocumentAssembler()
	.setInputCol("text")
	.setOutputCol("document")

val url_regex_matcher = RegexMatcherInternalModel.pretrained("url_matcher","en","clinical/models")
	.setInputCols(Array("document"))
	.setOutputCol("URL")

val flattener = new Flattener()
  .setInputCols("URL")
  .setExplodeSelectedFields(Map("URL" -> Array("result as chunk",
                                              "begin as begin",
                                              "end as end",
                                              "metadata.entity as label")))

val regex_pipeline = new Pipeline().setStages(Array(
		documentAssembler,
		url_regex_matcher,
    flattener
  ))

val data = Seq("""Name: ID: 1231511863, Driver's License No: A334455B, SSN: 324-59-8674. E-mail: hale@gmail.com.
        For more details, visit our website at www.johnsnowlabs.com or check out http://example.com for general info.
        For secure access, go to https://secure.example.com. File transfers can be done via ftp://files.example.com.""").toDF("text")

val result = regex_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+--------------------------+-----+---+-----+
|chunk                     |begin|end|label|
+--------------------------+-----+---+-----+
|www.johnsnowlabs.com      |142  |161|URL  |
|http://example.com        |176  |193|URL  |
|https://secure.example.com|247  |272|URL  |
|ftp://files.example.com   |306  |328|URL  |
+--------------------------+-----+---+-----+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|url_matcher|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[URL]|
|Language:|en|
|Size:|907 Bytes|