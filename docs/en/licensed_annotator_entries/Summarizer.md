{%- capture title -%}
Summarizer
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
Summarizer annotator that uses a generative deep learning model to create summaries of medical texts given clinical contexts. This annotator helps to quickly summarize complex medical information.

Available models can be found at the [Models Hub](https://nlp.johnsnowlabs.com/models?annotator=MedicalSummarizer).

For more extended examples on document pre-processing see the [Spark NLP Workshop](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/32.Medical_Text_Summarization.ipynb)
{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import * 

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("documents")

med_summarizer  = medical.Summarizer\
    .pretrained("summarizer_generic_jsl", "en", "clinical/models")\
    .setInputCols("documents")\
    .setOutputCol("summary")\
    .setMaxTextLength(512)\
    .setMaxNewTokens(512)\
    .setDoSample(True)\
    .setRefineSummary(True)\
    .setRefineSummaryTargetLength(100)\
    .setRefineMaxAttempts(3)\
    .setRefineChunkSize(512)\


pipeline = nlp.Pipeline(stages=[document_assembler, med_summarizer])


text = """Patient with hypertension, syncope, and spinal stenosis - for recheck.
(Medical Transcription Sample Report)
SUBJECTIVE:
The patient is a 78-year-old female who returns for recheck. She has hypertension. She denies difficulty with chest pain, palpations, orthopnea, nocturnal dyspnea, or edema.
PAST MEDICAL HISTORY / SURGERY / HOSPITALIZATIONS:
Reviewed and unchanged from the dictation on 12/03/2003.
MEDICATIONS:
Atenolol 50 mg daily, Premarin 0.625 mg daily, calcium with vitamin D two to three pills daily, multivitamin daily, aspirin as needed, and TriViFlor 25 mg two pills daily. She also has Elocon cream 0.1% and Synalar cream 0.01% that she uses as needed for rash.
ALLERGIES:..."""


data = spark.createDataFrame([[text]]).toDF("text")


pipeline.fit(data).transform(data)
{%- endcapture -%}


{%- capture model_scala_medical -%}
from johnsnowlabs import * 

val document_assembler = new nlp.DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("documents")


val med_summarizer  = medical.Summarizer.pretrained("summarizer_generic_jsl", "en", "clinical/models")
    .setInputCols("documents")
    .setOutputCol("summary")
    .setMaxTextLength(512)
    .setMaxNewTokens(512)
    .setDoSample(true)
    .setRefineSummary(true)
    .setRefineSummaryTargetLength(100)
    .setRefineMaxAttempts(3)
    .setRefineChunkSize(512)


val pipeline = new nlp.Pipeline().setStages(Array(document_assembler, med_summarizer))


val text = """Patient with hypertension, syncope, and spinal stenosis - for recheck.
(Medical Transcription Sample Report)
SUBJECTIVE:
The patient is a 78-year-old female who returns for recheck. She has hypertension. She denies difficulty with chest pain, palpations, orthopnea, nocturnal dyspnea, or edema.
PAST MEDICAL HISTORY / SURGERY / HOSPITALIZATIONS:
Reviewed and unchanged from the dictation on 12/03/2003.
MEDICATIONS:
Atenolol 50 mg daily, Premarin 0.625 mg daily, calcium with vitamin D two to three pills daily, multivitamin daily, aspirin as needed, and TriViFlor 25 mg two pills daily. She also has Elocon cream 0.1% and Synalar cream 0.01% that she uses as needed for rash.
ALLERGIES:..."""


val data = Seq(text).toDS.toDF("text")
val result = pipeline.fit(data).transform(data)
{%- endcapture -%}


{%- capture model_python_legal -%}
from johnsnowlabs import * 

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("documents")


med_summarizer  = legal.Summarizer\
    .pretrained("summarizer_generic_jsl", "en", "clinical/models")\
    .setInputCols("documents")\
    .setOutputCol("summary")\
    .setMaxTextLength(512)\
    .setMaxNewTokens(512)\
    .setDoSample(True)\
    .setRefineSummary(True)\
    .setRefineSummaryTargetLength(100)\
    .setRefineMaxAttempts(3)\
    .setRefineChunkSize(512)\


pipeline = nlp.Pipeline(stages=[document_assembler, med_summarizer])


text = """Patient with hypertension, syncope, and spinal stenosis - for recheck.
(Medical Transcription Sample Report)
SUBJECTIVE:
The patient is a 78-year-old female who returns for recheck. She has hypertension. She denies difficulty with chest pain, palpations, orthopnea, nocturnal dyspnea, or edema.
PAST MEDICAL HISTORY / SURGERY / HOSPITALIZATIONS:
Reviewed and unchanged from the dictation on 12/03/2003.
MEDICATIONS:
Atenolol 50 mg daily, Premarin 0.625 mg daily, calcium with vitamin D two to three pills daily, multivitamin daily, aspirin as needed, and TriViFlor 25 mg two pills daily. She also has Elocon cream 0.1% and Synalar cream 0.01% that she uses as needed for rash.
ALLERGIES:..."""


data = spark.createDataFrame([[text]]).toDF("text")


pipeline.fit(data).transform(data)
{%- endcapture -%}



{%- capture model_scala_legal -%}
from johnsnowlabs import * 

val document_assembler = new nlp.DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("documents")


val med_summarizer  = legal.Summarizer.pretrained("summarizer_generic_jsl", "en", "clinical/models")
    .setInputCols("documents")
    .setOutputCol("summary")
    .setMaxTextLength(512)
    .setMaxNewTokens(512)
    .setDoSample(true)
    .setRefineSummary(true)
    .setRefineSummaryTargetLength(100)
    .setRefineMaxAttempts(3)
    .setRefineChunkSize(512)


val pipeline = new nlp.Pipeline().setStages(Array(document_assembler, med_summarizer))


val text = """Patient with hypertension, syncope, and spinal stenosis - for recheck.
(Medical Transcription Sample Report)
SUBJECTIVE:
The patient is a 78-year-old female who returns for recheck. She has hypertension. She denies difficulty with chest pain, palpations, orthopnea, nocturnal dyspnea, or edema.
PAST MEDICAL HISTORY / SURGERY / HOSPITALIZATIONS:
Reviewed and unchanged from the dictation on 12/03/2003.
MEDICATIONS:
Atenolol 50 mg daily, Premarin 0.625 mg daily, calcium with vitamin D two to three pills daily, multivitamin daily, aspirin as needed, and TriViFlor 25 mg two pills daily. She also has Elocon cream 0.1% and Synalar cream 0.01% that she uses as needed for rash.
ALLERGIES:..."""


val data = Seq(text).toDS.toDF("text")
val result = pipeline.fit(data).transform(data)
{%- endcapture -%}




{%- capture model_python_finance -%}
from johnsnowlabs import * 

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("documents")


med_summarizer  = finance.Summarizer\
    .pretrained("summarizer_generic_jsl", "en", "clinical/models")\
    .setInputCols("documents")\
    .setOutputCol("summary")\
    .setMaxNewTokens(100)\
    .setMaxTextLength(1024)\
    .setDoSample(True)\
    .setRefineSummary(True)\
    .setRefineSummaryTargetLength(100)\
    .setRefineMaxAttempts(3)\
    .setRefineChunkSize(512)\


pipeline = nlp.Pipeline(stages=[document_assembler, med_summarizer])


text = """Patient with hypertension, syncope, and spinal stenosis - for recheck.
(Medical Transcription Sample Report)
SUBJECTIVE:
The patient is a 78-year-old female who returns for recheck. She has hypertension. She denies difficulty with chest pain, palpations, orthopnea, nocturnal dyspnea, or edema.
PAST MEDICAL HISTORY / SURGERY / HOSPITALIZATIONS:
Reviewed and unchanged from the dictation on 12/03/2003.
MEDICATIONS:
Atenolol 50 mg daily, Premarin 0.625 mg daily, calcium with vitamin D two to three pills daily, multivitamin daily, aspirin as needed, and TriViFlor 25 mg two pills daily. She also has Elocon cream 0.1% and Synalar cream 0.01% that she uses as needed for rash.
ALLERGIES:..."""


data = spark.createDataFrame([[text]]).toDF("text")


pipeline.fit(data).transform(data)
{%- endcapture -%}


{%- capture model_scala_finance -%}
from johnsnowlabs import * 

val document_assembler = new nlp.DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("documents")


val med_summarizer  = finance.Summarizer.pretrained("summarizer_generic_jsl", "en", "clinical/models")
    .setInputCols("documents")
    .setOutputCol("summary")
    .setMaxTextLength(512)
    .setMaxNewTokens(512)
    .setDoSample(True)
    .setRefineSummary(True)
    .setRefineSummaryTargetLength(100)
    .setRefineMaxAttempts(3)
    .setRefineChunkSize(512)


val pipeline = new nlp.Pipeline().setStages(Array(document_assembler, med_summarizer))


val text = """Patient with hypertension, syncope, and spinal stenosis - for recheck.
(Medical Transcription Sample Report)
SUBJECTIVE:
The patient is a 78-year-old female who returns for recheck. She has hypertension. She denies difficulty with chest pain, palpations, orthopnea, nocturnal dyspnea, or edema.
PAST MEDICAL HISTORY / SURGERY / HOSPITALIZATIONS:
Reviewed and unchanged from the dictation on 12/03/2003.
MEDICATIONS:
Atenolol 50 mg daily, Premarin 0.625 mg daily, calcium with vitamin D two to three pills daily, multivitamin daily, aspirin as needed, and TriViFlor 25 mg two pills daily. She also has Elocon cream 0.1% and Synalar cream 0.01% that she uses as needed for rash.
ALLERGIES:..."""


val data = Seq(text).toDS.toDF("text")
val result = pipeline.fit(data).transform(data)
{%- endcapture -%}

{%- capture model_api_link -%}
[MedicalSummarizer](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/seq2seq/MedicalSummarizer.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[MedicalSummarizer](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/seq2seq/medical_summarizer/index.html#sparknlp_jsl.annotator.seq2seq.medical_summarizer.MedicalSummarizer)
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
