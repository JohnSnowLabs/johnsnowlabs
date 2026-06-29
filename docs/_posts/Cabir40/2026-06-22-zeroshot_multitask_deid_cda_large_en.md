---
layout: model
title: ZeroShot Multitask - CDA/XML PHI Deidentification (Large)
author: John Snow Labs
name: zeroshot_multitask_deid_cda_large
date: 2026-06-22
tags: [en, licensed, clinical, multitask, zeroshot, ner, deid, cda, xml, phi, onnx]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.4.0
spark_version: 3.0
supported: true
engine: onnx
annotator: PretrainedZeroShotMultiTask
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

PHI de-identification NER model for clinical CDA/XML documents. Extracts personally identifiable information — person names, dates, addresses, and phone numbers — to support redaction/masking workflows for HL7 CDA-formatted patient records.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_multitask_deid_cda_large_en_6.4.0_3.0_1782137735667.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_multitask_deid_cda_large_en_6.4.0_3.0_1782137735667.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

zero_shot = PretrainedZeroShotMultiTask.pretrained("zeroshot_multitask_deid_cda_large", "en", "clinical/models")\
    .setInputCols(["sentence"])\
    .setOutputCol("extractions")\
    .setEntityThreshold(0.4)\
    .setEntities([
        "PERSON_NAME",
        "DATE_TIME",
        "STREET",
        "CITY",
        "STATE",
        "ID"
    ])

pipeline = Pipeline(
    stages = [
        document_assembler,
        sentence_detector,
        zero_shot
])

text = f"""
<recordTarget xmlns="urn:hl7-org:v3" xmlns:sdtc="urn:hl7-org:sdtc">
    <patientRole>
      <id extension="T-10118" root="2.16.840.1.113883.4.1" />
      <addr use="HP">
        <streetAddressLine>1357 Amber Dr</streetAddressLine>
        <city>Beaverton</city>
        <state>OR</state>
        <postalCode>97006</postalCode>
        <country>US</country>
      </addr>
      <telecom use="MC" value="tel:+1(555)-777-1234" />
      <telecom use="HP" value="tel:+1(555)-723-1544" />
      <telecom value="360mu.alice.newman@gmail.com" />
      <patient>
        <name use="L">
          <given>Alice</given>
          <given>Jones</given>
          <family>Newman</family>
        </name>
        <name>
          <given qualifier="BR">Alicia</given>
          <family>Newman</family>
        </name>
        <administrativeGenderCode code="F" codeSystem="2.16.840.1.113883.5.1" codeSystemName="AdministrativeGender" displayName="Female" />
        <birthTime value="19700501" />
        
    
<entry xmlns="urn:hl7-org:v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" typeCode="DRIV">
            <act classCode="ACT" moodCode="EVN">
              <templateId extension="2015-08-01" root="2.16.840.1.113883.10.20.22.4.30" />
              <templateId root="2.16.840.1.113883.10.20.22.4.30" />
              <id root="b03805bd-2eb6-4ab8-a9ff-473c6653971a" />
              <code code="CONC" codeSystem="2.16.840.1.113883.5.6" />
              <statusCode code="active" />
              <effectiveTime>
                <low value="19800510" />
              </effectiveTime>
              <entryRelationship typeCode="SUBJ">
                <observation classCode="OBS" moodCode="EVN">
                  <templateId extension="2014-06-09" root="2.16.840.1.113883.10.20.22.4.7" />
                  <templateId root="2.16.840.1.113883.10.20.22.4.7" />
                  <id root="4adc1020-7b14-11db-9fe1-0800200c9a68" />
                  <code code="ASSERTION" codeSystem="2.16.840.1.113883.5.4" />
                  <statusCode code="completed" />
                  <effectiveTime>
                    <low value="19800510" />
                  </effectiveTime>
                  <value code="419511003" codeSystem="2.16.840.1.113883.6.96" codeSystemName="SNOMED CT" displayName="Propensity to adverse reaction to drug" xsi:type="CD" />
                  <participant typeCode="CSM">
                    <participantRole classCode="MANU">
                      <playingEntity classCode="MMAT">
                        <code code="733" codeSystem="2.16.840.1.113883.6.88" codeSystemName="RxNorm" displayName="Ampicillin">
                          <originalText>
                            <reference value="#product2" />
                          </originalText>
                        </code>
                      </playingEntity>
                    </participantRole>
                  </participant>
                  <entryRelationship inversionInd="true" typeCode="MFST">
                    <observation classCode="OBS" moodCode="EVN">
                      <templateId extension="2014-06-09" root="2.16.840.1.113883.10.20.22.4.9" />
                      <templateId root="2.16.840.1.113883.10.20.22.4.9" />
                      <id root="4adc1020-7b14-11db-9fe1-0800200c9a69" />
                      <code code="ASSERTION" codeSystem="2.16.840.1.113883.5.4" />
                      <text>
                        <reference value="#reaction2" />
                      </text>
                      <statusCode code="completed" />
                      <effectiveTime>
                        <low nullFlavor="NI" />
                        <high nullFlavor="NI" />
                      </effectiveTime>
                      <value code="247472004" codeSystem="2.16.840.1.113883.6.96" displayName="Hives" xsi:type="CD" />
                      <entryRelationship inversionInd="true" typeCode="SUBJ">
                        <observation classCode="OBS" moodCode="EVN">
"""

data = spark.createDataFrame([[text]]).toDF("text")

results = pipeline.fit(data).transform(data)

results.select("extractions").show(truncate=False)
```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

zero_shot = medical.PretrainedZeroShotMultiTask.pretrained("zeroshot_multitask_deid_cda_large", "en", "clinical/models")\
    .setInputCols(["sentence"])\
    .setOutputCol("extractions")\
    .setEntityThreshold(0.4)\
    .setEntities([
         "PERSON_NAME",
        "DATE_TIME",
        "STREET",
        "CITY",
        "STATE",
        "ID"
    ])

pipeline = nlp.Pipeline(
    stages = [
        document_assembler,
        sentence_detector,
        zero_shot
])

text = f"""
<recordTarget xmlns="urn:hl7-org:v3" xmlns:sdtc="urn:hl7-org:sdtc">
    <patientRole>
      <id extension="T-10118" root="2.16.840.1.113883.4.1" />
      <addr use="HP">
        <streetAddressLine>1357 Amber Dr</streetAddressLine>
        <city>Beaverton</city>
        <state>OR</state>
        <postalCode>97006</postalCode>
        <country>US</country>
      </addr>
      <telecom use="MC" value="tel:+1(555)-777-1234" />
      <telecom use="HP" value="tel:+1(555)-723-1544" />
      <telecom value="360mu.alice.newman@gmail.com" />
      <patient>
        <name use="L">
          <given>Alice</given>
          <given>Jones</given>
          <family>Newman</family>
        </name>
        <name>
          <given qualifier="BR">Alicia</given>
          <family>Newman</family>
        </name>
        <administrativeGenderCode code="F" codeSystem="2.16.840.1.113883.5.1" codeSystemName="AdministrativeGender" displayName="Female" />
        <birthTime value="19700501" />
        
    
<entry xmlns="urn:hl7-org:v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" typeCode="DRIV">
            <act classCode="ACT" moodCode="EVN">
              <templateId extension="2015-08-01" root="2.16.840.1.113883.10.20.22.4.30" />
              <templateId root="2.16.840.1.113883.10.20.22.4.30" />
              <id root="b03805bd-2eb6-4ab8-a9ff-473c6653971a" />
              <code code="CONC" codeSystem="2.16.840.1.113883.5.6" />
              <statusCode code="active" />
              <effectiveTime>
                <low value="19800510" />
              </effectiveTime>
              <entryRelationship typeCode="SUBJ">
                <observation classCode="OBS" moodCode="EVN">
                  <templateId extension="2014-06-09" root="2.16.840.1.113883.10.20.22.4.7" />
                  <templateId root="2.16.840.1.113883.10.20.22.4.7" />
                  <id root="4adc1020-7b14-11db-9fe1-0800200c9a68" />
                  <code code="ASSERTION" codeSystem="2.16.840.1.113883.5.4" />
                  <statusCode code="completed" />
                  <effectiveTime>
                    <low value="19800510" />
                  </effectiveTime>
                  <value code="419511003" codeSystem="2.16.840.1.113883.6.96" codeSystemName="SNOMED CT" displayName="Propensity to adverse reaction to drug" xsi:type="CD" />
                  <participant typeCode="CSM">
                    <participantRole classCode="MANU">
                      <playingEntity classCode="MMAT">
                        <code code="733" codeSystem="2.16.840.1.113883.6.88" codeSystemName="RxNorm" displayName="Ampicillin">
                          <originalText>
                            <reference value="#product2" />
                          </originalText>
                        </code>
                      </playingEntity>
                    </participantRole>
                  </participant>
                  <entryRelationship inversionInd="true" typeCode="MFST">
                    <observation classCode="OBS" moodCode="EVN">
                      <templateId extension="2014-06-09" root="2.16.840.1.113883.10.20.22.4.9" />
                      <templateId root="2.16.840.1.113883.10.20.22.4.9" />
                      <id root="4adc1020-7b14-11db-9fe1-0800200c9a69" />
                      <code code="ASSERTION" codeSystem="2.16.840.1.113883.5.4" />
                      <text>
                        <reference value="#reaction2" />
                      </text>
                      <statusCode code="completed" />
                      <effectiveTime>
                        <low nullFlavor="NI" />
                        <high nullFlavor="NI" />
                      </effectiveTime>
                      <value code="247472004" codeSystem="2.16.840.1.113883.6.96" displayName="Hives" xsi:type="CD" />
                      <entryRelationship inversionInd="true" typeCode="SUBJ">
                        <observation classCode="OBS" moodCode="EVN">
"""

data = spark.createDataFrame([[text]]).toDF("text")

results = pipeline.fit(data).transform(data)

results.select("extractions").show(truncate=False)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")


val zero_shot = PretrainedZeroShotMultiTask.pretrained("zeroshot_multitask_deid_cda_large", "en", "clinical/models")
    .setInputCols("sentence")
    .setOutputCol("extractions")
    .setEntityThreshold(0.4)
    .setEntities(Array(
         "PERSON_NAME",
        "DATE_TIME",
        "STREET",
        "CITY",
        "STATE",
        "ID"
    ))

val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    zero_shot
))

val text = f"""
<recordTarget xmlns="urn:hl7-org:v3" xmlns:sdtc="urn:hl7-org:sdtc">
    <patientRole>
      <id extension="T-10118" root="2.16.840.1.113883.4.1" />
      <addr use="HP">
        <streetAddressLine>1357 Amber Dr</streetAddressLine>
        <city>Beaverton</city>
        <state>OR</state>
        <postalCode>97006</postalCode>
        <country>US</country>
      </addr>
      <telecom use="MC" value="tel:+1(555)-777-1234" />
      <telecom use="HP" value="tel:+1(555)-723-1544" />
      <telecom value="360mu.alice.newman@gmail.com" />
      <patient>
        <name use="L">
          <given>Alice</given>
          <given>Jones</given>
          <family>Newman</family>
        </name>
        <name>
          <given qualifier="BR">Alicia</given>
          <family>Newman</family>
        </name>
        <administrativeGenderCode code="F" codeSystem="2.16.840.1.113883.5.1" codeSystemName="AdministrativeGender" displayName="Female" />
        <birthTime value="19700501" />
        
    
<entry xmlns="urn:hl7-org:v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" typeCode="DRIV">
            <act classCode="ACT" moodCode="EVN">
              <templateId extension="2015-08-01" root="2.16.840.1.113883.10.20.22.4.30" />
              <templateId root="2.16.840.1.113883.10.20.22.4.30" />
              <id root="b03805bd-2eb6-4ab8-a9ff-473c6653971a" />
              <code code="CONC" codeSystem="2.16.840.1.113883.5.6" />
              <statusCode code="active" />
              <effectiveTime>
                <low value="19800510" />
              </effectiveTime>
              <entryRelationship typeCode="SUBJ">
                <observation classCode="OBS" moodCode="EVN">
                  <templateId extension="2014-06-09" root="2.16.840.1.113883.10.20.22.4.7" />
                  <templateId root="2.16.840.1.113883.10.20.22.4.7" />
                  <id root="4adc1020-7b14-11db-9fe1-0800200c9a68" />
                  <code code="ASSERTION" codeSystem="2.16.840.1.113883.5.4" />
                  <statusCode code="completed" />
                  <effectiveTime>
                    <low value="19800510" />
                  </effectiveTime>
                  <value code="419511003" codeSystem="2.16.840.1.113883.6.96" codeSystemName="SNOMED CT" displayName="Propensity to adverse reaction to drug" xsi:type="CD" />
                  <participant typeCode="CSM">
                    <participantRole classCode="MANU">
                      <playingEntity classCode="MMAT">
                        <code code="733" codeSystem="2.16.840.1.113883.6.88" codeSystemName="RxNorm" displayName="Ampicillin">
                          <originalText>
                            <reference value="#product2" />
                          </originalText>
                        </code>
                      </playingEntity>
                    </participantRole>
                  </participant>
                  <entryRelationship inversionInd="true" typeCode="MFST">
                    <observation classCode="OBS" moodCode="EVN">
                      <templateId extension="2014-06-09" root="2.16.840.1.113883.10.20.22.4.9" />
                      <templateId root="2.16.840.1.113883.10.20.22.4.9" />
                      <id root="4adc1020-7b14-11db-9fe1-0800200c9a69" />
                      <code code="ASSERTION" codeSystem="2.16.840.1.113883.5.4" />
                      <text>
                        <reference value="#reaction2" />
                      </text>
                      <statusCode code="completed" />
                      <effectiveTime>
                        <low nullFlavor="NI" />
                        <high nullFlavor="NI" />
                      </effectiveTime>
                      <value code="247472004" codeSystem="2.16.840.1.113883.6.96" displayName="Hives" xsi:type="CD" />
                      <entryRelationship inversionInd="true" typeCode="SUBJ">
                        <observation classCode="OBS" moodCode="EVN">
"""

val data = Seq(text).toDF("text")

val results = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
Entities
|    |   idx |   begin |   end | chunk                                |   sentence | ner_source   | entity      |   confidence |
|---:|------:|--------:|------:|:-------------------------------------|-----------:|:-------------|:------------|-------------:|
|  0 |     0 |       0 |     4 | alice                                |          2 | extractions  | PERSON_NAME |     0.985962 |
|  1 |     0 |      57 |    69 | 1357 Amber Dr                        |          1 | extractions  | STREET      |     0.999803 |
|  2 |     0 |     105 |   113 | Beaverton                            |          1 | extractions  | CITY        |     1        |
|  3 |     0 |     107 |   113 | T-10118                              |          0 | extractions  | ID          |     0.963742 |
|  4 |     0 |     109 |   116 | 19800510                             |          7 | extractions  | DATE_TIME   |     0.999946 |
|  5 |     0 |     124 |   131 | 19800510                             |          8 | extractions  | DATE_TIME   |     0.999957 |
|  6 |     0 |     127 |   132 | Newman                               |          4 | extractions  | STREET      |     0.680482 |
|  7 |     0 |     168 |   172 | 97006                                |          1 | extractions  | ID          |     0.995799 |
|  8 |     0 |     204 |   205 | US                                   |          1 | extractions  | STATE       |     1        |
|  9 |     0 |     239 |   244 | Newman                               |          4 | extractions  | PERSON_NAME |     0.998595 |
| 10 |     0 |     305 |   314 | 2015-08-01                           |          6 | extractions  | DATE_TIME   |     0.779459 |
| 11 |     0 |     322 |   322 | 1                                    |          9 | extractions  | ID          |     0.872957 |
| 12 |     0 |     387 |   395 | 247472004                            |         11 | extractions  | ID          |     0.850107 |
| 13 |     0 |     526 |   535 | 2014-06-09                           |         10 | extractions  | DATE_TIME   |     0.996584 |
| 14 |     0 |     686 |   721 | 4adc1020-7b14-11db-9fe1-0800200c9a69 |         10 | extractions  | ID          |     0.769531 |


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_multitask_deid_cda_large|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.0 GB|