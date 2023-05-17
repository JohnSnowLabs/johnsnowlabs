---
layout: model
title: Legal Multilabel Classification (MultiEURLEX, Greek)
author: John Snow Labs
name: legmulticlf_multieurlex_greek_combined
date: 2023-04-01
tags: [legal, classification, el, licensed, multieurlex, level1, level2, tensorflow]
task: Text Classification
language: el
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

The MultiEURLEX dataset was used to train a Multilabel Text Classification model that incorporates both Level 1 and Level 2 labels. This model is capable of classifying 29 distinct types of legal documents from Greek.

## Predicted Entities

`φθορά του περιβάλλοντος`, `χρηματοπιστωτικοί οργανισμοί`, `επικοινωνία`, `οικονομική ανάλυση`, `τεκμηρίωση`, `ενεργειακή πολιτική`, `χημεία`, `παραγωγή`, `βιομηχανία ξύλου`, `κοινωνική ζωή`, `συστήματα αγροτικής εκμετάλλευσης`, `τεχνολογία τροφίμων`, `πληροφόρηση και επεξεργασία πληροφοριών`, `ποινικό δίκαιο`, `επιστημες`, `πολιτικός τομέας`, `αγροδιατροφικός τομέας`, `μεταλλουργία και χαλυβουργία`, `καλλιέργεια γαιών`, `απασχόληση`, `αγορά της εργασίας`, `φυσικές και εφαρμοσμένες επιστήμες`, `πολιτική περιβάλλοντος`, `πολιτική μεταφορών`, `αστικό δίκαιο`, `βιομηχανική πολιτική και διάρθρωση της βιομηχανίας`, `τιμές`, `διεθνεις οργανισμοι`, `δημοσιονομικα`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legmulticlf_multieurlex_greek_combined_el_1.0.0_3.0_1680347039362.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legmulticlf_multieurlex_greek_combined_el_1.0.0_3.0_1680347039362.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

docClassifier = nlp.MultiClassifierDLModel().pretrained('legmulticlf_multieurlex_greek_combined', 'el', 'legal/models')\
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

result = light_model.annotate("""Κανονισμός (ΕΚ) αριθ. 1883/2003 της Επιτροπής
της 27ης Οκτωβρίου 2003
για καθορισμό των κατ' αποκοπή τιμών κατά την εισαγωγή για τον καθορισμό της τιμής εισόδου ορισμένων οπωροκηπευτικών
Η ΕΠΙΤΡΟΠΗ ΤΩΝ ΕΥΡΩΠΑΪΚΩΝ ΚΟΙΝΟΤΗΤΩΝ,
Έχοντας υπόψη:
τη συνθήκη για την ίδρυση της Ευρωπαϊκής Κοινότητας,
τον κανονισμό (ΕΚ) αριθ. 3223/94 της Επιτροπής, της 21ης Δεκεμβρίου 1994, σχετικά με τις λεπτομέρειες εφαρμογής του καθεστώτος κατά την εισαγωγή οπωροκηπευτικών(1), όπως τροποποιήθηκε τελευταία από τον κανονισμό (EK) αριθ. 1947/2002(2), και ιδίως το άρθρο 4 παράγραφος 1,
Εκτιμώντας τα ακόλουθα:
(1) Ο κανονισμός (EK) αριθ. 3223/94, σε εφαρμογή των αποτελεσμάτων των πολυμερών εμπορικών διαπραγματεύσεων του Γύρου της Ουρουγουάης, προβλέπει τα κριτήρια για τον καθορισμό από την Επιτροπή των κατ' αποκοπή τιμών κατά την εισαγωγή από τρίτες χώρες, για τα προϊόντα και τις περιόδους που ορίζονται στο παράρτημά του.
(2) Σε εφαρμογή των προαναφερθέντων κριτηρίων, οι κατ' αποκοπή τιμές κατά την εισαγωγή πρέπει να καθοριστούν, όπως αναγράφονται στο παράρτημα του παρόντος κανονισμού,
ΕΞΕΔΩΣΕ ΤΟΝ ΠΑΡΟΝΤΑ ΚΑΝΟΝΙΣΜΟ:
Άρθρο 1
Οι κατ' αποκοπή τιμές κατά την εισαγωγή που αναφέρονται στο άρθρο 4 του κανονισμού (EK) αριθ. 3223/94 καθορίζονται όπως αναγράφονται στον πίνακα που εμφαίνεται στο παράρτημα.
Άρθρο 2
Ο παρών κανονισμός αρχίζει να ισχύει στις 28 Οκτωβρίου 2003.
Ο παρών κανονισμός είναι δεσμευτικός ως προς όλα τα μέρη του και ισχύει άμεσα σε κάθε κράτος μέλος.
Βρυξέλλες, 27 Οκτωβρίου 2003.""")

```

</div>

## Results

```bash
τιμές,δημοσιονομικα
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legmulticlf_multieurlex_greek_combined|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[class]|
|Language:|el|
|Size:|13.0 MB|

## References

https://huggingface.co/datasets/nlpaueb/multi_eurlex

## Benchmarking

```bash
 
labels                                                                    precision    recall  f1-score   support
φθορά του περιβάλλοντος                                                        0.65      0.79      0.71       14
χρηματοπιστωτικοί οργανισμοί                                                   0.75      0.05      0.10       56
επικοινωνία                                                                    0.80      0.20      0.32       20
οικονομική ανάλυση                                                             0.89      0.25      0.39       32
τεκμηρίωση                                                                     0.50      0.12      0.10       12
ενεργειακή πολιτική                                                            0.69      0.24      0.35       38
χημεία                                                                         0.83      0.81      0.82      1069
παραγωγή                                                                       0.80      0.21      0.33       19
βιομηχανία ξύλου                                                               0.00      0.00      0.04       13
κοινωνική ζωή                                                                  1.00      0.18      0.31       33
συστήματα αγροτικής εκμετάλλευσης                                              0.93      0.79      0.85       33
τεχνολογία τροφίμων                                                            0.62      0.36      0.46       36
πληροφόρηση και επεξεργασία πληροφοριών                                        1.00      0.09      0.17       11
ποινικό δίκαιο                                                                 0.88      0.38      0.53       37
επιστημες                                                                      0.86      0.44      0.58       43
πολιτικός τομέας                                                               0.78      0.23      0.35       31
αγροδιατροφικός τομέας                                                         0.80      0.18      0.29       68
μεταλλουργία και χαλυβουργία                                                   0.83      0.26      0.40       19
καλλιέργεια γαιών                                                              0.41      0.17      0.24       41
απασχόληση                                                                     0.69      0.27      0.39       67
αγορά της εργασίας                                                             1.00      0.25      0.40       12
φυσικές και εφαρμοσμένες επιστήμες                                             0.65      0.35      0.45       49
πολιτική περιβάλλοντος                                                         0.85      0.31      0.45       36
πολιτική μεταφορών                                                             0.71      0.34      0.46       88
αστικό δίκαιο                                                                  0.86      0.93      0.90      1312
βιομηχανική πολιτική και διάρθρωση της βιομηχανίας                             0.77      0.38      0.51       52
τιμές                                                                          0.96      0.82      0.89       33
διεθνεις οργανισμοι                                                            0.88      0.26      0.40       58
δημοσιονομικα                                                                  0.50      0.10      0.17       30
   micro-avg       0.84      0.71      0.77      3362
   macro-avg       0.74      0.33      0.42      3362
weighted-avg       0.82      0.71      0.73      3362
 samples-avg       0.79      0.74      0.74      3362
F1-micro-averaging: 0.768041237113402
ROC:  0.8501134190103269

```