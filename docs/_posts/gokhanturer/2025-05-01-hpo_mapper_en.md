---
layout: model
title: Mapping Phenotype Entities with Corresponding HPO Codes
author: John Snow Labs
name: hpo_mapper
date: 2025-05-01
tags: [en, clinical, licensed, hpo]
task: Chunk Mapping
language: en
edition: Healthcare NLP 6.0.0
spark_version: 3.0
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is designed to map extracted phenotype entities from clinical or biomedical text to their corresponding Human Phenotype Ontology (HPO) codes. It ensures that observed symptoms, signs, and clinical abnormalities are standardized using HPO terminology.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hpo_mapper_en_6.0.0_3.0_1746106791365.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hpo_mapper_en_6.0.0_3.0_1746106791365.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

stopwords_cleaner = StopWordsCleaner()\
    .setInputCols("token")\
    .setOutputCol("cleanTokens")\
    .setCaseSensitive(False)

token_assembler = TokenAssembler()\
    .setInputCols(['document',"cleanTokens"])\
    .setOutputCol("cleanTokens_newDoc")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models") \
    .setInputCols(["cleanTokens_newDoc"]) \
    .setOutputCol("sentence") 

tokenizer_2 = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("clean_tokens")

entityExtractor = TextMatcherInternalModel().pretrained("hpo_matcher","en", "clinical/models")\
    .setInputCols(["sentence", "clean_tokens"])\
    .setOutputCol("hpo_term")\
    .setCaseSensitive(False)\
    .setMergeOverlapping(False)

mapper = ChunkMapperModel().pretrained("hpo_mapper","en", "clinical/models")\
    .setInputCols(["hpo_term"])\
    .setOutputCol("hpo_code")\
    .setLowerCase(True)

mapper_pipeline = Pipeline().setStages([
                  documentAssembler,                  
                  tokenizer,
                  stopwords_cleaner,
                  token_assembler,
                  sentenceDetector,
                  tokenizer_2,
                  entityExtractor,
                  mapper])

text =  ''' APNEA: Presumed apnea of prematurity since < 34 wks gestation at birth.
HYPERBILIRUBINEMIA: At risk for hyperbilirubinemia d/t prematurity. 
1/25-1/30: Received Amp/Gent while undergoing sepsis evaluation. '''

data = spark.createDataFrame([[text]]).toDF("text")
 
mapper_model = mapper_pipeline.fit(data).transform(data)
```

{:.jsl-block}
```python
documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

stopwords_cleaner = nlp.StopWordsCleaner()\
    .setInputCols("token")\
    .setOutputCol("cleanTokens")\
    .setCaseSensitive(False)

token_assembler = nlp.TokenAssembler()\
    .setInputCols(['document',"cleanTokens"])\
    .setOutputCol("cleanTokens_newDoc")

sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models") \
    .setInputCols(["cleanTokens_newDoc"]) \
    .setOutputCol("sentence") 

tokenizer_2 = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("clean_tokens")

entityExtractor = medical.TextMatcherInternalModel().pretrained("hpo_matcher","en", "clinical/models")\
    .setInputCols(["sentence", "clean_tokens"])\
    .setOutputCol("hpo_term")\
    .setCaseSensitive(False)\
    .setMergeOverlapping(False)

mapper = medical.ChunkMapperModel().pretrained("hpo_mapper","en", "clinical/models")\
    .setInputCols(["hpo_term"])\
    .setOutputCol("hpo_code")\
    .setLowerCase(True)

mapper_pipeline = nlp.Pipeline().setStages([
                  documentAssembler,                  
                  tokenizer,
                  stopwords_cleaner,
                  token_assembler,
                  sentenceDetector,
                  tokenizer_2,
                  entityExtractor,
                  mapper])

text =  ''' APNEA: Presumed apnea of prematurity since < 34 wks gestation at birth.
HYPERBILIRUBINEMIA: At risk for hyperbilirubinemia d/t prematurity. 
1/25-1/30: Received Amp/Gent while undergoing sepsis evaluation. '''

data = spark.createDataFrame([[text]]).toDF("text")
 
mapper_model = mapper_pipeline.fit(data).transform(data)
```
```scala
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("token")

val stopwordsCleaner = new StopWordsCleaner()
  .setInputCols("token")
  .setOutputCol("cleanTokens")
  .setCaseSensitive(false)

val tokenAssembler = new TokenAssembler()
  .setInputCols(Array("document", "cleanTokens"))
  .setOutputCol("cleanTokens_newDoc")

val sentenceDetector = SentenceDetectorDLModel
  .pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
  .setInputCols(Array("cleanTokens_newDoc"))
  .setOutputCol("sentence")

val tokenizer2 = new Tokenizer()
  .setInputCols("sentence")
  .setOutputCol("clean_tokens")

val entityExtractor = TextMatcherInternalModel
  .pretrained("hpo_matcher", "en", "clinical/models")
  .setInputCols(Array("sentence", "clean_tokens"))
  .setOutputCol("hpo_term")
  .setCaseSensitive(false)
  .setMergeOverlapping(false)

val mapper = medical.ChunkMapperModel
    .pretrained("hpo_mapper", "en", "clinical/models")\
    .setInputCols("hpo_term")
    .setOutputCol("hpo_code")
    .setLowerCase(True)

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  tokenizer,
  stopwordsCleaner,
  tokenAssembler,
  sentenceDetector,
  tokenizer2,
  entityExtractor,
  mapper
))

val data = Seq("""APNEA: Presumed apnea of prematurity since < 34 wks gestation at birth.
GENETICS: Holds thumbs in palms, findings on Hemolytic Uremic Syndrome, history of meconium plugs.
HYPERBILIRUBINEMIA: At risk for hyperbilirubinemia d/t prematurity. 
1/25-1/30: Received Amp/Gent while undergoing sepsis evaluation.""").toDF("text")

val mapper = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+------------------+-----+---+-----+----------+
|             chunk|begin|end|label|  hpo_code|
+------------------+-----+---+-----+----------+
|             APNEA|    0|  4|  HPO|HP:0002104|
|             apnea|   16| 20|  HPO|HP:0002104|
|HYPERBILIRUBINEMIA|   66| 83|  HPO|HP:0002904|
|hyperbilirubinemia|   91|108|  HPO|HP:0002904|
|            sepsis|  167|172|  HPO|HP:0100806|
+------------------+-----+---+-----+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hpo_mapper|
|Compatibility:|Healthcare NLP 6.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[hpo_code]|
|Language:|en|
|Size:|1.5 MB|