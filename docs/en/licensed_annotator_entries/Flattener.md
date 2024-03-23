{%- capture title -%}
Flattener
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
The `Flattener` converts annotation results into a format that easier to use. This annotator produces a DataFrame with flattened and exploded columns containing annotation results, making it easier to interpret and analyze the information.
It is particularly useful for extracting and organizing the results obtained from Spark NLP Pipelines.

Parametres:

- `inputCols`: Input annotations.
- `cleanAnnotations`: Whether to remove annotation columns, by default `True`.
- `explodeSelectedFields`: Dict of input columns to their corresponding selected fields.
- `flattenExplodedColumns`: Whether to flatten exploded columns(default : `True`).
- `orderByColumn`: Specify the column by which the DataFrame should be ordered..
- `orderDescending`: specifying whether to order the DataFrame in descending order.(default : `True`).


See [Spark NLP Workshop](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/41.Flattener.ipynb) for more examples of usage.
{%- endcapture -%}

{%- capture model_input_anno -%}
ANY
{%- endcapture -%}

{%- capture model_output_anno -%}
NONE
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

documentAssembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector() \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

clinical_ner = medical.NerModel.pretrained("ner_jsl", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner") \
    .setLabelCasing("upper")

ner_converter = medical.NerConverter() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk") \
    .setWhiteList(["SYMPTOM","VS_FINDING","DISEASE_SYNDROME_DISORDER","ADMISSION_DISCHARGE","PROCEDURE"])

flattener = medical.Flattener()\
    .setInputCols("ner_chunk") \
    .setExplodeSelectedFields({"ner_chunk": ["result as ner_chunks",
                                             "begin as begins",
                                             "end as ends",
                                             "metadata.entity as entities"]})

nlpPipeline = nlp.Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    word_embeddings,
    clinical_ner,
    ner_converter,
    flattener
])

text = """
GENERAL: He is an elderly gentleman in no acute distress. He is sitting up in bed eating his breakfast. He is alert and oriented and answering questions appropriately.
HEENT: Sclerae showed mild arcus senilis in the right. Left was clear. Pupils are equally round and reactive to light. Extraocular movements are intact. Oropharynx is clear.
NECK: Supple. Trachea is midline. No jugular venous pressure distention is noted. No adenopathy in the cervical, supraclavicular, or axillary areas.
ABDOMEN: Soft and not tender. There may be some fullness in the left upper quadrant, although I do not appreciate a true spleen with inspiration.
EXTREMITIES: There is some edema, but no cyanosis and clubbing .
"""

data = spark.createDataFrame([[text]]).toDF("text")

result = nlpPipeline.fit(data).transform(data)
result.show(truncate=False)

# result
+----------------------------------+------+----+-------------------------+
|ner_chunks                        |begins|ends|entities                 |
+----------------------------------+------+----+-------------------------+
|distress                          |49    |56  |SYMPTOM                  |
|arcus senilis                     |196   |208 |DISEASE_SYNDROME_DISORDER|
|jugular venous pressure distention|380   |413 |SYMPTOM                  |
|adenopathy                        |428   |437 |SYMPTOM                  |
|tender                            |514   |519 |SYMPTOM                  |
|fullness                          |540   |547 |SYMPTOM                  |
|edema                             |665   |669 |SYMPTOM                  |
|cyanosis                          |679   |686 |VS_FINDING               |
|clubbing                          |692   |699 |SYMPTOM                  |
+----------------------------------+------+----+-------------------------+
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

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

val clinicalNer = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner")
  .setLabelCasing("upper")

val nerConverter = new NerConverterInternal()
  .setInputCols(Array("sentence", "token", "ner"))
  .setOutputCol("ner_chunk")
  .setWhiteList(Array("SYMPTOM", "VS_FINDING", "DISEASE_SYNDROME_DISORDER", "ADMISSION_DISCHARGE", "PROCEDURE"))

val flattener = new Flattener()
  .setInputCols(Array("ner_chunk"))
  .setExplodeSelectedFields(Map("ner_chunk" -> Array("result", "begin", "end", "metadata.entity")))

val nlpPipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  wordEmbeddings,
  clinicalNer,
  nerConverter,
  flattener
))

val text = """
GENERAL: He is an elderly gentleman in no acute distress. He is sitting up in bed eating his breakfast. He is alert and oriented and answering questions appropriately.
HEENT: Sclerae showed mild arcus senilis in the right. Left was clear. Pupils are equally round and reactive to light. Extraocular movements are intact. Oropharynx is clear.
NECK: Supple. Trachea is midline. No jugular venous pressure distention is noted. No adenopathy in the cervical, supraclavicular, or axillary areas.
ABDOMEN: Soft and not tender. There may be some fullness in the left upper quadrant, although I do not appreciate a true spleen with inspiration.
EXTREMITIES: There is some edema, but no cyanosis and clubbing .
"""

val data = Seq(text).toDF("text")

val result = nlpPipeline.fit(data).transform(data)

# result
+----------------------------------+------+----+-------------------------+
|ner_chunks                        |begins|ends|entities                 |
+----------------------------------+------+----+-------------------------+
|distress                          |49    |56  |SYMPTOM                  |
|arcus senilis                     |196   |208 |DISEASE_SYNDROME_DISORDER|
|jugular venous pressure distention|380   |413 |SYMPTOM                  |
|adenopathy                        |428   |437 |SYMPTOM                  |
|tender                            |514   |519 |SYMPTOM                  |
|fullness                          |540   |547 |SYMPTOM                  |
|edema                             |665   |669 |SYMPTOM                  |
|cyanosis                          |679   |686 |VS_FINDING               |
|clubbing                          |692   |699 |SYMPTOM                  |
+----------------------------------+------+----+-------------------------+

{%- endcapture -%}


{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical%}
