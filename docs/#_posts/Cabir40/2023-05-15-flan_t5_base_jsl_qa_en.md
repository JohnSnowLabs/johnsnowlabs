---
layout: model
title: Medical Question Answering (flan_t5_base_jsl_qa)
author: John Snow Labs
name: flan_t5_base_jsl_qa
date: 2023-05-15
tags: [licensed, clinical, en, qa, question_answering, flan_t5, tensorflow]
task: Question Answering
language: en
edition: Healthcare NLP 4.4.2
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MedicalQuestionAnswering
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The flan_t5_base_jsl_qa model is designed to work seamlessly with the MedicalQuestionAnswering annotator. This model provides a powerful and efficient solution for accurately answering medical questions and delivering insightful information in the medical domain.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/flan_t5_base_jsl_qa_en_4.4.2_3.0_1684180120739.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/flan_t5_base_jsl_qa_en_4.4.2_3.0_1684180120739.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = MultiDocumentAssembler()\
    .setInputCols("question", "context")\
    .setOutputCols("document_question", "document_context")

med_qa = MedicalQuestionAnswering.pretrained("flan_t5_base_jsl_qa","en","clinical/models")\
    .setInputCols(["document_question", "document_context"])\
    .setCustomPrompt("{DOCUMENT} {QUESTION}")\
    .setMaxNewTokens(50)\
    .setOutputCol("answer")\

pipeline = Pipeline(stages=[document_assembler, med_qa])

#doi: 10.3758/s13414-011-0157-z.
paper_abstract = "The visual indexing theory proposed by Zenon Pylyshyn (Cognition, 32, 65-97, 1989) predicts that visual attention mechanisms are employed when mental images are projected onto a visual scene."
long_question = "What is the effect of directing attention on memory?"

data = spark.createDataFrame([[long_question, paper_abstract]]).toDF("question", "context")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new MultiDocumentAssembler()
    .setInputCols("question", "context")
    .setOutputCols("document_question", "document_context")

val med_qa = MedicalQuestionAnswering.pretrained("flan_t5_base_jsl_qa", "en", "clinical/models")
    .setInputCols(Array("document_question", "document_context"))
    .setOutputCol("answer")
    .setMaxNewTokens(50)
    .setCustomPrompt("{DOCUMENT} {QUESTION}")

val pipeline = new Pipeline().setStages(Array(document_assembler, med_qa))

paper_abstract = "The visual indexing theory proposed by Zenon Pylyshyn (Cognition, 32, 65–97, 1989) predicts that visual attention mechanisms are employed when mental images are projected onto a visual scene. Recent eye-tracking studies have supported this hypothesis by showing that people tend to look at empty places where requested information has been previously presented. However, it has remained unclear to what extent this behavior is related to memory performance. The aim of the present study was to explore whether the manipulation of spatial attention can facilitate memory retrieval. In two experiments, participants were asked first to memorize a set of four objects and then to determine whether a probe word referred to any of the objects. The results of both experiments indicate that memory accuracy is not affected by the current focus of attention and that all the effects of directing attention to specific locations on response times can be explained in terms of stimulus–stimulus and stimulus–response spatial compatibility."

long_question = "What is the effect of directing attention on memory?"
yes_no_question = "Does directing attention improve memory for items?"

val data = Seq( 
    (long_question, paper_abstract, ))
    .toDS.toDF("question", "context")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[The effect of directing attention on memory is that it can help to improve memory retention and recall. It can help to reduce the amount of time spent on tasks, such as focusing on one task at a time, or focusing on ]|
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|flan_t5_base_jsl_qa|
|Compatibility:|Healthcare NLP 4.4.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|920.8 MB|
|Case sensitive:|true|
