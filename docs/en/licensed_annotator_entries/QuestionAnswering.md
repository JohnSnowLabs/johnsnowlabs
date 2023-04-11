{%- capture title -%}
QuestionAnswering
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
QuestionAnswering is a GPT-based model for answering questions given a context. Unlike span-based models, it generates the answers to the questions, rather than selecting phrases from the given context. The model is capable of answering various types of questions, including yes-no or full-text ones. Types of questions are supported: `"short"` (producing yes/no/maybe) answers and `"long"` (full answers).

Available models can be found at the [Models Hub](https://nlp.johnsnowlabs.com/models?annotator=MedicalQuestionAnswering).

For more extended examples on the document, pre-processing see the [Spark NLP Workshop](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/23.0.Medical_Question_Answering.ipynb).
{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, DOCUMENT
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import * 

document_assembler = nlp.MultiDocumentAssembler()\
    .setInputCols("question", "context")\
    .setOutputCols("document_question", "document_context")

med_qa = medical.QuestionAnswering\
    .pretrained("medical_qa_biogpt", "en", "clinical/models")\
    .setInputCols(["document_question", "document_context"])\
    .setOutputCol("answer")\
    .setMaxNewTokens(30)\
    .setTopK(1)\
    .setQuestionType("long") # "short"


pipeline = nlp.Pipeline(stages=[document_assembler, med_qa])

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
{%- endcapture -%}


{%- capture model_scala_medical -%}
from johnsnowlabs import * 

val document_assembler = new nlp.MultiDocumentAssembler()
    .setInputCols("question", "context")
    .setOutputCols("document_question", "document_context")


val med_qa = medical.QuestionAnswering
    .pretrained("medical_qa_biogpt","en","clinical/models")
    .setInputCols(Array("document_question", "document_context"))
    .setOutputCol("answer")
    .setMaxNewTokens(30)
    .setTopK(1)
    .setQuestionType("long") # "short"


val pipeline = new nlp.Pipeline().setStages(Array(document_assembler, med_qa))

paper_abstract = "The visual indexing theory proposed by Zenon Pylyshyn (Cognition, 32, 65–97, 1989) predicts that visual attention mechanisms are employed when mental images are projected onto a visual scene. Recent eye-tracking studies have supported this hypothesis by showing that people tend to look at empty places where requested information has been previously presented. However, it has remained unclear to what extent this behavior is related to memory performance. The aim of the present study was to explore whether the manipulation of spatial attention can facilitate memory retrieval. In two experiments, participants were asked first to memorize a set of four objects and then to determine whether a probe word referred to any of the objects. The results of both experiments indicate that memory accuracy is not affected by the current focus of attention and that all the effects of directing attention to specific locations on response times can be explained in terms of stimulus–stimulus and stimulus–response spatial compatibility."
long_question = "What is the effect of directing attention on memory?"
yes_no_question = "Does directing attention improve memory for items?"


val data = Seq(
    (long_question, paper_abstract, "long" ),
    (yes_no_question, paper_abstract, "short"))
    .toDS.toDF("question", "context", "question_type")


val result = pipeline.fit(data).transform(data)
{%- endcapture -%}


{%- capture model_python_legal -%}
from johnsnowlabs import * 

document_assembler = nlp.MultiDocumentAssembler()\
    .setInputCols("question", "context")\
    .setOutputCols("document_question", "document_context")

med_qa = legal.QuestionAnswering\
    .pretrained("medical_qa_biogpt", "en", "clinical/models")\
    .setInputCols(["document_question", "document_context"])\
    .setOutputCol("answer")\
    .setMaxNewTokens(30)\
    .setTopK(1)\
    .setQuestionType("long") # "short"


pipeline = nlp.Pipeline(stages=[document_assembler, med_qa])

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
{%- endcapture -%}



{%- capture model_scala_legal -%}
from johnsnowlabs import * 

val document_assembler = new nlp.MultiDocumentAssembler()
    .setInputCols("question", "context")
    .setOutputCols("document_question", "document_context")


val med_qa = legal.QuestionAnswering
    .pretrained("medical_qa_biogpt","en","clinical/models")
    .setInputCols(Array("document_question", "document_context"))
    .setOutputCol("answer")
    .setMaxNewTokens(30)
    .setTopK(1)
    .setQuestionType("long") # "short"


val pipeline = new nlp.Pipeline().setStages(Array(document_assembler, med_qa))

paper_abstract = "The visual indexing theory proposed by Zenon Pylyshyn (Cognition, 32, 65–97, 1989) predicts that visual attention mechanisms are employed when mental images are projected onto a visual scene. Recent eye-tracking studies have supported this hypothesis by showing that people tend to look at empty places where requested information has been previously presented. However, it has remained unclear to what extent this behavior is related to memory performance. The aim of the present study was to explore whether the manipulation of spatial attention can facilitate memory retrieval. In two experiments, participants were asked first to memorize a set of four objects and then to determine whether a probe word referred to any of the objects. The results of both experiments indicate that memory accuracy is not affected by the current focus of attention and that all the effects of directing attention to specific locations on response times can be explained in terms of stimulus–stimulus and stimulus–response spatial compatibility."
long_question = "What is the effect of directing attention on memory?"
yes_no_question = "Does directing attention improve memory for items?"


val data = Seq(
    (long_question, paper_abstract, "long" ),
    (yes_no_question, paper_abstract, "short"))
    .toDS.toDF("question", "context", "question_type")


val result = pipeline.fit(data).transform(data)
{%- endcapture -%}




{%- capture model_python_finance -%}
from johnsnowlabs import * 

document_assembler = nlp.MultiDocumentAssembler()\
    .setInputCols("question", "context")\
    .setOutputCols("document_question", "document_context")

med_qa = finance.QuestionAnswering\
    .pretrained("medical_qa_biogpt", "en", "clinical/models")\
    .setInputCols(["document_question", "document_context"])\
    .setOutputCol("answer")\
    .setMaxNewTokens(30)\
    .setTopK(1)\
    .setQuestionType("long") # "short"


pipeline = nlp.Pipeline(stages=[document_assembler, med_qa])

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
{%- endcapture -%}


{%- capture model_scala_finance -%}
from johnsnowlabs import * 

val document_assembler = new nlp.MultiDocumentAssembler()
    .setInputCols("question", "context")
    .setOutputCols("document_question", "document_context")


val med_qa = finance.QuestionAnswering
    .pretrained("medical_qa_biogpt","en","clinical/models")
    .setInputCols(Array("document_question", "document_context"))
    .setOutputCol("answer")
    .setMaxNewTokens(30)
    .setTopK(1)
    .setQuestionType("long") # "short"


val pipeline = new nlp.Pipeline().setStages(Array(document_assembler, med_qa))

paper_abstract = "The visual indexing theory proposed by Zenon Pylyshyn (Cognition, 32, 65–97, 1989) predicts that visual attention mechanisms are employed when mental images are projected onto a visual scene. Recent eye-tracking studies have supported this hypothesis by showing that people tend to look at empty places where requested information has been previously presented. However, it has remained unclear to what extent this behavior is related to memory performance. The aim of the present study was to explore whether the manipulation of spatial attention can facilitate memory retrieval. In two experiments, participants were asked first to memorize a set of four objects and then to determine whether a probe word referred to any of the objects. The results of both experiments indicate that memory accuracy is not affected by the current focus of attention and that all the effects of directing attention to specific locations on response times can be explained in terms of stimulus–stimulus and stimulus–response spatial compatibility."
long_question = "What is the effect of directing attention on memory?"
yes_no_question = "Does directing attention improve memory for items?"


val data = Seq(
    (long_question, paper_abstract, "long" ),
    (yes_no_question, paper_abstract, "short"))
    .toDS.toDF("question", "context", "question_type")


val result = pipeline.fit(data).transform(data)
{%- endcapture -%}

{%- capture model_api_link -%}
[MedicalQuestionAnswering](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/qa/MedicalQuestionAnswering.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[MedicalQuestionAnswering](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/qa/medical_qa/index.html#sparknlp_jsl.annotator.qa.medical_qa.MedicalQuestionAnswering)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical
model_python_legal=model_python_legal
model_scala_legal=model_scala_legal
model_python_finance=model_python_finance
model_scala_finance=model_scala_finance
model_api_link=model_api_link
model_python_api_link=model_python_api_link
%}
