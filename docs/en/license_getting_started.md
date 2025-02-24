---
layout: docs
header: true
title: Enterprise Spark NLP
permalink: /docs/en/license_getting_started
key: docs-licensed-install
modify_date: "2021-03-09"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

<div class="tabs-model-aproach has_nlu" markdown="1">

{% include programmingLanguageSelectScalaPythonNLU.html %}

<div class="highlighter-rouge jsl-tabs tabs-python-scala-box language-python" markdown="1">
{% include programmingLanguageSelectPythons.html %}

<div class="tabs-mfl-box python-spark-nlp-jsl" markdown="1">

 ```python
...
pos = PerceptronModel.pretrained("pos_clinical","en","clinical/models")\
	.setInputCols(["token","sentence"])\
	.setOutputCol("pos")

pos_pipeline = Pipeline(stages=[document_assembler, sentence_detector, tokenizer, pos])
light_pipeline = LightPipeline(pos_pipeline.fit(spark.createDataFrame([[""]]).toDF("text")))
result = light_pipeline.fullAnnotate("""He was given boluses of MS04 with some effect, he has since been placed on a PCA - he take 80mg of oxycontin at home, his PCA dose is ~ 2 the morphine dose of the oxycontin, he has also received ativan for anxiety.""")
```

</div>
<div class="tabs-mfl-box python-johnsnowlabs" markdown="1">

```python
...
pos = PerceptronModel.pretrained("pos_clinical","en","clinical/models")\
    .setInputCols(["token","sentence"])\
    .setOutputCol("pos")

pos_pipeline = Pipeline(stages=[document_assembler, sentence_detector, tokenizer, pos])
light_pipeline = LightPipeline(pos_pipeline.fit(spark.createDataFrame([[""]]).toDF("text")))
result = light_pipeline.fullAnnotate("""He was given boluses of MS04 with some effect, he has since been placed on a PCA - he take 80mg of oxycontin at home, his PCA dose is ~ 2 the morphine dose of the oxycontin, he has also received ativan for anxiety.""")
```

</div>
</div>

{:.tabs-python-scala-box}
```scala
val pos = PerceptronModel.pretrained("pos_clinical","en","clinical/models")
	.setInputCols("token","sentence")
	.setOutputCol("pos")

val pipeline = new Pipeline().setStages(Array(document_assembler, sentence_detector, tokenizer, pos))
val data = Seq("He was given boluses of MS04 with some effect, he has since been placed on a PCA - he take 80mg of oxycontin at home, his PCA dose is ~ 2 the morphine dose of the oxycontin, he has also received ativan for anxiety.").toDF("text")
val result = pipeline.fit(data).transform(data)
```

{:.tabs-python-scala-box}
```python
import nlu
nlu.load("en.pos.clinical").predict("""He was given boluses of MS04 with some effect, he has since been placed on a PCA - he take 80mg of oxycontin at home, his PCA dose is ~ 2 the morphine dose of the oxycontin, he has also received ativan for anxiety.""")
```

</div><div class="h3-box" markdown="1">

### Getting started

We call *Enterprise Spark NLP libraries* to all the commercial NLP libraries, including Healthcare NLP (former
Spark NLP for Healthcare), Finance, Legal NLP, among others. This excludes Visual NLP (former Spark OCR), which has its own documentation page,
available [here](https://nlp.johnsnowlabs.com/docs/en/ocr).

If you don't have an Enterprise Spark NLP subscription yet, you can ask for a free trial by clicking on the Try Free button and following the instructions provides in the video below.

{:.btn-block}
[Try Free](https://www.johnsnowlabs.com/install/){:.button.button--primary.button--rounded.button--lg}


30-day free trials for the John Snow Labs NLP libraries can be obtained via AWS and Azure markeplaces. To get a free trial please subscribe to one of the pay-as-you-go products:
- [John Snow Labs NLP Libraries - AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-kpac4xtqkxuqu)
- [John Snow Labs NLP Libraries - Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/johnsnowlabsinc1646051154808.johnsnowlabs_nlp?tab=Overview)

**Note:** It is important to note that every AWS/Azure account is limited to one 30-day free trial period for John Snow Labs NLP Libraries, and users are responsible for verifying the status of any past trials before subscribing and being charged for usage.


Enterprise Spark NLP libraries provides healthcare-specific annotators, pipelines, models, and embeddings for:
- Entity recognition
- Entity Linking
- Entity normalization
- Assertion Status Detection
- De-identification
- Relation Extraction
- Spell checking & correction
- and much more!
 
<!---
Note: If you are going to use any pretrained licensed NER model, you don't need to install licensed libray. As long as you have the AWS keys and license keys in your environment, you will be able to use licensed NER models with Spark NLP public library. For the other licensed pretrained models like AssertionDL, Deidentification, Entity Resolvers and Relation Extraction models, you will need to install Spark NLP Enterprise as well.

 The library offers access to several clinical and biomedical transformers: JSL-BERT-Clinical, BioBERT, ClinicalBERT, GloVe-Med, GloVe-ICD-O. It also includes over 50 pre-trained healthcare models, that can recognize the following entities (any many more):
- Clinical - support Signs, Symptoms, Treatments, Procedures, Tests, Labs, Sections
- Drugs - support Name, Dosage, Strength, Route, Duration, Frequency
- Risk Factors- support Smoking, Obesity, Diabetes, Hypertension, Substance Abuse
- Anatomy - support Organ, Subdivision, Cell, Structure Organism, Tissue, Gene, Chemical
- Demographics - support Age, Gender, Height, Weight, Race, Ethnicity, Marital Status, Vital Signs
- Sensitive Data- support Patient Name, Address, Phone, Email, Dates, Providers, Identifiers
-->

</div>