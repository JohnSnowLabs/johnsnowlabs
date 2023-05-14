---
layout: model
title: Financial NER on Responsibility and ESG Reports(Medium)
author: John Snow Labs
name: finner_responsibility_reports_md
date: 2023-05-14
tags: [en, ner, finance, licensed, responsibility, reports]
task: Named Entity Recognition
language: en
edition: Finance NLP 1.0.0
spark_version: 3.0
supported: true
annotator: FinanceNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This Financial NER model can extract up to 20 quantifiable entities, including KPI, from the Responsibility and ESG Reports of companies. This `medium` model has been trained with more data.

If you look for a `small` version of the model, you can find it [here](https://nlp.johnsnowlabs.com/2023/03/09/finner_responsibility_reports_en.html)

## Predicted Entities

`AGE`, `AMOUNT`, `COUNTABLE_ITEM`, `DATE_PERIOD`, `ECONOMIC_ACTION`, `ECONOMIC_KPI`, `ENVIRONMENTAL_ACTION`, `ENVIRONMENTAL_KPI`, `ENVIRONMENTAL_UNIT`, `ESG_ROLE`, `FACILITY_PLACE`, `ISO`, `PERCENTAGE`, `PROFESSIONAL_GROUP`, `RELATIVE_METRIC`, `SOCIAL_ACTION`, `SOCIAL_KPI`, `TARGET_GROUP`, `TARGET_GROUP_BUSINESS`, `WASTE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finner_responsibility_reports_md_en_1.0.0_3.0_1684066884328.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finner_responsibility_reports_md_en_1.0.0_3.0_1684066884328.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")\

sentence_detector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")\

tokenizer = nlp.Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")\
    .setContextChars(['.', ',', ';', ':', '!', '?', '*', '-', '(', ')', '"', "'", '%', '&'])

embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base", "en") \
    .setInputCols("sentence", "token") \
    .setOutputCol("embeddings")\
    .setMaxSentenceLength(512)\
    .setCaseSensitive(True)

ner_model = finance.NerModel.pretrained("finner_responsibility_reports_md", "en", "finance/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = nlp.NerConverter()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

nlpPipeline = nlp.Pipeline(stages=[
    document_assembler,
    sentence_detector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter
])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = nlpPipeline.fit(empty_data)

text = """The company has reduced its direct GHG emissions from 12,135 million tonnes of CO2e in 2017 to 4 million tonnes of CO2e in 2021. The indirect GHG emissions (scope 2) are mainly from imported energy, including electricity, heat, steam, and cooling, and the company has reduced its scope 2 emissions from 3 million tonnes of CO2e in 2017-2018 to 4 million tonnes of CO2e in 2020-2021. The scope 3 emissions are mainly from the use of sold products, and the emissions have increased from 377 million tonnes of CO2e in 2017 to 408 million tonnes of CO2e in 2021."""

data = spark.createDataFrame([[text]]).toDF("text")

result = model.transform(data)

result.select(F.explode(F.arrays_zip('ner_chunk.result', 'ner_chunk.metadata')).alias("cols")) \
          .select(F.expr("cols['0']").alias("chunk"),
                       F.expr("cols['1']['entity']").alias("label")).show(50, truncate = False)
```

</div>

## Results

```bash
+----------------------+------------------+
|chunk                 |label             |
+----------------------+------------------+
|direct GHG emissions  |ENVIRONMENTAL_KPI |
|12,135 million        |AMOUNT            |
|tonnes of CO2e        |ENVIRONMENTAL_UNIT|
|2017                  |DATE_PERIOD       |
|4 million             |AMOUNT            |
|tonnes of CO2e        |ENVIRONMENTAL_UNIT|
|2021                  |DATE_PERIOD       |
|indirect GHG emissions|ENVIRONMENTAL_KPI |
|scope 2               |ENVIRONMENTAL_KPI |
|imported energy       |ENVIRONMENTAL_KPI |
|electricity           |ENVIRONMENTAL_KPI |
|heat                  |ENVIRONMENTAL_KPI |
|steam                 |ENVIRONMENTAL_KPI |
|cooling               |ENVIRONMENTAL_KPI |
|scope 2 emissions     |ENVIRONMENTAL_KPI |
|3 million             |AMOUNT            |
|tonnes of CO2e        |ENVIRONMENTAL_UNIT|
|2017-2018             |DATE_PERIOD       |
|4 million             |AMOUNT            |
|tonnes of CO2e        |ENVIRONMENTAL_UNIT|
|2020-2021             |DATE_PERIOD       |
|scope 3 emissions     |ENVIRONMENTAL_KPI |
|sold                  |ECONOMIC_ACTION   |
|products              |SOCIAL_KPI        |
|emissions             |ENVIRONMENTAL_KPI |
|377 million           |AMOUNT            |
|tonnes of CO2e        |ENVIRONMENTAL_UNIT|
|2017                  |DATE_PERIOD       |
|408 million           |AMOUNT            |
|tonnes of CO2e        |ENVIRONMENTAL_UNIT|
|2021                  |DATE_PERIOD       |
+----------------------+------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finner_responsibility_reports_md|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|16.4 MB|

## References

In-house annotations on Responsibility and ESG Reports

## Benchmarking

```bash
label                    precision  recall  f1-score  support 
B-AMOUNT                 0.97       0.97    0.97      1207    
I-AMOUNT                 0.97       0.94    0.96      361     
B-ENVIRONMENTAL_KPI      0.79       0.81    0.80      1051    
I-ENVIRONMENTAL_KPI      0.74       0.88    0.81      716     
B-DATE_PERIOD            0.94       0.95    0.94      980     
I-DATE_PERIOD            0.90       0.95    0.92      498     
B-PERCENTAGE             0.99       0.99    0.99      695     
I-PERCENTAGE             0.99       1.00    1.00      692     
B-SOCIAL_KPI             0.66       0.74    0.70      481     
I-SOCIAL_KPI             0.56       0.33    0.41      43      
B-ENVIRONMENTAL_UNIT     0.94       0.96    0.95      459     
I-ENVIRONMENTAL_UNIT     0.91       0.86    0.88      268     
B-PROFESSIONAL_GROUP     0.85       0.92    0.88      358     
I-PROFESSIONAL_GROUP     0.94       0.94    0.94      32      
B-TARGET_GROUP           0.89       0.85    0.87      337     
I-TARGET_GROUP           0.76       0.95    0.84      59      
B-ENVIRONMENTAL_ACTION   0.72       0.68    0.70      341     
I-ENVIRONMENTAL_ACTION   1.00       0.56    0.71      18      
B-SOCIAL_ACTION          0.59       0.72    0.65      241     
B-ESG_ROLE               0.76       0.72    0.74      109     
I-ESG_ROLE               0.81       0.84    0.83      305     
B-ECONOMIC_KPI           0.77       0.67    0.71      219     
I-ECONOMIC_KPI           0.47       0.70    0.56      50      
B-RELATIVE_METRIC        0.92       0.98    0.95      147     
I-RELATIVE_METRIC        0.89       0.99    0.94      178     
B-FACILITY_PLACE         0.74       0.89    0.81      139     
I-FACILITY_PLACE         0.77       0.93    0.84      89      
B-COUNTABLE_ITEM         0.64       0.69    0.67      154     
I-COUNTABLE_ITEM         0.25       1.00    0.40      1       
B-WASTE                  0.84       0.64    0.73      126     
I-WASTE                  0.91       0.51    0.65      57      
B-ECONOMIC_ACTION        0.73       0.74    0.73      91      
I-ECONOMIC_ACTION        0.00       0.00    0.00      1       
B-TARGET_GROUP_BUSINESS  0.93       0.85    0.89      74      
I-TARGET_GROUP_BUSINESS  0.00       0.00    0.00      1       
B-AGE                    0.74       0.70    0.72      37      
I-AGE                    0.90       0.65    0.75      40      
B-ISO                    0.84       0.72    0.78      36      
I-ISO                    0.91       0.80    0.85      25      
micro avg                0.86       0.88    0.87      10716   
macro avg                0.75       0.75    0.74      10716   
weighted avg             0.86       0.88    0.87      10716  
```
