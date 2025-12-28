---
layout: model
title: Numind Medical NER LLM v1 (numind_ner_medical_llm_2b_v1)
author: John Snow Labs
name: numind_ner_medical_llm_2b_v1
date: 2025-12-28
tags: [medical, clinical, ner, llm, en, licensed, numind, llamacpp]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.2.2
spark_version: 3.4
supported: true
engine: llamacpp
annotator: MedicalLLM
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This medical LLM model is trained to extract medical entities from clinical notes and return them in structured JSON format. It supports various entity types such as AGE, CITY, DRUG, PATIENT, PROBLEM, etc.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/numind_ner_medical_llm_2b_v1_en_6.2.2_3.4_1766915515658.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/numind_ner_medical_llm_2b_v1_en_6.2.2_3.4_1766915515658.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp_jsl.annotator import MedicalLLM
from sparknlp.base import DocumentAssembler
from pyspark.ml import Pipeline

prompt = """Extract all medical entities from the clinical note below and return them in JSON format according to the template.

#### Template:
{{
  "entities": [
    {{
      "AGE": ["verbatim-string"],
      "CITY": ["verbatim-string"],
      "COUNTRY": ["verbatim-string"],
      "DATE": ["verbatim-string"],
      "DOCTOR": ["verbatim-string"],
      "DOSAGE": ["verbatim-string"],
      "DRUG": ["verbatim-string"],
      "DURATION": ["verbatim-string"],
      "CANCER": ["verbatim-string"],
      "FREQUENCY": ["verbatim-string"],
      "HOSPITAL": ["verbatim-string"],
      "BODY_PART": ["verbatim-string"],
      "PATIENT": ["verbatim-string"],
      "PHONE": ["verbatim-string"],
      "PROBLEM": ["verbatim-string"],
      "PROFESSION": ["verbatim-string"],
      "STATE": ["verbatim-string"],
      "STRENGTH": ["verbatim-string"],
      "TEST": ["verbatim-string"],
      "TREATMENT": ["verbatim-string"]
    }}
  ]
}}

#### Clinical Note:
[Your clinical note here]

#### Instructions:
- Extract all entities exactly as they appear in the text
- Return only valid JSON format
- Use empty lists for categories with no entities found
- Do not add explanations, only return the JSON

#### Output:
"""

data = spark.createDataFrame([[prompt]]).toDF("text")

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

medical_llm = MedicalLLM.pretrained("numind_ner_medical_llm_2b_v1", "en", "clinical/models")\
    .setInputCols("document")\
    .setOutputCol("completions")\
    .setBatchSize(1)\
    .setNPredict(3000)\
    .setUseChatTemplate(True)\
    .setTemperature(0.1)\
    .setTopK(40)\
    .setTopP(0.9)

pipeline = Pipeline(stages=[
    document_assembler,
    medical_llm
])

model = pipeline.fit(data)
results = model.transform(data)

output = results.select("completions").collect()[0].completions[0].result
print(output)

```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

prompt = """Extract all medical entities from the clinical note below and return them in JSON format according to the template.

#### Template:
{{
  "entities": [
    {{
      "AGE": ["verbatim-string"],
      "CITY": ["verbatim-string"],
      "COUNTRY": ["verbatim-string"],
      "DATE": ["verbatim-string"],
      "DOCTOR": ["verbatim-string"],
      "DOSAGE": ["verbatim-string"],
      "DRUG": ["verbatim-string"],
      "DURATION": ["verbatim-string"],
      "CANCER": ["verbatim-string"],
      "FREQUENCY": ["verbatim-string"],
      "HOSPITAL": ["verbatim-string"],
      "BODY_PART": ["verbatim-string"],
      "PATIENT": ["verbatim-string"],
      "PHONE": ["verbatim-string"],
      "PROBLEM": ["verbatim-string"],
      "PROFESSION": ["verbatim-string"],
      "STATE": ["verbatim-string"],
      "STRENGTH": ["verbatim-string"],
      "TEST": ["verbatim-string"],
      "TREATMENT": ["verbatim-string"]
    }}
  ]
}}

#### Clinical Note:
[Your clinical note here]

#### Instructions:
- Extract all entities exactly as they appear in the text
- Return only valid JSON format
- Use empty lists for categories with no entities found
- Do not add explanations, only return the JSON

#### Output:
"""

data = nlp.SparkSession.builder.getOrCreate().createDataFrame([[prompt]]).toDF("text")

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

medical_llm = medical.MedicalLLM.pretrained("numind_ner_medical_llm_2b_v1", "en", "clinical/models")\
    .setInputCols("document")\
    .setOutputCol("completions")\
    .setBatchSize(1)\
    .setNPredict(3000)\
    .setUseChatTemplate(True)\
    .setTemperature(0.1)\
    .setTopK(40)\
    .setTopP(0.9)

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    medical_llm
])

model = pipeline.fit(data)
results = model.transform(data)

output = results.select("completions").collect()[0].completions[0].result
print(output)

```
```scala
import com.johnsnowlabs.nlp.base._
import com.johnsnowlabs.nlp.annotators._
import org.apache.spark.sql.functions._
import org.apache.spark.ml.Pipeline

val prompt = """Extract all medical entities from the clinical note below and return them in JSON format according to the template.

#### Template:
{{
  "entities": [
    {{
      "AGE": ["verbatim-string"],
      "CITY": ["verbatim-string"],
      "COUNTRY": ["verbatim-string"],
      "DATE": ["verbatim-string"],
      "DOCTOR": ["verbatim-string"],
      "DOSAGE": ["verbatim-string"],
      "DRUG": ["verbatim-string"],
      "DURATION": ["verbatim-string"],
      "CANCER": ["verbatim-string"],
      "FREQUENCY": ["verbatim-string"],
      "HOSPITAL": ["verbatim-string"],
      "BODY_PART": ["verbatim-string"],
      "PATIENT": ["verbatim-string"],
      "PHONE": ["verbatim-string"],
      "PROBLEM": ["verbatim-string"],
      "PROFESSION": ["verbatim-string"],
      "STATE": ["verbatim-string"],
      "STRENGTH": ["verbatim-string"],
      "TEST": ["verbatim-string"],
      "TREATMENT": ["verbatim-string"]
    }}
  ]
}}

#### Clinical Note:
[Your clinical note here]

#### Instructions:
- Extract all entities exactly as they appear in the text
- Return only valid JSON format
- Use empty lists for categories with no entities found
- Do not add explanations, only return the JSON

#### Output:
"""

val data = Seq(prompt).toDF("text")

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val medicalLLM = MedicalLLM
  .pretrained("numind_ner_medical_llm_2b_v1", "en", "clinical/models")
  .setInputCols(Array("document"))
  .setOutputCol("completions")
  .setBatchSize(1)
  .setNPredict(3000)
  .setUseChatTemplate(true)
  .setTemperature(0.1)
  .setTopK(40)
  .setTopP(0.9)

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  medicalLLM
))

val model = pipeline.fit(data)
val result = model.transform(data)

val output = result.select("completions").collect()(0).getAs[Seq[Row]]("completions")(0).getAs[String]("result")
println(output)

```
</div>

## Results

```bash


|chunk                     |begin|end |ner_label |confidence|
|--------------------------|-----|--------------------------|
|58-year-old               | 41  |51  |AGE       |0.90656307|
|chest                     |246  |250 |BODY_PART |0.93823762|
|non-small cell lung cancer|451  |476 |CANCER    |0.94392558|
|New York                  |112  |119 |CITY      |0.90966768|
|United States             |2829 |2841|COUNTRY   |0.90126566|
|March 15, 2024            |3    |16  |DATE      |0.94820805|
|Sarah Johnson             |155  |167 |DOCTOR    |0.99527312|
|30-pack-year              |379  |390 |DOSAGE    |0.99747109|
|osimertinib               |1128 |1138|DRUG      |0.96035763|
|once daily                |1153 |1162|DURATION  |0.97008323|
|daily                     |1158 |1162|FREQUENCY |0.9136936 |
|Memorial Hospital         |91   |107 |HOSPITAL  |0.97247546|
|John Smith                |27   |36  |PATIENT   |0.94148871|
|+1 (555) 123-4567         |2541 |2557|PHONE     |0.96758803|
|chest pain                |246  |255 |PROBLEM   |0.92068439|
|oncologist                |173  |182 |PROFESSION|0.98166695|
|New York                  |112  |119 |STATE     |0.94135707|
|80 mg                     |1140 |1144|STRENGTH  | 0.9556199|
|CT scan of the chest      |562  |581 |TEST      |0.97324896|
|targeted therapy          |1105 |1120|TREATMENT |0.95535014|

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|numind_ner_medical_llm_2b_v1|
|Compatibility:|Healthcare NLP 6.2.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[completions]|
|Language:|en|
|Size:|2.5 GB|