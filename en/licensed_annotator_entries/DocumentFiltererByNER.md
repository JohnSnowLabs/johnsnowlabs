{%- capture model -%}
model
{%- endcapture -%}

{%- capture title -%}
DocumentFiltererByNER
{%- endcapture -%}

{%- capture model_description -%}
The `DocumentFiltererByNER` annotator returns sentences containing the entity chunks you have filtered, allowing you to see only the sentences with the entities you want.It is particularly useful for extracting and organizing the results obtained from Spark NLP Pipelines.

Parameters:

- `blackList`: If defined, list of entities to ignore. The rest will be processed.
- `whiteList`: If defined, list of entities to process. The rest will be ignored.
- `caseSensitive`: Determines whether the definitions of the white listed and black listed entities are case sensitive or not.
- `outputAsDocument`: Whether to return all sentences joined into a single document.(default : `False`).
- `joinString`: This parameter specifies the string that will be inserted between results of documents when combining them into a single result if outputAsDocument is set to `True` (default is : " ").

{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
DOCUMENT
{%- endcapture -%}



{%- capture model_python_medical -%}

documentAssembler = nlp.DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
  .setInputCols("document")\
  .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
  .setInputCols("sentence")\
  .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models") \
  .setInputCols(["sentence", "token"])\
  .setOutputCol("embeddings")

ner_jsl = medical.NerModel.pretrained("ner_jsl", "en", "clinical/models") \
  .setInputCols(["sentence", "token", "embeddings"])\
  .setOutputCol("ner")

ner_converter = medical.NerConverterInternal() \
  .setInputCols(["sentence", "token", "ner"]) \
  .setOutputCol("ner_chunk")

filterer = medical.DocumentFiltererByNER() \
  .setInputCols(["sentence", "ner_chunk"]) \
  .setOutputCol("filterer") \
  .setWhiteList(["Disease_Syndrome_Disorder"])

pipeline = nlp.Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    word_embeddings,
    ner_jsl,
    ner_converter,
    filterer])

df = spark.createDataFrame([
    ["Coronavirus disease (COVID-19) is an infectious disease caused by the SARS-CoV-2 virus."],
    ["Most people infected with the virus will experience mild to moderate respiratory illness and recover without requiring special treatment."],
    ["However, some will become seriously ill and require medical attention. "],
    ["Older people and those with underlying medical conditions like cardiovascular disease, diabetes, chronic respiratory disease, or cancer are more likely to develop serious illness."],
    ["Anyone can get sick with COVID-19 and become seriously ill or die at any age."],
    ["The best way to prevent and slow down transmission is to be well informed about the disease and how the virus spreads."],
    ["Protect yourself and others from infection by staying at least 1 metre apart from others, wearing a properly fitted mask, and washing your hands or using an alcohol-based rub frequently."],
    ["Get vaccinated when it’s your turn and follow local guidance."],
    ["Stay home if you feel unwell."],
    ["If you have a fever, cough and difficulty breathing, seek medical attention."],
    ["The virus can spread from an infected person’s mouth or nose in small liquid particles when they cough, sneeze, speak, sing or breathe. "],
    ["These particles range from larger respiratory droplets to smaller aerosols. It is important to practice respiratory etiquette, for example by coughing into a flexed elbow, and to stay home and self-isolate until you recover if you feel unwell."]
    ]).toDF("text")

from pyspark.sql.window import Window as W
from pyspark.sql import functions as F
spark_df = df.coalesce(1).withColumn("idx", F.monotonically_increasing_id())

res = pipeline.fit(spark_df).transform(spark_df)

# Result

res.selectExpr("idx as doc_id","explode(filterer) as filter").show(truncate=80)

+------+--------------------------------------------------------------------------------+
|doc_id|                                                                          filter|
+------+--------------------------------------------------------------------------------+
|     0|{document, 0, 86, Coronavirus disease (COVID-19) is an infectious DISAESE cau...|
|     1|{document, 0, 136, Most people infected with the virus will experience mild t...|
|     3|{document, 0, 178, Older people and those with underlying medical conditions ...|
|     6|{document, 0, 185, Protect yourself and others from infection by staying at l...|
|    10|{document, 0, 134, The virus can spread from an infected person’s mouth or no...|
+------+--------------------------------------------------------------------------------+


{%- endcapture -%}


{%- capture model_scala_medical -%}
import spark.implicits._
 
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel
  .pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
  .setInputCols("document")
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols("sentence")
  .setOutputCol("token")

val wordEmbeddings = WordEmbeddingsModel
  .pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

val ner_jsl = NerModel
  .pretrained("ner_jsl", "en", "clinical/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner")

val nerConverter = new NerConverterInternal()
  .setInputCols(Array("sentence", "token", "ner"))
  .setOutputCol("ner_chunk")

val filterer = new DocumentFiltererByNER()
  .setInputCols(Array("sentence", "ner_chunk"))
  .setOutputCol("filterer")
  .setWhiteList(Array("Disease_Syndrome_Disorder"))

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  wordEmbeddings,
  ner_jsl,
  nerConverter,
  filterer
))

val data = Seq(
  "Coronavirus disease (COVID-19) is an infectious disease caused by the SARS-CoV-2 virus.",
  "Most people infected with the virus will experience mild to moderate respiratory illness and recover without requiring special treatment.",
  "However, some will become seriously ill and require medical attention.",
  "Older people and those with underlying medical conditions like cardiovascular disease, diabetes, chronic respiratory disease, or cancer are more likely to develop serious illness.",
  "Anyone can get sick with COVID-19 and become seriously ill or die at any age.",
  "The best way to prevent and slow down transmission is to be well informed about the disease and how the virus spreads.",
  "Protect yourself and others from infection by staying at least 1 metre apart from others, wearing a properly fitted mask, and washing your hands or using an alcohol-based rub frequently.",
  "Get vaccinated when it’s your turn and follow local guidance.",
  "Stay home if you feel unwell.",
  "If you have a fever, cough and difficulty breathing, seek medical attention.",
  "The virus can spread from an infected person’s mouth or nose in small liquid particles when they cough, sneeze, speak, sing or breathe.",
  "These particles range from larger respiratory droplets to smaller aerosols. It is important to practice respiratory etiquette, for example by coughing into a flexed elbow, and to stay home and self-isolate until you recover if you feel unwell."
).toDF("text")

val dfWithIdx = data.coalesce(1).withColumn("idx", monotonically_increasing_id())

val model = pipeline.fit(dfWithIdx)
val result = model.transform(dfWithIdx)

result.show(false) 

// result 

+------+--------------------------------------------------------------------------------+
|doc_id|                                                                          filter|
+------+--------------------------------------------------------------------------------+
|     0|{document, 0, 86, Coronavirus disease (COVID-19) is an infectious DISAESE cau...|
|     1|{document, 0, 136, Most people infected with the virus will experience mild t...|
|     3|{document, 0, 178, Older people and those with underlying medical conditions ...|
|     6|{document, 0, 185, Protect yourself and others from infection by staying at l...|
|    10|{document, 0, 134, The virus can spread from an infected person’s mouth or no...|
+------+--------------------------------------------------------------------------------+

{%- endcapture -%}


{%- capture model_notebook_link -%}
[DocumentFiltererByNER](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/DocumentFiltererByNER.ipynb)
{%- endcapture -%}

{%- capture model_api_link -%}
[DocumentFiltererByNER](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/DocumentFiltererByNER.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[DocumentFiltererByNER](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/document_filterer_by_ner/index.html#)
{%- endcapture -%}



{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical
model_notebook_link=model_notebook_link
model_api_link=model_api_link
model_python_api_link=model_python_api_link
%}
