---
layout: model
title: German NER for Laws (Bert, Base)
author: John Snow Labs
name: legner_bert_base_courts
date: 2022-10-02
tags: [de, legal, ner, laws, court, licensed]
task: Named Entity Recognition
language: de
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
annotator: LegalBertForTokenClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model can be used to detect legal entities in German text, predicting up to 19 different labels:
```
| tag	| meaning 
-----------------
| AN	| Anwalt 
| EUN	| Europäische Norm 
| GS	| Gesetz 
| GRT	| Gericht 
| INN	| Institution 
| LD	| Land 
| LDS	| Landschaft 
| LIT	| Literatur 
| MRK	| Marke 
| ORG	| Organisation 
| PER	| Person 
| RR	| Richter 
| RS	| Rechtssprechung 
| ST	| Stadt 
| STR	| Straße 
| UN	| Unternehmen 
| VO	| Verordnung 
| VS	| Vorschrift 
| VT	| Vertrag 
```

German Named Entity Recognition model, trained using large German Base Bert model and finetuned using Court Decisions (2017-2018) dataset (check `Data Source` section). You can also find a lighter Deep Learning (non-transformer based) in our Models Hub (`legner_courts`) and a Bert Large version (`legner_bert_large_courts`).

## Predicted Entities

`STR`, `LIT`, `PER`, `EUN`, `VT`, `MRK`, `INN`, `UN`, `RS`, `ORG`, `GS`, `VS`, `LDS`, `GRT`, `VO`, `RR`, `LD`, `AN`, `ST`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_LEGAL_DE/){:.button.button-orange}
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_bert_base_courts_de_1.0.0_3.0_1664708306072.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_bert_base_courts_de_1.0.0_3.0_1664708306072.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

ner_model = legal.BertForTokenClassification.pretrained("legner_bert_base_courts", "de", "legal/models")\
    .setInputCols(["document", "token"])\
    .setOutputCol("ner")\
    .setCaseSensitive(True)\
    .setMaxSentenceLength(512)

ner_converter = nlp.NerConverter()\
    .setInputCols(["document", "token", "ner"])\
    .setOutputCol("ner_chunk")

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    ner_model,
    ner_converter   
    ])

model = pipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

text_list = ["""Der Europäische Gerichtshof für Menschenrechte (EGMR) gibt dabei allerdings ebenso wenig wie das Bundesverfassungsgericht feste Fristen vor, sondern stellt auf die jeweiligen Umstände des Einzelfalls ab.""", 
             """Formelle Rechtskraft ( § 705 ZPO ) trat mit Verkündung des Revisionsurteils am 15. Dezember 2016 ein (vgl. Zöller / Seibel ZPO 32. Aufl. § 705 Rn. 8) ."""]
             
df = spark.createDataFrame(pd.DataFrame({"text" : text_list}))

result = model.transform(df)

result.select(F.explode(F.arrays_zip('ner_chunk.result', 'ner_chunk.metadata')).alias("cols")) \
               .select(F.expr("cols['0']").alias("ner_chunk"),
                       F.expr("cols['1']['entity']").alias("label")).show(truncate = False)
```

</div>

## Results

```bash
+------------------------------------------+-----+
|ner_chunk                                 |label|
+------------------------------------------+-----+
|Europäische Gerichtshof für Menschenrechte|GRT  |
|EGMR                                      |GRT  |
|Bundesverfassungsgericht                  |GRT  |
|§ 705 ZPO                                 |GS   |
|Zöller / Seibel ZPO 32. Aufl. § 705 Rn. 8 |LIT  |
+------------------------------------------+-----+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legner_bert_base_courts|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[ner]|
|Language:|de|
|Size:|407.0 MB|
|Case sensitive:|true|
|Max sentence length:|512|

## References

The dataset used to train this model is taken from Leitner, et.al (2019)

Leitner, E., Rehm, G., and Moreno-Schneider, J. (2019). Fine-grained Named Entity Recognition in Legal Documents. In Maribel Acosta, et al., editors, Semantic Systems. The Power of AI and Knowledge Graphs. Proceedings of the 15th International Conference (SEMANTiCS2019), number 11702 in Lecture Notes in Computer Science, pages 272–287, Karlsruhe, Germany, 9. Springer. 10/11 September 2019.

Source of the annotated text:

Court decisions from 2017 and 2018 were selected for the dataset, published online by the Federal Ministry of Justice and Consumer Protection. The documents originate from seven federal courts: Federal Labour Court (BAG), Federal Fiscal Court (BFH), Federal Court of Justice (BGH), Federal Patent Court (BPatG), Federal Social Court (BSG), Federal Constitutional Court (BVerfG) and Federal Administrative Court (BVerwG).

## Benchmarking

```bash
       label  precision    recall  f1-score   support
          AN       0.82      0.61      0.70        23
         EUN       0.90      0.93      0.92       210
         GRT       0.95      0.98      0.96       445
          GS       0.97      0.98      0.98      2739
         INN       0.87      0.88      0.88       321
          LD       0.92      0.94      0.93       189
         LDS       0.44      0.73      0.55        26
         LIT       0.85      0.91      0.88       449
         MRK       0.40      0.86      0.55        44
         ORG       0.72      0.79      0.76       184
         PER       0.71      0.91      0.80       260
          RR       0.73      0.58      0.65       208
          RS       0.95      0.97      0.96      1859
          ST       0.81      0.94      0.87       120
         STR       0.69      0.69      0.69        26
          UN       0.73      0.84      0.78       158
          VO       0.82      0.86      0.84       107
          VS       0.48      0.81      0.60        86
          VT       0.90      0.87      0.89       442
   micro-avg       0.90      0.93      0.92      7896
   macro-avg       0.77      0.85      0.80      7896
weighted-avg       0.91      0.93      0.92      7896
```