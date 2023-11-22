---
layout: model
title: test
author: John Snow Labs
name: ner_LungCancer10
date: 2023-11-22
tags: [en, licensed]
task: Named Entity Recognition
language: en
edition: Spark NLP 5.1.0
spark_version: 3.2
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

test

## Predicted Entities

`Adenopathy`, `Confirmed`, `SiteLiver`, `Dosage`, `HormonalTherapy`, `Metastasis`, `RelativeDate`, `Staging`, `Pathology_Result`, `UnspecificTherapy`, `RadiationDose`, `Biomarker_Result`, `SiteBone`, `Family`, `CancerScore`, `Past`, `Cyclecount`, `SiteBreast`, `Form`, `Tumor_Finding`, `Grade`, `DocSplit_NOT_NER`, `Cyclelength`, `SizeTrend`, `Absent`, `Chemotherapy`, `Frequency`, `Hypothetical`, `HistologicalType`, `TargetedTherapy`, `SiteBrain`, `PalliativeTreatment`, `Possible`, `Biomarker`, `Invasion`, `Oncogene`, `Planned`, `Route`, `SiteLymphNode`, `RelativeTime`, `Duration`, `Race_Ethnicity`, `Age`, `PerformanceStatus`, `LineOfTherapy`, `Immunotherapy`, `Cyclenumber`, `Date`, `ImagingTest`, `Death_Entity`, `CancerSurgery`, `ResponseToTreatment`, `Direction`, `BenignTumor`, `Gender`, `Radiotherapy`, `Cycleday`, `Strength`, `TumorSize`, `Lymph_Node_Modifier`, `CancerDx`, `Suspected`, `SiteOtherBodyPart`, `Cycledose`, `SmokingStatus`, `SiteLung`, `PathologyTest`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_LungCancer10_en_5.1.0_3.2_1700653747566.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_LungCancer10_en_5.1.0_3.2_1700653747566.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel().pretrained("ner_LungCancer10", "en" , "clinical/models")
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
asdasd
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_LungCancer10|
|Compatibility:|Spark NLP 5.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|3.0 MB|
|Dependencies:|embeddings_clinical|