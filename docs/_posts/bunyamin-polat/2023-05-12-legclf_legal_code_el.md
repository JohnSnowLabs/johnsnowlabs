---
layout: model
title: Legal Topic Classification on Greek Legislation
author: John Snow Labs
name: legclf_legal_code
date: 2023-05-12
tags: [el, legal, classification, bert, licensed, tensorflow]
task: Text Classification
language: el
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: LegalBertForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Greek Legal Code (GLC) is a dataset consisting of approx. 47k legal resources from Greek legislation. The origin of GLC is “Permanent Greek Legislation Code - Raptarchis”, a collection of Greek legislative documents classified into multi-level (from broader to more specialized) categories.

Given the text of a document, the `legclf_legal_code` model predicts the corresponding class

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legclf_legal_code_el_1.0.0_3.0_1683904327601.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legclf_legal_code_el_1.0.0_3.0_1683904327601.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

sequence_classifier = legal.BertForSequenceClassification.pretrained("legclf_legal_code", "el", "legal/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("class")\
    .setCaseSensitive(True)\
    .setMaxSentenceLength(512)

clf_pipeline = nlp.Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequence_classifier    
])

empty_df = spark.createDataFrame([['']]).toDF("text")

model = clf_pipeline.fit(empty_df)

text = """14. ΠΡΟΕΔΡΙΚΟΝ ΔΙΑΤΑΓΜΑ υπ’ αριθ. 545 της 5/25 Ιουλ. 1979 (ΦΕΚ Α΄ 168) Περί αυξήσεως των υπό του Ταμείου Προνοίας Εργοληπτών Δημοσίων Έργων παρεχομένων εφ’ άπαξ βοηθημάτων. Έχοντες υπ’ όψιν: 1.Τας διατάξεις της παρ. 8 του άρθρ. 2 του Ν.Δ. 75/1946 «περί συστάσεως Ταμείου Προνοίας Εργοληπτών Δημοσίων Έργων». 2.Τας διατάξεις της παρ. 2 του άρθρ. 12 του Νόμ. 400/1976 «περί Υπουργικού Συμβουλίου και Υπουργείων» (ΦΕΚ 203/76 τ.Α΄). 3.Τας διατάξεις των άρθρ. 17 παρ. 2 εδάφ. β΄ περίπτ. αα΄ και 113 παρ. 2 εδάφ. α΄ του Π.Δ. 544/1977 (ΦΕΚ 178/77 τ.Α΄) ως η τελευταία αντικατεστάθη δια της παρ. 1 του άρθρ. 2 του Νόμ. 728/1977 (ΦΕΚ 316/77 τ.Α΄). 4.Την υπ’ αριθ. Δ3/2087/6.12.77 (ΦΕΚ 1278/77 τ.Β΄) απόφασιν του Πρωθυπουργού και του Υπουργού Κοινωνικών Υπηρεσιών «περί αναθέσεως αρμοδιοτήτων στους Υφυπουργούς Κοινωνικών Υπηρεσιών». 5.Την σύμφωνον γνώμην του Διοικητικού Συμβουλίου του Ταμείου Προνοίας Εργοληπτών Δημοσίων Έργων, ληφθείσα κατά την υπ’ αριθ. 1/17.1.79 συνεδρίασιν αυτού και υποβληθείσα ημίν δια της υπ’ αριθ. 583/24.1.79 αναφοράς του Ταμείου. 6.Την γνωμοδότησιν του Συμβουλίου Κοινων. Ασφαλείας, ληφθείσα κατά την υπ’ αριθ. 9/11.4.79 συνεδρίασιν αυτού της Κ΄ περιόδου. 7.Την υπ’ αριθ. 490/1979 γνωμοδότησιν του Συμβουλίου της Επικρατείας, προτάσει του επί των Κοινωνικών Υπηρεσιών Υφυπουργού, αποφασίζομεν: Άρθρον μόνον.-1.Το υπό του Ταμείου Προνοίας Εργοληπτών Δημοσίων Έργων παρεχόμενον εις τους εξερχομένους του επαγγέλματος δι’ οιονδήποτε λόγον ησφαλισμένος αυτού, πλήρες εφ’ άπαξ βοήθημα (χορηγία) δια τους έχοντας συμπεπληρωμένην 35ετή υπηρεσίαν, καθορίζεται εφ’ εξής ως κάτωθι: α)Δια τους ησφαλισμένους Εργολήπτας Δημοσίων Έργων Γ΄ και Δ΄ τάξεως ως και τους μετόχους υπαλλήλους του Ταμείου και των Εργοληπτικών Οργανώσεων από του 6ου βαθμού συμπεριλαμβανομένου και άνω εις 474.500 δραχμάς. β)Δια τους λοιπούς ησφαλισμένους του Ταμείου εις 357.000 δραχμάς. 2.Εις περίπτωσιν κατά την οποίαν η συνολική υπηρεσία οιουδήποτε εκ των ανωτέρω ησφαλισμένων είναι μικροτέρα των 35 ετών και εφ’ όσον συντρέχουν αι προϋποθέσεις του άρθρ. 1 του Β.Δ/τος της 13/29 Μαρτ. 1947 «περί χορηγιών του Ταμείου Προνοίας Εργοληπτών Δημοσίων Έργων» ως ισχύει κατόπιν των τροποποιήσεων και συμπληρώσεων αυτού, ο ησφαλισμένος δικαιούται τόσων τριακοστών πέμπτων του πλήρους εφ’ άπαξ βοηθήματος, όσα και τα έτη της υπηρεσίας αυτού. 3.Προϋπηρεσία πλέον των 35 ετών δεν αναγνωρίζεται. (Αντί για τη σελ. 224,03(α) Σελ. 224,03(β) Τεύχος 709-Σελ. 113 Ταμείο Προνοίας Εργοληπτών 23.Γ.ε.12-14 Εις τον επί των Κοινωνικών Υπηρεσιών Υφυπουργόν ανατίθεμεν την δημοσίευσιν και εκτέλεσιν του παρόντος."""

result = model.transform(spark.createDataFrame([[text]]).toDF("text"))

```

</div>

## Results

```bash
+--------------------+--------------+
|                text|        result|
+--------------------+--------------+
|14. ΠΡΟΕΔΡΙΚΟΝ ΔΙ...|[ΔΗΜΟΣΙΑ_ΕΡΓΑ]|
+--------------------+--------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legclf_legal_code|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[class]|
|Language:|el|
|Size:|356.7 MB|
|Case sensitive:|true|
|Max sentence length:|512|

## References

The dataset is available [here](https://huggingface.co/datasets/greek_legal_code)

## Benchmarking

```bash
label                                                     precision  recall  f1-score  support 
ΑΓΟΡΑΝΟΜΙΚΗ_ΝΟΜΟΘΕΣΙΑ                                     0.79       0.83    0.81      41      
ΑΓΡΟΤΙΚΗ_ΝΟΜΟΘΕΣΙΑ                                        0.84       0.87    0.85      30      
ΑΜΕΣΗ_ΦΟΡΟΛΟΓΙΑ                                           0.87       0.90    0.89      94      
ΑΣΤΙΚΗ_ΝΟΜΟΘΕΣΙΑ                                          0.81       0.83    0.82      41      
ΑΣΤΥΝΟΜΙΚΗ_ΝΟΜΟΘΕΣΙΑ                                      0.85       0.87    0.86      70      
ΑΣΦΑΛΙΣΤΙΚΑ_ΤΑΜΕΙΑ                                        0.93       0.95    0.94      121     
ΒΙΟΜΗΧΑΝΙΚΗ_ΝΟΜΟΘΕΣΙΑ                                     0.85       0.83    0.84      93      
ΓΕΩΡΓΙΚΗ_ΝΟΜΟΘΕΣΙΑ                                        0.88       0.92    0.90      155     
ΔΑΣΗ_ΚΑΙ_ΚΤΗΝΟΤΡΟΦΙΑ                                      0.88       0.70    0.78      40      
ΔΗΜΟΣΙΑ_ΕΡΓΑ                                              0.88       0.88    0.88      111     
ΔΗΜΟΣΙΟ_ΛΟΓΙΣΤΙΚΟ                                         0.79       0.74    0.76      46      
ΔΗΜΟΣΙΟΙ_ΥΠΑΛΛΗΛΟΙ                                        0.78       0.79    0.78      90      
ΔΙΟΙΚΗΣΗ_ΔΙΚΑΙΟΣΥΝΗΣ                                      0.91       0.97    0.94      140     
ΔΙΟΙΚΗΤΙΚΗ_ΝΟΜΟΘΕΣΙΑ                                      0.80       0.86    0.83      42      
ΔΙΠΛΩΜΑΤΙΚΗ_ΝΟΜΟΘΕΣΙΑ                                     0.82       0.87    0.85      95      
ΕΘΝΙΚΗ_ΑΜΥΝΑ                                              0.84       0.80    0.82      121     
ΕΘΝΙΚΗ_ΟΙΚΟΝΟΜΙΑ                                          0.76       0.79    0.77      43      
ΕΚΚΛΗΣΙΑΣΤΙΚΗ_ΝΟΜΟΘΕΣΙΑ                                   0.92       0.98    0.95      47      
ΕΚΠΑΙΔΕΥΤΙΚΗ_ΝΟΜΟΘΕΣΙΑ                                    0.94       0.94    0.94      230     
ΕΛΕΓΚΤΙΚΟ_ΣΥΝΕΔΡΙΟ_ΚΑΙ_ΣΥΝΤΑΞΕΙΣ                          0.79       0.70    0.74      37      
ΕΜΜΕΣΗ_ΦΟΡΟΛΟΓΙΑ                                          0.81       0.84    0.83      62      
ΕΜΠΟΡΙΚΗ_ΝΑΥΤΙΛΙΑ                                         0.95       0.95    0.95      149     
ΕΜΠΟΡΙΚΗ_ΝΟΜΟΘΕΣΙΑ                                        0.85       0.95    0.90      42      
ΕΠΙΣΤΗΜΕΣ_ΚΑΙ_ΤΕΧΝΕΣ                                      0.94       0.95    0.95      285     
ΕΡΓΑΤΙΚΗ_ΝΟΜΟΘΕΣΙΑ                                        0.90       0.88    0.89      95      
ΚΟΙΝΩΝΙΚΕΣ_ΑΣΦΑΛΙΣΕΙΣ                                     0.92       0.89    0.91      66      
ΚΟΙΝΩΝΙΚΗ_ΠΡΟΝΟΙΑ                                         0.91       0.85    0.88      71      
ΛΙΜΕΝΙΚΗ_ΝΟΜΟΘΕΣΙΑ                                        0.91       0.96    0.94      78      
ΝΟΜΙΚΑ_ΠΡΟΣΩΠΑ_ΔΗΜΟΣΙΟΥ_ΔΙΚΑΙΟΥ                           0.95       0.91    0.93      67      
ΝΟΜΟΘΕΣΙΑ_ΑΝΩΝΥΜΩΝ_ΕΤΑΙΡΕΙΩΝ_ΤΡΑΠΕΖΩΝ_ΚΑΙ_ΧΡΗΜΑΤΙΣΤΗΡΙΩΝ  0.89       0.81    0.85      72      
ΝΟΜΟΘΕΣΙΑ_ΔΗΜΩΝ_ΚΑΙ_ΚΟΙΝΟΤΗΤΩΝ                            0.90       0.85    0.88      55      
ΝΟΜΟΘΕΣΙΑ_ΕΠΙΜΕΛΗΤΗΡΙΩΝ_ΣΥΝΕΤΑΙΡΙΣΜΩΝ_ΚΑΙ_ΣΩΜΑΤΕΙΩΝ       0.92       0.92    0.92      37      
ΟΙΚΟΝΟΜΙΚΗ_ΔΙΟΙΚΗΣΗ                                       0.86       0.70    0.77      53      
ΠΕΡΙΟΥΣΙΑ_ΔΗΜΟΣΙΟΥ_ΚΑΙ_ΝΟΜΙΣΜΑ                            0.80       0.80    0.80      46      
ΠΟΙΝΙΚΗ_ΝΟΜΟΘΕΣΙΑ                                         0.96       0.94    0.95      49      
ΠΟΛΕΜΙΚΗ_ΑΕΡΟΠΟΡΙΑ                                        0.89       0.83    0.86      29      
ΠΟΛΕΜΙΚΟ_ΝΑΥΤΙΚΟ                                          0.94       0.77    0.85      43      
ΠΟΛΙΤΙΚΗ_ΑΕΡΟΠΟΡΙΑ                                        0.93       0.90    0.92      30      
ΠΟΛΙΤΙΚΗ_ΔΙΚΟΝΟΜΙΑ                                        0.86       0.95    0.90      19      
ΡΑΔΙΟΦΩΝΙΑ_ΚΑΙ_ΤΥΠΟΣ                                      0.81       0.94    0.87      31      
ΣΤΡΑΤΟΣ_ΞΗΡΑΣ                                             0.74       0.83    0.78      71      
ΣΥΓΚΟΙΝΩΝΙΕΣ                                              0.91       0.92    0.91      178     
ΣΥΝΤΑΓΜΑΤΙΚΗ_ΝΟΜΟΘΕΣΙΑ                                    0.84       0.74    0.79      87      
ΤΑΧΥΔΡΟΜΕΙΑ_ΤΗΛΕΠΙΚΟΙΝΩΝΙΕΣ                               0.96       0.93    0.95      84      
ΤΕΛΩΝΕΙΑΚΗ_ΝΟΜΟΘΕΣΙΑ                                      0.87       0.84    0.85      73      
ΤΥΠΟΣ_ΚΑΙ_ΤΟΥΡΙΣΜΟΣ                                       0.96       0.98    0.97      50      
ΥΓΕΙΟΝΟΜΙΚΗ_ΝΟΜΟΘΕΣΙΑ                                     0.91       0.93    0.92      136     
accuracy                                                  -          -       0.88      3745    
macro avg                                                 0.87       0.87    0.87      3745    
weighted avg                                              0.89       0.88    0.88      3745    
```