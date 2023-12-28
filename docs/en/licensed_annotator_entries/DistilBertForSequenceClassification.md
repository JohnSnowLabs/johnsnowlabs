{%- capture title -%}
DistilBertForSequenceClassification
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}

 `DistilBertForSequenceClassification`  can load DistilBERT Models with sequence classification/regression head on top (a linear layer on top of the pooled output) e.g. for multi-class document classification tasks.

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

sequenceClassifier = medical.DistilBertForSequenceClassification.pretrained("distilbert_sequence_classifier_ade", "en", "clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("classes")

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    sequenceClassifier
])

data = spark.createDataFrame([["I have an allergic reaction to vancomycin so I have itchy skin, sore throat/burning/itching, numbness of tongue and gums.I would not recommend this drug to anyone, especially since I have never had such an adverse reaction to any other medication."],
                              ["Religare Capital Ranbaxy has been accepting approval for Diovan since 2012"]]).toDF("text")

result = pipeline.fit(data).transform(data)

result.select("text", "classes.result").show(truncate=100)

| text                                                                                           | result |
|------------------------------------------------------------------------------------------------|-------|
| I have an allergic reaction to vancomycin so I have itchy skin, sore throat/burning/itching, numb... | [True] |
| Religare Capital Ranbaxy has been accepting approval for Diovan since 2012 | [False] |

{%- endcapture -%}


{%- capture model_scala_medical -%}
import spark.implicits._

val document_assembler = new DocumentAssembler() 
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val sequenceClassifier = MedicalDistilBertForSequenceClassification.pretrained("distilbert_sequence_classifier_ade", "en", "clinical/models")
    .setInputCols(Array("document","token"))
    .setOutputCol("classes")

val pipeline =  new Pipeline().setStages(Array(
    document_assembler, 
    tokenizer, 
    sequenceClassifier))

var text =List(
    List("I have an allergic reaction to vancomycin so I have itchy skin, sore throat/burning/itching, numbness of tongue and gums.I would not recommend this drug to anyone, especially since I have never had such an adverse reaction to any other medication."),
    List("Religare Capital Ranbaxy has been accepting approval for Diovan since 2012")
)

val data = Seq(text).toDF("text")
val result = pipeline.fit(data).transform(data)

| text                                                                                           | result |
|------------------------------------------------------------------------------------------------|-------|
| I have an allergic reaction to vancomycin so I have itchy skin, sore throat/burning/itching, numb... | [True] |
| Religare Capital Ranbaxy has been accepting approval for Diovan since 2012 | [False] |

{%- endcapture -%}


{%- capture model_python_api_link -%}
[DistilBertForSequenceClassification](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/classification/medical_distilbert_for_sequence_classification/index.html)
{%- endcapture -%}

{%- capture model_scala_api_link -%}
[DistilBertForSequenceClassification](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/classification/MedicalDistilBertForSequenceClassification.html)
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