---
layout: model
title: Pipeline for National Cancer Institute Thesaurus (NCIt) Sentence Entity Resolver
author: John Snow Labs
name: ncit_resolver_pipeline
date: 2024-02-01
tags: [licensed, en, entity_resolution, clinical, pipeline, ncit]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This advanced pipeline extracts oncological entities from clinical texts and utilizes the `sbiobert_base_cased_mli` Sentence Bert Embeddings to map these entities to their corresponding National Cancer Institute Thesaurus (NCIt) codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ncit_resolver_pipeline_en_5.2.1_3.2_1706795236984.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ncit_resolver_pipeline_en_5.2.1_3.2_1706795236984.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ncit_resolver_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""A 65-year-old woman had a history of debulking surgery, bilateral oophorectomy with omentectomy, total hysterectomy with radical pelvic lymph nodes dissection due to ovarian carcinoma (mucinous-type carcinoma, stage Ic) 1 year ago. Patient's medical compliance was poor and failed to complete her chemotherapy (cyclophosphamide 750 mg/m2, carboplatin 300 mg/m2). Recently, she noted a palpable right breast mass, 15 cm in size which nearly occupied the whole right breast in 2 months. Core needle biopsy revealed metaplastic carcinoma.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ncit_resolver_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""A 65-year-old woman had a history of debulking surgery, bilateral oophorectomy with omentectomy, total hysterectomy with radical pelvic lymph nodes dissection due to ovarian carcinoma (mucinous-type carcinoma, stage Ic) 1 year ago. Patient's medical compliance was poor and failed to complete her chemotherapy (cyclophosphamide 750 mg/m2, carboplatin 300 mg/m2). Recently, she noted a palpable right breast mass, 15 cm in size which nearly occupied the whole right breast in 2 months. Core needle biopsy revealed metaplastic carcinoma.""")

```
</div>

## Results

```bash
+-------------------------------------+-----+---+-----------------+----------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                                chunk|begin|end|        ner_label|NCI-t Code|                                                 description|                                                 resolutions|                                                   all_codes|
+-------------------------------------+-----+---+-----------------+----------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                    debulking surgery|   37| 53|   Cancer_Surgery|    C15749|                       debulking surgery [debulking surgery]|debulking surgery [debulking surgery]:::primary debulking...|C15749:::C160865:::C160866:::C128096:::C146855:::C158758:...|
|               bilateral oophorectomy|   56| 77|   Cancer_Surgery|    C51590|             bilateral oophorectomy [bilateral oophorectomy]|bilateral oophorectomy [bilateral oophorectomy]:::oophore...|C51590:::C15291:::C51601:::C51765:::C29893:::C15323:::C49...|
|                          omentectomy|   84| 94|   Cancer_Surgery|    C51787|                                   omentectomy [omentectomy]|omentectomy [omentectomy]:::partial omentectomy [partial ...|C51787:::C51788:::C51596:::C15277:::C51780:::C96171:::C94...|
|                   total hysterectomy|   97|114|   Cancer_Surgery|    C15701|                     total hysterectomy [total hysterectomy]|total hysterectomy [total hysterectomy]:::total abdominal...|C15701:::C51695:::C40961:::C51941:::C51660:::C15256:::C15...|
|radical pelvic lymph nodes dissection|  121|157|   Cancer_Surgery|    C48936|radical lymph node dissection [radical lymph node dissect...|radical lymph node dissection [radical lymph node dissect...|C48936:::C166163:::C51896:::C48184:::C167218:::C166225:::...|
|                    ovarian carcinoma|  166|182|        Cancer_Dx|     C4908|                       ovarian carcinoma [ovarian carcinoma]|ovarian carcinoma [ovarian carcinoma]:::ovarian adenocarc...|C4908:::C7700:::C7550:::C4509:::C9192:::C5229:::C7832:::C...|
|                        mucinous-type|  185|197|Histological_Type|    C38768|         mucinous differentiation [mucinous differentiation]|mucinous differentiation [mucinous differentiation]:::muc...|C38768:::C14163:::C246:::C16883:::C36119:::C13259:::C7472...|
|                            carcinoma|  199|207|        Cancer_Dx|     C2916|                                       carcinoma [carcinoma]|carcinoma [carcinoma]:::carcinoma cell [carcinoma cell]::...|C2916:::C36779:::C3693:::C165723:::C26712:::C2915:::C7629...|
|                             stage Ic|  210|217|          Staging|    C27981|                                         stage ic [stage ic]|stage ic [stage ic]:::stage iv [stage iv]:::stage i [stag...|C27981:::C125478:::C112007:::C141199:::C28055:::C112012::...|
|                         chemotherapy|  297|308|     Chemotherapy|    C15632|                                 chemotherapy [chemotherapy]|chemotherapy [chemotherapy]:::chemotherapy received [chem...|C15632:::C160336:::C168835:::C274:::C15681:::C191:::C1588...|
|                     cyclophosphamide|  311|326|     Chemotherapy|      C405|                         cyclophosphamide [cyclophosphamide]|cyclophosphamide [cyclophosphamide]:::cyclophosphamide re...|C405:::C160014:::C11393:::C9667:::C37699:::C9713:::C11510...|
|                          carboplatin|  339|349|     Chemotherapy|     C1282|                                   carboplatin [carboplatin]|carboplatin [carboplatin]:::carboplatin regimen [carbopla...|C1282:::C160006:::C11881:::C376:::C175820:::C156262:::C97...|
|                                right|  394|398|        Direction|   C160199|                                               right [right]|right [right]:::correct [correct]:::definite [definite]::...|C160199:::C68815:::C190978:::C107561:::C137949:::C118396:...|
|                               breast|  400|405|      Site_Breast|    C12971|                                             breast [breast]|breast [breast]:::breast part [breast part]:::breast ln [...|C12971:::C13020:::C27939:::C93291:::C141134:::C12370:::C9...|
|                                 mass|  407|410|    Tumor_Finding|   C126027|                                                 mass [mass]|mass [mass]:::mass content [mass content]:::mass density ...|C126027:::C191347:::C75762:::C179798:::C48528:::C179799::...|
|                                right|  459|463|        Direction|   C160199|                                               right [right]|right [right]:::correct [correct]:::definite [definite]::...|C160199:::C68815:::C190978:::C107561:::C137949:::C118396:...|
|                               breast|  465|470|      Site_Breast|    C12971|                                             breast [breast]|breast [breast]:::breast part [breast part]:::breast ln [...|C12971:::C13020:::C27939:::C93291:::C141134:::C12370:::C9...|
|                   Core needle biopsy|  485|502|   Pathology_Test|    C15680|                     core needle biopsy [core needle biopsy]|core needle biopsy [core needle biopsy]:::needle biopsy [...|C15680:::C15190:::C51763:::C91832:::C15361:::C137909:::C1...|
|                          metaplastic|  513|523|Histological_Type|    C25566|                                   metaplastic [metaplastic]|metaplastic [metaplastic]:::metaplastic change [metaplast...|C25566:::C3236:::C36786:::C177595:::C80354:::C29745:::C45...|
|                            carcinoma|  525|533|        Cancer_Dx|     C2916|                                       carcinoma [carcinoma]|carcinoma [carcinoma]:::carcinoma cell [carcinoma cell]::...|C2916:::C36779:::C3693:::C165723:::C26712:::C2915:::C7629...|
+-------------------------------------+-----+---+-----------------+----------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ncit_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.6 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
