---
layout: model
title: Detect Genes, Human Phenotypes and Related Entities
author: John Snow Labs
name: ner_genes_phenotypes_wip
date: 2024-12-04
tags: [en, clinical, licensed, ner, gene, phenotype, human_phenotype, human, genetics, protein]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.5.1
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Decription

This Named Entity Recognition (NER) model is specifically trained to extract critical information related to genetics, their phenotypes and associated information contained within any medical document. 

The model recognizes the following entities:

`Clinical_Presentation`: All the medical conditions such as the signs and symptoms.
`Gene`: Genetic codes and base sequences present such as F508del, or rs1805007 along their normal or pathological variants.
`Gene_Diversity`: Variability of genes within a population.
`Gene_Function`: Function of the normal gene or an Allele.
`Gene_Penetrance`: Proportion of individuals with a specific genetic mutation or variant who exhibit the associated trait, condition, or disease.
`Incidence`: Number of new cases of a particular disease that occur in a specific population during a defined period.
`Inheritance_Pattern`: The pattern by which a genetic trait or disorder is passed down from one generation to the next.
`MPG`: Names of the genes and molecules, along with the abbreviations, including all the proteins, glycoproteins, polypeptides, or polymers.
`Phenotype_Disease`: Specific disease conditions or manifestations of a disease in an individual, influenced by the underlying genetic causes.
`Prevalence`: Population groups associated with the disease.
`Site`: Site of the genetic mutation or abnormality on the Genome.
`Type_Of_Mutation`: Type of mutation that occurred in the genome.

## Predicted Entities

`Clinical_Presentation`, `Gene`, `Gene_Diversity`, `Gene_Function`, `Gene_Penetrance`, `Incidence`, `Inheritance_Pattern`, `MPG`, `Phenotype_Disease`, `Prevalence`, `Site`, `Type_Of_Mutation`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_genes_phenotypes_wip_en_5.5.1_3.0_1733317407640.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_genes_phenotypes_wip_en_5.5.1_3.0_1733317407640.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

clinical_embeddings = WordEmbeddingsModel.pretrained('embeddings_clinical', "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained('ner_genes_phenotypes_wip', "en", "clinical/models")\
    .setInputCols(["sentence", "token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(['sentence', 'token', 'ner'])\
    .setOutputCol('ner_chunk')

pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter   
    ])

sample_texts = ["""
The CFTR gene, situated on chromosome 7, encodes a chloride channel protein crucial for epithelial salt and water regulation. This gene is associated with cystic fibrosis, demonstrating autosomal recessive inheritance. Mutations like the classic ΔF508 (deletion of phenylalanine at position 508) significantly impair protein folding and cellular transport. The gene shows incomplete penetrance, with variable clinical manifestations ranging from mild respiratory complications to severe multi-organ dysfunction. Diagnostic approaches include genetic testing, sweat chloride analysis, and pulmonary function assessments. Treatment modalities have evolved, incorporating targeted therapies like CFTR modulators that address specific molecular defects. Gene interactions with environmental factors and modifier genes influence disease progression and severity. Prevalence is notably higher in populations of Northern European descent, with approximately 1 in 2,500-3,500 live births affected.

The FMR1 gene, located on the X chromosome, is critical in neurological development and synaptic function. This gene is associated with Fragile X syndrome, exhibiting X-linked dominant inheritance with variable penetrance. Molecular characterization reveals CGG trinucleotide repeat expansions causing potential intellectual disability and neurodevelopmental challenges. Penetrance is complex, with males typically more severely affected than females due to X-chromosome inactivation patterns. Clinical presentations include developmental delays, characteristic facial features, and potential autism spectrum disorder associations. Diagnostic strategies involve molecular genetic testing to quantify CGG repeat expansions. Treatment approaches are multidisciplinary, focusing on educational interventions, behavioral therapies, and management of associated neurological symptoms. Environmental interactions and epigenetic modifications significantly influence phenotypic expressions.
"""]

data = spark.createDataFrame(sample_texts, StringType()).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_genes_phenotypes_wip", "en", "clinical/models")
    .setInputCols(Array("sentence", "token","embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentenceDetector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter   
))

val sample_texts = Seq("""The CFTR gene, situated on chromosome 7, encodes a chloride channel protein crucial for epithelial salt and water regulation. This gene is associated with cystic fibrosis, demonstrating autosomal recessive inheritance. Mutations like the classic ΔF508 (deletion of phenylalanine at position 508) significantly impair protein folding and cellular transport. The gene shows incomplete penetrance, with variable clinical manifestations ranging from mild respiratory complications to severe multi-organ dysfunction. Diagnostic approaches include genetic testing, sweat chloride analysis, and pulmonary function assessments. Treatment modalities have evolved, incorporating targeted therapies like CFTR modulators that address specific molecular defects. Gene interactions with environmental factors and modifier genes influence disease progression and severity. Prevalence is notably higher in populations of Northern European descent, with approximately 1 in 2,500-3,500 live births affected.

The FMR1 gene, located on the X chromosome, is critical in neurological development and synaptic function. This gene is associated with Fragile X syndrome, exhibiting X-linked dominant inheritance with variable penetrance. Molecular characterization reveals CGG trinucleotide repeat expansions causing potential intellectual disability and neurodevelopmental challenges. Penetrance is complex, with males typically more severely affected than females due to X-chromosome inactivation patterns. Clinical presentations include developmental delays, characteristic facial features, and potential autism spectrum disorder associations. Diagnostic strategies involve molecular genetic testing to quantify CGG repeat expansions. Treatment approaches are multidisciplinary, focusing on educational interventions, behavioral therapies, and management of associated neurological symptoms. Environmental interactions and epigenetic modifications significantly influence phenotypic expressions.
""").toDF("text")

val result = pipeline.fit(sample_texts).transform(sample_texts)
```
</div>

## Results

```bash
+----------------------------------------------+-----+----+---------------------+
|chunk                                         |begin|end |ner_label            |
+----------------------------------------------+-----+----+---------------------+
|CFTR gene                                     |5    |13  |MPG                  |
|chromosome 7                                  |28   |39  |Site                 |
|chloride channel protein                      |52   |75  |MPG                  |
|epithelial salt and water regulation          |89   |124 |Gene_Function        |
|cystic fibrosis                               |156  |170 |Phenotype_Disease    |
|autosomal recessive                           |187  |205 |Inheritance_Pattern  |
|ΔF508                                         |247  |251 |Gene                 |
|deletion                                      |254  |261 |Type_Of_Mutation     |
|phenylalanine                                 |266  |278 |MPG                  |
|incomplete penetrance                         |373  |393 |Gene_Penetrance      |
|multi-organ dysfunction                       |488  |510 |Other_Disease        |
|CFTR                                          |694  |697 |MPG                  |
|Northern European descent                     |906  |930 |Prevalence           |
|1 in 2,500-3,500                              |952  |967 |Incidence            |
|FMR1 gene                                     |996  |1004|MPG                  |
|X chromosome                                  |1022 |1033|Site                 |
|neurological development and synaptic function|1051 |1096|Gene_Function        |
|Fragile X syndrome                            |1128 |1145|Phenotype_Disease    |
|X-linked dominant                             |1159 |1175|Inheritance_Pattern  |
|variable penetrance                           |1194 |1212|Gene_Penetrance      |
|CGG                                           |1250 |1252|Gene                 |
|intellectual disability                       |1304 |1326|Clinical_Presentation|
|Penetrance is complex                         |1363 |1383|Gene_Penetrance      |
|males                                         |1391 |1395|Prevalence           |
|females                                       |1435 |1441|Prevalence           |
|X-chromosome                                  |1450 |1461|Site                 |
|developmental delays                          |1517 |1536|Clinical_Presentation|
|autism spectrum disorder                      |1585 |1608|Other_Disease        |
|CGG                                           |1692 |1694|Gene                 |
+----------------------------------------------+-----+----+---------------------+


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_genes_phenotypes_wip|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|4.9 MB|

## References

In-house annotated case reports.

## Benchmarking

```bash
                label  precision    recall  f1-score   support
Clinical_Presentation       0.80      0.72      0.75       193
                 Gene       0.93      0.62      0.75        66
       Gene_Diversity       0.91      0.97      0.94        33
        Gene_Function       0.81      0.75      0.78       145
      Gene_Penetrance       0.87      0.87      0.87        55
            Incidence       0.99      0.90      0.94        84
  Inheritance_Pattern       1.00      0.95      0.97       115
                  MPG       0.90      0.92      0.91       398
        Other_Disease       0.85      0.78      0.81       342
    Phenotype_Disease       0.87      0.90      0.88       350
           Prevalence       0.79      0.89      0.84        70
                 Site       0.90      0.99      0.94        83
     Type_Of_Mutation       0.97      0.92      0.95       126
            micro-avg       0.88      0.85      0.87      2060
            macro-avg       0.89      0.86      0.87      2060
         weighted-avg       0.88      0.85      0.87      2060
```
