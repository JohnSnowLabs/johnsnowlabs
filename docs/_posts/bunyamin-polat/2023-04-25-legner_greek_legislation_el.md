---
layout: model
title: Legal NER in Greek Legislations
author: John Snow Labs
name: legner_greek_legislation
date: 2023-04-25
tags: [el, legal, ner, licensed, legislation]
task: Named Entity Recognition
language: el
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
annotator: LegalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This Financial NER model extracts the following entities from the Greek legislation:

- `FACILITY`: Facilities, such as police stations, departments, etc.
- `GPE`: Geopolitical Entity; any reference to a geopolitical entity (e.g., country, city, Greek administrative unit, etc.)
- `LEG_REF`: Legislation Reference; any reference to Greek or European legislation
- `ORG`: Organization; any reference to a public or private organization
- `PER`: Any formal name of a person mentioned in the text
- `PUBLIC_DOC`: Public Document Reference

## Predicted Entities

`FACILITY`, `GPE`, `LEG_REF`, `PUBLIC_DOC`, `PER`, `ORG`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_greek_legislation_el_1.0.0_3.0_1682420832367.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_greek_legislation_el_1.0.0_3.0_1682420832367.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_base_el_cased","el")\
        .setInputCols(["document", "token"])\
        .setOutputCol("embeddings")\
        .setMaxSentenceLength(512)\
        .setCaseSensitive(True)

ner_model = legal.NerModel.pretrained("legner_greek_legislation", "el", "legal/models")\
        .setInputCols(["document", "token", "embeddings"])\
        .setOutputCol("ner")

ner_converter = nlp.NerConverter()\
        .setInputCols(["document", "token", "ner"])\
        .setOutputCol("ner_chunk")

nlpPipeline = nlp.Pipeline(stages=[
        document_assembler,
        tokenizer,
        embeddings,
        ner_model,
        ner_converter])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = nlpPipeline.fit(empty_data)

text_list = ["""3 του άρθρου 5 του ν. 3148/2003, όπως ισχύει, αντικαθίσταται ως εξής""",
                   """1 του άρθρου 1 ασκούνται πλέον από την ΕΥΔΕ/ΕΣΕΑ μέσα σε δύο μήνες από την έναρξη ισχύος του παρόντος Διατάγματος.""",
                   """Ο Πρόεδρος της Επιτροπής και τα τέσσερα μέλη με ισάριθμα αναπληρωματικά εκλέγονται μεταξύ των δημοτών του Δήμου Κυθήρων.""",
                   """Τη με αριθ. 117/Σ.10η/25 Ιουλ 2016 γνωμοδότηση του Ανωτάτου Στρατιωτικού Συμβουλίου."""]

result = model.transform(spark.createDataFrame(pd.DataFrame({"text" : text_list})))
```

</div>

## Results

```bash
+----------------------------------------+----------+
|chunk                                   |ner_label |
+----------------------------------------+----------+
|ν. 3148/2003                            |LEG_REF   |
|ΕΥΔΕ/ΕΣΕΑ                               |ORG       |
|Δήμου Κυθήρων                           |GPE       |
|αριθ. 117/Σ.10η/25 Ιουλ 2016 γνωμοδότηση|PUBLIC_DOC|
+----------------------------------------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legner_greek_legislation|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|el|
|Size:|16.4 MB|

## References

In-house annotations

## Benchmarking

```bash
label         precision  recall  f1-score  support 
FACILITY      0.94       0.80    0.86      64      
GPE           0.77       0.83    0.80      136     
LEG_REF       0.94       0.90    0.92      93      
ORG           0.85       0.74    0.79      173     
PER           0.72       0.71    0.71      58      
PUBLIC_DOC    0.76       0.82    0.79      39      
micro-avg     0.83       0.80    0.81      563     
macro-avg     0.83       0.80    0.81      563     
weighted-avg  0.84       0.80    0.82      563 
```
