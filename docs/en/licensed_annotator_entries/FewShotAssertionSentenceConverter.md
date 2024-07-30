{%- capture title -%}
FewShotAssertionSentenceConverter
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}

It is a util annotator that is used in some datasets to train a new FewShotAssertionClassifierModel.

Parameters:

- `scopeWindow` :  The scope window of the assertion expression


{%- endcapture -%}

{%- capture model_input_anno -%}
TOKEN
{%- endcapture -%}

{%- capture model_output_anno -%}
TOKEN
{%- endcapture -%}

{%- capture model_python_medical -%}

from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")\
    .setSplitChars(["-", "\/"])

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

# ner_oncology
ner_oncology = medical.NerModel.pretrained("ner_oncology","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner_oncology")

ner_oncology_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","ner_oncology"])\
    .setOutputCol("ner_chunk")

few_shot_assertion_converter = medical.FewShotAssertionSentenceConverter()\
    .setInputCols(["sentence", "token", "ner_chunk"])\
    .setOutputCol("assertion_sentence")

e5_embeddings = nlp.E5Embeddings.pretrained("e5_base_v2_embeddings_medical_assertion_oncology", "en", "clinical/models")\
    .setInputCols(["assertion_sentence"])\
    .setOutputCol("assertion_embedding")

few_shot_assertion_classifier = medical.FewShotAssertionClassifierModel()\
    .pretrained("fewhot_assertion_oncology_e5_base_v2_oncology", "en", "clinical/models")\
    .setInputCols(["assertion_embedding"])\
    .setOutputCol("assertion_fewshot")

assertion_pipeline = nlp.Pipeline(
    stages=[
        document_assembler,
        sentence_detector,
        tokenizer,
        word_embeddings,
        ner_oncology,
        ner_oncology_converter,
        few_shot_assertion_converter,
        e5_embeddings,
        few_shot_assertion_classifier
    ])

sample_text= [
"""The patient is suspected to have colorectal cancer. Her family history is positive for other cancers.
The result of the biopsy was positive. A CT scan was ordered to rule out metastases."""
]

data = spark.createDataFrame([sample_text]).toDF("text")

result = assertion_pipeline.fit(data).transform(data)

result.select(F.explode(F.arrays_zip(result.assertion_fewshot.metadata,
                        result.assertion_fewshot.begin,
                        result.assertion_fewshot.end,
                        result.assertion_fewshot.result,)).alias("cols")) \
                        .select(F.expr("cols['0']['ner_chunk']").alias("ner_chunk"),
                        F.expr("cols['1']").alias("begin"),
                        F.expr("cols['2']").alias("end"),
                        F.expr("cols['0']['ner_label']").alias("ner_label"),
                        F.expr("cols['3']").alias("assertion"),
                        F.expr("cols['0']['confidence']").alias("confidence") ).show(truncate=False)



## Result

+-----------------+-----+---+----------------+---------+----------+
|ner_chunk        |begin|end|ner_label       |assertion|confidence|
+-----------------+-----+---+----------------+---------+----------+
|colorectal cancer|33   |49 |Cancer_Dx       |Possible |0.5812815 |
|Her              |52   |54 |Gender          |Present  |0.9562998 |
|cancers          |93   |99 |Cancer_Dx       |Family   |0.23465642|
|biopsy           |120  |125|Pathology_Test  |Past     |0.95732147|
|positive         |131  |138|Pathology_Result|Present  |0.9564386 |
|CT scan          |143  |149|Imaging_Test    |Past     |0.9571699 |
|metastases       |175  |184|Metastasis      |Possible |0.54986554|
+-----------------+-----+---+----------------+---------+----------+



{%- endcapture -%}

{%- capture model_scala_medical -%}

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel
    .pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")
    .setSplitChars(Array("-", "/"))

val wordEmbeddings = WordEmbeddingsModel
    .pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val nerOncology = MedicalNerModel
    .pretrained("ner_oncology", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner_oncology")

val nerOncologyConverter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner_oncology"))
    .setOutputCol("ner_chunk")

val fewShotAssertionConverter = new FewShotAssertionSentenceConverter()
    .setInputCols(Array("sentence", "token", "ner_chunk"))
    .setOutputCol("assertion_sentence")

val e5Embeddings = E5Embeddings
    .pretrained("e5_base_v2_embeddings_medical_assertion_oncology", "en", "clinical/models")
    .setInputCols(Array("assertion_sentence"))
    .setOutputCol("assertion_embedding")

val fewShotAssertionClassifier = FewShotAssertionClassifierModel
    .pretrained("fewhot_assertion_oncology_e5_base_v2_oncology", "en", "clinical/models")
    .setInputCols(Array("assertion_embedding"))
    .setOutputCol("assertion_fewshot")

val pipeline = new Pipeline()
    .setStages(Array(
        documentAssembler,
        sentenceDetector,
        tokenizer,
        wordEmbeddings,
        nerOncology,
        nerOncologyConverter,
        fewShotAssertionConverter,
        e5Embeddings,
        fewShotAssertionClassifier
    ))

val sampleText = Seq("The patient is suspected to have colorectal cancer. Her family history is positive for other cancers. 
The result of the biopsy was positive. A CT scan was ordered to rule out metastases.")

val data = spark.createDataFrame(sampleText).toDF("text")

val result = pipeline.fit(data).transform(data)

result.show(false)

## Result

+-----------------+-----+---+----------------+---------+----------+
|ner_chunk        |begin|end|ner_label       |assertion|confidence|
+-----------------+-----+---+----------------+---------+----------+
|colorectal cancer|33   |49 |Cancer_Dx       |Possible |0.5812815 |
|Her              |52   |54 |Gender          |Present  |0.9562998 |
|cancers          |93   |99 |Cancer_Dx       |Family   |0.23465642|
|biopsy           |120  |125|Pathology_Test  |Past     |0.95732147|
|positive         |131  |138|Pathology_Result|Present  |0.9564386 |
|CT scan          |143  |149|Imaging_Test    |Past     |0.9571699 |
|metastases       |175  |184|Metastasis      |Possible |0.54986554|
+-----------------+-----+---+----------------+---------+----------+


{%- endcapture -%}


{%- capture model_api_link -%}
[FewShotAssertionSentenceConverter](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/assertion/FewShotAssertionSentenceConverter.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[FewShotAssertionSentenceConverter](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/assertion/fewshot_assertion_sentence_converter/index.html)
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
