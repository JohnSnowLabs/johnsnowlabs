---
layout: model
title: ICD10CM HCC CMS 2024 MidYear Resolver
author: John Snow Labs
name: mpnetresolve_icd10_cms_hcc_2024_midyear
date: 2024-07-27
tags: [licensed, en, entity_resolution, hcc]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.3.3
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical concepts to ICD10CM codes and their corresponding HCC categories.
Note: This model only supports ICD10CM codes that have valid HCC categories according to 2024 CMS HCC MidYear mappings.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/mpnetresolve_icd10_cms_hcc_2024_midyear_en_5.3.3_3.4_1722106166369.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/mpnetresolve_icd10_cms_hcc_2024_midyear_en_5.3.3_3.4_1722106166369.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = (
    DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
)

sentenceDetector = (
    SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models") 
    .setInputCols(["document"])
    .setOutputCol("sentence")#.setCustomBounds(['\|'])
)
    
tokenizer = Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")#\
        
clinical_embeddings = WordEmbeddingsModel.pretrained('embeddings_clinical', "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel().pretrained('ner_clinical', 'en', 'clinical/models')\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_conv = NerConverterInternal().setInputCols(['sentence', 'ner', 'token']).setOutputCol('ner_chunk')\
    .setWhiteList(['PROBLEM', 'TREATMENT'])

clinical_assertion = AssertionDLModel.pretrained("assertion_dl_large", "en", "clinical/models") \
    .setInputCols(["sentence", "ner_chunk", "embeddings"]) \
    .setOutputCol("assertion")

assertion_filterer = AssertionFilterer()\
    .setInputCols("sentence","ner_chunk","assertion")\
    .setOutputCol("assertion_filtered")\
    .setCaseSensitive(False)\
    .setWhiteList(["Present"])

c2doc = Chunk2Doc()\
    .setInputCols("assertion_filtered")\
    .setOutputCol("ner_chunk_doc")

schunk_embeddings = MPNetEmbeddings.pretrained("all_mpnet_base_v2","en") \
            .setInputCols(["ner_chunk_doc"]) \
            .setOutputCol("mpnet_embeddings")

icd10_resolver = SentenceEntityResolverModel.pretrained("mpnetresolve_icd10_cms_hcc_2024_midyear", "en", "clinical/models") \
    .setInputCols(["mpnet_embeddings"]) \
    .setOutputCol("icd10cm_code")\
    .setDistanceFunction("COSINE")


jsl_single_pipeline = Pipeline(
    stages=[
        documentAssembler,
        sentenceDetector,
        tokenizer,
        clinical_embeddings,
        ner_model,
        ner_conv,
        clinical_assertion,
        assertion_filterer,
        c2doc, schunk_embeddings, icd10_resolver
    ]
)

data_ner = spark.createDataFrame([[""]]).toDF("text")
p_model = jsl_single_pipeline.fit(data_ner)
l_model = LightPipeline(p_model)

text = """A 36-year-old patient with no significant medical history presented with acute deep venous thrombosis in the right lower extremity and bilateral pulmonary embolism. The patient was on intravenous heparin, complicated by acute renal failure. The patient, who works as a sales representative involving extensive travel, experienced acute dyspnea and syncope. Further investigations revealed a nonocclusive right popliteal artery thrombosis, multiple pulmonary emboli, and a possible renal infarct. With no family history of hypercoagulable conditions, the patient denies recent injury or calf symptoms. Medical and surgical history is unremarkable. The physical exam shows a robust individual with no evident signs of clotting, and laboratory findings indicate leukocytosis, possibly a reactive response."""

res = l_model.fullAnnotate([text])[0]

res_df = []
for chunk in res['icd10cm_code']:
    res_df.append({'chunk': chunk.metadata['target_text'],
                   'icd10_code': chunk.result,
                   'icd10_desc': chunk.metadata['resolved_text'],
                   'confidence': 1-float(chunk.metadata['all_k_cosine_distances'].split(':::')[0]),
                   'hcc_details': chunk.metadata['all_k_aux_labels'].split(':::')[0]})

res_df = pd.DataFrame(res_df)
res_df[res_df['confidence'] > 0.80] ## selecting codes with high confidence
```

</div>

## Results

```bash
| chunk                                                     | icd10_code   | icd10_desc                                                                      |   confidence | hcc_details                                                                                              |
|:----------------------------------------------------------|:-------------|:--------------------------------------------------------------------------------|-------------:|:---------------------------------------------------------------------------------------------------------|
| acute deep venous thrombosis in the right lower extremity | I82402       | Acute embolism and thrombosis of unspecified deep veins of left lower extremity |       0.8804 | version:v22,cat:108.0,billable:Yes|version:v24,cat:108.0,billable:Yes|version:v28,cat:267.0,billable:Yes |
| bilateral pulmonary embolism                              | I2699        | Other pulmonary embolism without acute cor pulmonale                            |       0.8343 | version:v22,cat:107.0,billable:Yes|version:v24,cat:107.0,billable:Yes|version:v28,cat:267.0,billable:Yes |
| acute renal failure                                       | N179         | Acute kidney failure, unspecified                                               |       0.9626 | version:v22,cat:135.0,billable:Yes|version:v24,cat:135.0,billable:Yes|version:v28,cat:N/A,billable:No    |
| a nonocclusive right popliteal artery thrombosis          | I82432       | Acute embolism and thrombosis of left popliteal vein                            |       0.9432 | version:v22,cat:108.0,billable:Yes|version:v24,cat:108.0,billable:Yes|version:v28,cat:267.0,billable:Yes |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|mpnetresolve_icd10_cms_hcc_2024_midyear|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[mpnet_embeddings]|
|Output Labels:|[icd_code]|
|Language:|en|
|Size:|97.6 MB|
|Case sensitive:|false|

## References

2024 CMS HCC MidYear Mappings, and ICD10CM JSL augmented data.