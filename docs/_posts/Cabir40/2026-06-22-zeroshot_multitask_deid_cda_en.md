---
layout: model
title: ZeroShot Multitask - CDA/XML PHI Deidentification
author: John Snow Labs
name: zeroshot_multitask_deid_cda
date: 2026-06-22
tags: [en, licensed, clinical, multitask, zeroshot, ner, onnx]
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_multitask_deid_cda_en_6.4.0_3.0_1782130653638.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_multitask_deid_cda_en_6.4.0_3.0_1782130653638.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

zero_shot = PretrainedZeroShotMultiTask.pretrained("zeroshot_multitask_deid_cda", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("extractions")\
    .setEntityThreshold(0.4)\
    .setEntities([
        "PERSON::All mentions of person names, including patients, providers, family members, or other individuals named in the record",
        "DATE::Dates in any format, including birth dates, encounter dates, and other chronological references",
        "ADDRESS::Street addresses, cities, states, postal codes, or other location identifiers",
        "PHONE::Telephone numbers in any format, including extensions and international codes",
    ])

pipeline = Pipeline(
    stages = [
        document_assembler,
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

zero_shot = medical.PretrainedZeroShotMultiTask.pretrained("zeroshot_multitask_deid_cda", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("extractions")\
    .setEntityThreshold(0.4)\
    .setEntities([
        "PERSON::All mentions of person names, including patients, providers, family members, or other individuals named in the record",
        "DATE::Dates in any format, including birth dates, encounter dates, and other chronological references",
        "ADDRESS::Street addresses, cities, states, postal codes, or other location identifiers",
        "PHONE::Telephone numbers in any format, including extensions and international codes",
    ])

pipeline = nlp.Pipeline(
    stages = [
        document_assembler,
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

val zero_shot = PretrainedZeroShotMultiTask.pretrained("zeroshot_multitask_deid_cda", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("extractions")
    .setEntityThreshold(0.4)
    .setEntities(Array(
        "PERSON::All mentions of person names, including patients, providers, family members, or other individuals named in the record",
        "DATE::Dates in any format, including birth dates, encounter dates, and other chronological references",
        "ADDRESS::Street addresses, cities, states, postal codes, or other location identifiers",
        "PHONE::Telephone numbers in any format, including extensions and international codes"
    ))

val pipeline = new Pipeline().setStages(Array(
    document_assembler,
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
|    |   idx |   begin |   end | chunk      |   sentence | ner_source   | entity   |   confidence |
|---:|------:|--------:|------:|:-----------|-----------:|:-------------|:---------|-------------:|
|  0 |     0 |     108 |   114 | T-10118    |          0 | extractions  | PHONE    |     0.406762 |
|  1 |     0 |    1182 |  1191 | 2015-08-01 |          0 | extractions  | DATE     |     0.988932 |
|  2 |     0 |    1540 |  1547 | 19800510   |          0 | extractions  | PERSON   |     0.783176 |
|  3 |     0 |    2124 |  2131 | 19800510   |          0 | extractions  | ADDRESS  |     0.82408  |


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_multitask_deid_cda|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|844.5 MB|