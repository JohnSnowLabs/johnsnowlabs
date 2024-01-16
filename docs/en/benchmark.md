---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Speed Bencmarks
permalink: /docs/en/benchmark
key: docs-benchmark
modify_date: "2021-10-04"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## Cluster Speed Benchmarks

### NER (BiLSTM-CNN-Char Architecture) Benchmark Experiment

- **Dataset :** 1000 Clinical Texts from MTSamples Oncology Dataset, approx. 500 tokens per text.
- **Driver :** Standard_D4s_v3 - 16 GB Memory - 4 Cores
- **Enable Autoscaling :** False
- **Cluster Mode :** Standart
- **Worker :**
  - Standard_D4s_v3 - 16 GB Memory - 4 Cores
  - Standard_D4s_v2 - 28 GB Memory - 8 Cores
- **Versions :**
  - **Databricks Runtime Version :** 8.3(Scala 2.12, Spark 3.1.1)
  - **spark-nlp Version:** v3.2.3
  - **spark-nlp-jsl Version :** v3.2.3
  - **Spark Version :** v3.1.1
- **Spark NLP Pipeline :**

  ```
  nlpPipeline = Pipeline(stages=[
        documentAssembler,
        sentenceDetector,
        tokenizer,  
        embeddings_clinical,  
        clinical_ner,  
        ner_converter
        ])

  ```
  
**NOTES :**

+ **The first experiment with 5 different cluster configurations :** `ner_chunk`  as a column in Spark NLP Pipeline (`ner_converter`) output data frame, exploded (lazy evaluation) as `ner_chunk` and `ner_label`. Then results were written as **parquet** and **delta** formats.

+ **A second experiment with 2 different cluster configuration :** Spark NLP Pipeline output data frame (except `word_embeddings` column) was written as **parquet** and **delta** formats.

+ In the first experiment with the most basic driver node and worker **(1 worker x 4 cores)** configuration selection, it took **4.64 mins** and **4.53 mins** to write **4 partitioned data** as parquet and delta formats respectively.

+ With basic driver node and **8 workers (x8 cores)** configuration selection, it took **40 seconds** and **22 seconds** to write **1000 partitioned data** as parquet and delta formats respectively.

+ In the second experiment with basic driver node and **4 workers (x 4 cores)** configuration selection, it took **1.41 mins** as parquet and **1.42 mins** as delta format to write **16 partitioned (exploded results) data**.  **Without explode it took 1.08 mins as parquet and 1.12 mins as delta format to write the data frame.**

+ Since given computation durations are highly dependent on different parameters including driver node and worker node configurations as well as partitions, **results show that explode method increases duration  %10-30  on chosen configurations.**

</div>
<div class="h3-box" markdown="1">

#### NER Benchmark Tables

{:.table-model-big.db}
| driver\_name      | driver\_memory | driver\_cores | worker\_name      | worker\_memory | worker\_cores | input\_data\_rows | output\_data\_rows | action           | total\_worker\_number | total\_cores | partition | NER timing|NER+RE timing|
| ----------------- | -------------- | ------------- | ----------------- | -------------- | ------------- | ----------------- | ------------------ | ---------------- | --------------------- | ------------ | --------- | --------  |-----------  |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v2 | 28 GB          | 8             | 1000              | 78000              | write\_parquet   | 8                     | 64           | 64        | 36 sec    | 1.14 mins   |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v2 | 28 GB          | 8             | 1000              | 78000              | write\_deltalake | 8                     | 64           | 64        | 19 sec    | 1.13 mins   |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v2 | 28 GB          | 8             | 1000              | 78000              | write\_parquet   | 8                     | 64           | 100       | 21 sec    | 50 sec      |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v2 | 28 GB          | 8             | 1000              | 78000              | write\_deltalake | 8                     | 64           | 100       | 41 sec    | 51 sec      |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v2 | 28 GB          | 8             | 1000              | 78000              | write\_parquet   | 8                     | 64           | 1000      | 40 sec    | 54 sec      |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v2 | 28 GB          | 8             | 1000              | 78000              | write\_deltalake | 8                     | 64           | 1000      | 22 sec    | 46 sec      |


{:.table-model-big.db}
| driver\_name      | driver\_memory | driver\_cores | worker\_name      | worker\_memory | worker\_cores | input\_data\_rows | output\_data\_rows | action           | total\_worker\_number | total\_cores | partition | duration  |NER+RE timing|
| ----------------- | -------------- | ------------- | ----------------- | -------------- | ------------- | ----------------- | ------------------ | ---------------- | --------------------- | ------------ | --------- | --------- |-----------  |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_parquet   | 8                     | 32           | 32        | 1.21 mins | 2.05 mins   |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_deltalake | 8                     | 32           | 32        | 55.8 sec  | 1.91 mins   |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_parquet   | 8                     | 32           | 100       | 41 sec    | 1.64 mins   |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_deltalake | 8                     | 32           | 100       | 48 sec    | 1.61 mins   |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_parquet   | 8                     | 32           | 1000      | 1.36 min  | 1.83 mins   |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_deltalake | 8                     | 32           | 1000      | 48 sec    | 1.70 mins   |


{:.table-model-big.db}
| driver\_name      | driver\_memory | driver\_cores | worker\_name      | worker\_memory | worker\_cores | input\_data\_rows | output\_data\_rows | action           | total\_worker\_number | total\_cores | partition | NER timing|NER+RE timing|
| ----------------- | -------------- | ------------- | ----------------- | -------------- | ------------- | ----------------- | ------------------ | ---------------- | --------------------- | ------------ | --------- | --------- |-----------  |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_parquet   | 4                     | 16           | 10        | 1.4 mins  |  3.78 mins  |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_deltalake | 4                     | 16           | 10        | 1.76 mins |  3.93 mins  |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_parquet   | 4                     | 16           | 16        | 1.41 mins |  3.97 mins  |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_deltalake | 4                     | 16           | 16        | 1.42 mins |  3.82 mins  |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_parquet   | 4                     | 16           | 32        | 1.36 mins |  3.70 mins  |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_deltalake | 4                     | 16           | 32        | 1.35 mins |  3.65 mins  |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_parquet   | 4                     | 16           | 100       | 1.21 mins |  3.18 mins  |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_deltalake | 4                     | 16           | 100       | 1.24 mins |  3.15 mins  |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_parquet   | 4                     | 16           | 1000      | 1.42 mins |  3.51 mins  |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_deltalake | 4                     | 16           | 1000      | 1.46 mins |  3.48 mins  |

{:.table-model-big.db}
| driver\_name      | driver\_memory | driver\_cores | worker\_name      | worker\_memory | worker\_cores | input\_data\_rows | output\_data\_rows | action           | total\_worker\_number | total\_cores | partition | NER timing|NER+RE timing|
| ----------------- | -------------- | ------------- | ----------------- | -------------- | ------------- | ----------------- | ------------------ | ---------------- | --------------------- | ------------ | --------- | --------- |------------ |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_parquet   | 2                     | 8            | 10        | 2.82 mins | 5.91 mins  |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_deltalake | 2                     | 8            | 10        | 2.82 mins | 5.99 mins  |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_parquet   | 2                     | 8            | 100       | 2.27 mins | 5.29 mins  |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_deltalake | 2                     | 8            | 100       | 2.25 min  | 5.26 mins  |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_parquet   | 2                     | 8            | 1000      | 2.65 mins | 5.78 mins  |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_deltalake | 2                     | 8            | 1000      | 2.7 mins  | 5.81 mins  |


{:.table-model-big.db}
| driver\_name      | driver\_memory | driver\_cores | worker\_name      | worker\_memory | worker\_cores | input\_data\_rows | output\_data\_rows | action           | total\_worker\_number | total\_cores | partition | NER timing|NER+RE timing|
| ----------------- | -------------- | ------------- | ----------------- | -------------- | ------------- | ----------------- | ------------------ | ---------------- | --------------------- | ------------ | --------- | --------- |----------- |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_parquet   | 1                     | 4            | 4         | 4.64 mins | 13.97 mins |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_deltalake | 1                     | 4            | 4         | 4.53 mins | 13.88 mins |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_parquet   | 1                     | 4            | 10        | 4.42 mins | 14.13 mins |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_deltalake | 1                     | 4            | 10        | 4.55 mins | 14.63 mins |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_parquet   | 1                     | 4            | 100       | 4.19 mins | 14.68 mins |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_deltalake | 1                     | 4            | 100       | 4.18 mins | 14.89 mins |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_parquet   | 1                     | 4            | 1000      | 5.01 mins | 16.38 mins |
| Standard\_D4s\_v3 | 16 GB          | 4             | Standard\_D4s\_v3 | 16 GB          | 4             | 1000              | 78000              | write\_deltalake | 1                     | 4            | 1000      | 4.99 mins | 16.52 mins |



</div>
<div class="h3-box" markdown="1">

### Clinical Bert For Token Classification Benchmark Experiment

- **Dataset :** 7537 Clinical Texts from PubMed Dataset
- **Driver :** Standard_DS3_v2 - 14GB Memory - 4 Cores
- **Enable Autoscaling :** True
- **Cluster Mode :** Standart
- **Worker :**
  - Standard_DS3_v2 - 14GB Memory - 4 Cores
- **Versions :**
  - **Databricks Runtime Version :** 10.0 (Apache Spark 3.2.0, Scala 2.12)
  - **spark-nlp Version:** v3.4.0
  - **spark-nlp-jsl Version :** v3.4.0
  - **Spark Version :** v3.2.0
- **Spark NLP Pipeline :**

```
nlpPipeline = Pipeline(stages=[
        documentAssembler,
        sentenceDetector,
        tokenizer,
        ner_jsl_slim_tokenClassifier,
        ner_converter,
        finisher])
```

**NOTES :**

+ In this experiment, the `bert_token_classifier_ner_jsl_slim` model was used to measure the inference time of clinical bert for token classification models in the databricks environment.
+ In the first experiment, the data read from the parquet file is saved as parquet after processing.

+ In the second experiment, the data read from the delta table was written to the delta table after it was processed.

</div>

#### Bert For Token Classification Benchmark Table

<div class="h3-box" markdown="1">

<table class="table-model-big table3">
    <thead>
        <tr>
            <th></th>
            <th>Repartition</th>
            <th>Time</th>
        </tr>
    </thead>    
    <tbody>
        <tr>
            <td rowspan="4"><strong>Read data from parquet</strong></td>
            <td>2</td>
            <td>26.03 mins</td>
        </tr>
        <tr>
            <td>64</td>
            <td>10.84 mins</td>
        </tr>
        <tr>
            <td>128</td>
            <td>7.53 mins</td>
        </tr>
        <tr>
            <td>1000</td>
            <td>8.93 mins</td>
        </tr>
        <tr>
            <td rowspan="4"><strong>Read data from delta table</strong></td>
            <td>2</td>
            <td>40.50 mins</td>
        </tr>
        <tr>
            <td>64</td>
            <td>11.84 mins</td>
        </tr>
        <tr>
            <td>128</td>
            <td>6.79 mins</td>
        </tr>
        <tr>
            <td>1000</td>
            <td>6.92 mins</td>
        </tr>
    </tbody>
</table>

</div>



<div class="h3-box" markdown="1">

### NER speed benchmarks across various Spark NLP and PySpark versions

This experiment compares the ClinicalNER runtime for different versions of `PySpark` and `Spark NLP`. 
In this experiment, all reports went through the pipeline 10 times and repeated execution 5 times, so we ran each report 50 times and averaged it, `%timeit -r 5 -n 10 run_model(spark, model)`.

- **Driver :** Standard Google Colab environment
- **Spark NLP Pipeline :**
```
nlpPipeline = Pipeline(
      stages=[
          documentAssembler,
          sentenceDetector,
          tokenizer,
          word_embeddings,
          clinical_ner,
          ner_converter
          ])
```

- **Dataset :** File sizes:
  - report_1: ~5.34kb
  - report_2: ~8.51kb
  - report_3: ~11.05kb
  - report_4: ~15.67kb
  - report_5: ~35.23kb


{:.table-model-big.db}
|          |Spark NLP 4.0.0 (PySpark 3.1.2) |Spark NLP 4.2.1 (PySpark 3.3.1) |Spark NLP 4.2.1 (PySpark 3.1.2) |Spark NLP 4.2.2 (PySpark 3.1.2) |Spark NLP 4.2.2 (PySpark 3.3.1) |Spark NLP 4.2.3 (PySpark 3.3.1) |Spark NLP 4.2.3 (PySpark 3.1.2) |
|:---------|-------------------------------:|-------------------------------:|-------------------------------:|-------------------------------:|-------------------------------:|-------------------------------:|-------------------------------:|
| report_1 |                        2.36066 |                        3.33056 |                        2.23723 |                        2.27243 |                        2.11513 |                        2.19655 |                        2.23915 |
| report_2 |                        2.2179  |                        3.31328 |                        2.15578 |                        2.23432 |                        2.07259 |                        2.07567 |                        2.16776 |
| report_3 |                        2.77923 |                        2.6134  |                        2.69023 |                        2.76358 |                        2.55306 |                        2.4424  |                        2.72496 |
| report_4 |                        4.41064 |                        4.07398 |                        4.66656 |                        4.59879 |                        3.98586 |                        3.92184 |                        4.6145  |
| report_5 |                        9.54389 |                        7.79465 |                        9.25499 |                        9.42764 |                        8.02252 |                        8.11318 |                        9.46555 |


Results show that the different versions can have some variance in the execution time, but the difference is not too relevant. 

</div>

<div class="h3-box" markdown="1">

### ChunkMapper + Sentence Entity Resolver Benchmark Experiment

- **Dataset :** 100 Clinical Texts from MTSamples, approx. 705 tokens and 11 chunks per text.

- **Versions :**
  - **Databricks Runtime Version :** 12.2 LTS(Scala 2.12, Spark 3.3.2)
  - **spark-nlp Version:** v5.2.0
  - **spark-nlp-jsl Version :** v5.2.0
  - **Spark Version :** v3.3.2

- **Spark NLP Pipelines :**

ChunkMapper Pipeline:

  ```
    mapper_pipeline = Pipeline().setStages([
        document_assembler,
        sentence_detector,
        tokenizer,
        word_embeddings,
        ner_model,
        ner_converter,
        chunkerMapper])

  ```

Sentence Entity Resolver Pipeline:

```
    resolver_pipeline = Pipeline(
        stages = [
            document_assembler,
            sentenceDetectorDL,
            tokenizer,
            word_embeddings,
            ner_model,
            ner_converter,
            c2doc,
            sbert_embedder,
            rxnorm_resolver
      ])

```

ChunkMapper + Sentence Entity Resolver Pipeline:

```
mapper_resolver_pipeline = Pipeline(
    stages = [
        document_assembler,
        sentence_detector,
        tokenizer,
        word_embeddings,
        ner_model,
        ner_converter,
        chunkerMapper,
        cfModel,
        chunk2doc,
        sbert_embedder,
        rxnorm_resolver,
        resolverMerger
])

```

**NOTES:**

+ **3 different pipelines:**
The first pipeline with ChunkMapper, the second with Sentence Entity Resolver, and the third pipeline with ChunkMapper and Sentence Entity Resolver together.

+ **4 different cluster configurations:**
Driver and worker types were kept the same in all cluster configurations. The number of workers were increased gradually and set as 2, 4, 8, 10.

+ **NER models were kept as same in all pipelines:** Pretrained `ner_posology_greedy` NER model was used in each pipeline.

#### Benchmark Tables

These  figures might differ based on the size of the mapper and resolver models. The larger the models, the higher the inference times.
Depending on the success rate of mappers (any chunk coming in caught by the mapper successfully), the combined mapper and resolver timing would be less than resolver-only timing.

If the resolver-only timing is equal to or very close to the combined mapper and resolver timing, it means that the mapper is not capable of catching/ mapping any chunk.
In that case, try playing with various parameters in the mapper or retrain/ augment the mapper.

- Driver Name: Standard_DS3_v2
- Driver Memory: 14GB
- Worker Name: Standard_DS3_v2
- Worker Memory: 14GB
- Worker Cores: 4
- Action: write_parquet
- Total Worker Numbers: 2
- Total Cores: 8

| partition | mapper timing | resolver timing | mapper+resolver timing |
| --------- | ------------- | --------------- | ---------------------- |
| 4         | 23 sec        | 4.36 mins       | 2.40 mins              |
| 8         | 15 sec        | 3.21 mins       | 1.48 mins              |
| 16        | 18 sec        | 2.52 mins       | 2.04 mins              |
| 32        | 13 sec        | 2.22 mins       | 1.38 mins              |
| 64        | 14 sec        | 2.36 sec        | 1.50 mins              |
| 100       | 14 sec        | 2.21 sec        | 1.36 mins              |
| 1000      | 21 sec        | 2.23 mins       | 1.43 mins              |

- Driver Name: Standard_DS3_v2
- Driver Memory: 14GB
- Worker Name: Standard_DS3_v2
- Worker Memory: 14GB
- Worker Cores: 4
- Action: write_parquet
- Total Worker Numbers: 4
- Total Cores: 16

| partition | mapper timing | resolver timing | mapper+resolver timing |
| --------- | ------------- | --------------- | ---------------------- |
| 4         | 32.5 sec      | 4.19 mins       | 2.58 mins              |
| 8         | 15.1 sec      | 2.25 mins       | 1.38 mins              |
| 16        | 9.52 sec      | 1.50 mins       | 1.15 mins              |
| 32        | 9.16 sec      | 1.47 mins       | 1.09 mins              |
| 64        | 9.32 sec      | 1.36 mins       | 1.03 mins              |
| 100       | 9.97 sec      | 1.48 mins       | 1.11 mins              |
| 1000      | 12.5 sec      | 1.31 mins       | 1.03 mins              |

- Driver Name: Standard_DS3_v2
- Driver Memory: 14GB
- Worker Name: Standard_DS3_v2
- Worker Memory: 14GB
- Worker Cores: 4
- Action: write_parquet
- Total Worker Numbers: 8
- Total Cores: 32

| partition | mapper timing | resolver timing | mapper+resolver timing |
| --------- | ------------- | --------------- | ---------------------- |
| 4         | 37.3 sec      | 4.46 mins       | 2.52 mins              |
| 8         | 26.7 sec      | 2.46 mins       | 1.37 mins              |
| 16        | 8.85 sec      | 1.27 mins       | 1.06 mins              |
| 32        | 7.74 sec      | 1.38 mins       | 54.5 sec               |
| 64        | 7.22 sec      | 1.23 mins       | 55.6 sec               |
| 100       | 6.32 sec      | 1.16 mins       | 50.9 sec               |
| 1000      | 8.37 sec      | 59.6 sec        | 49.3 sec               |

- Driver Name: Standard_DS3_v2
- Driver Memory: 14GB
- Worker Name: Standard_DS3_v2
- Worker Memory: 14GB
- Worker Cores: 4
- Action: write_parquet
- Total Worker Numbers: 10
- Total Cores: 40

| partition | mapper timing | resolver timing | mapper+resolver timing |
| --------- | ------------- | --------------- | ---------------------- |
| 4         | 40.8 sec      | 4.55 mins       | 3.20 mins              |
| 8         | 30.1 sec      | 3.34 mins       | 1.59 mins              |
| 16        | 11.6 sec      | 1.57 mins       | 1.12 mins              |
| 32        | 7.84 sec      | 1.33 mins       | 55.9 sec               |
| 64        | 7.25 sec      | 1.18 mins       | 56.1 sec               |
| 100       | 7.45 sec      | 1.05 mins       | 47.5 sec               |
| 1000      | 8.87 sec      | 1.14 mins       | 47.9 sec               |

</div>

<div class="h3-box" markdown="1">

### Deidentification Benchmark Experiment
 
- **Dataset:** 10000 Clinical Texts from MTSamples, approx. 503 tokens and 6 chunks per text.
 
- **Versions :**
  - **Databricks Runtime Version :** 12.2 LTS(Scala 2.12, Spark 3.3.2)
  - **spark-nlp Version:** v5.2.0
  - **spark-nlp-jsl Version :** v5.2.0
  - **Spark Version :** v3.3.2
 
- Driver Name: Standard_DS3_v2
- Driver Memory: 14GB
- Worker Name: Standard_DS3_v2
- Worker Memory: 14GB
- Worker Cores: 4
- Action:  write_parquet
- Total Worker Numbers: 10
- Total Cores: 40
 
 
- **Spark NLP Pipelines :**
 
Deidentification Pipeline:

```
    deid_pipeline = Pipeline().setStages([
      document_assembler,
      sentence_detector,
      tokenizer,
      word_embeddings,
      deid_ner,
      ner_converter,
      deid_ner_enriched,
      ner_converter_enriched,
      chunk_merge,
      ssn_parser,
      account_parser,
      dln_parser,
      plate_parser,
      vin_parser,
      license_parser,
      country_parser,
      age_parser,
      date_parser,
      phone_parser1,
      phone_parser2,
      ids_parser,
      zip_parser,
      med_parser,
      email_parser,
      chunk_merge1,
      chunk_merge2,
      deid_masked_rgx,
      deid_masked_char,
      deid_masked_fixed_char,
      deid_obfuscated,
      finisher])
```

|partition|data write|data read|transform| result timing |
|--------:|---------:|--------:|--------:|--------------:|
|   1024  |13.98 sec |0.94 sec |1.81 sec | 9 min  21 sec |
|    512  | 7.94 sec |0.51 sec |1.73 sec | 8 min  44 sec |
|    256  | 6.76 sec |0.42 sec |1.73 sec | 8 min  54 sec |
|    128  | 2.27 sec |0.32 sec |1.74 sec | 9 min  34 sec |
|     64  | 5.85 sec |0.24 sec |2.07 sec | 11 min  1 sec |
|     32  | 1.50 sec |0.22 sec |1.72 sec | 14 min 29 sec |
|     16  | 1.44 sec |0.26 sec |1.54 sec | 16 min 32 sec |
|      8  | 1.57 sec |0.19 sec |1.59 sec | 27 min 43 sec |
|      4  | 1.29 sec |0.20 sec |1.57 sec | 53 min 43 sec |

</div>

<div class="h3-box" markdown="1">

## CPU NER Benchmarks

### NER (BiLSTM-CNN-Char Architecture) CPU Benchmark Experiment

- **Dataset:** 1000 Clinical Texts from MTSamples Oncology Dataset, approx. 500 tokens per text.
- **Versions :**
  - **spark-nlp Version:** v3.4.4
  - **spark-nlp-jsl Version :** v3.5.2
  - **Spark Version :** v3.1.2
- **Spark NLP Pipeline:**

```python
  nlpPipeline = Pipeline(stages=[
        documentAssembler,
        sentenceDetector,
        tokenizer,  
        embeddings_clinical,  
        clinical_ner,  
        ner_converter
        ])
```

**NOTE:**

- Spark NLP Pipeline output data frame (except `word_embeddings` column) was written as **parquet** format in `transform` benchmarks.

</div><div class="h3-box" markdown="1">

<table class="table-model-big table3">
    <thead>
        <tr>
            <th>Plarform</th>
            <th>Process</th>
            <th>Repartition</th>
            <th>Time</th>
        </tr>
    </thead>    
    <tbody>
        <tr>
            <td rowspan="4">2 CPU cores, 13 GB RAM (Google COLAB)</td>
            <td>LP (fullAnnotate)</td>
            <td>-</td>
            <td>16min 52s</td>
        </tr>
        <tr>
            <td rowspan="3">Transform (parquet)</td>
            <td>10</td>
            <td>4min 47s</td>
        </tr>
        <tr>
            <td>100</td>
            <td><strong>4min 16s</strong></td>
        </tr>
        <tr>
            <td>1000</td>
            <td>5min 4s</td>
        </tr>
        <tr>
            <td rowspan="4">16 CPU cores, 27 GB RAM (AWS EC2 machine)</td>
            <td>LP (fullAnnotate)</td>
            <td>-</td>
            <td>14min 28s</td>
        </tr>
        <tr>
            <td rowspan="3">Transform (parquet)</td>
            <td>10</td>
            <td>1min 5s</td>
        </tr>
        <tr>
            <td>100</td>
            <td><strong>1min 1s</strong></td>
        </tr>
        <tr>
            <td>1000</td>
            <td>1min 19s</td>
        </tr>
    </tbody>
</table>

</div>
<div class="h3-box" markdown="1">

## GPU vs CPU benchmark

This section includes a benchmark for MedicalNerApproach(), comparing its performance when running in `m5.8xlarge` CPU vs a `Tesla V100 SXM2` GPU, as described in the `Machine Specs` section below.

Big improvements have been carried out from version 3.3.4, so please, make sure you use at least that version to fully levearge Spark NLP capabilities on GPU.

</div>
<div class="h3-box" markdown="1">

### Machine specs

#### CPU
An AWS `m5.8xlarge` machine was used for the CPU benchmarking. This machine consists of `32 vCPUs` and `128 GB of RAM`, as you can check in the official specification webpage available [here](https://aws.amazon.com/ec2/instance-types/m5/)

</div>
<div class="h3-box" markdown="1">

#### GPU
A `Tesla V100 SXM2` GPU with `32GB` of memory was used to calculate the GPU benchmarking.

</div>
<div class="h3-box" markdown="1">

### Versions
The benchmarking was carried out with the following Spark NLP versions:

Spark version: `3.0.2`

Hadoop version: `3.2.0`

SparkNLP version: `3.3.4`

SparkNLP for Healthcare version: `3.3.4`

Spark nodes: 1

</div>
<div class="h3-box" markdown="1">

### Benchmark on MedicalNerDLApproach()

This experiment consisted of training a Name Entity Recognition model (token-level), using our class NerDLApproach(), using Bert Word Embeddings and a Char-CNN-BiLSTM Neural Network. Only 1 Spark node was used for the training.

We used the Spark NLP class `MedicalNer` and it's method `Approach()` as described in the [documentation](https://nlp.johnsnowlabs.com/docs/en/licensed_annotators#medicalner).

The pipeline looks as follows:
![](/assets/images/CPUvsGPUbenchmarkpic4.png)

</div>
<div class="h3-box" markdown="1">

#### Dataset
The size of the dataset was small (17K), consisting of:

Training (rows): `14041`

Test (rows): `3250`

</div>
<div class="h3-box" markdown="1">

#### Training params
Different batch sizes were tested to demonstrate how GPU performance improves with bigger batches compared to CPU, for a constant number of epochs and learning rate.

Epochs: `10`

Learning rate:  `0.003`

Batch sizes: `32`, `64`, `256`,  `512`, `1024`, `2048`

</div>
<div class="h3-box" markdown="1">

#### Results
Even for this small dataset, we can observe that GPU is able to beat the CPU machine by a `62%` in `training` time and a `68%` in `inference` times. It's important to mention that the batch size is very relevant when using GPU, since CPU scales much worse with bigger batch sizes than GPU.

</div>
<div class="h3-box" markdown="1">

#### Training times depending on batch (in minutes)

![](/assets/images/CPUvsGPUbenchmarkpic6.png)

{:.table-model-big}
| Batch size | CPU | GPU |
| :---: | :---: | :--: |
| 32 | 9.5 | 10 |
| 64 | 8.1 | 6.5 |
| 256 | 6.9 | 3.5 |
| 512 | 6.7 | 3 |
| 1024 | 6.5 | 2.5 |
| 2048 | 6.5 | 2.5 |

</div>
<div class="h3-box" markdown="1">

#### Inference times (in minutes)
Although CPU times in inference remain more or less constant regardless the batch sizes, GPU time experiment good improvements the bigger the batch size is.

CPU times: `~29 min`

{:.table-model-big}
| Batch size |  GPU |
| :---: | :--: |
| 32 | 10 |
| 64 | 6.5 |
| 256 | 3.5 |
| 512 | 3 |
| 1024 | 2.5 |
| 2048 | 2.5 |

![](/assets/images/CPUvsGPUbenchmarkpic7.png)

</div>
<div class="h3-box" markdown="1">

#### Performance metrics
A macro F1-score of about `0.92` (`0.90` in micro) was achieved, with the following charts extracted from the `MedicalNerApproach()` logs:

![](/assets/images/CPUvsGPUbenchmarkpic8.png)

</div>
<div class="h3-box" markdown="1">

### Takeaways: How to get the best of the GPU
You will experiment big GPU improvements in the following cases:

{:.list1}
1. Embeddings and Transformers are used in your pipeline. Take into consideration that GPU will performance very well in Embeddings / Transformer components, but other components of your pipeline may not leverage as well GPU capabilities;
2. Bigger batch sizes get the best of GPU, while CPU does not scale with bigger batch sizes;
3. Bigger dataset sizes get the best of GPU, while may be a bottleneck while running in CPU and lead to performance drops;

</div>
<div class="h3-box" markdown="1">

### MultiGPU Inference on Databricks
In this part, we will give you an idea on how to choose appropriate hardware specifications for Databricks. Here is a few different hardwares, their prices, as well as their performance:
![image](https://user-images.githubusercontent.com/25952802/158796429-78ec52b1-c036-4a9c-89c2-d3d1f395f71d.png)

Apparently, GPU hardware is the cheapest among them although it performs the best. Let's see how overall performance looks like:

![image](https://user-images.githubusercontent.com/25952802/158799106-8ee03a8b-8590-49ae-9657-b9663b915324.png)

Figure above clearly shows us that GPU should be the first option of ours. 

In conclusion, please find the best specifications for your use case since these benchmarks might depend on dataset size, inference batch size, quickness, pricing and so on.

Please refer to this video for further info: https://events.johnsnowlabs.com/webinar-speed-optimization-benchmarks-in-spark-nlp-3-making-the-most-of-modern-hardware?hsCtaTracking=a9bb6358-92bd-4cf3-b97c-e76cb1dfb6ef%7C4edba435-1adb-49fc-83fd-891a7506a417

### MultiGPU training
Currently, we don't support multiGPU training, meaning training 1 model in different GPUs in parallel. However, you can train different models in different GPUs.

</div>
<div class="h3-box" markdown="1">

### MultiGPU inference
Spark NLP can carry out MultiGPU inference if GPUs are in different cluster nodes. For example, if you have a cluster with different GPUs, you can repartition your data to match the number of GPU nodes and then coalesce to retrieve the results back to the master node. 

Currently, inference on multiple GPUs on the same machine is not supported.

### Where to look for more information about Training
Please, take a look at the [Spark NLP](https://nlp.johnsnowlabs.com/docs/en/training) and [Spark NLP for Healthcare](https://nlp.johnsnowlabs.com/docs/en/licensed_training) Training sections, and feel free to reach us out in case you want to maximize the performance on your GPU.

</div>
<div class="h3-box" markdown="1">

## Spark NLP vs Spacy Pandas UDF with Arrow Benchmark

This benchmarking report aims to provide a comprehensive comparison between two NLP frameworks on Spark clusters: Spark NLP and SpaCy, specifically in the context of Pandas UDF with Arrow optimization.

Spark NLP is a distributed NLP library built on top of Apache Spark, designed to handle large-scale NLP tasks efficiently. On the other hand, SpaCy is a popular NLP library in single-machine environments.

In this benchmark, we evaluate the performance of both frameworks using Pandas UDF with Arrow, a feature that enhances data transfer between Apache Arrow and Pandas DataFrames, potentially leading to significant performance gains. We will use Spacy as a UDF in Spark to compare the performance of both frameworks.

The benchmark covers a range of common NLP tasks, including Named Entity Recognition (NER) and getting Roberta sentence embeddings.

We calculated the time for both arrow enabled and disabled pandas udf for each task. We reset the notebook before each task to ensure that the results are not affected by the previous task.

</div><div class="h3-box" markdown="1">

### Machine specs

Azure Databricks `Standard_DS3_v2` machine (6 workers + 1 driver) was used for the CPU benchmarking. This machine consists of `4 CPUs` and `14 GB of RAM`.

</div><div class="h3-box" markdown="1">

### Versions

The benchmarking was carried out with the following versions:

Spark version: `3.1.2`

SparkNLP version: `5.1.0`

spaCy version: `3.6.1`

Spark nodes: 7 (1 driver, 6 workers)

</div><div class="h3-box" markdown="1">

### Dataset

The size of the dataset is (120K), consisting of news articles that can be found [here](https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/open-source-nlp/data/news_category_train.csv).

</div><div class="h3-box" markdown="1">

### Benchmark on Named Entity Recognition (NER)

Named Entity Recognition (NER) is the process of identifying and classifying named entities in a text into predefined categories such as person names, organizations, locations, etc. In this benchmark, we compare the performance of Spark NLP and SpaCy in recognizing named entities in a text column.

The following pipeline shows how to recognize named entities in a text column using Spark NLP:

```python
glove_embeddings = WordEmbeddingsModel.pretrained('glove_100d').\
    setInputCols(["document", 'token']).\
    setOutputCol("embeddings")

public_ner = NerDLModel.pretrained("ner_dl", 'en') \
    .setInputCols(["document", "token", "embeddings"]) \
    .setOutputCol("ner")

pipeline = Pipeline(stages=[document_assembler,
                              tokenizer,
                              glove_embeddings,
                              public_ner
                           ])
```

SpaCy uses the following pandas UDF to recognize named entities in a text column. We exclude the tagger, parser, attribute ruler, and lemmatizer components to make the comparison fair.

```python
nlp_ner = spacy.load("en_core_web_sm", exclude=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"])

# Define a UDF to  perform NER
@pandas_udf(ArrayType(StringType()))
def ner_with_spacy(text_series):
    entities_list = []
    for text in text_series:
        doc = nlp_ner(text)
        entities = [f"{ent.text}:::{ent.label_}" for ent in doc.ents]
        entities_list.append(entities)
    return pd.Series(entities_list)
```

</div><div class="h3-box" markdown="1">

### Benchmark on Getting Roberta Sentence Embeddings

In this benchmark, we compare the performance of Spark NLP and SpaCy in getting Roberta sentence embeddings for a text column.

The following pipeline shows how to get Roberta embeddings for a text column using Spark NLP:

```python
embeddings = RoBertaSentenceEmbeddings.pretrained("sent_roberta_base", "en") \
      .setInputCols("document") \
      .setOutputCol("embeddings")

pipeline= Pipeline(stages=[document_assembler,
                            embeddings
                           ])
```

SpaCy uses the following pandas UDF.

```python
nlp_embeddings = spacy.load("en_core_web_trf")

# Define a UDF to get sentence embeddings 
@pandas_udf(ArrayType(FloatType()))
def embeddings_with_spacy(text_series):
    embeddings_list = []
    for text in text_series:
        doc = nlp_embeddings(text)
        embeddings = doc._.trf_data.tensors[-1][0]
        embeddings_list.append(embeddings)
    return pd.Series(embeddings_list)
```

</div><div class="h3-box" markdown="1">

### Results

Both frameworks were tested on a dataset of 120K rows. SpaCy was tested with and without Arrow enabled. Both frameworks utilized distributed computing to process the data in parallel.

 The following table shows the time taken by each framework to perform the tasks mentioned above:

{:.table-model-big}
| **Task**               | **Spark NLP** | **Spacy UDF with Arrow** | **Spacy UDF without Arrow** |
|------------------------|---------------|----------------------|------------------------|
| **NER extract**        | 3min 35sec    | 4min 49sec           | 5min 4sec              |
| **Roberta Embeddings** | 22min 16sec   | 29min 27sec          | 29min 30sec            |

</div><div class="h3-box" markdown="1">

### Conclusions

In our analysis, we delved into the performance of two Natural Language Processing (NLP) libraries: Spark NLP and SpaCy. While Spark NLP, seamlessly integrated with Apache Spark, excels in managing extensive NLP tasks on distributed systems and large datasets, SpaCy is used particularly in single-machine environments.

The results of our evaluation highlight clear disparities in processing times across the assessed tasks. In NER extraction, Spark NLP demonstrated exceptional efficiency, completing the task in a mere 3 minutes and 35 seconds. In contrast, Spacy UDF with Arrow and Spacy UDF without Arrow took 4 minutes and 49 seconds, and 5 minutes and 4 seconds, respectively. Moving on to the generation of Roberta embeddings, Spark NLP once again proved its prowess, completing the task in 22 minutes and 16 seconds. Meanwhile, Spacy UDF with Arrow and Spacy UDF without Arrow required 29 minutes and 27 seconds, and 29 minutes and 30 seconds, respectively.

These findings unequivocally affirm Spark NLP's superiority for NER extraction tasks, and its significant time advantage for tasks involving Roberta embeddings.

</div><div class="h3-box" markdown="1">

### Additional Comments

- **Scalability:**

*Spark NLP*: Built on top of Apache Spark, Spark NLP is inherently scalable and distributed. It is designed to handle large-scale data processing with distributed computing resources. It is well-suited for processing vast amounts of data across multiple nodes.

*SpaCy with pandas UDFs*: Using SpaCy within a pandas UDF (User-Defined Function) and Arrow for efficient data transfer can bring SpaCy's abilities into the Spark ecosystem. However, while Arrow optimizes the serialization and deserialization between JVM and Python processes, the scalability of this approach is still limited by the fact that the actual NLP processing is single-node (by SpaCy) for each partition of your Spark DataFrame.

- **Performance:**

*Spark NLP*: Since it's natively built on top of Spark, it is optimized for distributed processing. The performance is competitive, especially when you are dealing with vast amounts of data that need distributed processing.

*SpaCy with pandas UDFs*: SpaCy is fast for single-node processing. The combination of SpaCy with Arrow-optimized UDFs can be performant for moderate datasets or tasks. However, you might run into bottlenecks when scaling to very large datasets unless you have a massive Spark cluster.

- **Ecosystem Integration:**

*Spark NLP*: Being a Spark-native library, Spark NLP integrates seamlessly with other Spark components, making it easier to build end-to-end data processing pipelines.

*SpaCy with pandas UDFs*: While the integration with Spark is possible, it's a bit more 'forced.' It requires careful handling, especially if you're trying to ensure optimal performance.

- **Features & Capabilities:**

*Spark NLP*: Offers a wide array of NLP functionalities, including some that are tailored for the healthcare domain. It's continuously evolving and has a growing ecosystem.

*SpaCy*: A popular library for NLP with extensive features, optimizations, and pre-trained models. However, certain domain-specific features in Spark NLP might not have direct counterparts in SpaCy.

- **Development & Maintenance:**

*Spark NLP*: As with any distributed system, development and debugging might be more complex. You have to consider factors inherent to distributed systems.

*SpaCy with pandas UDFs*: Development might be more straightforward since you're essentially working with Python functions. However, maintaining optimal performance with larger datasets and ensuring scalability can be tricky.

</div>
