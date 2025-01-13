---
layout: model
title: Detect Genes, Human Phenotypes and Related Entities
author: John Snow Labs
name: ner_genes_phenotypes
date: 2025-01-11
tags: [en, clinical, licensed, ner, gene, phenotype, human_phenotype]
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

This Named Entity Recognition (NER) model is specifically trained to extract critical information related to genetics, their phenotypes and associated information contained within any medical document. 

The model recognizes the following entities:

`Clinical_Presentation`: All the medical conditions such as the signs and symptoms.
`Diagnostic_Test`: Medical procedures or tools used to determine the presence, absence, or extent of the genetic disease or condition in an individual.medical procedure or tool used to determine the presence, absence, or extent of the genetic disease or condition in an individual.
`Gene`: Genetic codes and base sequences present such as F508del, or rs1805007 along their normal or pathological variants.
`Gene_Diversity`: Variability of genes within a population.
`Gene_Function`: Function of the normal gene or an Allele.
`Gene_Interaction`: The interplay between different genes and/or between genes and environment that influences the expression of different traits.
`Gene_Penetrance`: Proportion of individuals with a specific genetic mutation or variant who exhibit the associated trait, condition, or disease.
`Incidence`: Number of new cases of a particular disease that occur in a specific population during a defined period.
`Inheritance_Pattern`: The pattern by which a genetic trait or disorder is passed down from one generation to the next.
`MPG`: Names of the genes and molecules, along with the abbreviations, including all the proteins, glycoproteins, polypeptides, or polymers.
`OMIM`: Online Mendelian Inheritance in Man (OMIM® Or MIM) database consist of a list of entries, that catalog human genes and genetic disorders.  
`Other_Disease`: Diseases without apparent genetic causes, such as infectious diseases, traumatic disease/injuries, etc.
`Phenotype_Disease`: Specific disease conditions or manifestations of a disease in an individual, influenced by the underlying genetic causes.
`Prevalence`: Population groups associated with the disease.
`Site`: Site of the genetic mutation or abnormality on the Genome.
`Treatment`: Gene-specific medical strategies, interventions, or therapies used to manage, cure or improve the quality of life in individuals with genetic disorders.
`Type_Of_Mutation`: Type of mutation that occurred in the genome.

## Predicted Entities

`Clinical_Presentation`, `Diagnostic_Test`, `Gene`, `Gene_Diversity`, `Gene_Function`, `Gene_Interaction`, `Gene_Penetrance`, `Incidence`, `Inheritance_Pattern`, `MPG`, `OMIM`, `Other_Disease`, `Phenotype_Disease`, `Prevalence`, `Site`, `Treatment`, `Type_Of_Mutation`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_genes_phenotypes_en_5.5.1_3.0_1736595330406.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_genes_phenotypes_en_5.5.1_3.0_1736595330406.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = MedicalNerModel.pretrained('ner_genes_phenotypes', "en", "clinical/models")\
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
The G6PD gene provides instructions for glucose-6-phosphate dehydrogenase, crucial for protecting cells from oxidative stress. 

Mutations in the G6PD gene cause G6PD deficiency, an X-linked recessive disorder affecting red blood cells. 

Over 400 variants have been identified, with the G6PD A- variant common in African populations. 

The variant G6PD protein results in reduced enzyme activity. 

Clinical presentations of G6PD deficiency include hemolytic anemia triggered by certain medications, foods (e.g., fava beans), or infections. 

Symptoms during hemolytic episodes include jaundice, fatigue, and dark urine. 

Gene-environment interactions are significant, with G6PD deficiency conferring some protection against malaria. 

Diagnosis involves enzyme activity assays and genetic testing. Management focuses on avoiding triggers and providing supportive care during hemolytic episodes. 

In severe cases, blood transfusions may be necessary. Patient education about trigger avoidance is crucial for preventing complications. 

The global prevalence of G6PD deficiency is estimated at 4.9%, with higher rates in malaria-endemic regions.

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

val ner_model = MedicalNerModel.pretrained("ner_genes_phenotypes", "en", "clinical/models")
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

val sample_texts = Seq("""The G6PD gene provides instructions for glucose-6-phosphate dehydrogenase, crucial for protecting cells from oxidative stress. 

Mutations in the G6PD gene cause G6PD deficiency, an X-linked recessive disorder affecting red blood cells. 

Over 400 variants have been identified, with the G6PD A- variant common in African populations. 

The variant G6PD protein results in reduced enzyme activity. 

Clinical presentations of G6PD deficiency include hemolytic anemia triggered by certain medications, foods (e.g., fava beans), or infections. 

Symptoms during hemolytic episodes include jaundice, fatigue, and dark urine. 

Gene-environment interactions are significant, with G6PD deficiency conferring some protection against malaria. 

Diagnosis involves enzyme activity assays and genetic testing. Management focuses on avoiding triggers and providing supportive care during hemolytic episodes. 

In severe cases, blood transfusions may be necessary. Patient education about trigger avoidance is crucial for preventing complications. 

The global prevalence of G6PD deficiency is estimated at 4.9%, with higher rates in malaria-endemic regions.
""").toDF("text")

val result = pipeline.fit(sample_texts).transform(sample_texts)
```
</div>

## Results

```bash
+--------------------------------------+-----+----+---------------------+
|chunk                                 |begin|end |ner_label            |
+--------------------------------------+-----+----+---------------------+
|G6PD gene                             |5    |13  |MPG                  |
|glucose-6-phosphate dehydrogenase     |41   |73  |MPG                  |
|protecting cells from oxidative stress|88   |125 |Gene_Function        |
|G6PD gene                             |145  |153 |MPG                  |
|G6PD deficiency                       |161  |175 |Phenotype_Disease    |
|X-linked recessive                    |181  |198 |Inheritance_Pattern  |
|G6PD A                                |285  |290 |Phenotype_Disease    |
|African populations                   |311  |329 |Prevalence           |
|G6PD protein                          |344  |355 |MPG                  |
|G6PD deficiency                       |419  |433 |Phenotype_Disease    |
|hemolytic anemia                      |443  |458 |Other_Disease        |
|fava beans                            |507  |516 |Gene_Interaction     |
|infections                            |523  |532 |Other_Disease        |
|hemolytic episodes                    |551  |568 |Clinical_Presentation|
|jaundice                              |578  |585 |Clinical_Presentation|
|fatigue                               |588  |594 |Clinical_Presentation|
|dark urine                            |601  |610 |Clinical_Presentation|
|G6PD deficiency                       |665  |679 |Phenotype_Disease    |
|malaria                               |716  |722 |Other_Disease        |
|hemolytic episodes                    |865  |882 |Clinical_Presentation|
|blood transfusions                    |902  |919 |Treatment            |
|G6PD deficiency                       |1047 |1061|Phenotype_Disease    |
+--------------------------------------+-----+----+---------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_genes_phenotypes|
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
                       precision    recall  f1-score   support

Clinical_Presentation       0.78      0.70      0.74       286
      Diagnostic_Test       1.00      0.59      0.74        34
                 Gene       0.78      1.00      0.88        42
       Gene_Diversity       1.00      1.00      1.00        39
        Gene_Function       0.71      0.93      0.80       183
     Gene_Interaction       0.86      0.79      0.82        47
      Gene_Penetrance       0.92      0.92      0.92        64
            Incidence       0.99      0.92      0.95       193
  Inheritance_Pattern       1.00      0.99      0.99       157
                  MPG       0.94      0.91      0.92       667
                 OMIM       1.00      1.00      1.00        18
        Other_Disease       0.77      0.87      0.82       406
    Phenotype_Disease       0.96      0.91      0.93       524
           Prevalence       0.94      0.92      0.93       103
                 Site       0.99      0.93      0.96       106
            Treatment       0.83      0.73      0.77       124
     Type_Of_Mutation       0.95      0.95      0.95       137

            micro avg       0.89      0.88      0.89      3130
            macro avg       0.91      0.89      0.89      3130
         weighted avg       0.89      0.88      0.89      3130
```
