---
layout: model
title: Legal Multilabel Classification (MultiEURLEX, German)
author: John Snow Labs
name: legmulticlf_multieurlex_german_combined
date: 2023-04-01
tags: [legal, classification, de, licensed, multieurlex, level1, level2, tensorflow]
task: Text Classification
language: de
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MultiClassifierDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The MultiEURLEX dataset was used to train a Multilabel Text Classification model that incorporates both Level 1 and Level 2 labels. This model is capable of classifying 38 distinct types of legal documents from German.

## Predicted Entities

`Landwirtschaftliche Erwerbstätigkeit`, `Preis`, `Getränk und Zucker`, `Internationaler Handel`, `Ozeanien`, `Agrarproduktion und Agrarstrukturen`, `geografie`, `umwelt`, `Internationale Politik`, `Internationales Recht`, ` und forstwirtschaft, fischerei`, `Nahrungsmittel`, `Europa`, `Landwirtschaftliches Betriebsmittel`, `Fischerei`, `Politisches Leben und öffentliche Sicherheit`, `Afrika`, `Finanzen der Europäischen Union`, `Pflanzliches Erzeugnis`, `Zolltarifpolitik`, `handel`, `agrarerzeugnisse und lebensmittel`, `Institutionen der Europäischen Union und Europäischer Öffentlicher Dienst`, `EUROPÄISCHE UNION`, `Politische Geografie`, `soziale fragen`, `Vermarktung`, `beschäftigung und arbeitsbedingungen`, `finanzwesen`, `Wirtschaftsverkehr`, ` und Binnenschiffsverkehr`, `internationale beziehungen`, `Gesundheit`, `Beschäftigung`, `Regionen der Mitgliedstaaten der Europäischen Union`, `Verbrauch`, `Wirtschaftsgeografie`, `Agrarpolitik`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legmulticlf_multieurlex_german_combined_de_1.0.0_3.0_1680346598548.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legmulticlf_multieurlex_german_combined_de_1.0.0_3.0_1680346598548.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")\
    .setCleanupMode("shrink")

embeddings = nlp.UniversalSentenceEncoder.pretrained()\
    .setInputCols("document")\
    .setOutputCol("sentence_embeddings")

docClassifier = nlp.MultiClassifierDLModel().pretrained('legmulticlf_multieurlex_german_combined', 'de', 'legal/models')\
    .setInputCols("sentence_embeddings") \
    .setOutputCol("class")

pipeline = nlp.Pipeline(
    stages=[
        document_assembler,
        embeddings,
        docClassifier
    ]
)

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = pipeline.fit(empty_data)

light_model = nlp.LightPipeline(model)

result = light_model.annotate("""DURCHFÜHRUNGSVERORDNUNG (EU) 2015/176 DER KOMMISSION
vom 5. Februar 2015
zur Genehmigung einer nicht geringfügigen Änderung der Spezifikation einer im Register der garantiert traditionellen Spezialitäten eingetragenen Bezeichnung (Prekmurska gibanica (g. t. S.))
DIE EUROPÄISCHE KOMMISSION -
gestützt auf den Vertrag über die Arbeitsweise der Europäischen Union,
gestützt auf die Verordnung (EU) Nr. 1151/2012 des Europäischen Parlaments und des Rates vom 21. November 2012 über Qualitätsregelungen für Agrarerzeugnisse und Lebensmittel (1), insbesondere auf Artikel 52 Absatz 2,
in Erwägung nachstehender Gründe:
(1)
Gemäß Artikel 53 Absatz 1 Unterabsatz 1 der Verordnung (EU) Nr. 1151/2012 hat die Kommission den Antrag Sloweniens auf Genehmigung einer Änderung der Spezifikation der garantiert traditionellen Spezialität „Prekmurska gibanica“ geprüft, die mit der Verordnung (EU) Nr. 172/2010 der Kommission (2) eingetragen worden ist.
(2)
Da es sich nicht um eine geringfügige Änderung im Sinne von Artikel 53 Absatz 2 der Verordnung (EU) Nr. 1151/2012 handelt, hat die Kommission den Antrag auf Änderung gemäß Artikel 50 Absatz 2 Buchstabe b der genannten Verordnung im Amtsblatt der Europäischen Union (3) veröffentlicht.
(3)
Bei der Kommission ist kein Einspruch gemäß Artikel 51 der Verordnung (EU) Nr. 1151/2012 eingegangen; daher sollte die Änderung der Spezifikation genehmigt werden -
HAT FOLGENDE VERORDNUNG ERLASSEN:
Artikel 1
Die im Amtsblatt der Europäischen Union veröffentlichte Änderung der Spezifikation für die Bezeichnung „Prekmurska gibanica“ (g. t. S.) wird genehmigt.
Artikel 2
Diese Verordnung tritt am zwanzigsten Tag nach ihrer Veröffentlichung im Amtsblatt der Europäischen Union in Kraft.
Diese Verordnung ist in allen ihren Teilen verbindlich und gilt unmittelbar in jedem Mitgliedstaat.
Brüssel, den 5. Februar 2015""")

```

</div>

## Results

```bash
geografie,Europa,handel,agrarerzeugnisse und lebensmittel,Politische Geografie,Vermarktung,Verbrauch,Wirtschaftsgeografie
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legmulticlf_multieurlex_german_combined|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[class]|
|Language:|de|
|Size:|13.0 MB|

## References

https://huggingface.co/datasets/nlpaueb/multi_eurlex

## Benchmarking

```bash
 
labels                                                                  precision    recall  f1-score   support
Landwirtschaftliche Erwerbstätigkeit                                           0.65      0.24      0.35       83
Preis                                                                          0.82      0.74      0.78      270
Getränk und Zucker                                                             0.57      0.13      0.22       30
Internationaler Handel                                                         0.81      0.47      0.59      107
Ozeanien                                                                       1.00      0.37      0.54       19
Agrarproduktion und Agrarstrukturen                                            0.79      0.64      0.71      461
geografie                                                                      0.83      0.57      0.68      321
umwelt                                                                         0.70      0.40      0.51      107
Internationale Politik                                                         0.90      0.54      0.68      100
Internationales Recht                                                          0.80      0.55      0.66      119
 und forstwirtschaft, fischerei                                                0.78      0.23      0.35       31
Nahrungsmittel                                                                 0.84      0.44      0.58       96
Europa                                                                         0.87      0.74      0.80      187
Landwirtschaftliches Betriebsmittel                                            0.65      0.31      0.42      126
Fischerei                                                                      0.74      0.46      0.57       70
Politisches Leben und öffentliche Sicherheit                                   0.76      0.42      0.54      144
Afrika                                                                         0.73      0.45      0.56       88
Finanzen der Europäischen Union                                                0.65      0.48      0.55      129
Pflanzliches Erzeugnis                                                         0.93      0.72      0.81      166
Zolltarifpolitik                                                               0.84      0.55      0.66      321
handel                                                                         0.93      0.28      0.43       46
agrarerzeugnisse und lebensmittel                                              0.98      0.95      0.96      124
Institutionen der Europäischen Union und Europäischer Öffentlicher Dienst      0.65      0.33      0.44       45
EUROPÄISCHE UNION                                                              0.97      0.68      0.80       56
Politische Geografie                                                           0.96      0.64      0.77      110
soziale fragen                                                                 0.80      0.67      0.73      243
Vermarktung                                                                    0.85      0.60      0.70      387
beschäftigung und arbeitsbedingungen                                           0.85      0.71      0.78      272
finanzwesen                                                                    0.83      0.42      0.56      151
Wirtschaftsverkehr                                                             0.84      0.79      0.82      399
 und Binnenschiffsverkehr                                                      1.00      0.17      0.30       40
internationale beziehungen                                                     0.91      0.63      0.75      221
Gesundheit                                                                     0.91      0.93      0.92      847
Beschäftigung                                                                  0.86      0.92      0.89      814
Regionen der Mitgliedstaaten der Europäischen Union                            0.80      0.65      0.72      284
Verbrauch                                                                      0.75      0.84      0.79      489
Wirtschaftsgeografie                                                           0.77      0.42      0.54      157
Agrarpolitik                                                                   0.75      0.28      0.40      141
   micro-avg       0.84      0.67      0.77      7801
   macro-avg       0.82      0.54      0.63      7801
weighted-avg       0.83      0.67      0.73      7801
 samples-avg       0.81      0.67      0.71      7801
F1-micro-averaging: 0.7452541770351937
ROC:  0.8223863679668545

```