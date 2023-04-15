---
layout: model
title: Legal Multilabel Classification (MultiEURLEX, English, 70 Labels)
author: John Snow Labs
name: legmulticlf_multieurlex_english_combined_2
date: 2023-04-01
tags: [legal, classification, en, licensed, multieurlex, level1, level2, tensorflow]
task: Text Classification
language: en
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

The MultiEURLEX dataset was used to train a Multilabel Text Classification model that incorporates both Level 1 and Level 2 labels. This model is capable of classifying 70 distinct types of legal documents from English. `legmulticlf_multieurlex_english_combined` is another english model which is trained using the MultiEURLEX dataset.

## Predicted Entities

`chemistry`, `EU finance`, `production`, `industry`, `prices`, `distributive trades`, `finance`, `Europe`, `communications`, `civil law`, `Africa`, `agricultural activity`, `agricultural structures and production`, `farming systems`, `research and intellectual property`, `foodstuffs`, `organisation of transport`, `fisheries`, `food technology`, `electronics and electrical engineering`, `European Union law`, `marketing`, `foodstuff`, `EUROPEAN UNION`, `information and information processing`, `international trade`, `transport`, `politics`, `technology and technical regulations`, `regions of EU Member States`, `geography`, `international affairs`, `consumption`, `accounting`, `deterioration of the environment`, `beverages and sugar`, `cooperation policy`, `economic policy`, `land transport`, `European construction`, `regions and regional policy`, `leather and textile industries`, `animal product`, `natural environment`, `EU institutions and European civil service`, `employment and working conditions`, `health`, `agricultural policy`, `processed agricultural produce`, `economics`, `education and communications`, `means of agricultural production`, `trade`, `trade policy`, `plant product`, `tariff policy`, `executive power and public service`, `agriculture, forestry and fisheries`, `economic analysis`, `business and competition`, `international relations`, `environmental policy`, `iron, steel and other metal industries`, `Asia and Oceania`, `production, technology and research`, `political geography`, `social questions`, `environment`, `economic geography`, `law`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legmulticlf_multieurlex_english_combined_2_en_1.0.0_3.0_1680345764354.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legmulticlf_multieurlex_english_combined_2_en_1.0.0_3.0_1680345764354.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

docClassifier = nlp.MultiClassifierDLModel().pretrained('legmulticlf_multieurlex_english_combined_2', 'en', 'legal/models')\
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

result = light_model.annotate("""COMMISSION DECISION
of 26 October 2004
laying down detailed rules for the application of Council Directive 93/24/EEC as regards the statistical surveys on cattle population and production
(notified under document number C(2004) 4091)
(Text with EEA relevance)
(2004/761/EC)
THE COMMISSION OF THE EUROPEAN COMMUNITIES,
Having regard to the Treaty establishing the European Community,
Having regard to Council Directive 93/24/EEC of 1 June 1993 on the statistical surveys to be carried out on bovine animal production (1), and in particular Articles 1(2) and (3), 2(2), 3(2), 6, 8(1) and (2), 10(3) and 12(2) thereof,
Whereas:
(1)
Commission Decision 94/433/EC of 30 May 1994 laying down detailed rules for the application of Council Directive 93/24/EEC as regards the statistical surveys on cattle population and production (2) has been amended several times.
(2)
Precise definitions are required in order to carry out the surveys provided for in Directive 93/24/EEC. This requires the definition of the agricultural holdings covered by the survey. The different categories for the breakdown of the survey results, and the herd size classes and the territorial subdivisions according to which the Member States draw up the survey results at regular intervals must also be precisely defined. A standard definition of carcass weight is necessary for drawing up slaughtering statistics.
(3)
Under Directive 93/24/EEC, the Member States may, at their request, be authorised to carry out the May/June or November/December surveys in selected regions, provided that these surveys cover at least 70 % of the bovine population. Member States whose bovine population makes up only a small percentage of the overall livestock population of the Community may also, at their request, be authorised to dispense altogether with either the May/June or the November/December survey or to use the regional breakdown for the final results of the May/June survey. Finally, the Member States may, at their request, be authorised to conduct the prescribed breakdown by herd size classes for the results of the May/June survey.
(4)
Applications have been made by the Member States for the various types of derogation.
(5)
By reason of the accession of the Czech Republic, Cyprus, Estonia, Hungary, Latvia, Lithuania, Malta, Poland, Slovakia and Slovenia, it is necessary to make certain technical adaptations and to extend certain derogations to these new Member States.
(6)
Regulation (EC) No 1059/2003 of the European Parliament and the Council (3) establishes a common classification of territorial units for statistics (NUTS) for the Member States; the new NUTS nomenclature must therefore replace the previously defined regional levels.
(7)
Decision 94/433/EC should therefore be repealed.
(8)
This Decision is in accordance with the opinion of the Standing Committee on Agricultural Statistics,
HAS ADOPTED THIS DECISION:
Article 1
1. For the purposes of Article 2(2) of Directive 93/24/EEC, ‘agricultural holding’ means any technical and economic unit under single management which produces agricultural products.
2. The survey referred to in Article 1(1) of Directive 93/24/EEC shall cover:
(a)
agricultural holdings with a utilised agricultural area of 1 ha or more;
(b)
agricultural holdings with a utilised agricultural area of less than 1 ha, if their production is to a certain extent intended for sale or if their production unit exceeds certain natural thresholds.
3. Member States wishing to apply a different survey threshold shall, however, undertake to determine that threshold in such a way that only the smallest holdings are excluded, and that together the holdings excluded account for 1 % or less of the total standard gross margin, within the meaning of Commission Decision 85/377/EEC (4), of the Member State concerned.
Article 2
The definitions of the categories of bovines referred to in Articles 3(1), 10(2) and 12(2) of Directive 93/24/EEC are set out in Annex I of this Decision.
Article 3
For the territorial subdivisions referred to in Article 6(1) of Directive 93/24/EEC, the Member States shall follow the level of the common classification of territorial units for statistics (NUTS) defined in Annex II of this Decision. They do not need to compile results for regions in which the bovine population is less than 1 % of the national bovine population.
Article 4
The herd size classes referred to in Article 8(1) of Directive 93/24/EEC are set out in Annex III of this Decision.
Article 5
The carcass weight referred to in Article 10(1) of Directive 93/24/EEC is the weight of the slaughtered animal’s cold body after being skinned, bled and eviscerated, and after removal of the external genitalia, the limbs at the carpus and tarsus, the head, the tail, the kidneys and kidney fats, and the udder.
Article 6
1. The list of Member States authorised to carry out the May/June or November/December surveys in selected regions, on the understanding that these surveys cover at least 70 % of the bovine population, is set out in point (a) of Annex IV to this Decision.
2. The list of Member States authorised to carry out the November/December survey only is set out in point (b) of Annex IV to this Decision.
3. The list of Member States authorised to use the regional breakdown for the final results of the May/June survey is set out in point (c) of Annex IV to this Decision.
4. The list of Member States authorised to use the breakdown by herd size classes for the results of the May/June survey is set out in point (d) of Annex IV to this Decision.
Article 7
Decision 94/433/EC is repealed.
References made to the repealed Decision shall be construed to be made to the present Decision.
Article 8
This Decision is addressed to the Member States.
Done at Brussels, 26 October 2004.""")

```

</div>

## Results

```bash
farming systems,agri-foodstuffs,European Union law,politics,animal product,economics,means of agricultural production,executive power and public service,agriculture, forestry and fisheries,economic analysis
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legmulticlf_multieurlex_english_combined_2|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[class]|
|Language:|en|
|Size:|13.0 MB|

## References

https://huggingface.co/datasets/nlpaueb/multi_eurlex

## Benchmarking

```bash
 
labels                                                                  precision    recall  f1-score   support
chemistry                                                                   0.58      0.47      0.52       53
EU finance                                                                  0.73      0.53      0.61      124
production                                                                  0.65      0.67      0.66      197
industry                                                                    0.74      0.68      0.71       94
prices                                                                      0.71      0.72      0.71      511
distributive trades                                                         0.73      0.73      0.73      541
finance                                                                     0.67      0.31      0.43      125
Europe                                                                      0.70      0.46      0.56      163
communications                                                              0.46      0.19      0.27       32
civil law                                                                   0.91      0.92      0.91      1114
Africa                                                                      0.67      0.59      0.63      285
agricultural activity                                                       0.54      0.44      0.49      266
agricultural structures and production                                      0.55      0.43      0.48      121
farming systems                                                             0.76      0.80      0.78      765
research and intellectual property                                          0.86      0.26      0.40       23
foodstuffs                                                                  0.82      0.69      0.75      211
organisation of transport                                                   0.79      0.69      0.74      131
fisheries                                                                   0.71      0.55      0.62      197
food technology                                                             0.45      0.17      0.25       53
electronics and electrical engineering                                      0.59      0.41      0.48       32
European Union law                                                          0.35      0.10      0.15       61
marketing                                                                   0.55      0.42      0.48      268
foodstuff                                                                   0.62      0.41      0.50       61
EUROPEAN UNION                                                              0.57      0.39      0.46       33
information and information processing                                      0.55      0.32      0.41       34
international trade                                                         0.74      0.71      0.73      708
transport                                                                   0.62      0.62      0.62      224
politics                                                                    0.61      0.64      0.62      293
technology and technical regulations                                        0.62      0.33      0.43      137
regions of EU Member States                                                 0.33      0.10      0.15       20
geography                                                                   0.60      0.20      0.30       15
international affairs                                                       0.86      0.74      0.79       68
consumption                                                                 0.66      0.54      0.59      113
accounting                                                                  0.58      0.51      0.54       67
deterioration of the environment                                            0.57      0.33      0.42       51
beverages and sugar                                                         0.70      0.20      0.31       35
cooperation policy                                                          0.75      0.78      0.76      323
economic policy                                                             0.96      0.85      0.90      163
land transport                                                              0.42      0.27      0.33       66
European construction                                                       0.64      0.52      0.58      213
regions and regional policy                                                 0.64      0.58      0.61       12
leather and textile industries                                              0.78      0.85      0.82      915
animal product                                                              0.78      0.48      0.60      195
natural environment                                                         0.73      0.68      0.70      237
EU institutions and European civil service                                  0.71      0.59      0.65       86
employment and working conditions                                           0.64      0.55      0.59      354
health                                                                      0.52      0.44      0.48      206
agricultural policy                                                         0.50      0.17      0.25        6
processed agricultural produce                                              0.85      0.46      0.59       24
economics                                                                   0.62      0.68      0.65       50
education and communications                                                0.66      0.34      0.45      190
means of agricultural production                                            0.87      0.48      0.62      155
trade                                                                       0.44      0.21      0.29       19
trade policy                                                                0.78      0.53      0.63       47
plant product                                                               1.00      0.50      0.67        2
tariff policy                                                               0.89      0.77      0.82      497
executive power and public service                                          0.71      0.72      0.71      583
agriculture, forestry and fisheries                                         0.54      0.29      0.38       73
economic analysis                                                           0.80      0.85      0.83      222
business and competition                                                    0.87      0.81      0.84      189
international relations                                                     0.62      0.38      0.47      148
environmental policy                                                        0.54      0.37      0.44       38
iron, steel and other metal industries                                      0.76      0.63      0.69       87
Asia and Oceania                                                            0.59      0.52      0.55       31
production, technology and research                                         0.79      0.50      0.61      220
political geography                                                         0.88      0.71      0.78      478
social questions                                                            0.69      0.41      0.51       86
environment                                                                 0.88      0.87      0.88      1235
economic geography                                                          0.82      0.66      0.73      480
law                                                                         0.81      0.62      0.70      117
   micro-avg       0.75      0.66      0.71     15227
   macro-avg       0.65      0.47      0.53     15227
weighted-avg       0.74      0.66      0.69     15227
 samples-avg       0.76      0.69      0.70     15227
F1-micro-averaging: 0.7066298921202387
ROC:  0.8217655554093952

```