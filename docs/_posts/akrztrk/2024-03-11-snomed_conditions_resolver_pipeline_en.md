---
layout: model
title: Pipeline for SNOMED Conditions Sentence Entity Resolver
author: John Snow Labs
name: snomed_conditions_resolver_pipeline
date: 2024-03-11
tags: [licensed, en, entity_resolution, clinical, pipeline, snomed, conditions]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.3.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This advanced pipeline extracts clinical conditions from clinical texts and utilizes the `sbiobert_base_cased_mli` Sentence Bert Embeddings to map these entities to their corresponding SNOMED codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_conditions_resolver_pipeline_en_5.3.0_3.4_1710174497124.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_conditions_resolver_pipeline_en_5.3.0_3.4_1710174497124.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("snomed_conditions_resolver_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""Medical professionals rushed in the bustling emergency room to attend to the patient with distressed breathing.
          The attending physician immediately noted signs of respiratory distress, including stridor, a high-pitched sound indicative of upper respiratory tract obstruction.
          The patient, struggling to breathe, exhibited dyspnea. Concern raised when they began experiencing syncope,
          a sudden loss of consciousness likely stemming from inadequate oxygenation. Further examination revealed a respiratory tract hemorrhage.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("snomed_conditions_resolver_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""Medical professionals rushed in the bustling emergency room to attend to the patient with distressed breathing.
          The attending physician immediately noted signs of respiratory distress, including stridor, a high-pitched sound indicative of upper respiratory tract obstruction.
          The patient, struggling to breathe, exhibited dyspnea. Concern raised when they began experiencing syncope,
          a sudden loss of consciousness likely stemming from inadequate oxygenation. Further examination revealed a respiratory tract hemorrhage.""")

```
</div>

## Results

```bash
|    | chunks                              |   begin |   end | entities                  |      Code | description                         | resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | all_codes                                                                                                                                                                                                                                                                             |
|---:|:------------------------------------|--------:|------:|:--------------------------|----------:|:------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | distressed breathing                |      90 |   109 | Symptom                   | 271825005 | distressed breathing                | distressed breathing:::difficulty breathing:::breathing abnormal:::irregular breathing:::harsh breath sounds:::breathy voice:::noisy breathing:::painful respiration:::difficulty controlling breathing:::hissing respiration:::paradoxical breathing:::laboured breathing:::groaning respiration:::respiratory tract congestion:::increasing breathlessness                                                                                                                                                                                                                                                                                                        | 271825005:::230145002:::386813002:::248585001:::47653008:::56505000:::248573009:::75483001:::289105003:::248576001:::12025005:::248549001:::248575002:::418092006:::297216006                                                                                                         |
|  1 | respiratory distress                |     173 |   192 | VS_Finding                | 271825005 | respiratory distress                | respiratory distress:::respiratory tract congestion:::painful respiration:::acute respiratory distress:::respiration difficult:::respiratory failure:::harsh breath sounds:::respiratory insufficiency:::mental distress:::feeling distress:::upper facial weakness:::respiratory obstruction:::distress:::respiratory depression:::confusional state:::flail chest:::breathy voice:::increasing breathlessness:::respiratory injury:::breathing abnormal:::emotional upset                                                                                                                                                                                         | 271825005:::418092006:::75483001:::373895009:::230145002:::409622000:::47653008:::409623005:::271596009:::224977004:::298281008:::79688008:::69328002:::80954004:::286933003:::78011002:::56505000:::297216006:::127275008:::386813002:::309838005                                    |
|  2 | stridor                             |     205 |   211 | Symptom                   |  70407001 | stridor                             | stridor:::intermittent stridor:::inhalatory stridor:::expiratory stridor:::biphasic stridor:::laryngeal stridor:::breathiness:::nasal grimacing:::drooling:::smelly breath:::malaise:::general unsteadiness:::bloating:::croaky voice:::fussiness:::restlessness:::stertorous respiration:::functional bloating:::cataplexy:::soreness:::apprehension:::bloated face                                                                                                                                                                                                                                                                                                | 70407001:::301826004:::58596002:::301287002:::307487006:::773117009:::56505000:::84215002:::62718007:::79879001:::367391008:::271713000:::60728008:::50219008:::55929007:::24199005:::271621004:::722879009:::46263000:::71393004:::49971008:::248184009                              |
|  3 | a high-pitched sound                |     214 |   233 | PROBLEM                   |  51406002 | high pitched voice                  | high pitched voice:::responds to high frequency sounds:::heart sounds exaggerated:::high airway pressure:::high-pitch group:::large airway sounds:::finding of response to high frequency sounds:::high body temperature:::sounds are very loud:::heavy periods:::increased pressure:::finding of ability to hear loud voice:::heavy legs:::high head:::heightened sensation:::chest hyperinflated:::high muscle tone:::heavy feeling:::increased vocal resonance:::high blood pressure:::elevated psa                                                                                                                                                              | 51406002:::300211002:::271661003:::405495005:::23292001:::248615003:::366098000:::50177009:::247285003:::386692008:::23085004:::247303009:::161873000:::62098001:::14151009:::249674001:::56731001:::161874006:::248616002:::38341003:::396152005                                     |
|  4 | upper respiratory tract obstruction |     249 |   283 | Disease_Syndrome_Disorder |  68372009 | upper respiratory tract obstruction | upper respiratory tract obstruction:::respiratory obstruction:::tracheal obstruction:::finding of respiratory obstruction:::disorder of upper respiratory system:::expiratory partial airway obstruction:::chronic irreversible airway obstruction:::respiratory tract congestion:::respiratory insufficiency:::inspiratory partial airway obstruction:::bronchial obstruction:::disorder of respiratory system:::chronic respiratory insufficiency:::inspiratory and expiratory partial airway obstruction:::airway constriction:::injury of upper respiratory tract:::supraglottic airway obstruction:::nasal airway obstruction:::obstructive ventilatory defect | 68372009:::79688008:::73342002:::301252002:::201060008:::301254001:::13645005:::418092006:::409623005:::301253007:::36925002:::50043002:::427896006:::301255000:::44416002:::125589001:::371035002:::232209000:::447009000                                                            |
|  5 | struggling to breathe               |     309 |   329 | Symptom                   | 289105003 | difficulty controlling breathing    | difficulty controlling breathing:::difficulty breathing:::difficulty coughing:::breathing problem:::distressed breathing:::irregular breathing:::gasping for breath:::difficulty expectorating:::choking during respiration:::short of breath on exertion:::difficulty mobilising:::paradoxical breathing:::difficulty coping:::breathing pattern impairment:::difficulty in swallowing:::difficulty closing mouth:::hissing respiration:::difficulty greeting:::breathing painful                                                                                                                                                                                  | 289105003:::230145002:::289116005:::386813002:::271825005:::248585001:::23141003:::289121008:::248556007:::60845006:::302046008:::12025005:::18232000:::20573003:::40739000:::285472001:::248576001:::288810006:::75483001                                                            |
|  6 | dyspnea                             |     342 |   348 | Symptom                   | 267036007 | dyspnea                             | dyspnea:::exertional dyspnea:::inspiratory dyspnea:::expiratory dyspnea:::paroxysmal dyspnea:::chronic dyspnea:::apnea:::oligopnea:::secondary apnea:::dyspnea associated with aids:::platypnea:::orthopnea                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 267036007:::60845006:::25209001:::34560001:::59265000:::870535009:::1023001:::386614005:::90701007:::422177004:::30744009:::62744007                                                                                                                                                  |
|  7 | syncope                             |     395 |   401 | Symptom                   | 271594007 | syncope                             | syncope:::situational syncope:::tussive syncope:::witnessed syncope:::effort syncope:::cardiac syncope:::near syncope:::convulsive syncope:::deglutition syncope:::syncope symptom:::defaecation syncope:::neurally-mediated syncope:::psychogenic syncope:::hypotensive syncope:::carotid sinus syncope:::heat syncope:::syncope and collapse                                                                                                                                                                                                                                                                                                                      | 271594007:::234167006:::90129003:::445535007:::31457007:::788877005:::427461000:::438113009:::234170005:::272030005:::234169009:::398665005:::386572005:::58077008:::51723007:::89797005:::309585006                                                                                  |
|  8 | a sudden loss of consciousness      |     414 |   443 | PROBLEM                   |  32834005 | brief loss of consciousness         | brief loss of consciousness:::moderate loss of consciousness:::prolonged loss of consciousness:::sudden visual loss:::loss of consciousness:::circulatory collapse:::transient situational disturbance, nos:::decreased level of consciousness:::clouding of consciousness:::acute confusion:::disturbance of consciousness:::precipitous drop in hematocrit:::acute confusional state:::subacute confusional state:::cardiorespiratory arrest:::respiratory arrest:::temporary cerebral vascular dysfunction:::acute situational disturbance:::bilateral sudden visual loss:::concussion with loss of consciousness:::transient limb paralysis                     | 32834005:::40863000:::7862002:::15203004:::419045004:::27942005:::17226007:::443371007:::40917007:::130987000:::3006004:::417186004:::2776000:::191507002:::410430005:::87317003:::266257000:::192041001:::343331000119104:::62564004:::274662006                                     |
|  9 | inadequate oxygenation              |     466 |   487 | Symptom                   | 238161004 | impaired oxygen delivery            | impaired oxygen delivery:::impaired gas exchange:::impaired oxygen extraction:::abnormal oxygen supply:::disorder of oxygen transport:::low oxygen saturation:::decreased blood oxygen pressure:::poor tissue perfusion:::inadequate peripheral blood flow:::respiratory obstruction:::abnormal blood oxygen pressure:::poor respiratory drive:::decreased oxygen supply:::impaired consciousness:::impaired adjustment:::impaired sensation:::interrupted breathing:::respiratory insufficiency:::impaired insight:::sensory disturbance:::difficulty controlling breathing:::difficulty breathing:::impaired focus:::blood oxygen level abnormal                  | 238161004:::70944005:::238162006:::123826004:::238160003:::449171008:::123823007:::409055009:::764268008:::79688008:::123821009:::276572003:::389086002:::3006004:::18232000:::397974008:::90480005:::409623005:::12200008:::85972008:::289105003:::230145002:::246720002:::167026000 |
| 10 | a respiratory tract hemorrhage      |     519 |   548 | PROBLEM                   |  95431003 | respiratory tract hemorrhage        | respiratory tract hemorrhage:::tracheal hemorrhage:::bronchial hemorrhage:::pulmonary hemorrhage:::tracheobronchial hemorrhage:::esophageal hemorrhage:::pharyngeal hemorrhage:::bronchial anastomotic hemorrhage:::neonatal respiratory tract hemorrhage:::upper gastrointestinal hemorrhage                                                                                                                                                                                                                                                                                                                                                                       | 95431003:::233783005:::405541003:::78144005:::276543004:::15238002:::324618004:::233802008:::95621004:::37372002                                                                                                                                                                      |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_conditions_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel