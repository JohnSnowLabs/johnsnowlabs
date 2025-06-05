---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Healthcare NLP v6.0.2 Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/release_notes_6_0_2
key: docs-licensed-release-notes
modify_date: 2025-06-05
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 6.0.2

#### Highlights

#### Highlights

We are delighted to announce remarkable enhancements in our latest release of Healthcare NLP. **This release comes with improvements to the De-Identification module, including advanced masking strategies, geographic consistency for address obfuscation, customizable date formats, case-sensitive fake data generation for PHI obfuscation, and fine-grained control over obfuscation sources and replacement rules. Alongside these, the release also includes a new Metadata Annotation Converter annotator, expanded phrase matching capabilities in Text Matcher, enhanced entity filtering in ChunkMapper Filterer, and several new and updated clinical pretrained models and pipelines.**

+ Geographic consistency support and country obfuscation control in `De-Identification` module
+ New masking policies for entity redaction in `De-Identification` to control how masked entities look like afterwards
+ Custom date format support for date obfuscation for normalizing and shifting dates in uncommon formats
+ Improved case sensitivity for fake data generation in `De-Identification` to ensure the casing of each token and chars intact for certain entities after PHI obfuscation
+ Selective obfuscation source configuration in `De-Identification` to allow more flexibility while using custom fake data sources vs embedded ones
+ Static and file-based obfuscation entity vs chunk pair support in `De-Identification` for a better treatment of VIP entities 
+ Enhanced phrase matching in `TextMatcher`: Lemmatization, Stemming, Stopword Handling & Token Shuffling in both source text and target keywords while matching
+ Introducing a new annotator `MetadataAnnotationConverter` to utilise metadata information within the pipeline
+ Enhanced entity filtering in `ChunkMapperFilterer` with whitelist and blacklist support
+ Updated notebooks and demonstrations for making Healthcare NLP easier to navigate and understand
    - New [TextMatcherInternal](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/40.1.Text_Matcher_Internal.ipynb) Notebook
+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

These enhancements will elevate your experience with Spark NLP for Healthcare, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.


</div><div class="h3-box" markdown="1">

#### Geographic Consistency Support and Country Obfuscation Control in `De-Identification`

A new parameter `setGeoConsistency(True)` has been introduced in the `DeIdentification` annotator to ensure **realistic and coherent obfuscation of geographic entities**. This feature guarantees that obfuscated addresses make sense by maintaining valid combinations between: 
    - `state`
    - `city`
    - `zip`
    - `street`
    - `phone`

When enabled, the system intelligently selects related fake address components from a unified pool using a deterministic algorithm. This prevents nonsensical combinations like `"New York City, California, ZIP 98006"` by enforcing priority-based mapping across geographic types.

- Priority Order for Consistent Mapping
    1. **State** (highest priority)
    2. **City**
    3. **Zip code**
    4. **Street**
    5. **Phone** (lowest priority)

- Language Requirement
This feature is available only when:
    - `setGeoConsistency(True)` **is enabled**
    - `setLanguage("en")` **is set**

For all non-English languages, the feature is ignored (for now).

- Interaction with Other Parameters
Enabling `geoConsistency` will automatically override:
    - `keepTextSizeForObfuscation`
    - `consistentObfuscation` on some address entities
    - any file-based faker settings

This ensures full control over the address pool for geographic coherence and we plan to improve this feature further with user feedbacks for a seamless experience.

- **Country Obfuscation Control**

Previously, country entities were **always obfuscated** by default in `DeIdentification`.  
Now, country obfuscation is **explicitly controlled** via the new parameter:

If set to True, country names will be obfuscated.  
If set to False (default), country names will be preserved.

*Example:*

```python
deid_with_geo_consistency = DeIdentification() \
            .setInputCols(["ner_chunk", "token", "document"]) \
            .setOutputCol("deid_with_geo_consistency") \
            .setMode("obfuscate") \
            .setGeoConsistency(True) \
            .setCountryObfuscation(False) \
            .setSeed(10)

deid_without_geo_consistency = DeIdentification() \
            .setInputCols(["ner_chunk", "token", "document"]) \
            .setOutputCol("deid_without_geo_consistency") \
            .setMode("obfuscate") \
            .setGeoConsistency(False) \
            .setCountryObfuscation(False) \
            .setSeed(10)

text = """
        Patient Medical Record
        Patient Name: Sarah Johnson

        Patient Demographics and Contact Information
        Primary Address:
        1247 Maple Street
        Austin, Texas 78701
        USA
        Contact Information:
        Primary Phone: (512) 555-0198
        """

text_df = self.spark.createDataFrame([[text]]).toDF("text")
```


*Result*:

```bash
Orginal text:
        Patient Medical Record
        Patient Name: Sarah Johnson

        Patient Demographics and Contact Information
        Primary Address:
        1247 Maple Street
        Austin, Texas 78701
        USA
        Contact Information:
        Primary Phone: (512) 555-0198

--------------------------------------------------------
With Geo Consistency:

        Patient Medical Record
        Patient Name: Amanda Shilling

        Patient Demographics and Contact Information
        Primary Address:
        3600 Constitution Blvd
        West Valley City, UT 84119
        USA
        Contact Information:
        Primary Phone: (801) 555-0222

---------------------------------------------------------
Without Geo Consistency:

        Patient Medical Record
        Patient Name: Amanda Shilling

        Patient Demographics and Contact Information
        Primary Address:
        800 West Leslie
        Hart, Texas 41452
        USA
        Contact Information:
        Primary Phone: (029) 000-5281

```



</div><div class="h3-box" markdown="1">

#### New Masking Policies for Entity Redaction in `De-Identification`

- Introduced `same_length_chars_without_brackets` masking policy: masks entities with asterisks of the same length **without square brackets**.
- Introduced `entity_labels_without_brackets` masking policy: replaces entities with their label **without square brackets**.

*Example:*

```python
deid_entity_labels = DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"])\
    .setOutputCol("deid_entity_label")\
    .setMode("mask")\
    .setReturnEntityMappings(True)\
    .setMaskingPolicy("entity_labels_without_brackets")

deid_same_length = DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"])\
    .setOutputCol("deid_same_length")\
    .setMode("mask")\
    .setReturnEntityMappings(True)\
    .setMaskingPolicy("same_length_chars_without_brackets")

deid_fixed_length = DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"])\
    .setOutputCol("deid_fixed_length")\
    .setMode("mask")\
    .setReturnEntityMappings(True)\
    .setMaskingPolicy("fixed_length_chars")\
    .setFixedMaskLength(4)
```    

*Result*:

{:.table-model-big}
|Sentence | `deid_entity_label` | `deid_same_length` | `deid_fixed_length` |
|---------|---------------------| -------------------| --------------------|
| Record date : 2093-01-13 , David Hale , M.D . | Record date : DATE , NAME , M.D .                 | Record date : \*\*\*\*\*\*\*\*\*\* , \*\*\*\*\*\*\*\*\*\* , M.D . | Record date : \*\*\*\* , \*\*\*\* , M.D . |
| , Name : Hendrickson Ora , MR # 7194334 Date : 01/13/93 . | , Name : NAME , MR # ID Date : DATE . | , Name : \*\*\*\*\*\*\*\*\*\*\*\*\*\*\* , MR # \*\*\*\*\*\*\* Date : \*\*\*\*\*\*\*\* . | , Name : \*\*\*\* , MR # \*\*\*\* Date : \*\*\*\* . |
| PCP : Oliveira , 25 years-old , Record date : 01/13/93 . | PCP : NAME , AGE years-old , Record date : DATE . | PCP : \*\*\*\*\*\*\*\* , \*\* years-old , Record date : \*\*\*\*\*\*\*\* . | PCP : \*\*\*\* , \*\*\*\* years-old , Record date : \*\*\*\* . |
| Cocke County Baptist Hospital , 0295 Keats Street , Phone 800-555-5555 . | LOCATION , LOCATION , Phone CONTACT . | \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* , \*\*\*\*\*\*\*\*\*\*\*\*\*\* , Phone \*\*\*\*\*\*\*\*\*\*\*\* . | \*\*\*\* , \*\*\*\* , Phone \*\*\*\* . |


</div><div class="h3-box" markdown="1">

#### Custom Date Format Support for Date Obfuscation

- **Added** support for `additionalDateFormats` parameter to allow specifying custom date formats in addition to the built-in `dateFormats`.

This enables more flexible parsing and obfuscation of non-standard or region-specific date patterns.

*Example:*

```python
de_identification_mask = DeIdentification() \
    .setInputCols(["ner_chunk", "token", "document2"]) \
    .setOutputCol("deid_text_mask") \
    .setMode("masked") \
    .setObfuscateDate(True) \
    .setLanguage("en") \
    .setObfuscateRefSource('faker') \
    .setAdditionalDateFormats(["dd MMMyyyy", "dd/MMM-yyyy"]) \ # new parameter
    .setUseShiftDays(True) \
    .setRegion('us') \
    .setUnnormalizedDateMode("skip")

de_identification_obf = DeIdentification() \
    .setInputCols(["ner_chunk", "token", "document2"]) \
    .setOutputCol("deid_text_obs") \
    .setMode("obfuscate") \
    .setObfuscateDate(True) \
    .setLanguage("en") \
    .setObfuscateRefSource('faker') \
    .setAdditionalDateFormats(["dd MMMyyyy", "dd/MMM-yyyy"]) \ # new parameter
    .setUseShifDays(True) \
    .setRegion('us') \
    .setUnnormalizedDateMode("skip")
```


*Result*:

{:.table-model-big}
| Original Text | Date Shift | Masked Result | Obfuscated Result |
|---------------| ---------- |---------------|-------------------|
| Chris Brown was discharged on 10/02/2022 | -5         | \<PATIENT> was discharged on \<DATE> | Larwance Engels was discharged on 09/27/2022 |
| John was discharged on 03 Apr2022        | 10         | \<PATIENT> was discharged on \<DATE> | Vonda was discharged on 13 Apr2022          |
| John Moore was discharged on 11/May-2025 | 20         | \<PATIENT> was discharged on \<DATE> | Vonda Seals was discharged on 31/May-2025    |



</div><div class="h3-box" markdown="1">

#### Improved Case Sensitivity for Fake Data Generation in `De-Identification`

- **Enhancement:** Fake values generated during obfuscation now respect the original text's casing by default.
- This ensures that fake data matches the case style (lowercase, uppercase, mixed case) of the input entities for more natural and consistent masking results.

*Example*:

```python
obfuscation = DeIdentification()\
    .setInputCols(["sentence", "token", "ner_subentity_chunk"]) \
    .setOutputCol("deidentified") \
    .setMode("obfuscate")\
    .setObfuscateDate(True)\
    .setObfuscateRefSource("faker")

text = '''
Record date : 2093-01-13 , david hale , M.D . , Name : MARIA , Ora MR # 7194334 Date : 01/13/93 . Patient : Oliveira, 25 years-old , Record date : 2079-11-09 .
'''
```


*Result*:

{:.table-model-big}
| sentence | deidentified |
|----------|--------------|
| Record date : 2093-01-13 , david hale , M.D .        | Record date : 2093-03-13 , paula favia , M.D .     |
| , Name : MARIA , Ora MR # 7194334 Date : 01/13/93 .  | , Name : MARYAGNES Liberty MR # 2805665 Date : ... |
| Patient : Oliveira, 25 years-old , Record date : ... | Patient : Johann, 27 years-old , Record date : ... |
    

#### Selective Obfuscation Source Configuration in `De-Identification`
 
Introduced the `setSelectiveObfuscateRefSource()` method to allow **per-entity customization** of obfuscation sources.  
This enables users to specify different obfuscation strategies (e.g., `'faker'`, `'custom'`, `'file'`, `'both'`) for different entity types.  
If an entity is not explicitly configured in this dictionary, the global `obfuscateRefSource` setting will be used as a fallback.

*Example*:

```python
selective_obfuscate_ref_source = {"Drug": "file", "state": "both"}

de_identification = DeIdentification() \
            .setInputCols(["token", "sentence","ner_chunk"]) \
            .setOutputCol("obfuscated") \
            .setObfuscateRefSource("faker") \
            .setMode("obfuscate") \
            .setSelectiveObfuscateRefSource(selective_obfuscate_ref_source) \

```

</div><div class="h3-box" markdown="1">

#### Static and File-Based Obfuscation Pair Support in `De-Identification`

- **Added** `setStaticObfuscationPairs`: allows users to define static `[original, entityType, fake]` triplets directly in code for deterministic obfuscation.
- **Added** `setStaticObfuscationPairsResource`: allows loading obfuscation triplets from an external file (e.g., CSV). Supports custom delimiter through the `options` parameter.

This feature is especially useful in **VIP or high-profile patient** scenarios, where specific sensitive names or locations must always be replaced in a controlled and reproducible way.  

*Example:*

```python
text = """John Smith visited Los Angeles. He was admitted to the emergency department at St. Mary's Hospital after experiencing chest pain. His mother worked as a Nurse  """


# Define pairs in code
pairs = [
    ["John Smith", "PATIENT", "Andrew Snow"],
    ["Los Angeles", "CITY", "New York City"],
    ["St. Mary's Hospital", "HOSPITAL", "Johns Hopkins Hospital"],
    ["Nurse", "PROFESSION", "Cardiologist"]
]

deid = DeIdentification() \
    .setInputCols(["sentence", "token", "ner_chunk"]) \
    .setOutputCol("deidentified") \
    .setMode("obfuscate") \
    .setStaticObfuscationPairs(pairs)

```

*Result*:

{:.table-model-big}
| index | sentence                                                                 | deidentified                                                                 |
|-------|--------------------------------------------------------------------------|------------------------------------------------------------------------------|
| 0     | John Smith visited Los Angeles.                                          | <DOCTOR> visited New York City.                                              |
| 1     | He was admitted to the emergency department at St. Mary's Hospital after experiencing chest pain. | He was admitted to the emergency department at Johns Hopkins Hospital after experiencing chest pain. |
| 2     | His mother worked as a Nurse                                             | His mother worked as a Cardiologist                                          |




</div><div class="h3-box" markdown="1">

#### Enhanced Phrase Matching in TextMatcherInternal: Lemmatization, Stemming, Stopword Handling & Token Shuffling for Smarter NLP

This release introduces **powerful new features** to the `TextMatcherInternal` annotator, enabling more **flexible**, **accurate**, and **linguistically aware** phrase matching in clinical or general NLP pipelines. The additions include support for **lemmatization**, **stemming**, **token permutations**, **stopword control**, and **customizable matching behavior**.


Below are the new parameters and their descriptions in TextMatcherInternal:

{:.table-model-big}
| Parameter | Description |
|-----------|-------------|
| `setEnableLemmatizer(<True/False>)` | Enable lemmatizer                           |
| `setEnableStemmer(<True/False>)`    | Enable stemmer                              |
| `setStopWords(["<word1>", "<word2>", "..."])` | Custom stop word list             |
| `setCleanStopWords(<True/False>)`   | Remove stop words from input                |
| `setShuffleEntitySubTokens(<True/False>)` | Use permutations of entity phrase tokens |
| `setSafeKeywords(["<keyword1>", "<keyword2>", "..."])` | Preserve critical terms, even if stop words |
| `setExcludePunctuation(<True/False>)` | Remove all punctuation during matching      |
| `setCleanKeywords(["<noise1>", "<noise2>", "..."])` | Extra domain-specific noise words to remove |
| `setExcludeRegexPatterns(["<regex_pattern1>", "<regex_pattern2>"])` | Drop matched chunks matching regex          |
| `setReturnChunks("<original/matched>")` | Return stemmed/lemmatized matched phrases   |
| `setSkipMatcherAugmentation(<True/False>)` | Disable matcher-side augmentation        |
| `setSkipSourceTextAugmentation(<True/False>)` | Disable source-side augmentation      |


- Lemmatization & Stemming Support

You can now enable both **lemmatization** and **stemming** to increase recall by matching different inflections of the same word.

Example for Lemmatization and Stemming:  
    - .setEnableLemmatizer(True):  Enables lemmatization to reduce words to their base (dictionary) form  
    - .setEnableStemmer(True): Enables stemming to reduce words to their root form by stripping suffixes

`"talking"` will match `"talk"`  
`"lives"` will match `"life"`  
`"running"` → `"run"`  
`"studies"` → `"study"`  

This is useful for matching core meanings even when word forms vary.

- Shuffiling Support

Example for Shuffiling Subtoken Entities:
    - `.setShuffleEntitySubTokens(True)`: the matcher will consider **all possible token orderings** for each phrase. For example:

**Entity phrase:** `"sleep difficulty"`  
Will match:  
    - `"sleep difficulty"`  
    - `"difficulty sleep"` 

Disabling this option restricts the match to the original order only.

Only available in `TextMatcherInternal`, **not** in `TextMatcherInternalModel`.



- Stop Word Removal for Cleaner Matching

Example for Cleaning StopWords:
    - `.setCleanStopWords(True)`: the matcher will remove common stop words (like `"and"`, `"the"`, `"about"`) from **both the input** and the **entity phrases** before matching. This reduces false negatives caused by unimportant words.

Example for StopWords:
Optional Customization  to set
    - `.setStopWords(["and", "of", "about"])`: # Custom stop words  
    - `.setSafeKeywords(["about"])`: Don't remove important stop words  


- Advanced Cleaning with `safeKeywords`, `cleanKeywords`, `excludePunctuation`

You now have full control over text cleaning:

| Parameter                     | Description |
|-------------------------------|-------------|
| `setStopWords([...])`         | Custom stop word list |
| `setCleanKeywords([...])`     | Extra domain-specific noise words to remove |
| `setSafeKeywords([...])`      | Preserve critical terms, even if they are stop words |
| `setExcludePunctuation(True)` | Remove all punctuation during matching |

These controls allow more precise preprocessing in noisy or informal text environments.


- Augmentation Controls

Control how much automatic variation the matcher considers:  
     - `.setSkipMatcherAugmentation(True)`:  Disable matcher phrase variations     
     - `.setSkipSourceTextAugmentation(True)`:  Disable variations on input text 
      
Disable both for **strict, high-precision** matching. Leave enabled for **broad, high-recall** matching.


-  Controling Match Output Format:
    - .setReturnChunks("original")  # Return chunk as it appears in input  
    - .setReturnChunks("matched")   # Return normalized form (e.g., stemmed or lemmatized)

Regardless of format, `begin` and `end` positions refer to the **original text**.


*Example*:

```python

test_phrases = """
stressor
evaluation psychiatric state
sleep difficulty
"""

with open("test-phrases.txt", "w") as file:
    file.write(test_phrases)

text_matcher = TextMatcherInternal()\
    .setInputCols(["sentence","token"])\
    .setOutputCol("matched_text")\
    .setEntities("./test-phrases.txt")\
    .setEnableLemmatizer(True)\
    .setEnableStemmer(True)\
    .setCleanStopWords(True)\
    .setBuildFromTokens(True)\
    .setReturnChunks("matched")\
    .setShuffleEntitySubTokens(True)\
    .setSkipMatcherAugmentation(False)\
    .setSkipSourceTextAugmentation(False)

text = """
Patient was able to talk briefly about recent life stressors during evaluation of psychiatric state.
She reports difficulty sleeping and ongoing anxiety. Denies suicidal ideation.
"""
```

*Result*:

{:.table-model-big}
| `matched_text`        | `original` | Explanation |
|-----------------------|------------|-------------|
| `evaluation psychiatric state`| `evaluation of psychiatric state`| **Stop word removal**: the word **"of"** was filtered out to enable a match |
| `stressor`                   | `stressors`                      | **Lemmatization** reduced plural form to base word                          |
| `sleep difficulty`           | `difficulty sleeping`            | **Stemming + token shuffle** allowed match despite different word order     |

These examples show how stemming, lemmatization, stop word removal, and token shuffling **combine to increase recall** while still producing interpretable and aligned results.


Please check the [TextMatcherInternal](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/40.1.Text_Matcher_Internal.ipynb) notebook for more informations.


</div><div class="h3-box" markdown="1">

#### Introducing a New Annotator MetadataAnnotationConverter for Custom Annotation Field Mapping

**Added** `MetadataAnnotationConverter`: a new annotator that converts metadata fields in annotations into actual begin, end, or result values.

`MetadataAnnotationConverter` enables users to override fields in Spark NLP annotations using values from their `metadata` dictionary. This is especially useful when metadata contains normalized values, corrected character offsets, or alternative representations of the entity or phrase.


*Example:*

```python
text_matcher = TextMatcherInternal()\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("matched_text")\
    .setEntities("./test-phrases.txt")\
    .setEnableLemmatizer(True) \
    .setEnableStemmer(True) \
    .setCleanStopWords(True) \
    .setBuildFromTokens(False)\
    .setReturnChunks("original")

metadata_annotation_converter = MetadataAnnotationConverter()\
    .setInputCols(["matched_text"])\
    .setInputType("chunk") \
    .setBeginField("begin") \
    .setEndField("end") \
    .setResultField("original_or_matched") \
    .setOutputCol("new_chunk")
```

*Text Matcher Internal Output*:

{:.table-model-big}
| entity | begin | end | result                          | matched                      |
| ------ | ----- | --- | ------------------------------- | ---------------------------- |
| entity | 69    | 99  | evaluation of psychiatric state | evaluation psychiatric state |
| entity | 52    | 60  | stressors                       | stressor                     |
| entity | 114   | 132 | difficulty sleeping             | difficulty sleep             |



*Metadata Annotation Converter Output*:

{:.table-model-big}
| Entity | Begin | End | Result                      |
|--------|-------|-----|-----------------------------|
| entity | 69    | 99  | evaluation psychiatric state|
| entity | 52    | 60  | stressor                    |
| entity | 114   | 132 | difficulty sleep            |


</div><div class="h3-box" markdown="1">

#### Enhanced Entity Filtering in ChunkMapperFilterer with Whitelist and Blacklist Support

The ChunkMapperFilterer annotator now supports fine-grained entity filtering through the introduction of three new parameters:
- whiteList: a list of entity types to explicitly include during filtering. Only entities in this list will be processed.
- blackList: a list of entity types to exclude from filtering. Entities in this list will be ignored.
- caseSensitive: a boolean flag indicating whether the entity matching in whiteList and blackList is case-sensitive.

*Example*:

```python
chunk_mapper_filterer = ChunkMapperFilterer() \
      .setInputCols(["chunk", "RxNorm_Mapper"]) \
      .setOutputCol("chunks_success") \
      .setReturnCriteria("success")\
      .setBlackList(["Tegretol", "ZYVOX"])\
      .setCaseSensitive(False)

samples = [["The patient was given Avandia 4 mg, Tegretol"],
           ["The patient was previously prescribed Zyrtec for allergies, Zyvox for a bacterial infection, and Zytopic to manage a skin condition."]]

data = spark.createDataFrame(samples).toDF("text")
```


*Result without blacklist*:

Before:
{:.table-model-big}
|chunk                   |RxNorm_Mapper          |chunks_success          |
|------------------------|-----------------------|------------------------|
|[Avandia 4 mg, Tegretol]|[261242, 203029]       |[Avandia 4 mg, Tegretol]|
|[Zyrtec, Zyvox, Zytopic]|[58930, 261710, 763297]|[Zyrtec, Zyvox, Zytopic]|


*Result with blacklist*:

{:.table-model-big}
|chunk                   |RxNorm_Mapper          |chunks_success   |
|------------------------|-----------------------|-----------------|
|[Avandia 4 mg, Tegretol]|[261242, 203029]       |[Avandia 4 mg]   |
|[Zyrtec, Zyvox, Zytopic]|[58930, 261710, 763297]|[Zyrtec, Zytopic]|




</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For making Spark NLP For Healthcare Easier To Navigate And Understand

- New [TextMatcherInternal](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/40.1.Text_Matcher_Internal.ipynb) Notebook



</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">

## Versions

</div>
{%- include docs-healthcare-pagination.html -%}
