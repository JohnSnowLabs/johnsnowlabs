---
layout: model
title: RCT Binary Classifier (BioBERT) Pipeline
author: John Snow Labs
name: bert_sequence_classifier_binary_rct_biobert_pipeline
date: 2023-06-16
tags: [licensed, classifier, rct, clinical, en]
task: Entity Resolution
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pre-trained pipeline is a BioBERT based classifier that can classify if an article is a randomized clinical trial (RCT) or not. This pretrained pipeline is built on the top of [bert_sequence_classifier_binary_rct_biobert](https://nlp.johnsnowlabs.com/2022/04/25/bert_sequence_classifier_binary_rct_biobert_en_3_0.html) model.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_binary_rct_biobert_pipeline_en_4.4.4_3.4_1686932746440.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_binary_rct_biobert_pipeline_en_4.4.4_3.4_1686932746440.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("bert_sequence_classifier_binary_rct_biobert_pipeline", "en", "clinical/models")

result = pipeline.annotate("""Abstract:Based on the American Society of Anesthesiologists' Practice Guidelines for Sedation and Analgesia by Non-Anesthesiologists (ASA-SED), a sedation training course aimed at improving medical safety was developed by the Japanese Association for Medical Simulation in 2011. This study evaluated the effect of debriefing on participants' perceptions of the essential points of the ASA-SED. A total of 38 novice doctors participated in the sedation training course during the research period. Of these doctors, 18 participated in the debriefing group, and 20 participated in non-debriefing group. Scoring of participants' guideline perceptions was conducted using an evaluation sheet (nine items, 16 points) created based on the ASA-SED. The debriefing group showed a greater perception of the ASA-SED, as reflected in the significantly higher scores on the evaluation sheet (median, 16 points) than the control group (median, 13 points; p < 0.05). No significant differences were identified before or during sedation, but the difference after sedation was significant (p < 0.05). Debriefing after sedation training courses may contribute to better perception of the ASA-SED, and may lead to enhanced attitudes toward medical safety during sedation and analgesia. """)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("bert_sequence_classifier_binary_rct_biobert_pipeline", "en", "clinical/models")

val result = pipeline.annotate("""Abstract:Based on the American Society of Anesthesiologists' Practice Guidelines for Sedation and Analgesia by Non-Anesthesiologists (ASA-SED), a sedation training course aimed at improving medical safety was developed by the Japanese Association for Medical Simulation in 2011. This study evaluated the effect of debriefing on participants' perceptions of the essential points of the ASA-SED. A total of 38 novice doctors participated in the sedation training course during the research period. Of these doctors, 18 participated in the debriefing group, and 20 participated in non-debriefing group. Scoring of participants' guideline perceptions was conducted using an evaluation sheet (nine items, 16 points) created based on the ASA-SED. The debriefing group showed a greater perception of the ASA-SED, as reflected in the significantly higher scores on the evaluation sheet (median, 16 points) than the control group (median, 13 points; p < 0.05). No significant differences were identified before or during sedation, but the difference after sedation was significant (p < 0.05). Debriefing after sedation training courses may contribute to better perception of the ASA-SED, and may lead to enhanced attitudes toward medical safety during sedation and analgesia. """)
```


{:.nlu-block}
```python
import nlu
nlu.load("en.classify.bert_sequence.binary_rct_biobert.pipeline").predict("""Abstract:Based on the American Society of Anesthesiologists' Practice Guidelines for Sedation and Analgesia by Non-Anesthesiologists (ASA-SED), a sedation training course aimed at improving medical safety was developed by the Japanese Association for Medical Simulation in 2011. This study evaluated the effect of debriefing on participants' perceptions of the essential points of the ASA-SED. A total of 38 novice doctors participated in the sedation training course during the research period. Of these doctors, 18 participated in the debriefing group, and 20 participated in non-debriefing group. Scoring of participants' guideline perceptions was conducted using an evaluation sheet (nine items, 16 points) created based on the ASA-SED. The debriefing group showed a greater perception of the ASA-SED, as reflected in the significantly higher scores on the evaluation sheet (median, 16 points) than the control group (median, 13 points; p < 0.05). No significant differences were identified before or during sedation, but the difference after sedation was significant (p < 0.05). Debriefing after sedation training courses may contribute to better perception of the ASA-SED, and may lead to enhanced attitudes toward medical safety during sedation and analgesia. """)
```

</div>


## Results

```bash
+----+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|rct |text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+----+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|True|Abstract:Based on the American Society of Anesthesiologists' Practice Guidelines for Sedation and Analgesia by Non-Anesthesiologists (ASA-SED), a sedation training course aimed at improving medical safety was developed by the Japanese Association for Medical Simulation in 2011. This study evaluated the effect of debriefing on participants' perceptions of the essential points of the ASA-SED. A total of 38 novice doctors participated in the sedation training course during the research period. Of these doctors, 18 participated in the debriefing group, and 20 participated in non-debriefing group. Scoring of participants' guideline perceptions was conducted using an evaluation sheet (nine items, 16 points) created based on the ASA-SED. The debriefing group showed a greater perception of the ASA-SED, as reflected in the significantly higher scores on the evaluation sheet (median, 16 points) than the control group (median, 13 points; p < 0.05). No significant differences were identified before or during sedation, but the difference after sedation was significant (p < 0.05). Debriefing after sedation training courses may contribute to better perception of the ASA-SED, and may lead to enhanced attitudes toward medical safety during sedation and analgesia. |
+----+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_binary_rct_biobert_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|406.0 MB|

## Included Models

- DocumentAssembler
- TokenizerModel
- MedicalBertForSequenceClassification