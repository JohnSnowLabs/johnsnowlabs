---
layout: model
title: Sentence Entity Resolver for ICD10-CM (Augmented)
author: John Snow Labs
name: sbertresolve_icd10cm_augmented
date: 2023-05-30
tags: [licensed, en, icd10cm, entity_resolution]
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

This model maps extracted medical entities to ICD-10-CM codes using `sbert_jsl_medium_uncased` Sentence Bert Embeddings. Also, it has been augmented with synonyms for making it more accurate.

## Predicted Entities

`ICD10CM Codes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbertresolve_icd10cm_augmented_en_4.4.2_3.0_1685420954806.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbertresolve_icd10cm_augmented_en_4.4.2_3.0_1685420954806.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
| ner_chunk                             | entity   | icd10_code   | all_codes                                                                                                                                                                                                        | resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:--------------------------------------|:---------|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| gestational diabetes mellitus         | PROBLEM  | O24.4        | O24.4:::O24.41:::O24.43:::Z86.32:::K86.8:::P70.2:::O24.434:::E10.9                                                                                                                                               | gestational diabetes mellitus [gestational diabetes mellitus]:::gestational diabetes mellitus [gestational diabetes mellitus in pregnancy]:::gestational diabetes mellitus in the puerperium [gestational diabetes mellitus in the puerperium]:::history of gestational diabetes mellitus [personal history of gestational diabetes]:::secondary pancreatic diabetes mellitus [other specified diseases of pancreas]:::neonatal diabetes mellitus [neonatal diabetes mellitus]:::gestational diabetes mellitus in the puerperium, insulin controlled [gestational diabetes mellitus in the puerperium, insulin controlled]:::juvenile onset diabetes mellitus [type 1 diabetes mellitus without complications]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| subsequent type two diabetes mellitus | PROBLEM  | E11          | E11:::E11.9:::E10.9:::E10:::E13.9:::Z83.3:::L83:::E11.8:::E11.32:::E10.8:::Z86.39:::O24.11:::E11.3:::E11.2:::E11.65                                                                                              | type 2 diabetes mellitus [type 2 diabetes mellitus]:::type ii diabetes mellitus [type 2 diabetes mellitus without complications]:::type i diabetes mellitus [type 1 diabetes mellitus without complications]:::type 1 diabetes mellitus [type 1 diabetes mellitus]:::secondary diabetes mellitus [other specified diabetes mellitus without complications]:::fh: diabetes mellitus [family history of diabetes mellitus]:::type 2 diabetes mellitus with acanthosis nigricans [acanthosis nigricans]:::complication of type ii diabetes mellitus [type 2 diabetes mellitus with unspecified complications]:::secondary endocrine diabetes mellitus [type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy]:::complication of type i diabetes mellitus [type 1 diabetes mellitus with unspecified complications]:::history of diabetes mellitus type ii [personal history of other endocrine, nutritional and metabolic disease]:::pregnancy and type 2 diabetes mellitus [pre-existing type 2 diabetes mellitus, in pregnancy]:::type 2 diabetes mellitus with ophthalmic complications [type 2 diabetes mellitus with ophthalmic complications]:::proteinuria due to type 2 diabetes mellitus [type 2 diabetes mellitus with kidney complications]:::type 2 diabetes mellitus with hyperglycemia [type 2 diabetes mellitus with hyperglycemia]                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| HTG-induced pancreatitis              | PROBLEM  | M79.3        | M79.3:::F10.2:::K85.3:::T46.5X:::K85.20:::K85.32:::T50.90:::A39.8:::J98.5:::K91.8:::K29.5:::K05.0:::M33.0:::Q21.1:::K29.4:::K86.1:::I33.0:::K85.90:::J30.0:::B30.3:::K29.6                                       | drug-induced panniculitis [panniculitis, unspecified]:::drug-induced chronic pancreatitis [alcohol dependence]:::drug-induced acute pancreatitis [drug induced acute pancreatitis]:::drug-induced pericarditis [poisoning by, adverse effect of and underdosing of other antihypertensive drugs]:::alcohol-induced pancreatitis [alcohol induced acute pancreatitis without necrosis or infection]:::drug induced acute pancreatitis with infected necrosis [drug induced acute pancreatitis with infected necrosis]:::drug-induced dermatomyositis [poisoning by, adverse effect of and underdosing of unspecified drugs, medicaments and biological substances]:::rbn - retrobulbar neuritis [other meningococcal infections]:::drug-induced granulomatous mediastinitis [diseases of mediastinum, not elsewhere classified]:::post-ercp acute pancreatitis (disorder) [other intraoperative and postprocedural complications and disorders of digestive system]:::cg - chronic gastritis [unspecified chronic gastritis]:::aug - acute ulcerative gingivitis [acute gingivitis]:::dm - dermatomyositis [juvenile dermatomyositis]:::infective endocarditis at site of patch of interatrial communication (disorder) [atrial septal defect]:::cag - chronic atrophic gastritis [chronic atrophic gastritis]:::relapsing pancreatitis (disorder) [other chronic pancreatitis]:::infective endocarditis at site of interatrial communication (disorder) [acute and subacute infective endocarditis]:::hemorrhagic pancreatitis [acute pancreatitis without necrosis or infection, unspecified]:::vmr - vasomotor rhinitis [vasomotor rhinitis]:::ahc - acute hemorrhagic conjunctivitis [acute epidemic hemorrhagic conjunctivitis (enteroviral)]:::drug-induced gastritis [other gastritis]                         |
| acute hepatitis                       | PROBLEM  | K72.0        | K72.0:::B15:::B17.2:::B17.10:::B17.1:::B16:::B17.9:::B18.8:::B15.9:::K75.2:::K73.9:::B16.0:::B15.0:::K74.6:::K75.9:::K75.8:::B18                                                                                 | acute hepatitis [acute and subacute hepatic failure]:::acute hepatitis a [acute hepatitis a]:::acute hepatitis e [acute hepatitis e]:::acute hepatitis c [acute hepatitis c without hepatic coma]:::acute hepatitis c [acute hepatitis c]:::acute hepatitis b [acute hepatitis b]:::acute viral hepatitis [acute viral hepatitis, unspecified]:::chronic hepatitis e [other chronic viral hepatitis]:::acute type a viral hepatitis [hepatitis a without hepatic coma]:::acute focal hepatitis [nonspecific reactive hepatitis]:::chronic hepatitis [chronic hepatitis, unspecified]:::acute type b viral hepatitis [acute hepatitis b with delta-agent with hepatic coma]:::hepatitis a [hepatitis a with hepatic coma]:::chronic hepatitis c [other and unspecified cirrhosis of liver]:::hepatitis [inflammatory liver disease, unspecified]:::ischemic hepatitis [other specified inflammatory liver diseases]:::chronic viral hepatitis [chronic viral hepatitis]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| obesity                               | PROBLEM  | E66.9        | E66.9:::E66.8:::P90:::Q13.0:::M79.4:::Z86.39                                                                                                                                                                     | obesity [obesity, unspecified]:::upper body obesity [other obesity]:::childhood obesity [convulsions of newborn]:::central obesity [coloboma of iris]:::localised obesity [hypertrophy of (infrapatellar) fat pad]:::history of obesity [personal history of other endocrine, nutritional and metabolic disease]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| a body mass index                     | PROBLEM  | E66.9        | E66.9:::Z68.41:::Z68:::E66.8:::Z68.45:::Z68.4:::Z68.1:::Z68.2:::R22.9:::Z68.22:::Z68.21:::Z68.25:::Z68.43:::Z68.20:::Z68.26:::Z68.31:::Z68.42:::Z68.29:::R19.0:::Z68.24:::R22.0:::R22.2                          | observation of body mass index [obesity, unspecified]:::finding of body mass index [body mass index [bmi] 40.0-44.9, adult]:::body mass index [bmi] [body mass index [bmi]]:::body mass index equal to or greater than 40 [other obesity]:::body mass index [bmi] 70 or greater, adult [body mass index [bmi] 70 or greater, adult]:::body mass index [bmi] 40 or greater, adult [body mass index [bmi] 40 or greater, adult]:::body mass index [bmi] 19.9 or less, adult [body mass index [bmi] 19.9 or less, adult]:::body mass index [bmi] 20-29, adult [body mass index [bmi] 20-29, adult]:::mass of body region [localized swelling, mass and lump, unspecified]:::body mass index [bmi] 22.0-22.9, adult [body mass index [bmi] 22.0-22.9, adult]:::body mass index [bmi] 21.0-21.9, adult [body mass index [bmi] 21.0-21.9, adult]:::body mass index [bmi] 25.0-25.9, adult [body mass index [bmi] 25.0-25.9, adult]:::body mass index [bmi] 50.0-59.9, adult [body mass index [bmi] 50.0-59.9, adult]:::body mass index [bmi] 20.0-20.9, adult [body mass index [bmi] 20.0-20.9, adult]:::body mass index [bmi] 26.0-26.9, adult [body mass index [bmi] 26.0-26.9, adult]:::body mass index [bmi] 31.0-31.9, adult [body mass index [bmi] 31.0-31.9, adult]:::body mass index [bmi] 45.0-49.9, adult [body mass index [bmi] 45.0-49.9, adult]:::body mass index [bmi] 29.0-29.9, adult [body mass index [bmi] 29.0-29.9, adult]:::defined border of mass of abdomen [intra-abdominal and pelvic swelling, mass and lump]:::body mass index [bmi] 24.0-24.9, adult [body mass index [bmi] 24.0-24.9, adult]:::subcutaneous mass of head (finding) [localized swelling, mass and lump, head]:::mass of thoracic structure (finding) [localized swelling, mass and lump, trunk]                                |
| polyuria                              | PROBLEM  | R35          | R35:::E88.8:::R30.0:::N28.89:::O04.8:::R82.4:::E74.8:::R82.2:::E73.9:::R82.0:::R34:::N40.1:::R82.8:::E74.2:::R80:::R35.89:::R35.8:::E70.2:::E79.8:::P96.0:::E72.1                                                | polyuria [polyuria]:::sialuria [other specified metabolic disorders]:::stranguria [dysuria]:::isosthenuria [other specified disorders of kidney and ureter]:::oliguria [(induced) termination of pregnancy with other and unspecified complications]:::ketonuria [acetonuria]:::xylosuria [other specified disorders of carbohydrate metabolism]:::biliuria [biliuria]:::sucrosuria [lactose intolerance, unspecified]:::chyluria [chyluria]:::anuria [anuria and oliguria]:::pollakiuria [benign prostatic hyperplasia with lower urinary tract symptoms]:::podocyturia [abnormal findings on cytological and histological examination of urine]:::galactosuria [disorders of galactose metabolism]:::proteinuria [proteinuria]:::other polyuria [other polyuria]:::other polyuria [other polyuria]:::alcaptonuria [disorders of tyrosine metabolism]:::xanthinuria [other disorders of purine and pyrimidine metabolism]:::oliguria and anuria [congenital renal failure]:::hawkinsinuria [disorders of sulfur-bearing amino-acid metabolism]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| polydipsia                            | PROBLEM  | R63.1        | R63.1:::Q17.0:::Q89.4:::Q89.09:::Q74.8:::H53.8:::H53.2:::Q13.2:::R63.8:::E23.2:::H53.1:::R94.13:::K31.7:::H47.03:::O92.6:::H74.4:::Q78.8:::Q83.3:::M33.2:::Q85.8:::Q70.9                                         | polydipsia [polydipsia]:::polyotia [accessory auricle]:::polysomia [conjoined twins]:::polysplenia [congenital malformations of spleen]:::polymelia [other specified congenital malformations of limb(s)]:::palinopsia [other visual disturbances]:::polyopia [diplopia]:::polycoria [other congenital malformations of iris]:::adipsia [other symptoms and signs concerning food and fluid intake]:::primary polydipsia [diabetes insipidus]:::chromatopsia [subjective visual disturbances]:::polyphasic units [abnormal results of function studies of peripheral nervous system]:::duodenal polyp [polyp of stomach and duodenum]:::polymicrogyria [optic nerve hypoplasia]:::polygalactia [galactorrhea]:::otic polyp [polyp of middle ear]:::pseudochondroplasia [other specified osteochondrodysplasias]:::polythelia [accessory nipple]:::polymyositis [polymyositis]:::juvenile polyps of large bowel [other phakomatoses, not elsewhere classified]:::syndactylia [syndactyly, unspecified]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| poor appetite                         | PROBLEM  | R63.0        | R63.0:::R63.2:::P92.9:::R45.81:::Z55.8:::R41.84:::R41.3:::Z74.8:::R46.89:::R45.8:::R63.3:::Z73.89:::R29.89:::Z63.9:::E63.8:::Z56.89:::Z72.4:::Z76.89:::E61.0                                                     | poor appetite [anorexia]:::excessive appetite [polyphagia]:::poor feeding [feeding problem of newborn, unspecified]:::poor self-esteem [low self-esteem]:::poor education [other problems related to education and literacy]:::poor concentration [other specified cognitive deficit]:::poor memory [other amnesia]:::poor informal care arrangements (finding) [other problems related to care provider dependency]:::poor attention control [other symptoms and signs involving appearance and behavior]:::poor self-esteem (finding) [other symptoms and signs involving emotional state]:::trouble eating [feeding difficulties]:::poor daily routine (finding) [other problems related to life management difficulty]:::poor manual dexterity [other symptoms and signs involving the musculoskeletal system]:::poor family relationship (finding) [problem related to primary support group, unspecified]:::inadequate psyllium intake (finding) [other specified nutritional deficiencies]:::poor work record [other problems related to employment]:::diet poor [inappropriate diet and eating habits]:::poor historian [persons encountering health services in other specified circumstances]:::inadequate copper intake [copper deficiency]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| vomiting                              | PROBLEM  | R11.1        | R11.1:::K91.0:::K92.0:::A08.39:::R11:::P92.0:::P92.09:::R11.12:::R11.10:::O21.9:::F63.8:::G43.A1                                                                                                                 | vomiting [vomiting]:::vomiting bile [vomiting following gastrointestinal surgery]:::vomiting blood [hematemesis]:::viral vomiting [other viral enteritis]:::vomiting (disorder) [nausea and vomiting]:::vomiting of newborn [vomiting of newborn]:::vomiting in newborn (disorder) [other vomiting of newborn]:::projectile vomiting [projectile vomiting]:::morning vomiting (disorder) [vomiting, unspecified]:::vomiting of pregnancy [vomiting of pregnancy, unspecified]:::habit vomiting (disorder) [other impulse disorders]:::periodic vomiting [cyclical vomiting, in migraine, intractable]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| a respiratory tract infection         | PROBLEM  | J98.8        | J98.8:::J06.9:::P39.3:::J22:::N39.0:::A49.9:::Z59.3:::T83.51                                                                                                                                                     | respiratory tract infection [other specified respiratory disorders]:::upper respiratory tract infection [acute upper respiratory infection, unspecified]:::urinary tract infection [neonatal urinary tract infection]:::lrti - lower respiratory tract infection [unspecified acute lower respiratory infection]:::uti - urinary tract infection [urinary tract infection, site not specified]:::bacterial respiratory infection [bacterial infection, unspecified]:::institution-acquired respiratory infection [problems related to living in residential institution]:::catheter-associated urinary tract infection [infection and inflammatory reaction due to urinary catheter]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
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