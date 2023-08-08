---
layout: model
title: Extract Health Behaviors and Problems Entities from Social Determinants of Health Texts
author: John Snow Labs
name: ner_sdoh_health_behaviours_problems
date: 2023-07-02
tags: [health_behavior, problem, disease, sdoh, social_determinants, public_health, en, licensed]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

SDOH NER model is designed to detect and label social determinants of health (SDOH) health behavior and problem related entities within text data. Social determinants of health are crucial factors that influence individuals' health outcomes, encompassing various social, economic, and environmental elements. 
The model has been trained using advanced machine-learning techniques on a diverse range of text sources. The model's accuracy and precision have been carefully validated against expert-labeled data to ensure reliable and consistent results. Here are the labels of the SDOH NER model with their description:

- `Communicable_Disease`: Include all the communicable diseases. "HIV, hepatitis, tuberculosis, sexually transmitted diseases, etc."
- `Diet`: Information regarding the patient’s dietary habits. "vegetarian, vegan, healthy foods, low-calorie diet, etc."
- `Disability`: Mentions related to disability
- `Eating_Disorder`: This entity is used to extract eating disorders. "anorexia, bulimia, pica, etc."
- `Exercise`: Mentions of the exercise habits of a patient. "exercise, physical activity, play football, go to the gym, etc."
- `Hyperlipidemia`: Terms that indicate hyperlipidemia and relevant subtypes. "hyperlipidemia, hypercholesterolemia, elevated cholesterol, etc."
- `Hypertension`: Terms related to hypertension. "hypertension, high blood pressure, etc."
- `Mental_Health`: Include all the mental, neurodegenerative, and neurodevelopmental diagnoses, disorders, conditions, or syndromes mentioned. "depression, anxiety, bipolar disorder, psychosis, etc."
- `Obesity`: Terms related to the patient being obese. "obesity, overweight, etc."
- `Other_Disease`: Include all the diseases mentioned. "psoriasis, thromboembolism, etc." 
- `Quality_Of_Life`: Quality of life refers to how an individual feels about their current station in life. " lower quality of life, profoundly impact his quality of life, etc."
- `Sexual_Activity`: Mentions of patient’s sexual behaviors. "monogamous, sexual activity, inconsistent condom use, etc."

## Predicted Entities

`Communicable_Disease`, `Diet`, `Disability`, `Eating_Disorder`, `Exercise`, `Hyperlipidemia`, `Hypertension`, `Mental_Health`, `Obesity`, `Other_Disease`, `Quality_Of_Life`, `Sexual_Activity`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/SDOH/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/27.0.Social_Determinant_of_Health_Models.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_health_behaviours_problems_en_4.4.4_3.0_1688321491656.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_sdoh_health_behaviours_problems_en_4.4.4_3.0_1688321491656.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from pyspark.sql.types import StringType

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_sdoh_health_behaviours_problems", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter   
    ])

sample_texts = ["She has not been getting regular exercise and not followed the diet for approximately two years due to chronic sciatic pain.", "Medical History: The patient is a 32-year-old female who presents with a history of anxiety, depression, bulimia nervosa, elevated cholesterol, and substance abuse. She used to play basketball and tennis.", "Pt was intubated at the scene & currently sedated due to high BP. Also, he is currently on social security disability.", "A 28-year-old single female teacher presented with concerns about her overall health and well-being. She had a history of hypertension and hyperlipidemia. Her sedentary lifestyle and poor diet contributed to obesity, negatively impacting her quality of life and self-esteem. She expressed a desire to improve her lifestyle, lose weight, and address her mental well-being and sexual satisfaction. She is also advised to go to the gym."]


data = spark.createDataFrame(sample_texts, StringType()).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_sdoh_health_behaviours_problems", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter   
))

val data = Seq(Array("She has not been getting regular exercise and not followed the diet for approximately two years due to chronic sciatic pain.", "Medical History: The patient is a 32-year-old female who presents with a history of anxiety, depression, bulimia nervosa, elevated cholesterol, and substance abuse. She used to play basketball and tennis.", "Pt was intubated at the scene & currently sedated due to high BP. Also, he is currently on social security disability.", "A 28-year-old single female teacher presented with concerns about her overall health and well-being. She had a history of hypertension and hyperlipidemia. Her sedentary lifestyle and poor diet contributed to obesity, negatively impacting her quality of life and self-esteem. She expressed a desire to improve her lifestyle, lose weight, and address her mental well-being and sexual satisfaction. She is also advised to go to the gym.")).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+--------------------+-----+---+---------------+
|chunk               |begin|end|ner_label      |
+--------------------+-----+---+---------------+
|regular exercise    |25   |40 |Exercise       |
|diet                |63   |66 |Diet           |
|chronic sciatic pain|103  |122|Other_Disease  |
|anxiety             |84   |90 |Mental_Health  |
|depression          |93   |102|Mental_Health  |
|bulimia nervosa     |105  |119|Eating_Disorder|
|basketball          |182  |191|Exercise       |
|tennis              |197  |202|Exercise       |
|high BP             |57   |63 |Hypertension   |
|disability          |107  |116|Disability     |
|overall health      |70   |83 |Quality_Of_Life|
|well-being          |89   |98 |Quality_Of_Life|
|hypertension        |122  |133|Hypertension   |
|hyperlipidemia      |139  |152|Hyperlipidemia |
|sedentary lifestyle |159  |177|Exercise       |
|poor diet           |183  |191|Diet           |
|obesity             |208  |214|Obesity        |
|quality of life     |242  |256|Quality_Of_Life|
|self-esteem         |262  |272|Quality_Of_Life|
|mental well-being   |353  |369|Mental_Health  |
|sexual satisfaction |375  |393|Sexual_Activity|
|gym                 |429  |431|Exercise       |
+--------------------+-----+---+---------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_sdoh_health_behaviours_problems|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|3.0 MB|
|Dependencies:|embeddings_clinical|

## References

Internal SDOH Project

## Benchmarking

```bash
               label  precision    recall  f1-score   support
Communicable_Disease       0.77      1.00      0.87        17
                Diet       0.93      0.95      0.94        44
          Disability       0.98      1.00      0.99        53
     Eating_Disorder       0.89      0.94      0.91        33
            Exercise       0.86      0.98      0.92        52
      Hyperlipidemia       1.00      0.85      0.92        13
        Hypertension       0.95      1.00      0.98        21
       Mental_Health       0.92      0.92      0.92       476
             Obesity       1.00      0.71      0.83        14
       Other_Disease       0.89      0.92      0.91       628
     Quality_Of_Life       0.79      0.96      0.87        47
     Sexual_Activity       0.86      0.86      0.86        29
           micro-avg       0.90      0.93      0.91      1427
           macro-avg       0.90      0.92      0.91      1427
        weighted-avg       0.90      0.93      0.91      1427

```