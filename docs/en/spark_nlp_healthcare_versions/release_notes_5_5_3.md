---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Healthcare NLP v5.5.3 Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/release_notes_5_5_3
key: docs-licensed-release-notes
modify_date: 2025-02-20
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 5.5.3

#### Highlights

We are delighted to announce remarkable enhancements and updates in our latest release of Spark NLP for Healthcare. **This release includes advanced Structured Deidentification with new obfuscation parameters, expanded ContextualEntityRuler capabilities with regex, prefix, and suffix support, and updated clinical pretrained models, and pipelines**. 

+ Enhanced `StructuredDeidentification` with new obfuscation parameters
+ Customizing named entities with contextual rules: enhanced prefix, suffix, and regex support in `ContextualEntityRuler`
+ Enhanced flexibility for chunk-based output in `StructuredJsonConverter`
+ Supporting overlapping sentences in sentence-aware document splitting to feed a longer and better context to downstream models
+ Advanced one-liner clinical NLP pipelines for `oncological` document analysis
+ Introducing the Veterinary MeSH Resolver for accurately mapping veterinary terms to the corresponding MeSH codes
+ New Spanish medical entity resolver for SNOMED mapping
+ New BlogPosts on various topics 
+ Various core improvements; bug fixes, enhanced overall robustness and reliability of Spark NLP for Healthcare
    - Fixed broken `encodeModel` and `setInputSuffix` functions in `LLMLoader`
    - Fixed end index issue in `AssertionChunkConverter`
+ Updated notebooks and demonstrations for making Spark NLP for Healthcare easier to navigate and understand
    - New [Deidentification_Performance_Comparison_Of_Healthcare_NLP_VS_Cloud_Solutions](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/academic/Deidentification_Performance_Comparison_Of_Healthcare_NLP_VS_Cloud_Solutions.ipynb) Notebook
    - Updated [Loading Medical and Open-Souce LLMs](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.Loading_Medical_and_Open-Souce_LLMs.ipynb) Notebook
    - Updated [Contextual_Entity_Ruler](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/47.Contextual_Entity_Ruler.ipynb) Notebook
    - Updated [Clinical Deidentification for Structured Data](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.8.Clinical_Deidentification_for_Structured_Data.ipynb) Notebook
    - Updated [PipelineTracer and PipelineOutputParser](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.4.PipelineTracer_and_PipelineOutputParser.ipynb) Notebook
+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

These enhancements will elevate your experience with Spark NLP for Healthcare, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.


</div><div class="h3-box" markdown="1">

####  Enhanced StructuredDeidentification with New Obfuscation Parameters  

This update introduces new parameters to the `StructuredDeidentification` tool, improving its flexibility for handling sensitive data obfuscation. Key additions include options for regional date formats `region`, selective date obfuscation `keepYear`, `keepMonth`, text length preservation `keepTextSizeForObfuscation`, `fakerLengthOffset`, gender-aware name obfuscation `genderAwareness`, and HIPAA-compliant age anonymization `ageRangesByHipaa`.  

Additionally, new parameters have been added to the `obfuscateColumns()` function, allowing control over output formatting `outputAsArray`, overwriting behavior `overwrite`, and column suffixing `suffix`. These enhancements provide greater control over data anonymization while maintaining data integrity and compliance.


*Example DataFrme*:

```python
# Example DataFrame
data = [
    ("Juan García", "13/02/1977", "711 Nulla St.", 140, "673 431234"),
    ("Will Smith", "23/02/1977", "1 Green Avenue.", 140, "+23 (673) 431234"),
    ("Pedro Ximénez", "11/04/2000", "Calle del Libertador, 7", 100, "912 345623")
]
```

*Example Code*:

```python
obfuscator = StructuredDeidentification(spark=spark,
                                        columns={"NAME": "NAME", "DOB": "DATE", "TEL": "PHONE"},
                                        columnsSeed={"NAME": 23, "DOB": 23},
                                        obfuscateRefSource="faker",
                                        days=5)

obfuscator_df = obfuscator.obfuscateColumns(df)
obfuscator_df.show(truncate=False)
```

*Result*:

{:.table-model-big}
|NAME            |DOB         |ADDRESS                |SBP|TEL               |
|----------------|------------|-----------------------|---|------------------|
|[Gwynda Leriche]|[18/02/1977]|711 Nulla St.          |140|[217 075870]      |
|[Sharman Debar] |[28/02/1977]|1 Green Avenue.        |140|[+76 (106) 964769]|
|[Lavera Postal] |[16/04/2000]|Calle del Libertador, 7|100|[358 709287]      |


*Example Code*:

```python
obfuscator = StructuredDeidentification(spark,
                                        columns={"PATIENT": "PATIENT", "DOB": "DATE", "TEL": "PHONE"},
                                        columnsSeed={"PATIENT": 23, "DOB": 23, "TEL": 23},
                                        obfuscateRefSource = "faker",
                                        days=60,
                                        region="eu",
                                        keepYear=True,
                                        keepTextSizeForObfuscation=True
                                        )
obfuscator_df = obfuscator.obfuscateColumns(df, outputAsArray=False, overwrite=False, suffix="_obfuscated")
obfuscator_df.show(truncate=False)
```

*Result*:

{:.table-model-big}
|NAME         |DOB       |ADDRESS                |SBP|TEL             |DOB_obfuscated|TEL_obfuscated  |NAME_obfuscated|
|-------------|----------|-----------------------|---|----------------|--------------|----------------|---------------|
|Juan García  |13/02/1977|711 Nulla St.          |140|673 431234      |08/02/1977    |984 742547      |Marc Senior    |
|Will Smith   |23/02/1977|1 Green Avenue.        |140|+23 (673) 431234|18/02/1977    |+54 (984) 742547|Leora Rand     |
|Pedro Ximénez|11/04/2000|Calle del Libertador, 7|100|912 345623      |06/04/2000    |681 032510      |Temple Feeler  |

Please check the [Clinical Deidentification for Structured Data](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.8.Clinical_Deidentification_for_Structured_Data.ipynb) Notebook for more information

</div><div class="h3-box" markdown="1">
	
#### Enhanced Flexibility for Chunk-Based Output in `StructuredJsonConverter`

This update adds support for chunk-based results in `StructuredJsonConverter`, providing greater flexibility in text processing. By using the new `.setParentSource("chunk")` option, users can extract structured chunks instead of base schema results, enabling more precise control over text segmentation. Additionally, the new `sentenceColumn` parameter allows retrieval of sentence-level details. The enhanced output schema includes chunk metadata, NER attributes, assertions, and relations, making it particularly valuable for structured NLP applications like clinical text analysis.

*Example*:

```python
pipeline = PretrainedPipeline("explain_clinical_doc_oncology", "en", "clinical/models")
pipeline_tracer = PipelineTracer(pipeline)
converter_schema = pipeline_tracer.createParserDictionary()

text = """The Patient underwent a CT scan of the abdomen, which showed a complex mass."""
text_df = spark.createDataFrame([[text]]).toDF("text")
base_df = pipeline.transform(text_df)

structured_json_converter = (
    StructuredJsonConverter()
      .setConverterSchema(converter_schema)
      .setOutputCol("json")
      .setCleanAnnotations(True)
      .setOutputAsStr(True)
      .setParentSource("chunk")
      .setSentenceColumn("sentence")
)
result_df = structured_json_converter.transform(base_df)

collected_result = result_df.selectExpr("json").collect()
json_result = eval(collected_result[0]["json"])
```

*Result for Before Setting Parameters*:

```python
{
    document_identifier='dabbb011-5900-4542-b771-693151850a2d', 
    document_text=['The Patient underwent a CT scan of the abdomen, which showed a complex mass.\n'], 
    entities=[
        {'ner_label': 'Imaging_Test', 'sentence': '0', 'chunk': 'CT scan of the abdomen', 'end': '45', 'ner_source': 'ner_oncology_chunk', 'ner_confidence': '0.76256', 'begin': '24', 'chunk_id': 'cbe58cc4'}, 
        {'ner_label': 'Tumor_Finding', 'sentence': '0', 'chunk': 'mass', 'end': '74', 'ner_source': 'ner_oncology_chunk', 'ner_confidence': '0.7887', 'begin': '71', 'chunk_id': 'ebfe618e'}, 
        {'ner_label': 'Imaging_Test', 'sentence': '0', 'chunk': 'CT scan of the abdomen', 'end': '45', 'ner_source': 'ner_oncology_chunk', 'ner_confidence': '0.76256', 'begin': '24', 'chunk_id': 'cbe58cc4'}, 
        {'ner_label': 'Tumor_Finding', 'sentence': '0', 'chunk': 'mass', 'end': '74', 'ner_source': 'ner_oncology_chunk', 'ner_confidence': '0.7887', 'begin': '71', 'chunk_id': 'ebfe618e'}], 
    assertions=[
        {'chunk': 'CT scan of the abdomen', 'assertion_source': 'assertion', 'assertion': 'Past', 'assertion_confidence': '1.0', 'chunk_id': 'cbe58cc4'}, 
        {'chunk': 'mass', 'assertion_source': 'assertion', 'assertion': 'Present', 'assertion_confidence': '0.9986', 'chunk_id': 'ebfe618e'}
      ], 
    resolutions=[], 
    relations=[], 
    summaries=[], 
    deidentifications=[], 
    classifications=[]
}
```

*Result for After Setting Parameters*:

```python
[
    {
        'chunk_id': 'cbe58cc4',
        'chunk': 'CT scan of the abdomen',
        'begin': 24,
        'end': 45,
        'sentence_id': 0,
        'sentence': 'The Patient underwent a CT scan of the abdomen, which showed a complex mass.',
        'ner_label': 'Imaging_Test',
        'ner_source': 'ner_oncology_chunk',
        'ner_confidence': '0.76256',
        'assertion': 'Past',
        'assertion_confidence': '1.0',
        'relations': []
    },
    {
        'chunk_id': 'ebfe618e',
        'chunk': 'mass',
        'begin': 71,
        'end': 74,
        'sentence_id': 0,
        'sentence': 'The Patient underwent a CT scan of the abdomen, which showed a complex mass.',
        'ner_label': 'Tumor_Finding',
        'ner_source': 'ner_oncology_chunk',
        'ner_confidence': '0.7887',
        'assertion': 'Present',
        'assertion_confidence': '0.9986',
        'relations': []
    },
    {
        'chunk_id': 'cbe58cc4',
        'chunk': 'CT scan of the abdomen',
        'begin': 24,
        'end': 45,
        'sentence_id': 0,
        'sentence': 'The Patient underwent a CT scan of the abdomen, which showed a complex mass.',
        'ner_label': 'Imaging_Test',
        'ner_source': 'ner_oncology_chunk',
        'ner_confidence': '0.76256',
        'assertion': 'Past',
        'assertion_confidence': '1.0',
        'relations': []
    },
    {
        'chunk_id': 'ebfe618e',
        'chunk': 'mass',
        'begin': 71,
        'end': 74,
        'sentence_id': 0,
        'sentence': 'The Patient underwent a CT scan of the abdomen, which showed a complex mass.',
        'ner_label': 'Tumor_Finding',
        'ner_source': 'ner_oncology_chunk',
        'ner_confidence': '0.7887',
        'assertion': 'Present',
        'assertion_confidence': '0.9986',
        'relations': []
    }
]
```
Please check the [PipelineTracer and PipelineOutputParser](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.4.PipelineTracer_and_PipelineOutputParser.ipynb) Notebook for more information

</div><div class="h3-box" markdown="1">

####  Customizing Named Entities with Contextual Rules: Enhanced Prefix, Suffix, and Regex Support in `ContextualEntityRuler`

The latest update to `ContextualEntityRuler` introduces `prefixEntities` and `suffixEntities`, refining entity recognition by adjusting chunk information based on surrounding context. Additionally, the new `regexInBetween` parameter enables pattern matching between entities, enhancing accuracy and flexibility in contextual constraints. These improvements allow for more precise entity customization, making `ContextualEntityRuler` a powerful tool for domain-specific text processing.

- This update introduces `prefixEntities` and `suffixEntities` to `ContextualEntityRuler`, allowing entity recognition to be refined based on the surrounding context. These parameters adjust chunk information when specified entities appear before or after the target entity.  
These parameters allow entity recognition based on contextual constraints:
    - `prefixEntities`: Updates chunk information if the specified entities appear before the target entity.
    - `suffixEntities`: Updates chunk information if the specified entities appear after the target entity.

 *Example*:

```python
rules = [  
    {
        "entity": "CONTACT",
        "scopeWindow": [6,6],
        "scopeWindowLevel": "token",
        "prefixEntities": ["LOCATION"],
        "replaceEntity": "ZIP_CODE",
        "mode": "replace_label_only"
    }
]

contextual_entity_ruler = ContextualEntityRuler()\
            .setInputCols("sentence", "token", "ner_chunks")\
            .setOutputCol("ruled_ner_chunks")\
            .setRules(rules)\
            .setCaseSensitive(False)\
            .setDropEmptyChunks(True)\
            .setAllowPunctuationInBetween(False)\
            .setAllowTokensInBetween(True)

text = "Los Angeles, zip code 90001, is located in the South Los Angeles region of the city."
data = spark.createDataFrame([text], StringType()).toDF("text")
```

*Result*:

Before

{:.table-model-big}
| entity   | begin | end | ner_chunks_result  |  
|----------|-------|-----|--------------------|  
| LOCATION | 0     | 10  | Los Angeles        |  
| CONTACT  | 22    | 26  | 90001              |  
| LOCATION | 47    | 63  | South Los Angeles  |  


After

{:.table-model-big}
| entity   | begin | end | ruled_ner_chunks_result | CHANGES                       |  
|----------|-------|-----|-------------------------|-------------------------------|  
| LOCATION | 0     | 10  | Los Angeles             |                               |  
| ZIP_CODE | 22    | 26  | 90001                   | CONTACT updated as ZIP_CODE   |  
| LOCATION | 47    | 63  | South Los Angeles       |                               |  


- Additionally, the `regexInBetween` parameter has been added, enabling pattern matching between entities to enforce contextual constraints. These improvements enhance entity recognition accuracy and flexibility. This parameter allows searching for a regex pattern that occurs between two entities. If the regex pattern matches, the chunk will be updated according to the parameters.

 *Example*:

```python
rules = [  
    {
        "entity": "LOCATION",
        "scopeWindow": [6,6],
        "scopeWindowLevel": "token",
        "regexInBetween": "^zip$",
        "suffixEntities": ["CONTACT", "IDNUM"],
        "replaceEntity": "REPLACED_LOC",
        "mode": "include"
    }
]

contextual_entity_ruler = ContextualEntityRuler() \
    .setInputCols("sentence", "token", "ner_chunks") \
    .setOutputCol("ruled_ner_chunks") \
    .setRules(rules) \
    .setCaseSensitive(False)\
    .setDropEmptyChunks(True)\
    .setAllowPunctuationInBetween(False)\
    .setAllowTokensInBetween(True)

text = "Los Angeles, zip code 90001, is located in the South Los Angeles region of the city."
data = spark.createDataFrame([text], StringType()).toDF("text")
```

*Result*:

- Before:

{:.table-model-big}
| entity   | begin | end | ner_chunks_result  |  
|----------|-------|-----|--------------------|  
| LOCATION | 0     | 10  | Los Angeles        |  
| CONTACT  | 22    | 26  | 90001              |  
| LOCATION | 47    | 63  | South Los Angeles  |  

- After:

{:.table-model-big}
| entity       | begin | end | ruled_ner_chunks_result     | CHANGES                                           |  
|--------------|-------|-----|-----------------------------|---------------------------------------------------|  
| REPLACED_LOC | 0     | 26  | Los Angeles, zip code 90001 | Two entities are merged with the text between them|  
| LOCATION     | 47    | 63  | South Los Angeles           |                                                   |  

Please check the [Contextual Entity Ruler](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/47.Contextual_Entity_Ruler.ipynb) Notebook for more information

</div><div class="h3-box" markdown="1">
	
#### Supporting Overlapping Sentences in Sentence-Aware document Splitting to Feed a Longer and Better Context to Downstream Models

This feature introduces support for overlapping sentences in sentence-aware document splitting, enabling downstream models to process longer and more contextually rich text segments. The `setChunkOverlap` method allows users to define the overlap length between text chunks, improving coherence and continuity in recursive and sentence-based splitting modes.


</div><div class="h3-box" markdown="1">

####  Advanced One-Liner Clinical NLP Pipelines for `Oncological` Document Analysis

We introduce a cutting-edge suite of pretrained NLP pipelines designed to simplify oncological clinical document analysis. Built upon state-of-the-art models, these pipelines efficiently extract oncological entities, determine their assertion status, and establish relationships within clinical texts—all in a seamless, user-friendly manner. By eliminating the complexities of model selection and pipeline construction, this solution enables rapid, accurate insights for oncology research and clinical decision-making.


{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`explain_clinical_doc_oncology_slim`](https://nlp.johnsnowlabs.com/2025/02/06/explain_clinical_doc_oncology_slim_en.html) | This pipeline is designed to extract all oncological entities, assign assertion status to the extracted entities, and establish relations between the extracted entities from the clinical documents. |



*Example*:

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline_sdoh = PretrainedPipeline("explain_clinical_doc_oncology_slim", "en", "clinical/models")

text = """A 56-year-old man presented with a 2-month history of whole-body weakness, double vision, difficulty swallowing, and a 45 mm anterior mediastinal mass detected via chest CT.
Neurological examination and electromyography confirmed a diagnosis of Lambert-Eaton Myasthenic Syndrome (LEMS), associated with anti-P/Q-type VGCC antibodies. The patient was treated with
cisplatin 75 mg/m² on day 1, combined with etoposide 100 mg/m² on days 1-3, repeated every 3 weeks for four cycles. A video-assisted thoracic surgery revealed histopathological features consistent
with small cell lung cancer (SCLC) with lymph node metastases. The immunohistochemical analysis showed positive markers for AE1/AE3, TTF-1, chromogranin A, and synaptophysin. Notably,
a pulmonary nodule in the left upper lobe disappeared, and FDG-PET/CT post-surgery revealed no primary lesions or metastases."""

```

*NER and Assertion Result*:

{:.table-model-big}
|    | chunks                          |begin | end | entities              | assertion|
|---:|:--------------------------------|-----:|----:|:----------------------|:---------|
|  0 | mass                            |  146 | 149 | Tumor_Finding         | Present  |
|  1 | VGCC                            |  317 | 320 | Biomarker             | Present  |
|  2 | cisplatin                       |  363 | 371 | Chemotherapy          | Past     |
|  3 | etoposide                       |  406 | 414 | Chemotherapy          | Present  |
|  4 | for four cycles                 |  462 | 476 | Duration              | Present  |
|  5 | video-assisted thoracic surgery |  481 | 511 | Cancer_Surgery        | Past     |
|  6 | small cell lung cancer          |  565 | 586 | Carcinoma_Type        | Present  |
|  7 | SCLC                            |  589 | 592 | Carcinoma_Type        | Present  |
|  8 | metastases                      |  611 | 620 | Metastasis            | Present  |
|  9 | AE1/AE3                         |  684 | 690 | Biomarker             | Present  |
| 10 | TTF-1                           |  693 | 697 | Biomarker             | Present  |
| 11 | chromogranin A                  |  700 | 713 | Biomarker             | Present  |
| 12 | synaptophysin                   |  720 | 732 | Biomarker             | Present  |
| 13 | nodule                          |  756 | 761 | Tumor_Finding         | Present  |
| 14 | disappeared                     |  786 | 796 | Response_To_Treatment | Present  |
| 15 | primary lesions                 |  839 | 853 | Tumor_Finding         | Absent   |
| 16 | metastases                      |  858 | 867 | Metastasis            | Absent   |


*Relation Extraction Result*:

{:.table-model-big}
| chunk1            | entity1              | chunk2         | entity2       | relation               |confidence |
|:------------------|:---------------------|:---------------|:--------------|:-----------------------|----------:|
| cisplatin         | Chemotherapy         | 75 mg/m²       | Dosage        | Chemotherapy-Dosage    |  1        |
| cisplatin         | Chemotherapy         | day 1          | Cycle_Day     | Chemotherapy-Cycle_Day |  1        |
| cisplatin         | Chemotherapy         | 100 mg/m²      | Dosage        | Chemotherapy-Dosage    |  1        |
| cisplatin         | Chemotherapy         | days 1-3       | Cycle_Day     | Chemotherapy-Cycle_Day |  1        |
| 75 mg/m²          | Dosage               | etoposide      | Chemotherapy  | Dosage-Chemotherapy    |  1        |
| day 1             | Cycle_Day            | etoposide      | Chemotherapy  | Cycle_Day-Chemotherapy |  1        |
| etoposide         | Chemotherapy         | 100 mg/m²      | Dosage        | Chemotherapy-Dosage    |  1        |
| etoposide         | Chemotherapy         | days 1-3       | Cycle_Day     | Chemotherapy-Cycle_Day |  1        |
| 45 mm             | Tumor_Size           | mass           | Tumor_Finding | is_size_of             |  0.97 |
| mediastinal       | Site_Other_Body_Part | mass           | Tumor_Finding | is_location_of         |  0.93 |
| histopathological | Pathology_Test       | SCLC           | Cancer_Dx     | is_finding_of          |  0.74 |
| positive          | Biomarker_Result     | AE1/AE3        | Biomarker     | is_finding_of          |  0.91 |
| positive          | Biomarker_Result     | TTF-1          | Biomarker     | is_finding_of          |  0.90 |
| positive          | Biomarker_Result     | chromogranin A | Biomarker     | is_finding_of          |  0.89 |
| positive          | Biomarker_Result     | synaptophysin  | Biomarker     | is_finding_of          |  0.72 |
| pulmonary         | Site_Lung            | nodule         | Tumor_Finding | is_location_of         |  0.93 |
| nodule            | Tumor_Finding        | upper lobe     | Site_Lung     | is_location_of         |  0.93 |


Please check the [Task Based Clinical Pretrained Pipelines](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.3.Task_Based_Clinical_Pretrained_Pipelines.ipynb) model for more information

</div><div class="h3-box" markdown="1">

#### Introducing The Veterinary MeSH Resolver For Accurately Mapping Veterinary Terms To The Corresponding MeSH Codes

The Veterinary MeSH Resolver is designed to accurately map species-specific terms to MeSH codes in veterinary clinical notes, electronic health records (EHRs), and research articles, improving information retrieval and data analysis. It is especially useful for diagnostics and epidemiological studies, enabling more accurate extraction of disease entities, drug interactions, and treatment outcomes. This makes it an invaluable tool for veterinary informatics and biomedical research.

*Example*:

```python
...

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli",' en',' clinical/models')\
  .setInputCols(["ner_chunk_doc"])\
  .setOutputCol("sbert_embeddings")\
  .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_mesh_veterinary", "en", "clinical/models") \
  .setInputCols(["sbert_embeddings"]) \
  .setOutputCol("mesh_code")\
  .setDistanceFunction("EUCLIDEAN")

sample_text = "The dog is a labrador retriever, 4-year-old, it was brought in with vomiting and diarrhea for the past 2 days. A preliminary diagnosis of canine parvovirus infection was made, and supportive care was recommended. The owner was advised on isolation precautions to prevent the spread of the virus."
```
*Result*:

{:.table-model-big}
|chunk|begin|end|ner_label|resolution|description|all_k_results|all_k_resolutions|
|-----|-----|---|---------|----------|-----------|-------------|-----------------|
|vomiting|   68| 75|  PROBLEM|   C536228|  periodic vomiting| C536228:::C007262:::C080875...| periodic vomiting:::vomitoxin:::mirage:::propargite:::ena...|
|diarrhea|   81| 88|  PROBLEM|   C565627| diarrhea, syndromic| C565627:::C564019:::C531700...| diarrhea, syndromic:::diarrhea, chronic, with villous atr...|
|canine parvovirus infection|  138|164|  PROBLEM|   D017993|  canine parvovirus| D017993:::D052660:::D028323...| canine parvovirus:::bovine parvovirus:::porcine parvoviru...|
|the virus|  285|293|  PROBLEM|   D014780|              virus| D014780:::D006678:::D006476...| virus:::aids virus:::andes virus:::virus, associated:::pr...|

</div><div class="h3-box" markdown="1">


#### New Spanish Medical Entity Resolver for SNOMED Mapping

This model maps Spanish medical entities and concepts to SNOMED codes using the `sent_xlm_roberta_biolord_2023_m` sentence embeddings. It leverages a specialized resolver to accurately link medical terms to SNOMED terminologies, ensuring precise medical coding. 

*Example*:

```python
biolord_embeddings = XlmRoBertaSentenceEmbeddings.pretrained("sent_xlm_roberta_biolord_2023_m", "xx")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("biolord_embeddings")

snomed_resolver = SentenceEntityResolverModel\
    .pretrained("biolordresolve_snomed_augmented", "es", "clinical/models") \
    .setInputCols(["biolord_embeddings"]) \
    .setOutputCol("snomed_code")\
    .setDistanceFunction("EUCLIDEAN")

clinical_note = ("La paciente, con antecedente de diabetes mellitus gestacional evolucionada a tipo 2 y obesidad, presenta vómitos de una semana de evolución junto con dolorosa inflamación de sínfisis de pubis que dificulta la deambulación.")
```

*Result*:

{:.table-model-big}
| ner_chunk                     | entity             |snomed_code | resolutions                                                   | all_codes                                | all_resolutions                                                   |
|:------------------------------|:-------------------|-----------:|:--------------------------------------------------------------|:-----------------------------------------|:------------------------------------------------------------------|
| diabetes mellitus gestacional | clinical_condition |   11687002 | diabetes mellitus gestacional [diabetes mellitus gestacional] | ['11687002', '40801000119106', '168964...| ['diabetes mellitus gestacional [diabetes mellitus gestacional]...|
| obesidad                      | clinical_condition |  414916001 | obesidad [obesidad]                                           | ['414916001', '414915002', '271590003'...| ['obesidad [obesidad]', 'obeso [obeso]', 'constitución obesa [c...|
| vómitos                       | clinical_condition |  422400008 | vómitos [vómitos]                                             | ['422400008', '249497008', '23971007',...| ['vómitos [vómitos]', 'síntoma de vómito [síntoma de vómito]', ...|
| dolorosa                      | clinical_condition |   71393004 | dolorimiento [dolorimiento]                                   | ['71393004', '22253000', '301371003', ...| ['dolorimiento [dolorimiento]', 'dolor [dolor]', 'dolor que cor...|
| inflamación                   | clinical_condition |  128139000 | enfermedad inflamatoria [enfermedad inflamatoria]             | ['128139000', '409774005', '4532008', ...| ['enfermedad inflamatoria [enfermedad inflamatoria]', 'morfolog...|


</div><div class="h3-box" markdown="1">
	
#### New Blog Posts On Various Topics

Dive into our latest blog series exploring cutting-edge advancements in healthcare NLP. The integration of **Natural Language Processing (NLP) and Large Language Models (LLMs)** is transforming healthcare by extracting critical insights from unstructured clinical text. From enhancing **genomic research and precision medicine** to revolutionizing **oncology case analysis**, these AI-driven tools enable faster, more accurate decision-making. Additionally, ensuring **GDPR-compliant de-identification** and detecting **dataset shifts in PHI data** are crucial for maintaining data security and model performance over time.  

- [Extracting Key Entities in Clinical Text for Enhanced Genomic Research and Precision Medicine](https://medium.com/john-snow-labs/extracting-key-entities-in-clinical-text-for-enhanced-genomic-research-and-precision-medicine-06024d7838a5) This blog post explores how John Snow Labs’ Healthcare NLP & LLM library can be used to extract genes and phenotypes from clinical text. By leveraging NLP techniques, we can transform unstructured medical data into actionable insights, enabling more efficient genetic research, clinical diagnostics, and personalized medicine. The blog covers the key steps in training NER and assertion status detection models for this task, including data preparation, annotation, and evaluation, and highlights real-world use cases where extracting genetic and phenotypic entities enhances precision in clinical decision-making.
- [AI-Powered Oncology: Healthcare NLP’s Role in Cancer Research and Treatment](https://medium.com/john-snow-labs/ai-powered-oncology-healthcare-nlps-role-in-cancer-research-and-treatment-1deaf41b74b2) This blog post explores how John Snow Labs’ Healthcare NLP & LLM library revolutionizes oncology case analysis by extracting actionable insights from clinical text. Key use cases include detecting valuable information using NER, assertion status, relation extraction, and ICD-10 mapping models; summarizing reports and enabling Q&A with LLMs; and leveraging zero-shot NER for identifying new entities with minimal effort. These approaches streamline oncology data analysis, enhance decision-making, and improve patient outcomes.
- [De-Identification of German Medical Text for GDPR Compliance](https://medium.com/john-snow-labs/de-identification-of-german-medical-text-for-gdpr-compliance-eee377b4398b) This blog post explores how specialized de-identification pipelines ensure GDPR compliance and protect patient privacy in German clinical texts. By leveraging advanced NLP techniques such as masking, entity replacement, and context-aware obfuscation, these pipelines anonymize names, dates, and locations while preserving data usability. The blog highlights key challenges posed by complex linguistic structures and high-density personal data.
- [Detecting a Dataset Shift in PHI Data to Ensure De-IDentification Model Performance on Future Data](https://www.johnsnowlabs.com/detecting-a-dataset-shift-in-phi-data-to-ensure-de-identification-model-performance-on-future-data/) This blog post explores how PHI detection models must adapt to evolving clinical data, as dataset shifts—such as changes in document types, patient populations, or medical contexts—can impact performance.



</div><div class="h3-box" markdown="1">

#### Various Core Improvements: Bug Fixes, Enhanced Overall Robustness, and Reliability of Spark NLP for Healthcare

- Fixed broken `encodeModel` and `setInputSuffix` functions in `LLMLoader`
- Fixed end index issue in `AssertionChunkConverter`


</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For making Spark NLP For Healthcare Easier To Navigate And Understand

- New [Deidentification_Performance_Comparison_Of_Healthcare_NLP_VS_Cloud_Solutions](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/academic/Deidentification_Performance_Comparison_Of_Healthcare_NLP_VS_Cloud_Solutions.ipynb) Notebook
- Updated [Loading Medical and Open-Souce LLMs](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.Loading_Medical_and_Open-Souce_LLMs.ipynb) Notebook
- Updated [Contextual_Entity_Ruler](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/47.Contextual_Entity_Ruler.ipynb) Notebook
- Updated [Clinical Deidentification for Structured Data](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.8.Clinical_Deidentification_for_Structured_Data.ipynb) Notebook
- Updated [PipelineTracer and PipelineOutputParser](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.4.PipelineTracer_and_PipelineOutputParser.ipynb) Notebook

</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.

+ `explain_clinical_doc_oncology_slim`    
+ `biolordresolve_snomed_augmented`
+ `sbiobertresolve_mesh`
+ `sbiobertresolve_mesh_augmented`
+ `sbiobertresolve_mesh_veterinary`


</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">




## Versions

</div>
{%- include docs-healthcare-pagination.html -%}
