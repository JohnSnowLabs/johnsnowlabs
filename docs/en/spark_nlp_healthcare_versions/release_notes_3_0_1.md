---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Healthcare NLP v3.0.1 Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/release_notes_3_0_1
key: docs-licensed-release-notes
modify_date: 2021-07-14
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="prev_ver h3-box" markdown="1">

### 3.0.1

We are very excited to announce that **Spark NLP for Healthcare 3.0.1** has been released!

</div><div class="h3-box" markdown="1">

#### Highlights:

* Fixed problem in Assertion Status internal tokenization (reported in Spark-NLP #2470).
* Fixes in the internal implementation of DeIdentificationModel/Obfuscator.
* Being able to disable the use of regexes in the Deidentification process
* Other minor bug fixes & general improvements.

</div><div class="h3-box" markdown="1">

#### DeIdentificationModel Annotator

##### New `seed` parameter.
Now we have the possibility of using a seed to guide the process of obfuscating entities and returning the same result across different executions. To make that possible a new method setSeed(seed:Int) was introduced.

**Example:**
Return obfuscated documents in a repeatable manner based on the same seed.
##### Scala
```scala
deIdentification = DeIdentification()
      .setInputCols(Array("ner_chunk", "token", "sentence"))
      .setOutputCol("dei")
      .setMode("obfuscate")
      .setObfuscateRefSource("faker")
      .setSeed(10)
      .setIgnoreRegex(true)
```
##### Python
```python
de_identification = DeIdentification() \
            .setInputCols(["ner_chunk", "token", "sentence"]) \
            .setOutputCol("dei") \
            .setMode("obfuscate") \
            .setObfuscateRefSource("faker") \
            .setSeed(10) \
            .setIgnoreRegex(True)

```

This seed controls how the obfuscated values are picked from a set of obfuscation candidates. Fixing the seed allows the process to be replicated.

**Example:**

Given the following input to the deidentification:
```
"David Hale was in Cocke County Baptist Hospital. David Hale"
```

If the annotator is set up with a seed of 10:
##### Scala
```
val deIdentification = new DeIdentification()
      .setInputCols(Array("ner_chunk", "token", "sentence"))
      .setOutputCol("dei")
      .setMode("obfuscate")
      .setObfuscateRefSource("faker")
      .setSeed(10)
      .setIgnoreRegex(true)
```
##### Python
```python
de_identification = DeIdentification() \
            .setInputCols(["ner_chunk", "token", "sentence"]) \
            .setOutputCol("dei") \
            .setMode("obfuscate") \
            .setObfuscateRefSource("faker") \
            .setSeed(10) \
            .setIgnoreRegex(True)

```

The result will be the following for any execution,

```
"Brendan Kitten was in New Megan.Brendan Kitten"
```
Now if we set up a seed of 32,
##### Scala

```scala
val deIdentification = new DeIdentification()
      .setInputCols(Array("ner_chunk", "token", "sentence"))
      .setOutputCol("dei")
      .setMode("obfuscate")
      .setObfuscateRefSource("faker")
      .setSeed(32)
      .setIgnoreRegex(true)
```
##### Python
```python
de_identification = DeIdentification() \
            .setInputCols(["ner_chunk", "token", "sentence"]) \
            .setOutputCol("dei") \
            .setMode("obfuscate") \
            .setObfuscateRefSource("faker") \
            .setSeed(10) \
            .setIgnoreRegex(True)
```

The result will be the following for any execution,

```
"Louise Pear was in Lake Edward.Louise Pear"
```

##### New `ignoreRegex` parameter.
You can now choose to completely disable the use of regexes in the deidentification process by setting the setIgnoreRegex param to True.
**Example:**
##### Scala

```scala
DeIdentificationModel.setIgnoreRegex(true)
```

</div><div class="h3-box" markdown="1">

##### Python
```python
DeIdentificationModel().setIgnoreRegex(True)
```

The default value for this param is `False` meaning that regexes will be used by default.

</div><div class="h3-box" markdown="1">

##### New supported entities for Deidentification & Obfuscation:

We added new entities to the default supported regexes:

* `SSN - Social security number.`
* `PASSPORT - Passport id.`
* `DLN - Department of Labor Number.`
* `NPI - National Provider Identifier.`
* `C_CARD - The id number for credits card.`
* `IBAN - International Bank Account Number.`
* `DEA - DEA Registration Number, which is an identifier assigned to a health care provider by the United States Drug Enforcement Administration.`

We also introduced new Obfuscator cases for these new entities.

</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>
{%- include docs-healthcare-pagination.html -%}