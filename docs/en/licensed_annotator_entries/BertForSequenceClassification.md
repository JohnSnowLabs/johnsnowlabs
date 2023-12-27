{%- capture title -%}
BertForSequenceClassification
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
 `BertForSequenceClassification`  can load Bert Models with sequence classification/regression head on top (a linear layer on top of the pooled output) e.g. for multi-class document classification tasks.

Parameters:

- `batchSize`',  'Size of every batch': default: 8,

- `coalesceSentences`': "Instead of 1 class per sentence (if inputCols is '''sentence''' output 1 class per document by averaging probabilities in all sentences." default: False,

- `maxSentenceLength`', 'Max sentence length to process', default: 128

- `caseSensitive`', 'whether to ignore case in tokens for embeddings matching',default: True,
{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, TOKEN
{%- endcapture -%}

{%- capture model_output_anno -%}
CATEGORY
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical
 
document_assembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

sequenceClassifier = medical.BertForSequenceClassification.pretrained("bert_sequence_classifier_ade", "en", "clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("classes")

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    sequenceClassifier
])


text =[["Right inguinal hernia repair in childhood Cervical discectomy 3 years ago Umbilical hernia repair 2137. Retired schoolteacher, now substitutes. Lives with wife in location 1439. Has a 27 yo son and a 25 yo daughter. Name (NI) past or present smoking hx, no EtOH."],
     ["Atrial Septal Defect with Right Atrial Thrombus Pulmonary Hypertension Obesity, Obstructive Sleep Apnea. Denies tobacco and ETOH. Works as cafeteria worker."]]

data = spark.createDataFrame(text).toDF("text")
result = pipeline.fit(data).transform(data)

result.select("text", "classes.result").show(2,truncate=100)

| text                                                                                           | result |
|------------------------------------------------------------------------------------------------|-------|
| Right inguinal hernia repair in childhood Cervical discectomy 3 years ago Umbilical hernia repair... | [False] |
| Atrial Septal Defect with Right Atrial Thrombus Pulmonary Hypertension Obesity, Obstructive Sleep... | [False] |

{%- endcapture -%}


{%- capture model_scala_medical -%}
import spark.implicits._

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_ade", "en", "clinical/models")
    .setInputCols(Array("document","token"))
    .setOutputCol("classes")

val pipeline =  new Pipeline().setStages(Array(
    document_assembler, 
    tokenizer, 
    sequenceClassifier))

val text = List(
  List("Right inguinal hernia repair in childhood Cervical discectomy 3 years ago Umbilical hernia repair 2137. Retired schoolteacher, now substitutes. Lives with wife in location 1439. Has a 27 yo son and a 25 yo daughter. Name (NI) past or present smoking hx, no EtOH."),
  List("Atrial Septal Defect with Right Atrial Thrombus Pulmonary Hypertension Obesity, Obstructive Sleep Apnea. Denies tobacco and ETOH. Works as cafeteria worker.")
)

val data = Seq(text).toDF("text")

val result = pipeline.fit(data).transform(data)

| text                                                                                           | result |
|------------------------------------------------------------------------------------------------|-------|
| Right inguinal hernia repair in childhood Cervical discectomy 3 years ago Umbilical hernia repair... | [False] |
| Atrial Septal Defect with Right Atrial Thrombus Pulmonary Hypertension Obesity, Obstructive Sleep... | [False] |


{%- endcapture -%}


{%- capture model_python_api_link -%}
[BertForSequenceClassification](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/classification/medical_bert_for_sequence_classification/index.html#)
{%- endcapture -%}

{%- capture model_scala_api_link -%}
[BertForSequenceClassification](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/classification/MedicalBertForSequenceClassification.html)
{%- endcapture -%}


{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical
model_python_api_link=model_python_api_link
model_scala_api_link=model_scala_api_link
%}
