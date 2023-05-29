---
layout: model
title: Legal FLAN-T5 Question Answering
author: John Snow Labs
name: legqa_flant5_finetuned
date: 2023-05-29
tags: [en, legal, qa, question_answering, licensed, tensorflow]
task: Question Answering
language: en
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: LegalQuestionAnswering
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This Question Answering model has been fine-tuned on FLANT5 using legal data. FLAN-T5 is a state-of-the-art language model developed by Google AI that utilizes the T5 architecture for text generation tasks. This model provides a powerful and efficient solution for accurately answering legal questions and delivering insightful information in the legal domain.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legqa_flant5_finetuned_en_1.0.0_3.0_1685371188640.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legqa_flant5_finetuned_en_1.0.0_3.0_1685371188640.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.MultiDocumentAssembler()\
    .setInputCols("question", "context")\
    .setOutputCols("document_question", "document_context")

leg_qa = legal.QuestionAnswering.pretrained("legqa_flant5_finetuned","en","legal/models")\
    .setInputCols(["document_question", "document_context"])\
    .setCustomPrompt("question: {QUESTION} context: {CONTEXT}")\
    .setMaxNewTokens(50)\
    .setOutputCol("answer")

pipeline = nlp.Pipeline(stages=[document_assembler, leg_qa])

question = 'How often will the incentive rate be reviewed?'
context = '''

The incentive rate shall remain in effect for a period of one year from the effective date. After the one year period, the incentive rate may be adjusted, or new incentive rates may be put in place, as determined by the governing body of Lincoln Parish, Louisiana. 
The incentive rate shall be reviewed annually by the governing body and any changes or adjustments shall be made in accordance with the terms and conditions of this agreement. Furthermore, the incentive rate shall be adjusted to reflect any changes in the cost of production of the oil or the market price of the oil, as determined by the governing body.
If an adjustment is necessary, the governing body shall notify the parties of such adjustment in writing.'''

data = spark.createDataFrame([[question, context]]).toDF("question", "context")

result = pipeline.fit(data).transform(data)
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legqa_flant5_finetuned|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|920.9 MB|
|Case sensitive:|true|

## References

In house annotated dataset
