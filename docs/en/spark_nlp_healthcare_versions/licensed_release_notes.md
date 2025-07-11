---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Healthcare NLP Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/licensed_release_notes
key: docs-licensed-release-notes
modify_date: 2025-06-26
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 6.0.3

#### Highlights

We are delighted to announce the release of our latest enhancements and updates for Healthcare NLP.

+ Support for obfuscation equivalents to normalize entity variants in DeIdentification (e.g. Robert vs Rob will be treated same)
+ Deterministic fallback for missing Date shifts in DeIdentification
+ Dictionary support for `Deidentification` with `setSelectiveObfuscationModes` parameter
+ New MedS-NER LLM for structured medical entity extraction via small LLMs
+ Memory optimisation for pretrained zero shot NER models to extract custom entities from out-of-distribution datasets
+ Enhanced phenotype entity mapping pipeline with HPO standardization and advanced entity extraction
+ Optimized clinical De-Identification pipelines for secure and compliant healthcare data processing with one liner
+ Various core improvements, bug fixes, enhanced overall robustness, and reliability of Spark NLP for Healthcare
    - Improved incorrect multi-letter replacements for single-letter names in obfuscation
    - Substring logic crash fix in `TextMatcherInternal` for safer token handling
    - Memory optimization for `PretrainedZeroShotNER` to reduce memory usage during inference
+ New and updated notebooks and demonstrations
    - Updated [Text Matcher Internal](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/40.1.Text_Matcher_Internal.ipynb) Notebook

These enhancements will elevate your experience with Healthcare NLP, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.


</div><div class="h3-box" markdown="1">
    
#### New Feature: Support for Obfuscation Equivalents to Normalize Entity Variants

A new **feature** has been added to support defining *obfuscation equivalents* — enabling consistent replacement of variant forms of the same entity during de-identification.

**Use case examples:**
- `"Alex"` and `"Alexander"` → always mapped to the same obfuscated value under `"NAME"`
- `"CA"` and `"Calif."` → normalized to `"California"` under `"STATE"`

**How it works:**
- Accepts a list of string triplets: `[variant, entityType, canonical]`
- Both `variant` and `entityType` are **case-insensitive**
- Ensures consistent and semantically aligned obfuscation across documents



*Example*:

```python
from johnsnowlabs import nlp, medical
equvalent_list = [
    ["Alex", "NAME", "Alexander"],
    ["Jenny", "NAME", "Jennifer"],
    ["Liz", "NAME", "Elizabeth"],
    ["CA", "LOCATION", "California"],
    ["NY", "CITY", "New York"]
]
obfuscation = DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"]) \
    .setOutputCol("deidentified") \
    .setMode("obfuscate")\
    .setObfuscationEquivalents(equvalent_list)\
    .setSeed(103)\
    .setGenderAwareness(True)

text ='''
Record date: 2023-03-08. The patient, Jennifer Thompson, is 63 years old.
Dr. Elizabeth Carter, from Downtown Health Center in New York, NY, 10027, Phone: 212-123-4567.
Dr. Liz discharged Jenny on 2023-03-08. Her medical record number is 77881234.
'''

```

*Result*:

```bash
Record date: 2023-04-10. The patient, Maryl Gallant, is 75 years old.                                                       
Dr. Rosanne Grand, from Doctors Specialty Hospital in Watonga, Watonga, 01194, Phone: 909-098-7654.
Dr. Rosanne discharged Maryl on 2023-04-10. Her medical record number is 44330987.                                                             
```

- Also supports loading equivalence rules from external files via `.setObfuscationEquivalentsResource`.

*Example*:

```python
obfuscation.setObfuscationEquivalentsResource("path/to/equivalents.csv")
```

- `getDefaultObfuscationEquivalents`: Returns the default obfuscation equivalents for common entities

```python
[
    ['Alex', 'FIRST_NAME', 'Alexander'],
    ['Rob', 'FIRST_NAME', 'Robert'],
    ['Bob', 'FIRST_NAME', 'Robert'],
    ['Bobby', 'FIRST_NAME', 'Robert'],
    ['Liz', 'FIRST_NAME', 'Elizabeth'],
    ['Beth', 'FIRST_NAME', 'Elizabeth'],
    ['Lizzy', 'FIRST_NAME', 'Elizabeth'],
    .....
]
```


- `setEnableDefaultObfuscationEquivalents`: Sets whether to enable default obfuscation equivalents for common entities.
This parameter allows the system to automatically include a set of predefined common English name equivalents. The default is False.


</div><div class="h3-box" markdown="1">


#### New Feature: Deterministic Fallback for Missing Date Shifts in DeIdentification

A new utility has been added to **automatically fill missing or empty values** in a date shift column using a **deterministic, ID-based pseudo-random fallback**.

This feature is especially useful in **de-identification pipelines** where:

- Date shifts must be **consistent per ID**
- Some rows have **null or missing shift values**

**Logic:**

- If another row with the same `ID` has a shift value, it is **reused**
- If no shift exists for that ID, a fallback shift is **generated using a deterministic hash function** based on the `ID` and a fixed seed
- Fallback shifts are **always within the range** `[1, maxShiftDays]`


*Example*:

```python
import pandas as pd
data = pd.DataFrame(
    {'patientID' : ['A001', 'A002', 'A001', 'A002', 'A003', 'A003'],
     'text' : [
         'Chris Brown was discharged on 10/02/2022',
          'Mark White was discharged on 03/01/2020',
          'Chris Brown was born on 05/10/1982',
          'Mark White was born on 10/04/2000',
          'John was discharged on 03/15/2022',
          'John Moore was born on 12/31/2002'
      ],
     'dateshift' : ['10', '-2', None, None, None, 5]
    }
)
input_df = spark.createDataFrame(data)

from sparknlp_jsl.utils import DateShiftFiller
filler = sparknlp_jsl.utils.DateShiftFiller(spark, seed=42, max_shift_days=60)
result_df = filler.fill_missing_shifts(input_df, id_col="patientID", 
                                       shift_col="dateshift", suffix="_filled")
```

*Result*:

```bash
|patientID|text                                    |dateshift|dateshift_filled|
|---------|----------------------------------------|---------|----------------|
|A002     |Mark White was discharged on 03/01/2020 |-2       |-2              |
|A001     |Chris Brown was discharged on 10/02/2022|10       |10              |
|A001     |Chris Brown was discharged on 03/15/2022|NULL     |10              |
|A003     |John was discharged on 03/15/2022       |NULL     |5               |
|A003     |John Moore was discharged on 12/31/2022 |5        |5               |
|A002     |Mark White discharged on 12/31/2022     |NULL     |-2              |
```



#### Dictionary Support for `Deidentification` with `setSelectiveObfuscationModes` Parameter

Added support for **dictionary input** in the `setSelectiveObfuscationModes` method, allowing more flexible configuration of obfuscation modes for specific entities or contexts.

*Example*:

```python
from johnsnowlabs import nlp, medical

sample_json = {
	"obfuscate": ["PHONE"] ,
	"mask_entity_labels": ["ID", "NAME"],
	"skip": ["DATE"],
	"mask_same_length_chars":["location"],
	"mask_fixed_length_chars":["zip"]
}

deid_doc = nlp.DeIdentification() \
    .setInputCols(["sentence", "token", "ner_chunk"]) \
    .setOutputCol("deidentified") \
    .setMode("mask")\
    .setSameLengthFormattedEntities(["PHONE"])\
    .setFixedMaskLength(2)\
    .setSelectiveObfuscationModes(sample_json)

text = """Record date : 2023-01-13.                                                               
The patient, Emma Wilson, is 50 years old.                                                 
Dr. John Lee, from Royal Medical Clinic in Chicago, 0295 Keats Street , Phone 55-555-5555.
Her phone number: 444-456-7890 and her medical record number is 56467890.                  
"""
```

*Result*:

```bash
Record date : 2023-01-13.                                                                
The patient, <NAME>, is <AGE> years old.                                                 
Dr. <NAME>, from [******************] in [*****], [***************] , Phone 66-666-6666.
Her phone number: 777-765-4321 and her medical record number is <ID>.  
```



</div><div class="h3-box" markdown="1">
    
#### New MedS NER Model for Structured Medical Entity Extraction

This LLM model is trained to extract and link entities in a document. Users need to define an input schema as explained in the example section. Drug is defined as a list that tells the model that there could be multiple drugs in the document, and it has to extract all of them. Each drug has properties like its name and reaction. Since “name” is only one, it is a string, but there could be multiple reactions, hence it is a list. Similarly, users can define any schema for any entity.

*Example*:

```python
from johnsnowlabs import nlp, medical
medical_llm = medical.AutoGGUFModel.pretrained("jsl_meds_ner_q16_v3", "en", "clinical/models")\
    .setInputCols("document")\
    .setOutputCol("completions")\
    .setBatchSize(1)\
    .setNPredict(100)\
    .setUseChatTemplate(True)\
    .setTemperature(0)

med_ner_prompt = """
### Template:
{
    "drugs": [
        {
            "name": "",
            "reactions": []
        }
    ]
}
### Text:
I feel a bit drowsy & have a little blurred vision , and some gastric problems .
I 've been on Arthrotec 50 for over 10 years on and off , only taking it when I needed it .
Due to my arthritis getting progressively worse , to the point where I am in tears with the agony.
Gp 's started me on 75 twice a day and I have to take it every day for the next month to see how I get on , here goes .
So far its been very good , pains almost gone , but I feel a bit weird , did n't have that when on 50.

"""
```

*Result*:

```bash
{
    "drugs": [
        {
            "name": "Arthrotec",
            "reactions": [
                "drowsy",
                "blurred vision",
                "gastric problems"
            ]
        },
        {
            "name": "75",
            "reactions": [
                "weird"
            ]
        }
    ]
}
```



</div><div class="h3-box" markdown="1">
    
#### Enhanced Phenotype Entity Mapping Pipeline with HPO Standardization and Advanced Entity Extraction

This pipeline is designed to map extracted phenotype entities from clinical or biomedical text to their corresponding Human Phenotype Ontology (HPO) codes and assign their **assertion status** (e.g., present, absent, possible). It ensures that observed symptoms, signs, and clinical abnormalities are **standardized** using controlled HPO terminology, facilitating downstream tasks like cohort retrieval, diagnostics, and phenotype-based decision support.

New enhancements in `TextMatcherInternal`—notably **lemmatization** (`enableLemmatizer`) and **stopword removal** (`enableStopWordsRemoval`)—the matcher now captures a much wider variety of **phrase variations** that were previously missed due to strict string matching.

**Examples:**
- `"apnea of prematurity"` matched to `"Apnea prematurity"` by ignoring stopwords like *"of"*  
- `"bidirectional shunting"` matched to `"bidirectional shunt"` through token normalization

In addition, the `ChunkMapper` leverages **fuzzy matching**, enabling the system to link **non-exact matches** to the correct HPO codes. This makes the entire pipeline more **robust and flexible**, especially in noisy or highly variable clinical narratives.

These improvements significantly increase **recall** and **semantic matching coverage**, supporting more accurate and complete phenotype extraction from real-world medical text.


*Example*:

```python
from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("hpo_mapper_pipeline_v2", "en", "clinical/models")

text= """APNEA: Presumed apnea of prematurity since < 34 wks gestation at birth.
HYPERBILIRUBINEMIA: At risk for hyperbilirubinemia d/t prematurity.
1/25-1/30: Received Amp/Gent while undergoing sepsis evaluation.
Mother is A+, GBS unknown, and infant delivered
for decreasing fetal movement and preeclampsia.
Echo showed PFO with bidirectional shunting.
"""
```

*Result*:

{:.table-model-big}
| hpo_code   | matched_text            | ner_chunk                | begin | end | result   |
|------------|-------------------------|--------------------------|--------|-----|----------|
| HP:0002104 | apnea                   | apnea                    | 16     | 20  | possible |
| HP:0034236 | Apnea prematurity       | apnea of prematurity     | 16     | 35  | present  |
| HP:0002904 | Hyperbilirubinemia      | hyperbilirubinemia       | 104    | 121 | present  |
| HP:0100806 | sepsis                  | sepsis                   | 186    | 191 | present  |
| HP:0100602 | Preeclampsia            | preeclampsia             | 287    | 298 | present  |
| HP:0012383 | bidirectional shunt     | bidirectional shunting   | 322    | 343 | present  |
| HP:0001558 | decrease fetal movement | decreasing fetal movement| 257    | 281 | present  |



#### Optimized Clinical De-identification Pipelines for Secure and Compliant Healthcare Data Processing

We’ve introduced a suite of optimized clinical de-identification pipelines to enhance the anonymization of sensitive healthcare data. These pipelines combine deep learning (NERDL), zero-shot models, and rule-based methods to perform accurate Named Entity Recognition (NER) across clinical documents. Each pipeline is tailored for performance, scalability, and compliance with privacy regulations, ensuring data integrity while supporting both benchmarking and real-world deployment.


{:.table-model-big}
|    Pipeline Name                                      | Stages |
|-------------------------------------------------------|---------------------------------------|
|`ner_profiling_deidentification`                       |20 NERDL, 1 ZeroShot, 20 RuleBased NER |
|`ner_deid_docwise_benchmark_optimized`                 | 3 NERDL, 19 RuleBased NER             |
|`ner_deid_docwise_benchmark_optimized_zeroshot_partial`| 1 ZeroShot                            |
|`clinical_deidentification_docwise_benchmark_optimized`| 3 NERDL, 19 RuleBased NER             |
|`clinical_deidentification_docwise_benchmark_light`    | 3 NERDL, 19 RuleBased NER             |
|`clinical_deidentification_docwise_benchmark_light_v2` | 1 NERDL, 1 ZeroShot, 19 RuleBased NER |



*Example*:

```python
from johnsnowlabs import nlp, medical

deid_pipeline = nlp.PretrainedPipeline("clinical_deidentification_docwise_benchmark_optimized", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890 ."""

deid_result = deid_pipeline.fullAnnotate(text)
```

*Result*:

```bash
Masked with entity labels
------------------------------
Dr. <DOCTOR>, from <HOSPITAL> in <CITY>, attended to the patient on <DATE>.
The patient’s medical record number is <ID>.
The patient, <PATIENT>, is <AGE>, her Contact number: <PHONE> .

Obfuscated
------------------------------
Dr. Valerie Aho, from Mercy Hospital Aurora in Berea, attended to the patient on 30/05/2024.
The patient’s medical record number is 78689012.
The patient, Johnathon Bunde, is 55 years old, her Contact number: 666-678-9012 .
```



</div><div class="h3-box" markdown="1">
    
#### Various core improvements, bug fixes, and overall enhancements to the robustness of Spark NLP for Healthcare

- **Improved incorrect multi-letter replacements for single-letter names in obfuscation**  
Resolved an issue where single-letter initials (e.g., "R" in "William R") were being obfuscated into multi-letter strings (e.g., "LU").  
Initials are now consistently replaced with a **different single-letter initial**, preserving length and format.

- **Substring logic crash fix in `TextMatcherInternal` for safer token handling**  
Enhanced reliability by adding safer token index handling and guarding substring extraction against unexpected errors.

- **Memory optimization for `PretrainedZeroShotNER` to reduce memory usage during inference**
Reduced memory footprint during inference by optimizing the internal handling of zero-shot NER models, improving performance and scalability for large datasets.



</div><div class="h3-box" markdown="1">

#### Updated Notebooks and Demonstrations for making Spark NLP for Healthcare Easier To Navigate And Understand

- Updated [Text Matcher Internal](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/40.1.Text_Matcher_Internal.ipynb) Notebook



</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.


+ `jsl_meds_ner_q16_v3`
+ `jsl_meds_ner_q8_v3`
+ `jsl_meds_ner_q4_v3`
+ `sbiobertresolve_umls_disease_syndrome`
+ `sbiobertresolve_umls_findings`
+ `sbiobertresolve_umls_clinical_drugs`
+ `sbiobertresolve_umls_general_concepts`
+ `sbiobertresolve_umls_major_concepts`
+ `sbiobertresolve_umls_drug_substance`
+ `biolordresolve_umls_general_concepts`
+ `hpo_mapper_pipeline`
+ `meddra_llt_snomed_mapper`            
+ `snomed_meddra_llt_mapper`             
+ `explain_clinical_doc_sdoh`            
+ `explain_clinical_doc_mental_health`   
+ `ner_medication_generic_pipeline`      
+ `ner_deid_context_augmented_pipeline`  
+ `icd10cm_umls_mapper`
+ `loinc_umls_mapper`
+ `mesh_umls_mapper`
+ `rxnorm_umls_mapper`
+ `snomed_umls_mapper`
+ `umls_icd10cm_mapper`
+ `umls_loinc_mapper`
+ `umls_mesh_mapper`
+ `umls_rxnorm_mapper`
+ `umls_snomed_mapper`
+ `umls_clinical_drugs_mapper`
+ `umls_clinical_findings_mapper`
+ `umls_disease_syndrome_mapper`
+ `umls_drug_substance_mapper`
+ `umls_major_concepts_mapper`
+ `ner_profiling_deidentification`
+ `ner_deid_docwise_benchmark_optimized`
+ `ner_deid_docwise_benchmark_optimized_zeroshot_partial`
+ `clinical_deidentification_docwise_benchmark_optimized`
+ `clinical_deidentification_docwise_benchmark_light`
+ `clinical_deidentification_docwise_benchmark_light_v2`




</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">



## Previous versions

</div>
{%- include docs-healthcare-pagination.html -%}
