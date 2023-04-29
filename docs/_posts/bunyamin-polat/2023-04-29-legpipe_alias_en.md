---
layout: model
title: Legal Alias Pipeline
author: John Snow Labs
name: legpipe_alias
date: 2023-04-29
tags: [en, ner, legal, licensed, alias]
task: Pipeline Legal
language: en
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline allows you to detect names in quotes and brackets like ("Recipient"), ("Disclosing Parties"), very common in Legal Agreements to reference the parties

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legpipe_alias_en_1.0.0_3.0_1682799794751.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legpipe_alias_en_1.0.0_3.0_1682799794751.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
legal_pipeline = nlp.PretrainedPipeline("legpipe_alias", "en", "legal/models")

text = ["""MUTUAL NON DISCLOSURE AGREEMENT 
This Mutual Non Disclosure Agreement (the “Agreement”) is made on _________ by and between:  
John Snow Labs, a Delaware corporation, registered at 16192 Coastal Highway, Lewes, Delaware 19958 (“John Snow Labs”), and 
Bosonit, S.L, a Spanish corporation, registered at Portales 71, 2º floor, Offices 7,8,9 and 
10. (“Company”), (each a “party” and together the “parties”). 
Recitals: 
John Snow Labs and Company intend to explore the possibility of a business relationship between each other, whereby each party (“Discloser”) may disclose sensitive information to the other party (“Recipient”). 
The parties agree as follows:"""]

result = legal_pipeline.annotate(text)
```

</div>

## Results

```bash
['(“John Snow Labs”)', '(“Company”)', '( “ Discloser ” )', '(“Recipient”)']
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legpipe_alias|
|Type:|pipeline|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|14.5 KB|

## Included Models

- DocumentAssembler
- TokenizerModel
- ContextualParserModel
- ChunkConverter
