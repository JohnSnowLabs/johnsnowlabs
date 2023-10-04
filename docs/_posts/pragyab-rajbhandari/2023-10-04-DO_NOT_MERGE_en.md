---
layout: model
title: THIS_IS_A_TEST
author: John Snow Labs
name: DO_NOT_MERGE
date: 2023-10-04
tags: [en, licensed]
task: Named Entity Recognition
language: en
edition: Spark NLP 4.3.1
spark_version: 3.2
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

THIS IS A TEST

## Predicted Entities

`Pathogen`, `Medicine`, `MedicalCondition`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/models-hub-auxdata/clinical/models/DO_NOT_MERGE_en_4.3.1_3.2_1696447791818.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://models-hub-auxdata/clinical/models/DO_NOT_MERGE_en_4.3.1_3.2_1696447791818.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()
			.setInputCol("text")
			.setOutputCol("

sentence_detector = SentenceDetector()
			.setInputCols(["document"])
			.setOutputCol("sentence")
			.setCustomBounds([""])

tokenizer = Tokenizer()
		.setInputCols(["sentence"])
		.setOutputCol(\"token\")
		.setSplitChars(['-'])"

word_embeddings = WordEmbeddingsModel()
			.pretrained("glove_100d", "en", "clinical/models")
			.setInputCols(["sentence", "token"])
			.setOutputCol("embeddings")

ner = MedicalNerModel().pretrained("ner_TestAnalyticsPage2", "en","clinical/models")
		.setInputCols(["sentence", "token", "embeddings"])
		.setOutputCol("ner")

ner_converter = NerConverter()
			.setInputCols(["sentence", "token", "ner"])
			.setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[document_assembler,
			    sentence_detector,
			    tokenizer,
			    word_embeddings,
			    ner,
			    ner_converter])

data = spark.createDataFrame([["SAMPLE TEXT"]]).toDF("text")
result = pipeline.fit(data).transform(data)

```

</div>

## Results

```bash
THIS IS RESULTS
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|DO_NOT_MERGE|
|Compatibility:|Spark NLP 4.3.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|2.5 MB|
|Dependencies:|glove_100d|