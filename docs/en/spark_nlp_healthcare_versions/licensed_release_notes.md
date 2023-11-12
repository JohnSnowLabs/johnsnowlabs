---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Spark NLP for Healthcare Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/licensed_release_notes
key: docs-licensed-release-notes
modify_date: 2023-11-10
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 5.1.3

#### Highlights

We are delighted to announce a suite of remarkable enhancements and updates in our latest release of Spark NLP for Healthcare. **This release comes with the very first Patient Frailty classification as well as 7 new clinical pretrained models and pipelines**. It is a testament to our commitment to continuously innovate and improve, furnishing you with a more sophisticated and powerful toolkit for healthcare natural language processing.

+ 3 new augmented NER models by leveraging the capabilities of the `LangTest` library to boost their robustness significantly
+ New clinical NER models for extracting clinical entities in the Hebrew language
+ New Social Determinants of Healthcare (SDoH) model for patient frailty classification
+ New rule-based `ContextualParserModel` designed to identify date-of-death (DOD) entities with contextual awareness
+ `RelationExtractionModel` has undergone significant optimization, resulting in a substantial improvement in inference speed
+ OCR Deidentification Module now supports the deidentification of handwritten or printed text
+ Introducing a customizable random seed algorithm in Spark for enhanced data privacy
+ Various core improvements; bug fixes, enhanced overall robustness and reliability of SparkNLP for Healthcare
    - Some minor naming changes have been made in Deidentification
    - Added new unnormalized date formats into the date faker list in Deidentification annotator
    - Default `locale` operating system language set as English when starting the session
    - License validation process has been fastened now
    - Fixed the issues in ALAB Module; `get_conll_data` "missing sentence detector" failure and `get_assertion_data` method for getting more annotations from annotated JSON file
+ New and updated demos
  - New [Social Determinant of Health Text Classification Demo](https://demo.johnsnowlabs.com/healthcare/SOCIAL_DETERMINANT_SEQUENCE_CLASSIFICATION/) with new `bert_sequence_classifier_sdoh_frailty_en` model
  - Updated [Multi Language Clinical NER Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/) with Finnish (`ner_clinical_fi`) model
  - Updated [Contextual Parser Rule Based NER Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.2.Contextual_Parser_Rule_Based_NER.ipynb) with the example of `date_of_death_parser` model
  - Updated [Clinical Relation Extraction Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/10.Clinical_Relation_Extraction.ipynb) with Filtering Entity Types examples
  - Updated [Spark OCR Utility Module Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/5.3.Spark_OCR_Utility_Module.ipynb#scrollTo=6Eh0uX-ZZLVj) with `text_type` param introduced and examples

These enhancements will elevate your experience with Spark NLP for Healthcare, enabling more efficient, accurate, and streamlined healthcare-related natural language data analysis.

</div><div class="h3-box" markdown="1">



#### 3 New Augmented NER Models by Leveraging the Capabilities of the LangTest Library to Boost Their Robustness Significantly

Newly introduced 3 augmented NER models that are powered by the innovative `LangTest` library. This cutting-edge NLP toolkit is at the forefront of language processing advancements, incorporating state-of-the-art techniques and algorithms to enhance the capabilities of our models significantly.

| Model Name               |   Predicted Entities        |
|--------------------------|-----------------------------|
| [`ner_human_phenotype_gene_clinical_langtest`](https://nlp.johnsnowlabs.com/2023/11/04/ner_human_phenotype_gene_clinical_langtest_en.html)  | `GENE`, `HP` |
| [`ner_human_phenotype_go_clinical_langtest`](https://nlp.johnsnowlabs.com/2023/11/04/ner_human_phenotype_go_clinical_langtest_en.html)      | `GO`, `HP` |
| [`ner_risk_factors_langtest`](https://nlp.johnsnowlabs.com/2023/11/06/ner_risk_factors_langtest_en.html)      | `CAD`, `DIABETES`, `FAMILY_HIST`, `HYPERLIPIDEMIA`, `HYPERTENSION`, `MEDICATION`, `OBESE`, `PHI`, `SMOKER` |

- The table below shows the robustness of overall test results for these models.

| model names        | original robustness  |  new robustness  |
|-------------------------------------------|---------|--------|
| ner_human_phenotype_gene_clinical_langtest| 48.79%  | 82.60% |
| ner_human_phenotype_go_clinical_langtest  | 43.48%  | 85.57% |
| ner_risk_factors_langtest                 | 89.69%  | 93.75% |



</div><div class="h3-box" markdown="1">

#### New Clinical Named Entity Recognition (NER) Models for Extracting Clinical Entities in the Hebrew Language

We have a new clinical NER model specifically designed for the Hebrew language. This model excels at identifying clinical entities, enabling the automation of critical clinical data extraction. It proves invaluable for various healthcare-related tasks, such as research, medical record documentation, and other applications within the Hebrew-speaking healthcare sector.


| Model Name                                                                   | Predicted Entities           | Language |
|------------------------------------------------------------------------------|------------------------------|----------|
| [ner_clinical](https://nlp.johnsnowlabs.com/2023/10/23/ner_clinical_he.html) | `PROBLEM` `TEST` `TREATMENT` |  he      |


</div><div class="h3-box" markdown="1">


####  New Social Determinants of Healthcare (SDoH) Model for Frailty Classification

Introducing a new frailty classification model trained on a diverse dataset and it provides accurate label assignments and confidence scores for its predictions. The primary goal of this model is to categorize text into two key labels: `Frail` and `Non_Frail`.


*Example*:

```python
sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_sdoh_frailty", "en", "clinical/models")\
    .setInputCols(["document", "token"])\
    .setOutputCol("prediction")

sample_texts=[  
  "Patient demonstrates a marked decrease in muscle strength and endurance, requiring assistance for basic activities.",
  "Clinical evaluation indicates robust health with no signs of physical debilitation.",
  "Noted significant weight loss and diminished muscle mass over the past several months.",
  "Follow-up examinations show complete remission of previous oncological concerns.",
  "The patient exhibits increased susceptibility to skin tears and bruising with minimal contact.",
  "Laboratory results reveal the patient's complete recovery from hepatitis, with normal liver function tests."
]

```

*Result*:

|                                                                                          text      | result    |
|----------------------------------------------------------------------------------------------------|-----------|
|Patient demonstrates a marked decrease in muscle strength and endurance, requiring assistance for...| Frail     |
|Clinical evaluation indicates robust health with no signs of physical debilitation.                 | Non_Frail |
|Noted significant weight loss and diminished muscle mass over the past several months.              | Frail     |
|Follow-up examinations show complete remission of previous oncological concerns.                    | Non_Frail |
|The patient exhibits increased susceptibility to skin tears and bruising with minimal contact.      | Frail     |
|Laboratory results reveal the patient's complete recovery from hepatitis, with normal liver funct...| Non_Frail |


Please check [Social Determinant Sequence Classification Demo](https://demo.johnsnowlabs.com/healthcare/SOCIAL_DETERMINANT_SEQUENCE_CLASSIFICATION/)

</div><div class="h3-box" markdown="1">


#### New Rule-Based `ContextualParserModel` Designed to Identify Date-Of-Death (DOD) Entities With Contextual Awareness

We are releasing a new `ContextualParserModel` that can extract date-of-death (DOD) entities in clinical texts.

*Example*:

```python
dod_contextual_parser = ContextualParserModel.pretrained("date_of_death_parser", "en", "clinical/models") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("chunk_dod")

sample_text = """
Record date : 2081-01-04
DB : 11.04.1962
DT : 12-03-1978
DOD : 10.25.23

SOCIAL HISTORY:
Jane Doe was born on November 4, 1962, in London, and she got married on April 5, 1979.
When she got pregnant on May 15, 1979, the doctor wanted to verify her date of birth, which was confirmed to be November 4, 1962.
Jane was 45 years old when she sadly passed away on September 25, 2007.

PROCEDURES:
Patient Jane Doe was evaluated on March 15, 1988, for allergies. She was seen by the endocrinology service and was discharged on September 23, 1988.

MEDICATIONS:
1. Coumadin 1 mg daily. Jane's last INR was measured on August 14, 2007, and it was 2.3."""
```

*Result*:

|sentence_id|chunk             |begin|end|ner_label|
|-----------|------------------|-----|---|---------|
|3          |10.25.23          |64   |71 |DOD      |
|5          |September 25, 2007|360  |377|DOD      |



Please check [Model Card](https://nlp.johnsnowlabs.com/2023/11/05/date_of_death_parser_en.html) and [Contextual Parser Rule Based NER Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.2.Contextual_Parser_Rule_Based_NER.ipynb) for more information.




</div><div class="h3-box" markdown="1">

#### `RelationExtractionModel` Has Undergone Significant Optimization, Resulting In A Substantial Improvement In Inference Speed

Through meticulous optimization efforts, we have significantly improved the `RelationExtractionModel` annotator, ensuring a notably expedited process for extracting relations between clinical entities. 

</div><div class="h3-box" markdown="1">


#### OCR Deidentification Module Now Supports The Deidentification Of Handwritten Or Printed Text

In this update, a new `text_type` parameter has been introduced for the `ocr_nlp_processor` module, allowing users to choose the type of text to be handled and deidentified, supporting all available styles: `colored_box`, `bounding_box` as well as ``highlight``. The available `text_type` values are described as follows:

    - `printed`: just the detected printed entities will be deidentified
    - `handwritten`: just the detected handwritten text will be deidentified
    - `both`: both the detected printed entities and the detected handwritten text will be deidentified

*Example*:

```python
from sparknlp_jsl.utils.ocr_nlp_processor import ocr_entity_processor

# Bounding Box with a text type parameter
# Handling just handwritten text

path='content/*.pdf'
box = "bounding_box"

ocr_entity_processor(spark=spark,
                    file_path = path,
                    ner_pipeline = nlp_model,
                    chunk_col = "merged_chunk",
                    style = box,
                    save_dir = "bounding_box",
                    label= False,
                    display_result = True,
                    outline_width = 4,
                    outline_color = (42, 170, 138),
                    text_type = "handwritten")    ## Default = "printed"
```

Please check [Spark_OCR_Utility_Module](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/5.3.Spark_OCR_Utility_Module.ipynb) Notebook for more examples

</div><div class="h3-box" markdown="1">

#### Introducing a Customizable Random Seed Algorithm in Spark for Enhanced Data Privacy

In this release, a new configuration parameter has been introduced in Spark NLP for Healthcare - `spark.jsl.settings.seed.numberGenerationAlgorithm`, allowing users to select a `SecureRandom` algorithm for random seed generation. The available algorithms include `SHA1PRNG` when in obfuscation mode, which is used by DeIdentification for generating fake data. Users now have the flexibility to choose the desired generation algorithm, impacting the quality of fake data, system performance, and potential blocking issues.

The alternative Number Generation Algorithms are `NativePRNG`, `NativePRNGBlocking`, `NativePRNGNonBlocking`, `PKCS11`, `SHA1PRNG`, and `Windows-PRNG`, for more information please see [this documentation](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#SecureRandom).



*Example*:

```python
import sparknlp_jsl

params = {"spark.jsl.settings.seed.numberGenerationAlgorithm": "SHA1PRNG"}

spark = sparknlp_jsl.start(license_keys['SECRET'], params=params)
```




</div><div class="h3-box" markdown="1">

#### Various Core Improvements; Bug Fixes, Enhanced Overall Robustness and Reliability of SparkNLP for Healthcare

- Some minor naming changes have been made in Deidentification:  `useShifDays() -> useShiftDays()`
- Added new unnormalized date formats into the date faker list in Deidentification annotator
- Default locale operating system language set as English when starting the session
- License validation process has been fastened now
- Fixed the issues in ALAB Module; `get_conll_data` "missing sentence detector" failure and `get_assertion_data` method for getting more annotations from annotated JSON file



</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For making Spark NLP For Healthcare Easier To Navigate And Understand

- New [Social Determinant of Health Text Classification Demo](https://demo.johnsnowlabs.com/healthcare/SOCIAL_DETERMINANT_SEQUENCE_CLASSIFICATION/) with new `bert_sequence_classifier_sdoh_frailty` model
- Updated [Multi Language Clinical NER Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/) with Finnish (`ner_clinical_fi`) model
- Updated [Contextual Parser Rule Based NER Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.2.Contextual_Parser_Rule_Based_NER.ipynb) with the example of `date_of_death_parser` model
- Updated [Clinical Relation Extraction Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/10.Clinical_Relation_Extraction.ipynb) with Filtering Entity Types examples
- Updated [Spark OCR Utility Module Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/5.3.Spark_OCR_Utility_Module.ipynb#scrollTo=6Eh0uX-ZZLVj) with `text_type` param introduced and examples



</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.

+ `ner_clinical` -> `he`
+ `date_of_death_parser`
+ `date_of_birth_parser`
+ `bert_sequence_classifier_sdoh_frailty`
+ `ner_human_phenotype_go_clinical_langtest`
+ `ner_human_phenotype_gene_clinical_langtest`
+ `ner_risk_factors_langtest`




</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">



## Previous versions

</div>
{%- include docs-healthcare-pagination.html -%}
