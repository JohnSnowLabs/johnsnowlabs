---
layout: model
title: sss
author: John Snow Labs
name: ner_healthcare
date: 2023-10-23
tags: [en, licensed]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.1.0
spark_version: 3.2
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

dasda

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/models-hub-auxdata/clinical/models/ner_healthcare_en_5.1.0_3.2_1698084867443.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://models-hub-auxdata/clinical/models/ner_healthcare_en_5.1.0_3.2_1698084867443.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()
			.setInputCol("text")
			.setOutputCol("document")

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

ner = MedicalNerModel().pretrained("ner_healthcare", "en","clinical/models")
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

data = spark.createDataFrame([["SAMPLE_TEXT"]]).toDF("text")
result = pipeline.fit(data).transform(data)
```

</div>

## Results

```bash
dasdasda
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_healthcare|
|Compatibility:|Healthcare NLP 5.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|2.5 MB|
|Dependencies:|glove_100d|