---
layout: model
title: Pipeline for Extraction of Biomarkers, itis assertions and relations
author: John Snow Labs
name: custom_biomarker_pipeline
date: 2025-06-18
tags: [en, licensed]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.5.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pipeline for Extraction of Biomarkers, itis assertions and relations

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/custom_biomarker_pipeline_en_5.5.0_3.4_1750218320379.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/custom_biomarker_pipeline_en_5.5.0_3.4_1750218320379.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_biomarker_1 = MedicalNerModel.pretrained("ner_oncology_test_wip", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner_biomarker_1")

ner_converter_1 = NerConverter() \
    .setInputCols(["sentence", "token", "ner_biomarker_1"]) \
    .setOutputCol("ner_chunk_biomarker_1")

ner_biomarker_2 = MedicalNerModel.pretrained("ner_oncology_biomarker_wip", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner_biomarker_2")

ner_converter_2 = NerConverter() \
    .setInputCols(["sentence", "token", "ner_biomarker_2"]) \
    .setOutputCol("ner_chunk_biomarker_2")

ner_biomarker_3 = MedicalNerModel.pretrained("ner_oncology_wip", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner_biomarker_3")

ner_converter_3 = NerConverter() \
    .setInputCols(["sentence", "token", "ner_biomarker_3"]) \
    .setOutputCol("ner_chunk_biomarker_3")

assertions_1 = AssertionDLModel.pretrained("assertion_oncology_wip", "en", "clinical/models") \
    .setInputCols(["sentence", "ner_chunk_biomarker_1", "embeddings"]) \
    .setOutputCol("assertions_1")

assertions_2 = AssertionDLModel.pretrained("assertion_oncology_test_binary_wip", "en", "clinical/models") \
    .setInputCols(["sentence", "ner_chunk_biomarker_2", "embeddings"]) \
    .setOutputCol("assertions_2")

assertions_3 = AssertionDLModel.pretrained("assertion_oncology_problem_wip", "en", "clinical/models") \
    .setInputCols(["sentence", "ner_chunk_biomarker_3", "embeddings"]) \
    .setOutputCol("assertions_3")

pos_tagger = PerceptronModel.pretrained("pos_clinical", "en", "clinical/models") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("pos_tags")

dependency_parser = DependencyParserModel.pretrained("dependency_conllu", "en") \
    .setInputCols(["sentence", "pos_tags", "token"]) \
    .setOutputCol("dependencies")

re_model_1 = RelationExtractionModel.pretrained("re_oncology_biomarker_result", "en", "clinical/models") \
    .setInputCols(["embeddings", "pos_tags", "ner_chunk_biomarker_1", "dependencies"]) \
    .setOutputCol("relation_extraction_1") \
    .setRelationPairs(['Biomarker-Biomarker_Result', 'Biomarker_Result-Biomarker', 'Oncogene-Biomarker_Result', 'Biomarker_Result-Oncogene']) \
    .setMaxSyntacticDistance(10)

re_model_2 = RelationExtractionModel.pretrained("re_oncology_granular_wip", "en", "clinical/models") \
    .setInputCols(["embeddings", "pos_tags", "ner_chunk_biomarker_2", "dependencies"]) \
    .setOutputCol("relation_extraction_2") \
    .setRelationPairs(['Biomarker-Biomarker_Result', 'Biomarker_Result-Biomarker', 'Oncogene-Biomarker_Result', 'Biomarker_Result-Oncogene']) \
    .setMaxSyntacticDistance(10)

re_model_3 = RelationExtractionModel.pretrained("re_oncology_wip", "en", "clinical/models") \
    .setInputCols(["embeddings", "pos_tags", "ner_chunk_biomarker_3", "dependencies"]) \
    .setOutputCol("relation_extraction_3") \
    .setRelationPairs(['Biomarker-Biomarker_Result', 'Biomarker_Result-Biomarker', 'Oncogene-Biomarker_Result', 'Biomarker_Result-Oncogene']) \
    .setMaxSyntacticDistance(10)

pipeline = Pipeline(stages=[
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_biomarker_1,
    ner_converter_1,
    ner_biomarker_2,
    ner_converter_2,
    ner_biomarker_3,
    ner_converter_3,
    assertions_1,
    assertions_2,
    assertions_3,
    pos_tagger,
    dependency_parser,
    re_model_1,
    re_model_2,
    re_model_3
])

data = spark.createDataFrame([["Immunohistochemistry was negative for thyroid transcription factor-1 and napsin A. The test was positive for ER and PR, and negative for HER2."]]).toDF("text")

result = pipeline.fit(data).transform(data)
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|custom_biomarker_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- AssertionDLModel
- AssertionDLModel
- AssertionDLModel
- PerceptronModel
- DependencyParserModel
- RelationExtractionModel
- RelationExtractionModel
- RelationExtractionModel