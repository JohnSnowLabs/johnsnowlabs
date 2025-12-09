---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Healthcare NLP v6.2.0 Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/release_notes_6_2_0
key: docs-licensed-release-notes
modify_date: 2025-10-31
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 6.2.0

#### Highlights

We are delighted to announce a release of **Healthcare NLP 6.2.0**, introducing production-ready deployment of state-of-the-art medical Large Language Models (LLMs) and Vision Language Models (VLMs) on Databricks infrastructure. This release introduces **the first containerized LLM solution for Databricks Container Services, as well as 3 new or updated clinical pre-trained models and pipeline**. We aim to bring enterprise-grade, medical-specific AI to healthcare organizations, with three flexible deployment options with industry-leading accuracy that outperforms GPT-4, Claude, and Gemini on healthcare benchmarks.

+ Support for GGUF based John Snow Labs LLMs/ VLMs on Databricks environment
+ Containerized LLM solutions for Databricks Container Services and other platforms
+ A new inflammatory bowel disease (IBD) classification model
+ Introducing a new model for ICD10CM coding
+ Updated certification training and Databricks tutorial notebooks for Healthcare NLP
+ New blog posts on various topics
+ Various core improvements; bug fixes, enhanced overall robustness and reliability of Spark NLP for Healthcare
+ Updated notebooks and demonstrations for making Spark NLP for Healthcare easier to navigate and understand
+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

These enhancements will elevate your experience with Spark NLP for Healthcare, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.


</div><div class="h3-box" markdown="1">

#### LLM/ VLM Benchmarks

+ 83.5% accuracy on OpenMed clinical benchmarks (vs. 71-77% for open-source alternatives)
+ 88% higher physician preference on clinical summarization compared to GPT-4o
+ 79.83% on MedHELM evaluation (+4.7 to +6.0 points ahead of GPT-5, Gemini 2.5 Pro, and Claude Sonnet 4)
+ 92% accuracy on handwritten medical documents with Vision Language Models
+ Zero data leaving your environment with HIPAA, GDPR, SOC 2, and HITRUST compliance

</div><div class="h3-box" markdown="1">

####  Support for John Snow Labs' LLMs/VLMs on Databricks 

John Snow Labs’ LLMs/VLMs now support seamless integration with Databricks, enabling efficient deployment and use of lightweight large language models (LLMs) in gguf format. These modules are designed to facilitate interaction with LLMs that have been converted into the gguf format—optimized for performance and resource efficiency. They make it possible to use John Snow Labs’ licensed, domain-specific models directly within the Databricks environment.

Features:
- Model Flexibility: Supports various model sizes tailored to medical and healthcare-related tasks.
- Comprehensive API: Provides methods for setting parameters, loading models, generating text outputs, and retrieving metadata.
- Simplifies the deployment of specialized LLMs on Databricks.
- Enables efficient inference with smaller model footprints.
- Ensures compliance with John Snow Labs’ licensing for secure enterprise use.

please see the example [AutoGGUFModel](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/databricks/python/healthcare-nlp/30.0.MedicalLLM.ipynb) and  [Multi_Modal_LLMs](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/databricks/python/healthcare-nlp/30.1.Multi_Modal_LLMs.ipynb) notebooks

</div><div class="h3-box" markdown="1">

####  John Snow Labs Containerized LLM/VLM Solutions for Databricks Container Services and Other Platforms

We provide containerized Large Language Model (LLM) solutions that can be seamlessly deployed in Databricks or any other environment supporting Docker. These solutions enable users to run JSL’s healthcare-specific LLMs locally within containerized clusters—without relying on external APIs.

By configuring a Databricks cluster with the provided Docker image and license environment variables, users can immediately access and run models such as text-only, vision, and reasoning variants. Each model is pre-packaged and ready for inference directly within the container, ensuring performance, security, and data privacy.

This setup allows healthcare and enterprise users to easily load, execute, and scale LLM workloads in isolated and compliant environments, making it ideal for production-grade deployments across various infrastructure setups.

- 1. Configure the cluster

    In databricks, go to cluster configuration and add the image name and tag. Also need to add the environment variables with the following:
    
    - Go to Compute -> Configuration -> Advenced -> Spark -> Environment variables, and set your license variable
    ```
    SPARK_NLP_LICENSE=eyXXXX......
    ```
    
    - Go to Compute -> Configuration -> Advenced -> Docker
    ```
    Docker Image URL: docker.io/johnsnowlabs/dockerized-applications-healthcare:dbr-llm-test-201
    Authentication: Username and password
    UserName: <docker hub user name>
    Password: <docker hub user password>
    ```

    - Run the notebook using this cluster. Add the following in the first cell of the notebook
    
    ```python
    # this section only needs for onDataBricks 
    import sys
    import runpy
    sys.path.extend(["/", "/usr/local/lib/python3.10/site-packages"])
    runpy.run_path("/usr/local/lib/python3.10/site-packages/sitecustomize.py")
    ```

- 2. Model List

    |model_name             | model_type | test      |
    |-----------------------|------------|-----------|
    | jsl_meds_4b           | text only  | available |
    | jsl_meds_8b           | text only  | available |
    | jsl_medm_14b          | text only  | available |
    | jsl_meds_vl_3b        | vision     | available |
    | jsl_meds_vl_7b        | vision     | available |
    | jsl_meds_vl_4b        | vision     | will be available |
    | jsl_meds_vl_8b        | vision     | will be available |
    | jsl_medm_vl_30b       | vision     | available |
    | jsl_meds_reasoning_8b | reasoning  | available |
    | jsl_medm_reasoning_32b| reasoning  | available |


- Text Only Models

```python
from jsl_llm_lib.jsl_llm import JslLlm
llm = JslLlm()
llm.load_model(llm_name="jsl_meds_4b")

text = """.."""

prompt = f"""
"""

result = llm.get_prediction(prompt=prompt)
print("Result:",f"{result}")
```


- Reasoning Models

```python
from jsl_llm_lib.jsl_llm import JslLlm
llm = JslLlm()
llm.load_model(llm_name="jsl_meds_reasoning_8b")

text = """.."""

prompt = f"""
"""

result = llm.get_prediction(prompt=prompt, thinking=True)
print("Result:",f"{result}")
```


- Vision Models

```python
from jsl_llm_lib.jsl_llm import JslLlm
llm = JslLlm()
llm.load_model(llm_name="jsl_meds_vl_3b")

images_dir = "images"
os.makedirs(images_dir, exist_ok=True)
os.system(f"wget -O {images_dir}/prescription.png  -q \"https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/healthcare-nlp/data/ocr/prescription_02.png\"")

image_path = os.path.join(images_dir, "prescription.png")

prompt = """Extract demographic, clinical disease and medication informations"""

result = llm.get_prediction(prompt=prompt, image_path=image_path)
```

Please check the [gitbub](https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/products) for more information



</div><div class="h3-box" markdown="1">

#### New Inflammatory Bowel Disease (IBD) Classification Model

John Snow Labs introduces a new Inflammatory Bowel Disease (IBD) Classification Model designed to accurately distinguish between clinical documents that reference IBD and those that do not. 
The model classifies input text into two categories:
- IBD: Documents containing evidence or discussion related to Inflammatory Bowel Disease.
- Not IBD: Documents without any suggestive indications of IBD.

Built on a pretrained BERT architecture, this model leverages sequence classification techniques to identify IBD-related patterns in clinical narratives efficiently.
The model [`bert_sequence_classifier_ibd_onnx`](https://nlp.johnsnowlabs.com/2025/10/21/bert_sequence_classifier_ibd_onnx_en.html) is optimized for use with the compatible embeddings [`distil_ibd_bert_onnx`](https://nlp.johnsnowlabs.com/2025/10/21/distil_ibd_bert_onnx_en.html), ensuring high performance and efficiency in clinical text classification workflows.


*Example*:

```python
bfsc_loaded = BertForSequenceClassification.pretrained("bert_sequence_classifier_ibd_onnx", "en", "clinical/models") \
    .setInputCols(['document', 'token']) \
    .setOutputCol("label")

data = spark.createDataFrame([
    ["Patient with inflammatory bowel disease and colon inflammation."],
    ["Normal colonoscopy findings, no evidence of inflammation."],
]).toDF("text")

data = spark.createDataFrame([
    ["A 30-year-old man presents with chronic abdominal pain, fatigue, and intermittent diarrhea lasting several months. He reports 3–4 loose stools per day, often with postprandial cramping. Colonoscopy shows patchy ulceration and cobblestoning in the terminal ileum, while biopsies confirm chronic granulomatous inflammation. Labs reveal mild iron-deficiency anemia and elevated CRP. He is started on azathioprine and mesalamine, and receives dietary counseling on low-residue and high-protein intake."],
    ["A 49-year-old female presents with chronic constipation over several years. Colonoscopy is normal. Thyroid function, CRP, and electrolytes are within normal limits. She is diagnosed with chronic idiopathic constipation and started on polyethylene glycol and dietary fiber. No evidence of mucosal inflammation or IBD."],
]).toDF("text")
```

*Result for short text*:

{:.table-model-big}
|text                                                           |result   |
|---------------------------------------------------------------|---------|
|Patient with inflammatory bowel disease and colon inflammation.|[IBD]    |
|Normal colonoscopy findings, no evidence of inflammation.      |[Not IBD]|



*Result for long text*:

{:.table-model-big}
|text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |result   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
|A 30-year-old man presents with chronic abdominal pain, fatigue, and intermittent diarrhea lasting several months. He reports 3–4 loose stools per day, often with postprandial cramping. Colonoscopy shows patchy ulceration and cobblestoning in the terminal ileum, while biopsies confirm chronic granulomatous inflammation. Labs reveal mild iron-deficiency anemia and elevated CRP. He is started on azathioprine and mesalamine, and receives dietary counseling on low-residue and high-protein intake.|[Not IBD]|
|A 49-year-old female presents with chronic constipation over several years. Colonoscopy is normal. Thyroid function, CRP, and electrolytes are within normal limits. She is diagnosed with chronic idiopathic constipation and started on polyethylene glycol and dietary fiber. No evidence of mucosal inflammation or IBD.                                                                                                                                                                                     |[Not IBD]|


**Advanced IBD Classification**

```python
labels = ["inflammatory_bowel_diseases", "Crohn's_disease", "Ulcerative_colitis", "Indeterminate_colitis", "Irritable_Bowel_Syndrome", "other_disease"]

pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_generic_large", "en", "clinical/models")\
      .setInputCols("sentence", "token")\
      .setOutputCol("ner")\
      .setPredictionThreshold(0.5)\
      .setLabels(labels)

...
assertion_classifier = BertForAssertionClassification.pretrained("assertion_bert_classification_clinical", "en", "clinical/models")\
      .setInputCols(["sentence", "ner_chunk"])\
      .setOutputCol("assertion_class")


data = spark.createDataFrame([
    ["A 30-year-old man presents with chronic abdominal pain, fatigue, and intermittent diarrhea lasting several months. He reports 3–4 loose stools per day, often with postprandial cramping. Colonoscopy shows patchy ulceration and cobblestoning in the terminal ileum, while biopsies confirm chronic granulomatous inflammation. Labs reveal mild iron-deficiency anemia and elevated CRP. He is started on azathioprine and mesalamine, and receives dietary counseling on low-residue and high-protein intake."],
    ["A 49-year-old female presents with chronic constipation over several years. Colonoscopy is normal. Thyroid function, CRP, and electrolytes are within normal limits. She is diagnosed with chronic idiopathic constipation and started on polyethylene glycol and dietary fiber. No evidence of mucosal inflammation or IBD."],
]).toDF("text")
```


*Result:*

{:.table-model-big}
| doc_id | text           | ner_chunk | ner_label | assertion_result |
|--------|----------------|-----------|-----------|------------------|
| 1 | A 30-year-old man presents with chronic abdominal pain, fatigue, and intermittent diarrhea lasting several months. He reports 3–4 loose stools per day, often with postprandial cramping. Colonoscopy shows patchy ulceration and cobblestoning in the terminal ileum, while biopsies confirm chronic granulomatous inflammation. Labs reveal mild iron-deficiency anemia and elevated CRP. He is started on azathioprine and mesalamine, and receives dietary counseling on low-residue and high-protein intake. | chronic granulomatous inflammation | inflammatory_bowel_diseases | present |
| 2 | A 49-year-old female presents with chronic constipation over several years. Colonoscopy is normal. Thyroid function, CRP, and electrolytes are within normal limits. She is diagnosed with chronic idiopathic constipation and started on polyethylene glycol and dietary fiber. No evidence of mucosal inflammation or IBD. | IBD | inflammatory_bowel_diseases | absent |


JSL provides powerful annotators like NER, Assertion Classification, and DocumentFiltererByNER that enable more detailed and advanced clinical text processing workflows.
This advanced pipeline enables precise IBD document classification with entity-level granularity and assertion status.


</div><div class="h3-box" markdown="1">

####  Introducing a New TextMatcher Model for ICD10CM Coding

A new TextMatcher model from John Snow Labs automatically maps clinical text to ICD10CM codes, making medical coding faster and more accurate. It streamlines documentation, reduces manual effort, and improves overall coding efficiency.

*Example*:

```python
text_matcher = TextMatcherInternalModel.pretrained("icd10cm_matcher", "en" ,"clinical/models") \
    .setInputCols(["document", "token"])\
    .setOutputCol("icd10cm")\
    .setMergeOverlapping(True)

data = spark.createDataFrame([["""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, associated with obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection."""]]).toDF("text")
```

*Result:*
|chunk                        |begin|end|ner_label   |
|-----------------------------|-----|---|------------|
|gestational diabetes mellitus|39   |67 |ICD10_ENTITY|
|polyuria                     |261  |268|ICD10_ENTITY|
|polydipsia                   |271  |280|ICD10_ENTITY|
|vomiting                     |302  |309|ICD10_ENTITY|


</div><div class="h3-box" markdown="1">

#### Updated Certification Training and Databricks Tutorial Notebooks for Healthcare NLP

All Certification Training and Databricks Tutorial notebooks for John Snow Labs Healthcare NLP have been updated with the latest enhancements, ensuring better usability, performance, and compatibility with the latest Spark NLP releases. These updates aim to provide a smoother learning experience and more efficient model deployment within healthcare AI and NLP pipelines.

Please see the [Healthcare NLP Workshop](https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/healthcare-nlp) and [Databricks Tutorials](https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/databricks/python/healthcare-nlp) folders



</div><div class="h3-box" markdown="1">

#### New Blog Posts on Various Topics

Explore our latest John Snow Labs blog posts, highlighting new advancements in Healthcare NLP and real-world applications that enhance clinical insights and patient care.

- [John Snow Labs Healthcare NLP 6.1 Launch: Expanding LLM and VLM Capabilities](https://medium.com/john-snow-labs/john-snow-labs-healthcare-nlp-6-1-launch-expanding-llm-and-vlm-capabilities-899a4ca8818d) Discover how the latest release combines domain-specific NLP with Large Language Models (LLMs) and Vision Language Models (VLMs) to revolutionize healthcare AI and improve patient outcomes.
- [Automated Vaccine Registries: From Unstructured Notes to Structured Insights](https://medium.com/john-snow-labs/automated-vaccine-registries-from-unstructured-notes-to-structured-insights-d3789b485975) Learn how NLP models can automatically extract vaccine types, infectious diseases, and related symptoms from unstructured clinical text—turning free-text notes into actionable data for public health and research.


</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.

+ `bert_sequence_classifier_ibd_onnx`
+ `distil_ibd_bert_onnx`
+ `icd10cm_matcher`         


</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">

## Versions

</div>
{%- include docs-healthcare-pagination.html -%}
