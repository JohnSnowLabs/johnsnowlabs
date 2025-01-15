---
layout: model
title: asd
author: John Snow Labs
name: ner_Colorectal_Cancer_Training_Set1
date: 2025-01-15
tags: [en, licensed]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.4.1
spark_version: 3.4
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

asd

## Predicted Entities

`Metastasis`, `Hypothetical`, `SizeTrend`, `Pathology_Result`, `Direction`, `CancerDx`, `RelativeTime`, `Race_Ethnicity`, `Biomarker`, `Family`, `TargetedTherapy`, `Chemotherapy`, `Immunotherapy`, `Past`, `SomeoneElse`, `Staging`, `Adenopathy`, `HistologicalType`, `Cycleday`, `Cyclenumber`, `TumorSize`, `CancerSurgery`, `Form`, `SiteLiver`, `Cycledose`, `Frequency`, `SiteBone`, `RelativeDate`, `PathologyTest`, `ResponseToTreatment`, `Invasion`, `SiteLung`, `Absent`, `SiteBreast`, `Strength`, `BenignTumor`, `SiteColorectal`, `Planned`, `Dosage`, `Confirmed`, `Lymph_Node_Modifier`, `Oncogene`, `Cyclecount`, `Gender`, `Duration`, `SiteBrain`, `PerformanceStatus`, `SiteOtherBodyPart`, `ImagingTest`, `Date`, `SiteLymphNode`, `Age`, `Radiotherapy`, `Tumor_Finding`, `LineOfTherapy`, `Suspected`, `Biomarker_Result`, `Grade`, `UnspecificTherapy`, `Route`, `Death_Entity`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_Colorectal_Cancer_Training_Set1_en_5.4.1_3.4_1736952598022.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_Colorectal_Cancer_Training_Set1_en_5.4.1_3.4_1736952598022.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
			.pretrained("embeddings_clinical", "en" , "clinical/models")
			.setInputCols(["sentence", "token"])
			.setOutputCol("embeddings")

ner = MedicalNerModel().pretrained("ner_Colorectal_Cancer_Training_Set1", "en" , "clinical/models")
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
asd
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_Colorectal_Cancer_Training_Set1|
|Compatibility:|Healthcare NLP 5.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|2.9 MB|
|Dependencies:|embeddings_clinical|