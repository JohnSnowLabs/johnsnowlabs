---
layout: model
title: Detect Sentences in Healthcare Texts
author: John Snow Labs
name: sentence_detector_dl_healthcare_v2_wip
date: 2024-09-11
tags: [licensed, clinical, en, sentence_detection, sentence, tensorflow]
task: Sentence Detection
language: en
edition: Healthcare NLP 5.4.1
spark_version: 3.0
supported: true
engine: tensorflow
annotator: SentenceDetectorDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

SentenceDetectorDL (SDDL) is based on a general-purpose neural network model for sentence boundary detection. The task of sentence boundary detection is to identify sentences within a text. Many natural language processing tasks take a sentence as an input unit, such as part-of-speech tagging, dependency parsing, named entity recognition, or machine translation.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sentence_detector_dl_healthcare_v2_wip_en_5.4.1_3.0_1726075086487.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sentence_detector_dl_healthcare_v2_wip_en_5.4.1_3.0_1726075086487.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel\
    .pretrained("sentence_detector_dl_healthcare_v2_wip", "en", "clinical/models") \
    .setInputCols(["document"]) \
    .setOutputCol("sentences")


pipeline = Pipeline(
    stages=[
        document_assembler, 
        sentence_detector
    ])

text = """He was given boluses of MS04 with some effect, he has since been placed on a PCA - 
he take 80mg of oxycontin at home, his PCA dose is ~ 2 the morphine dose of the oxycontin, 
he has also received ativan for anxiety. Repleted with 20 meq kcl po, 30 mmol K-phos iv and 2 gms 
mag so4 iv. Size: Prostate gland measures 10x1.1x4.9 cm (LS x AP x TS). Estimated volume is 51.9 ml 
and is mildly enlarged in size. Normal delineation pattern of the prostate gland is preserved.
"""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)
```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetectorDLModel\
    .pretrained("sentence_detector_dl_healthcare_v2_wip", "en", "clinical/models") \
    .setInputCols(["document"]) \
    .setOutputCol("sentences")


pipeline = nlp.Pipeline(
    stages=[
        document_assembler, 
        sentence_detector
    ])

text = """He was given boluses of MS04 with some effect, he has since been placed on a PCA - 
he take 80mg of oxycontin at home, his PCA dose is ~ 2 the morphine dose of the oxycontin, 
he has also received ativan for anxiety. Repleted with 20 meq kcl po, 30 mmol K-phos iv and 2 gms 
mag so4 iv. Size: Prostate gland measures 10x1.1x4.9 cm (LS x AP x TS). Estimated volume is 51.9 ml 
and is mildly enlarged in size. Normal delineation pattern of the prostate gland is preserved.
"""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel
    .pretrained("sentence_detector_dl_healthcare_v2_wip", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val pipeline = new Pipeline().setStages(Array(document_assembler, sentence_detector))

val data = Seq("""He was given boluses of MS04 with some effect, he has since been placed on a PCA - 
he take 80mg of oxycontin at home, his PCA dose is ~ 2 the morphine dose of the oxycontin, 
he has also received ativan for anxiety. Repleted with 20 meq kcl po, 30 mmol K-phos iv and 2 gms 
mag so4 iv. Size: Prostate gland measures 10x1.1x4.9 cm (LS x AP x TS). Estimated volume is 51.9 ml 
and is mildly enlarged in size. Normal delineation pattern of the prostate gland is preserved.
""").toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
|sent_id|sentence                                                                                                                                                                                                                  |
|------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|0      |He was given boluses of MS04 with some effect, he has since been placed on a PCA - \nhe take 80mg of oxycontin at home, his PCA dose is ~ 2 the morphine dose of the oxycontin, \nhe has also received ativan for anxiety.|
|1      |Repleted with 20 meq kcl po, 30 mmol K-phos iv and 2 gms \nmag so4 iv.                                                                                                                                                    |
|2      |Size: Prostate gland measures 10x1.1x4.9 cm (LS x AP x TS).                                                                                                                                                               |
|3      |Estimated volume is 51.9 ml \nand is mildly enlarged in size.                                                                                                                                                             |
|4      |Normal delineation pattern of the prostate gland is preserved.                                                                                                                                                            |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sentence_detector_dl_healthcare_v2_wip|
|Compatibility:|Healthcare NLP 5.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[sentences]|
|Language:|en|
|Size:|377.4 KB|

## References

The healthcare sentence detector DL model is trained on in-house domain-specific data.
