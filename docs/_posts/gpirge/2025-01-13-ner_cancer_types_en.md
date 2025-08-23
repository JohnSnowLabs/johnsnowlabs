---
layout: model
title: Detect Cancer Types
author: John Snow Labs
name: ner_cancer_types
date: 2025-01-13
tags: [en, clinical, licensed, ner, cancer_types, biomarker, oncology]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.5.1
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Description

This Named Entity Recognition (NER) model is specifically trained to extract critical information from clinical and biomedical text related to oncology. The model recognizes 6 main cancer types:

`CNS Tumor Type`: Tumors originating in the central nervous system, including brain and spinal cord tumors.
`Carcinoma Type`: Cancers arising from epithelial cells, which are the most common type of cancer, including breast, lung, and colorectal carcinomas.
`Leukemia Type`: Cancers of the blood and bone marrow, characterized by the abnormal proliferation of white blood cells.
`Lymphoma Type`: Cancers of the lymphatic system, affecting lymphocytes (a type of white blood cell), including Hodgkin and non-Hodgkin lymphomas.
`Melanoma`: A type of skin cancer originating from melanocytes, the cells that produce pigment.
`Sarcoma Type`: Cancers arising from connective tissues, such as bone, cartilage, fat, muscle, or vascular tissues.
`Other_Tumors`: All benign tumors (such as lipoma, fibroma, hemangioma, neurofibroma, osteochondroma, adenoma, papilloma, chordoma etc.) go under this entity. 

The model also extracts the following items, which provide crucial context for cancer diagnosis, treatment, and prognosis.

`Metastasis`: Recognizes terms related to the spread of cancer to different parts of the body, including mentions of metastatic sites and related clinical descriptions.
`Biomarker`: Extracts entities related to cancer biomarkers, including genetic markers, protein levels, and other measurable indicators used for cancer diagnosis, prognosis, and treatment response.
`Biomarker_Quant`: Extracts numerical measurements or values associated with the biomarker.
`Biomarker_Result`: Extracts descriptive or categorical assessments of the biomarker status.
`Body Site`: Knowing the primary site of the tumor is essential for diagnosis and treatment planning. The body site where the cancer originates often determines the type of cancer and influences therapeutic approaches.

## Predicted Entities

`Biomarker`, `Biomarker_Quant`, `Biomarker_Result`, `Body_Site`, `CNS_Tumor_Type`, `Carcinoma_Type`, `Leukemia_Type`, `Lymphoma_Type`, `Melanoma`, `Metastasis`, `Other_Tumors`, `Sarcoma_Type`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/01.0.Clinical_Named_Entity_Recognition_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_cancer_types_en_5.5.1_3.0_1736798165184.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_cancer_types_en_5.5.1_3.0_1736798165184.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

clinical_embeddings = WordEmbeddingsModel.pretrained('embeddings_clinical', "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained('ner_cancer_types', "en", "clinical/models")\
    .setInputCols(["sentence", "token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(['sentence', 'token', 'ner'])\
    .setOutputCol('ner_chunk')

pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter   
    ])

sample_texts = ["""
We report a case of CD3 negative, CD20 positive T-cell prolymphocytic leukemia (T-PLL). The leukemic cells were negative for surface CD3, CD2, and CD7 and strongly positive for CD20. 

T-cell lineage markers such as CD4, CD5, and cytoplasmic CD3 were also positive. A monoclonal rearrangement of the T-cell receptor (TCR) β chain gene was detected. 

CD3 negative T-PLL has been reported often, but CD20 positive T-PLL has not. We reviewed seven cases of CD20 positive immature and mature T-cell leukemias, including the present case. 

Three were immature T-cell leukemias (acute lymphoblastic leukemia), and four were mature T-cell leukemias (granular lymphocytic leukemia, small lymphocytic lymphoma/chronic lymphocytic leukemia, 
adult T-cell leukemia, and the present case). 

"""]

data = spark.createDataFrame(sample_texts, StringType()).toDF("text")

result = pipeline.fit(data).transform(data)
```
{:.jsl-block}
```python
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

clinical_embeddings = nlp.WordEmbeddingsModel.pretrained('embeddings_clinical', "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = medical.NerModel.pretrained('ner_cancer_types', "en", "clinical/models")\
    .setInputCols(["sentence", "token","embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(['sentence', 'token', 'ner'])\
    .setOutputCol('ner_chunk')

pipeline = nlp.Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter   
    ])

sample_texts = ["""
We report a case of CD3 negative, CD20 positive T-cell prolymphocytic leukemia (T-PLL). The leukemic cells were negative for surface CD3, CD2, and CD7 and strongly positive for CD20. 

T-cell lineage markers such as CD4, CD5, and cytoplasmic CD3 were also positive. A monoclonal rearrangement of the T-cell receptor (TCR) β chain gene was detected. 

CD3 negative T-PLL has been reported often, but CD20 positive T-PLL has not. We reviewed seven cases of CD20 positive immature and mature T-cell leukemias, including the present case. 

Three were immature T-cell leukemias (acute lymphoblastic leukemia), and four were mature T-cell leukemias (granular lymphocytic leukemia, small lymphocytic lymphoma/chronic lymphocytic leukemia, 
adult T-cell leukemia, and the present case). 

"""]

data = spark.createDataFrame(sample_texts, StringType()).toDF("text")

result = pipeline.fit(data).transform(data)
```

```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_cancer_types", "en", "clinical/models")
    .setInputCols(Array("sentence", "token","embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentenceDetector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter   
))

val sample_texts = Seq("""We report a case of CD3 negative, CD20 positive T-cell prolymphocytic leukemia (T-PLL). The leukemic cells were negative for surface CD3, CD2, and CD7 and strongly positive for CD20. 

T-cell lineage markers such as CD4, CD5, and cytoplasmic CD3 were also positive. A monoclonal rearrangement of the T-cell receptor (TCR) β chain gene was detected. 

CD3 negative T-PLL has been reported often, but CD20 positive T-PLL has not. We reviewed seven cases of CD20 positive immature and mature T-cell leukemias, including the present case. 

Three were immature T-cell leukemias (acute lymphoblastic leukemia), and four were mature T-cell leukemias (granular lymphocytic leukemia, small lymphocytic lymphoma/chronic lymphocytic leukemia, 
adult T-cell leukemia, and the present case).
""").toDF("text")

val result = pipeline.fit(sample_texts).transform(sample_texts)
```
</div>

## Results

```bash
+-------------------------------------------------------+-----+---+----------------+
|chunk                                                  |begin|end|ner_label       |
+-------------------------------------------------------+-----+---+----------------+
|CD3                                                    |21   |23 |Biomarker       |
|negative                                               |25   |32 |Biomarker_Result|
|CD20                                                   |35   |38 |Biomarker       |
|positive                                               |40   |47 |Biomarker_Result|
|T-cell prolymphocytic leukemia                         |49   |78 |Leukemia_Type   |
|T-PLL                                                  |81   |85 |Leukemia_Type   |
|negative                                               |113  |120|Biomarker_Result|
|CD3                                                    |134  |136|Biomarker       |
|CD2                                                    |139  |141|Biomarker       |
|CD7                                                    |148  |150|Biomarker       |
|positive                                               |165  |172|Biomarker_Result|
|CD20                                                   |178  |181|Biomarker       |
|CD4                                                    |215  |217|Biomarker       |
|CD5                                                    |220  |222|Biomarker       |
|CD3                                                    |241  |243|Biomarker       |
|positive                                               |255  |262|Biomarker_Result|
|CD3                                                    |348  |350|Biomarker       |
|negative                                               |352  |359|Biomarker_Result|
|T-PLL                                                  |361  |365|Leukemia_Type   |
|CD20                                                   |396  |399|Biomarker       |
|positive                                               |401  |408|Biomarker_Result|
|T-PLL                                                  |410  |414|Leukemia_Type   |
|CD20                                                   |452  |455|Biomarker       |
|positive                                               |457  |464|Biomarker_Result|
|mature T-cell leukemias                                |479  |501|Leukemia_Type   |
|T-cell leukemias                                       |552  |567|Leukemia_Type   |
|acute lymphoblastic leukemia                           |570  |597|Leukemia_Type   |
|mature T-cell leukemias                                |615  |637|Leukemia_Type   |
|granular lymphocytic leukemia                          |640  |668|Leukemia_Type   |
|small lymphocytic lymphoma/chronic lymphocytic leukemia|671  |725|Leukemia_Type   |
|adult T-cell leukemia                                  |728  |748|Leukemia_Type   |
+-------------------------------------------------------+-----+---+----------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_cancer_types|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|5.0 MB|

## References

In-house annotated case reports.

## Benchmarking

```bash
           label  precision    recall  f1-score   support
       Biomarker       0.89      0.89      0.89      1676
 Biomarker_Quant       0.69      0.89      0.78       162
Biomarker_Result       0.85      0.87      0.86       537
       Body_Site       0.90      0.95      0.92      3754
  CNS_Tumor_Type       0.80      0.78      0.79       137
  Carcinoma_Type       0.92      0.92      0.92       719
   Leukemia_Type       0.89      0.86      0.88       175
   Lymphoma_Type       0.86      0.91      0.89       365
        Melanoma       0.92      0.96      0.94       197
      Metastasis       0.98      0.98      0.98       289
    Other_Tumors       0.81      0.84      0.82       439
    Sarcoma_Type       0.94      0.87      0.90       344
       micro-avg       0.89      0.92      0.90      8794
       macro-avg       0.87      0.89      0.88      8794
    weighted-avg       0.89      0.92      0.90      8794
```
