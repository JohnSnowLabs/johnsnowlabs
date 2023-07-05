---
layout: model
title: Multilabel Classification For Hallmarks of Cancer
author: John Snow Labs
name: multiclassifierdl_hoc
date: 2023-07-04
tags: [en, classification, hoc, pubmed, licensed, tensorflow]
task: Text Classification
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MultiClassifierDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The process of multi-label document classification involves identifying semantic categories at the document level. In the biomedical domain, these semantic categories are useful for understanding the main topics and searching for relevant literature. Unlike multi-class classification, which assigns only one label to an instance, multi-label classification can assign multiple labels, up to N, to an instance. For the hallmarks of cancer, a manually annotated multi-label document classification dataset called HoC has been created, consisting of 10 labels.

The purpose of the multilabel classification model is to semantically classify an article based on its abstract, specifically related to the hallmarks of cancer. The model determines whether the article is associated with any of the 10 cancer hallmarks listed below:

- Activating Invasion And Metastasis
- Avoiding Immune Destruction
- Cellular Energetics
- Enabling Replicative Immortality
- Evading Growth Suppressors
- Genomic Instability And Mutation
- Inducing Angiogenesis
- Resisting Cell Death
- Sustaining Proliferative Signaling
- Tumor Promoting Inflammation

This model is inspired from [Large language models in biomedical natural language processing: benchmarks, baselines, and recommendations](https://arxiv.org/abs/2305.16326) and augmented internally for better coverage and performance.

## Predicted Entities

`Activating_Invasion_And_Metastasis`, `Avoiding_Immune_Destruction`, `Cellular_Energetics`, `Enabling_Replicative_Immortality`, `Evading_Growth_Suppressors`, `Genomic_Instability_And_Mutation`, `Inducing_Angiogenesis`, `Resisting_Cell_Death`, `Sustaining_Proliferative_Signaling`, `Tumor_Promoting_Inflammation`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/multiclassifierdl_hoc_en_4.4.4_3.0_1688491502473.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/multiclassifierdl_hoc_en_4.4.4_3.0_1688491502473.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["document", "token"])\
    .setOutputCol("word_embeddings")

sentence_embeddings = SentenceEmbeddings()\
    .setInputCols(["document", "word_embeddings"])\
    .setOutputCol("sentence_embeddings")\
    .setPoolingStrategy("AVERAGE")

multi_classifier_dl = MultiClassifierDLModel.pretrained("multiclassifierdl_hoc", "en", "clinical/models")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("category")
    
pipeline = Pipeline(
    stages = [
        document_assembler,
        tokenizer,
        word_embeddings,
        sentence_embeddings,
        multi_classifier_dl
    ])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = pipeline.fit(empty_data)

text = """Often the use of cytotoxic drugs in cancer therapy results in stable disease rather than regression of the tumor , and this is typically seen as a failure of treatment . We now show that DNA damage is able to induce senescence in tumor cells expressing wild-type p53 . We also show that cytotoxics are capable of inducing senescence in tumor tissue in vivo . Our results suggest that p53 and p21 play a central role in the onset of senescence , whereas p16(INK4a) function may be involved in maintaining senescence . Thus , like apoptosis , senescence appears to be a p53-induced cellular response to DNA damage and an important factor in determining treatment outcome ."""

df = spark.createDataFrame([[text]]).toDF("text")

result = model.transform(df)

result.select("text", "category.result").show(truncate=120)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols(Array("document"))
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("document", "token"))
    .setOutputCol("word_embeddings")

val sentence_embeddings = new SentenceEmbeddings()
    .setInputCols(Array("document", "word_embeddings"))
    .setOutputCol("sentence_embeddings")
    .setPoolingStrategy("AVERAGE")

val multi_classifier_dl = MultiClassifierDLModel.pretrained("multiclassifierdl_hoc", "en", "clinical/models")
    .setInputCols(Array("sentence_embeddings"))
    .setOutputCol("category")
    
val pipeline = new Pipeline().setStages(Array(
     document_assembler, 
     tokenizer,
     word_embeddings, 
     sentence_embeddings, 
     multi_classifier_dl))

val data = Seq("""Often the use of cytotoxic drugs in cancer therapy results in stable disease rather than regression of the tumor , and this is typically seen as a failure of treatment . We now show that DNA damage is able to induce senescence in tumor cells expressing wild-type p53 . We also show that cytotoxics are capable of inducing senescence in tumor tissue in vivo . Our results suggest that p53 and p21 play a central role in the onset of senescence , whereas p16(INK4a) function may be involved in maintaining senescence . Thus , like apoptosis , senescence appears to be a p53-induced cellular response to DNA damage and an important factor in determining treatment outcome.""").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
|                                                                                                                    text|                                                                                    result|
+------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
|Often the use of cytotoxic drugs in cancer therapy results in stable disease rather than regression of the tumor , an...|[Genomic_Instability_And_Mutation, Enabling_Replicative_Immortality, Resisting_Cell_Death]|
+------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|multiclassifierdl_hoc|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[class]|
|Language:|en|
|Size:|11.7 MB|

## References

The training dataset is available [here](https://github.com/qingyu-qc/gpt_bionlp_benchmark/tree/main/Benchmarks/Hoc)

## Benchmarking

```bash
label                               precision  recall  f1-score  support 
Activating_Invasion_And_Metastasis  0.83       0.60    0.69      42      
Avoiding_Immune_Destruction         0.70       0.64    0.67      11      
Cellular_Energetics                 1.00       0.64    0.78      11      
Enabling_Replicative_Immortality    0.71       0.77    0.74      13      
Evading_Growth_Suppressors          0.76       0.52    0.62      31      
Genomic_Instability_And_Mutation    0.90       0.88    0.89      49      
Inducing_Angiogenesis               0.80       0.63    0.71      19      
Resisting_Cell_Death                0.80       0.73    0.76      62      
Sustaining_Proliferative_Signaling  0.87       0.69    0.77      67      
Tumor_Promoting_Inflammation        0.84       0.63    0.72      43      
micro-avg                           0.83       0.68    0.75      348     
macro-avg                           0.82       0.67    0.73      348     
weighted-avg                        0.83       0.68    0.75      348     
samples-avg                         0.79       0.74    0.73      348     
```
