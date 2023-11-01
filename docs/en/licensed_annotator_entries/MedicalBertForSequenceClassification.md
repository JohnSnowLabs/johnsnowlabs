{%- capture title -%}
MedicalBertForSequenceClassification
{%- endcapture -%}

{%- capture approach -%}
approach
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
 `MedicalBertForSequenceClassification`  can load Bert Models with sequence classification/regression head on top (a linear layer on top of the pooled output) e.g. for multi-class document classification tasks. Pretrained models can be loaded with :method :`.pretrained` of the companion object:

For available pretrained models please see the [`Models Hub`](https://nlp.johnsnowlabs.com/models?task=Named+Entity+Recognition)


Parameters:
- '`batchSize`', 'Size of every batch',`default`: 8,
- '`coalesceSentences`', "Instead of 1 class per sentence (if inputCols is '''sentence''') output 1 class per document by averaging probabilities in all sentences.",`default`: False,
- '`engine`', 'Deep Learning engine used for this model',`default`: 'tensorflow',
- '`lazyAnnotator`', 'Whether this AnnotatorModel acts as lazy in RecursivePipelines',`default`: False,
- '`maxSentenceLength`', 'Max sentence length to process',`default`: 128,
- '`caseSensitive`', 'whether to ignore case in tokens for embeddings matching',`default`: True,
- '`inputCols`', 'previous annotations columns, if renamed,`default`: ['document','token'],
- '`outputCol`', 'output annotation column. can be left default.',`default`: 'classes'

{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, TOKEN
{%- endcapture -%}

{%- capture model_output_anno -%}
CATEGORY
{%- endcapture -%}


{%- capture model_python_api_link -%}
[MedicalBertForSequenceClassification](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/classification/medical_bert_for_sequence_classification/index.html#)
{%- endcapture -%}

{%- capture model_scala_api_link -%}
[MedicalBertForSequenceClassification](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/classification/MedicalBertForSequenceClassification.html)
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


{%- capture model_python_finance -%}

{%- endcapture -%}

{%- capture model_python_legal -%}

{%- endcapture -%}

{%- capture model_scala_medical -%}

val document_assembler = new DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

val tokenizer = new Tokenizer() \
    .setInputCols(Array("document")) \
    .setOutputCol("token")

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_ade", "en", "clinical/models")\
    .setInputCols(Array("document","token"))\
    .setOutputCol("classes")

val pipeline =  new Pipeline(stages=Array(document_assembler, tokenizer, sequenceClassifier))

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

{%- capture model_scala_finance -%}
{%- endcapture -%}

{%- capture model_scala_legal -%}
{%- endcapture -%}


{%- capture approach_description -%}
`MedicalBertForSequenceClassification` can load Bert Models with a token classification head on top (a linear layer on top of the hidden-states output) e.g. for Named-Entity-Recognition (NER) tasks.
Pretrained models can be loaded with pretrained() of the companion object.
The default model is "bert_token_classifier_ner_bionlp", if no name is provided.
For available pretrained models please see the [Models Hub](https://nlp.johnsnowlabs.com/models).
### Parameters:
- `configProtoBytes`: ConfigProto from tensorflow, serialized into byte array.

- `maxSentenceLength`: Max sentence length to process, by default 128.

{%- endcapture -%}

{%- capture approach_input_anno -%}
DOCUMENT, TOKEN
{%- endcapture -%}

{%- capture approach_output_anno -%}
NAMED_ENTITY
{%- endcapture -%}

{%- capture approach_python_medical -%}

from johnsnowlabs import nlp, medical
documentAssembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

sequenceClassifier = medical.BertForSequenceClassification.pretrained() \
    .setInputCols(["token", "document"]) \
    .setOutputCol("classes") \
    .setCaseSensitive(True)

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

| text | result |
| ---- | ------ |
| Right inguinal hernia repair in childhood Cervical discectomy 3 years ago Umbilical hernia repair... | [False] |
| Atrial Septal Defect with Right Atrial Thrombus Pulmonary Hypertension Obesity, Obstructive Sleep... | [False] |


{%- endcapture -%}

{%- capture approach_python_legal -%}
{%- endcapture -%}

{%- capture approach_python_finance -%}

{%- endcapture -%}


{%- capture approach_scala_medical -%}

val documentAssembler = new DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

val tokenizer = new Tokenizer() \
    .setInputCols(Array("document")) \
    .setOutputCol("token")

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained() \
    .setInputCols(Array("token", "document")) \
    .setOutputCol("label") \
    .setCaseSensitive(true)

val pipeline = new Pipeline().setStages(Array(documentAssembler, tokenizer,sequenceClassifier))

val text = "Both the erbA IRES and the erbA/myb virus constructs transformed erythroid cells after infection of bone marrow or blastoderm cultures."

val data = Seq(text).toDF("text")
val result = pipeline.fit(data).transform(data)


| text                                                                                           | result |
|------------------------------------------------------------------------------------------------|-------|
| Right inguinal hernia repair in childhood Cervical discectomy 3 years ago Umbilical hernia repair... | [False] |
| Atrial Septal Defect with Right Atrial Thrombus Pulmonary Hypertension Obesity, Obstructive Sleep... | [False] |

{%- endcapture -%}

{%- capture approach_scala_legal -%}
  
{%- endcapture -%}

{%- capture approach_scala_finance -%}

{%- endcapture -%}

{%- capture approach_api_link -%}
{%- endcapture -%}

{%- capture approach_python_api_link -%}
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
approach=approach
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_api_link=model_python_api_link
model_scala_api_link=model_scala_api_link
model_python_medical=model_python_medical
model_python_finance=model_python_finance
model_python_legal=model_python_legal
model_scala_finance=model_scala_finance
model_scala_legal=model_scala_legal
approach_description=approach_description
approach_input_anno=approach_input_anno
approach_output_anno=approach_output_anno
approach_python_medical=approach_python_medical
approach_python_legal=approach_python_legal
approach_python_finance=approach_python_finance
approach_scala_medical=approach_scala_medical
approach_scala_legal=approach_scala_legal
approach_scala_finance=approach_scala_finance
approach_api_link=approach_api_link
approach_python_api_link=approach_python_api_link
%}
