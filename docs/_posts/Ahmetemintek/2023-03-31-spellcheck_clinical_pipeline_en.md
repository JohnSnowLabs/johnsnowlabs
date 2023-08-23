---
layout: model
title: Medical Spell Checker Pipeline
author: John Snow Labs
name: spellcheck_clinical_pipeline
date: 2023-03-31
tags: [spellcheck, medical, medical_spell_check, spell_corrector, spell_pipeline, en, licensed, clinical]
task: Pipeline Healthcare
language: en
edition: Healthcare NLP 4.3.2
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained medical spellchecker pipeline is built on the top of `spellcheck_clinical` model. This pipeline is for PySpark 2.4.x users with SparkNLP 3.4.2 and above.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/CONTEXTUAL_SPELL_CHECKER.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/spellcheck_clinical_pipeline_en_4.3.2_3.2_1680277489830.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/spellcheck_clinical_pipeline_en_4.3.2_3.2_1680277489830.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("spellcheck_clinical_pipeline", "en", "clinical/models")
example = ["Witth the hell of phisical terapy the patient was imbulated and on postoperative, the impatient tolerating a post curgical soft diet.",
           "With paint wel controlled on orall pain medications, she was discharged too reihabilitation facilitay.",
           "Abdomen is sort, nontender, and nonintended.",
           "Patient not showing pain or any wealth problems.",
           "No cute distress"]
pipeline.fullAnnotate(example)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("spellcheck_clinical_pipeline", "en", "clinical/models")
val example = Array("Witth the hell of phisical terapy the patient was imbulated and on postoperative, the impatient tolerating a post curgical soft diet.",
           "With paint wel controlled on orall pain medications, she was discharged too reihabilitation facilitay.",
           "Abdomen is sort, nontender, and nonintended.",
           "Patient not showing pain or any wealth problems.",
           "No cute distress")
pipeline.fullAnnotate(example)
```


{:.nlu-block}
```python
import nlu
nlu.load("en.spell.clinical.pipeline").predict("""Witth the hell of phisical terapy the patient was imbulated and on postoperative, the impatient tolerating a post curgical soft diet.""")
```

</div>

## Results

```bash
[{'checked': ['With','the','cell','of','physical','therapy','the','patient','was','ambulated','and','on','postoperative',',','the','patient','tolerating','a','post','surgical','soft','diet','.'],
  'document': ['Witth the hell of phisical terapy the patient was imbulated and on postoperative, the impatient tolerating a post curgical soft diet.'],
  'token': ['Witth','the','hell','of','phisical','terapy','the','patient','was','imbulated','and','on','postoperative',',','the','impatient','tolerating','a','post','curgical','soft','diet','.']},
 
 {'checked': ['With','pain','well','controlled','on','oral','pain','medications',',','she','was','discharged','to','rehabilitation','facility','.'],
  'document': ['With paint wel controlled on orall pain medications, she was discharged too reihabilitation facilitay.'],
  'token': ['With','paint','wel','controlled','on','orall','pain','medications',',','she','was','discharged','too','reihabilitation','facilitay','.']},
 
 {'checked': ['Abdomen','is','soft',',','nontender',',','and','nondistended','.'],
  'document': ['Abdomen is sort, nontender, and nonintended.'],
  'token': ['Abdomen','is','sort',',','nontender',',','and','nonintended','.']},
 
 {'checked': ['Patient','not','showing','pain','or','any','health','problems','.'],
  'document': ['Patient not showing pain or any wealth problems.'],
  'token': ['Patient','not','showing','pain','or','any','wealth','problems','.']},
 
 {'checked': ['No', 'acute', 'distress'],
  'document': ['No cute distress'],
  'token': ['No', 'cute', 'distress']}]
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|spellcheck_clinical_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|100.1 MB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- ContextSpellCheckerModel