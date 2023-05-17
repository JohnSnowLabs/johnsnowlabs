---
layout: model
title: Legal Multilabel Classification (MultiEURLEX, Slovak)
author: John Snow Labs
name: legmulticlf_multieurlex_slovak_combined
date: 2023-04-01
tags: [legal, classification, sk, licensed, multieurlex, level1, level2, tensorflow]
task: Text Classification
language: sk
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

The MultiEURLEX dataset was used to train a Multilabel Text Classification model that incorporates both Level 1 and Level 2 labels. This model is capable of classifying 95 distinct types of legal documents from Slovakia.

## Predicted Entities

`Amerika`, `potravinárska technológia`, `sociálne otázky`, `zdravie`, `strojárenstvo`, `komunikácia`, `technológia a technické predpisy`, `manažment`, `potravinárstvo`, `hospodárska súťaž`, `účtovníctvo`, `priemyselné štruktúry a politika`, `poškodzovanie životného prostredia`, `spotreba`, `Európa`, `občianske právo`, `ekonomická analýza`, `pozemná doprava`, `voľný pohyb kapitálu`, `obchod`, `podnikanie a súťaž`, `výroba`, `budovanie Európy`, `politická geografia`, `hutníctvo železa, ocele a železných kovov`, `vzdelanie a komunikácie`, `poľnohospodárske štruktúry a produkcia`, `elektronika a elektrotechnika`, `menové a finančné inštitúcie`, `dokumentácia`, `marketing`, `geografia`, `informácie a spracovanie informácií`, `obchodná politika`, `trestné právo`, `živočíšny produkt`, `financie EÚ`, `ekologická politika`, `medzinárodné právo`, `životné prostredie`, `energetická politika`, `zamestnanie a pracovné podmienky`, `energia`, `colná politika`, `zdaňovanie`, `spracované poľnohospodárske produkty`, `chémia`, `organizácia dopravy`, `Afrika`, `medzinárodný obchod`, `EURÓPSKA ÚNIA`, `výroba, technológia a výskum`, `spoločenský život`, `právo Európskej únie`, `financie`, `rastlinný produkt`, `Ázia a Oceánia`, `doprava`, `politika a bezpečnosť verejnosti`, `prírodné prostredie`, `informačná technológia a spracovanie údajov`, `poľnohospodárska činnosť`, `potraviny`, `regióny a regionálna politika`, `poľnohospodárska politika`, `hospodárska politika`, `rybárstvo`, `veda`, `hospodárska situácia`, `politika spolupráce`, `námorná a vnútrozemská riečna doprava`, `medzinárodné vzťahy`, `zamestnanosť`, `dopravná politika`, `ekonomická geografia`, `medzinárodná politika`, `medzinárodné organizácie`, `inštitúcie EÚ a európska verejná služba`, `obrana`, `letecká a kozmická doprava`, `výskum a duševné vlastníctvo`, `poľnohospodárstvo, lesníctvo a rybárstvo`, `rozpočet`, `ekonomika`, `medzinárodná bezpečnosť`, `nápoje a cukor`, `priemysel`, `prostriedky poľnohospodárskej výroby`, `organizácia podniku`, `výkonná moc a štátna správa`, `regióny členských štátov EÚ`, `prírodné a aplikované vedy`, `právo`, `politika`, `ceny`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legmulticlf_multieurlex_slovak_combined_sk_1.0.0_3.0_1680339464524.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legmulticlf_multieurlex_slovak_combined_sk_1.0.0_3.0_1680339464524.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

docClassifier = nlp.MultiClassifierDLModel().pretrained('legmulticlf_multieurlex_slovak_combined', 'sk', 'legal/models')\
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

result = light_model.annotate("""VYKONÁVACIE NARIADENIE KOMISIE (EÚ) 2015/176
z 5. februára 2015,
ktorým sa schvaľuje podstatná zmena špecifikácie názvu zapísaného do Registra zaručených tradičných špecialít [Prekmurska gibanica (ZTŠ)]
EURÓPSKA KOMISIA,
so zreteľom na Zmluvu o fungovaní Európskej únie,
so zreteľom na nariadenie Európskeho parlamentu a Rady (EÚ) č. 1151/2012 z 21. novembra 2012 o systémoch kvality pre poľnohospodárske výrobky a potraviny (1), a najmä na jeho článok 52 ods. 2,
keďže:
(1)
V súlade s článkom 53 ods. 1 prvým pododsekom nariadenia (EÚ) č. 1151/2012 Komisia preskúmala žiadosť Slovinska o schválenie zmeny špecifikácie zaručenej tradičnej špeciality „Prekmurska gibanica“, zapísanej do registra na základe nariadenia Komisie (EÚ) č. 172/2010 (2).
(2)
Vzhľadom na to, že nejde o nepodstatnú zmenu v zmysle článku 53 ods. 2 nariadenia (EÚ) č. 1151/2012, Komisia danú žiadosť o zmenu uverejnila v zmysle článku 50 ods. 2 písm. b) uvedeného nariadenia v Úradnom vestníku Európskej únie (3).
(3)
Vzhľadom na to, že Komisii nebola oznámená žiadna námietka v zmysle článku 51 nariadenia (EÚ) č. 1151/2012, zmena špecifikácie sa musí schváliť,
PRIJALA TOTO NARIADENIE:
Článok 1
Zmena špecifikácie uverejnená v Úradnom vestníku Európskej únie týkajúca sa názvu „Prekmurska gibanica“ (ZTŠ) sa schvaľuje.
Článok 2
Toto nariadenie nadobúda účinnosť dvadsiatym dňom po jeho uverejnení v Úradnom vestníku Európskej únie.
Toto nariadenie je záväzné v celom rozsahu a priamo uplatniteľné vo všetkých členských štátoch.
V Bruseli 5. februára 2015""")

```

</div>

## Results

```bash
potravinárstvo,spotreba,Európa,obchod,politická geografia,marketing,geografia,ekonomická geografia
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legmulticlf_multieurlex_slovak_combined|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[class]|
|Language:|sk|
|Size:|13.0 MB|

## References

https://huggingface.co/datasets/nlpaueb/multi_eurlex

## Benchmarking

```bash
 
labels                                      precision    recall  f1-score   support
Amerika                                         0.76      0.47      0.58        87
potravinárska technológia                       1.00      0.02      0.04        45
sociálne otázky                                 0.84      0.72      0.78       379
zdravie                                         0.89      0.79      0.84       365
strojárenstvo                                   0.82      0.57      0.67       171
komunikácia                                     1.00      0.95      0.97       164
technológia a technické predpisy                0.60      0.11      0.19        80
manažment                                       0.81      0.68      0.74       161
potravinárstvo                                  1.00      0.06      0.12        32
hospodárska súťaž                               0.96      0.57      0.72       188
účtovníctvo                                     0.83      0.11      0.20        44
priemyselné štruktúry a politika                0.97      0.35      0.52        85
poškodzovanie životného prostredia              1.00      0.06      0.11        34
spotreba                                        0.87      0.76      0.81       455
Európa                                          0.80      0.33      0.46       123
občianske právo                                 0.80      0.13      0.22        31
ekonomická analýza                              1.00      0.04      0.07        27
pozemná doprava                                 1.00      0.05      0.10        56
voľný pohyb kapitálu                            0.94      0.77      0.85       284
obchod                                          0.87      0.60      0.71       109
podnikanie a súťaž                              0.90      0.89      0.90       631
výroba                                          0.87      0.39      0.54        67
budovanie Európy                                0.73      0.26      0.38        31
politická geografia                             0.93      0.73      0.82        59
hutníctvo železa, ocele a železných kovov       0.81      0.34      0.48        38
vzdelanie a komunikácie                         0.80      0.21      0.34        75
poľnohospodárske štruktúry a produkcia          0.78      0.16      0.27        43
elektronika a elektrotechnika                   0.83      0.52      0.64        92
menové a finančné inštitúcie                    1.00      0.16      0.28        31
dokumentácia                                    0.00      0.00      0.00        24
marketing                                       1.00      0.22      0.36        18
geografia                                       0.89      0.79      0.84       307
informácie a spracovanie informácií             0.80      0.39      0.53        51
obchodná politika                               0.92      0.84      0.88       204
trestné právo                                   0.80      0.11      0.20        35
živočíšny produkt                               0.78      0.58      0.66        99
financie EÚ                                     0.91      0.78      0.84       318
ekologická politika                             0.82      0.47      0.60       158
medzinárodné právo                              0.80      0.35      0.49        34
životné prostredie                              1.00      0.73      0.84        91
energetická politika                            1.00      0.31      0.47        36
zamestnanie a pracovné podmienky                0.87      0.90      0.89       786
energia                                         0.61      0.10      0.18       107
colná politika                                  0.62      0.19      0.29        27
zdaňovanie                                      0.00      0.00      0.00        17     
spracované poľnohospodárske produkty            0.73      0.16      0.26        69
chémia                                          0.00      0.00      0.00        12
organizácia dopravy                             0.92      0.51      0.66       107
Afrika                                          0.89      0.78      0.83       371
medzinárodný obchod                             0.91      0.40      0.56       107
EURÓPSKA ÚNIA                                   0.97      0.53      0.69        58
výroba, technológia a výskum                    0.78      0.25      0.38       122
spoločenský život                               0.81      0.50      0.61       151
právo Európskej únie                            0.74      0.44      0.56        45
financie                                        0.92      0.86      0.89       477
rastlinný produkt                               0.75      0.08      0.15        36
Ázia a Oceánia                                  0.90      0.84      0.87       316
doprava                                         0.81      0.59      0.68       140
politika a bezpečnosť verejnosti                0.88      0.44      0.58        32
prírodné prostredie                             0.90      0.88      0.89       562
informačná technológia a spracovanie údajov     0.89      0.27      0.41        63
poľnohospodárska činnosť                        0.78      0.42      0.55       198
potraviny                                       0.00      0.00      0.00        14
regióny a regionálna politika                   0.84      0.62      0.71       115
poľnohospodárska politika                       0.80      0.53      0.64       165
hospodárska politika                            1.00      0.03      0.07        86
rybárstvo                                       0.00      0.00      0.00        21
veda                                            0.95      0.71      0.81        85
hospodárska situácia                            0.96      0.74      0.84       210
politika spolupráce                             0.00      0.00      0.00        12
námorná a vnútrozemská riečna doprava           0.83      0.43      0.56        56
medzinárodné vzťahy                             0.73      0.38      0.50        50
zamestnanosť                                    0.97      0.73      0.83       126
dopravná politika                               0.92      0.43      0.59       228
ekonomická geografia                            0.00      0.00      0.00        31
medzinárodná politika                           0.95      0.63      0.76       139
medzinárodné organizácie                        0.42      0.09      0.15        55
inštitúcie EÚ a európska verejná služba         0.00      0.00      0.00        28
obrana                                          0.87      0.35      0.50       130
letecká a kozmická doprava                      0.83      0.33      0.48        45
výskum a duševné vlastníctvo                    0.00      0.00      0.00        22
poľnohospodárstvo, lesníctvo a rybárstvo        1.00      0.23      0.38        30
rozpočet                                        0.78      0.26      0.39       136
ekonomika                                       1.00      0.18      0.31        44
medzinárodná bezpečnosť                         0.67      0.38      0.48        16
nápoje a cukor                                  0.84      0.38      0.52       173
priemysel                                       0.0       0.0       0.0         37
prostriedky poľnohospodárskej výroby            1.0       0.24      0.39        49
organizácia podniku                             1.0       0.39      0.56        31
výkonná moc a štátna správa                     1.0       0.47      0.64        19
regióny členských štátov EÚ                     0.93      0.56      0.7        170
prírodné a aplikované vedy                      0.69      0.42      0.52       113
právo                                           1.0       0.22      0.36        18
politika                                        0.9       0.53      0.66       175
ceny                                            0.8       0.36      0.5         78
   micro-avg       0.88      0.61      0.72     11872
   macro-avg       0.77      0.39      0.48     11872
weighted-avg       0.86      0.61      0.69     11872
 samples-avg       0.82      0.61      0.67     11872
F1-micro-averaging: 0.7228042301772504
ROC:  0.8025993754073506

```