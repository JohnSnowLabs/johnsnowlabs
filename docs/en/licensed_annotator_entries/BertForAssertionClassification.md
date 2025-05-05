{%- capture title -%}
BertForAssertionClassification
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
BertForAssertionClassification extracts the assertion status from text by analyzing both the extracted entities
and their surrounding context.

This classifier leverages pre-trained BERT models fine-tuned on biomedical text (e.g., BioBERT) and applies a
sequence classification/regression head (a linear layer on the pooled output) to support multi-class document
classification.

**Key features:**

- Accepts DOCUMENT and CHUNK type inputs and produces ASSERTION type annotations.
- Emphasizes entity context by marking target entities with special tokens (e.g., [entity]), allowing the model to better focus on them.
- Utilizes a transformer-based architecture (BERT for Sequence Classification) to achieve accurate assertion status prediction.

**Input Example:**

This annotator preprocesses the input text to emphasize the target entities as follows:
[CLS] Patient with [entity] severe fever [entity].

Models from the HuggingFace 🤗 Transformers library are also compatible with
Spark NLP 🚀. To see which models are compatible and how to import them see
[Import Transformers into Spark NLP 🚀](https://github.com/JohnSnowLabs/spark-nlp/discussions/5669)


Parameters:

- `configProtoBytes`: ConfigProto from tensorflow, serialized into byte array.
- `classificationCaseSensitive`: Whether to use case sensitive classification. Default is True.

       

  {%- endcapture -%}


{%- capture model_input_anno -%}
DOCUMENT, CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
ASSERTION
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text") \
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetector()\
    .setInputCols("document")\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)

ner = medical.NerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["PROBLEM"])

assertion_classifier = medical.BertForAssertionClassification.pretrained("assertion_bert_classification_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "ner_chunk"])\
    .setOutputCol("assertion_class")

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    sentence_detector,
    tokenizer,
    embeddings,
    ner,
    ner_converter,
    assertion_classifier
])

text = """
GENERAL: He is an elderly gentleman in no acute distress. He is sitting up in bed eating his breakfast. He is alert and oriented and answering questions appropriately.
HEENT: Sclerae showed mild arcus senilis in the right. Left was clear. Pupils are equally round and reactive to light. Extraocular movements are intact. Oropharynx is clear.
NECK: Supple. Trachea is midline. No jugular venous pressure distention is noted. No adenopathy in the cervical, supraclavicular, or axillary areas.
ABDOMEN: Soft and not tender. There may be some fullness in the left upper quadrant, although I do not appreciate a true spleen with inspiration.
EXTREMITIES: There is some edema, but no cyanosis and clubbing .
"""

data = spark.createDataFrame([[text]]).toDF("text")
result = pipeline.fit(data).transform(data)


# result

+--------------------------------------------------------------+-----+----+---------+----------------------+
|ner_chunk                                                     |begin|end |ner_label|assertion_class_result|
+--------------------------------------------------------------+-----+----+---------+----------------------+
|acute distress                                                |43   |56  |PROBLEM  |absent                |
|mild arcus senilis in the right                               |191  |221 |PROBLEM  |present               |
|jugular venous pressure distention                            |380  |413 |PROBLEM  |absent                |
|adenopathy in the cervical, supraclavicular, or axillary areas|428  |489 |PROBLEM  |absent                |
|tender                                                        |514  |519 |PROBLEM  |absent                |
|some fullness in the left upper quadrant                      |535  |574 |PROBLEM  |possible              |
|some edema                                                    |660  |669 |PROBLEM  |present               |
|cyanosis                                                      |679  |686 |PROBLEM  |absent                |
|clubbing                                                      |692  |699 |PROBLEM  |absent                |
+--------------------------------------------------------------+-----+----+---------+----------------------+


{%- endcapture -%}


{%- capture model_scala_medical -%}

import spark.implicits._

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols("document", "token")
    .setOutputCol("embeddings")

val jslNer = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")
   .setInputCols("sentence", "token", "embeddings")
   .setOutputCol("jsl_ner")

val jslNerConverter = new NerConverterInternal()
    .setInputCols("sentence", "token", "jsl_ner")
    .setOutputCol("ner_chunks")

val clinicalAssertion = BertForAssertionClassification.pretrained("assertion_bert_classification_clinical", "en", "clinical/models")
    .setInputCols("sentence", "ner_chunk")
    .setOutputCol("assertion")
    .setCaseSensitive(false)

val pipeline = new Pipeline().setStages(
  Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    wordEmbeddings,
    jslNer,
    jslNerConverter,
    clinicalAssertion
  ))

val text = "GENERAL: He is an elderly gentleman in no acute distress. He is sitting up in bed eating his breakfast. He is alert and oriented and answering questions appropriately.
HEENT: Sclerae showed mild arcus senilis in the right. Left was clear. Pupils are equally round and reactive to light. Extraocular movements are intact. Oropharynx is clear.
NECK: Supple. Trachea is midline. No jugular venous pressure distention is noted. No adenopathy in the cervical, supraclavicular, or axillary areas.
ABDOMEN: Soft and not tender. There may be some fullness in the left upper quadrant, although I do not appreciate a true spleen with inspiration.
EXTREMITIES: There is some edema, but no cyanosis and clubbing ."

val df = Seq(text).toDF("text")
val result = pipeline.fit(df).transform(df)


# result
+--------------------------------------------------------------+-----+----+---------+----------------------+
|ner_chunk                                                     |begin|end |ner_label|assertion_class_result|
+--------------------------------------------------------------+-----+----+---------+----------------------+
|acute distress                                                |43   |56  |PROBLEM  |absent                |
|mild arcus senilis in the right                               |191  |221 |PROBLEM  |present               |
|jugular venous pressure distention                            |380  |413 |PROBLEM  |absent                |
|adenopathy in the cervical, supraclavicular, or axillary areas|428  |489 |PROBLEM  |absent                |
|tender                                                        |514  |519 |PROBLEM  |absent                |
|some fullness in the left upper quadrant                      |535  |574 |PROBLEM  |possible              |
|some edema                                                    |660  |669 |PROBLEM  |present               |
|cyanosis                                                      |679  |686 |PROBLEM  |absent                |
|clubbing                                                      |692  |699 |PROBLEM  |absent                |
+--------------------------------------------------------------+-----+----+---------+----------------------+

{%- endcapture -%}

{%- capture model_api_link -%}
[BertForAssertionClassification](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/assertion/BertForAssertionClassification.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}

[BertForAssertionClassification](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/assertion/bert_for_assertion_classification/index.html)

{%- endcapture -%}

{%- capture model_notebook_link -%}
[BertForAssertionClassification](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/2.4.BertForAssertionClassification.ipynb)
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
