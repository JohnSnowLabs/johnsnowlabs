---
layout: model
title: Sentence Entity Resolver for ICD10-CM (Augmented)
author: John Snow Labs
name: sbertresolve_icd10cm_augmented
date: 2023-05-24
tags: [en, clinical, licensed, icd10cm, entity_resolution]
task: Entity Resolution
language: en
edition: Healthcare NLP 4.4.2
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps extracted medical entities to ICD-10-CM codes using `sbert_jsl_medium_uncased`. Also, it has been augmented with synonyms for making it more accurate.

## Predicted Entities

`ICD10CM Codes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbertresolve_icd10cm_augmented_en_4.4.2_3.0_1684961214137.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbertresolve_icd10cm_augmented_en_4.4.2_3.0_1684961214137.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverter()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(['PROBLEM'])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

bert_embeddings = BertSentenceEmbeddings.pretrained("sbert_jsl_medium_uncased", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bert_embeddings")\
    .setCaseSensitive(False)

icd10_resolver = SentenceEntityResolverModel.pretrained("sbertresolve_icd10cm_augmented", "en", "clinical/models") \
    .setInputCols(["bert_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

nlpPipeline = Pipeline(stages=[document_assembler, 
                               sentence_detector, 
                               tokenizer, 
                               word_embeddings, 
                               clinical_ner, 
                               ner_converter, 
                               chunk2doc, 
                               bert_embeddings, 
                               icd10_resolver])

data_ner = spark.createDataFrame([["A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with acute hepatitis, and obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection."]]).toDF("text")

results = nlpPipeline.fit(data_ner).transform(data_ner)
```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence","token"))
    .setOutputCol("embeddings")

val clinical_ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence","token","embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverter()
    .setInputCols(Array("sentence","token","ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList("PROBLEM")

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val bert_embeddings = BertSentenceEmbeddings.pretrained("sbert_jsl_medium_uncased", "en", "clinical/models")
    .setInputCols("ner_chunk_doc")
    .setOutputCol("bert_embeddings")
    .setCaseSensitive(False)

val icd10_resolver = SentenceEntityResolverModel.pretrained("sbertresolve_icd10cm_augmented", "en", "clinical/models")
    .setInputCols("bert_embeddings")
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(document_assembler, sentence_detector, tokenizer, word_embeddings, clinical_ner, ner_converter, chunk2doc, sbert_embedder, icd10_resolver))

val data = Seq("A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with acute hepatitis, and obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection.").toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
| ner_chunk                             | entity   | icd10_code   | all_codes                                                                           | resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|:--------------------------------------|:---------|:-------------|:------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| gestational diabetes mellitus         | PROBLEM  | O24.4        | O24.4:::O24.41:::O24.43:::Z86.32:::K86.8:::P70.2:::O24.434:::E10.9                  | gestational diabetes mellitus [gestational diabetes mellitus]:::gestational diabetes mellitus [gestational diabetes mellitus]:::gestational diabetes mellitus in the puerperium [gestational diabetes mellitus in the puerperium]:::history of gestational diabetes mellitus [history of gestational diabetes mellitus]:::secondary pancreatic diabetes mellitus [secondary pancreatic diabetes mellitus]:::neonatal diabetes mellitus [neonatal diabetes mellitus]:::gestational diabetes mellitus in the puerperium, insulin controlled [gestational diabetes mellitus in the puerperium, insulin controlled]:::juvenile onset diabetes mellitus [juvenile onset diabetes mellitus]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| subsequent type two diabetes mellitus | PROBLEM  | E11          | E11:::E11.9:::E10.9:::E10:::E13.9:::Z83.3:::L83:::E11.8:::E11.32:::E10.8:::Z86.39   | type 2 diabetes mellitus [type 2 diabetes mellitus]:::type ii diabetes mellitus [type ii diabetes mellitus]:::type i diabetes mellitus [type i diabetes mellitus]:::type 1 diabetes mellitus [type 1 diabetes mellitus]:::secondary diabetes mellitus [secondary diabetes mellitus]:::fh: diabetes mellitus [fh: diabetes mellitus]:::type 2 diabetes mellitus with acanthosis nigricans [type 2 diabetes mellitus with acanthosis nigricans]:::complication of type ii diabetes mellitus [complication of type ii diabetes mellitus]:::secondary endocrine diabetes mellitus [secondary endocrine diabetes mellitus]:::complication of type i diabetes mellitus [complication of type i diabetes mellitus]:::history of diabetes mellitus type ii [history of diabetes mellitus type ii]:::pregnancy and type 2 diabetes mellitus [pregnancy and type 2 diabetes mellitus]:::type 2 diabetes mellitus with ophthalmic complications [type 2 diabetes mellitus with ophthalmic complications]:::proteinuria due to type 2 diabetes mellitus [proteinuria due to type 2 diabetes mellitus]:::type 2 diabetes mellitus with hyperglycemia [type 2 diabetes mellitus with hyperglycemia]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| drug-induced pancreatitis             | PROBLEM  | F10.2        | F10.2:::K85.3:::M79.3:::T46.5X:::K29.6:::T50.90:::J98.5:::K85.20:::T36.95:::K85.32  | drug-induced chronic pancreatitis [drug-induced chronic pancreatitis]:::drug-induced acute pancreatitis [drug-induced acute pancreatitis]:::drug-induced panniculitis [drug-induced panniculitis]:::drug-induced pericarditis [drug-induced pericarditis]:::drug-induced gastritis [drug-induced gastritis]:::drug-induced dermatomyositis [drug-induced dermatomyositis]:::drug-induced granulomatous mediastinitis [drug-induced granulomatous mediastinitis]:::alcohol-induced pancreatitis [alcohol-induced pancreatitis]:::drug-induced colitis [drug-induced colitis]:::drug induced acute pancreatitis with infected necrosis [drug induced acute pancreatitis with infected necrosis]', 'drug-induced pneumonitis [drug-induced pneumonitis]:::rbn - retrobulbar neuritis [rbn - retrobulbar neuritis]:::drug induced pneumonitis [drug induced pneumonitis]:::infective endocarditis at site of patch of interatrial communication (disorder) [infective endocarditis at site of patch of interatrial communication (disorder)]:::infective endocarditis at site of interatrial communication (disorder) [infective endocarditis at site of interatrial communication (disorder)]:::post-ercp acute pancreatitis (disorder) [post-ercp acute pancreatitis (disorder)]:::dm - dermatomyositis [dm - dermatomyositis]:::drug-induced pericarditis (disorder) [drug-induced pericarditis (disorder)]:::alcohol-induced chronic pancreatitis [alcohol-induced chronic pancreatitis]                                                                                                                                                                                                                                                                         |
| acute hepatitis                       | PROBLEM  | K72.0        | K72.0:::B15:::B17.2:::B17.10:::B17.1:::B16:::B17.9:::B18.8                          | acute hepatitis [acute hepatitis]:::acute hepatitis a [acute hepatitis a]:::acute hepatitis e [acute hepatitis e]:::acute hepatitis c [acute hepatitis c]:::acute hepatitis c [acute hepatitis c]:::acute hepatitis b [acute hepatitis b]:::acute viral hepatitis [acute viral hepatitis]:::chronic hepatitis e [chronic hepatitis e]:::acute type a viral hepatitis [acute type a viral hepatitis]:::acute focal hepatitis [acute focal hepatitis]:::chronic hepatitis [chronic hepatitis]:::acute type b viral hepatitis [acute type b viral hepatitis]:::hepatitis a [hepatitis a]:::chronic hepatitis c [chronic hepatitis c]:::hepatitis [hepatitis]:::ischemic hepatitis [ischemic hepatitis]:::chronic viral hepatitis [chronic viral hepatitis]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| obesity                               | PROBLEM  | E66.9        | E66.9:::E66.8:::P90:::Q13.0:::M79.4:::Z86.39                                        | obesity [obesity]:::upper body obesity [upper body obesity]:::childhood obesity [childhood obesity]:::central obesity [central obesity]:::localised obesity [localised obesity]:::history of obesity [history of obesity]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |    
| a body mass index                     | PROBLEM  | E66.9        | E66.9:::Z68.41:::Z68:::E66.8:::Z68.45:::Z68.4:::Z68.1:::Z68.2                       | observation of body mass index [observation of body mass index]:::finding of body mass index [finding of body mass index]:::body mass index [bmi] [body mass index [bmi]]:::body mass index equal to or greater than 40 [body mass index equal to or greater than 40]:::body mass index [bmi] 70 or greater, adult [body mass index [bmi] 70 or greater, adult]:::body mass index [bmi] 40 or greater, adult [body mass index [bmi] 40 or greater, adult]:::body mass index [bmi] 19.9 or less, adult [body mass index [bmi] 19.9 or less, adult]:::body mass index [bmi] 20-29, adult [body mass index [bmi] 20-29, adult]:::mass of body region [mass of body region]:::body mass index [bmi] 22.0-22.9, adult [body mass index [bmi] 22.0-22.9, adult]:::body mass index [bmi] 21.0-21.9, adult [body mass index [bmi] 21.0-21.9, adult]:::body mass index [bmi] 25.0-25.9, adult [body mass index [bmi] 25.0-25.9, adult]:::body mass index [bmi] 50.0-59.9, adult [body mass index [bmi] 50.0-59.9, adult]:::body mass index [bmi] 20.0-20.9, adult [body mass index [bmi] 20.0-20.9, adult]:::body mass index [bmi] 26.0-26.9, adult [body mass index [bmi] 26.0-26.9, adult]:::body mass index [bmi] 31.0-31.9, adult [body mass index [bmi] 31.0-31.9, adult]:::body mass index [bmi] 45.0-49.9, adult [body mass index [bmi] 45.0-49.9, adult]:::body mass index [bmi] 29.0-29.9, adult [body mass index [bmi] 29.0-29.9, adult]:::defined border of mass of abdomen [defined border of mass of abdomen]:::body mass index [bmi] 24.0-24.9, adult [body mass index [bmi] 24.0-24.9, adult]:::subcutaneous mass of head (finding) [subcutaneous mass of head (finding)]:::mass of thoracic structure (finding) [mass of thoracic structure (finding)]    |
| polyuria                              | PROBLEM  | R35          | R35:::E88.8:::R30.0:::N28.89:::O04.8:::R82.4:::E74.8:::R82.2                        | polyuria [polyuria]:::sialuria [sialuria]:::stranguria [stranguria]:::isosthenuria [isosthenuria]:::oliguria [oliguria]:::ketonuria [ketonuria]:::xylosuria [xylosuria]:::biliuria [biliuria]:::sucrosuria [sucrosuria]:::chyluria [chyluria]:::anuria [anuria]:::pollakiuria [pollakiuria]:::podocyturia [podocyturia]:::galactosuria [galactosuria]:::proteinuria [proteinuria]:::other polyuria [other polyuria]:::other polyuria [other polyuria]:::alcaptonuria [alcaptonuria]:::xanthinuria [xanthinuria]:::oliguria and anuria [oliguria and anuria]:::hawkinsinuria [hawkinsinuria]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| polydipsia                            | PROBLEM  | R63.1        | R63.1:::Q17.0:::Q89.4:::Q89.09:::Q74.8:::H53.8:::H53.2:::Q13.2                      | polydipsia [polydipsia]:::polyotia [polyotia]:::polysomia [polysomia]:::polysplenia [polysplenia]:::polymelia [polymelia]:::palinopsia [palinopsia]:::polyopia [polyopia]:::polycoria [polycoria]:::adipsia [adipsia]:::primary polydipsia [primary polydipsia]:::chromatopsia [chromatopsia]:::polyphasic units [polyphasic units]:::duodenal polyp [duodenal polyp]:::polymicrogyria [polymicrogyria]:::polygalactia [polygalactia]:::otic polyp [otic polyp]:::pseudochondroplasia [pseudochondroplasia]:::polythelia [polythelia]:::polymyositis [polymyositis]:::juvenile polyps of large bowel [juvenile polyps of large bowel]:::syndactylia [syndactylia]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| poor appetite                         | PROBLEM  | R63.0        | R63.0:::R63.2:::P92.9:::R45.81:::Z55.8:::R41.84:::R41.3:::Z74.8                     | poor appetite [poor appetite]:::excessive appetite [excessive appetite]:::poor feeding [poor feeding]:::poor self-esteem [poor self-esteem]:::poor education [poor education]:::poor concentration [poor concentration]', 'poor memory [poor memory]:::poor informal care arrangements (finding) [poor informal care arrangements (finding)]:::poor attention control [poor attention control]:::poor self-esteem (finding) [poor self-esteem (finding)]:::trouble eating [trouble eating]:::poor daily routine (finding) [poor daily routine (finding)]:::poor manual dexterity [poor manual dexterity]:::poor family relationship (finding) [poor family relationship (finding)]:::inadequate psyllium intake (finding) [inadequate psyllium intake (finding)]:::poor work record [poor work record]:::diet poor [diet poor]:::poor historian [poor historian]:::inadequate copper intake [inadequate copper intake]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| vomiting                              | PROBLEM  | R11.1        | R11.1:::K91.0:::K92.0:::A08.39:::R11:::P92.0:::P92.09:::R11.12                      | vomiting [vomiting]:::vomiting bile [vomiting bile]:::vomiting blood [vomiting blood]:::viral vomiting [viral vomiting]:::vomiting (disorder) [vomiting (disorder)]:::vomiting of newborn [vomiting of newborn]:::vomiting in newborn (disorder) [vomiting in newborn (disorder)]:::projectile vomiting [projectile vomiting]:::morning vomiting (disorder) [morning vomiting (disorder)]:::vomiting of pregnancy [vomiting of pregnancy]:::habit vomiting (disorder) [habit vomiting (disorder)]:::periodic vomiting [periodic vomiting]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| a respiratory tract infection         | PROBLEM  | J98.8        | J98.8:::J06.9:::P39.3:::J22:::N39.0:::A49.9:::Z59.3:::T83.51                        | respiratory tract infection [respiratory tract infection]:::upper respiratory tract infection [upper respiratory tract infection]:::urinary tract infection [urinary tract infection]:::lrti - lower respiratory tract infection [lrti - lower respiratory tract infection]', 'uti - urinary tract infection [uti - urinary tract infection]:::bacterial respiratory infection [bacterial respiratory infection]:::institution-acquired respiratory infection [institution-acquired respiratory infection]:::catheter-associated urinary tract infection [catheter-associated urinary tract infection]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbertresolve_icd10cm_augmented|
|Compatibility:|Healthcare NLP 4.4.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bert_embeddings]|
|Output Labels:|[icd10cm_code]|
|Language:|en|
|Size:|1.0 GB|
|Case sensitive:|false|
