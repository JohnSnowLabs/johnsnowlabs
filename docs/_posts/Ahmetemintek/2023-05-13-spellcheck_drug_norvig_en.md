---
layout: model
title: Spell Checker for Drug Names (Norvig)
author: John Snow Labs
name: spellcheck_drug_norvig
date: 2023-05-13
tags: [spellcheck, clinical, en, drug, norvig, licensed]
task: Spell Check
language: en
edition: Healthcare NLP 4.4.0
spark_version: 3.0
supported: true
annotator: NorvigSweetingModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model corrects spelling mistakes in drug names by using The Symmetric Delete spelling correction algorithm which reduces the complexity of edit candidate generation and dictionary lookup for a given Damerau-Levenshtein distance.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/spellcheck_drug_norvig_en_4.4.0_3.0_1684020970665.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/spellcheck_drug_norvig_en_4.4.0_3.0_1684020970665.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = Tokenizer()\
    .setInputCols("document")\
    .setOutputCol("token")

spell = NorvigSweetingModel.pretrained("spellcheck_drug_norvig", "en", "clinical/models")\
    .setInputCols("token")\
    .setOutputCol("corrected_token")\

pipeline = Pipeline(
    stages = [
        documentAssembler,
        tokenizer, 
        spell
        ])

model = pipeline.fit(spark.createDataFrame([['']]).toDF('text')) 

text = "You have to take Amrosia artemisiifoli, Oactra and a bit of Grastk and lastacaf"
test_df= spark.createDataFrame([[text]]).toDF("text")
result= model.transform(test_df)
```
```scala
val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols(Array("document"))
    .setOutputCol("token")

val spell= NorvigSweetingModel.pretrained("spellcheck_drug_norvig", "en", "clinical/models")
    .setInputCols("token")
    .setOutputCol("corrected_token")

val pipeline =  new Pipeline().setStages(Array(documentAssembler, tokenizer, spell))

val data = Seq("You have to take Amrosia artemisiifoli, Oactra and a bit of Grastk and lastacaf").toDS.toDF("text")
val result= pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
Original Text: 
You have to take Amrosia artemisiifoli , Oactra and a bit of Grastk and lastacaf  

Corrected Text: 
You have to take Ambrosia artemisiifolia , Odactra and a bit of Grastek and lastacaft
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|spellcheck_drug_norvig|
|Compatibility:|Healthcare NLP 4.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[token]|
|Output Labels:|[spell]|
|Language:|en|
|Size:|4.5 MB|
|Case sensitive:|true|