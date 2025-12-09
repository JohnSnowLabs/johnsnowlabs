---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Healthcare NLP Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/licensed_release_notes
key: docs-licensed-release-notes
modify_date: 2025-11-20
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 6.2.1

#### Highlights

We are delighted to announce remarkable enhancements and updates in our latest release of Healthcare NLP. This release focuses on making NER training and clinical document analysis significantly faster and easier with a major upgrade to **Annotation2Training**, major improvements and reduced memory usage in **MedicalNerApproach** training, new one-liner pretrained pipelines and models for end-to-end clinical document understanding. In addition, this version delivers core robustness improvements, refreshed notebooks and demonstrations, and 5 new and updated clinical models and pipelines to further strengthen our Healthcare NLP.


- Major training performance improvements for `MedicalNerApproach`, including significantly reduced memory usage and faster multi-epoch NER training. 
- `Annotation2Training` makes it much easier to prepare high-quality NER training datasets with built-in label filtering, relabeling, CoNLL export, and quick label distribution insights
- Clinical document analysis with one-liner pretrained-pipelines for specific clinical tasks and concepts
- Introducing a new city TextMatcher model for extracting city names from clinical text
- New blog post to understand how to deploy Medical LLMs on Databricks
- Various core improvements; bug fixes, enhanced overall robustness and reliability of Healthcare NLP
- Updated notebooks and demonstrations for making Healthcare NLP easier to navigate and understand
    - New Databricks [Generative AI to Ner Training](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/databricks/python/tutorials/healthcare_tutorials/1.1.Generative_AI_to_Ner_Training.ipynb) Notebook
    - Updated [Generative AI to Ner Training](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.7.Generative_AI_to_Ner_Training.ipynb) Notebook

+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

These enhancements will elevate your experience with Healthcare NLP, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.


</div><div class="h3-box" markdown="1">

#### MedicalNerApproach Training Optimizations: Faster & More Memory-Efficient NER Training

Significant performance upgrades have been introduced to **MedicalNerApproach**, making NER model training faster, lighter, and more efficient—especially when working with BERT-based embeddings or memory-constrained environments.

- **Reduced Memory Usage with BERT-Based Embeddings**  
  Optimized internal handling of output embeddings substantially reduces the peak memory footprint during training. Users can expect **up to 2× lower RAM consumption**, particularly with transformer-based embeddings.

- **Automatic Dataset Caching for Multi-Epoch Training**  
  When using `setEnableMemoryOptimizer(true)` and running with `maxEpoch > 1`, input datasets are now **automatically cached**, resulting in faster epoch transitions and less data reloading overhead.

- **TensorFlow Graph Metadata Reuse**  
  The `MedicalNerDLGraphChecker` now stores TensorFlow graph metadata that can be reused by `MedicalNerApproach`, reducing redundant initialization work and improving overall training responsiveness.

- **Smarter Graph Selection for NER Models**

  We've enhanced the graph selection logic in MedicalNerApproach. It now identifies the most efficient (smallest compatible) TensorFlow graph, resulting in improved performance and lower memory consumption.

</div><div class="h3-box" markdown="1">

#### `Annotation2Training` makes it much easier to prepare high-quality NER training datasets with built-in label filtering, relabeling, CoNLL export, and quick label distribution insights

`Annotation2Training` now turns raw annotation JSON into training-ready NER datasets much faster and with less manual work. With built-in label filtering, on-the-fly relabeling, CoNLL export, and label distribution inspection, you can clean, reshape, and export your data in a few lines of code—making NER training more efficient, shorter to set up, and easier to iterate on.


- **CoNLL file generation (generateConll)**

Generates a CoNLL-2003 formatted file directly from a Spark NLP NER DataFrame, writing TOKEN -X- -X- LABEL lines with -DOCSTART- document headers and sentence boundaries. Supports local paths and DBFS, and enforces unique document IDs to prevent training issues.

*Example*:

```python
annotation2training.generateConll(training_df_json, "main.conll")
```


- **Label whitelisting & blacklisting (convertJson2NerDF)**

Adds white_list and black_list parameters so you can explicitly include or exclude specific entity labels when converting JSON annotations to a NER DataFrame. 

*Example*:

```python
JSON_PATH = "/content/result.json"

from sparknlp_jsl.training import Annotation2Training
annotation2training = Annotation2Training(spark)
training_df_json = annotation2training.convertJson2NerDF(
    json_path = JSON_PATH,                   # Path to the input JSON file.
    pipeline_model = base_pipeline_model,    # A pre-trained Spark NLP PipelineModel that includes at least a DocumentAssembler, and Tokenizer.
    repartition = (os.cpu_count() * 4),      # Number of partitions to use when creating the DataFrame (default is 32).
    token_output_col = "token",              # The name of the column containing token annotations (default is "token").
    ner_label_col = "label",                  # The name of the output column for NER labels (default is "label").
    black_list = ["Quit_Attempts"],
    replace_labels = {"Smoking_Type":"Smoking_Status"})
```

- **Label distribution explorer (showLabelDistributions)**

A utility method to quickly display the frequency distribution of entity labels in the training DataFrame. It explodes the label column and prints counts per label, helping you spot class imbalance, missing labels, or noisy annotations before training.


*Example*:

```python
annotation2training.showLabelDistributions(training_df_json, "label")
```


Please check [Generative AI to Ner Training](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.7.Generative_AI_to_Ner_Training.ipynb) notebook for more detail


</div><div class="h3-box" markdown="1">

####  Clinical Document Analysis with One-Liner Pretrained-Pipelines for Specific Clinical Tasks and Concepts

We introduce a suite of advanced, hybrid pretrained pipelines, specifically designed to streamline the clinical document analysis process. These pipelines are built upon multiple state-of-the-art (SOTA) pretrained models, delivering a comprehensive solution for quickly extracting vital information.

What sets this release apart is the elimination of complexities typically involved in building and chaining models. Users no longer need to navigate the intricacies of constructing intricate pipelines from scratch or the uncertainty of selecting the most effective model combinations. Our new pretrained pipelines simplify these processes, offering a seamless, user-friendly experience.


{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`pp_docwise_benchmark_large_preann`](https://nlp.johnsnowlabs.com/2025/11/14/pp_docwise_benchmark_large_preann_en.html) |  Detect PHI entities in medical texts using Named Entity Recognition (NER). |
| [`pp_docwise_benchmark_medium_preann`](https://nlp.johnsnowlabs.com/2025/11/14/pp_docwise_benchmark_medium_preann_en.html) |  Detect PHI entities in medical texts using Named Entity Recognition (NER). |
| [`clinical_deidentification_sentwise_benchmark_large`](https://nlp.johnsnowlabs.com/2025/11/05/clinical_deidentification_sentwise_benchmark_large_en.html) |  Deidentify PHI information from medical texts. |
| [`clinical_deidentification_sentwise_benchmark_medium`](https://nlp.johnsnowlabs.com/2025/11/05/clinical_deidentification_sentwise_benchmark_medium_en.html) |  Deidentify PHI information from medical texts. |



*Example*:

```python
from johnsnowlabs import nlp, medical

ner_docwise = nlp.PretrainedPipeline("ner_docwise_benchmark_large_preann", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 ."""
```

*Result*:

{:.table-model-big}
|chunk               |begin|end|ner_label|
|--------------------|-----|---|---------|
|John Lee            |4    |11 |DOCTOR   |
|Royal Medical Clinic|19   |38 |HOSPITAL |
|Chicago             |43   |49 |CITY     |
|11/05/2024          |79   |88 |DATE     |
|56467890            |130  |137|IDNUM    |
|Emma Wilson         |153  |163|PATIENT  |
|50 years old        |169  |180|AGE      |
|444-456-7890        |203  |214|PHONE    |




</div><div class="h3-box" markdown="1">

#### Introducing a new city TextMatcher model for extracting city names from clinical text

A new TextMatcherInternal model from John Snow Labs automatically extracts city names from clinical text, enabling structured geo-location information for downstream analytics and reporting.


*Example*:

```python
text_matcher = TextMatcherInternalModel.pretrained("city_matcher","en","clinical/models") \
    .setInputCols(["sentence", "token"])\
    .setOutputCol("city_name")\
    .setMergeOverlapping(True)

data = spark.createDataFrame([["""Name: Johnson, Alice, Record date: 2093-03-22, MR: 846275.
Dr. Emily Brown, IP 192.168.1.1.
She is a 55-year-old female who was admitted to the Global Hospital in Los Angeles for hip replacement on 03/22/93.
Patient's VIN: 2HGFA165X8H123456, SSN: 444-55-8888, Driver's license no: C789012D.
Phone: (212) 555-7890, 4321 Oak Street, New York City, USA, E-MAIL: alice.johnson@example.com.
Patient has traveled to Tokyo, Paris, and Sydney in the past year."""]]).toDF("text")
```


*Result*:

{:.table-model-big}
|        chunk|begin|end|label|
|-------------|-----|---|-----|
|  Los Angeles|  163|173| CITY|
|New York City|  331|343| CITY|
|        Tokyo|  410|414| CITY|
|        Paris|  417|421| CITY|
|       Sydney|  428|433| CITY|



</div><div class="h3-box" markdown="1">

#### New blog post to understand how to deploy Medical LLMs on Databricks

- [Deploying John Snow Labs Medical LLMs on Databricks: Three Flexible Deployment Options](https://medium.com/john-snow-labs/deploying-john-snow-labs-medical-llms-on-databricks-three-flexible-deployment-options-6005e7129b42) This blog post explores how to securely and efficiently deploy healthcare-focused Large Language Models (LLMs) and Vision Language Models (VLMs) on Databricks. It introduces three flexible deployment options developed in collaboration with Databricks, each balancing performance, cost, and operational control while meeting strict healthcare security and compliance requirements. The post walks through these options using a real customer scenario, illustrating how to run state-of-the-art medical LLMs on Databricks infrastructure and helping teams choose the setup that best fits their clinical workflows and IT constraints.



</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For making Healthcare NLP Easier To Navigate And Understand

- New Databricks [Generative AI to Ner Training](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/databricks/python/tutorials/healthcare_tutorials/1.1.Generative_AI_to_Ner_Training.ipynb) Notebook
- Updated [Generative AI to Ner Training](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.7.Generative_AI_to_Ner_Training.ipynb) Notebook


</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.


+ `pp_docwise_benchmark_large_preann`
+ `pp_docwise_benchmark_medium_preann`
+ `clinical_deidentification_sentwise_benchmark_large`
+ `clinical_deidentification_sentwise_benchmark_medium`
+ `city_matcher`            



</div><div class="h3-box" markdown="1">

For all Healthcare NLP models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">


## Previous versions

</div>
{%- include docs-healthcare-pagination.html -%}
