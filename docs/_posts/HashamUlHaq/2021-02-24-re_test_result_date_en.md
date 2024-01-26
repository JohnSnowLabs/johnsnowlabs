---
layout: model
title: Relation Extraction between Tests, Results, and Dates
author: John Snow Labs
name: re_test_result_date
date: 2021-02-24
tags: [licensed, en, clinical, relation_extraction]
task: Relation Extraction
language: en
nav_key: models
edition: Healthcare NLP 2.7.4
spark_version: 2.4
supported: true
annotator: RelationExtractionModel
article_header:
type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Relation extraction between lab test names, their findings, measurements, results, and date.

## Predicted Entities

`is_finding_of`, `is_result_of`, `is_date_of`, `O`.

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/RE_CLINICAL_DATE/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/10.Clinical_Relation_Extraction.ipynb#scrollTo=D8TtVuN-Ee8s){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/re_test_result_date_en_2.7.4_2.4_1614168615976.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/re_test_result_date_en_2.7.4_2.4_1614168615976.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

Use as part of an nlp pipeline with the following stages: DocumentAssembler, SentenceDetector, Tokenizer, PerceptronModel, DependencyParserModel, WordEmbeddingsModel, NerDLModel, NerConverter, RelationExtractionModel


In the table below, `re_test_result_date` RE model, its labels, optimal NER model, and meaningful relation pairs are illustrated.



|       RE MODEL      |                     RE MODEL LABES                     | NER MODEL | RE PAIRS                                                                                                                                                                                                                                                                                                                                 |
|:-------------------:|:------------------------------------------------------:|:---------:|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| re_test_result_date | is_finding_of, <br>is_result_of, <br>is_date_of, <br>O |  ner_jsl  | ['test-test_result', 'test_result-test', <br>'date-admission_discharge','admission_discharge-date', <br>'date-alcohol', 'alcohol-date', <br>'date-bmi', 'bmi-date', <br>'date-birth_entity', 'birth_entity-date', <br>'date-blood_pressure','blood_pressure-date', <br>'date-cerebrovascular_disease', 'cerebrovascular_disease-date', <br>'date-communicable_disease', 'communicable_disease-date',<br>'date-death_entity', 'death_entity-date', <br>'date-diabetes', 'diabetes-date', <br>'date-diet', 'diet-date', <br>'date-disease_syndrome_disorder', disease_syndrome_disorder-date', <br>'date-drug_brandname', 'drug_brandname-date', <br>'date-drug_ingredient', 'drug_ingredient-date', <br>'date-ekg_findings','ekg_findings-date', <br>'date-employment', 'employment-date', <br>'date-fetus_newborn', 'fetus_newborn-date', <br>'date-hdl', 'hdl-date', <br>'date-heart_disease', 'heart_disease-date', <br>'date-height', 'height-date', <br>'date-hyperlipidemia', 'hyperlipidemia-date', <br>'date-hypertension', 'hypertension-date',<br>'date-imagingfindings', 'imagingfindings-date', <br>'date-imaging_technique', 'imaging_technique-date', <br>'date-injury_or_poisoning', 'injury_or_poisoning-date',<br>'date-internal_organ_or_component', 'internal_organ_or_component-date', <br>'date-kidney_disease', 'kidney_disease-date', <br>'date-ldl', 'ldl-date',<br>'date-labour_delivery', 'labour_delivery-date', <br>'date-o2_saturation', 'o2_saturation-date', <br>'date-obesity', 'obesity-date', <br>'date-oncological', 'oncological-date', <br>'date-overweight', 'overweight-date', <br>'date-oxygen_therapy', 'oxygen_therapy-date', <br>'date-pregnancy', 'pregnancy-date',<br>'date-procedure', 'procedure-date', <br>'date-psychological_condition', 'psychological_condition-date', <br>'date-pulse', 'pulse-date',<br>'date-relationship_status', 'relationship_status-date', <br>'date-relativedate', 'relativedate-date', <br>'date-relativetime', 'relativetime-date', <br>'date-respiration', 'respiration-date', <br>'date-route', 'route-date', <br>'date-sexually_active_or_sexual_orientation','sexually_active_or_sexual_orientation-date', <br>'date-smoking', 'smoking-date', <br>'date-substance', 'substance-date', <br>'date-substance_quantity', substance_quantity-date', <br>'date-symptom', 'symptom-date', <br>'date-temperature', 'temperature-date', <br>'date-test', 'test-date', <br>'date-test_result', 'test_result-date', <br>'date-total_cholesterol', 'total_cholesterol-date', <br>'date-treatment', 'treatment-date', <br>'date-triglycerides', 'triglycerides-date',<br>'date-vs_finding', 'vs_finding-date', <br>'date-vaccine', 'vaccine-date', <br>'date-weight', 'weight-date', <br>'relativedate-admission_discharge','admission_discharge-relativedate', <br>'relativedate-alcohol', 'alcohol-relativedate', <br>'relativedate-bmi', 'bmi-relativedate', <br>'relativedate-birth_entity', 'birth_entity-relativedate', <br>'relativedate-blood_pressure', 'blood_pressure-relativedate', <br>'relativedate-cerebrovascular_disease', cerebrovascular_disease-relativedate', <br>'relativedate-communicable_disease', 'communicable_disease-relativedate', <br>'relativedate-death_entity', 'death_entity-relativedate', <br>'relativedate-diabetes', 'diabetes-relativedate', <br>'relativedate-diet', 'diet-relativedate', <br>'relativedate-disease_syndrome_disorder', 'disease_syndrome_disorder-relativedate', <br>'relativedate-drug_brandname', 'drug_brandname-relativedate',<br>'relativedate-drug_ingredient', 'drug_ingredient-relativedate', <br>'relativedate-ekg_findings', 'ekg_findings-relativedate', <br>'relativedate-employment', 'employment-relativedate', <br>'relativedate-fetus_newborn', 'fetus_newborn-relativedate', <br>'relativedate-hdl', 'hdl-relativedate', <br>'relativedate-heart_disease', 'heart_disease-relativedate', <br>'relativedate-height', 'height-relativedate', <br>'relativedate-hyperlipidemia', 'hyperlipidemia-relativedate',<br>'relativedate-hypertension', 'hypertension-relativedate', <br>'relativedate-imagingfindings', 'imagingfindings-relativedate', <br>'relativedate-imaging_technique', 'imaging_technique-relativedate', <br>'relativedate-injury_or_poisoning', 'injury_or_poisoning-relativedate', <br>'relativedate-internal_organ_or_component', internal_organ_or_component-relativedate', <br>'relativedate-kidney_disease', 'kidney_disease-relativedate', <br>'relativedate-ldl', 'ldl-relativedate',<br>'relativedate-labour_delivery', 'labour_delivery-relativedate', <br>'relativedate-o2_saturation', 'o2_saturation-relativedate', <br>'relativedate-obesity', 'obesity-relativedate', <br>'relativedate-oncological', 'oncological-relativedate', <br>'relativedate-overweight', 'overweight-relativedate',<br>'relativedate-oxygen_therapy', 'oxygen_therapy-relativedate', <br>'relativedate-pregnancy', 'pregnancy-relativedate', <br>'relativedate-procedure', 'procedure-relativedate', <br>'relativedate-psychological_condition', 'psychological_condition-relativedate', <br>'relativedate-pulse', 'pulse-relativedate',<br>'relativedate-relationship_status', 'relationship_status-relativedate', <br>'relativedate-relativedate', 'relativedate-relativetime',<br>'relativedate-relativetime', 'relativetime-relativedate', <br>'relativedate-respiration', 'respiration-relativedate', <br>'relativedate-route', 'route-relativedate',<br>'relativedate-sexually_active_or_sexual_orientation', 'sexually_active_or_sexual_orientation-relativedate', <br>'relativedate-smoking', 'smoking-relativedate',<br>'relativedate-substance', 'substance-relativedate', <br>'relativedate-substance_quantity', 'substance_quantity-relativedate', <br>'relativedate-symptom', symptom-relativedate', <br>'relativedate-temperature', 'temperature-relativedate', <br>'relativedate-test', 'test-relativedate', <br>'relativedate-test_result', 'test_result-relativedate', <br>'relativedate-total_cholesterol', 'total_cholesterol-relativedate', <br>'relativedate-treatment', 'treatment-relativedate',<br>'relativedate-triglycerides', 'triglycerides-relativedate', <br>'relativedate-vs_finding', 'vs_finding-relativedate', <br>'relativedate-vaccine','vaccine-relativedate', <br>'relativedate-weight', 'weight-relativedate', <br>'test-cerebrovascular_disease', 'cerebrovascular_disease-test', <br>'test-communicable_disease', 'communicable_disease-test', <br>'test-diabetes', 'diabetes-test', <br>'test-disease_syndrome_disorder', disease_syndrome_disorder-test', <br>'test-ekg_findings', 'ekg_findings-test', <br>'test-heart_disease', 'heart_disease-test', <br>'test-hyperlipidemia','hyperlipidemia-test', <br>'test-hypertension', 'hypertension-test', <br>'test-imagingfindings', 'imagingfindings-test', <br>'test-injury_or_poisoning', 'injury_or_poisoning-test', <br>'test-kidney_disease', 'kidney_disease-test', <br>'test-oncological', 'oncological-test', <br>'test-vs_finding', 'vs_finding-test',<br>'weight-overweight', 'overweight-weight', <br>'weight-obesity', 'obesity-weight', <br>'bmi-obesity', 'obesity-bmi', <br>'bmi-overweight', 'overweight-bmi',<br>'ekg_findings-heart_disease', 'heart_disease-ekg_findings', <br>'imaging_technique-imagingfindings', 'imagingfindings-imaging_technique'] |


<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = DocumentAssembler()\
	.setInputCol("text")\
	.setOutputCol("document")

sentencer = SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentences")

tokenizer = Tokenizer()\
    .setInputCols(["sentences"])\
    .setOutputCol("tokens")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentences", "tokens"])\
    .setOutputCol("embeddings")

pos_tagger = PerceptronModel()\
    .pretrained("pos_clinical", "en", "clinical/models") \
    .setInputCols(["sentences", "tokens"])\
    .setOutputCol("pos_tags")

ner_tagger = MedicalNerModel().pretrained('ner_jsl',"en","clinical/models")\
    .setInputCols("sentences", "tokens", "embeddings")\
    .setOutputCol("ner_tags")

ner_chunker = NerConverterInternal()\
    .setInputCols(["sentences", "tokens", "ner_tags"])\
    .setOutputCol("ner_chunks")

dependency_parser = DependencyParserModel()\
    .pretrained("dependency_conllu", "en")\
    .setInputCols(["sentences", "pos_tags", "tokens"])\
    .setOutputCol("dependencies")

re_model = RelationExtractionModel().pretrained("re_test_result_date", "en", 'clinical/models')\
    .setInputCols(["embeddings", "pos_tags", "ner_chunks", "dependencies"])\
    .setOutputCol("relations")\
    .setMaxSyntacticDistance(4)\
    .setPredictionThreshold(0.9)


nlp_pipeline = Pipeline(stages=[document_assembler,
                                sentencer,
                                tokenizer,
                                word_embeddings,
                                pos_tagger,
                                ner_tagger,
                                ner_chunker,
                                dependency_parser,
                                re_model])

light_pipeline = LightPipeline(nlp_pipeline.fit(spark.createDataFrame([['']]).toDF("text")))

results = light_pipeline.fullAnnotate("""He was advised chest X-ray or CT scan after checking his SpO2 which was <= 93%""")
```

```scala
val document_assembler = new DocumentAssembler()
	.setInputCol("text")
	.setOutputCol("document")
	
val sentencer = new SentenceDetector()
	.setInputCols(Array("document"))
	.setOutputCol("sentences")
	
val tokenizer = new Tokenizer()
	.setInputCols(Array("sentences"))
	.setOutputCol("tokens")
	
val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
	.setInputCols(Array("sentences","tokens"))
	.setOutputCol("embeddings")
	
val pos_tagger = PerceptronModel
	.pretrained("pos_clinical","en","clinical/models")
	.setInputCols(Array("sentences","tokens"))
	.setOutputCol("pos_tags")
	
val ner_tagger = MedicalNerModel
	.pretrained("ner_jsl","en","clinical/models")
	.setInputCols("sentences","tokens","embeddings")
	.setOutputCol("ner_tags")
	
val ner_chunker = new NerConverterInternal()
	.setInputCols(Array("sentences","tokens","ner_tags"))
	.setOutputCol("ner_chunks")
	
val dependency_parser = DependencyParserModel
	.pretrained("dependency_conllu","en")
	.setInputCols(Array("sentences","pos_tags","tokens"))
	.setOutputCol("dependencies")
	
val re_model = RelationExtractionModel.pretrained("re_test_result_date","en","clinical/models")
	.setInputCols(Array("embeddings","pos_tags","ner_chunks","dependencies"))
	.setOutputCol("relations")
	.setMaxSyntacticDistance(4)
	.setPredictionThreshold(0.9)
	
val nlp_pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentencer, 
    tokenizer, 
    word_embeddings, 
    pos_tagger, 
    ner_tagger, 
    ner_chunker, 
    dependency_parser, 
    re_model))
	
val light_pipeline = new LightPipeline(nlp_pipeline.fit(Seq("") .toDF("text")))
	
val results = light_pipeline.fullAnnotate("""He was advised chest X-ray or CT scan after checking his SpO2 which was <= 93%""")
```


{:.nlu-block}
```python
import nlu
nlu.load("en.relation.test_result_date").predict("""He was advised chest X-ray or CT scan after checking his SpO2 which was <= 93%""")
```

</div>

## Results

```bash
|   |      relation | entity1 | entity1_begin | entity1_end |      chunk1 | entity2 | entity2_begin | entity2_end |      chunk2 | confidence |
|--:|--------------:|--------:|--------------:|------------:|------------:|--------:|--------------:|------------:|------------:|-----------:|
| 0 | is_finding_of |  Gender |             0 |           1 |          He |    Test |            15 |          25 | chest X-ray |    0.99916 |
| 1 | is_finding_of |  Gender |             0 |           1 |          He |    Test |            30 |          36 |     CT scan |    1.00000 |
| 2 | is_finding_of |    Test |            15 |          25 | chest X-ray |    Test |            30 |          36 |     CT scan |    1.00000 |
| 3 | is_finding_of |    Test |            30 |          36 |     CT scan |  Gender |            53 |          55 |         his |    1.00000 |
| 4 | is_finding_of |    Test |            30 |          36 |     CT scan |    Test |            57 |          60 |        SpO2 |    1.00000 |
| 5 |    is_date_of |  Gender |            53 |          55 |         his |    Test |            57 |          60 |        SpO2 |    0.98956 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|re_test_result_date|
|Type:|re|
|Compatibility:|Healthcare NLP 2.7.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[embeddings, pos_tags, train_ner_chunks, dependencies]|
|Output Labels:|[relations]|
|Language:|en|

## Data Source

Trained on internal data.

## Benchmarking

```bash
| relation        | prec |
|-----------------|------|
| O               | 0.77 |
| is_finding_of   | 0.80 |
| is_result_of    | 0.96 |
| is_date_of      | 0.94 |

```