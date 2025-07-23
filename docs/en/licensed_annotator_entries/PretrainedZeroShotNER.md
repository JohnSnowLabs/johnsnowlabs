{%- capture title -%}
PretrainedZeroShotNER
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
`Pretrained Zero-shot Named Entity Recognition (NER)` makes it easy to identify specific entities in text without needing 
pre-labeled datasets. It uses advanced pre-trained language models to recognize entities in different fields and languages,
saving time and effort.
This method is flexible, letting you define your own entity labels instead of relying on a fixed set of examples. 
For the best results, it’s helpful to choose labels similar to the provided examples, as they guide the model’s understanding.

Parameters:

- `labels`:  A list of labels descriving the entities. For example: ["person", "location"]
- `predictionThreshold`:   Minimal confidence score to encode an entity (Default: 0.01f)
- `setBatchSize`: Sets the number of inputs processed together in a single batch during inference. A higher batch size can improve throughput and reduce overall inference time on supported hardware, but may increase memory usage. (Default: `8`).
  
{%- endcapture -%}

{%- capture model_input_anno -%}


{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, TOKEN
{%- endcapture -%}

{%- capture model_output_anno -%}
NAMED_ENTITY
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

labels = ['DOCTOR', 'PATIENT', 'AGE', 'DATE', 'HOSPITAL', 'CITY', 'STREET', 'STATE', 'COUNTRY', 'PHONE', 'IDNUM', 'EMAIL','ZIP', 'ORGANIZATION', 'PROFESSION', 'USERNAME']

pretrained_zero_shot_ner = medical.PretrainedZeroShotNER().pretrained("zeroshot_ner_deid_subentity_merged_medium", "en", "clinical/models")\
    .setInputCols("sentence", "token")\
    .setOutputCol("ner")\
    .setPredictionThreshold(0.5)\
    .setLabels(labels)

ner_converter = medical.NerConverterInternal()\
    .setInputCols("sentence", "token", "ner")\
    .setOutputCol("ner_chunk")


pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    pretrained_zero_shot_ner,
    ner_converter
    ])

text = """Dr. John Lee, from Royal Medical Clinic in Chicago,  attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890. The patient, Emma Wilson, is 50 years old,  her Contact number: 444-456-7890 .
Dr. John Taylor, ID: 982345, a cardiologist at St. Mary's Hospital in Boston, was contacted on 05/10/2023 regarding a 45-year-old.
"""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)


# result

+--------------------+-----+---+----------+
|chunk               |begin|end|ner_label |
+--------------------+-----+---+----------+
|John Lee            |4    |11 |DOCTOR    |
|Royal Medical Clinic|19   |38 |HOSPITAL  |
|Chicago             |43   |49 |CITY      |
|11/05/2024          |80   |89 |DATE      |
|56467890            |131  |138|IDNUM     |
|Emma Wilson         |154  |164|PATIENT   |
|50                  |170  |171|AGE       |
|444-456-7890        |205  |216|PHONE     |
|John Taylor         |224  |234|DOCTOR    |
|982345              |241  |246|IDNUM     |
|cardiologist        |251  |262|PROFESSION|
|St. Mary's Hospital |267  |285|HOSPITAL  |
|Boston              |290  |295|CITY      |
|05/10/2023          |315  |324|DATE      |
|45-year-old         |338  |348|AGE       |
+--------------------+-----+---+----------+
{%- endcapture -%}


{%- capture model_scala_medical -%}

import spark.implicits._

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

val labels = Array(
    "DOCTOR", "PATIENT", "AGE", "DATE", "HOSPITAL", "CITY", "STREET",
    "STATE", "COUNTRY", "PHONE", "IDNUM", "EMAIL", "ZIP",
    "ORGANIZATION", "PROFESSION", "USERNAME"
    )

val pretrainedZeroShotNer = PretrainedZeroShotNER
    .pretrained("zeroshot_ner_deid_subentity_merged_medium", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("ner")
    .setPredictionThreshold(0.5.toFloat)
    .setLabels(labels)

val nerConverter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline()
    .setStages(Array(
        documentAssembler,
        sentenceDetector,
        tokenizer,
        pretrainedZeroShotNer,
        nerConverter
    ))

val text = """Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890. The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890.
Dr. John Taylor, ID: 982345, a cardiologist at St. Mary's Hospital in Boston, was contacted on 05/10/2023 regarding a 45-year-old.
"""


val data = spark.createDataFrame(Seq((text))).toDF("text")
val pipelineModel = pipeline.fit(data)
val result = pipelineModel.transform(data)



# result

+--------------------+-----+---+----------+
|chunk               |begin|end|ner_label |
+--------------------+-----+---+----------+
|John Lee            |4    |11 |DOCTOR    |
|Royal Medical Clinic|19   |38 |HOSPITAL  |
|Chicago             |43   |49 |CITY      |
|11/05/2024          |80   |89 |DATE      |
|56467890            |131  |138|IDNUM     |
|Emma Wilson         |154  |164|PATIENT   |
|50                  |170  |171|AGE       |
|444-456-7890        |205  |216|PHONE     |
|John Taylor         |224  |234|DOCTOR    |
|982345              |241  |246|IDNUM     |
|cardiologist        |251  |262|PROFESSION|
|St. Mary's Hospital |267  |285|HOSPITAL  |
|Boston              |290  |295|CITY      |
|05/10/2023          |315  |324|DATE      |
|45-year-old         |338  |348|AGE       |
+--------------------+-----+---+----------+

{%- endcapture -%}

{%- capture model_api_link -%}
[PretrainedZeroShotNER](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/ner/PretrainedZeroShotNER.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}

[PretrainedZeroShotNER](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/ner/pretrained_zero_shot_ner/index.html)

{%- endcapture -%}

{%- capture model_notebook_link -%}
[PretrainedZeroShotNER](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/PretrainedZeroShotNER.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical
model_api_link=model_api_link
model_python_api_link=model_python_api_link
model_notebook_link=model_notebook_link
%}
