---
layout: model
title: Text Classification for Age
author: John Snow Labs
name: genericclassifier_age_e5
date: 2024-02-12
tags: [en, licensed, classification, age]
task: Text Classification
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.0
supported: true
annotator: GenericClassifierModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The GenericClassifierModel is a sophisticated text classification tool tailored to identify and categorize text according to different age groups. This model distinguishes among 'Old Adult', 'Adult', and 'Child and Teen' contexts, providing valuable insights into textual data that references age-specific scenarios or concerns. Detailed information about the classes is as follows:

`Old Adult`: This category includes texts that pertain to older adults, often addressing age-specific health issues, lifestyle considerations, or geriatric care. For instance, a text might discuss mobility challenges or medical conditions more prevalent in elderly populations.

`Adult`: Texts under this classification refer to the adult age group, encompassing a wide range of topics from general health care to workplace issues. These texts often deal with health, social, and economic aspects relevant to the adult population. 

`Child and Teen`: This classification captures texts related to children and teenagers, focusing on pediatric health, developmental stages, educational concerns, and youth-related social issues.

`Other/Unknown`: This category includes texts where the patient's age is not specified or is irrelevant to the content. These texts may cover a wide range of topics applicable to all age groups or focus on general health and wellness issues that are not age-specific. For example, a text might discuss the importance of maintaining a balanced diet and regular exercise routine for overall health, without targeting a specific age group.

## Predicted Entities

`Old Adult`, `Adult`, `Child and Teen`, `Other/Unknown`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/genericclassifier_age_e5_en_5.2.1_3.0_1707776992202.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/genericclassifier_age_e5_en_5.2.1_3.0_1707776992202.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")
        
embeddings = E5Embeddings.pretrained("e5_large", 'en')\
    .setInputCols(["document"])\
    .setOutputCol("embeddings")\
    .setMaxSentenceLength(512)

features_asm = FeaturesAssembler()\
    .setInputCols(["embeddings"])\
    .setOutputCol("features")

generic_classifier = GenericClassifierModel.pretrained("genericclassifier_age_e5", "en", "clinical/models")\
    .setInputCols(["features"])\
    .setOutputCol("prediction")

pipeline = Pipeline(stages=[
    document_assembler,
    embeddings,
    features_asm,
    generic_classifier    
])

sample_texts = [
"""The patient presents with conditions often associated with the stresses and lifestyle of early career and possibly higher education stages, including sleep irregularities and repetitive stress injuries. There's a notable emphasis on preventative care, with discussions around lifestyle choices that can impact long-term health, such as smoking cessation, regular exercise, and balanced nutrition. The patient is also counseled on mental health, particularly in managing stress and anxiety that may arise from personal and professional responsibilities and ambitions at this stage of life.""",
"""The patient, in the infancy stage, is experiencing typical developmental milestones such as teething and learning to crawl. Regular check-ups focus on monitoring growth patterns, ensuring proper nutrition, especially with the transition from milk to solid foods, and addressing common infant concerns like colic and sleep patterns. Immunizations are up-to-date, following the recommended schedule for this critical early life stage.""",
"""The toddler patient shows normal signs of curiosity and motor skill development for their age. Concerns include potential delays in speech development and the challenges of transitioning from crib to bed. Nutritional guidance is provided, focusing on balanced diets and managing the picky eating phase common in toddlers. Safety in the home environment is also discussed, given the patient's increased mobility and exploratory behavior.""",
"""The senior patient presents with age-related issues such as reduced hearing and vision, arthritis, and memory lapses. Emphasis is on managing chronic conditions, maintaining social engagement, and adapting lifestyle to changing physical abilities. Discussions include medication management, dietary adjustments to suit older digestion, and the importance of regular, low-impact exercise.""",
"""The late teenage patient is dealing with final growth spurts, the stress of impending adulthood, and decisions about higher education or career paths. Health discussions include maintaining a balanced diet, the importance of regular sleep patterns, and managing academic and social pressures. Mental health support is considered crucial at this stage, with a focus on building resilience and coping mechanisms.""",
"""The patient, faces adjustments to a new lifestyle with changes in daily routines and social interactions. Health concerns include managing the transition from an active work life to more leisure time, which may impact physical and mental health. Preventative health measures are emphasized, along with the importance of staying mentally and physically active and engaged in the community."""
]

data = spark.createDataFrame(sample_texts, StringType()).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
        
val embeddings = E5Embeddings.pretrained("e5_large", 'en')\
    .setInputCols(["document"])\
    .setOutputCol("embeddings")\
    .setMaxSentenceLength(512)

val features_asm = new FeaturesAssembler()
    .setInputCols("embeddings")
    .setOutputCol("features")

val generic_classifier = GenericClassifierModel.pretrained("genericclassifier_age_e5", "en", "clinical/models")
    .setInputCols("features")
    .setOutputCol("prediction")

val pipeline = new PipelineModel().setStages(Array(
    document_assembler,
    embeddings,
    features_asm,
    generic_classifier    
))

val data = Seq(Array("""The patient presents with conditions often associated with the stresses and lifestyle of early career and possibly higher education stages, including sleep irregularities and repetitive stress injuries. There's a notable emphasis on preventative care, with discussions around lifestyle choices that can impact long-term health, such as smoking cessation, regular exercise, and balanced nutrition. The patient is also counseled on mental health, particularly in managing stress and anxiety that may arise from personal and professional responsibilities and ambitions at this stage of life.""",
"""The patient, in the infancy stage, is experiencing typical developmental milestones such as teething and learning to crawl. Regular check-ups focus on monitoring growth patterns, ensuring proper nutrition, especially with the transition from milk to solid foods, and addressing common infant concerns like colic and sleep patterns. Immunizations are up-to-date, following the recommended schedule for this critical early life stage.""",
"""The toddler patient shows normal signs of curiosity and motor skill development for their age. Concerns include potential delays in speech development and the challenges of transitioning from crib to bed. Nutritional guidance is provided, focusing on balanced diets and managing the picky eating phase common in toddlers. Safety in the home environment is also discussed, given the patient's increased mobility and exploratory behavior.""",
"""The senior patient presents with age-related issues such as reduced hearing and vision, arthritis, and memory lapses. Emphasis is on managing chronic conditions, maintaining social engagement, and adapting lifestyle to changing physical abilities. Discussions include medication management, dietary adjustments to suit older digestion, and the importance of regular, low-impact exercise.""",
"""The late teenage patient is dealing with final growth spurts, the stress of impending adulthood, and decisions about higher education or career paths. Health discussions include maintaining a balanced diet, the importance of regular sleep patterns, and managing academic and social pressures. Mental health support is considered crucial at this stage, with a focus on building resilience and coping mechanisms.""",
"""The patient, faces adjustments to a new lifestyle with changes in daily routines and social interactions. Health concerns include managing the transition from an active work life to more leisure time, which may impact physical and mental health. Preventative health measures are emphasized, along with the importance of staying mentally and physically active and engaged in the community.""")).toDF("text")


val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+----------------+
|                                                                                                text|          result|
+----------------------------------------------------------------------------------------------------+----------------+
|The patient presents with conditions often associated with the stresses and lifestyle of early ca...|         [Adult]|
|The patient, in the infancy stage, is experiencing typical developmental milestones such as teeth...|[Child and Teen]|
|The toddler patient shows normal signs of curiosity and motor skill development for their age. Co...|[Child and Teen]|
|The senior patient presents with age-related issues such as reduced hearing and vision, arthritis...|     [Old Adult]|
|The late teenage patient is dealing with final growth spurts, the stress of impending adulthood, ...|[Child and Teen]|
|The patient, faces adjustments to a new lifestyle with changes in daily routines and social inter...| [Other/Unknown]|
+----------------------------------------------------------------------------------------------------+----------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|genericclassifier_age_e5|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[features]|
|Output Labels:|[prediction]|
|Language:|en|
|Size:|4.3 MB|

## References

In-house annotated datasets

## Benchmarking

```bash
label           precision  recall  f1-score  support 
Adult           0.82       0.80    0.81      367     
Child and Teen  0.95       0.91    0.93      271     
Old Adult       0.84       0.83    0.84      187     
Other/Unknown   0.81       0.86    0.84      342     
accuracy        -          -       0.85      1167    
macro-avg       0.86       0.85    0.85      1167    
weighted-avg    0.85       0.85    0.85      1167    
```