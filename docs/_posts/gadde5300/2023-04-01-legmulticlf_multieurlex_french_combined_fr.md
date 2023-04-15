---
layout: model
title: Legal Multilabel Classification (MultiEURLEX, French)
author: John Snow Labs
name: legmulticlf_multieurlex_french_combined
date: 2023-04-01
tags: [legal, classification, fr, licensed, multieurlex, level1, level2, tensorflow]
task: Text Classification
language: fr
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

The MultiEURLEX dataset was used to train a Multilabel Text Classification model that incorporates both Level 1 and Level 2 labels. This model is capable of classifying 95 distinct types of legal documents from French.

## Predicted Entities

`géographie économique`, `documentation`, `emploi et travail`, `production`, `échanges économiques et commerciaux`, `institutions financières et crédit`, `droit`, `entreprise et concurrence`, `Europe`, `électronique et électrotechnique`, `recherche et propriété intellectuelle`, `vie sociale`, `emploi`, `relations internationales`, `pêche`, `politique internationale`, `produit végétal`, `technologie alimentaire`, `économie`, `métallurgie et sidérurgie`, `gestion administrative`, `politique commerciale`, `politique des transports`, `milieu naturel`, `finances de l&#39;Union européenne`, `situation économique`, `consommation`, `libre circulation des capitaux`, `organisation des transports`, `droit pénal`, `sécurité internationale`, `transports maritime et fluvial`, `produit animal`, `Amérique`, `transports aérien et spatial`, `production, technologie et recherche`, `énergie`, `questions sociales`, `sciences`, `droit international`, `politique de coopération`, `politique tarifaire`, `industrie mécanique`, `finances`, `industrie`, `transport terrestre`, `transports`, `vie politique et sécurité publique`, `produit agricole transformé`, `organisations internationales`, `politique et structures industrielles`, `politique énergétique`, `vie politique`, `informatique et traitement des données`, `détérioration de l&#39;environnement`, `fiscalité`, `géographie politique`, `analyse économique`, `politique agricole`, `droit de l&#39;Union européenne`, `système d&#39;exploitation agricole`, `échanges économiques`, `information et traitement de l&#39;information`, `gestion comptable`, `produit alimentaire`, `région et politique régionale`, `boisson et sucre`, `éducation et communication`, `alimentaire`, `budget`, `concurrence`, `commerce international`, `défense`, `chimie`, `commercialisation`, `activité agricole`, `production et structures agricoles`, `UNION EUROPÉENNE`, `prix`, `construction européenne`, `géographie`, `institutions de l&#39;Union européenne et fonction publique européenne`, `environnement`, `pouvoir exécutif et administration publique`, `politique économique`, `communication`, `technologie et réglementation technique`, ` Océanie`, `agriculture, sylviculture et pêche`, `sciences naturelles et appliquées`, `politique de l&#39;environnement`, `moyen de production agricole`, `Afrique`, `régions des États membres de l&#39;Union européenne`, `droit civil`, `droits et libertés`, `santé`, `organisation de l&#39;entreprise`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legmulticlf_multieurlex_french_combined_fr_1.0.0_3.0_1680343957532.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legmulticlf_multieurlex_french_combined_fr_1.0.0_3.0_1680343957532.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

docClassifier = nlp.MultiClassifierDLModel().pretrained('legmulticlf_multieurlex_french_combined', 'sk', 'legal/models')\
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

result = light_model.annotate("""RÈGLEMENT D'EXÉCUTION (UE) 2015/176 DE LA COMMISSION
du 5 février 2015
approuvant une modification non mineure du cahier des charges d'une dénomination enregistrée dans le registre des spécialités traditionnelles garanties [Prekmurska gibanica (STG)]
LA COMMISSION EUROPÉENNE,
vu le traité sur le fonctionnement de l'Union européenne,
vu le règlement (UE) no 1151/2012 du Parlement européen et du Conseil du 21 novembre 2012 relatif aux systèmes de qualité applicables aux produits agricoles et aux denrées alimentaires (1), et notamment son article 52, paragraphe 2,
considérant ce qui suit:
(1)
Conformément à l'article 53, paragraphe 1, premier alinéa, du règlement (UE) no 1151/2012, la Commission a examiné la demande de la Slovénie pour l'approbation d'une modification du cahier des charges de la spécialité traditionnelle garantie «Prekmurska gibanica», enregistrée en vertu du règlement (UE) no 172/2010 de la Commission (2).
(2)
La modification en question n'étant pas mineure au sens de l'article 53, paragraphe 2, du règlement (UE) no 1151/2012, la Commission a publié la demande de modification, en application de l'article 50, paragraphe 2, point b), dudit règlement, au Journal officiel de l'Union européenne (3).
(3)
Aucune déclaration d'opposition, conformément à l'article 51 du règlement (UE) no 1151/2012, n'ayant été notifiée à la Commission, la modification du cahier des charges doit être approuvée,
A ADOPTÉ LE PRÉSENT RÈGLEMENT:
Article premier
La modification du cahier des charges publiée au Journal officiel de l'Union européenne concernant la dénomination «Prekmurska gibanica» (STG) est approuvée.
Article 2
Le présent règlement entre en vigueur le vingtième jour suivant celui de sa publication au Journal officiel de l'Union européenne.
Le présent règlement est obligatoire dans tous ses éléments et directement applicable dans tout État membre.
Fait à Bruxelles, le 5 février 2015.""")

```

</div>

## Results

```bash
géographie économique,échanges économiques et commerciaux,Europe,consommation,géographie politique,agro-alimentaire,commercialisation,géographie,régions des États membres de l&#39;Union européenne
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legmulticlf_multieurlex_french_combined|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[class]|
|Language:|fr|
|Size:|13.0 MB|

## References

https://huggingface.co/datasets/nlpaueb/multi_eurlex

## Benchmarking

```bash
 
labels                                                                  precision    recall  f1-score   support
géographie économique                                                       0.73      0.38      0.50       80
documentation                                                               1.00      0.02      0.04       47
emploi et travail                                                           0.74      0.39      0.51       99
production                                                                  0.92      0.72      0.81      382
échanges économiques et commerciaux                                         0.80      0.76      0.78      385
institutions financières et crédit                                          0.87      0.50      0.63      142
droit                                                                       0.92      0.82      0.87      555
entreprise et concurrence                                                   0.96      0.87      0.91      467
Europe                                                                      1.00      0.09      0.17       32
électronique et électrotechnique                                            0.89      0.48      0.63       33
recherche et propriété intellectuelle                                       0.71      0.35      0.47       48
vie sociale                                                                 0.52      0.16      0.25       73
emploi                                                                      0.83      0.52      0.64      143
relations internationales                                                   0.93      0.75      0.83      314
pêche                                                                       0.79      0.30      0.43       37
politique internationale                                                    0.94      0.77      0.85       66
produit végétal                                                             0.98      0.60      0.74      138
technologie alimentaire                                                     0.77      0.55      0.64      172
économie                                                                    0.29      0.06      0.10       34
métallurgie et sidérurgie                                                   0.65      0.69      0.67      168
gestion administrative                                                      0.00      0.00      0.00       18
politique commerciale                                                       0.00      0.00      0.00       88
politique des transports                                                    0.78      0.66      0.71       99
milieu naturel                                                              0.74      0.49      0.59       47
finances de l&#39;Union européenne                                          0.67      0.20      0.31       20
situation économique                                                        0.87      0.42      0.57       31
consommation                                                                0.64      0.42      0.50       65
libre circulation des capitaux                                              0.93      0.45      0.61       31
organisation des transports                                                 1.00      0.27      0.42       52
droit pénal                                                                 0.80      0.56      0.66      116
sécurité internationale                                                     0.78      0.69      0.73      181
transports maritime et fluvial                                              0.91      0.77      0.83      277
produit animal                                                              0.74      0.67      0.70      112
Amérique                                                                    1.00      0.33      0.50       18
transports aérien et spatial                                                0.86      0.32      0.46       19
production, technologie et recherche                                        0.62      0.28      0.38       18
énergie                                                                     0.92      0.85      0.89      626
questions sociales                                                          0.89      0.67      0.77      384
sciences                                                                    0.91      0.71      0.80      464
droit international                                                         0.71      0.54      0.61      206
politique de coopération                                                    0.00      0.00      0.00       27
politique tarifaire                                                         0.65      0.33      0.43       46
industrie mécanique                                                         0.62      0.34      0.44       76
finances                                                                    0.75      0.53      0.62       97
industrie                                                                   0.85      0.47      0.61       36
transport terrestre                                                         0.71      0.29      0.41       35
transports                                                                  0.90      0.74      0.81       89
vie politique et sécurité publique                                          0.87      0.62      0.72      110
produit agricole transformé                                                 0.75      0.40      0.52       45
organisations internationales                                               1.00      0.08      0.15       12
politique et structures industrielles                                       0.66      0.36      0.47       69
politique énergétique                                                       0.00      0.00      0.00       36
vie politique                                                               0.92      0.77      0.84      309
informatique et traitement des données                                      0.62      0.05      0.08      111
détérioration de l&#39;environnement                                        0.67      0.25      0.36      121
fiscalité                                                                   0.71      0.49      0.58       85
géographie politique                                                        0.47      0.19      0.27       47
analyse économique                                                          0.00      0.00      0.00       18
politique agricole                                                          0.91      0.82      0.86      195
droit de l&#39;Union européenne                                             0.80      0.61      0.70      161
système d&#39;exploitation agricole                                         0.90      0.48      0.63       77
échanges économiques                                                        1.00      0.03      0.06       30
information et traitement de l&#39;information                              0.80      0.08      0.14       53
gestion comptable                                                           0.99      0.95      0.97      157
produit alimentaire                                                         0.67      0.35      0.46       17
région et politique régionale                                               0.80      0.23      0.36       35
boisson et sucre                                                            0.71      0.47      0.57      173
éducation et communication                                                  0.33      0.02      0.03       56
alimentaire                                                                 0.72      0.42      0.53      149
budget                                                                      0.83      0.25      0.39       79
concurrence                                                                 0.96      0.76      0.85      197
commerce international                                                      0.99      0.73      0.84      129
défense                                                                     0.85      0.54      0.66      233
chimie                                                                      1.00      0.11      0.20       36
commercialisation                                                           0.84      0.72      0.77      310
activité agricole                                                           0.00      0.00      0.00       11
production et structures agricoles                                          0.81      0.51      0.62       57
UNION EUROPÉENNE                                                            0.87      0.64      0.74      166
prix                                                                        1.00      0.06      0.11       17
construction européenne                                                     1.00      0.06      0.12       16
géographie                                                                  0.75      0.40      0.52       30
institutions de l&#39;Union européenne et fonction publique européenne      0.00      0.00      0.00       16
environnement                                                               0.80      0.47      0.59       43
pouvoir exécutif et administration publique                                 0.68      0.28      0.40       46
politique économique                                                        0.77      0.57      0.66      129
communication                                                               0.60      0.26      0.37       34
technologie et réglementation technique                                     0.88      0.67      0.76      192
 Océanie                                                                    0.67      0.08      0.14       26
agriculture, sylviculture et pêche                                          0.99      0.76      0.86       90
sciences naturelles et appliquées                                           0.83      0.31      0.45      109
politique de l&#39;environnement                                            0.89      0.47      0.62       51
moyen de production agricole                                                0.75      0.09      0.16       33
Afrique                                                                     0.87      0.83      0.85      300
régions des États membres de l&#39;Union européenne                         0.91      0.89      0.90      778
droit civil                                                                 0.79      0.41      0.54      128
droits et libertés                                                          0.65      0.51      0.57      146
santé                                                                       0.50      0.14      0.22       35
organisation de l&#39;entreprise                                            0.67      0.03      0.06       61
   micro-avg       0.86      0.62      0.72     12257
   macro-avg       0.74      0.42      0.50     12257
weighted-avg       0.83      0.62      0.69     12257
 samples-avg       0.82      0.62      0.68     12257
F1-micro-averaging: 0.7210601041173686
ROC:  0.8058916850998259

```