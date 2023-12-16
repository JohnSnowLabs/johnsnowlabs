---
layout: model
title: Medical Question Answering (biogpt)
author: John Snow Labs
name: medical_qa_biogpt
date: 2023-03-09
tags: [licensed, clinical, en, gpt, biogpt, pubmed, question_answering, tensorflow]
task: Question Answering
language: en
edition: Healthcare NLP 4.3.1
spark_version: 3.0
supported: true
recommended: true
engine: tensorflow
annotator: MedicalQuestionAnswering
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is directly ported from the  official BioGPT [implementation](https://github.com/microsoft/BioGPT)  that is trained on Pubmed abstracts and then finetuned with PubmedQA dataset. It is the baseline version called [BioGPT-QA-PubMedQA-BioGPT](https://msramllasc.blob.core.windows.net/modelrelease/BioGPT/checkpoints/QA-PubMedQA-BioGPT.tgz).
It can generate two types of answers, short and long. Types of questions are supported: `"short"`(producing yes/no/maybe) answers and `"full"` (long answers).

## Predicted Entities



{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/BIOGPT_MEDICAL_QUESTION_ANSWERING/){:.button.button-orange}{:target="_blank"}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/31.Medical_Question_Answering.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}{:target="_blank"}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/medical_qa_biogpt_en_4.3.1_3.0_1678355315206.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/medical_qa_biogpt_en_4.3.1_3.0_1678355315206.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python

document_assembler = MultiDocumentAssembler()\
    .setInputCols("question", "context")\
    .setOutputCols("document_question", "document_context")

med_qa = sparknlp_jsl.annotators.MedicalQuestionAnswering\
    .pretrained("medical_qa_biogpt","en","clinical/models")\
    .setInputCols(["document_question", "document_context"])\
    .setOutputCol("answer")\
    .setMaxNewTokens(30)\
    .setTopK(1)\
    .setQuestionType("long") # "short"

pipeline = Pipeline(stages=[document_assembler, med_qa])

paper_abstract = "The visual indexing theory proposed by Zenon Pylyshyn (Cognition, 32, 65–97, 1989) predicts that visual attention mechanisms are employed when mental images are projected onto a visual scene. Recent eye-tracking studies have supported this hypothesis by showing that people tend to look at empty places where requested information has been previously presented. However, it has remained unclear to what extent this behavior is related to memory performance. The aim of the present study was to explore whether the manipulation of spatial attention can facilitate memory retrieval. In two experiments, participants were asked first to memorize a set of four objects and then to determine whether a probe word referred to any of the objects. The results of both experiments indicate that memory accuracy is not affected by the current focus of attention and that all the effects of directing attention to specific locations on response times can be explained in terms of stimulus–stimulus and stimulus–response spatial compatibility."

long_question = "What is the effect of directing attention on memory?"
yes_no_question = "Does directing attention improve memory for items?"

data = spark.createDataFrame(
    [
        [long_question, paper_abstract, "long"],
        [yes_no_question, paper_abstract, "short"],
    ]
).toDF("question", "context", "question_type")

pipeline.fit(data).transform(data.where("question_type == 'long'"))\
    .select("answer.result")\
    .show(truncate=False)

pipeline.fit(data).transform(data.where("question_type == 'short'"))\
    .select("answer.result")\
    .show(truncate=False)
```
```scala
val document_assembler = new MultiDocumentAssembler()
    .setInputCols("question", "context")
    .setOutputCols("document_question", "document_context")

val med_qa = MedicalQuestionAnswering
    .pretrained("medical_qa_biogpt", "en", "clinical/models")
    .setInputCols(Array("document_question", "document_context"))
    .setOutputCol("answer")
    .setMaxNewTokens(30)
    .setTopK(1)
    .setQuestionType("long") # "short"

val pipeline = new Pipeline().setStages(Array(document_assembler, med_qa))

paper_abstract = "The visual indexing theory proposed by Zenon Pylyshyn (Cognition, 32, 65–97, 1989) predicts that visual attention mechanisms are employed when mental images are projected onto a visual scene. Recent eye-tracking studies have supported this hypothesis by showing that people tend to look at empty places where requested information has been previously presented. However, it has remained unclear to what extent this behavior is related to memory performance. The aim of the present study was to explore whether the manipulation of spatial attention can facilitate memory retrieval. In two experiments, participants were asked first to memorize a set of four objects and then to determine whether a probe word referred to any of the objects. The results of both experiments indicate that memory accuracy is not affected by the current focus of attention and that all the effects of directing attention to specific locations on response times can be explained in terms of stimulus–stimulus and stimulus–response spatial compatibility."

long_question = "What is the effect of directing attention on memory?"
yes_no_question = "Does directing attention improve memory for items?"

val data = Seq( 
    (long_question, paper_abstract,"long" ),
    (yes_no_question, paper_abstract, "short"))
    .toDS.toDF("question", "context", "question_type")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[the present study investigated whether directing spatial attention to one location in a visual array would enhance memory for the array features. participants memorized two]|
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|medical_qa_biogpt|
|Compatibility:|Healthcare NLP 4.3.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.1 GB|
|Case sensitive:|true|