---
layout: docs
header: true
seotitle: Spark NLP | John Snow Labs
title: Risk Adjustments Score Calculation
permalink: /docs/en/healthcare_risk_adjustments_score_calculation
key: docs-licensed-risk-adjustments-score-calculation
modify_date: "2022-12-26"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

Risk Adjustment Score (RAF) implementation uses the Hierarchical Condition Category (HCC) and Prescription Hierarchical Condition Category (RxHCC) Risk Adjustment models from the Centers for Medicare & Medicaid Service (CMS). HCC groups similar conditions in terms of healthcare costs and similarities in the diagnosis, and the model uses any ICD code that has a corresponging HCC and RxHCC category in the computation, discarding other ICD codes.

</div><div class="h3-box" markdown="1">

## CMS-HCC Risk Score Calculation

This module supports **versions 22, 23, 24, 28 and ESRDV21 of the CMS-HCC** risk adjustment model and needs the following parameters in order to calculate the risk score:

- ICD Codes (Obtained by, e.g., our pretrained model `sbiobertresolve_icd10cm_augmented_billable_hcc` from the[SentenceEntityResolverModel](https://nlp.johnsnowlabs.com/docs/en/licensed_annotators#sentenceentityresolver) annotator)
- Age (Obtained by, e.g., our pretrained model `ner_jsl` from the[NerModel](https://nlp.johnsnowlabs.com/docs/en/licensed_annotators#nermodel) annotator)
- Gender (Obtained by, e.g., our pretrained model `classifierdl_gender_biobert` from the [ClassifierDLModel](https://nlp.johnsnowlabs.com/docs/en/annotators#classifierdl) annotator)
- The eligibility segment of the patient (information from the health plan provider)
- The original reason for entitlement (information from the health plan provider)
- If the patient is in Medicaid or not (information from the health plan provider)

</div><div class="h3-box" markdown="1">

### Available Softwares and Profiles

**CMS-HCC** module supports the following versions and years:

| Version 22| Version 23| Version 24| Version 28| ESRD V21|
|-|-|-|-|-|
|Year 2017|Year 2018|Year 2019| Year 24| Year 19|
|Year 2018|Year 2019|Year 2020| | |
|Year 2019| |Year 2021| | |
|Year 2020| |Year 2022| | |
|Year 2021| | | | |
|Year 2022| | | | |

</div><div class="h3-box" markdown="1">

### Usage

The module can perform the computations given a data frame containing the required information (age, gender, ICD codes, eligibility segment, the original reason for entitlement, and if the patient is in Medicaid or not). For example, given the dataset `df`:

```
+--------------+---+--------------------+------+-----------+----+--------+----------+
|      filename|age|          icd10_code|gender|eligibility|orec|medicaid|       DOB|
+--------------+---+--------------------+------+-----------+----+--------+----------+
|mt_note_03.txt| 66|[C499, C499, D618...|     F|        CND|   1|   false|1956-05-30|
|mt_note_01.txt| 59|              [C801]|     F|        CFA|   0|    true|1961-10-12|
|mt_note_10.txt| 16|      [C6960, C6960]|     M|        CFA|   2|   false|2006-02-14|
|mt_note_08.txt| 66|        [C459, C800]|     F|        CND|   1|    true|1956-03-17|
|mt_note_09.txt| 19|      [D5702, K5505]|     M|        CPA|   3|    true|2003-06-11|
|mt_note_05.txt| 57|[C5092, C5091, C5...|     F|        CPA|   3|    true|1963-08-12|
|mt_note_06.txt| 63|        [F319, F319]|     F|        CFA|   0|   false|1959-07-24|
+--------------+---+--------------------+------+-----------+----+--------+----------+
```
Where column `orec` means original reason for entitlement and `DOB` means date of birth (can also be used to compute age). You can use any of the available profiles to compute the scores (in the example, we use version 24, year 2020):

```python
from johnsnowlabs import medical

# Creates the risk profile
df = df.withColumn(
    "hcc_profile",
    medical.profileV24Y20(
        df.icd10_code,
        df.age,
        df.gender,
        df.eligibility,
        df.orec,
        df.medicaid
    ),
)

# Extract relevant information
df = (
    df.withColumn("risk_score", df.hcc_profile.getItem("risk_score"))
      .withColumn("hcc_lst", df.hcc_profile.getItem("hcc_lst"))
      .withColumn("parameters", df.hcc_profile.getItem("parameters"))
      .withColumn("details", df.hcc_profile.getItem("details"))
)

df.select(
    "filename",
    "risk_score",
    "icd10_code",
    "age",
    "gender",
    "eligibility",
    "orec",
    "medicaid",
).show(truncate=False)
```

```
+--------------+----------+---------------------------------------------+---+------+-----------+----+--------+
|filename      |risk_score|icd10_code                                   |age|gender|eligibility|orec|medicaid|
+--------------+----------+---------------------------------------------+---+------+-----------+----+--------+
|mt_note_01.txt|0.158     |[C801]                                       |59 |F     |CFA        |0   |true    |
|mt_note_03.txt|1.03      |[C499, C499, D6181, M069, C801]              |66 |F     |CND        |1   |false   |
|mt_note_05.txt|2.991     |[C5092, C5091, C779, C5092, C800, G20, C5092]|57 |F     |CPA        |3   |true    |
|mt_note_06.txt|0.299     |[F319]                                       |63 |F     |CFA        |0   |true    |
|mt_note_08.txt|2.714     |[C459, C800]                                 |66 |F     |CND        |1   |false   |
|mt_note_09.txt|1.234     |[D5702, K5505]                               |19 |F     |CPA        |3   |true    |
+--------------+----------+---------------------------------------------+---+------+-----------+----+--------+
```

For more details and usage examples, check the [Medicare Risk Adjustment](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings_JSL/Healthcare/3.1.Calculate_Medicare_Risk_Adjustment_Score.ipynb) notebook from our Spark NLP Workshop repository.

</div><div class="h3-box" markdown="1">

## CMS-RxHCC Risk Score Calculation

This module supports **versions 05 and 08 of CMS-RxHCC** risk adjustment model and needs the following parameters in order to calculate the risk score:

- ICD Codes (Obtained by, e.g., our pretrained model `sbiobertresolve_icd10cm_augmented_billable_hcc` from the[SentenceEntityResolverModel](https://nlp.johnsnowlabs.com/docs/en/licensed_annotators#sentenceentityresolver) annotator)
- Age (Obtained by, e.g., our pretrained model `ner_jsl` from the[NerModel](https://nlp.johnsnowlabs.com/docs/en/licensed_annotators#nermodel) annotator)
- Gender (Obtained by, e.g., our pretrained model `classifierdl_gender_biobert` from the [ClassifierDLModel](https://nlp.johnsnowlabs.com/docs/en/annotators#classifierdl) annotator)
- The eligibility segment of the patient (information from the health plan provider)
- The original reason for entitlement (information from the health plan provider)
- End-stage renal disease indicator (ESRD) of the patient (information from the health plan provider)

</div><div class="h3-box" markdown="1">

### Available Softwares and Profiles

**CMS-RxHCC** module supports the following versions and years:

| Version 05| Version 08|
|-|-|
|Year 20|Year 22|
|Year 21|Year 23|
|Year 22| |
|Year 23| |

</div><div class="h3-box" markdown="1">

### Usage

The module can perform the computations given a data frame containing the required information (age, gender, ICD codes, eligibility segment, the original reason for entitlement, and the ESRD indicator of the patient). For example, given the dataset `rxhcc_df`:

```
+--------------+---+------------------------------------------------------------------------------------------+------+--------------+----+-----+----------+
|      filename|age|                                                                                icd10_code|gender|   eligibility|orec| esrd|       DOB|
+--------------+---+------------------------------------------------------------------------------------------+------+--------------+----+-----+----------+
|mt_note_01.txt| 59|                                                                    [C50.92, P61.4, C80.1]|     F|CE_NoLowNoAged|   0| true|1961-10-12|
|mt_note_03.txt| 66|                                                 [C49.9, J18.9, C49.9, D61.81, I26, M06.9]|     F|  CE_NoLowAged|   1|false|1956-05-30|
|mt_note_05.txt| 57|[C50.92, C50.91, C50.9, C50.92, C50.9, C80.0, T78.40, R50.9, G25.81, P39.9, I97.2, C50.92]|     F|        CE_LTI|   3| true|1963-08-12|
|mt_note_06.txt| 63|                                     [C45, F31.9, Q40.1, D35.00, R18, D20.1, F31.9, L72.0]|     F|         NE_Lo|   0|false|1959-07-24|
|mt_note_08.txt| 66|                                                             [J90, C45.9, J90, C45, C80.0]|     F|       NE_NoLo|   1| true|1956-03-17|
|mt_note_09.txt| 19|                                             [D50.8, D57.0, O99.0, D57.02, K55.05, M46.42]|     M|  CE_LowNoAged|   3| true|2003-06-11|
|mt_note_10.txt| 16|                                                                          [C69.60, C69.60]|     M|        NE_LTI|   2|false|2006-02-14|
+--------------+---+------------------------------------------------------------------------------------------+------+--------------+----+-----+----------+
```
Where column `orec` means original reason for entitlement, `esrd` means end-stage renal disease indicator and `DOB` means date of birth (can also be used to compute age).

```python
from johnsnowlabs import medical

# Creates the risk profile
rxhcc_df = rxhcc_df.withColumn(
    "rxhcc_profile",
    medical.profileRxHCCV08Y23(
        rxhcc_df.icd10_code,
        rxhcc_df.age,
        rxhcc_df.gender,
        rxhcc_df.eligibility,
        rxhcc_df.orec,
        rxhcc_df.esrd
    ),
)

# Extract relevant information
rxhcc_df = (
    rxhcc_df.withColumn("risk_score", df.rxhcc_profile.getItem("risk_score"))
            .withColumn("parameters", df.rxhcc_profile.getItem("parameters"))
            .withColumn("details", df.rxhcc_profile.getItem("details"))
)

df.select(
    "filename",
    "risk_score",
    "age",
    "icd10_code",
    "gender",
    "eligibility",
    "orec",
    "esrd",
).show(truncate=False)
```

```
+--------------+----------+---+------------------------------------------------------------------------------------------+------+--------------+----+-----+
|      filename|risk_score|age|                                                                                icd10_code|gender|   eligibility|orec| esrd|
+--------------+----------+---+------------------------------------------------------------------------------------------+------+--------------+----+-----+
|mt_note_01.txt|0.575     | 59|                                                                    [C50.92, P61.4, C80.1]|     F|CE_NoLowNoAged|   0| true|
|mt_note_03.txt|0.367     | 66|                                                 [C49.9, J18.9, C49.9, D61.81, I26, M06.9]|     F|  CE_NoLowAged|   1|false|
|mt_note_05.txt|2.729     | 57|[C50.92, C50.91, C50.9, C50.92, C50.9, C80.0, T78.40, R50.9, G25.81, P39.9, I97.2, C50.92]|     F|        CE_LTI|   3| true|
|mt_note_06.txt|1.703     | 63|                                     [C45, F31.9, Q40.1, D35.00, R18, D20.1, F31.9, L72.0]|     F|         NE_Lo|   0|false|
|mt_note_08.txt|1.38      | 66|                                                             [J90, C45.9, J90, C45, C80.0]|     F|       NE_NoLo|   1| true|
|mt_note_09.txt|1.677     | 19|                                             [D50.8, D57.0, O99.0, D57.02, K55.05, M46.42]|     M|  CE_LowNoAged|   3| true|
|mt_note_10.txt|1.645     | 16|                                                                          [C69.60, C69.60]|     M|        NE_LTI|   2|false|
+--------------+----------+---+------------------------------------------------------------------------------------------+------+--------------+----+-----+
```

For more details and usage examples, check the [Medicare Risk Adjustment](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings_JSL/Healthcare/3.1.Calculate_Medicare_Risk_Adjustment_Score.ipynb) notebook from our Spark NLP Workshop repository.

</div>