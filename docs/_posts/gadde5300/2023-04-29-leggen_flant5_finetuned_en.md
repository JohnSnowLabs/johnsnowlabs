---
layout: model
title: Legal Finetuned FLAN-T5 Text Generation
author: John Snow Labs
name: leggen_flant5_finetuned
date: 2023-04-29
tags: [en, legal, text_generation, licensed, tensorflow]
task: Text Generation
language: en
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: LegalTextGenerator
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This Text Generation model has been fine-tuned on FLANT5 Using legal texts. FLAN-T5 is a state-of-the-art language model developed by Facebook AI that utilizes the T5 architecture for text generation tasks.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/leggen_flant5_finetuned_en_1.0.0_3.0_1682797013244.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/leggen_flant5_finetuned_en_1.0.0_3.0_1682797013244.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("question")

flant5 = legal.TextGenerator.pretrained('leggen_flant5_finetuned,'en','legal/models')\
    .setInputCols(["question"])\
    .setOutputCol("generated_text")
    .setMaxNewTokens(150)\
    .setStopAtEos(True)
  
pipeline = nlp.Pipeline(stages=[document_assembler, flant5])

data = spark.createDataFrame([
  [1,'''This exhibit has been redacted and is the subject of a confidential treatment request. redacted material is marked with [* * *] and has been filed separately with the securities and exchange commission. this agreement (this "agreement"), dated december 30, 2016 (the "effective date"), is''']
]).toDF('id', 'text')
results = pipeline.fit(data).transform(data)
results.select("generated_text.result").show(truncate=False)
```

</div>

## Results

```bash
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[The parties agree that this Agreement shall be binding upon and inure to the benefit of the parties, their successors and assigns. The parties further agree that any disputes arising out of or related to this Agreement shall be resolved through binding arbitration. The parties agree to submit to binding arbitration in accordance with the rules of the American Arbitration Association]|
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|leggen_flant5_finetuned|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.6 GB|

## References

In house annotated data
