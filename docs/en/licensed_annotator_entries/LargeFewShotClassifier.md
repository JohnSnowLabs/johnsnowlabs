{%- capture title -%}
LargeFewShotClassifier
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}

The  LargeFewShotClassifierModel annotator is designed to work effectively with minimal labeled data, offering flexibility and adaptability to new, unseen classes. Key parameters include batch size, case sensitivity, and maximum sentence length.Large Few-Shot Classifier Model can achieve impressive performance even with minimal labeled data. 

Parameters:

- `inputCols` : Input columns containing DOCUMENT annotations.
- `outputCol` : Output column name where classification results (CATEGORY) are stored.
- `batchSize` : Batch size for processing documents (default: 8).
- `caseSensitive` : Whether the classifier is sensitive to text casing (default: false).
- `maxSentenceLength` : Maximum input sentence length (text beyond this may be truncated).

{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_output_anno -%}
CATEGORY
{%- endcapture -%}

{%- capture model_python_medical -%}

from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

large_few_shot_classifier = medical.LargeFewShotClassifierModel()\
    .pretrained("large_fewshot_classifier_ade", "en", "clinical/models")\
    .setInputCols("document")\
    .setOutputCol("prediction")

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    large_few_shot_classifier
])

data = spark.createDataFrame(["The patient developed severe liver toxicity after taking the medication for three weeks",
                              "He experienced no complications during the treatment and reported feeling much better.",
                              "She experienced a sudden drop in blood pressure after the administration of the new drug.",
                              "The doctor recommended a daily dosage of the vitamin supplement to improve her health."], StringType()).toDF("text")

result = pipeline.fit(data).transform(data)

result.select("text", col("prediction.result").getItem(0).alias("result")).show(truncate=False)

## Result

+-----------------------------------------------------------------------------------------+------+
|text                                                                                     |result|
+-----------------------------------------------------------------------------------------+------+
|The patient developed severe liver toxicity after taking the medication for three weeks  |ADE   |
|He experienced no complications during the treatment and reported feeling much better.   |noADE |
|She experienced a sudden drop in blood pressure after the administration of the new drug.|ADE   |
|The doctor recommended a daily dosage of the vitamin supplement to improve her health.   |noADE |
+-----------------------------------------------------------------------------------------+------+

{%- endcapture -%}

{%- capture model_scala_medical -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val largeFewShotClassifier = LargeFewShotClassifierModel()
    .pretrained("large_fewshot_classifier_ade")
    .setInputCols("document")
    .setOutputCol("prediction")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    largeFewShotClassifier
))

val textList = Seq(
    ("The patient developed severe liver toxicity after taking the medication for three weeks"),
    ("He experienced no complications during the treatment and reported feeling much better."),
    ("She experienced a sudden drop in blood pressure after the administration of the new drug."),
    ("The doctor recommended a daily dosage of the vitamin supplement to improve her health.")
)

val data = spark.createDataFrame(textList).toDF("text")

val result = pipeline.fit(data).transform(data)

result.select(col("text"), col("prediction.result").getItem(0).alias("result")).show(truncate = false)

// Result

+-----------------------------------------------------------------------------------------+------+
|text                                                                                     |result|
+-----------------------------------------------------------------------------------------+------+
|The patient developed severe liver toxicity after taking the medication for three weeks  |ADE   |
|He experienced no complications during the treatment and reported feeling much better.   |noADE |
|She experienced a sudden drop in blood pressure after the administration of the new drug.|ADE   |
|The doctor recommended a daily dosage of the vitamin supplement to improve her health.   |noADE |
+-----------------------------------------------------------------------------------------+------+

{%- endcapture -%}


{%- capture model_api_link -%}
[LargeFewShotClassifier](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/deid/LargeFewShotClassifier.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[LargeFewShotClassifier](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/classification/large_few_shot_classifier/index.html#)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[Mapper2Chunk](https://https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/tutorials/Certification_Trainings/Healthcare/30.4.Text_Classification_with_LargeFewShotClassifier.ipynb)
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
