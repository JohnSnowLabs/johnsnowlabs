---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Spark NLP for Healthcare Release Notes 5.1.4
permalink: /docs/en/spark_nlp_healthcare_versions/release_notes_5_1_4
key: docs-licensed-release-notes
modify_date: 2023-12-01
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 5.1.4

#### Highlights

We are delighted to announce a suite of remarkable enhancements and updates in our latest release of Spark NLP for Healthcare. **This release comes with the advanced Document Splitter annotator specifically designed for medical context and more flexibility in Deidentification as well as robust exception handling in `MedicalNerModel` for corrupted inputs**. 

+ Introducing the Advanced `Medical Document Splitter` annotator with more flexibility and customization for RAG pipelines
+ Enhancing `ChunkFiltererApproach` by introducing json-based entity confidence configuration
+ Advanced data privacy with `DeIdentification` unleashing custom regex patterns 
+ Robust exception handling in `MedicalNerModel` for corrupted inputs 
+ Various core improvements; bug fixes, enhanced overall robustness and reliability of Spark NLP for Healthcare
  - Enhanced the `ChunkSentenceSplitter` annotator and revised documentation
  - Updated the `training_log_parser` and its utility script to align with the latest NumPy version
  - Transitioned the SecureRandom algorithm from Spark configuration to the system environment. Please check the previous [Random Seed Algorithm](https://nlp.johnsnowlabs.com/docs/en/spark_nlp_healthcare_versions/release_notes_5_1_3) implementation for details.
  - Revised some imports for improved functionality in Deidentification
+ New and updated demos
  - New [Drug Resolver Demo](https://demo.johnsnowlabs.com/healthcare/ER_DRUG/)
  - Updated [Multi Language Clinical NER Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/) 
  - New [Medical Document Splitter Notebook]()
  - Updated [Clinical Named Entity Recognition Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb) with `setDoExceptionHandling` information
  - Updated [Clinical DeIdentification Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.Clinical_DeIdentification.ipynb) with `setRegexPatternsDictionaryAsJsonString` and `setCombineRegexPatterns` examples
  - Updated [Calculate Medicare Risk Adjustment Score Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.1.Calculate_Medicare_Risk_Adjustment_Score.ipynb) with the latest improvement

These enhancements will elevate your experience with Spark NLP for Healthcare, enabling more efficient, accurate, and streamlined healthcare-related natural language data analysis.




</div><div class="h3-box" markdown="1">
  
####  Introducing the Advanced `Medical Document Splitter` Annotator with More Flexibility and Customization for RAG Pipelines

Discover our cutting-edge Internal Document Splitter—an innovative annotator designed to effortlessly break down extensive documents into manageable segments. Empowering users with the ability to define custom separators, this tool seamlessly divides texts, ensuring each chunk adheres to specified length criteria.

InternalDocumentSplitter has a setSplitMode method to decide how to split documents. Default: 'regex'. It should be one of the following values:
- `char`: Split text based on individual characters.
- `token`: Split text based on tokens. You should supply tokens from inputCols.
- `sentence`: Split text based on sentences. You should supply sentences from inputCols.
- `recursive`: Split text recursively using a specific algorithm.
- `regex`: Split text based on a regular expression pattern.

*Example*:

```python
document_splitter = InternalDocumentSplitter()\
    .setInputCols("document")\
    .setOutputCol("splits")\
    .setSplitMode("recursive")\
    .setChunkSize(100)\
    .setChunkOverlap(3)\
    .setExplodeSplits(True)\
    .setPatternsAreRegex(False)\
    .setSplitPatterns(["\n\n", "\n", " "])\
    .setKeepSeparators(False)\
    .setTrimWhitespace(True)

text = [( 
    "The patient is a 28-year-old, who is status post gastric bypass surgery"
    " nearly one year ago. \nHe has lost about 200 pounds and was otherwise doing well"
    " until yesterday evening around 7:00-8:00 when he developed nausea and right upper quadrant pain," 
    " which apparently wrapped around toward his right side and back. He feels like he was on it"
    " but has not done so. He has overall malaise and a low-grade temperature of 100.3." 
    " \n\nHe denies any prior similar or lesser symptoms. His last normal bowel movement was yesterday." 
    " He denies any outright chills or blood per rectum." 
)]
```

*Result*:

|sentence                                          |doc_id|
|--------------------------------------------------|------|
|The patient is a 28-year-old, who is status post gastric bypass surgery nearly one year ago.       |0     |
|He has lost about 200 pounds and was otherwise doing well until yesterday evening around 7:00-8:00 |1     |
|when he developed nausea and right upper quadrant pain, which apparently wrapped around toward his |2     |
|his right side and back. He feels like he was on it but has not done so. He has overall malaise and|3     |
|and a low-grade temperature of 100.3.                                                              |4     |
|He denies any prior similar or lesser symptoms. His last normal bowel movement was yesterday. He   |5     |
|He denies any outright chills or blood per rectum.                                                 |6     |

Please check [InternalDocumentSplitter Notebook]() for more information





</div><div class="h3-box" markdown="1">
  
#### Enhancing `ChunkFiltererApproach` by Introducing JSON-Based Entity Confidence Configuration

The new `setEntitiesConfidenceResourceAsJsonString` method allows users to finely tune entity confidence levels using a JSON configuration.

*Example*:

```python
chunk_filterer = ChunkFiltererApproach()\
    .setInputCols("sentence","ner_chunk")\
    .setOutputCol("chunk_filtered")\
    .setFilterEntity("entity")\
    .setEntitiesConfidenceResourceAsJsonString("""{'DURATION':'0.9',
                                                  'DOSAGE':'0.9',
                                                  'FREQUENCY':'0.9',
                                                  'STRENGTH':'0.9',
                                                  'DRUG':'0.9'}""")

text ='The patient was prescribed 1 capsule of Advil for 5 days . He was seen by the endocrinology service and she was discharged on 40 units of insulin glargine at night , 12 units of insulin lispro with meals , metformin 1000 mg two times a day . It was determined that all SGLT2 inhibitors should be discontinued indefinitely fro 3 months .'
```

*Without Filtering Results*:

| chunks                       | begin | end | sentence_id | entities  |confidence |
|:-----------------------------|------:|----:|------------:|:----------|--------:|
| 1 capsule of Advil           |    27 |  44 |           0 | DRUG      |    0.64 |
| for 5 days                   |    46 |  55 |           0 | DURATION  |    0.55 |
| 40 units of insulin glargine |   126 | 153 |           1 | DRUG      |    0.62 |
| at night                     |   155 | 162 |           1 | FREQUENCY |    0.74 |
| 12 units of insulin lispro   |   166 | 191 |           1 | DRUG      |    0.67 |
| with meals                   |   193 | 202 |           1 | FREQUENCY |    0.72 |
| metformin 1000 mg            |   206 | 222 |           1 | DRUG      |    0.70 |
| two times a day              |   224 | 238 |           1 | FREQUENCY |    0.67 |
| SGLT2 inhibitors             |   269 | 284 |           2 | DRUG      |    0.89 |

*Filtered Results*:

| chunks           | begin | end | sentence_id | entities  | confidence |
|:-----------------|------:|----:|------------:|:----------|-----------:|
| at night         |   155 | 162 |           1 | FREQUENCY |    0.74 |
| with meals       |   193 | 202 |           1 | FREQUENCY |    0.72 |
| SGLT2 inhibitors |   269 | 284 |           2 | DRUG      |    0.89 |





</div><div class="h3-box" markdown="1">

#### Advanced Data Privacy with DeIdentification Unleashing Regex Patterns Unleashed

The latest update in the DeIdentification library brings advanced data privacy with the introduction of the setRegexPatternsDictionaryAsJsonString method. This powerful feature empowers users to create custom regular expression patterns for masking specific protected entities. 

*Example*:

```python
deid = DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"]) \
    .setOutputCol("deidentified") \
    .setMode("mask") \
    .setRegexPatternsDictionaryAsJsonString("{'NUMBER':'\d+'},"+
                                            "{'NUMBER':'(\d+.?\d+.?\d+)'}")\
    .setRegexOverride(True) # Prioritizing regex rules

text ='''
Record date : 2093-01-13 , David Hale , M.D . , Name : Hendrickson Ora , MR # 7194334 Date : 01/13/93 . PCP : Oliveira , 25 years-old , Record date : 2079-11-09 . Cocke County Baptist Hospital , Keats Street , ZIP 45662, Phone 55-555-5555 .
'''
```

*Without RegexOverride Results (default regex)*:

```bash
[Record date : <DATE> , David Hale , M.D ., , Name : Hendrickson Ora ,  Date : <DATE> ., PCP : Oliveira , 25 years-old , Record date : <DATE> ., Cocke County Baptist Hospital , Keats Street , ZIP 45662, Phone <PHONE> .]
```
 
*With RegexOverride Results (custom regex)*:

```bash
[Record date : <NUMBER> , David Hale , M.D ., , Name : Hendrickson Ora ,  Date : <NUMBER> ., PCP : Oliveira , <NUMBER> years-old , Record date : <NUMBER> ., Cocke County Baptist Hospital , Keats Street , ZIP <NUMBER>, Phone <NUMBER> .]
```

- Merging default regex rules and custom user-defined regex with `setCombineRegexPatterns`

*Example*:

```python
deid = DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"]) \
    .setOutputCol("deidentified") \
    .setMode("mask") \
    .setCombineRegexPatterns(True)\
    .setRegexPatternsDictionary("./custom_regex.txt")
```

Please check: [Clinical DeIdentification Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.Clinical_DeIdentification.ipynb) for more information




</div><div class="h3-box" markdown="1">

####  Robust Exception Handling in `MedicalNerModel` for Corrupted Inputs

Enhance the resilience of your Medical Named Entity Recognition (NER) model with the ExceptionHandling feature. When the `setDoExceptionHandling` is set to true, the model attempts to compute batch-wise as usual. In the event of an exception within a batch, the system switches to row-wise processing. Any exception during row processing results in the emission of an Error Annotation, ensuring that only the problematic rows are lost rather than the entire batch. 

*Example*:

```python
clinical_ner = MedicalNerModel.pretrained("ner_oncology", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")\
    .setDoExceptionHandling(True)
```

Please check: [Clinical Named Entity Recognition Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb) for more information





</div><div class="h3-box" markdown="1">

#### Various Core Improvements: Bug Fixes, Enhanced Overall Robustness, And Reliability Of Spark NLP For Healthcare

- Enhanced the `ChunkSentenceSplitter` annotator and revised documentation
- Updated the `training_log_parser` and its utility script to align with the latest NumPy version
- Transitioned the SecureRandom algorithm from Spark configuration to the system environment. Please check the previous [Random Seed Algorithm](https://nlp.johnsnowlabs.com/docs/en/spark_nlp_healthcare_versions/release_notes_5_1_3) implementation for details.
- Revised some imports for improved functionality in Deidentification

</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For making Spark NLP For Healthcare Easier To Navigate And Understand

- New [Drug Resolver Demo](https://demo.johnsnowlabs.com/healthcare/ER_DRUG/)
- Updated [Multi Language Clinical NER Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/) 
- New [InternalDocumentSplitter Notebook]()
- Updated [Clinical Named Entity Recognition Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb) with `setDoExceptionHandling` information
- Updated [Clinical DeIdentification Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.Clinical_DeIdentification.ipynb) with `setRegexPatternsDictionaryAsJsonString` and `setCombineRegexPatterns` examples
- Updated [Calculate Medicare Risk Adjustment Score Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.1.Calculate_Medicare_Risk_Adjustment_Score.ipynb) with the latest improvement


</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">



## Versions

</div>
{%- include docs-healthcare-pagination.html -%}
