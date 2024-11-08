---
layout: model
title: Email Regex Matcher
author: John Snow Labs
name: email_matcher
date: 2024-08-21
tags: [en, clinical, email, licensed, regexmatcher]
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

This model extracts emails in clinical notes using rule-based RegexMatcherInternal annotator.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/email_matcher_en_5.4.0_3.0_1724236339739.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/email_matcher_en_5.4.0_3.0_1724236339739.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

email_regex_matcher = RegexMatcherInternalModel.pretrained("email_matcher","en","clinical/models") \
    .setInputCols(["document"])\
    .setOutputCol("EMAIL")\

email_regex_matcher_pipeline = Pipeline(
    stages=[
        documentAssembler,
        email_regex_matcher
        ])

data = spark.createDataFrame([["""ID: 1231511863, The driver's license no:A334455B, the SSN:324598674 and info@domain.net, mail: tech@support.org, e-mail: hale@gmail.com .
 E-mail: sales@gmail.com."""]]).toDF("text")


email_regex_matcher_model = email_regex_matcher_pipeline.fit(data)
result = email_regex_matcher_model.transform(data)

```
```scala
val documentAssembler = new DocumentAssembler()
	.setInputCol("text")
	.setOutputCol("document")

val email_regex_matcher = RegexMatcherInternalModel.pretrained("email_matcher","en","clinical/models")
	.setInputCols(Array("document"))
	.setOutputCol("EMAIL")

val email_regex_pipeline = new Pipeline().setStages(Array(
		documentAssembler,
		email_regex_matcher
  ))

val data = Seq("""ID: 1231511863, The driver's license no:A334455B, the SSN:324598674 and info@domain.net, mail: tech@support.org, e-mail: hale@gmail.com .
 E-mail: sales@gmail.com.""").toDF("text")

val result = email_regex_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------+-----+---+-----+
|chunk           |begin|end|label|
+----------------+-----+---+-----+
|info@domain.net |72   |86 |EMAIL|
|tech@support.org|95   |110|EMAIL|
|hale@gmail.com  |121  |134|EMAIL|
|sales@gmail.com |147  |161|EMAIL|
+----------------+-----+---+-----+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|email_matcher|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[EMAIL]|
|Language:|en|
|Size:|2.2 KB|