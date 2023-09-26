---
layout: model
title: Clinical Deidentification Pipeline (Romanian)
author: John Snow Labs
name: clinical_deidentification
date: 2023-06-13
tags: [licensed, clinical, ro, deid, deidentification]
task: [De-identification, Pipeline Healthcare]
language: ro
edition: Healthcare NLP 4.4.4
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is trained with `w2v_cc_300d` Romanian embeddings and can be used to deidentify PHI information from medical texts in Romanian. The PHI information will be masked and obfuscated in the resulting text. The pipeline can mask, fake or obfuscate the following entities: `AGE`, `CITY`, `COUNTRY`, `DATE`, `DOCTOR`, `EMAIL`, `FAX`, `HOSPITAL`, `IDNUM`, `LOCATION-OTHER`, `MEDICALRECORD`, `ORGANIZATION`, `PATIENT`, `PHONE`, `PROFESSION`, `STREET`, `ZIP`, `ACCOUNT`, `LICENSE`, `PLATE`

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_ro_4.4.4_3.2_1686665695668.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_deidentification_ro_4.4.4_3.2_1686665695668.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification", "ro", "clinical/models")

sample = """Medic : Dr. Agota EVELYN, C.N.P : 2450502264401, Data setului de analize: 25 May 2022 
Varsta : 77, Nume si Prenume : BUREAN MARIA 
Tel: +40(235)413773, E-mail : hale@gmail.com,
Licență : B004256985M, Înmatriculare : CD205113, Cont : FXHZ7170951927104999, 
Spitalul Pentru Ochi de Deal Drumul Oprea Nr. 972 Vaslui, 737405 """

result = deid_pipeline.annotate(sample)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = new PretrainedPipeline("clinical_deidentification", "ro", "clinical/models")

val sample = """Medic : Dr. Agota EVELYN, C.N.P : 2450502264401, Data setului de analize: 25 May 2022 
Varsta : 77, Nume si Prenume : BUREAN MARIA 
Tel: +40(235)413773, E-mail : hale@gmail.com,
Licență : B004256985M, Înmatriculare : CD205113, Cont : FXHZ7170951927104999, 
Spitalul Pentru Ochi de Deal Drumul Oprea Nr. 972 Vaslui, 737405 """

val result = deid_pipeline.annotate(sample)
```


{:.nlu-block}
```python
import nlu
nlu.load("ro.deid.clinical").predict("""Medic : Dr. Agota EVELYN, C.N.P : 2450502264401, Data setului de analize: 25 May 2022 
Varsta : 77, Nume si Prenume : BUREAN MARIA 
Tel: +40(235)413773, E-mail : hale@gmail.com,
Licență : B004256985M, Înmatriculare : CD205113, Cont : FXHZ7170951927104999, 
Spitalul Pentru Ochi de Deal Drumul Oprea Nr. 972 Vaslui, 737405 """)
```

</div>

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("clinical_deidentification", "ro", "clinical/models")

sample = """Medic : Dr. Agota EVELYN, C.N.P : 2450502264401, Data setului de analize: 25 May 2022 
Varsta : 77, Nume si Prenume : BUREAN MARIA 
Tel: +40(235)413773, E-mail : hale@gmail.com,
Licență : B004256985M, Înmatriculare : CD205113, Cont : FXHZ7170951927104999, 
Spitalul Pentru Ochi de Deal Drumul Oprea Nr. 972 Vaslui, 737405 """

result = deid_pipeline.annotate(sample)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val deid_pipeline = new PretrainedPipeline("clinical_deidentification", "ro", "clinical/models")

val sample = """Medic : Dr. Agota EVELYN, C.N.P : 2450502264401, Data setului de analize: 25 May 2022 
Varsta : 77, Nume si Prenume : BUREAN MARIA 
Tel: +40(235)413773, E-mail : hale@gmail.com,
Licență : B004256985M, Înmatriculare : CD205113, Cont : FXHZ7170951927104999, 
Spitalul Pentru Ochi de Deal Drumul Oprea Nr. 972 Vaslui, 737405 """

val result = deid_pipeline.annotate(sample)
```

{:.nlu-block}
```python
import nlu
nlu.load("ro.deid.clinical").predict("""Medic : Dr. Agota EVELYN, C.N.P : 2450502264401, Data setului de analize: 25 May 2022 
Varsta : 77, Nume si Prenume : BUREAN MARIA 
Tel: +40(235)413773, E-mail : hale@gmail.com,
Licență : B004256985M, Înmatriculare : CD205113, Cont : FXHZ7170951927104999, 
Spitalul Pentru Ochi de Deal Drumul Oprea Nr. 972 Vaslui, 737405 """)
```
</div>

## Results

```bash
Results


Masked with entity labels
------------------------------
Medic : Dr. <DOCTOR>, C.N.P : <IDNUM>, Data setului de analize: <DATE>
Varsta : <AGE>, Nume si Prenume : <PATIENT>
Tel: <PHONE>, E-mail : <EMAIL>,
Licență : <LICENSE>, Înmatriculare : <PLATE>, Cont : <ACCOUNT>, 
<HOSPITAL> <STREET> <CITY>, <ZIP>

Masked with chars
------------------------------
Medic : Dr. [**********], C.N.P : [***********], Data setului de analize: [*********]
Varsta : **, Nume si Prenume : [**********]
Tel: [************], E-mail : [************],
Licență : [*********], Înmatriculare : [******], Cont : [******************], 
[**************************] [******************] [****], [****]

Masked with fixed length chars
------------------------------
Medic : Dr. ****, C.N.P : ****, Data setului de analize: ****
Varsta : ****, Nume si Prenume : ****
Tel: ****, E-mail : ****,
Licență : ****, Înmatriculare : ****, Cont : ****, 
**** **** ****, ****

Obfuscated
------------------------------
Medic : Dr. Doina Gheorghiu, C.N.P : 6794561192919, Data setului de analize: 01-04-2001
Varsta : 91, Nume si Prenume : Dragomir Emilia
Tel: 0248 551 376, E-mail : tudorsmaranda@kappa.ro,
Licență : T003485962M, Înmatriculare : AR-65-UPQ, Cont : KHHO5029180812813651, 
Centrul Medical de Evaluare si Recuperare pentru Copii si Tineri Cristian Serban Buzias Aleea Voinea Curcani, 328479


{:.model-param}
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_deidentification|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|ro|
|Size:|1.2 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ChunkMergeModel
- ChunkMergeModel
- DeIdentificationModel
- DeIdentificationModel
- DeIdentificationModel
- DeIdentificationModel
- Finisher