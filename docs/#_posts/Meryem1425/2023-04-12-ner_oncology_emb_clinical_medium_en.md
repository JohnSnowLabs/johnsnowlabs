---
layout: model
title: Detect Oncology-Specific Entities (clinical_medium)
author: John Snow Labs
name: ner_oncology_emb_clinical_medium
date: 2023-04-12
tags: [licensed, en, clinical, clinical_medium, ner, oncology, biomarker, treatment]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.3.2
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts more than 40 oncology-related entities, including therapies, tests and staging.

Definitions of Predicted Entities:

`Adenopathy:` Mentions of pathological findings of the lymph nodes.
`Age:` All mention of ages, past or present, related to the patient or with anybody else.
`Biomarker:` Biological molecules that indicate the presence or absence of cancer, or the type of cancer. Oncogenes are excluded from this category.
`Biomarker_Result:` Terms or values that are identified as the result of a biomarkers.
`Cancer_Dx:` Mentions of cancer diagnoses (such as “breast cancer”) or pathological types that are usually used as synonyms for “cancer” (e.g. “carcinoma”). When anatomical references are present, they are included in the Cancer_Dx extraction.
`Cancer_Score:` Clinical or imaging scores that are specific for cancer settings (e.g. “BI-RADS” or “Allred score”).
`Cancer_Surgery:` Terms that indicate surgery as a form of cancer treatment.
`Chemotherapy:` Mentions of chemotherapy drugs, or unspecific words such as “chemotherapy”.
`Cycle_Coun:` The total number of cycles being administered of an oncological therapy (e.g. “5 cycles”).
`Cycle_Day:` References to the day of the cycle of oncological therapy (e.g. “day 5”).
`Cycle_Number:` The number of the cycle of an oncological therapy that is being applied (e.g. “third cycle”).
`Date:` Mentions of exact dates, in any format, including day number, month and/or year.
`Death_Entity:` Words that indicate the death of the patient or someone else (including family members), such as “died” or “passed away”.
`Direction:` Directional and laterality terms, such as “left”, “right”, “bilateral”, “upper” and “lower”.
`Dosage:` The quantity prescribed by the physician for an active ingredient.
`Duration:` Words indicating the duration of a treatment (e.g. “for 2 weeks”).
`Frequency:` Words indicating the frequency of treatment administration (e.g. “daily” or “bid”).
`Gender:` Gender-specific nouns and pronouns (including words such as “him” or “she”, and family members such as “father”).
`Grade:` All pathological grading of tumors (e.g. “grade 1”) or degrees of cellular differentiation (e.g. “well-differentiated”)
`Histological_Type:` Histological variants or cancer subtypes, such as “papillary”, “clear cell” or “medullary”.
`Hormonal_Therapy:` Mentions of hormonal drugs used to treat cancer, or unspecific words such as “hormonal therapy”.
`Imaging_Test:` Imaging tests mentioned in texts, such as “chest CT scan”.
`Immunotherapy:` Mentions of immunotherapy drugs, or unspecific words such as “immunotherapy”.
`Invasion:` Mentions that refer to tumor invasion, such as “invasion” or “involvement”. Metastases or lymph node involvement are excluded from this category.
`Line_Of_Therapy:` Explicit references to the line of therapy of an oncological therapy (e.g. “first-line treatment”).
`Metastasis:` Terms that indicate a metastatic disease. Anatomical references are not included in these extractions.
`Oncogene:` Mentions of genes that are implicated in the etiology of cancer.
`Pathology_Result:` The findings of a biopsy from the pathology report that is not covered by another entity (e.g. “malignant ductal cells”).
`Pathology_Test:` Mentions of biopsies or tests that use tissue samples.
`Performance_Status:` Mentions of performance status scores, such as ECOG and Karnofsky. The name of the score is extracted together with the result (e.g. “ECOG performance status of 4”).
`Race_Ethnicity:` The race and ethnicity categories include racial and national origin or sociocultural groups.
`Radiotherapy:` Terms that indicate the use of Radiotherapy.
`Response_To_Treatment:` Terms related to clinical progress of the patient related to cancer treatment, including “recurrence”, “bad response” or “improvement”.
`Relative_Date:` Temporal references that are relative to the date of the text or to any other specific date (e.g. “yesterday” or “three years later”).
`Route:` Words indicating the type of administration route (such as “PO” or “transdermal”).
`Site_Bone:` Anatomical terms that refer to the human skeleton.
`Site_Brain:` Anatomical terms that refer to the central nervous system (including the brain stem and the cerebellum).
`Site_Breast:` Anatomical terms that refer to the breasts.
`Site_Liver:` Anatomical terms that refer to the liver.
`Site_Lung:` Anatomical terms that refer to the lungs.
`Site_Lymph_Node:` Anatomical terms that refer to lymph nodes, excluding adenopathies.
`Site_Other_Body_Part:` Relevant anatomical terms that are not included in the rest of the anatomical entities.
`Smoking_Status:` All mentions of smoking related to the patient or to someone else.
`Staging:` Mentions of cancer stage such as “stage 2b” or “T2N1M0”. It also includes words such as “in situ”, “early-stage” or “advanced”.
`Targeted_Therapy:` Mentions of targeted therapy drugs, or unspecific words such as “targeted therapy”.
`Tumor_Finding:` All nonspecific terms that may be related to tumors, either malignant or benign (for example: “mass”, “tumor”, “lesion”, or “neoplasm”).
`Tumor_Size:` Size of the tumor, including numerical value and unit of measurement (e.g. “3 cm”).
`Unspecific_Therapy:` Terms that indicate a known cancer therapy but that is not specific to any other therapy entity (e.g. “chemoradiotherapy” or “adjuvant therapy”).

## Predicted Entities

`Histological_Type`, `Direction`, `Staging`, `Cancer_Score`, `Imaging_Test`, `Cycle_Number`, `Tumor_Finding`, `Site_Lymph_Node`, `Invasion`, `Response_To_Treatment`, `Smoking_Status`, `Tumor_Size`, `Cycle_Count`, `Adenopathy`, `Age`, `Biomarker_Result`, `Unspecific_Therapy`, `Site_Breast`, `Chemotherapy`, `Targeted_Therapy`, `Radiotherapy`, `Performance_Status`, `Pathology_Test`, `Site_Other_Body_Part`, `Cancer_Surgery`, `Line_Of_Therapy`, `Pathology_Result`, `Hormonal_Therapy`, `Site_Bone`, `Biomarker`, `Immunotherapy`, `Cycle_Day`, `Frequency`, `Route`, `Duration`, `Death_Entity`, `Metastasis`, `Site_Liver`, `Cancer_Dx`, `Grade`, `Date`, `Site_Lung`, `Site_Brain`, `Relative_Date`, `Race_Ethnicity`, `Gender`, `Oncogene`, `Dosage`, `Radiation_Dose`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_ONCOLOGY_CLINICAL/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/27.Oncology_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_oncology_emb_clinical_medium_en_4.3.2_3.0_1681316892301.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_oncology_emb_clinical_medium_en_4.3.2_3.0_1681316892301.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical_medium", "en", "clinical/models")\
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")                

ner = MedicalNerModel.pretrained("ner_oncology_emb_clinical_medium", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[document_assembler,
                            sentence_detector,
                            tokenizer,
                            word_embeddings,
                            ner,
                            ner_converter])

data = spark.createDataFrame([["""The had previously undergone a left mastectomy and an axillary lymph node dissection for a left breast cancer twenty years ago.
The tumor was positive for ER and PR. Postoperatively, radiotherapy was administered to the residual breast.
The cancer recurred as a right lung metastasis 13 years later. The patient underwent a regimen consisting of adriamycin (60 mg/m2) and cyclophosphamide (600 mg/m2) over six courses, as first line therapy."""]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical_medium", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")                

val ner = MedicalNerModel.pretrained("ner_oncology_emb_clinical_medium", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(document_assembler,
                            sentence_detector,
                            tokenizer,
                            word_embeddings,
                            ner,
                            ner_converter))    

val data = Seq("The had previously undergone a left mastectomy and an axillary lymph node dissection for a left breast cancer twenty years ago.
The tumor was positive for ER and PR. Postoperatively, radiotherapy was administered to the residual breast.
The cancer recurred as a right lung metastasis 13 years later. The patient underwent a regimen consisting of adriamycin (60 mg/m2) and cyclophosphamide (600 mg/m2) over six courses, as first line therapy.").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-------------------+-----+---+---------------------+
|chunk              |begin|end|ner_label            |
+-------------------+-----+---+---------------------+
|left               |31   |34 |Direction            |
|mastectomy         |36   |45 |Cancer_Surgery       |
|axillary lymph node|54   |72 |Site_Lymph_Node      |
|dissection         |74   |83 |Cancer_Surgery       |
|left               |91   |94 |Direction            |
|breast cancer      |96   |108|Cancer_Dx            |
|twenty years ago   |110  |125|Relative_Date        |
|tumor              |132  |136|Tumor_Finding        |
|positive           |142  |149|Biomarker_Result     |
|ER                 |155  |156|Biomarker            |
|PR                 |162  |163|Response_To_Treatment|
|radiotherapy       |183  |194|Radiotherapy         |
|breast             |229  |234|Site_Breast          |
|cancer             |241  |246|Cancer_Dx            |
|recurred           |248  |255|Response_To_Treatment|
|right              |262  |266|Direction            |
|lung               |268  |271|Site_Lung            |
|metastasis         |273  |282|Metastasis           |
|13 years later     |284  |297|Relative_Date        |
|adriamycin         |346  |355|Chemotherapy         |
|60 mg/m2           |358  |365|Chemotherapy         |
|cyclophosphamide   |372  |387|Chemotherapy         |
|600 mg/m2          |390  |398|Dosage               |
|six courses        |406  |416|Cycle_Count          |
|first line         |422  |431|Line_Of_Therapy      |
+-------------------+-----+---+---------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_oncology_emb_clinical_medium|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|15.4 MB|

## Benchmarking

```bash
               label     tp    fp    fn  total precision recall     f1
   Histological_Type  138.0  27.0  73.0  211.0    0.8364  0.654  0.734
           Direction  679.0 163.0 152.0  831.0    0.8064 0.8171 0.8117
             Staging  112.0  24.0  26.0  138.0    0.8235 0.8116 0.8175
        Cancer_Score    9.0   2.0  12.0   21.0    0.8182 0.4286 0.5625
        Imaging_Test  759.0 132.0 141.0  900.0    0.8519 0.8433 0.8476
        Cycle_Number   43.0  29.0  17.0   60.0    0.5972 0.7167 0.6515
       Tumor_Finding  971.0  98.0 108.0 1079.0    0.9083 0.8999 0.9041
     Site_Lymph_Node  210.0  80.0  61.0  271.0    0.7241 0.7749 0.7487
            Invasion  146.0  33.0  21.0  167.0    0.8156 0.8743 0.8439
Response_To_Treat...  224.0  98.0 146.0  370.0    0.6957 0.6054 0.6474
      Smoking_Status   39.0  14.0   9.0   48.0    0.7358 0.8125 0.7723
         Cycle_Count  113.0  34.0  31.0  144.0    0.7687 0.7847 0.7766
          Tumor_Size  203.0  44.0  35.0  238.0    0.8219 0.8529 0.8371
          Adenopathy   32.0  12.0  11.0   43.0    0.7273 0.7442 0.7356
                 Age  203.0  20.0  25.0  228.0    0.9103 0.8904 0.9002
    Biomarker_Result  537.0 117.0 148.0  685.0    0.8211 0.7839 0.8021
  Unspecific_Therapy  107.0  32.0  67.0  174.0    0.7698 0.6149 0.6837
         Site_Breast   95.0  17.0  15.0  110.0    0.8482 0.8636 0.8559
        Chemotherapy  684.0  72.0  58.0  742.0    0.9048 0.9218 0.9132
    Targeted_Therapy  170.0  31.0  36.0  206.0    0.8458 0.8252 0.8354
        Radiotherapy  141.0  43.0  20.0  161.0    0.7663 0.8758 0.8174
  Performance_Status   20.0  12.0  12.0   32.0     0.625  0.625  0.625
      Pathology_Test  359.0 159.0 127.0  486.0    0.6931 0.7387 0.7151
Site_Other_Body_Part  744.0 338.0 394.0 1138.0    0.6876 0.6538 0.6703
      Cancer_Surgery  380.0  83.0 113.0  493.0    0.8207 0.7708  0.795
     Line_Of_Therapy   38.0   7.0  10.0   48.0    0.8444 0.7917 0.8172
    Pathology_Result  124.0 144.0 217.0  341.0    0.4627 0.3636 0.4072
    Hormonal_Therapy   96.0  13.0  27.0  123.0    0.8807 0.7805 0.8276
           Site_Bone  167.0  50.0  56.0  223.0    0.7696 0.7489 0.7591
       Immunotherapy   61.0  13.0  21.0   82.0    0.8243 0.7439 0.7821
           Biomarker  681.0  88.0 150.0  831.0    0.8856 0.8195 0.8513
           Cycle_Day   85.0  43.0  43.0  128.0    0.6641 0.6641 0.6641
           Frequency  200.0  40.0  35.0  235.0    0.8333 0.8511 0.8421
               Route   98.0  13.0  18.0  116.0    0.8829 0.8448 0.8634
            Duration  195.0  57.0 101.0  296.0    0.7738 0.6588 0.7117
        Death_Entity   40.0   9.0   4.0   44.0    0.8163 0.9091 0.8602
          Metastasis  335.0  34.0  27.0  362.0    0.9079 0.9254 0.9166
          Site_Liver  146.0  64.0  28.0  174.0    0.6952 0.8391 0.7604
           Cancer_Dx  722.0  96.0 108.0  830.0    0.8826 0.8699 0.8762
               Grade   55.0  19.0  11.0   66.0    0.7432 0.8333 0.7857
                Date  403.0  16.0  14.0  417.0    0.9618 0.9664 0.9641
           Site_Lung  341.0 151.0  61.0  402.0    0.6931 0.8483 0.7629
          Site_Brain  184.0  82.0  22.0  206.0    0.6917 0.8932 0.7797
       Relative_Date  365.0 249.0  95.0  460.0    0.5945 0.7935 0.6797
      Race_Ethnicity   47.0   2.0   8.0   55.0    0.9592 0.8545 0.9038
              Gender 1260.0  15.0   2.0 1262.0    0.9882 0.9984 0.9933
              Dosage  425.0  76.0  60.0  485.0    0.8483 0.8763 0.8621
            Oncogene  178.0  89.0  57.0  235.0    0.6667 0.7574 0.7092
      Radiation_Dose   41.0   6.0  11.0   52.0    0.8723 0.7885 0.8283
               macro     -     -     -     -        -      -    0.7859
               micro     -     -     -     -        -      -    0.8130
```