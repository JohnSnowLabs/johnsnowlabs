---
layout: model
title: Legal Question Answering (MPRE)
author: John Snow Labs
name: legqa_flant5_mpre
date: 2023-09-04
tags: [qa, question_answering, legal, mpre, en, licensed, tensorflow]
task: Question Answering
language: en
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MedicalQuestionAnswering
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This Question Answering model has been fine-tuned on FLANT5 using legal MPRE data. MPRE stands for Multistate Professional Responsibility Examination. The dataset contains examples of questions from past MPRE exams along with their answers and explanations. This model provides a powerful and efficient solution for accurately answering the questions and delivering insightful information.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legqa_flant5_mpre_en_1.0.0_3.0_1693846701106.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legqa_flant5_mpre_en_1.0.0_3.0_1693846701106.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.MultiDocumentAssembler()\
    .setInputCols("question", "context")\
    .setOutputCols("document_question", "document_context")

leg_qa = legal.QuestionAnswering.pretrained("legqa_flant5_mpre","en","legal/models")\
    .setInputCols(["document_question", "document_context"])\
    .setCustomPrompt("question: {QUESTION} context: {CONTEXT}")\
    .setMaxNewTokens(50)\
    .setOutputCol("answer")

pipeline = nlp.Pipeline(stages=[document_assembler, leg_qa])

context = "Mr. Burns, the chief executive officer of Conglomerate Corporation, now faces criminal charges of discussing prices with the president of a competing firm. If found guilty, both Mr. Burns and Conglomerate Corporation will be subject to civil and criminal penalties under state and federal antitrust laws. An attorney has been representing Conglomerate Corporation. She has conducted a thorough investigation of the matter, and she has personally concluded that no such pricing discussions occurred. Both Conglomerate Corporation and Mr. Burns plan to defend on that ground. Mr. Burns has asked the attorney to represent him, as well as Conglomerate Corporation, in the proceedings. The legal and factual defenses of Conglomerate Corporation and Mr. Burns seem completely consistent at the outset of the matter. Would the attorney need to obtain informed consent to a conflict of interest from both Mr."

question = " Burns and a separate corporate officer at Conglomerate Corporation before proceeding with this dual representation?"


data = spark.createDataFrame([[question, context]]).toDF("question", "context")

result = pipeline.fit(data).transform(data)
```

</div>

## Results

```bash
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[Yes, because the conflicting positions in the legal and factual defenses require the attorney to obtain the informed consent of both clients before proceeding with the representation. ]|
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legqa_flant5_mpre|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.6 GB|
|Case sensitive:|true|

## References

In house annotated dataset