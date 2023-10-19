---
layout: model
title: Multilabel Text Classification for Heart Disease
author: John Snow Labs
name: multiclassifierdl_heart_disease
date: 2023-10-16
tags: [licensed, en, classification, text_classification, multiclassifier, heart_disease, hypertension, coronary_artery_disease, myocardial_infarction, tensorflow]
task: Text Classification
language: en
edition: Healthcare NLP 5.1.1
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MultiClassifierDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The PHS-BERT Heart Disease Classifier Model is a specialized text classification system, engineered to accurately identify and categorize textual mentions of three prominent cardiovascular diseases: Hypertension, Coronary Artery Disease, and Myocardial Infarction. More detailed information about classes as follows:

`Hypertension`: This category is designated for text mentions that correspond to Hypertension, a medical condition where the blood pressure in the arteries is persistently elevated. Chronic hypertension can lead to heart diseases, stroke, and other complications. Example: "Due to his consistent high blood pressure readings, my father was diagnosed with hypertension."

`Coronary Artery Disease`(CAD): Textual content that implicates CAD is classified here. CAD, also known as ischemic heart disease, is characterized by a reduced blood flow to the heart muscle due to the build-up of plaque in the arteries supplying the heart. This could result in chest pain (angina) or a heart attack. Example: "My aunt had chest pain and, after some tests, she was told it was due to coronary artery disease."

`Myocardial Infarction`(MI): Entries here incorporate text alluding to MI, more commonly known as a heart attack. MI occurs when blood flow to a part of the heart muscle gets blocked, usually by a blood clot. This can damage or destroy that part of the heart muscle. Example: "Last year, my neighbour experienced severe chest pain and was rushed to the hospital; the diagnosis was a myocardial infarction."

## Predicted Entities

`Hypertension`, `MI`, `CAD`, `Other/Unknown`, `No`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/CLASSIFICATION_HEART_DISEASE/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/PUBLIC_HEALTH_CLASSIFIER_DL.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/multiclassifierdl_heart_disease_en_5.1.1_3.0_1697443096682.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/multiclassifierdl_heart_disease_en_5.1.1_3.0_1697443096682.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["document", "token"])\
    .setOutputCol("embeddings")

sentence_embeddings = SentenceEmbeddings()\
    .setInputCols(["document", "embeddings"]) \
    .setOutputCol("sentence_embeddings") \
    .setPoolingStrategy("AVERAGE")

multiclassifierdl = MultiClassifierDLModel.pretrained("multiclassifierdl_heart_disease", "en", "clinical/models")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("predicted_class")\
    .setThreshold(0.999)

clf_pipeline = Pipeline(
    stages=[
        documentAssembler,
        tokenizer,
        word_embeddings,
        sentence_embeddings,
        multiclassifierdl
])


data = spark.createDataFrame([
     ["""Mrs. Allen was diagnosed with hypertension after consistently recording blood pressure readings above 140/90 mmHg."""],
     ["""Following a series of diagnostic tests, Mr. Harris was confirmed to have CAD (Coronary Artery Disease)."""],
     ["""After presenting with crushing chest pain and diaphoresis, Mr. Stevens was diagnosed with an MI (Myocardial Infarction)."""]
]).toDF("text")


result = clf_pipeline.fit(data).transform(data)
```
```scala
val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols(Array("document"))
    .setOutputCol("token")

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("document", "token"))
    .setOutputCol("embeddings")

val sentence_embeddings = new SentenceEmbeddings()\
    .setInputCols(Array("document", "embeddings")) \
    .setOutputCol("sentence_embeddings") \
    .setPoolingStrategy("AVERAGE")

val multiclassifierdl = MultiClassifierDLModel.pretrained("multiclassifierdl_heart_disease", "en", "clinical/models")\
    .setInputCols("sentence_embeddings")\
    .setOutputCol("predicted_class")\
    .setThreshold(0.999)

val clf_pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    tokenizer,
    wordEmbeddings,
    sentence_embeddings,
    multiclassifierdl
))

val data = Seq(Array(
      """Mrs. Allen was diagnosed with hypertension after consistently recording blood pressure readings above 140/90 mmHg.""",
      """Following a series of diagnostic tests, Mr. Harris was confirmed to have CAD (Coronary Artery Disease).""",
      """After presenting with crushing chest pain and diaphoresis, Mr. Stevens was diagnosed with an MI (Myocardial Infarction)."""
 )).toDS.toDF("text")

val result = clf_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+--------------+
|                                                                                                text|        result|
+----------------------------------------------------------------------------------------------------+--------------+
|Mrs. Allen was diagnosed with hypertension after consistently recording blood pressure readings a...|[Hypertension]|
|Following a series of diagnostic tests, Mr. Harris was confirmed to have CAD (Coronary Artery Dis...|         [CAD]|
|After presenting with crushing chest pain and diaphoresis, Mr. Stevens was diagnosed with an MI (...|          [MI]|
+----------------------------------------------------------------------------------------------------+--------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|multiclassifierdl_heart_disease|
|Compatibility:|Healthcare NLP 5.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[class]|
|Language:|en|
|Size:|87.8 MB|
|Dependencies:|`embeddings_clinical`|

## References

Trained with the in-house dataset

## Sample text from the training dataset

Hypertension: Mr. Daniels was diagnosed with hypertension during a routine check-up at the age of 45. He had consistently high blood pressure readings over several visits, indicative of hypertension. Often experiencing headaches and occasional bouts of dizziness, these could be linked to his elevated blood pressure. He has been prescribed antihypertensive medications and advised to adopt lifestyle modifications, such as reducing salt intake and engaging in regular exercise, to manage his hypertension effectively.

Coronary Artery Disease (CAD): Mrs. Martinez, a 58-year-old, began experiencing chest discomfort and shortness of breath during physical exertion. After undergoing an angiogram, she was diagnosed with coronary artery disease due to significant blockage in her coronary arteries. Her family history reveals her father had a similar condition, making her predisposed to CAD. Along with prescribed medications to reduce her risk of a heart attack, Mrs. Martinez will undergo a cardiac rehabilitation program and make dietary changes to manage her coronary artery disease.

Myocardial Infarction (MI): Mr. Jackson, at the age of 52, suddenly experienced severe chest pain while at work and was immediately rushed to the emergency department. The ECG and elevated cardiac enzymes confirmed a diagnosis of myocardial infarction. Recounting the event, Mr. Jackson mentioned that he felt a crushing pain in his chest, radiating to his left arm, typical symptoms of a heart attack. Post-treatment, he was advised to engage in cardiac rehabilitation, maintain a heart-healthy diet, and take prescribed medications diligently to prevent another myocardial infarction in the future.

## Benchmarking

```bash
label         tp     fp    fn    prec            rec         f1
Other/Unknown 48     10    28    0.82758623     0.6315789    0.7164179
No            366    39    41    0.9037037      0.8992629    0.9014778
MI            128    13    12    0.9078014      0.9142857    0.911032
Hypertension  184    30    41    0.8598131      0.8177778    0.8382688
CAD           191    13    14    0.9362745      0.9317073    0.9339853
Macro-average 917    105   136   0.8870357      0.8389225    0.8623085
Micro-average 917    105   136   0.89726025     0.8708452    0.88385534
```