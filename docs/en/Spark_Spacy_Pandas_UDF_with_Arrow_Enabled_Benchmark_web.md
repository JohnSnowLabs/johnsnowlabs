---
layout: docs
header: true
title: Spark NLP vs Spacy Pandas UDF with Arrow Benchmark
permalink: /docs/en/sparknlp_spacy_pandas_udf_arrow_benchmark
key: docs-concepts
modify_date: "2023-09-15"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

This benchmarking report aims to provide a comprehensive comparison between two NLP frameworks on Spark clusters: Spark NLP and SpaCy, specifically in the context of Pandas UDF with Arrow optimization.

Spark NLP is a distributed NLP library built on top of Apache Spark, designed to handle large-scale NLP tasks efficiently. On the other hand, SpaCy is a popular NLP library known for its speed and accuracy in single-machine environments.

In this benchmark, we evaluate the performance of both frameworks using Pandas UDF with Arrow, a feature that enhances data transfer between Apache Arrow and Pandas DataFrames, potentially leading to significant performance gains. We will use Spacy as a UDF in Spark to compare the performance of both frameworks.

The benchmark covers a range of common NLP tasks, including Named Entity Recognition (NER) and getting embeddings.

We calculated the time for both arrow enabled and disabled pandas udf for each task. We reset the notebook before each task to ensure that the results are not affected by the previous task.
</div>

<div class="h3-box" markdown="1">

### Machine specs

Azure Databricks `Standard_DS3_v2` machine (6 workers + 1 driver) was used for the CPU benchmarking. This machine consists of `4 CPUs` and `14 GB of RAM`.
</div>

<div class="h3-box" markdown="1">

### Versions

The benchmarking was carried out with the following versions:

Spark version: `3.1.2`

SparkNLP version: `5.1.0`

spaCy version: `3.6.1`

Spark nodes: 7 (1 driver, 6 workers)
</div>

<div class="h3-box" markdown="1">

### Dataset

The size of the dataset is (120K), consisting of news articles that can be found [here](https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/open-source-nlp/data/news_category_train.csv).
</div>

<div class="h3-box" markdown="1">

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

</div>

<div class="h3-box" markdown="1">

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

</div>

<div class="h3-box" markdown="1">

### Results

Both frameworks were tested on a dataset of 120K rows. SpaCy was tested with and without Arrow enabled. Both frameworks utilized distributed computing to process the data in parallel.

 The following table shows the time taken by each framework to perform the tasks mentioned above:

{:.table-model-big}
| **Task**               | **Spark NLP** | **Spacy UDF with Arrow** | **Spacy UDF without Arrow** |
|------------------------|---------------|----------------------|------------------------|
| **NER extract**        | 3min 35sec    | 4min 49sec           | 5min 4sec              |
| **Roberta Embeddings** | 22min 16sec   | 29min 27sec          | 29min 30sec            |

</div>

<div class="h3-box" markdown="1">

### Comments

1. Scalability:

- Spark NLP: Built on top of Apache Spark, Spark NLP is inherently scalable and distributed. It is designed to handle large-scale data processing with distributed computing resources. It is well-suited for processing vast amounts of data across multiple nodes.
- SpaCy with pandas UDFs: Using SpaCy within a pandas UDF (User-Defined Function) and Arrow for efficient data transfer can bring SpaCy's power into the Spark ecosystem. However, while Arrow optimizes the serialization and deserialization between JVM and Python processes, the scalability of this approach is still limited by the fact that the actual NLP processing is single-node (by SpaCy) for each partition of your Spark DataFrame.

2. Performance:

- Spark NLP: Since it's natively built on top of Spark, it is optimized for distributed processing. The performance is competitive, especially when you are dealing with vast amounts of data that need distributed processing.
- SpaCy with pandas UDFs: SpaCy is incredibly fast and efficient for single-node processing. The combination of SpaCy with Arrow-optimized UDFs can be performant for moderate datasets or tasks. However, you might run into bottlenecks when scaling to very large datasets unless you have a massive Spark cluster.

3. Ecosystem Integration:

- Spark NLP: Being a Spark-native library, Spark NLP integrates seamlessly with other Spark components, making it easier to build end-to-end data processing pipelines.
- SpaCy with pandas UDFs: While the integration with Spark is possible, it's a bit more "forced." It requires careful handling, especially if you're trying to ensure optimal performance.

4. Features & Capabilities:

- Spark NLP: Offers a wide array of NLP functionalities, including some that are tailored for the healthcare domain. It's continuously evolving and has a growing ecosystem.
- SpaCy: A leading library for NLP with extensive features, optimizations, and pre-trained models. However, certain domain-specific features in Spark NLP might not have direct counterparts in SpaCy.

5. Development & Maintenance:

- Spark NLP: As with any distributed system, development and debugging might be more complex. You have to consider factors inherent to distributed systems.
- SpaCy with pandas UDFs: Development might be more straightforward since you're essentially working with Python functions. However, maintaining optimal performance with larger datasets and ensuring scalability can be tricky.

</div>
