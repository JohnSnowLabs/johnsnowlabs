---
layout: model
title: Sentence Entity Resolver for SNOMED CT (Miscellaneous (No Class) Concepts) (sbiobert_base_cased_mli_onnx embeddings) - Pipeline
author: John Snow Labs
name: sbiobertresolve_snomed_no_class_pipeline_20260901
date: 2026-09-12
tags: [en, entity_resolution, licensed, clinical, snomed, pipeline, sbiobert, no_class]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 6.4.1
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline extracts clinical entities from text and maps them to SNOMED CT concepts not assigned to a specific class using `sbiobert_base_cased_mli_onnx` embeddings.

Wraps the `sbiobertresolve_snomed_no_class_20260901` resolver, trained on SNOMED CT US Edition 20260901.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_no_class_pipeline_20260901_en_6.4.1_3.4_1789230533538.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_snomed_no_class_pipeline_20260901_en_6.4.1_3.4_1789230533538.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

snomed_pipeline = PretrainedPipeline("sbiobertresolve_snomed_no_class_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["The patient developed postsurgical gastroparesis after her procedure. Pathology confirmed a malignant gastroblastoma. On eye exam she was also noted to have trichiasis of upper eyelid."]]).toDF("text")
result = snomed_pipeline.transform(data)

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

snomed_pipeline = nlp.PretrainedPipeline("sbiobertresolve_snomed_no_class_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["The patient developed postsurgical gastroparesis after her procedure. Pathology confirmed a malignant gastroblastoma. On eye exam she was also noted to have trichiasis of upper eyelid."]]).toDF("text")
result = snomed_pipeline.transform(data)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val snomed_pipeline = PretrainedPipeline("sbiobertresolve_snomed_no_class_pipeline_20260901", "en", "clinical/models")

val data = Seq("The patient developed postsurgical gastroparesis after her procedure. Pathology confirmed a malignant gastroblastoma. On eye exam she was also noted to have trichiasis of upper eyelid.").toDF("text")
val result = snomed_pipeline.transform(data)

```
</div>

## Results

```bash
| chunk                      | label                     |     snomed_code | resolution                               | all_codes                                                                                                                                                                                                                                                                                                                      | all_resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|:---------------------------|:--------------------------|----------------:|:-----------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| gastroparesis              | Disease_Syndrome_Disorder |      1397402007 | postsurgical gastroparesis               | 1397402007:::440295211000119108:::1396770008:::1389031007:::1389007002:::1384135004:::1388584008:::510204201000119100:::1399444005:::1389191007:::1396814004:::1396027004:::1395863006:::465961000087104                                                                                                                       | postsurgical gastroparesis:::intestinal failure:::type 2 intestinal failure:::esophageal spasm:::ifald - intestinal failure associated liver disease:::assessment of nutritional disorder:::gastric dilatation:::autoimmune gastritis:::gastric burping:::distal esophageal spasm:::recurrent giardia lamblia intestinal infection:::erosion of mucous membrane of large intestine:::bleeding superficial ulcer of stomach:::right thoracic radiculopathy                                                                                                                                                                                                                                                                                                                                    |
| malignant gastroblastoma   | Oncological               |   2711000181102 | malignant gastroblastoma                 | 2711000181102:::1395929008:::112751000112108:::1388817002:::1388815005:::1388810000:::1388811001:::1388814009:::1388813003                                                                                                                                                                                                     | malignant gastroblastoma:::mixed glioma of brain:::gist (gastrointestinal stromal tumor) suspected:::malignant succinate dehydrogenase-deficient renal cell carcinoma:::malignant fumarate hydratase-deficient renal cell carcinoma:::malignant eloc-mutated renal cell carcinoma:::malignant alk-rearranged renal cell carcinoma:::malignant tfeb-altered renal cell carcinoma:::malignant tfe3-rearranged renal cell carcinoma                                                                                                                                                                                                                                                                                                                                                             |
| trichiasis of upper eyelid | Disease_Syndrome_Disorder | 412041000087109 | entropion and trichiasis of upper eyelid | 412041000087109:::412031000087103:::412021000087100:::412001000087106:::331531000119106:::1389166007:::11854611000119104:::1395935008:::412011000087108:::15998671000119101:::699881010000107:::1397845007:::408631000087107:::1397358000:::1397511009:::1388547006:::1388359009:::1396995000:::1396238009:::11854571000119108 | entropion and trichiasis of upper eyelid:::entropion and trichiasis of right upper eyelid:::entropion and trichiasis of right lower eyelid:::entropion and trichiasis of left upper eyelid:::spastic ectropion of right upper eyelid:::infected blister of eyelid:::infected blister of right eyelid:::wet line of upper lip:::entropion and trichiasis of lower eyelid:::cysticercosis of right eye:::lens esculenta igg:::subretinal hyperreflective material on optical coherence tomography:::contact dermatitis of skin of upper arm:::intraretinal cystoid space on optical coherence tomography:::excoriation disorder:::granulomatous uveitis:::ultrasonography of eye region abnormal:::ifag - idiopathic facial aseptic granuloma:::acne tarda:::traumatic blister of right eyelid |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_snomed_no_class_pipeline_20260901|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.2 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel