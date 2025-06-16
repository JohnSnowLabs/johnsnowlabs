---
layout: model
title: Named Entity Recognition Profiling (De-Identification)
author: John Snow Labs
name: ner_profiling_deidentification
date: 2025-06-16
tags: [licensed, en, clinical, profiling, ner_profiling, ner, deid, de_identification]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 6.0.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed for deidentification in clinical texts, leveraging a range of pretrained NER models tailored for extracting and anonymizing sensitive information. By integrating these models, the pipeline provides a comprehensive solution for protecting patient privacy and complying with data protection regulations.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_profiling_deidentification_en_6.0.0_3.0_1750049032078.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_profiling_deidentification_en_6.0.0_3.0_1750049032078.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_profiling_pipeline = PretrainedPipeline("ner_profiling_deidentification", "en", "clinical/models")

text = """Name : Hendrickson, Ora, Record date: 2093-01-13, Age: 25, # 719435. Dr. John Green, ID: 1231511863, IP 203.120.223.13. He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93. Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no:A334455B. Phone (302) 786-5227, 0295 Keats Street, San Francisco."""

ner_profiling_pipeline_result = ner_profiling_pipeline.fullAnnotate(text)[0]


```

{:.jsl-block}
```python

ner_profiling_pipeline = nlp.PretrainedPipeline("ner_profiling_deidentification", "en", "clinical/models")

text = """Name : Hendrickson, Ora, Record date: 2093-01-13, Age: 25, # 719435. Dr. John Green, ID: 1231511863, IP 203.120.223.13. He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93. Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no:A334455B. Phone (302) 786-5227, 0295 Keats Street, San Francisco."""

ner_profiling_pipeline_result = ner_profiling_pipeline.fullAnnotate(text)[0]



```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_profiling_pipeline = PretrainedPipeline("ner_profiling_deidentification", "en", "clinical/models")

val text = """Name : Hendrickson, Ora, Record date: 2093-01-13, Age: 25, # 719435. Dr. John Green, ID: 1231511863, IP 203.120.223.13. He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93. Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no:A334455B. Phone (302) 786-5227, 0295 Keats Street, San Francisco."""

val ner_profiling_pipeline_result = ner_profiling_pipeline.fullAnnotate(text)[0]


```
</div>

## Results

```bash

 ******************** ner_deid_augmented Model Results ******************** 

[('Name', 'O'), (':', 'O'), ('Hendrickson', 'B-NAME'), (',', 'I-NAME'), ('Ora', 'I-NAME'), (',', 'O'), ('Record', 'O'), ('date', 'O'), (':', 'O'), ('2093-01-13', 'B-DATE'), (',', 'O'), ('Age', 'O'), (':', 'O'), ('25', 'B-AGE'), (',', 'O'), ('#', 'O'), ('719435', 'B-CONTACT'), ('.', 'O'), ('Dr', 'O'), ('.', 'O'), ('John', 'B-NAME'), ('Green', 'I-NAME'), (',', 'O'), ('ID', 'O'), (':', 'O'), ('1231511863', 'B-ID'), (',', 'O'), ('IP', 'B-CONTACT'), ('203.120.223.13', 'I-CONTACT'), ('.', 'O'), ('He', 'O'), ('is', 'O'), ('a', 'O'), ('60-year-old', 'O'), ('male', 'O'), ('was', 'O'), ('admitted', 'O'), ('to', 'O'), ('the', 'O'), ('Day', 'B-LOCATION'), ('Hospital', 'I-LOCATION'), ('for', 'O'), ('cystectomy', 'O'), ('on', 'O'), ('01/13/93', 'B-DATE'), ('.', 'O'), ("Patient's", 'O'), ('VIN', 'O'), (':', 'O'), ('1HGBH41JXMN109286', 'B-ID'), (',', 'O'), ('SSN', 'O'), ('#333-44-6666', 'O'), (',', 'O'), ("Driver's", 'O'), ('license', 'O'), ('no:A334455B', 'O'), ('.', 'O'), ('Phone', 'O'), ('(', 'B-CONTACT'), ('302', 'I-CONTACT'), (')', 'I-CONTACT'), ('786-5227', 'I-CONTACT'), (',', 'O'), ('0295', 'B-LOCATION'), ('Keats', 'I-LOCATION'), ('Street', 'I-LOCATION'), (',', 'O'), ('San', 'B-LOCATION'), ('Francisco', 'I-LOCATION'), ('.', 'O')]


 ******************** ner_deid_subentity_augmented_i2b2 Model Results ******************** 

[('Name', 'O'), (':', 'O'), ('Hendrickson', 'B-PATIENT'), (',', 'I-PATIENT'), ('Ora', 'I-PATIENT'), (',', 'O'), ('Record', 'O'), ('date', 'O'), (':', 'O'), ('2093-01-13', 'B-DATE'), (',', 'O'), ('Age', 'O'), (':', 'O'), ('25', 'B-AGE'), (',', 'O'), ('#', 'O'), ('719435', 'B-ZIP'), ('.', 'O'), ('Dr', 'O'), ('.', 'O'), ('John', 'B-DOCTOR'), ('Green', 'I-DOCTOR'), (',', 'O'), ('ID', 'O'), (':', 'B-IDNUM'), ('1231511863', 'I-IDNUM'), (',', 'O'), ('IP', 'O'), ('203.120.223.13', 'B-PHONE'), ('.', 'O'), ('He', 'O'), ('is', 'O'), ('a', 'O'), ('60-year-old', 'O'), ('male', 'O'), ('was', 'O'), ('admitted', 'O'), ('to', 'O'), ('the', 'O'), ('Day', 'O'), ('Hospital', 'O'), ('for', 'O'), ('cystectomy', 'O'), ('on', 'O'), ('01/13/93', 'B-DATE'), ('.', 'O'), ("Patient's", 'O'), ('VIN', 'O'), (':', 'O'), ('1HGBH41JXMN109286', 'B-IDNUM'), (',', 'O'), ('SSN', 'O'), ('#333-44-6666', 'B-PHONE'), (',', 'O'), ("Driver's", 'O'), ('license', 'O'), ('no:A334455B', 'B-IDNUM'), ('.', 'O'), ('Phone', 'O'), ('(', 'B-PHONE'), ('302', 'I-PHONE'), (')', 'I-PHONE'), ('786-5227', 'I-PHONE'), (',', 'O'), ('0295', 'B-STREET'), ('Keats', 'I-STREET'), ('Street', 'I-STREET'), (',', 'O'), ('San', 'B-CITY'), ('Francisco', 'I-CITY'), ('.', 'O')]


 ******************** ner_deidentify_dl Model Results ******************** 

[('Name', 'O'), (':', 'O'), ('Hendrickson', 'B-PATIENT'), (',', 'I-PATIENT'), ('Ora', 'I-PATIENT'), (',', 'O'), ('Record', 'O'), ('date', 'O'), (':', 'O'), ('2093-01-13', 'B-DATE'), (',', 'O'), ('Age', 'O'), (':', 'O'), ('25', 'B-AGE'), (',', 'O'), ('#', 'O'), ('719435', 'B-PHONE'), ('.', 'O'), ('Dr', 'O'), ('.', 'O'), ('John', 'B-DOCTOR'), ('Green', 'I-DOCTOR'), (',', 'O'), ('ID', 'O'), (':', 'O'), ('1231511863', 'B-IDNUM'), (',', 'O'), ('IP', 'O'), ('203.120.223.13', 'O'), ('.', 'O'), ('He', 'O'), ('is', 'O'), ('a', 'O'), ('60-year-old', 'O'), ('male', 'O'), ('was', 'O'), ('admitted', 'O'), ('to', 'O'), ('the', 'O'), ('Day', 'B-HOSPITAL'), ('Hospital', 'I-HOSPITAL'), ('for', 'O'), ('cystectomy', 'O'), ('on', 'O'), ('01/13/93', 'B-DATE'), ('.', 'O'), ("Patient's", 'O'), ('VIN', 'O'), (':', 'O'), ('1HGBH41JXMN109286', 'O'), (',', 'O'), ('SSN', 'O'), ('#333-44-6666', 'O'), (',', 'O'), ("Driver's", 'O'), ('license', 'O'), ('no:A334455B', 'B-IDNUM'), ('.', 'O'), ('Phone', 'O'), ('(', 'B-PHONE'), ('302', 'I-PHONE'), (')', 'I-PHONE'), ('786-5227', 'I-PHONE'), (',', 'O'), ('0295', 'B-STREET'), ('Keats', 'I-STREET'), ('Street', 'I-STREET'), (',', 'O'), ('San', 'B-CITY'), ('Francisco', 'I-CITY'), ('.', 'I-CITY')]


 ******************** ner_deid_subentity_augmented_langtest Model Results ******************** 

[('Name', 'O'), (':', 'O'), ('Hendrickson', 'B-PATIENT'), (',', 'I-PATIENT'), ('Ora', 'I-PATIENT'), (',', 'O'), ('Record', 'O'), ('date', 'O'), (':', 'O'), ('2093-01-13', 'B-DATE'), (',', 'O'), ('Age', 'O'), (':', 'O'), ('25', 'B-AGE'), (',', 'O'), ('#', 'O'), ('719435', 'B-PHONE'), ('.', 'O'), ('Dr', 'O'), ('.', 'O'), ('John', 'B-DOCTOR'), ('Green', 'I-DOCTOR'), (',', 'O'), ('ID', 'O'), (':', 'O'), ('1231511863', 'B-IDNUM'), (',', 'O'), ('IP', 'O'), ('203.120.223.13', 'B-PHONE'), ('.', 'O'), ('He', 'O'), ('is', 'O'), ('a', 'O'), ('60-year-old', 'B-AGE'), ('male', 'O'), ('was', 'O'), ('admitted', 'O'), ('to', 'O'), ('the', 'O'), ('Day', 'B-HOSPITAL'), ('Hospital', 'I-HOSPITAL'), ('for', 'O'), ('cystectomy', 'O'), ('on', 'O'), ('01/13/93', 'B-DATE'), ('.', 'O'), ("Patient's", 'O'), ('VIN', 'O'), (':', 'O'), ('1HGBH41JXMN109286', 'B-IDNUM'), (',', 'O'), ('SSN', 'O'), ('#333-44-6666', 'B-PHONE'), (',', 'O'), ("Driver's", 'O'), ('license', 'O'), ('no:A334455B', 'B-IDNUM'), ('.', 'O'), ('Phone', 'O'), ('(', 'B-PHONE'), ('302', 'I-PHONE'), (')', 'I-PHONE'), ('786-5227', 'I-PHONE'), (',', 'O'), ('0295', 'B-STREET'), ('Keats', 'I-STREET'), ('Street', 'I-STREET'), (',', 'O'), ('San', 'B-CITY'), ('Francisco', 'I-CITY'), ('.', 'O')]


 ******************** ner_deid_synthetic Model Results ******************** 

[('Name', 'O'), (':', 'O'), ('Hendrickson', 'B-NAME'), (',', 'I-NAME'), ('Ora', 'I-NAME'), (',', 'O'), ('Record', 'O'), ('date', 'O'), (':', 'O'), ('2093-01-13', 'B-DATE'), (',', 'O'), ('Age', 'O'), (':', 'O'), ('25', 'B-AGE'), (',', 'O'), ('#', 'O'), ('719435', 'B-ID'), ('.', 'O'), ('Dr', 'O'), ('.', 'O'), ('John', 'B-NAME'), ('Green', 'I-NAME'), (',', 'O'), ('ID', 'O'), (':', 'O'), ('1231511863', 'B-ID'), (',', 'O'), ('IP', 'O'), ('203.120.223.13', 'O'), ('.', 'O'), ('He', 'O'), ('is', 'O'), ('a', 'O'), ('60-year-old', 'O'), ('male', 'O'), ('was', 'O'), ('admitted', 'O'), ('to', 'O'), ('the', 'O'), ('Day', 'B-LOCATION'), ('Hospital', 'I-LOCATION'), ('for', 'O'), ('cystectomy', 'O'), ('on', 'O'), ('01/13/93', 'B-DATE'), ('.', 'O'), ("Patient's", 'O'), ('VIN', 'O'), (':', 'O'), ('1HGBH41JXMN109286', 'B-ID'), (',', 'O'), ('SSN', 'O'), ('#333-44-6666', 'O'), (',', 'O'), ("Driver's", 'O'), ('license', 'O'), ('no:A334455B', 'O'), ('.', 'O'), ('Phone', 'O'), ('(', 'B-CONTACT'), ('302', 'I-CONTACT'), (')', 'O'), ('786-5227', 'B-CONTACT'), (',', 'O'), ('0295', 'B-LOCATION'), ('Keats', 'I-LOCATION'), ('Street', 'I-LOCATION'), (',', 'O'), ('San', 'B-LOCATION'), ('Francisco', 'I-LOCATION'), ('.', 'O')]


 ******************** ner_deid_aipii Model Results ******************** 

[('Name', 'O'), (':', 'O'), ('Hendrickson', 'B-NAME'), (',', 'O'), ('Ora', 'O'), (',', 'O'), ('Record', 'O'), ('date', 'O'), (':', 'O'), ('2093-01-13', 'B-SSN'), (',', 'O'), ('Age', 'O'), (':', 'O'), ('25', 'O'), (',', 'O'), ('#', 'O'), ('719435', 'O'), ('.', 'O'), ('Dr', 'O'), ('.', 'O'), ('John', 'B-STREET'), ('Green', 'I-STREET'), (',', 'O'), ('ID', 'O'), (':', 'O'), ('1231511863', 'B-IDNUM'), (',', 'O'), ('IP', 'O'), ('203.120.223.13', 'B-SSN'), ('.', 'O'), ('He', 'O'), ('is', 'O'), ('a', 'O'), ('60-year-old', 'O'), ('male', 'O'), ('was', 'O'), ('admitted', 'O'), ('to', 'O'), ('the', 'O'), ('Day', 'O'), ('Hospital', 'O'), ('for', 'O'), ('cystectomy', 'O'), ('on', 'O'), ('01/13/93', 'O'), ('.', 'O'), ("Patient's", 'O'), ('VIN', 'O'), (':', 'O'), ('1HGBH41JXMN109286', 'O'), (',', 'O'), ('SSN', 'O'), ('#333-44-6666', 'O'), (',', 'O'), ("Driver's", 'O'), ('license', 'O'), ('no:A334455B', 'O'), ('.', 'O'), ('Phone', 'O'), ('(', 'B-PHONE'), ('302', 'I-PHONE'), (')', 'I-PHONE'), ('786-5227', 'I-PHONE'), (',', 'O'), ('0295', 'B-STREET'), ('Keats', 'I-STREET'), ('Street', 'I-STREET'), (',', 'O'), ('San', 'B-CITY'), ('Francisco', 'I-CITY'), ('.', 'O')]


 ******************** ner_deid_large_langtest Model Results ******************** 

[('Name', 'O'), (':', 'O'), ('Hendrickson', 'B-NAME'), (',', 'I-NAME'), ('Ora', 'I-NAME'), (',', 'O'), ('Record', 'O'), ('date', 'O'), (':', 'O'), ('2093-01-13', 'B-DATE'), (',', 'O'), ('Age', 'O'), (':', 'O'), ('25', 'B-AGE'), (',', 'O'), ('#', 'O'), ('719435', 'B-CONTACT'), ('.', 'O'), ('Dr', 'O'), ('.', 'O'), ('John', 'B-NAME'), ('Green', 'I-NAME'), (',', 'O'), ('ID', 'O'), (':', 'O'), ('1231511863', 'B-ID'), (',', 'O'), ('IP', 'O'), ('203.120.223.13', 'O'), ('.', 'O'), ('He', 'O'), ('is', 'O'), ('a', 'O'), ('60-year-old', 'O'), ('male', 'O'), ('was', 'O'), ('admitted', 'O'), ('to', 'O'), ('the', 'O'), ('Day', 'B-LOCATION'), ('Hospital', 'I-LOCATION'), ('for', 'O'), ('cystectomy', 'O'), ('on', 'O'), ('01/13/93', 'B-DATE'), ('.', 'O'), ("Patient's", 'O'), ('VIN', 'O'), (':', 'O'), ('1HGBH41JXMN109286', 'B-ID'), (',', 'O'), ('SSN', 'O'), ('#333-44-6666', 'O'), (',', 'O'), ("Driver's", 'O'), ('license', 'O'), ('no:A334455B', 'B-ID'), ('.', 'O'), ('Phone', 'O'), ('(', 'B-CONTACT'), ('302', 'I-CONTACT'), (')', 'I-CONTACT'), ('786-5227', 'I-CONTACT'), (',', 'O'), ('0295', 'B-LOCATION'), ('Keats', 'I-LOCATION'), ('Street', 'I-LOCATION'), (',', 'O'), ('San', 'B-LOCATION'), ('Francisco', 'I-LOCATION'), ('.', 'O')]


 ******************** ner_deid_large Model Results ******************** 

[('Name', 'O'), (':', 'O'), ('Hendrickson', 'B-NAME'), (',', 'I-NAME'), ('Ora', 'I-NAME'), (',', 'O'), ('Record', 'O'), ('date', 'O'), (':', 'O'), ('2093-01-13', 'B-DATE'), (',', 'O'), ('Age', 'O'), (':', 'O'), ('25', 'B-AGE'), (',', 'O'), ('#', 'O'), ('719435', 'B-CONTACT'), ('.', 'O'), ('Dr', 'O'), ('.', 'O'), ('John', 'B-NAME'), ('Green', 'I-NAME'), (',', 'O'), ('ID', 'O'), (':', 'O'), ('1231511863', 'B-ID'), (',', 'O'), ('IP', 'O'), ('203.120.223.13', 'O'), ('.', 'O'), ('He', 'O'), ('is', 'O'), ('a', 'O'), ('60-year-old', 'O'), ('male', 'O'), ('was', 'O'), ('admitted', 'O'), ('to', 'O'), ('the', 'O'), ('Day', 'B-LOCATION'), ('Hospital', 'I-LOCATION'), ('for', 'O'), ('cystectomy', 'O'), ('on', 'O'), ('01/13/93', 'B-DATE'), ('.', 'O'), ("Patient's", 'O'), ('VIN', 'O'), (':', 'O'), ('1HGBH41JXMN109286', 'B-ID'), (',', 'O'), ('SSN', 'O'), ('#333-44-6666', 'O'), (',', 'O'), ("Driver's", 'O'), ('license', 'O'), ('no:A334455B', 'O'), ('.', 'O'), ('Phone', 'O'), ('(', 'B-CONTACT'), ('302', 'I-CONTACT'), (')', 'I-CONTACT'), ('786-5227', 'I-CONTACT'), (',', 'O'), ('0295', 'B-LOCATION'), ('Keats', 'I-LOCATION'), ('Street', 'I-LOCATION'), (',', 'O'), ('San', 'B-LOCATION'), ('Francisco', 'I-LOCATION'), ('.', 'O')]


 ******************** ner_deid_subentity_docwise Model Results ******************** 

[('Name', 'O'), (':', 'O'), ('Hendrickson', 'B-PATIENT'), (',', 'I-PATIENT'), ('Ora', 'I-PATIENT'), (',', 'O'), ('Record', 'O'), ('date', 'O'), (':', 'O'), ('2093-01-13', 'B-DATE'), (',', 'O'), ('Age', 'O'), (':', 'O'), ('25', 'B-AGE'), (',', 'O'), ('#', 'O'), ('719435', 'B-DEVICE'), ('.', 'O'), ('Dr', 'O'), ('.', 'O'), ('John', 'B-DOCTOR'), ('Green', 'I-DOCTOR'), (',', 'O'), ('ID', 'O'), (':', 'O'), ('1231511863', 'B-IDNUM'), (',', 'O'), ('IP', 'O'), ('203.120.223.13', 'B-DATE'), ('.', 'O'), ('He', 'O'), ('is', 'O'), ('a', 'O'), ('60-year-old', 'B-AGE'), ('male', 'O'), ('was', 'O'), ('admitted', 'O'), ('to', 'O'), ('the', 'O'), ('Day', 'O'), ('Hospital', 'O'), ('for', 'O'), ('cystectomy', 'O'), ('on', 'O'), ('01/13/93', 'B-DATE'), ('.', 'O'), ("Patient's", 'O'), ('VIN', 'O'), (':', 'O'), ('1HGBH41JXMN109286', 'B-IDNUM'), (',', 'O'), ('SSN', 'O'), ('#333-44-6666', 'O'), (',', 'O'), ("Driver's", 'O'), ('license', 'O'), ('no:A334455B', 'B-IDNUM'), ('.', 'O'), ('Phone', 'O'), ('(', 'B-PHONE'), ('302', 'I-PHONE'), (')', 'I-PHONE'), ('786-5227', 'I-PHONE'), (',', 'O'), ('0295', 'B-STREET'), ('Keats', 'I-STREET'), ('Street', 'I-STREET'), (',', 'O'), ('San', 'B-CITY'), ('Francisco', 'I-CITY'), ('.', 'O')]


 ******************** ner_deid_subentity_augmented_v2 Model Results ******************** 

[('Name', 'O'), (':', 'O'), ('Hendrickson', 'B-PATIENT'), (',', 'I-PATIENT'), ('Ora', 'I-PATIENT'), (',', 'O'), ('Record', 'O'), ('date', 'O'), (':', 'O'), ('2093-01-13', 'B-DATE'), (',', 'O'), ('Age', 'O'), (':', 'O'), ('25', 'B-AGE'), (',', 'O'), ('#', 'O'), ('719435', 'B-PHONE'), ('.', 'O'), ('Dr', 'O'), ('.', 'O'), ('John', 'B-DOCTOR'), ('Green', 'I-DOCTOR'), (',', 'O'), ('ID', 'O'), (':', 'O'), ('1231511863', 'B-IDNUM'), (',', 'O'), ('IP', 'O'), ('203.120.223.13', 'B-USERNAME'), ('.', 'O'), ('He', 'O'), ('is', 'O'), ('a', 'O'), ('60-year-old', 'B-AGE'), ('male', 'O'), ('was', 'O'), ('admitted', 'O'), ('to', 'O'), ('the', 'O'), ('Day', 'B-HOSPITAL'), ('Hospital', 'I-HOSPITAL'), ('for', 'O'), ('cystectomy', 'O'), ('on', 'O'), ('01/13/93', 'B-DATE'), ('.', 'O'), ("Patient's", 'O'), ('VIN', 'O'), (':', 'O'), ('1HGBH41JXMN109286', 'B-IDNUM'), (',', 'O'), ('SSN', 'O'), ('#333-44-6666', 'B-IDNUM'), (',', 'O'), ("Driver's", 'O'), ('license', 'O'), ('no:A334455B', 'B-PHONE'), ('.', 'O'), ('Phone', 'O'), ('(', 'B-PHONE'), ('302', 'I-PHONE'), (')', 'I-PHONE'), ('786-5227', 'I-PHONE'), (',', 'O'), ('0295', 'B-STREET'), ('Keats', 'I-STREET'), ('Street', 'I-STREET'), (',', 'O'), ('San', 'B-STATE'), ('Francisco', 'I-STATE'), ('.', 'O')]


 ******************** ner_deid_subentity_augmented_docwise Model Results ******************** 

[('Name', 'O'), (':', 'O'), ('Hendrickson', 'B-PATIENT'), (',', 'I-PATIENT'), ('Ora', 'I-PATIENT'), (',', 'O'), ('Record', 'O'), ('date', 'O'), (':', 'O'), ('2093-01-13', 'B-DATE'), (',', 'O'), ('Age', 'O'), (':', 'O'), ('25', 'B-AGE'), (',', 'O'), ('#', 'O'), ('719435', 'B-PHONE'), ('.', 'O'), ('Dr', 'O'), ('.', 'O'), ('John', 'B-DOCTOR'), ('Green', 'I-DOCTOR'), (',', 'O'), ('ID', 'O'), (':', 'O'), ('1231511863', 'B-IDNUM'), (',', 'O'), ('IP', 'O'), ('203.120.223.13', 'B-PHONE'), ('.', 'O'), ('He', 'O'), ('is', 'O'), ('a', 'O'), ('60-year-old', 'B-AGE'), ('male', 'O'), ('was', 'O'), ('admitted', 'O'), ('to', 'O'), ('the', 'O'), ('Day', 'B-HOSPITAL'), ('Hospital', 'I-HOSPITAL'), ('for', 'O'), ('cystectomy', 'O'), ('on', 'O'), ('01/13/93', 'B-DATE'), ('.', 'O'), ("Patient's", 'O'), ('VIN', 'O'), (':', 'O'), ('1HGBH41JXMN109286', 'B-IDNUM'), (',', 'O'), ('SSN', 'O'), ('#333-44-6666', 'B-IDNUM'), (',', 'O'), ("Driver's", 'O'), ('license', 'O'), ('no:A334455B', 'B-PHONE'), ('.', 'O'), ('Phone', 'O'), ('(', 'B-PHONE'), ('302', 'I-PHONE'), (')', 'I-PHONE'), ('786-5227', 'I-PHONE'), (',', 'O'), ('0295', 'B-LOCATION'), ('Keats', 'I-LOCATION'), ('Street', 'I-LOCATION'), (',', 'I-LOCATION'), ('San', 'I-LOCATION'), ('Francisco', 'I-LOCATION'), ('.', 'O')]


 ******************** zeroshot_ner_deid_subentity_merged_medium Model Results ******************** 

[('Name', 'O'), (':', 'O'), ('Hendrickson', 'B-PATIENT'), (',', 'I-PATIENT'), ('Ora', 'I-PATIENT'), (',', 'O'), ('Record', 'O'), ('date', 'O'), (':', 'O'), ('2093-01-13', 'B-DATE'), (',', 'O'), ('Age', 'O'), (':', 'O'), ('25', 'B-AGE'), (',', 'O'), ('#', 'O'), ('719435', 'B-IDNUM'), ('.', 'O'), ('Dr', 'O'), ('.', 'O'), ('John', 'B-DOCTOR'), ('Green', 'I-DOCTOR'), (',', 'O'), ('ID', 'O'), (':', 'O'), ('1231511863', 'B-IDNUM'), (',', 'O'), ('IP', 'O'), ('203.120.223.13', 'O'), ('.', 'O'), ('He', 'O'), ('is', 'O'), ('a', 'O'), ('60-year-old', 'B-AGE'), ('male', 'O'), ('was', 'O'), ('admitted', 'O'), ('to', 'O'), ('the', 'O'), ('Day', 'B-HOSPITAL'), ('Hospital', 'I-HOSPITAL'), ('for', 'O'), ('cystectomy', 'O'), ('on', 'O'), ('01/13/93', 'B-DATE'), ('.', 'O'), ("Patient's", 'O'), ('VIN', 'O'), (':', 'O'), ('1HGBH41JXMN109286', 'B-IDNUM'), (',', 'O'), ('SSN', 'O'), ('#333-44-6666', 'O'), (',', 'O'), ("Driver's", 'O'), ('license', 'O'), ('no:A334455B', 'O'), ('.', 'O'), ('Phone', 'O'), ('(', 'B-PHONE'), ('302', 'I-PHONE'), (')', 'I-PHONE'), ('786-5227', 'I-PHONE'), (',', 'O'), ('0295', 'B-STREET'), ('Keats', 'I-STREET'), ('Street', 'I-STREET'), (',', 'O'), ('San', 'B-CITY'), ('Francisco', 'I-CITY'), ('.', 'O')]


 ******************** ner_deid_sd_large Model Results ******************** 

[('Name', 'O'), (':', 'O'), ('Hendrickson', 'B-NAME'), (',', 'I-NAME'), ('Ora', 'I-NAME'), (',', 'O'), ('Record', 'O'), ('date', 'O'), (':', 'O'), ('2093-01-13', 'B-DATE'), (',', 'O'), ('Age', 'O'), (':', 'O'), ('25', 'B-AGE'), (',', 'O'), ('#', 'O'), ('719435', 'B-ID'), ('.', 'O'), ('Dr', 'O'), ('.', 'O'), ('John', 'B-NAME'), ('Green', 'I-NAME'), (',', 'O'), ('ID', 'O'), (':', 'O'), ('1231511863', 'B-ID'), (',', 'O'), ('IP', 'O'), ('203.120.223.13', 'O'), ('.', 'O'), ('He', 'O'), ('is', 'O'), ('a', 'O'), ('60-year-old', 'O'), ('male', 'O'), ('was', 'O'), ('admitted', 'O'), ('to', 'O'), ('the', 'O'), ('Day', 'B-LOCATION'), ('Hospital', 'I-LOCATION'), ('for', 'O'), ('cystectomy', 'O'), ('on', 'O'), ('01/13/93', 'B-DATE'), ('.', 'O'), ("Patient's", 'O'), ('VIN', 'O'), (':', 'O'), ('1HGBH41JXMN109286', 'O'), (',', 'O'), ('SSN', 'O'), ('#333-44-6666', 'O'), (',', 'O'), ("Driver's", 'O'), ('license', 'O'), ('no:A334455B', 'O'), ('.', 'O'), ('Phone', 'O'), ('(', 'O'), ('302', 'O'), (')', 'O'), ('786-5227', 'I-CONTACT'), (',', 'O'), ('0295', 'B-LOCATION'), ('Keats', 'I-LOCATION'), ('Street', 'I-LOCATION'), (',', 'O'), ('San', 'B-LOCATION'), ('Francisco', 'I-LOCATION'), ('.', 'O')]


 ******************** ner_deid_enriched_langtest Model Results ******************** 

[('Name', 'O'), (':', 'O'), ('Hendrickson', 'B-PATIENT'), (',', 'I-PATIENT'), ('Ora', 'I-PATIENT'), (',', 'O'), ('Record', 'O'), ('date', 'O'), (':', 'O'), ('2093-01-13', 'B-DATE'), (',', 'O'), ('Age', 'O'), (':', 'O'), ('25', 'B-AGE'), (',', 'O'), ('#', 'O'), ('719435', 'B-PHONE'), ('.', 'O'), ('Dr', 'O'), ('.', 'O'), ('John', 'B-DOCTOR'), ('Green', 'I-DOCTOR'), (',', 'O'), ('ID', 'O'), (':', 'O'), ('1231511863', 'B-IDNUM'), (',', 'O'), ('IP', 'O'), ('203.120.223.13', 'O'), ('.', 'O'), ('He', 'O'), ('is', 'O'), ('a', 'O'), ('60-year-old', 'O'), ('male', 'O'), ('was', 'O'), ('admitted', 'O'), ('to', 'O'), ('the', 'O'), ('Day', 'O'), ('Hospital', 'O'), ('for', 'O'), ('cystectomy', 'O'), ('on', 'O'), ('01/13/93', 'B-DATE'), ('.', 'O'), ("Patient's", 'O'), ('VIN', 'O'), (':', 'O'), ('1HGBH41JXMN109286', 'B-IDNUM'), (',', 'O'), ('SSN', 'O'), ('#333-44-6666', 'O'), (',', 'O'), ("Driver's", 'O'), ('license', 'O'), ('no:A334455B', 'O'), ('.', 'O'), ('Phone', 'O'), ('(', 'B-PHONE'), ('302', 'I-PHONE'), (')', 'I-PHONE'), ('786-5227', 'I-PHONE'), (',', 'O'), ('0295', 'B-STREET'), ('Keats', 'I-STREET'), ('Street', 'I-STREET'), (',', 'O'), ('San', 'B-CITY'), ('Francisco', 'I-CITY'), ('.', 'O')]


 ******************** token Model Results ******************** 

[('Name', 'Name'), (':', ':'), ('Hendrickson', 'Hendrickson'), (',', ','), ('Ora', 'Ora'), (',', ','), ('Record', 'Record'), ('date', 'date'), (':', ':'), ('2093-01-13', '2093-01-13'), (',', ','), ('Age', 'Age'), (':', ':'), ('25', '25'), (',', ','), ('#', '#'), ('719435', '719435'), ('.', '.'), ('Dr', 'Dr'), ('.', '.'), ('John', 'John'), ('Green', 'Green'), (',', ','), ('ID', 'ID'), (':', ':'), ('1231511863', '1231511863'), (',', ','), ('IP', 'IP'), ('203.120.223.13', '203.120.223.13'), ('.', '.'), ('He', 'He'), ('is', 'is'), ('a', 'a'), ('60-year-old', '60-year-old'), ('male', 'male'), ('was', 'was'), ('admitted', 'admitted'), ('to', 'to'), ('the', 'the'), ('Day', 'Day'), ('Hospital', 'Hospital'), ('for', 'for'), ('cystectomy', 'cystectomy'), ('on', 'on'), ('01/13/93', '01/13/93'), ('.', '.'), ("Patient's", "Patient's"), ('VIN', 'VIN'), (':', ':'), ('1HGBH41JXMN109286', '1HGBH41JXMN109286'), (',', ','), ('SSN', 'SSN'), ('#333-44-6666', '#333-44-6666'), (',', ','), ("Driver's", "Driver's"), ('license', 'license'), ('no:A334455B', 'no:A334455B'), ('.', '.'), ('Phone', 'Phone'), ('(', '('), ('302', '302'), (')', ')'), ('786-5227', '786-5227'), (',', ','), ('0295', '0295'), ('Keats', 'Keats'), ('Street', 'Street'), (',', ','), ('San', 'San'), ('Francisco', 'Francisco'), ('.', '.')]


 ******************** ner_deid_sd Model Results ******************** 

[('Name', 'O'), (':', 'O'), ('Hendrickson', 'B-NAME'), (',', 'I-NAME'), ('Ora', 'I-NAME'), (',', 'O'), ('Record', 'O'), ('date', 'O'), (':', 'O'), ('2093-01-13', 'B-DATE'), (',', 'O'), ('Age', 'O'), (':', 'O'), ('25', 'B-AGE'), (',', 'O'), ('#', 'O'), ('719435', 'B-CONTACT'), ('.', 'O'), ('Dr', 'O'), ('.', 'O'), ('John', 'B-NAME'), ('Green', 'I-NAME'), (',', 'O'), ('ID', 'O'), (':', 'O'), ('1231511863', 'B-ID'), (',', 'O'), ('IP', 'O'), ('203.120.223.13', 'B-CONTACT'), ('.', 'O'), ('He', 'O'), ('is', 'O'), ('a', 'O'), ('60-year-old', 'O'), ('male', 'O'), ('was', 'O'), ('admitted', 'O'), ('to', 'O'), ('the', 'O'), ('Day', 'O'), ('Hospital', 'O'), ('for', 'O'), ('cystectomy', 'O'), ('on', 'O'), ('01/13/93', 'B-DATE'), ('.', 'O'), ("Patient's", 'O'), ('VIN', 'O'), (':', 'O'), ('1HGBH41JXMN109286', 'O'), (',', 'O'), ('SSN', 'O'), ('#333-44-6666', 'O'), (',', 'O'), ("Driver's", 'O'), ('license', 'O'), ('no:A334455B', 'O'), ('.', 'O'), ('Phone', 'O'), ('(', 'B-CONTACT'), ('302', 'I-CONTACT'), (')', 'I-CONTACT'), ('786-5227', 'I-CONTACT'), (',', 'O'), ('0295', 'B-LOCATION'), ('Keats', 'I-LOCATION'), ('Street', 'I-LOCATION'), (',', 'O'), ('San', 'B-LOCATION'), ('Francisco', 'I-LOCATION'), ('.', 'O')]


 ******************** ner_deid_generic_augmented Model Results ******************** 

[('Name', 'O'), (':', 'O'), ('Hendrickson', 'B-NAME'), (',', 'I-NAME'), ('Ora', 'I-NAME'), (',', 'O'), ('Record', 'O'), ('date', 'O'), (':', 'O'), ('2093-01-13', 'B-DATE'), (',', 'O'), ('Age', 'O'), (':', 'O'), ('25', 'B-AGE'), (',', 'O'), ('#', 'O'), ('719435', 'B-CONTACT'), ('.', 'O'), ('Dr', 'O'), ('.', 'O'), ('John', 'B-NAME'), ('Green', 'I-NAME'), (',', 'O'), ('ID', 'O'), (':', 'O'), ('1231511863', 'B-ID'), (',', 'O'), ('IP', 'O'), ('203.120.223.13', 'O'), ('.', 'O'), ('He', 'O'), ('is', 'O'), ('a', 'O'), ('60-year-old', 'B-AGE'), ('male', 'O'), ('was', 'O'), ('admitted', 'O'), ('to', 'O'), ('the', 'O'), ('Day', 'B-LOCATION'), ('Hospital', 'I-LOCATION'), ('for', 'O'), ('cystectomy', 'O'), ('on', 'O'), ('01/13/93', 'B-DATE'), ('.', 'O'), ("Patient's", 'O'), ('VIN', 'O'), (':', 'O'), ('1HGBH41JXMN109286', 'B-ID'), (',', 'O'), ('SSN', 'O'), ('#333-44-6666', 'B-ID'), (',', 'O'), ("Driver's", 'O'), ('license', 'O'), ('no:A334455B', 'B-ID'), ('.', 'O'), ('Phone', 'O'), ('(', 'B-CONTACT'), ('302', 'I-CONTACT'), (')', 'I-CONTACT'), ('786-5227', 'I-CONTACT'), (',', 'O'), ('0295', 'B-LOCATION'), ('Keats', 'I-LOCATION'), ('Street', 'I-LOCATION'), (',', 'O'), ('San', 'B-LOCATION'), ('Francisco', 'I-LOCATION'), ('.', 'O')]


 ******************** ner_deid_enriched Model Results ******************** 

[('Name', 'O'), (':', 'O'), ('Hendrickson', 'B-PATIENT'), (',', 'I-PATIENT'), ('Ora', 'I-PATIENT'), (',', 'O'), ('Record', 'O'), ('date', 'O'), (':', 'O'), ('2093-01-13', 'B-DATE'), (',', 'O'), ('Age', 'O'), (':', 'O'), ('25', 'B-AGE'), (',', 'O'), ('#', 'O'), ('719435', 'B-PHONE'), ('.', 'O'), ('Dr', 'O'), ('.', 'O'), ('John', 'B-DOCTOR'), ('Green', 'I-DOCTOR'), (',', 'O'), ('ID', 'O'), (':', 'O'), ('1231511863', 'O'), (',', 'O'), ('IP', 'O'), ('203.120.223.13', 'O'), ('.', 'O'), ('He', 'O'), ('is', 'O'), ('a', 'O'), ('60-year-old', 'O'), ('male', 'O'), ('was', 'O'), ('admitted', 'O'), ('to', 'O'), ('the', 'O'), ('Day', 'O'), ('Hospital', 'O'), ('for', 'O'), ('cystectomy', 'O'), ('on', 'O'), ('01/13/93', 'B-DATE'), ('.', 'O'), ("Patient's", 'O'), ('VIN', 'O'), (':', 'O'), ('1HGBH41JXMN109286', 'O'), (',', 'O'), ('SSN', 'O'), ('#333-44-6666', 'O'), (',', 'O'), ("Driver's", 'O'), ('license', 'O'), ('no:A334455B', 'O'), ('.', 'O'), ('Phone', 'O'), ('(', 'B-PHONE'), ('302', 'I-PHONE'), (')', 'I-PHONE'), ('786-5227', 'I-PHONE'), (',', 'O'), ('0295', 'B-STREET'), ('Keats', 'I-STREET'), ('Street', 'I-STREET'), (',', 'O'), ('San', 'B-CITY'), ('Francisco', 'I-CITY'), ('.', 'O')]


 ******************** ner_deid_generic_augmented_langtest Model Results ******************** 

[('Name', 'O'), (':', 'O'), ('Hendrickson', 'B-NAME'), (',', 'I-NAME'), ('Ora', 'I-NAME'), (',', 'O'), ('Record', 'O'), ('date', 'O'), (':', 'O'), ('2093-01-13', 'B-DATE'), (',', 'O'), ('Age', 'O'), (':', 'O'), ('25', 'B-AGE'), (',', 'O'), ('#', 'O'), ('719435', 'B-CONTACT'), ('.', 'O'), ('Dr', 'O'), ('.', 'O'), ('John', 'B-NAME'), ('Green', 'I-NAME'), (',', 'O'), ('ID', 'O'), (':', 'O'), ('1231511863', 'B-ID'), (',', 'O'), ('IP', 'O'), ('203.120.223.13', 'O'), ('.', 'O'), ('He', 'O'), ('is', 'O'), ('a', 'O'), ('60-year-old', 'B-AGE'), ('male', 'O'), ('was', 'O'), ('admitted', 'O'), ('to', 'O'), ('the', 'O'), ('Day', 'O'), ('Hospital', 'O'), ('for', 'O'), ('cystectomy', 'O'), ('on', 'O'), ('01/13/93', 'B-DATE'), ('.', 'O'), ("Patient's", 'O'), ('VIN', 'O'), (':', 'O'), ('1HGBH41JXMN109286', 'O'), (',', 'O'), ('SSN', 'O'), ('#333-44-6666', 'O'), (',', 'O'), ("Driver's", 'O'), ('license', 'O'), ('no:A334455B', 'O'), ('.', 'O'), ('Phone', 'O'), ('(', 'B-CONTACT'), ('302', 'I-CONTACT'), (')', 'I-CONTACT'), ('786-5227', 'I-CONTACT'), (',', 'O'), ('0295', 'B-LOCATION'), ('Keats', 'I-LOCATION'), ('Street', 'I-LOCATION'), (',', 'O'), ('San', 'B-LOCATION'), ('Francisco', 'I-LOCATION'), ('.', 'O')]


 ******************** ner_deid_subentity_augmented Model Results ******************** 

[('Name', 'O'), (':', 'O'), ('Hendrickson', 'B-PATIENT'), (',', 'I-PATIENT'), ('Ora', 'I-PATIENT'), (',', 'O'), ('Record', 'O'), ('date', 'O'), (':', 'O'), ('2093-01-13', 'B-DATE'), (',', 'O'), ('Age', 'O'), (':', 'O'), ('25', 'B-AGE'), (',', 'O'), ('#', 'O'), ('719435', 'B-PHONE'), ('.', 'O'), ('Dr', 'O'), ('.', 'O'), ('John', 'B-DOCTOR'), ('Green', 'I-DOCTOR'), (',', 'O'), ('ID', 'O'), (':', 'O'), ('1231511863', 'B-DEVICE'), (',', 'O'), ('IP', 'O'), ('203.120.223.13', 'O'), ('.', 'O'), ('He', 'O'), ('is', 'O'), ('a', 'O'), ('60-year-old', 'B-AGE'), ('male', 'O'), ('was', 'O'), ('admitted', 'O'), ('to', 'O'), ('the', 'O'), ('Day', 'B-HOSPITAL'), ('Hospital', 'I-HOSPITAL'), ('for', 'O'), ('cystectomy', 'O'), ('on', 'O'), ('01/13/93', 'B-DATE'), ('.', 'O'), ("Patient's", 'O'), ('VIN', 'O'), (':', 'O'), ('1HGBH41JXMN109286', 'O'), (',', 'O'), ('SSN', 'O'), ('#333-44-6666', 'O'), (',', 'O'), ("Driver's", 'O'), ('license', 'O'), ('no:A334455B', 'B-IDNUM'), ('.', 'O'), ('Phone', 'O'), ('(', 'B-PHONE'), ('302', 'I-PHONE'), (')', 'I-PHONE'), ('786-5227', 'I-PHONE'), (',', 'O'), ('0295', 'B-STREET'), ('Keats', 'I-STREET'), ('Street', 'I-STREET'), (',', 'O'), ('San', 'B-STATE'), ('Francisco', 'I-STATE'), ('.', 'O')]


 ******************** ner_deid_generic_docwise Model Results ******************** 

[('Name', 'O'), (':', 'O'), ('Hendrickson', 'B-NAME'), (',', 'I-NAME'), ('Ora', 'I-NAME'), (',', 'O'), ('Record', 'O'), ('date', 'O'), (':', 'O'), ('2093-01-13', 'B-DATE'), (',', 'O'), ('Age', 'O'), (':', 'O'), ('25', 'B-AGE'), (',', 'O'), ('#', 'O'), ('719435', 'B-CONTACT'), ('.', 'O'), ('Dr', 'O'), ('.', 'O'), ('John', 'B-NAME'), ('Green', 'I-NAME'), (',', 'O'), ('ID', 'O'), (':', 'O'), ('1231511863', 'B-ID'), (',', 'O'), ('IP', 'B-NAME'), ('203.120.223.13', 'B-DATE'), ('.', 'O'), ('He', 'O'), ('is', 'O'), ('a', 'O'), ('60-year-old', 'B-AGE'), ('male', 'O'), ('was', 'O'), ('admitted', 'O'), ('to', 'O'), ('the', 'O'), ('Day', 'O'), ('Hospital', 'O'), ('for', 'O'), ('cystectomy', 'O'), ('on', 'O'), ('01/13/93', 'B-DATE'), ('.', 'O'), ("Patient's", 'O'), ('VIN', 'O'), (':', 'O'), ('1HGBH41JXMN109286', 'B-ID'), (',', 'O'), ('SSN', 'O'), ('#333-44-6666', 'B-ID'), (',', 'O'), ("Driver's", 'O'), ('license', 'O'), ('no:A334455B', 'B-ID'), ('.', 'O'), ('Phone', 'O'), ('(', 'B-CONTACT'), ('302', 'I-CONTACT'), (')', 'I-CONTACT'), ('786-5227', 'I-CONTACT'), (',', 'I-CONTACT'), ('0295', 'I-CONTACT'), ('Keats', 'B-LOCATION'), ('Street', 'I-LOCATION'), (',', 'O'), ('San', 'B-LOCATION'), ('Francisco', 'I-LOCATION'), ('.', 'O')]


 ******************** ner_deid_generic_augmented_allUpperCased_langtest Model Results ******************** 

[('Name', 'O'), (':', 'O'), ('Hendrickson', 'B-NAME'), (',', 'I-NAME'), ('Ora', 'I-NAME'), (',', 'O'), ('Record', 'O'), ('date', 'O'), (':', 'O'), ('2093-01-13', 'B-DATE'), (',', 'O'), ('Age', 'O'), (':', 'O'), ('25', 'B-AGE'), (',', 'O'), ('#', 'O'), ('719435', 'B-ID'), ('.', 'O'), ('Dr', 'O'), ('.', 'O'), ('John', 'B-NAME'), ('Green', 'I-NAME'), (',', 'O'), ('ID', 'O'), (':', 'O'), ('1231511863', 'B-ID'), (',', 'O'), ('IP', 'O'), ('203.120.223.13', 'O'), ('.', 'O'), ('He', 'O'), ('is', 'O'), ('a', 'O'), ('60-year-old', 'B-AGE'), ('male', 'O'), ('was', 'O'), ('admitted', 'O'), ('to', 'O'), ('the', 'O'), ('Day', 'O'), ('Hospital', 'O'), ('for', 'O'), ('cystectomy', 'O'), ('on', 'O'), ('01/13/93', 'B-DATE'), ('.', 'O'), ("Patient's", 'O'), ('VIN', 'O'), (':', 'O'), ('1HGBH41JXMN109286', 'B-NAME'), (',', 'I-NAME'), ('SSN', 'I-NAME'), ('#333-44-6666', 'B-ID'), (',', 'O'), ("Driver's", 'O'), ('license', 'O'), ('no:A334455B', 'B-ID'), ('.', 'O'), ('Phone', 'O'), ('(', 'B-CONTACT'), ('302', 'I-CONTACT'), (')', 'I-CONTACT'), ('786-5227', 'I-CONTACT'), (',', 'O'), ('0295', 'B-LOCATION'), ('Keats', 'I-LOCATION'), ('Street', 'I-LOCATION'), (',', 'O'), ('San', 'B-LOCATION'), ('Francisco', 'I-LOCATION'), ('.', 'O')]

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_profiling_deidentification|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.0+|
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
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- ContextualParserModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- RegexMatcherInternalModel
- TextMatcherInternalModel
- TextMatcherInternalModel
- PretrainedZeroShotNER
- NerConverterInternalModel
- Finisher