{%- capture title -%}
FewShotAssertionClassifierModel
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}

FewShotAssertionClassifierModel does assertion classification using can run large (LLMS based)
few shot classifiers based on the SetFit approach.

Parameters:

- `batchSize` *(Int)*: Batch size

- `caseSensitive` *(Bool)*: Whether the classifier is sensitive to text casing

- `maxSentenceLength` *(Int)*: The maximum length of the input text


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
     .setInputCol("text")\
     .setOutputCol("document")

 sentence_detector = nlp.SentenceDetector()\
    .setInputCol("document")\
    .setOutputCol("sentence")

 tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

 embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings") \
    .setCaseSensitive(False)

 ner = medical.NerModel.pretrained("ner_jsl", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

 ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setWhiteList("Disease_Syndrome_Disorder", "Hypertension")\
    .setOutputCol("ner_chunk")

 few_shot_assertion_classifier = medical.FewShotAssertionClassifierModel().pretrained()\
     .setInputCols(["sentence", "ner_chunk"])\
     .setOutputCol("assertion")

data = spark.createDataFrame(
    [["Includes hypertension and chronic obstructive pulmonary disease."]]
     ).toDF("text")

results = Pipeline() \
    .setStages([
                document_assembler,
                sentence_detector,
                tokenizer, 
                embeddings,
                ner,
                ner_converter,
                few_shot_assertion_classifier]) \
    .fit(data) \
    .transform(data) \

results.selectExpr("assertion.result", "assertion.metadata.chunk", "assertion.metadata.confidence").show()

## Result

+--------+----------------------------+-----------+
|  result|                       chunk| confidence|
+--------+----------------------------+-----------+
| present|                hypertension|        1.0|
|  absent| arteriovenous malformations|        1.0|
+--------+----------------------------+-----------+

{%- endcapture -%}

{%- capture model_scala_medical -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
    .setInputCols(Array("document"))
    .setOutputCol("sentences")

val tokenizer = Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

val embeddings = WordEmbeddingsModel
    .pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")
    .setCaseSensitive(False)

val ner = MedicalNerModel
    .pretrained("ner_jsl", "en", "clinical/models")
    .setInputCols(["sentence", "token", "embeddings"])
    .setOutputCol("ner")

val nerConverter = NerConverter()
    .setInputCols(Array("sentence", "token", "ner"))
    .setWhiteList("Disease_Syndrome_Disorder", "Hypertension")
    .setOutputCol("ner_chunk")

val fewShotAssertionClassifier = LargeFewShotClassifierModel
    .pretrained("clinical_assertion")
    .setInputCols(Array("sentence"))
    .setBatchSize(1)
    .setOutputCol("label")

val pipeline = new Pipeline()
    .setStages(Array(
        documentAssembler,
        sentenceDetector, 
        tokenizer,
        embeddings,
        ner, 
        nerConverter,
        fewShotAssertionClassifier))

val model = pipeline.fit(Seq().toDS.toDF("text"))
val results = model.transform(Seq("Includes hypertension and chronic obstructive pulmonary disease.").toDS.toDF("text"))

results.selectExpr("explode(assertion) as assertion")
       .selectExpr("assertion.result", "assertion.metadata.chunk", "assertion.metadata.confidence")
       .show(truncate = false)

// Result       

+-------+-------------------------------------+----------+
|result |chunk                                |confidence|
+-------+-------------------------------------+----------+
|present|hypertension                         |1.0       |
|present|chronic obstructive pulmonary disease|1.0       |
|absent |arteriovenous malformations          |1.0       |
|absent |vascular malformation                |0.9999997 |
+-------+-------------------------------------+----------+

{%- endcapture -%}

{%- capture model_api_link -%}
[FewShotAssertionClassifierModel](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/classification/FewShotAssertionClassifierModel.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[FewShotAssertionClassifierModel](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/classification/few_shot_assertion_classifier/index.html)
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
%}
