---
layout: model
title: Detect Oncology-Specific Entities (clinical_large)
author: John Snow Labs
name: ner_oncology_emb_clinical_large
date: 2023-04-12
tags: [licensed, clinical, en, oncology, biomarker, treatment, ner, clinical_large]
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_oncology_emb_clinical_large_en_4.3.2_3.0_1681316109615.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_oncology_emb_clinical_large_en_4.3.2_3.0_1681316109615.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical_large","en","clinical/models")\
        .setInputCols(["sentence","token"])\
        .setOutputCol("word_embeddings")    

ner = MedicalNerModel.pretrained("ner_oncology_emb_clinical_large", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[document_assembler,
                            sentence_detector,
                            tokenizer,
                            embeddings,
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

val embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical_large","en","clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("word_embeddings")                

val ner = MedicalNerModel.pretrained("ner_oncology_emb_clinical_large", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "word_embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(document_assembler,
                            sentence_detector,
                            tokenizer,
                            embeddings,
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
+------------------------------+-----+---+---------------------+
|chunk                         |begin|end|ner_label            |
+------------------------------+-----+---+---------------------+
|left                          |31   |34 |Direction            |
|mastectomy                    |36   |45 |Cancer_Surgery       |
|axillary lymph node dissection|54   |83 |Cancer_Surgery       |
|left                          |91   |94 |Direction            |
|breast cancer                 |96   |108|Cancer_Dx            |
|twenty years ago              |110  |125|Relative_Date        |
|tumor                         |132  |136|Tumor_Finding        |
|positive                      |142  |149|Biomarker_Result     |
|ER                            |155  |156|Biomarker            |
|PR                            |162  |163|Biomarker            |
|radiotherapy                  |183  |194|Radiotherapy         |
|breast                        |229  |234|Site_Breast          |
|cancer                        |241  |246|Cancer_Dx            |
|recurred                      |248  |255|Response_To_Treatment|
|right                         |262  |266|Direction            |
|lung                          |268  |271|Site_Lung            |
|metastasis                    |273  |282|Metastasis           |
|13 years later                |284  |297|Relative_Date        |
|adriamycin                    |346  |355|Chemotherapy         |
|60 mg/m2                      |358  |365|Dosage               |
|cyclophosphamide              |372  |387|Chemotherapy         |
|600 mg/m2                     |390  |398|Dosage               |
|six courses                   |406  |416|Cycle_Count          |
|first line                    |422  |431|Line_Of_Therapy      |
+------------------------------+-----+---+---------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_oncology_emb_clinical_large|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, word_embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|15.3 MB|

## Benchmarking

```bash
               label     tp    fp    fn  total precision recall     f1
   Histological_Type  141.0  40.0  70.0  211.0     0.779 0.6682 0.7194
           Direction  672.0 150.0 159.0  831.0    0.8175 0.8087 0.8131
             Staging  102.0  27.0  36.0  138.0    0.7907 0.7391  0.764
        Cancer_Score   10.0   2.0  11.0   21.0    0.8333 0.4762 0.6061
        Imaging_Test  754.0 147.0 146.0  900.0    0.8368 0.8378 0.8373
        Cycle_Number   48.0  43.0  12.0   60.0    0.5275    0.8 0.6358
       Tumor_Finding  970.0  89.0 109.0 1079.0     0.916  0.899 0.9074
     Site_Lymph_Node  210.0  68.0  61.0  271.0    0.7554 0.7749  0.765
            Invasion  146.0  39.0  21.0  167.0    0.7892 0.8743 0.8295
Response_To_Treat...  280.0 146.0  90.0  370.0    0.6573 0.7568 0.7035
      Smoking_Status   42.0  11.0   6.0   48.0    0.7925  0.875 0.8317
         Cycle_Count  104.0  23.0  40.0  144.0    0.8189 0.7222 0.7675
          Tumor_Size  197.0  37.0  41.0  238.0    0.8419 0.8277 0.8347
          Adenopathy   30.0  13.0  13.0   43.0    0.6977 0.6977 0.6977
                 Age  205.0  15.0  23.0  228.0    0.9318 0.8991 0.9152
    Biomarker_Result  564.0 160.0 121.0  685.0     0.779 0.8234 0.8006
  Unspecific_Therapy  108.0  30.0  66.0  174.0    0.7826 0.6207 0.6923
         Site_Breast   92.0  18.0  18.0  110.0    0.8364 0.8364 0.8364
        Chemotherapy  687.0  59.0  55.0  742.0    0.9209 0.9259 0.9234
    Targeted_Therapy  178.0  29.0  28.0  206.0    0.8599 0.8641  0.862
        Radiotherapy  143.0  22.0  18.0  161.0    0.8667 0.8882 0.8773
  Performance_Status   17.0  15.0  15.0   32.0    0.5313 0.5313 0.5313
      Pathology_Test  387.0 197.0  99.0  486.0    0.6627 0.7963 0.7234
Site_Other_Body_Part  678.0 287.0 460.0 1138.0    0.7026 0.5958 0.6448
      Cancer_Surgery  398.0  82.0  95.0  493.0    0.8292 0.8073 0.8181
     Line_Of_Therapy   38.0   9.0  10.0   48.0    0.8085 0.7917    0.8
    Pathology_Result  180.0 206.0 161.0  341.0    0.4663 0.5279 0.4952
    Hormonal_Therapy   98.0  12.0  25.0  123.0    0.8909 0.7967 0.8412
           Site_Bone  172.0  43.0  51.0  223.0       0.8 0.7713 0.7854
           Biomarker  693.0 144.0 138.0  831.0     0.828 0.8339 0.8309
       Immunotherapy   66.0  17.0  16.0   82.0    0.7952 0.8049    0.8
           Cycle_Day   85.0  44.0  43.0  128.0    0.6589 0.6641 0.6615
           Frequency  199.0  37.0  36.0  235.0    0.8432 0.8468  0.845
               Route   91.0  10.0  25.0  116.0     0.901 0.7845 0.8387
            Duration  179.0  57.0 117.0  296.0    0.7585 0.6047 0.6729
        Death_Entity   40.0  10.0   4.0   44.0       0.8 0.9091 0.8511
          Metastasis  337.0  27.0  25.0  362.0    0.9258 0.9309 0.9284
          Site_Liver  149.0  56.0  25.0  174.0    0.7268 0.8563 0.7863
           Cancer_Dx  723.0 114.0 107.0  830.0    0.8638 0.8711 0.8674
               Grade   47.0  21.0  19.0   66.0    0.6912 0.7121 0.7015
                Date  403.0  15.0  14.0  417.0    0.9641 0.9664 0.9653
           Site_Lung  338.0 134.0  64.0  402.0    0.7161 0.8408 0.7735
          Site_Brain  165.0  53.0  41.0  206.0    0.7569  0.801 0.7783
       Relative_Date  376.0 271.0  84.0  460.0    0.5811 0.8174 0.6793
      Race_Ethnicity   42.0   0.0  13.0   55.0       1.0 0.7636  0.866
              Gender 1255.0  17.0   7.0 1262.0    0.9866 0.9945 0.9905
              Dosage  417.0  53.0  68.0  485.0    0.8872 0.8598 0.8733
            Oncogene  178.0  83.0  57.0  235.0     0.682 0.7574 0.7177
      Radiation_Dose   41.0   4.0  11.0   52.0    0.9111 0.7885 0.8454
               macro     -     -     -     -        -      -    0.7863
               micro     -     -     -     -        -      -    0.8145
```