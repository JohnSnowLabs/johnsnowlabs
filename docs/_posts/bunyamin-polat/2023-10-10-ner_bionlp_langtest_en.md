---
layout: model
title: Detect Cancer Genetics (LangTest)
author: John Snow Labs
name: ner_bionlp_langtest
date: 2023-10-10
tags: [en, ner, licensed, clinical, bionlp, langtest]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.1.1
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for biology and genetics terms. It is the version of [ner_bionlp](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_en.html) model augmented with `langtest` library.

| **test_type**             | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|---------------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_ocr_typo**          | 654                   | 121                  | 610                   | 1143                 | 70%                   | 48%                  | 90%                 |
| **lowercase**             | 463                   | 307                  | 802                   | 958                  | 70%                   | 63%                  | 76%                 |
| **strip_all_punctuation** | 220                   | 219                  | 1059                  | 1060                 | 70%                   | 83%                  | 83%                 |
| **titlecase**             | 714                   | 373                  | 563                   | 904                  | 60%                   | 44%                  | 71%                 |
| **uppercase**             | 1161                  | 464                  | 122                   | 819                  | 60%                   | 10%                  | 64%                 |
| **weighted average**      | **3212**              | **1484**             | **3156**              | **4884**             | **66%**               | **49.56%**           | **76.70%**          |

## Predicted Entities

`Amino_acid`, `Anatomical_system`, `Cancer`, `Cell`, `Cellular_component`, `Developing_anatomical_Structure`, `Gene_or_gene_product`, `Immaterial_anatomical_entity`, `Multi-tissue_structure`, `Organ`, `Organism`, `Organism_subdivision`, `Simple_chemical`, `Tissue`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_bionlp_langtest_en_5.1.1_3.0_1696934822369.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_bionlp_langtest_en_5.1.1_3.0_1696934822369.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")
         
sentence_detector = SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_bionlp_langtest", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter()\
 	.setInputCols(["sentence", "token", "ner"])\
 	.setOutputCol("ner_chunk")
    
nlp_pipeline = Pipeline(stages=[document_assembler, sentence_detector, tokenizer, word_embeddings, clinical_ner, ner_converter])

model = nlp_pipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

results = model.transform(spark.createDataFrame([["""The human KCNJ9 (Kir 3.3, GIRK3) is a member of the G-protein-activated inwardly rectifying potassium (GIRK) channel family. Here we describe the genomicorganization of the KCNJ9 locus on chromosome 1q21-23 as a candidate gene for Type II diabetes mellitus in the Pima Indian population. The gene spans approximately 7.6 kb and contains one noncoding and two coding exons separated by approximately 2.2 and approximately 2.6 kb introns, respectively. We identified 14 single nucleotide polymorphisms (SNPs), including one that predicts aVal366Ala substitution, and an 8 base-pair (bp) insertion/deletion. Ourexpression studies revealed the presence of the transcript in various human tissues including the pancreas, and two major insulin-responsive tissues. The characterization of the KCNJ9 gene should facilitate further studies on the function of the KCNJ9 protein and allow evaluation of the potential role of the locus in Type II diabetes."""]], ["text"]))
```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
         
val sentence_detector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner = MedicalNerModel.pretrained("ner_bionlp_langtest", "en", "clinical/models")
    .setInputCols("sentence", "token", "embeddings")
    .setOutputCol("ner")

val ner_converter = new NerConverter()
 	.setInputCols(Array("sentence", "token", "ner"))
 	.setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(document_assembler, sentence_detector, tokenizer, word_embeddings, ner, ner_converter))

val data = Seq("""The human KCNJ9 (Kir 3.3, GIRK3) is a member of the G-protein-activated inwardly rectifying potassium (GIRK) channel family. Here we describe the genomicorganization of the KCNJ9 locus on chromosome 1q21-23 as a candidate gene for Type II diabetes mellitus in the Pima Indian population. The gene spans approximately 7.6 kb and contains one noncoding and two coding exons separated by approximately 2.2 and approximately 2.6 kb introns, respectively. We identified 14 single nucleotide polymorphisms (SNPs), including one that predicts aVal366Ala substitution, and an 8 base-pair (bp) insertion/deletion. Ourexpression studies revealed the presence of the transcript in various human tissues including the pancreas, and two major insulin-responsive tissues. The characterization of the KCNJ9 gene should facilitate further studies on the function of the KCNJ9 protein and allow evaluation of the potential role of the locus in Type II diabetes.""").toDS().toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------------------------+--------------------+
|chunk                        |ner_label           |
+-----------------------------+--------------------+
|human                        |Organism            |
|Kir 3.3                      |Gene_or_gene_product|
|GIRK3                        |Gene_or_gene_product|
|inwardly rectifying potassium|Gene_or_gene_product|
|GIRK                         |Gene_or_gene_product|
|chromosome 1q21-23           |Cellular_component  |
|Type II                      |Gene_or_gene_product|
|human                        |Organism            |
|tissues                      |Tissue              |
|pancreas                     |Organ               |
|insulin-responsive tissues   |Tissue              |
|KCNJ9                        |Gene_or_gene_product|
|KCNJ9                        |Gene_or_gene_product|
|locus                        |Cellular_component  |
+-----------------------------+--------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_bionlp_langtest|
|Compatibility:|Healthcare NLP 5.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.6 MB|

## References

Trained on the Cancer Genetics (CG) task of the [BioNLP Shared Task 2013](https://aclanthology.org/W13-2008/)

## Benchmarking

```bash
label                            precision  recall  f1-score  support 
Amino_acid                       0.96       0.62    0.75      37      
Anatomical_system                0.89       0.62    0.73      13      
Cancer                           0.92       0.90    0.91      570     
Cell                             0.93       0.92    0.92      806     
Cellular_component               0.86       0.89    0.87      141     
Developing_anatomical_structure  0.75       0.60    0.67      5       
Gene_or_gene_product             0.93       0.93    0.93      1818    
Immaterial_anatomical_entity     0.92       0.76    0.83      29      
Multi-tissue_structure           0.86       0.79    0.82      196     
Organ                            0.90       0.91    0.90      85      
Organism                         0.94       0.90    0.92      414     
Organism_subdivision             0.74       0.64    0.68      22      
Organism_substance               0.86       0.89    0.87      61      
Pathological_formation           0.78       0.76    0.77      46      
Simple_chemical                  0.94       0.93    0.93      538     
Tissue                           0.76       0.83    0.79      110     
micro-avg                        0.92       0.91    0.91      4891    
macro-avg                        0.87       0.80    0.83      4891    
weighted-avg                     0.92       0.91    0.91      4891    
```