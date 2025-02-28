---
layout: model
title: Detect Oncology-Specific Entities (German)
author: John Snow Labs
name: ner_oncology_wip
date: 2025-02-28
tags: [de, licensed]
task: Named Entity Recognition
language: de
edition: Healthcare NLP 5.5.2
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

- `Adenopathy`: Mentions of pathological findings of the lymph nodes.
- `Age`: All mention of ages, past or present, related to the patient or with anybody else.
- `Biomarker`: Biological molecules that indicate the presence or absence of cancer, or the type of cancer. Oncogenes are excluded from this category.
- `Biomarker_Result`: Terms or values that are identified as the result of a biomarkers.
- `Cancer_Dx`: Mentions of cancer diagnoses (such as "breast cancer") or pathological types that are usually used as synonyms for "cancer" (e.g. "carcinoma"). When anatomical references are present, they are included in the Cancer_Dx extraction.
- `Cancer_Score`: Clinical or imaging scores that are specific for cancer settings (e.g. "BI-RADS" or "Allred score").
- `Cancer_Surgery`: Terms that indicate surgery as a form of cancer treatment.
- `Chemotherapy`: Mentions of chemotherapy drugs, or unspecific words such as "chemotherapy".
- `Cycle_Coun`: The total number of cycles being administered of an oncological therapy (e.g. "5 cycles"). 
- `Cycle_Day`: References to the day of the cycle of oncological therapy (e.g. "day 5").
- `Cycle_Number`: The number of the cycle of an oncological therapy that is being applied (e.g. "third cycle").
- `Date`: Mentions of exact dates, in any format, including day number, month and/or year.
- `Death_Entity`: Words that indicate the death of the patient or someone else (including family members), such as "died" or "passed away".
- `Direction`: Directional and laterality terms, such as "left", "right", "bilateral", "upper" and "lower".
- `Dosage`: The quantity prescribed by the physician for an active ingredient.
- `Duration`: Words indicating the duration of a treatment (e.g. "for 2 weeks").
- `Frequency`: Words indicating the frequency of treatment administration (e.g. "daily" or "bid").
- `Gender`: Gender-specific nouns and pronouns (including words such as "him" or "she", and family members such as "father").
- `Grade`: All pathological grading of tumors (e.g. "grade 1") or degrees of cellular differentiation (e.g. "well-differentiated")
- `Histological_Type`: Histological variants or cancer subtypes, such as "papillary", "clear cell" or "medullary". 
- `Hormonal_Therapy`: Mentions of hormonal drugs used to treat cancer, or unspecific words such as "hormonal therapy".
- `Imaging_Test`: Imaging tests mentioned in texts, such as "chest CT scan".
- `Immunotherapy`: Mentions of immunotherapy drugs, or unspecific words such as "immunotherapy".
- `Invasion`: Mentions that refer to tumor invasion, such as "invasion" or "involvement". Metastases or lymph node involvement are excluded from this category.
- `Line_Of_Therapy`: Explicit references to the line of therapy of an oncological therapy (e.g. "first-line treatment").
- `Metastasis`: Terms that indicate a metastatic disease. Anatomical references are not included in these extractions.
- `Oncogene`: Mentions of genes that are implicated in the etiology of cancer.
- `Pathology_Result`: The findings of a biopsy from the pathology report that is not covered by another entity (e.g. "malignant ductal cells").
- `Pathology_Test`: Mentions of biopsies or tests that use tissue samples.
- `Performance_Status`: Mentions of performance status scores, such as ECOG and Karnofsky. The name of the score is extracted together with the result (e.g. "ECOG performance status of 4").
- `Race_Ethnicity`: The race and ethnicity categories include racial and national origin or sociocultural groups.
- `Radiotherapy`: Terms that indicate the use of Radiotherapy.
- `Response_To_Treatment`: Terms related to clinical progress of the patient related to cancer treatment, including "recurrence", "bad response" or "improvement".
- `Relative_Date`: Temporal references that are relative to the date of the text or to any other specific date (e.g. "yesterday" or "three years later").
- `Route`: Words indicating the type of administration route (such as "PO" or "transdermal").
- `Site_Bone`: Anatomical terms that refer to the human skeleton.
- `Site_Brain`: Anatomical terms that refer to the central nervous system (including the brain stem and the cerebellum).
- `Site_Breast`: Anatomical terms that refer to the breasts.
- `Site_Liver`: Anatomical terms that refer to the liver.
- `Site_Lung`: Anatomical terms that refer to the lungs.
- `Site_Lymph_Node`: Anatomical terms that refer to lymph nodes, excluding adenopathies.
- `Site_Other_Body_Part`: Relevant anatomical terms that are not included in the rest of the anatomical entities.
- `Smoking_Status`: All mentions of smoking related to the patient or to someone else.
- `Staging`: Mentions of cancer stage such as "stage 2b" or "T2N1M0". It also includes words such as "in situ", "early-stage" or "advanced".
- `Targeted_Therapy`: Mentions of targeted therapy drugs, or unspecific words such as "targeted therapy".
- `Tumor_Finding`: All nonspecific terms that may be related to tumors, either malignant or benign (for example: "mass", "tumor", "lesion", or "neoplasm").
- `Tumor_Size`: Size of the tumor, including numerical value and unit of measurement (e.g. "3 cm").
- `Unspecific_Therapy`: Terms that indicate a known cancer therapy but that is not specific to any other therapy entity (e.g. "chemoradiotherapy" or "adjuvant therapy").

## Predicted Entities

`Histological_Type`, `Direction`, `Staging`, `Cancer_Score`, `Imaging_Test`, `Cycle_Number`, `Tumor_Finding`, `Site_Lymph_Node`, `Invasion`, `Response_To_Treatment`, `Smoking_Status`, `Tumor_Size`, `Cycle_Count`, `Adenopathy`, `Age`, `Biomarker_Result`, `Unspecific_Therapy`, `Site_Breast`, `Chemotherapy`, `Targeted_Therapy`, `Radiotherapy`, `Performance_Status`, `Pathology_Test`, `Site_Other_Body_Part`, `Cancer_Surgery`, `Line_Of_Therapy`, `Pathology_Result`, `Hormonal_Therapy`, `Site_Bone`, `Biomarker`, `Immunotherapy`, `Cycle_Day`, `Frequency`, `Route`, `Duration`, `Death_Entity`, `Metastasis`, `Site_Liver`, `Cancer_Dx`, `Grade`, `Date`, `Site_Lung`, `Site_Brain`, `Relative_Date`, `Race_Ethnicity`, `Gender`, `Oncogene`, `Dosage`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_oncology_wip_de_5.5.2_3.0_1740779155357.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_oncology_wip_de_5.5.2_3.0_1740779155357.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx") \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d", "de", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_oncology_wip", "de", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

nlpPipeline = Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter])


data = spark.createDataFrame([["""Patient: 67-jährige weibliche Patientin
Diagnose: Invasives duktales Karzinom der linken Brust
Klinische Präsentation:
Die Patientin stellte sich mit einer schmerzlosen, palpablen Verhärtung im oberen äußeren Quadranten der linken Brust vor. Zudem berichtete sie über eine leichte Rötung der Haut sowie eine eingezogene Mamille. Axilläre Lymphknoten waren bei der klinischen Untersuchung tastbar vergrößert.

Histopathologie:
Die Biopsie ergab ein invasives duktales Karzinom (G3) mit positiven Hormonrezeptoren (ER+, PR+). HER2/neu-Expression war negativ. Der Ki-67-Proliferationsindex lag bei 35 %.

Bildgebung:

Mammographie: 2,8 cm große suspekte Läsion in der linken Brust mit Mikroverkalkungen
MRT: Tumorausdehnung 3,1 cm mit Infiltration des Drüsengewebes
PET-CT: Kein Anhalt für Fernmetastasen
Therapieempfehlung:

Neoadjuvante Chemotherapie (EC-T Schema)
Anschließend brusterhaltende Operation mit Sentinel-Lymphknotenbiopsie
Adjuvante Strahlentherapie
Hormontherapie mit Letrozol für 5 Jahre
Beurteilung:
Fortgeschrittenes, aber lokalisierbares Mammakarzinom mit günstigem Hormonrezeptorstatus. Therapie gemäß interdisziplinärer Tumorkonferenz empfohlen."""]]).toDF("text")


result = nlpPipeline.fit(data).transform(data)

```

{:.jsl-block}
```python
documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx") \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = nlp.WordEmbeddingsModel.pretrained("w2v_cc_300d", "de", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = medical.NerModel.pretrained("ner_oncology_wip", "de", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

nlpPipeline = nlp.Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter])


data = spark.createDataFrame([["""Patient: 67-jährige weibliche Patientin
Diagnose: Invasives duktales Karzinom der linken Brust
Klinische Präsentation:
Die Patientin stellte sich mit einer schmerzlosen, palpablen Verhärtung im oberen äußeren Quadranten der linken Brust vor. Zudem berichtete sie über eine leichte Rötung der Haut sowie eine eingezogene Mamille. Axilläre Lymphknoten waren bei der klinischen Untersuchung tastbar vergrößert.

Histopathologie:
Die Biopsie ergab ein invasives duktales Karzinom (G3) mit positiven Hormonrezeptoren (ER+, PR+). HER2/neu-Expression war negativ. Der Ki-67-Proliferationsindex lag bei 35 %.

Bildgebung:

Mammographie: 2,8 cm große suspekte Läsion in der linken Brust mit Mikroverkalkungen
MRT: Tumorausdehnung 3,1 cm mit Infiltration des Drüsengewebes
PET-CT: Kein Anhalt für Fernmetastasen
Therapieempfehlung:

Neoadjuvante Chemotherapie (EC-T Schema)
Anschließend brusterhaltende Operation mit Sentinel-Lymphknotenbiopsie
Adjuvante Strahlentherapie
Hormontherapie mit Letrozol für 5 Jahre
Beurteilung:
Fortgeschrittenes, aber lokalisierbares Mammakarzinom mit günstigem Hormonrezeptorstatus. Therapie gemäß interdisziplinärer Tumorkonferenz empfohlen."""]]).toDF("text")


result = nlpPipeline.fit(data).transform(data)

```
```scala
val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
    
val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")
    
val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")
    
val embeddings = WordEmbeddingsModel().pretrained("w2v_cc_300d", "de", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")                
    
val ner = MedicalNerModel.pretrained("ner_oncology_wip", "de", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")
    
val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter))    

val data = Seq("""Patient: 67-jährige weibliche Patientin
Diagnose: Invasives duktales Karzinom der linken Brust
Klinische Präsentation:
Die Patientin stellte sich mit einer schmerzlosen, palpablen Verhärtung im oberen äußeren Quadranten der linken Brust vor. Zudem berichtete sie über eine leichte Rötung der Haut sowie eine eingezogene Mamille. Axilläre Lymphknoten waren bei der klinischen Untersuchung tastbar vergrößert.

Histopathologie:
Die Biopsie ergab ein invasives duktales Karzinom (G3) mit positiven Hormonrezeptoren (ER+, PR+). HER2/neu-Expression war negativ. Der Ki-67-Proliferationsindex lag bei 35 %.

Bildgebung:

Mammographie: 2,8 cm große suspekte Läsion in der linken Brust mit Mikroverkalkungen
MRT: Tumorausdehnung 3,1 cm mit Infiltration des Drüsengewebes
PET-CT: Kein Anhalt für Fernmetastasen
Therapieempfehlung:

Neoadjuvante Chemotherapie (EC-T Schema)
Anschließend brusterhaltende Operation mit Sentinel-Lymphknotenbiopsie
Adjuvante Strahlentherapie
Hormontherapie mit Letrozol für 5 Jahre
Beurteilung:
Fortgeschrittenes, aber lokalisierbares Mammakarzinom mit günstigem Hormonrezeptorstatus. Therapie gemäß interdisziplinärer Tumorkonferenz empfohlen.""").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+------------------------------+-----+----+--------------------+
|chunk                         |begin|end |ner_label           |
+------------------------------+-----+----+--------------------+
|67-jährige                    |9    |18  |Age                 |
|weibliche                     |20   |28  |Gender              |
|Invasives                     |50   |58  |Histological_Type   |
|duktales                      |60   |67  |Histological_Type   |
|Karzinom der linken Brust     |69   |93  |Cancer_Dx           |
|oberen äußeren Quadranten     |194  |218 |Direction           |
|linken                        |224  |229 |Direction           |
|Brust                         |231  |235 |Site_Breast         |
|sie                           |259  |261 |Gender              |
|Haut                          |292  |295 |Site_Other_Body_Part|
|Axilläre Lymphknoten          |329  |348 |Site_Lymph_Node     |
|Histopathologie               |409  |423 |Pathology_Test      |
|Biopsie                       |430  |436 |Pathology_Test      |
|invasives                     |448  |456 |Histological_Type   |
|duktales                      |458  |465 |Histological_Type   |
|Karzinom                      |467  |474 |Cancer_Dx           |
|positiven                     |485  |493 |Biomarker_Result    |
|Hormonrezeptoren              |495  |510 |Biomarker           |
|HER2/neu-Expression           |524  |542 |Oncogene            |
|negativ                       |548  |554 |Biomarker_Result    |
|Ki-67-Proliferationsindex     |561  |585 |Biomarker           |
|35 %                          |595  |598 |Biomarker_Result    |
|Bildgebung                    |602  |611 |Imaging_Test        |
|Mammographie                  |615  |626 |Imaging_Test        |
|2,8 cm                        |629  |634 |Tumor_Size          |
|Läsion                        |651  |656 |Tumor_Finding       |
|linken                        |665  |670 |Direction           |
|Brust                         |672  |676 |Site_Breast         |
|MRT                           |700  |702 |Imaging_Test        |
|Tumorausdehnung               |705  |719 |Tumor_Finding       |
|3,1 cm                        |721  |726 |Tumor_Size          |
|Infiltration                  |732  |743 |Invasion            |
|Drüsengewebes                 |749  |761 |Site_Other_Body_Part|
|PET-CT                        |763  |768 |Imaging_Test        |
|Neoadjuvante Chemotherapie    |823  |848 |Chemotherapy        |
|brusterhaltende Operation     |877  |901 |Cancer_Surgery      |
|Sentinel-Lymphknotenbiopsie   |907  |933 |Pathology_Test      |
|Adjuvante Strahlentherapie    |935  |960 |Radiotherapy        |
|Hormontherapie                |962  |975 |Hormonal_Therapy    |
|Letrozol                      |981  |988 |Hormonal_Therapy    |
|für 5 Jahre                   |990  |1000|Duration            |
|lokalisierbares               |1039 |1053|Histological_Type   |
|Mammakarzinom                 |1055 |1067|Cancer_Dx           |
|günstigem Hormonrezeptorstatus|1073 |1102|Biomarker_Result    |
+------------------------------+-----+----+--------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_oncology_wip|
|Compatibility:|Healthcare NLP 5.5.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|de|
|Size:|3.1 MB|

## Benchmarking

```bash
                label    precision  recall      f1  support
    Histological_Type       0.7533   0.689  0.7197    164.0
            Direction       0.8469  0.8758  0.8611    499.0
              Staging       0.9006  0.9063  0.9034    160.0
         Cancer_Score       0.9828  0.8636  0.9194     66.0
         Imaging_Test       0.8284  0.8273  0.8278    741.0
         Cycle_Number         0.95  0.6552  0.7755     58.0
        Tumor_Finding       0.9024  0.8898   0.896    644.0
      Site_Lymph_Node       0.8235  0.8434  0.8333    166.0
             Invasion          0.8  0.7027  0.7482     74.0
Response_To_Treatment       0.6931  0.6231  0.6563    337.0
       Smoking_Status       0.8125  0.6842  0.7429     19.0
           Tumor_Size       0.8991  0.9159  0.9074    535.0
          Cycle_Count        0.701  0.9408  0.8034    152.0
           Adenopathy       0.8919  0.7674   0.825     43.0
                  Age       0.9086  0.9747  0.9405    316.0
     Biomarker_Result        0.852  0.7795  0.8141    635.0
   Unspecific_Therapy       0.6707  0.5556  0.6077     99.0
          Site_Breast       0.8875  0.8161  0.8503     87.0
         Chemotherapy       0.8897  0.9089  0.8992    417.0
     Targeted_Therapy       0.8247  0.8247  0.8247     97.0
         Radiotherapy       0.8837  0.8172  0.8492     93.0
   Performance_Status       0.9302  0.8511  0.8889     47.0
       Pathology_Test       0.7832  0.7592   0.771    490.0  
 Site_Other_Body_Part       0.6967  0.7168  0.7066    625.0  
       Cancer_Surgery       0.8631  0.8536  0.8583    362.0  
      Line_Of_Therapy         0.84     0.7  0.7636     30.0  
     Pathology_Result        0.625  0.6436  0.6341    505.0  
     Hormonal_Therapy       0.8679  0.7541   0.807     61.0  
            Site_Bone       0.7273  0.7339  0.7306    109.0  
            Biomarker       0.8056  0.8781  0.8403    689.0  
        Immunotherapy       0.9524  0.4545  0.6154     44.0  
            Cycle_Day       0.6744  0.8467  0.7508    137.0  
                Route       0.8667  0.8864  0.8764     44.0  
            Frequency       0.9278  0.8564  0.8907    195.0  
             Duration       0.7583  0.6223  0.6836    368.0  
         Death_Entity       0.9231  0.4615  0.6154     26.0
           Metastasis       0.9042  0.7438  0.8162    203.0
           Site_Liver       0.8675  0.8182  0.8421     88.0
            Cancer_Dx       0.9025  0.8597  0.8806    549.0
                Grade       0.8015  0.8015  0.8015    136.0
                 Date       0.9767   0.973  0.9749    518.0
            Site_Lung       0.8483  0.8027  0.8249    223.0
           Site_Brain       0.8286  0.5686  0.6744    102.0
        Relative_Date       0.7418  0.8146  0.7765    642.0
       Race_Ethnicity       0.8621  0.8333  0.8475     30.0
               Gender       0.8953  0.9265  0.9106    517.0
               Dosage       0.8859  0.8787  0.8823    371.0
             Oncogene        0.785  0.7904  0.7877    291.0
       Radiation_Dose       0.9273  0.9107  0.9189     56.0  
            macro-avg         -         -   0.8077       -
            micro-avg         -         -   0.8218       -
```