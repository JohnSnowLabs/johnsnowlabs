---
layout: model
title: Detect Cancer Types
author: John Snow Labs
name: ner_cancer_types_wip
date: 2024-08-16
tags: [en, clinical, licensed, ner, cancer_types, oncology, biomarker]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.4.0
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This Named Entity Recognition (NER) model is specifically trained to extract critical information from clinical and biomedical text related to oncology. The model recognizes 6 main cancer types:

`CNS Tumor Type`: Tumors originating in the central nervous system, including brain and spinal cord tumors.
`Carcinoma Type`: Cancers arising from epithelial cells, which are the most common type of cancer, including breast, lung, and colorectal carcinomas.
`Leukemia Type`: Cancers of the blood and bone marrow, characterized by the abnormal proliferation of white blood cells.
`Lymphoma Type`: Cancers of the lymphatic system, affecting lymphocytes (a type of white blood cell), including Hodgkin and non-Hodgkin lymphomas.
`Melanoma`: A type of skin cancer originating from melanocytes, the cells that produce pigment.
`Sarcoma Type`: Cancers arising from connective tissues, such as bone, cartilage, fat, muscle, or vascular tissues.

The model also extracts the following items, which provide crucial context for cancer diagnosis, treatment, and prognosis.

`Metastasis`: Recognizes terms related to the spread of cancer to different parts of the body, including mentions of metastatic sites and related clinical descriptions.
`Biomarker`: Extracts entities related to cancer biomarkers, including genetic markers, protein levels, and other measurable indicators used for cancer diagnosis, prognosis, and treatment response.
`Biomarker_Quant`: Extracts numerical measurements or values associated with the biomarker.
`Biomarker_Result`: Extracts descriptive or categorical assessments of the biomarker status.
`Body Site`: Knowing the primary site of the tumor is essential for diagnosis and treatment planning. The body site where the cancer originates often determines the type of cancer and influences therapeutic approaches.


## Predicted Entities

`CNS_Tumor_Type`, `Carcinoma_Type`, `Leukemia_Type`, `Lymphoma_Type`, `Melanoma`, `Sarcoma_Type`, `Metastasis`, `Body_Site`, `Biomarker`, `Biomarker_Quant`, `Biomarker_Result`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_cancer_types_wip_en_5.4.0_3.0_1723812559734.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_cancer_types_wip_en_5.4.0_3.0_1723812559734.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = MedicalNerModel.pretrained('cancer_types_wip', "en", "clinical/models")\
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
Patient A, a 55-year-old female, presented with carcinoma in the left breast. A biopsy revealed an elevated HER2. The patient also showed a slightly elevated CA 15-3 level at 45 U/mL. Follow-up imaging revealed metastasis to the axillary lymph nodes, and further scans indicated small metastatic lesions in the liver.

Additionally, imaging of the patient's lower back indicated a possible sarcoma. Subsequent tests identified elevated levels of lactate dehydrogenase (LDH), with a result of 580 IU/L (normal range: 140-280 IU/L), and a biopsy confirmed metastasis to the lungs.

Routine bloodwork revealed a mild increase in B2M (Beta-2 microglobulin), suggestive of possible lymphoma, and a normal range for hemoglobin and white blood cells, ruling out leukemia. CNS involvement was ruled out as imaging did not indicate any anomalies.

For melanoma screening, a suspicious mole on the patient's arm was biopsied, and tests confirmed a BRAF V600E mutation. Further imaging revealed metastatic spread to the lungs and liver.
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

val ner_model = MedicalNerModel.pretrained("ner_cancer_types_wip", "en", "clinical/models")
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

val sample_texts = Seq("""Patient A, a 55-year-old female, presented with carcinoma in the left breast. A biopsy revealed an elevated HER2. The patient also showed a slightly elevated CA 15-3 level at 45 U/mL. Follow-up imaging revealed metastasis to the axillary lymph nodes, and further scans indicated small metastatic lesions in the liver.

Additionally, imaging of the patient's lower back indicated a possible sarcoma. Subsequent tests identified elevated levels of lactate dehydrogenase (LDH), with a result of 580 IU/L (normal range: 140-280 IU/L), and a biopsy confirmed metastasis to the lungs.

Routine bloodwork revealed a mild increase in B2M (Beta-2 microglobulin), suggestive of possible lymphoma, and a normal range for hemoglobin and white blood cells, ruling out leukemia. CNS involvement was ruled out as imaging did not indicate any anomalies.

For melanoma screening, a suspicious mole on the patient's arm was biopsied, and tests confirmed a BRAF V600E mutation. Further imaging revealed metastatic spread to the lungs and liver.
""").toDF("text")

val result = pipeline.fit(sample_texts).transform(sample_texts)
```
</div>

## Results

```bash
+--------------------+-----+----+----------------+
|chunk               |begin|end |ner_label       |
+--------------------+-----+----+----------------+
|carcinoma           |49   |57  |Carcinoma_Type  |
|breast              |71   |76  |Body_Site       |
|elevated            |100  |107 |Biomarker_Result|
|HER2                |109  |112 |Biomarker       |
|elevated            |150  |157 |Biomarker_Result|
|CA 15-3             |159  |165 |Biomarker       |
|45 U/mL             |176  |182 |Biomarker_Quant |
|metastasis          |212  |221 |Metastasis      |
|axillary lymph nodes|230  |249 |Body_Site       |
|metastatic          |286  |295 |Metastasis      |
|liver               |312  |316 |Body_Site       |
|sarcoma             |391  |397 |Sarcoma_Type    |
|elevated            |428  |435 |Biomarker_Result|
|LDH                 |470  |472 |Biomarker       |
|580 IU/L            |493  |500 |Biomarker_Quant |
|metastasis          |555  |564 |Metastasis      |
|lungs               |573  |577 |Body_Site       |
|B2M                 |627  |629 |Biomarker       |
|lymphoma            |678  |685 |Lymphoma_Type   |
|leukemia            |756  |763 |Leukemia_Type   |
|CNS                 |766  |768 |Body_Site       |
|melanoma            |844  |851 |Melanoma        |
|arm                 |899  |901 |Body_Site       |
|BRAF                |939  |942 |Biomarker       |
|mutation            |950  |957 |Biomarker_Result|
|metastatic          |985  |994 |Metastasis      |
|lungs               |1010 |1014|Body_Site       |
|liver               |1020 |1024|Body_Site       |
+--------------------+-----+----+----------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_cancer_types_wip|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|4.9 MB|

## References

In-house annotated oncology case reports.

## Benchmarking

```bash
           label  precision    recall  f1-score   support
       Biomarker       0.94      0.89      0.92       624
 Biomarker_Quant       0.82      0.74      0.78       119
Biomarker_Result       0.87      0.81      0.84       201
       Body_Site       0.93      0.91      0.92      1675
  CNS_Tumor_Type       0.93      0.93      0.93       243
  Carcinoma_Type       0.85      0.92      0.88       334
   Leukemia_Type       1.00      1.00      1.00         4
   Lymphoma_Type       0.91      0.90      0.90        86
        Melanoma       0.97      0.96      0.97       326
      Metastasis       0.99      0.97      0.98       176
    Sarcoma_Type       0.86      0.99      0.92        84
       micro avg       0.92      0.91      0.92      3872
       macro avg       0.92      0.91      0.91      3872
    weighted avg       0.92      0.91      0.92      3872
```
