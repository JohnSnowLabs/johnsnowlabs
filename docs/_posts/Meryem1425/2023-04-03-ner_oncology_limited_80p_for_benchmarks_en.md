---
layout: model
title: Detect Oncology-Specific Entities
author: John Snow Labs
name: ner_oncology_limited_80p_for_benchmarks
date: 2023-04-03
tags: [licensed, clinical, en, oncology, biomarker, treatment]
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

`Important Note:` This model is trained with a partial dataset that is used to train [ner_oncology](https://nlp.johnsnowlabs.com/2022/11/24/ner_oncology_en.html); and meant to be used for benchmarking run at [LLMs Healthcare Benchmarks](https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/tutorials/academic/LLMs_in_Healthcare).

This model extracts more than 40 oncology-related entities, including therapies, tests and staging.

Definitions of Predicted Entities:

`Adenopathy`: Mentions of pathological findings of the lymph nodes.
`Age`: All mention of ages, past or present, related to the patient or with anybody else.
`Biomarker`: Biological molecules that indicate the presence or absence of cancer, or the type of cancer. Oncogenes are excluded from this category.
`Biomarker_Result`: Terms or values that are identified as the result of a biomarkers.
`Cancer_Dx`: Mentions of cancer diagnoses (such as “breast cancer”) or pathological types that are usually used as synonyms for “cancer” (e.g. “carcinoma”). When anatomical references are present, they are included in the Cancer_Dx extraction.
`Cancer_Score`: Clinical or imaging scores that are specific for cancer settings (e.g. “BI-RADS” or “Allred score”).
`Cancer_Surgery`: Terms that indicate surgery as a form of cancer treatment.
`Chemotherapy`: Mentions of chemotherapy drugs, or unspecific words such as “chemotherapy”.
`Cycle_Coun`: The total number of cycles being administered of an oncological therapy (e.g. “5 cycles”).
`Cycle_Day`: References to the day of the cycle of oncological therapy (e.g. “day 5”).
`Cycle_Number`: The number of the cycle of an oncological therapy that is being applied (e.g. “third cycle”).
`Date`: Mentions of exact dates, in any format, including day number, month and/or year.
`Death_Entity`: Words that indicate the death of the patient or someone else (including family members), such as “died” or “passed away”.
`Direction`: Directional and laterality terms, such as “left”, “right”, “bilateral”, “upper” and “lower”.
`Dosage`: The quantity prescribed by the physician for an active ingredient.
`Duration`: Words indicating the duration of a treatment (e.g. “for 2 weeks”).
`Frequency`: Words indicating the frequency of treatment administration (e.g. “daily” or “bid”).
`Gender`: Gender-specific nouns and pronouns (including words such as “him” or “she”, and family members such as “father”).
`Grade`: All pathological grading of tumors (e.g. “grade 1”) or degrees of cellular differentiation (e.g. “well-differentiated”)
`Histological_Type`: Histological variants or cancer subtypes, such as “papillary”, “clear cell” or “medullary”.
`Hormonal_Therapy`: Mentions of hormonal drugs used to treat cancer, or unspecific words such as “hormonal therapy”.
`Imaging_Test`: Imaging tests mentioned in texts, such as “chest CT scan”.
`Immunotherapy`: Mentions of immunotherapy drugs, or unspecific words such as “immunotherapy”.
`Invasion`: Mentions that refer to tumor invasion, such as “invasion” or “involvement”. Metastases or lymph node involvement are excluded from this category.
`Line_Of_Therapy`: Explicit references to the line of therapy of an oncological therapy (e.g. “first-line treatment”).
`Metastasis`: Terms that indicate a metastatic disease. Anatomical references are not included in these extractions.
`Oncogene`: Mentions of genes that are implicated in the etiology of cancer.
`Pathology_Result`: The findings of a biopsy from the pathology report that is not covered by another entity (e.g. “malignant ductal cells”).
`Pathology_Test`: Mentions of biopsies or tests that use tissue samples.
`Performance_Status`: Mentions of performance status scores, such as ECOG and Karnofsky. The name of the score is extracted together with the result (e.g. “ECOG performance status of 4”).
`Race_Ethnicity`: The race and ethnicity categories include racial and national origin or sociocultural groups.
`Radiotherapy`: Terms that indicate the use of Radiotherapy.
`Response_To_Treatment`: Terms related to clinical progress of the patient related to cancer treatment, including “recurrence”, “bad response” or “improvement”.
`Relative_Date`: Temporal references that are relative to the date of the text or to any other specific date (e.g. “yesterday” or “three years later”).
`Route`: Words indicating the type of administration route (such as “PO” or “transdermal”).
`Site_Bone`: Anatomical terms that refer to the human skeleton.
`Site_Brain`: Anatomical terms that refer to the central nervous system (including the brain stem and the cerebellum).
`Site_Breast`: Anatomical terms that refer to the breasts.
`Site_Liver`: Anatomical terms that refer to the liver.
`Site_Lung`: Anatomical terms that refer to the lungs.
`Site_Lymph_Node`: Anatomical terms that refer to lymph nodes, excluding adenopathies.
`Site_Other_Body_Part`: Relevant anatomical terms that are not included in the rest of the anatomical entities.
`Smoking_Status`: All mentions of smoking related to the patient or to someone else.
`Staging`: Mentions of cancer stage such as “stage 2b” or “T2N1M0”. It also includes words such as “in situ”, “early-stage” or “advanced”.
`Targeted_Therapy`: Mentions of targeted therapy drugs, or unspecific words such as “targeted therapy”.
`Tumor_Finding`: All nonspecific terms that may be related to tumors, either malignant or benign (for example: “mass”, “tumor”, “lesion”, or “neoplasm”).
`Tumor_Size`: Size of the tumor, including numerical value and unit of measurement (e.g. “3 cm”).
`Unspecific_Therapy`: Terms that indicate a known cancer therapy but that is not specific to any other therapy entity (e.g. “chemoradiotherapy” or “adjuvant therapy”).

## Predicted Entities

`Histological_Type`, `Direction`, `Staging`, `Cancer_Score`, `Imaging_Test`, `Cycle_Number`, `Tumor_Finding`, `Site_Lymph_Node`, `Invasion`, `Response_To_Treatment`, `Smoking_Status`, `Tumor_Size`, `Cycle_Count`, `Adenopathy`, `Age`, `Biomarker_Result`, `Unspecific_Therapy`, `Site_Breast`, `Chemotherapy`, `Targeted_Therapy`, `Radiotherapy`, `Performance_Status`, `Pathology_Test`, `Site_Other_Body_Part`, `Cancer_Surgery`, `Line_Of_Therapy`, `Pathology_Result`, `Hormonal_Therapy`, `Site_Bone`, `Biomarker`, `Immunotherapy`, `Cycle_Day`, `Frequency`, `Route`, `Duration`, `Death_Entity`, `Metastasis`, `Site_Liver`, `Cancer_Dx`, `Grade`, `Date`, `Site_Lung`, `Site_Brain`, `Relative_Date`, `Race_Ethnicity`, `Gender`, `Oncogene`, `Dosage`, `Radiation_Dose`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_ONCOLOGY_CLINICAL/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/27.Oncology_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_oncology_limited_80p_for_benchmarks_en_4.3.2_3.0_1680548141397.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_oncology_limited_80p_for_benchmarks_en_4.3.2_3.0_1680548141397.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")                

ner = MedicalNerModel.pretrained("ner_oncology_limited_80p_for_benchmarks", "en", "clinical/models")\
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

val word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")                

val ner = MedicalNerModel.pretrained("ner_oncology_limited_80p_for_benchmarks", "en", "clinical/models")
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
|Model Name:|ner_oncology_limited_80p_for_benchmarks|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|15.3 MB|

## Benchmarking

```bash
               label     tp    fp    fn  total precision recall     f1
   Histological_Type  135.0  60.0  68.0  203.0    0.6923  0.665 0.6784
           Direction  642.0 170.0 149.0  791.0    0.7906 0.8116  0.801
             Staging  122.0  20.0  29.0  151.0    0.8592 0.8079 0.8328
        Cancer_Score   14.0   8.0   8.0   22.0    0.6364 0.6364 0.6364
        Imaging_Test  743.0 197.0 155.0  898.0    0.7904 0.8274 0.8085
        Cycle_Number   45.0  34.0  10.0   55.0    0.5696 0.8182 0.6716
       Tumor_Finding  948.0 104.0 110.0 1058.0    0.9011  0.896 0.8986
     Site_Lymph_Node  199.0  62.0  57.0  256.0    0.7625 0.7773 0.7698
            Invasion  116.0  33.0  20.0  136.0    0.7785 0.8529  0.814
Response_To_Treat...  244.0 145.0 144.0  388.0    0.6272 0.6289 0.6281
      Smoking_Status   54.0   7.0   2.0   56.0    0.8852 0.9643 0.9231
         Cycle_Count   96.0  26.0  32.0  128.0    0.7869   0.75  0.768
          Tumor_Size  205.0  43.0  49.0  254.0    0.8266 0.8071 0.8167
          Adenopathy   29.0   6.0   4.0   33.0    0.8286 0.8788 0.8529
                 Age  212.0  14.0  18.0  230.0    0.9381 0.9217 0.9298
    Biomarker_Result  593.0 138.0 122.0  715.0    0.8112 0.8294 0.8202
  Unspecific_Therapy  124.0  47.0  50.0  174.0    0.7251 0.7126 0.7188
         Site_Breast   96.0  13.0  14.0  110.0    0.8807 0.8727 0.8767
        Chemotherapy  570.0  40.0  65.0  635.0    0.9344 0.8976 0.9157
    Targeted_Therapy  173.0  11.0  17.0  190.0    0.9402 0.9105 0.9251
        Radiotherapy  128.0  26.0  21.0  149.0    0.8312 0.8591 0.8449
  Performance_Status   29.0  10.0  14.0   43.0    0.7436 0.6744 0.7073
      Pathology_Test  395.0 157.0 105.0  500.0    0.7156   0.79  0.751
Site_Other_Body_Part  682.0 284.0 370.0 1052.0     0.706 0.6483 0.6759
      Cancer_Surgery  388.0 100.0  75.0  463.0    0.7951  0.838  0.816
     Line_Of_Therapy   30.0   9.0   8.0   38.0    0.7692 0.7895 0.7792
    Pathology_Result  135.0 162.0 169.0  304.0    0.4545 0.4441 0.4493
    Hormonal_Therapy   95.0   9.0  10.0  105.0    0.9135 0.9048 0.9091
           Site_Bone  171.0  42.0  68.0  239.0    0.8028 0.7155 0.7566
       Immunotherapy   57.0  31.0  13.0   70.0    0.6477 0.8143 0.7215
           Biomarker  759.0 161.0 118.0  877.0     0.825 0.8655 0.8447
           Cycle_Day   84.0  32.0  32.0  116.0    0.7241 0.7241 0.7241
           Frequency  199.0  33.0  32.0  231.0    0.8578 0.8615 0.8596
               Route   88.0  12.0  23.0  111.0      0.88 0.7928 0.8341
            Duration  184.0  60.0 110.0  294.0    0.7541 0.6259  0.684
        Death_Entity   36.0   3.0   2.0   38.0    0.9231 0.9474 0.9351
          Metastasis  307.0  18.0  21.0  328.0    0.9446  0.936 0.9403
          Site_Liver  138.0  46.0  35.0  173.0      0.75 0.7977 0.7731
           Cancer_Dx  720.0 112.0 100.0  820.0    0.8654  0.878 0.8717
               Grade   48.0  21.0  13.0   61.0    0.6957 0.7869 0.7385
                Date  365.0  17.0  16.0  381.0    0.9555  0.958 0.9567
           Site_Lung  354.0 100.0  87.0  441.0    0.7797 0.8027 0.7911
          Site_Brain  133.0  28.0  59.0  192.0    0.8261 0.6927 0.7535
       Relative_Date  365.0 264.0  80.0  445.0    0.5803 0.8202 0.6797
      Race_Ethnicity   51.0  10.0   5.0   56.0    0.8361 0.9107 0.8718
              Gender 1267.0  15.0   3.0 1270.0    0.9883 0.9976 0.9929
              Dosage  337.0  45.0  78.0  415.0    0.8822  0.812 0.8457
            Oncogene  135.0  57.0  78.0  213.0    0.7031 0.6338 0.6667
      Radiation_Dose   35.0  10.0   6.0   41.0    0.7778 0.8537  0.814
               macro     -     -     -     -        -      -    0.7974
               micro     -     -     -     -        -      -    0.8154
```