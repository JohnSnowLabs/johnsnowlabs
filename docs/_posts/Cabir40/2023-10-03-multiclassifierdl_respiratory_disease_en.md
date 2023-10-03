---
layout: model
title: Multilabel Text Classification For Respiratory Disease
author: John Snow Labs
name: multiclassifierdl_respiratory_disease
date: 2023-10-03
tags: [en, licensed, text_classification, multiclassifier, respiratory_disease, asthma, emphysema, chronic_bronchitis, tensorflow]
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

The PHS-BERT Respiratory Disease Classifier Model is a specialized text classification system, engineered to accurately identify and categorize textual mentions of four prominent respiratory diseases: Asthma, Chronic Obstructive Pulmonary Disease (COPD), Emphysema, and Chronic bronchitis. More detailed information about classes as follows:  

`Asthma`: A classification indicating textual mentions explicitly or implicitly referring to Asthma, a condition characterized by chronic inflammation of the airways, leading to episodes of wheezing, shortness of breath, chest tightness, and coughing. Example: “I can’t take part in the marathon due to my persistent asthma issues.  

`Chronic Obstructive Pulmonary Disease` (COPD): This category encapsulates text referring to COPD, a progressive lung disease that engenders obstructed airflow from the lungs. Symptoms include breathing difficulty, cough, mucus production, and wheezing. Example: "COPD makes it incredibly hard for my dad to walk long distances without becoming breathless."  

`Emphysema`: Text that signifies mentions of Emphysema falls into this classification. Emphysema, a subset of COPD, involves the gradual damage of the air sacs (alveoli) in the lungs, impeding the outward flow of air and causing breathlessness. Example: "Ever since being diagnosed with emphysema, climbing stairs has become a significant challenge."  

`Chronic Bronchitis`: Any textual content that points toward Chronic Bronchitis is categorized here. Chronic bronchitis is a form of COPD characterized by a chronic cough and mucus production due to the long-term inflammation of the bronchial tubes. Example: "The incessant coughing from chronic bronchitis keeps me awake most nights."

## Predicted Entities

`Astham`,`COPD`, `Emphysema`, `Chronic bronchitis`, `Other/Unknown`, `No` 

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/multiclassifierdl_respiratory_disease_en_5.1.1_3.0_1696348950217.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/multiclassifierdl_respiratory_disease_en_5.1.1_3.0_1696348950217.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

multiclassifierdl = MultiClassifierDLModel.pretrained("multiclassifierdl_respiratory_disease", "en", "clinical/models")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("predicted_class")

clf_pipeline = Pipeline(
    stages=[
        documentAssembler,
        tokenizer,
        word_embeddings,
        sentence_embeddings,
        multiclassifierdl
])


data = spark.createDataFrame([
    ["""The patient, experiencing recurrent episodes of wheezing and shortness of breath, has been diagnosed with Asthma and is advised to use a daily controller inhaler to manage the symptoms."""],
    ["""Due to the patient's long history of tobacco use and persistent cough producing large amounts of sputum, a diagnosis of Chronic Obstructive Pulmonary Disease (COPD) has been established, necessitating bronchodilators for management."""],
    ["""The presence of dyspnea, chronic cough, and a history of smoking have led to the diagnosis of Emphysema for the patient, warranting the initiation of long-term oxygen therapy."""],
    ["""The patient has been diagnosed with Chronic Bronchitis following the prolonged occurrence of cough and mucus production, and is recommended to undergo pulmonary rehabilitation and pharmacotherapy."""],
    ["""With a clinical presentation of persistent wheezing and respiratory discomfort, the patient has been conclusively diagnosed with Asthma, necessitating immediate commencement of anti-inflammatory medications."""],
    ["""Manifesting prolonged symptoms of breathlessness and a productive cough, the patient has received a diagnosis of Chronic Obstructive Pulmonary Disease (COPD), and a comprehensive treatment involving bronchodilators and lifestyle modifications has been recommended."""],
    ["""The patient, exhibiting extensive lung damage and significant shortness of breath, has been diagnosed with Emphysema, requiring meticulous management with bronchodilators and pulmonary rehabilitation to improve lung function."""],
    ["""Chronic Bronchitis has been diagnosed in the patient presenting with a chronic cough and frequent respiratory infections, necessitating a treatment plan inclusive of antibiotics and chest physiotherapy."""],

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

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_healthcare_100d", "en", "clinical/models")
    .setInputCols(Array("document", "token"))
    .setOutputCol("embeddings")

val sentence_embeddings = new SentenceEmbeddings()\
    .setInputCols(Array()"document", "embeddings")) \
    .setOutputCol("sentence_embeddings") \
    .setPoolingStrategy("AVERAGE")

val multiclassifierdl = MultiClassifierDLModel.pretrained("multiclassifierdl_respiratory_disease", "en", "clinical/models")\
    .setInputCols("sentence_embeddings")\
    .setOutputCol("predicted_class")

val clf_pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    tokenizer,
    wordEmbeddings,
    sentence_embeddings,
    multiclassifierdl
))

val data = Seq(Array(
    """The patient, experiencing recurrent episodes of wheezing and shortness of breath, has been diagnosed with Asthma and is advised to use a daily controller inhaler to manage the symptoms.""",
    """Due to the patient's long history of tobacco use and persistent cough producing large amounts of sputum, a diagnosis of Chronic Obstructive Pulmonary Disease (COPD) has been established, necessitating bronchodilators for management.""",
    """The presence of dyspnea, chronic cough, and a history of smoking have led to the diagnosis of Emphysema for the patient, warranting the initiation of long-term oxygen therapy.""",
    """The patient has been diagnosed with Chronic Bronchitis following the prolonged occurrence of cough and mucus production, and is recommended to undergo pulmonary rehabilitation and pharmacotherapy.""",
    """With a clinical presentation of persistent wheezing and respiratory discomfort, the patient has been conclusively diagnosed with Asthma, necessitating immediate commencement of anti-inflammatory medications.""",
    """Manifesting prolonged symptoms of breathlessness and a productive cough, the patient has received a diagnosis of Chronic Obstructive Pulmonary Disease (COPD), and a comprehensive treatment involving bronchodilators and lifestyle modifications has been recommended.""",
    """The patient, exhibiting extensive lung damage and significant shortness of breath, has been diagnosed with Emphysema, requiring meticulous management with bronchodilators and pulmonary rehabilitation to improve lung function.""",
    """Chronic Bronchitis has been diagnosed in the patient presenting with a chronic cough and frequent respiratory infections, necessitating a treatment plan inclusive of antibiotics and chest physiotherapy,""",
    )).toDS.toDF("text")

val result = clf_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+-------------------------------------+
|                                                                                              result|                               result|
+----------------------------------------------------------------------------------------------------+-------------------------------------+
|[The patient, experiencing recurrent episodes of wheezing and shortness of breath, has been diagn...|         [Asthma, Chronic bronchitis]|
|[Due to the patient's long history of tobacco use and persistent cough producing large amounts of...|           [COPD, Chronic bronchitis]|
|[The presence of dyspnea, chronic cough, and a history of smoking have led to the diagnosis of Em...|[Emphysema, COPD, Chronic bronchitis]|
|[The patient has been diagnosed with Chronic Bronchitis following the prolonged occurrence of cou...|                 [Chronic bronchitis]|
|[With a clinical presentation of persistent wheezing and respiratory discomfort, the patient has ...|              [Asthma, Other/Unknown]|
|[Manifesting prolonged symptoms of breathlessness and a productive cough, the patient has receive...|           [COPD, Chronic bronchitis]|
|[The patient, exhibiting extensive lung damage and significant shortness of breath, has been diag...|     [Emphysema, COPD, Other/Unknown]|
|[Chronic Bronchitis has been diagnosed in the patient presenting with a chronic cough and frequen...|                 [Chronic bronchitis]|
|[To manage the symptoms of Asthma, the patient has been advised to use inhaled corticosteroids re...|   [COPD, Asthma, Chronic bronchitis]|
|[In light of the COPD diagnosis, a comprehensive pulmonary rehabilitation program, coupled with l...|                               [COPD]|
|[The patient with Emphysema has been recommended to undergo oxygen therapy and regular use of bro...|                    [Emphysema, COPD]|
|[For the effective management of Chronic Bronchitis, a course of appropriate antibiotics, coupled...|                 [Chronic bronchitis]|
+----------------------------------------------------------------------------------------------------+-------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|multiclassifierdl_respiratory_disease|
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

Asthma:The patient was first diagnosed with asthma at the age of 12 following a severe respiratory infection. The patient reports experiencing wheezing, shortness of breath, and chest tightness, consistent with
asthma exacerbations. The patient has been prescribed a combination inhaler containing a long-acting beta-agonist and an inhaled corticosteroid to manage and prevent asthma symptoms. 

Chronic Obstructive Pulmonary Disease (COPD): Mr. Smith was diagnosed with Chronic Obstructive Pulmonary Disease (COPD) 5 years ago, primarily attributed to his 30-year smoking history. He frequently experiences chronic coughing with mucus production and difficulty in breathing,
especially during physical activities, indicative of his COPD. As part of his COPD management, the patient has been advised to use a bronchodilator inhaler regularly and undergo pulmonary rehabilitation to improve lung function and quality of life.

Emphysema: The patient's emphysema diagnosis was confirmed three years ago after a high-resolution CT scanshowed damage to the alveoli. The patient complains of progressive shortness of breath and an inability to sustain physical exertion, characteristics of emphysema.
Oxygen therapy has been recommended for the patient to alleviate the symptoms of emphysema and improve oxygen saturation levels.

Chronic Bronchitis: Mrs. Johnson has a recurring history of chronic bronchitis, often triggered by winter months and viral infections. She presents with persistent coughing that produces yellowish mucus, accompanied by fatigue and
chest discomfort, hallmark signs of chronic bronchitis. The treatment plan includes regular use of mucolytic agents, chest physiotherapy, and a short course of bronchodilator therapy to relieve symptoms of chronic bronchitis.

## Benchmarking

```bash
label                tp	   fp	   fn	   prec	       rec	       f1
Other/Unknown        13	   10	   34	   0.5652174	 0.27659574	 0.37142858
Emphysema            143   23	   38	   0.8614458	 0.7900553	 0.82420754
COPD                 267   27	   52	   0.90816325	 0.8369906	 0.8711256
No                   55	   8	   19	   0.8730159	 0.7432432	 0.8029197
Chronic bronchitis   241   27	   25	   0.8992537	 0.90601504	 0.9026217
Asthma               104   15	   25	   0.8739496	 0.8062016	 0.83870965
Macro-average        823   110   193   0.83017427  0.7265169   0.7748944
Micro-average        823   110   193   0.88210076  0.8100393   0.84453565
```
