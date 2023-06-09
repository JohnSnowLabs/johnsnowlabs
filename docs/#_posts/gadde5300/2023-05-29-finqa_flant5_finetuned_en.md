---
layout: model
title: Finance FLAN-T5 Question Answering
author: John Snow Labs
name: finqa_flant5_finetuned
date: 2023-05-29
tags: [en, finance, qa, question_answering, licensed, tensorflow]
task: Question Answering
language: en
edition: Finance NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: FinanceQuestionAnswering
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This Question Answering model has been fine-tuned on FLANT5 using finance data. FLAN-T5 is a state-of-the-art language model developed by Google AI that utilizes the T5 architecture for text generation tasks. This model provides a powerful and efficient solution for accurately answering finance questions and delivering insightful information in the finance domain.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finqa_flant5_finetuned_en_1.0.0_3.0_1685385263205.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finqa_flant5_finetuned_en_1.0.0_3.0_1685385263205.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.MultiDocumentAssembler()\
    .setInputCols("question", "context")\
    .setOutputCols("document_question", "document_context")

fin_qa = finance.QuestionAnswering.pretrained("finqa_flant5_finetuned","en","finance/models")\
    .setInputCols(["document_question", "document_context"])\
    .setCustomPrompt("question: {QUESTION} context: {CONTEXT}")\
    .setMaxNewTokens(50)\
    .setOutputCol("answer")

pipeline = nlp.Pipeline(stages=[document_assembler, fin_qa])

context = "In the world of finance, understanding the concept of risk and return is essential for investors. Risk refers to the uncertainty associated with an investment, while return represents the potential gain or loss. These two factors are intrinsically linked, as higher-risk investments typically offer the potential for higher returns, while lower-risk investments tend to yield lower returns."
question = "What is the relationship between risk and return in the world of finance?"

data = spark.createDataFrame([[question, context]]).toDF("question", "context")
result = pipeline.fit(data).transform(data)
```

</div>

## Results

```bash
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[Risk refers to the uncertainty associated with an investment, while return represents the potential gain or loss. These two factors are intrinsically linked, as higher-risk investments typically offer the potential for higher returns, while lower-risk investments tend to yield lower returns.      ]|
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finqa_flant5_finetuned|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|920.9 MB|
|Case sensitive:|true|

## References

In house annotated dataset