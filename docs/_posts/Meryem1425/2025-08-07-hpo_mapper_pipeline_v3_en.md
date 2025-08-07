---
layout: model
title: Phenotype Entity Recognition and HPO Mapping to UMLS, EOM, Genes, and Diseases (Pretrained Pipeline)
author: John Snow Labs
name: hpo_mapper_pipeline_v3
date: 2025-08-07
tags: [licensed, en, clinical, hpo, pipeline, ner, assertion, mapper, disease, gene, eom]
task: [Named Entity Recognition, Chunk Mapping, Assertion Status, Pipeline Healthcare]
language: en
edition: Healthcare NLP 6.0.4
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to extract phenotype-related entities from clinical or biomedical text, map them to their corresponding Human Phenotype Ontology (HPO) codes, and determine their assertion status (e.g., present, absent, suspected).
In addition to HPO mapping, the pipeline also performs the following:
 - Maps HPO codes to UMLS CUIs
 - Identifies associations with Extraocular Movements (EOM)
 - Maps HPO terms to related genes
 - Retrieves diseases associated with those genes
This pretrained pipeline enables deeper phenotypic and genomic insights directly from unstructured text.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hpo_mapper_pipeline_v3_en_6.0.4_3.4_1754587104660.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hpo_mapper_pipeline_v3_en_6.0.4_3.4_1754587104660.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("hpo_mapper_pipeline_v3", "en", "clinical/models")

result = pipeline.fullAnnotate("""APNEA: Presumed apnea of prematurity since < 34 wks gestation at birth.
HYPERBILIRUBINEMIA: At risk for hyperbilirubinemia d/t prematurity.
1/25-1/30: Received Amp/Gent while undergoing sepsis evaluation.
Mother is A+, GBS unknown, and infant delivered
for decreasing fetal movement and preeclampsia.
Long finger and toes detected.
he has a increased overbite expression.
""")

```

{:.jsl-block}
```python

pipeline = nlp.PretrainedPipeline("hpo_mapper_pipeline_v3", "en", "clinical/models")


result = pipeline.fullAnnotate("""APNEA: Presumed apnea of prematurity since < 34 wks gestation at birth.
HYPERBILIRUBINEMIA: At risk for hyperbilirubinemia d/t prematurity.
1/25-1/30: Received Amp/Gent while undergoing sepsis evaluation.
Mother is A+, GBS unknown, and infant delivered
for decreasing fetal movement and preeclampsia.
Long finger and toes detected.
he has a increased overbite expression.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("hpo_mapper_pipeline_v3", "en", "clinical/models")

val result = pipeline.fullAnnotate("""APNEA: Presumed apnea of prematurity since < 34 wks gestation at birth.
HYPERBILIRUBINEMIA: At risk for hyperbilirubinemia d/t prematurity.
1/25-1/30: Received Amp/Gent while undergoing sepsis evaluation.
Mother is A+, GBS unknown, and infant delivered
for decreasing fetal movement and preeclampsia.
Long finger and toes detected.
he has a increased overbite expression.
""")

```
</div>

## Results

```bash

+-----------------------+-------------------------+-----+---+---------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------+--------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|           matched_text|                ner_chunk|begin|end|assertion|  hpo_code|                                                                                                                                            hpo_parent|umls_mapping|         eom_mapping|                                                                                                                                          gene_disease|
+-----------------------+-------------------------+-----+---+---------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------+--------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|      apnea prematurity|     apnea of prematurity|   16| 35|  present|HP:0034236|HP:0002104: Apnea ## Lack of breathing with no movement of the respiratory muscles and no exchange of air in the lungs. This term refers to a dispo...|        NONE|                NONE|                                                                                                                                                  NONE|
|     hyperbilirubinemia|       hyperbilirubinemia|  104|121|  present|HP:0002904|HP:0033479: Abnormal circulating bilirubin concentration ##  => HP:0010995: Abnormal circulating dicarboxylic acid concentration ## A dicarboxylic ...|    C1142335|                NONE|{"ADK": ["poor speech", "seizure", "hypotonia", "increased csf methionine concentration", "hepatic steatosis", "cholestasis", "muscle weakness", "a...|
|                 sepsis|                   sepsis|  186|191|  present|HP:0100806|HP:0010978: Abnormality of immune system physiology ## A functional abnormality of the immune system. => HP:0002715: Abnormality of the immune syst...|        NONE|                NONE|{"ABCA3": ["honeycomb lung", "ground-glass opacification", "nonspecific interstitial pneumonia", "bronchial wall thickening", "sepsis", "clubbing",...|
|decrease fetal movement|decreasing fetal movement|  257|281|  present|HP:0001558|HP:0001557: Prenatal movement abnormality ## Fetal movements generally become apparent during the second trimester of pregnancy around the 20th wee...|        NONE|                NONE|{"AARS1": ["distal muscle weakness", "limb dystonia", "bilateral sensorineural hearing impairment", "abnormality of prenatal development or birth",...|
|           preeclampsia|             preeclampsia|  287|298|  present|HP:0100602|HP:0100603: Toxemia of pregnancy ## Pregnancy-induced toxic reactions of the mother that can be as harmless as slight Maternal hypertension or as l...|        NONE|                NONE|{"SLC25A20": ["reduced circulating 6-pyruvoyltetrahydropterin synthase activity", "reduced tissue carnitine-acylcarnitine translocase activity", "e...|
|            Long finger|              Long finger|  301|311|  present|HP:0100807|HP:0001167: Abnormal finger morphology ## An anomaly of a finger. => HP:0001155: Abnormality of the hand ## An abnormality affecting one or both ha...|        NONE|EOM:41535e8ed3dc9076|{"BIN1": ["distal muscle weakness", "exercise-induced myalgia", "proximal muscle weakness", "generalized amyotrophy", "generalized hypotonia", "lon...|
|     increased overbite|       increased overbite|  341|358|  present|HP:0011094|HP:0000692: Tooth malposition ## Abnormal alignment, positioning, or spacing of the teeth, i.e., misaligned teeth. => HP:0000164: Abnormality of th...|        NONE|                NONE|{"EP300": ["adducted thumb", "syndactyly", "trichiasis", "simple ear", "spina bifida", "sporadic", "panic attack", "generalized hypotonia", "agenes...|
+-----------------------+-------------------------+-----+---+---------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------+--------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hpo_mapper_pipeline_v3|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.8 GB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- InternalDocumentSplitter
- TokenizerModel
- TextMatcherInternalModel
- ChunkMergeModel
- WordEmbeddingsModel
- ChunkMapperModel
- Mapper2Chunk
- ChunkMapperModel
- ChunkMapperModel
- ChunkMapperModel
- ChunkMapperModel
- AssertionDLModel