---
layout: model
title: Multilabel Classification For LitCovid
author: John Snow Labs
name: multiclassifierdl_litcovid
date: 2023-07-04
tags: [en, classification, covid, pubmed, licensed, tensorflow]
task: Text Classification
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MultiClassifierDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Multi-label document classification identifies semantic categories at the document-level. The semantic categories are effective for grasping the main topics and searching for relevant literature in the biomedical domain. Unlike multi-class classification, which assigns only one label to an instance, multi-label classification can assign up to N labels to an instance. LitCovid is manually annotated multi-label document classification datasets for COVID-19 topics (7 labels).

The multilabel classification model decides relevant COVID-19 topics of the article based on its abstract.

There are 7 topics you will need to decide whether the article is related to. The followings are the topics and their definitions.
- Mechanism: underlying cause(s) of COVID-19 infections and transmission and possible drug mechanism of action. 
- Transmission: characteristics and modes of COVID-19 transmissions. 
- Diagnosis: COVID-19 assessment through symptoms, test results, and radiological features for COVID-19. 
- Treatment: treatment strategies, therapeutic procedures, and vaccine development for COVID-19. 
- Prevention: prevention, control, mitigation, and management strategies for COVID-19. 
- Case_Report: descriptions of specific patient cases related to COVID-19. 
- Epidemic_Forecasting: estimation on the trend of COVID-19 spread and related modeling approach.

## Predicted Entities

`Mechanism`, `Transmission`, `Diagnosis`, `Treatment`, `Prevention`, `Case_Report`, `Epidemic_Forecasting`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/multiclassifierdl_litcovid_en_4.4.4_3.0_1688487368052.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/multiclassifierdl_litcovid_en_4.4.4_3.0_1688487368052.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["document", "token"])\
    .setOutputCol("word_embeddings")

sentence_embeddings = SentenceEmbeddings()\
    .setInputCols(["document", "word_embeddings"])\
    .setOutputCol("sentence_embeddings")\
    .setPoolingStrategy("AVERAGE")

multi_classifier_dl = MultiClassifierDLModel.pretrained("multiclassifierdl_litcovid", "en", "clinical/models")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("category")
    
pipeline = Pipeline(
    stages = [
        document_assembler,
        tokenizer,
        word_embeddings,
        sentence_embeddings,
        multi_classifier_dl
    ])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = pipeline.fit(empty_data)

text = """Low level of plasminogen increases risk for mortality in COVID-19 patients. The pathophysiology of coronavirus disease 2019 (COVID-19), caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2), and especially of its complications is still not fully understood. In fact, a very high number of patients with COVID-19 die because of thromboembolic causes. A role of plasminogen, as precursor of fibrinolysis, has been hypothesized. In this study, we aimed to investigate the association between plasminogen levels and COVID-19-related outcomes in a population of 55 infected Caucasian patients (mean age: 69.8 +/- 14.3, 41.8% female). Low levels of plasminogen were significantly associated with inflammatory markers (CRP, PCT, and IL-6), markers of coagulation (D-dimer, INR, and APTT), and markers of organ dysfunctions (high fasting blood glucose and decrease in the glomerular filtration rate). A multidimensional analysis model, including the correlation of the expression of coagulation with inflammatory parameters, indicated that plasminogen tended to cluster together with IL-6, hence suggesting a common pathway of activation during disease's complication. Moreover, low levels of plasminogen strongly correlated with mortality in COVID-19 patients even after multiple adjustments for presence of confounding. These data suggest that plasminogen may play a pivotal role in controlling the complex mechanisms beyond the COVID-19 complications, and may be useful both as biomarker for prognosis and for therapeutic target against this extremely aggressive infection."""

df = spark.createDataFrame([[text]]).toDF("text")

result = model.transform(df)

result.select("text", "category.result").show(truncate=120)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols(Array("document"))
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("document", "token"))
    .setOutputCol("word_embeddings")

val sentence_embeddings = new SentenceEmbeddings()
    .setInputCols(Array("document", "word_embeddings"))
    .setOutputCol("sentence_embeddings")
    .setPoolingStrategy("AVERAGE")

val multi_classifier_dl = MultiClassifierDLModel.pretrained("multiclassifierdl_litcovid", "en", "clinical/models")
    .setInputCols(Array("sentence_embeddings"))
    .setOutputCol("category")
    
val pipeline = new Pipeline().setStages(Array(
     document_assembler, 
     tokenizer,
     word_embeddings, 
     sentence_embeddings, 
     multi_classifier_dl))

val data = Seq("""Low level of plasminogen increases risk for mortality in COVID-19 patients. The pathophysiology of coronavirus disease 2019 (COVID-19), caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2), and especially of its complications is still not fully understood. In fact, a very high number of patients with COVID-19 die because of thromboembolic causes. A role of plasminogen, as precursor of fibrinolysis, has been hypothesized. In this study, we aimed to investigate the association between plasminogen levels and COVID-19-related outcomes in a population of 55 infected Caucasian patients (mean age: 69.8 +/- 14.3, 41.8% female). Low levels of plasminogen were significantly associated with inflammatory markers (CRP, PCT, and IL-6), markers of coagulation (D-dimer, INR, and APTT), and markers of organ dysfunctions (high fasting blood glucose and decrease in the glomerular filtration rate). A multidimensional analysis model, including the correlation of the expression of coagulation with inflammatory parameters, indicated that plasminogen tended to cluster together with IL-6, hence suggesting a common pathway of activation during disease's complication. Moreover, low levels of plasminogen strongly correlated with mortality in COVID-19 patients even after multiple adjustments for presence of confounding. These data suggest that plasminogen may play a pivotal role in controlling the complex mechanisms beyond the COVID-19 complications, and may be useful both as biomarker for prognosis and for therapeutic target against this extremely aggressive infection.""").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
+------------------------------------------------------------------------------------------------------------------------+---------------------------------+
|                                                                                                                    text|                           result|
+------------------------------------------------------------------------------------------------------------------------+---------------------------------+
|Low level of plasminogen increases risk for mortality in COVID-19 patients. The pathophysiology of coronavirus diseas...|[Mechanism, Treatment, Diagnosis]|
+------------------------------------------------------------------------------------------------------------------------+---------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|multiclassifierdl_litcovid|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[class]|
|Language:|en|
|Size:|11.7 MB|

## References

The training dataset is available [here](https://github.com/qingyu-qc/gpt_bionlp_benchmark/tree/main/Benchmarks/LitCovid)

## Benchmarking

```bash
| label                | precision | recall | f1-score | support |
|----------------------|-----------|--------|----------|---------|
| Case_Report          | 0.88      | 0.85   | 0.86     | 252     |
| Diagnosis            | 0.86      | 0.86   | 0.86     | 886     |
| Epidemic_Forecasting | 0.72      | 0.69   | 0.70     | 77      |
| Mechanism            | 0.84      | 0.85   | 0.85     | 609     |
| Prevention           | 0.92      | 0.91   | 0.92     | 1419    |
| Transmission         | 0.67      | 0.61   | 0.64     | 146     |
| Treatment            | 0.90      | 0.87   | 0.88     | 1221    |
| micro-avg            | 0.88      | 0.86   | 0.87     | 4610    |
| macro-avg            | 0.83      | 0.80   | 0.82     | 4610    |
| weighted-avg         | 0.88      | 0.86   | 0.87     | 4610    |
| samples-avg          | 0.89      | 0.89   | 0.88     | 4610    |
```