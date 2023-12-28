{%- capture title -%}
BertSentenceChunkEmbeddings
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
This annotator allows aggregating sentence embeddings with ner chunk embeddings to get specific and more accurate resolution codes. It works by averaging sentence and chunk embeddings add contextual information in the embedding value. Input to this annotator is the context (sentence) and ner chunks, while the output is embedding for each chunk that can be fed to the resolver model. 

Parameters:

- `inputCols`: The name of the columns containing the input annotations. It can read either a String column or an Array.

- `outputCol`: The name of the column in Document type that is generated. We can specify only one column here.

- `chunkWeight`: Relative weight of chunk embeddings in comparison to sentence embeddings. The value should between 0 and 1. The default is 0.5, which means the chunk and sentence embeddings are given equal weight.

- `setMaxSentenceLength`: Sets max sentence length to process, by default 128.

- `caseSensitive`: Determines whether the definitions of the white listed entities are case sensitive.

All the parameters can be set using the corresponding set method in camel case. For example, `.setInputcols()`.

> For more information and examples of `BertSentenceChunkEmbeddings` annotator, you can check the [Spark NLP Workshop](https://github.com/JohnSnowLabs/spark-nlp-workshop), and in special, the notebook [24.1.Improved_Entity_Resolution_with_SentenceChunkEmbeddings.ipynb](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/24.1.Improved_Entity_Resolution_with_SentenceChunkEmbeddings.ipynb).

{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
SENTENCE_EMBEDDINGS
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical
# Define the pipeline

document_assembler = nlp.DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

tokenizer = nlp.Tokenizer()\
      .setInputCols(["document"])\
      .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
      .setInputCols(["document", "token"])\
      .setOutputCol("word_embeddings")

clinical_ner = medical.NerModel.pretrained("ner_abbreviation_clinical", "en", "clinical/models") \
      .setInputCols(["document", "token", "word_embeddings"]) \
      .setOutputCol("ner")

ner_converter = medical.NerConverterInternal() \
      .setInputCols(["document", "token", "ner"]) \
      .setOutputCol("ner_chunk")\
      .setWhiteList(['ABBR'])

sentence_chunk_embeddings = medical.BertSentenceChunkEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
      .setInputCols(["document", "ner_chunk"])\
      .setOutputCol("sentence_embeddings")\
      .setChunkWeight(0.5)\
      .setCaseSensitive(True)
    
resolver_pipeline = nlp.Pipeline(
    stages = [
      document_assembler,
      tokenizer,
      word_embeddings,
      clinical_ner,
      ner_converter,
      sentence_chunk_embeddings
])


sample_text = [
"""The patient admitted from the IR for aggressive irrigation of the Miami pouch. DISCHARGE DIAGNOSES: 1. A 58-year-old female with a history of stage 2 squamous cell carcinoma of the cervix status post total pelvic exenteration in 1991.""",
"""Gravid with estimated fetal weight of 6-6/12 pounds. LOWER EXTREMITIES: No edema. LABORATORY DATA: Laboratory tests include a CBC which is normal. 
Blood Type: AB positive. Rubella: Immune. VDRL: Nonreactive. Hepatitis C surface antigen: Negative. HIV: Negative. One-Hour Glucose: 117. Group B strep has not been done as yet."""]

from pyspark.sql.types import StringType, IntegerType

df = spark.createDataFrame(sample_text, StringType()).toDF('text')
result = resolver_pipeline.fit(df).transform(df)

result.selectExpr("explode(sentence_embeddings) AS s")\
      .selectExpr("s.result", "slice(s.embeddings, 1, 5) AS averageEmbedding")\
      .show(truncate=False)

+------+--------------------------------------------------------------+
|result|averageEmbedding                                              |
+------+--------------------------------------------------------------+
|IR    |[0.11792798, 0.36022937, -1.0620842, 0.87576616, 0.5389829]   |
|CBC   |[-0.07262431, -0.671684, 0.009878114, 0.76053196, 0.4687413]  |
|AB    |[-0.2781681, -0.43619046, -0.20924012, 0.84943366, 0.40831584]|
|VDRL  |[-0.07109344, -0.20644212, 0.0367461, 0.43459156, 0.3684616]  |
|HIV   |[-0.1740405, -0.4599509, -0.041505605, 0.61368394, 0.66777927]|
+------+--------------------------------------------------------------+

{%- endcapture -%}


{%- capture model_scala_medical -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")

val tokenizer = new Tokenizer()
      .setInputCols("document")
      .setOutputCol("tokens")

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
      .setInputCols(Array("document", "tokens"))
      .setOutputCol("word_embeddings")

val nerModel = MedicalNerModel.pretrained("ner_abbreviation_clinical", "en", "clinical/models")
      .setInputCols(Array("document", "tokens", "word_embeddings"))
      .setOutputCol("ner")

val nerConverter = new NerConverterInternal()
      .setInputCols("document", "tokens", "ner")
      .setOutputCol("ner_chunk")
      .setWhiteList(Array('ABBR'))

val sentenceChunkEmbeddings = BertSentenceChunkEmbeddings.pretrained("sbluebert_base_uncased_mli", "en", "clinical/models")
      .setInputCols(Array("document", "ner_chunk"))
      .setOutputCol("sentence_embeddings")
      .setChunkWeight(0.5)
      .setCaseSensitive(True)

val pipeline = new Pipeline().setStages(Array(
      documentAssembler,
      sentenceDetector,
      tokenizer,
      wordEmbeddings,
      nerModel,
      nerConverter,
      sentenceChunkEmbeddings))

val sampleText = "The patient admitted from the IR for aggressive irrigation of the Miami pouch. DISCHARGE DIAGNOSES: 1. A 58-year-old female with a history of stage 2 squamous cell carcinoma of the cervix status post total pelvic exenteration in 1991." +
"Gravid with estimated fetal weight of 6-6/12 pounds. LOWER EXTREMITIES: No edema. LABORATORY DATA: Laboratory tests include a CBC which is normal. 
Blood Type: AB positive. Rubella: Immune. VDRL: Nonreactive. Hepatitis C surface antigen: Negative. HIV: Negative. One-Hour Glucose: 117. Group B strep has not been done as yet."

val data = Seq(sampleText).toDF("sampleText")
val result = pipeline.fit(data).transform(data)

+------+--------------------------------------------------------------+
|result|averageEmbedding                                              |
+------+--------------------------------------------------------------+
|IR    |[0.11792798, 0.36022937, -1.0620842, 0.87576616, 0.5389829]   |
|CBC   |[-0.07262431, -0.671684, 0.009878114, 0.76053196, 0.4687413]  |
|AB    |[-0.2781681, -0.43619046, -0.20924012, 0.84943366, 0.40831584]|
|VDRL  |[-0.07109344, -0.20644212, 0.0367461, 0.43459156, 0.3684616]  |
|HIV   |[-0.1740405, -0.4599509, -0.041505605, 0.61368394, 0.66777927]|
+------+--------------------------------------------------------------+

{%- endcapture -%}


{%- capture model_api_link -%}
[BertSentenceChunkEmbeddings](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/embeddings/BertSentenceChunkEmbeddings.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[BertSentenceChunkEmbeddings](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/embeddings/bert_sentence_embeddings/index.html#sparknlp_jsl.annotator.embeddings.bert_sentence_embeddings.BertSentenceChunkEmbeddings)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[BertSentenceChunkEmbeddingsNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/BertSentenceChunkEmbeddings.ipynb)
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
