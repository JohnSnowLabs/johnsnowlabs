---
layout: model
title: Cancer Diagnosis Text Matcher
author: John Snow Labs
name: cancer_dx_matcher
date: 2024-06-12
tags: [en, licensed, cancer, textmatcher]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.3.3
spark_version: 3.0
supported: true
annotator: TextMatcherInternalModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts cancer diagnoses in clinical notes using a rule-based TextMatcherInternal annotator.

## Predicted Entities

`cancer_dx`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/cancer_dx_matcher_en_5.3.3_3.0_1718227331876.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/cancer_dx_matcher_en_5.3.3_3.0_1718227331876.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

text_matcher = TextMatcherInternalModel.pretrained("cancer_dx_matcher","en","clinical/models") \
    .setInputCols(["sentence", "token"])\
    .setOutputCol("cancer_dx")\
    .setMergeOverlapping(True)

mathcer_pipeline = Pipeline().setStages([
    documentAssembler,
    sentenceDetector,
    tokenizer,
    text_matcher])

data = spark.createDataFrame([["""A 65-year-old woman had a history of debulking surgery, bilateral oophorectomy with omentectomy,
 total anterior hysterectomy with radical pelvic lymph nodes dissection due to ovarian carcinoma (mucinous-type carcinoma, stage Ic) 1 year ago.
 The patient's medical compliance was poor and failed to complete her chemotherapy (cyclophosphamide 750 mg/m2, carboplatin 300 mg/m2). Recently, she noted a palpable right breast mass, 15 cm in size which nearly occupied the whole right breast in 2 months. Core needle biopsy revealed metaplastic carcinoma. Neoadjuvant chemotherapy with the regimens of Taxotere (75 mg/m2), Epirubicin (75 mg/m2), and Cyclophosphamide (500 mg/m2) was given for 6 cycles with poor response, followed by a modified radical mastectomy (MRM) with dissection of axillary lymph nodes and skin grafting. Postoperatively, radiotherapy was done with 5000 cGy in 25 fractions. The histopathologic examination revealed a metaplastic carcinoma with squamous differentiation associated with adenomyoepithelioma. Immunohistochemistry study showed that the tumor cells are positive for epithelial markers-cytokeratin (AE1/AE3) stain, and myoepithelial markers, including cytokeratin 5/6 (CK 5/6), p63, and S100 stains.
 Expressions of hormone receptors, including ER, PR, and Her-2/Neu, were all negative."""]]).toDF("text")

result = mathcer_pipeline.fit(data).transform(data)
```
```scala
val documentAssembler = new DocumentAssembler()
	.setInputCol("text")
	.setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
	.setInputCols(Array("document"))
	.setOutputCol("sentence")

val tokenizer = new Tokenizer()
	.setInputCols(Array("sentence"))
	.setOutputCol("token")

val text_matcher = TextMatcherInternalModel.pretrained("cancer_dx_matcher","en","clinical/models")
	.setInputCols(Array("sentence","token"))
	.setOutputCol("cancer_dx")
	.setMergeOverlapping(true)

val mathcer_pipeline = new Pipeline()
	.setStages(Array(
		documentAssembler,
		sentenceDetector,
		tokenizer,
		text_matcher))

val data = Seq("""A 65-year-old woman had a history of debulking surgery, bilateral oophorectomy with omentectomy,
 total anterior hysterectomy with radical pelvic lymph nodes dissection due to ovarian carcinoma (mucinous-type carcinoma, stage Ic) 1 year ago.
 The patient's medical compliance was poor and failed to complete her chemotherapy (cyclophosphamide 750 mg/m2, carboplatin 300 mg/m2). Recently, she noted a palpable right breast mass, 15 cm in size which nearly occupied the whole right breast in 2 months. Core needle biopsy revealed metaplastic carcinoma. Neoadjuvant chemotherapy with the regimens of Taxotere (75 mg/m2), Epirubicin (75 mg/m2), and Cyclophosphamide (500 mg/m2) was given for 6 cycles with poor response, followed by a modified radical mastectomy (MRM) with dissection of axillary lymph nodes and skin grafting. Postoperatively, radiotherapy was done with 5000 cGy in 25 fractions. The histopathologic examination revealed a metaplastic carcinoma with squamous differentiation associated with adenomyoepithelioma. Immunohistochemistry study showed that the tumor cells are positive for epithelial markers-cytokeratin (AE1/AE3) stain, and myoepithelial markers, including cytokeratin 5/6 (CK 5/6), p63, and S100 stains.
 Expressions of hormone receptors, including ER, PR, and Her-2/Neu, were all negative.""") .toDF("text")

val result = mathcer_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------------------+-----+----+---------+
|                  chunk|begin| end|    label|
+-----------------------+-----+----+---------+
|      ovarian carcinoma|  176| 192|Cancer_dx|
|mucinous-type carcinoma|  195| 217|Cancer_dx|
|  metaplastic carcinoma|  528| 548|Cancer_dx|
|  metaplastic carcinoma|  937| 957|Cancer_dx|
|    adenomyoepithelioma| 1005|1023|Cancer_dx|
+-----------------------+-----+----+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|cancer_dx_matcher|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[cancer_name]|
|Language:|en|
|Size:|43.8 KB|
|Case sensitive:|false|