---
layout: model
title: SDOH Mental Health For Classification
author: John Snow Labs
name: genericclassifier_sdoh_mental_health_clinical
date: 2023-04-10
tags: [en, licenced, clinical, sdoh, generic_classifier, mental_health, embeddings_clinical, licensed]
task: Text Classification
language: en
edition: Healthcare NLP 4.3.2
spark_version: [3.2, 3.0]
supported: true
annotator: GenericClassifierModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This Generic Classifier model is intended for detecting if the patient has mental health problems in clinical notes. This model is trained by using GenericClassifierApproach annotator.

`Mental_Disorder`: The patient has mental health problems. 

`No_Or_Not_Mentioned`: The patient doesn't have mental health problems or it is not mentioned in the clinical notes.

## Predicted Entities

`Mental_Disorder`, `No_Or_Not_Mentioned`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/genericclassifier_sdoh_mental_health_clinical_en_4.3.2_3.0_1681132553520.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/genericclassifier_sdoh_mental_health_clinical_en_4.3.2_3.0_1681132553520.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")
        
tokenizer = Tokenizer() \
            .setInputCols(["document"]) \
            .setOutputCol("token")
        
word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
        .setInputCols(["document","token"])\
        .setOutputCol("word_embeddings")

sentence_embeddings = SentenceEmbeddings() \
        .setInputCols(["document", "word_embeddings"]) \
        .setOutputCol("sentence_embeddings") \
        .setPoolingStrategy("AVERAGE")

features_asm = FeaturesAssembler()\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("features")

generic_classifier = GenericClassifierModel.pretrained("genericclassifier_sdoh_mental_health_clinical", 'en', 'clinical/models')\
    .setInputCols(["features"])\
    .setOutputCol("class")

pipeline = Pipeline(stages=[
    document_assembler,
    tokenizer,
    word_embeddings,
    sentence_embeddings,
    features_asm,
    generic_classifier    
])

sample_texts = ["""James is a 28-year-old man who has been struggling with schizophrenia for the past five years. He was diagnosed with the condition after experiencing a psychotic episode in his early 20s. The following is a case study that explores James' background, symptoms, diagnosis, treatment, and outcomes.

Background:

James grew up in a middle-class family with his parents and two younger siblings. He had a relatively normal childhood and was an above-average student in school. However, in his late teens, James started experiencing paranoid delusions and hallucinations. He became increasingly isolated and withdrawn, and his grades started to suffer. James was eventually hospitalized after experiencing a psychotic episode in college.

Symptoms:

James' symptoms of schizophrenia include delusions, hallucinations, disorganized speech and behavior, and negative symptoms. He experiences paranoid delusions, believing that people are out to get him or that he is being followed. James also experiences auditory hallucinations, hearing voices that are critical or commanding. He has difficulty organizing his thoughts and expressing himself coherently. James also experiences negative symptoms, such as reduced motivation, social withdrawal, and flattened affect.

Diagnosis:

James' diagnosis of schizophrenia was based on his symptoms, history, and a comprehensive evaluation by a mental health professional. He was diagnosed with paranoid schizophrenia, which is characterized by delusions and hallucinations.

Treatment:

James' treatment for schizophrenia consisted of medication and therapy. He was prescribed antipsychotic medication to help manage his symptoms. He also participated in cognitive-behavioral therapy (CBT), which focused on helping him identify and challenge his delusions and improve his communication skills. James also attended support groups for individuals with schizophrenia.

Outcomes:

With ongoing treatment, James' symptoms have become more manageable. He still experiences occasional psychotic episodes, but they are less frequent and less severe. James has also developed better coping skills and has learned to recognize the warning signs of an impending episode. He is able to maintain employment and has a stable home life. James' family has also been involved in his treatment, which has helped to improve his support system and overall quality of life.
""",
 """Patient John is a 60-year-old man who presents to a primary care clinic for a routine check-up. He reports feeling generally healthy, with no significant medical concerns. However, he reveals that he is a smoker and drinks alcohol on a regular basis. The patient also mentions that he has a history of working long hours and has limited time for physical activity and social interactions.

Based on this information, it appears that Patient John's overall health may be affected by several social determinants of health, including tobacco and alcohol use, lack of physical activity, and social isolation. To address these issues, the healthcare provider may recommend a comprehensive physical exam and develop a treatment plan that includes lifestyle modifications, such as smoking cessation and reduction of alcohol intake. Additionally, the patient may benefit from referrals to local organizations that provide resources for physical activity and social engagement. The healthcare provider may also recommend strategies to reduce work-related stress and promote work-life balance. By addressing these social determinants of health, healthcare providers can help promote Patient John's overall health and prevent future health problems."""]

df = spark.createDataFrame(text_list, StringType()).toDF("text")

result = pipeline.fit(df).transform(df)

result.select("text", "class.result").show(truncate=100)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
  
val tokenizer = Tokenizer()
            .setInputCols(["document"])
            .setOutputCol("token")
        
val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
        .setInputCols(["document","token"])
        .setOutputCol("word_embeddings")

val sentence_embeddings = SentenceEmbeddings()
        .setInputCols(["document", "word_embeddings"])
        .setOutputCol("sentence_embeddings")
        .setPoolingStrategy("AVERAGE")

val features_asm = new FeaturesAssembler()
    .setInputCols("sentence_embeddings")
    .setOutputCol("features")

val generic_classifier = GenericClassifierModel.pretrained("genericclassifier_sdoh_mental_health_clinical", "en", "clinical/models")
    .setInputCols("features")
    .setOutputCol("class")

val pipeline = new PipelineModel().setStages(Array(
    document_assembler,
    tokenizer,
    word_embeddings,
    sentence_embeddings,
    features_asm,
    generic_classifier))

val data = Seq(Array("""James is a 28-year-old man who has been struggling with schizophrenia for the past five years. He was diagnosed with the condition after experiencing a psychotic episode in his early 20s. The following is a case study that explores James' background, symptoms, diagnosis, treatment, and outcomes.

Background:

James grew up in a middle-class family with his parents and two younger siblings. He had a relatively normal childhood and was an above-average student in school. However, in his late teens, James started experiencing paranoid delusions and hallucinations. He became increasingly isolated and withdrawn, and his grades started to suffer. James was eventually hospitalized after experiencing a psychotic episode in college.

Symptoms:

James' symptoms of schizophrenia include delusions, hallucinations, disorganized speech and behavior, and negative symptoms. He experiences paranoid delusions, believing that people are out to get him or that he is being followed. James also experiences auditory hallucinations, hearing voices that are critical or commanding. He has difficulty organizing his thoughts and expressing himself coherently. James also experiences negative symptoms, such as reduced motivation, social withdrawal, and flattened affect.

Diagnosis:

James' diagnosis of schizophrenia was based on his symptoms, history, and a comprehensive evaluation by a mental health professional. He was diagnosed with paranoid schizophrenia, which is characterized by delusions and hallucinations.

Treatment:

James' treatment for schizophrenia consisted of medication and therapy. He was prescribed antipsychotic medication to help manage his symptoms. He also participated in cognitive-behavioral therapy (CBT), which focused on helping him identify and challenge his delusions and improve his communication skills. James also attended support groups for individuals with schizophrenia.

Outcomes:

With ongoing treatment, James' symptoms have become more manageable. He still experiences occasional psychotic episodes, but they are less frequent and less severe. James has also developed better coping skills and has learned to recognize the warning signs of an impending episode. He is able to maintain employment and has a stable home life. James' family has also been involved in his treatment, which has helped to improve his support system and overall quality of life.
""",
 """Patient John is a 60-year-old man who presents to a primary care clinic for a routine check-up. He reports feeling generally healthy, with no significant medical concerns. However, he reveals that he is a smoker and drinks alcohol on a regular basis. The patient also mentions that he has a history of working long hours and has limited time for physical activity and social interactions.

Based on this information, it appears that Patient John's overall health may be affected by several social determinants of health, including tobacco and alcohol use, lack of physical activity, and social isolation. To address these issues, the healthcare provider may recommend a comprehensive physical exam and develop a treatment plan that includes lifestyle modifications, such as smoking cessation and reduction of alcohol intake. Additionally, the patient may benefit from referrals to local organizations that provide resources for physical activity and social engagement. The healthcare provider may also recommend strategies to reduce work-related stress and promote work-life balance. By addressing these social determinants of health, healthcare providers can help promote Patient John's overall health and prevent future health problems.""")).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+---------------------+
|                                                                                                text|               result|
+----------------------------------------------------------------------------------------------------+---------------------+
|James is a 28-year-old man who has been struggling with schizophrenia for the past five years. He...|    [Mental_Disorder]|
|Patient John is a 60-year-old man who presents to a primary care clinic for a routine check-up. H...|[No_Or_Not_Mentioned]|
+----------------------------------------------------------------------------------------------------+---------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|genericclassifier_sdoh_mental_health_clinical|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[features]|
|Output Labels:|[prediction]|
|Language:|en|
|Size:|1.5 MB|
|Dependencies:|embeddings_clinical|

## References

Internal SDOH Project

## Benchmarking

```bash
              label  precision    recall  f1-score   support
    Mental_Disorder       0.79      0.85      0.82       223
No_Or_Not_Mentioned       0.85      0.78      0.82       240
           accuracy        -         -        0.82       463
          macro-avg       0.82      0.82      0.82       463
       weighted-avg       0.82      0.82      0.82       463
```
