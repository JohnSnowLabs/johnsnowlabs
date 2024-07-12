---
layout: model
title: Relation Extraction between different oncological entity types using granular classes (ReDL)
author: John Snow Labs
name: redl_oncology_granular_biobert
date: 2024-07-03
tags: [licensed, en, clinical, oncology, relation_extraction, temporal, test, biomarker, anatomy, tensorflow]
task: Relation Extraction
language: en
edition: Healthcare NLP 5.4.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: RelationExtractionDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Using this relation extraction model, four relation types can be identified: `is_date_of` (between date entities and other clinical entities), `is_size_of` (between `Tumor_Finding` and `Tumor_Size`), `is_location_of` (between anatomical entities and other entities) and `is_finding_of` (between test entities and their results).

## Predicted Entities

`is_date_of`, `is_size_of`, `is_location_of`, `is_finding_of`, `O`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/redl_oncology_granular_biobert_en_5.4.0_3.0_1720038256440.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/redl_oncology_granular_biobert_en_5.4.0_3.0_1720038256440.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel.pretrained("ner_oncology_wip", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")

pos_tagger = PerceptronModel.pretrained("pos_clinical", "en", "clinical/models") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("pos_tags")

dependency_parser = DependencyParserModel.pretrained("dependency_conllu", "en") \
    .setInputCols(["sentence", "pos_tags", "token"]) \
    .setOutputCol("dependencies")

re_ner_chunk_filter = RENerChunksFilter()\
    .setInputCols(["ner_chunk", "dependencies"])\
    .setOutputCol("re_ner_chunk")\
    .setMaxSyntacticDistance(10)\
    .setRelationPairs(['Date-Cancer_Dx',
                       'Tumor_Finding-Site_Breast',
                       'Tumor_Finding-Site_Bone',
                       'Tumor_Finding-Site_Liver',
                       'Tumor_Finding-Site_Lung',
                       'Tumor_Finding-Site_Lymph_Node',
                       'Tumor_Finding-Site_Other_Body_Part',
                       'Tumor_Fiding-Relative_Date',
                       'Tumor_Finding-Tumor_Size',
                       'Biomarker-Biomarker_Result',
                       'Pathology_Test-Cancer_Dx',
                       'Biomarker_Result-Biomarker',
                       'Imaging_Test-Tumor_Finding',
                       'Pathology_Test-Relative_Date',
                       'Pathology_Test-Pathology_Result',
                       'Relative_Date-Metastasis',
                       'Site-Lung-Metastasis',
                       'Tumor_Finding-Tumor_Size'
                       ])

re_model = RelationExtractionDLModel.pretrained("redl_oncology_granular_biobert", "en", "clinical/models")\
    .setInputCols(["re_ner_chunk", "sentence"])\
    .setOutputCol("relation_extraction")

pipeline = Pipeline(stages=[document_assembler,
                            sentence_detector,
                            tokenizer,
                            word_embeddings,
                            ner,
                            ner_converter,
                            pos_tagger,
                            dependency_parser,
                            re_ner_chunk_filter,
                            re_model])

data = spark.createDataFrame([["The Patient underwent a computed tomography scan, which showed a complex ovarian mass, 2 cm insize . A Pap smear performed one month later was positive for atypical glandular cells suspicious for adenocarcinoma. The pathologic specimen showed extension of the tumor throughout the fallopian tubes, appendix, omentum, and 5 out of 5 enlarged lymph nodes."]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala

val document_assembler = new DocumentAssembler()
	.setInputCol("text")
	.setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
	.setInputCols(Array("document"))
	.setOutputCol("sentence")

val tokenizer = new Tokenizer()
	.setInputCols(Array("sentence"))
	.setOutputCol("token")

val word_embeddings = WordEmbeddingsModel
	.pretrained("embeddings_clinical","en","clinical/models")
	.setInputCols(Array("sentence","token"))
	.setOutputCol("embeddings")

val ner = MedicalNerModel.pretrained("ner_oncology_wip","en","clinical/models")
	.setInputCols(Array("sentence","token","embeddings"))
	.setOutputCol("ner")

val ner_converter = new NerConverter()
	.setInputCols(Array("sentence","token","ner"))
	.setOutputCol("ner_chunk")

val pos_tagger = PerceptronModel.pretrained("pos_clinical","en","clinical/models")
	.setInputCols(Array("sentence","token"))
	.setOutputCol("pos_tags")

val dependency_parser = DependencyParserModel.pretrained("dependency_conllu","en")
	.setInputCols(Array("sentence","pos_tags","token"))
	.setOutputCol("dependencies")

val re_ner_chunk_filter = new RENerChunksFilter()
	.setInputCols(Array("ner_chunk","dependencies"))
	.setOutputCol("re_ner_chunk")
	.setMaxSyntacticDistance(10)
	.setRelationPairs(Array(
     "Date-Cancer_Dx",
     "Tumor_Finding-Site_Breast",
     "Tumor_Finding-Site_Bone",
     "Tumor_Finding-Site_Liver",
     "Tumor_Finding-Site_Lung",
     "Tumor_Finding-Site_Lymph_Node",
     "Tumor_Finding-Site_Other_Body_Part",
     "Tumor_Fiding-Relative_Date",
     "Tumor_Finding-Tumor_Size",
     "Biomarker-Biomarker_Result",
     "Pathology_Test-Cancer_Dx",
     "Biomarker_Result-Biomarker",
     "Imaging_Test-Tumor_Finding",
     "Pathology_Test-Relative_Date",
     "Pathology_Test-Pathology_Result",
     "Relative_Date-Metastasis",
     "Site-Lung-Metastasis",
     "Tumor_Finding-Tumor_Size" ))

val re_model = RelationExtractionDLModel.pretrained("redl_oncology_granular_biobert","en","clinical/models")
	.setInputCols(Array("re_ner_chunk","sentence"))
	.setOutputCol("relation_extraction")

val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner,
    ner_converter,
    pos_tagger,
    dependency_parser,
    re_ner_chunk_filter,
    re_model))

val data = Seq("The Patient underwent a computed tomography scan, which showed a complex ovarian mass, 2 cm insize . A Pap smear performed one month later was positive for atypical glandular cells suspicious for adenocarcinoma. The pathologic specimen showed extension of the tumor throughout the fallopian tubes, appendix, omentum, and 5 out of 5 enlarged lymph nodes.").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

|   |       relation |              entity1 | entity1_begin | entity1_end |                   chunk1 |              entity2 | entity2_begin | entity2_end |                   chunk2 | confidence |
|--:|---------------:|---------------------:|--------------:|------------:|-------------------------:|---------------------:|--------------:|------------:|-------------------------:|-----------:|
| 0 |  is_finding_of |         Imaging_Test |            24 |          47 | computed tomography scan |        Tumor_Finding |            81 |          84 |                     mass |   0.672964 |
| 1 | is_location_of | Site_Other_Body_Part |            73 |          79 |                  ovarian |        Tumor_Finding |            81 |          84 |                     mass |   0.976508 |
| 2 |     is_size_of |        Tumor_Finding |            81 |          84 |                     mass |           Tumor_Size |            87 |          90 |                     2 cm |   0.952546 |
| 3 |     is_date_of |       Pathology_Test |           103 |         111 |                Pap smear |        Relative_Date |           123 |         137 |          one month later |   0.927102 |
| 4 |  is_finding_of |       Pathology_Test |           103 |         111 |                Pap smear |     Pathology_Result |           156 |         179 | atypical glandular cells |   0.860861 |
| 5 |  is_finding_of |       Pathology_Test |           103 |         111 |                Pap smear |            Cancer_Dx |           196 |         209 |           adenocarcinoma |   0.545740 |
| 6 | is_location_of |        Tumor_Finding |           260 |         264 |                    tumor | Site_Other_Body_Part |           281 |         295 |          fallopian tubes |   0.875905 |
| 7 | is_location_of |        Tumor_Finding |           260 |         264 |                    tumor | Site_Other_Body_Part |           298 |         305 |                 appendix |   0.774170 |
| 8 | is_location_of |        Tumor_Finding |           260 |         264 |                    tumor | Site_Other_Body_Part |           308 |         314 |                  omentum |   0.906041 |
 
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|redl_oncology_granular_biobert|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[re_ner_chunk, sentence]|
|Output Labels:|[relation_extraction]|
|Language:|en|
|Size:|405.4 MB|

## References

In-house annotated oncology case reports.

## Benchmarking

```bash
         label  recall  precision   f1  
             O    0.83       0.91 0.87   
    is_date_of    0.82       0.80 0.81    
 is_finding_of    0.92       0.85 0.88   
is_location_of    0.95       0.85 0.90    
    is_size_of    0.91       0.80 0.85    
     macro-avg    0.89       0.84 0.86
```
