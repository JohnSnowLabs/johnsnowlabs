---
layout: model
title: Sentence Entity Resolver for NCI-t
author: John Snow Labs
name: sbiobertresolve_ncit
date: 2023-03-26
tags: [entity_resolution, clinical, en, licensed, ncit]
task: Entity Resolution
language: en
edition: Healthcare NLP 4.3.2
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps extracted medical entities related to clinical care, translational and basic research, public information and administrative activities to NCI-t codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings.

## Predicted Entities

`NCI-t codes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_ncit_en_4.3.2_3.0_1679843528109.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_ncit_en_4.3.2_3.0_1679843528109.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = DocumentAssembler()\
		.setInputCol("text")\
		.setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models") \
		.setInputCols(["document"]) \
		.setOutputCol("sentence")

tokenizer = Tokenizer()\
		.setInputCols(["sentence"])\
		.setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
		.setInputCols(["sentence", "token"])\
		.setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_oncology", "en", "clinical/models") \
		.setInputCols(["sentence", "token", "embeddings"]) \
		.setOutputCol("ner")

ner_converter = NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")\
    .setPreservePosition(False)\
    .setBlackList(["Age",
                   "Date",
                   "Death_Entity",
                   "Gender",
                   "Race_Ethnicity",
                   "Relative_Date",
                   "Smoking_Status",
                   "Dosage",
                   "Tumor_Size"
                   ])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_ncit","en", "clinical/models") \
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")


pipeline = Pipeline(stages=[document_assembler,
                               sentence_detector,
                               tokenizer,
                               word_embeddings,
                               ner_model,
                               ner_converter,
                               chunk2doc,
                               sbert_embedder,
                               resolver])

data = spark.createDataFrame([["A 65-year-old woman had a history of debulking surgery, bilateral oophorectomy with omentectomy, total hysterectomy with radical pelvic lymph nodes dissection due to ovarian carcinoma (mucinous-type carcinoma, stage Ic) 1 year ago. Patient's medical compliance was poor and failed to complete her chemotherapy (cyclophosphamide 750 mg/m2, carboplatin 300 mg/m2). Recently, she noted a palpable right breast mass, 15 cm in size which nearly occupied the whole right breast in 2 months. Core needle biopsy revealed metaplastic carcinoma."]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
	.setInputCol("text")
	.setOutputCol("document")
	
val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
	.setInputCols(Array("document"))
	.setOutputCol("sentence")
	
val tokenizer = new Tokenizer()
	.setInputCols(Array("sentence"))
	.setOutputCol("token")
	
val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
	.setInputCols(Array("sentence","token"))
	.setOutputCol("embeddings")
	
val ner_model = MedicalNerModel.pretrained("ner_oncology","en","clinical/models")
	.setInputCols(Array("sentence","token","embeddings"))
	.setOutputCol("ner")
	
val ner_converter = new NerConverterInternal()
	.setInputCols(Array("sentence","token","ner"))
	.setOutputCol("ner_chunk")
	.setPreservePosition(false)
	.setBlackList(Array(
     "Age", 
     "Date", 
     "Death_Entity", 
     "Gender", 
     "Race_Ethnicity", 
     "Relative_Date", 
     "Smoking_Status",
     "Dosage",
     "Tumor_Size"))
	
val chunk2doc = new Chunk2Doc()
	.setInputCols("ner_chunk")
	.setOutputCol("ner_chunk_doc")
	
val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
	.setInputCols(Array("ner_chunk_doc"))
	.setOutputCol("sbert_embeddings")
	.setCaseSensitive(false)
	
val resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_ncit","en","clinical/models")
	.setInputCols(Array("sbert_embeddings"))
	.setOutputCol("resolution")
	.setDistanceFunction("EUCLIDEAN")
	
val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector, 
    tokenizer, 
    word_embeddings, 
    ner_model, 
    ner_converter,
    chunk2doc, 
    sbert_embedder, 
    resolver))
	
val data = Seq("A 65-year-old woman had a history of debulking surgery, bilateral oophorectomy with omentectomy, total hysterectomy with radical pelvic lymph nodes dissection due to ovarian carcinoma (mucinous-type carcinoma, stage Ic) 1 year ago. Patient's medical compliance was poor and failed to complete her chemotherapy (cyclophosphamide 750 mg/m2, carboplatin 300 mg/m2). Recently, she noted a palpable right breast mass, 15 cm in size which nearly occupied the whole right breast in 2 months. Core needle biopsy revealed metaplastic carcinoma.") .toDF("text")
	
val result = pipeline.fit(data) .transform(data)
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
|Model Name:|sbiobertresolve_ncit|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[nci-t_code]|
|Language:|en|
|Size:|1.5 GB|
|Case sensitive:|false|

## References

https://evs.nci.nih.gov/ftp1/NCI_Thesaurus/
