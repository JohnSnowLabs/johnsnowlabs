{%- capture title -%}
ZeroShotNerModel
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}

This is a zero shot named entity recognition based on `RoBertaForQuestionAnswering`. Zero shot models excel at generalization, meaning that the model can accurately predict entities in very different data sets without the need to fine tune the model or train from scratch for each different domain.

Even though a model trained to solve a specific problem can achieve better accuracy than a zero-shot model in this specific task, it probably won't be be useful in a different task. That is where zero-shot models shows its usefulness by being able to achieve good results in many different scenarions.

Parametres:

- `entityDefinitions`: A dictionary with definitions of the named entities. The keys of dictionary are the entity types and the values are lists of hypothesis templates.

- `predictionThreshold`: Minimal confidence score to consider the entity(Default: `0.01`)

- `ignoreEntitites`: A list of entities to be discarted from the output..

All the parameters can be set using the corresponding set method in camel case. For example, `.setMultiLabel()`.

{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, TOKEN 
{%- endcapture -%}

{%- capture model_output_anno -%}
NAMED_ENTITY
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

documentAssembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector() \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

zero_shot_ner = medical.ZeroShotNerModel.pretrained("zero_shot_ner_roberta", "en", "clinical/models")\
    .setEntityDefinitions(
        {
            "PROBLEM": ["What is the disease?", "What is his symptom?", "What is her disease?", "What is his disease?",
                        "What is the problem?" ,"What does a patient suffer", 'What was the reason that the patient is admitted to the clinic?'],
            "DRUG": ["Which drug?", "Which is the drug?", "What is the drug?", "Which drug does he use?", "Which drug does she use?", "Which drug do I use?", "Which drug is prescribed for a symptom?"],
            "ADMISSION_DATE": ["When did patient admitted to a clinic?"],
            "PATIENT_AGE": ["How old is the patient?","What is the gae of the patient?"]
        })\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("zero_shot_ner")\
    .setPredictionThreshold(0.1) # default 0.01

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "zero_shot_ner"])\
    .setOutputCol("ner_chunk")\

pipeline = nlp.Pipeline(stages = [
    documentAssembler,
    sentenceDetector,
    tokenizer,
    zero_shot_ner,
    ner_converter])

text_list = ["The doctor pescribed Majezik for my severe headache.",
             "The patient was admitted to the hospital for his colon cancer.",
             "27 years old patient was admitted to clinic on Sep 1st by Dr. X for a right-sided pleural effusion for thoracentesis."
            ]

data = spark.createDataFrame(text_list, nlp.StringType()).toDF("text")

result = pipeline.fit(data).transform(data)

result.select(F.explode(F.arrays_zip(result.ner_chunk.result, result.ner_chunk.metadata)).alias("cols"))\
      .select(F.expr("cols['0']").alias("chunk"),
              F.expr("cols['1']['entity']").alias("ner_label"),
              F.expr("cols['1']['confidence']").alias("confidence")).show(50, truncate=100)

+------------------------------------------------+--------------+----------+
|                                           chunk|     ner_label|confidence|
+------------------------------------------------+--------------+----------+
|                                         Majezik|          DRUG|0.64671576|
|                                 severe headache|       PROBLEM| 0.5526346|
|                                    colon cancer|       PROBLEM| 0.8898498|
|                                    27 years old|   PATIENT_AGE| 0.6943085|
|                                         Sep 1st|ADMISSION_DATE|0.95646095|
|a right-sided pleural effusion for thoracentesis|       PROBLEM|0.50026613|
+------------------------------------------------+--------------+----------+

{%- endcapture -%}

{%- capture model_python_finance -%}
from johnsnowlabs import nlp, finance

documentAssembler = nlp.DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

textsplitter = finance.TextSplitter()\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
  .setInputCols("sentence")\
  .setOutputCol("token")

zero_shot_ner = finance.ZeroShotNerModel.pretrained("finner_roberta_zeroshot", "en", "finance/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("zero_shot_ner")\
    .setEntityDefinitions(
        {
            "DATE": ['When was the company acquisition?', 'When was the company purchase agreement?'],
            "ORG": ["Which company was acquired?"],
            "PRODUCT": ["Which product?"],
            "PROFIT_INCREASE": ["How much has the gross profit increased?"],
            "REVENUES_DECLINED": ["How much has the revenues declined?"],
            "OPERATING_LOSS_2020": ["Which was the operating loss in 2020"],
            "OPERATING_LOSS_2019": ["Which was the operating loss in 2019"]
        })

ner_converter = finance.NerConverterInternal()\
  .setInputCols(["sentence", "token", "zero_shot_ner"])\
  .setOutputCol("ner_chunk")

pipeline =  nlp.Pipeline(stages=[
  documentAssembler,
  textsplitter,
  tokenizer,
  zero_shot_ner,
  ner_converter
  ]
)

from pyspark.sql.types import StringType
text_list = ["In March 2012, as part of a longer-term strategy, the Company acquired Vertro, Inc., which owned and operated the ALOT product portfolio.",
              "In February 2017, the Company entered into an asset purchase agreement with NetSeer, Inc.",
              "While our gross profit margin increased to 81.4% in 2020 from 63.1% in 2019, our revenues declined approximately 27% in 2020 as compared to 2019.",
              "We reported an operating loss of approximately $8,048,581 million in 2020 as compared to an operating loss of $7,738,193 in 2019."]

data = spark.createDataFrame(text_list, nlp.StringType()).toDF("text")

result = pipeline.fit(data).transform(data)

result.select(F.explode(F.arrays_zip(result.ner_chunk.result, result.ner_chunk.metadata)).alias("cols"))\
      .select(F.expr("cols['0']").alias("chunk"),
              F.expr("cols['1']['entity']").alias("ner_label")).show(50, truncate=100)


+------------------+-------------------+
|chunk             |ner_label          |
+------------------+-------------------+
|March 2012        |DATE               |
|Vertro            |ORG                |
|ALOT              |PRODUCT            |
|February 2017     |DATE               |
|NetSeer           |ORG                |
|81.4%             |PROFIT_INCREASE    |
|27%               |REVENUES_DECLINED  |
|$8,048,581 million|OPERATING_LOSS_2020|
|$7,738,193        |OPERATING_LOSS_2019|
|2019              |DATE               |
+------------------+-------------------+

{%- endcapture -%}

{%- capture model_python_legal -%}
from johnsnowlabs import nlp, legal

documentAssembler = nlp.DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

textSplitter = legal.TextSplitter()\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
  .setInputCols("sentence")\
  .setOutputCol("token")

zero_shot_ner = legal.ZeroShotNerModel.pretrained("legner_roberta_zeroshot", "en", "legal/models")\
  .setInputCols(["sentence", "token"])\
  .setOutputCol("zero_shot_ner")\
  .setEntityDefinitions(
        {
            "DATE": ['When was the company acquisition?', 'When was the company purchase agreement?', "When was the agreement?"],
            "ORG": ["Which company?"],
            "STATE": ["Which state?"],
            "AGREEMENT": ["What kind of agreement?"],
            "LICENSE": ["What kind of license?"],
            "LICENSE_RECIPIENT": ["To whom the license is granted?"]
        })
    
ner_converter = legal.NerConverterInternal()\
  .setInputCols(["sentence", "token", "zero_shot_ner"])\
  .setOutputCol("ner_chunk")

pipeline =  nlp.Pipeline(stages=[
  documentAssembler,
  textSplitter,
  tokenizer,
  zero_shot_ner,
  nerconverter
  ]
)

from pyspark.sql.types import StringType

text_list = [
    "In March 2012, as part of a longer-term strategy, the Company acquired Vertro, Inc., which owned and operated the ALOT product portfolio.",
    "In February 2017, the Company entered into an asset purchase agreement with NetSeer, Inc.",
    "This INTELLECTUAL PROPERTY AGREEMENT, dated as of December 31, 2018 (the 'Effective Date') is entered into by and between Armstrong Flooring, Inc., a Delaware corporation ('Seller') and AFI Licensing LLC, a Delaware company (the 'Licensee')",
    "The Company hereby grants to Seller a perpetual, non- exclusive, royalty-free license",
]

data = spark.createDataFrame(text_list, nlp.StringType()).toDF("text")

result = pipeline.fit(data).transform(data)

result.select(F.explode(F.arrays_zip(result.ner_chunk.result, result.ner_chunk.metadata)).alias("cols"))\
      .select(F.expr("cols['0']").alias("chunk"),
              F.expr("cols['1']['entity']").alias("ner_label")).show(50, truncate=100)

+-------------------------------------+-----------------+
|chunk                                |ner_label        |
+-------------------------------------+-----------------+
|March 2012                           |DATE             |
|Vertro, Inc                          |ORG              |
|February 2017                        |DATE             |
|asset purchase agreement             |AGREEMENT        |
|NetSeer                              |ORG              |
|INTELLECTUAL PROPERTY                |AGREEMENT        |
|December 31, 2018                    |DATE             |
|Armstrong Flooring                   |LICENSE_RECIPIENT|
|Delaware                             |STATE            |
|AFI Licensing LLC, a Delaware company|LICENSE_RECIPIENT|
|Seller                               |LICENSE_RECIPIENT|
|perpetual                            |LICENSE          |
|non- exclusive                       |LICENSE          |
|royalty-free                         |LICENSE          |
+-------------------------------------+-----------------+

{%- endcapture -%}


{%- capture model_scala_medical -%}

import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val zeroShotNer = ZeroShotNerModel.pretrained("zero_shot_ner_roberta", "en", "clinical/models")
  .setEntityDefinitions(Map(
    "PROBLEM" -> Seq("What is the disease?", "What is his symptom?", "What is her disease?", "What is his disease?",
                     "What is the problem?" ,"What does a patient suffer", "What was the reason that the patient is admitted to the clinic?"),
    "DRUG" -> Seq("Which drug?", "Which is the drug?", "What is the drug?", "Which drug does he use?", "Which drug does she use?", "Which drug do I use?", "Which drug is prescribed for a symptom?"),
    "ADMISSION_DATE" -> Seq("When did patient admitted to a clinic?"),
    "PATIENT_AGE" -> Seq("How old is the patient?", "What is the gae of the patient?")
  ))
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("zero_shot_ner")
  .setPredictionThreshold(0.1)

val nerConverter = new NerConverterInternal()
  .setInputCols(Array("sentence", "token", "zero_shot_ner"))
  .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, 
    sentenceDetector, 
    tokenizer, 
    zeroShotNer, 
    nerConverter))

val textList = Seq(
  "The doctor pescribed Majezik for my severe headache.",
  "The patient was admitted to the hospital for his colon cancer.",
  "27 years old patient was admitted to clinic on Sep 1st by Dr. X for a right-sided pleural effusion for thoracentesis."
).toDS.toDF("text")

val result = pipeline.fit(textList).transform(textList)

result.selectExpr("explode(arrays_zip(ner_chunk.result, ner_chunk.metadata)) as cols")
  .selectExpr(
    "cols['0'] as chunk",
    "cols['1']['entity'] as ner_label",
    "cols['1']['confidence'] as confidence").show(70) 
  
+------------------------------------------------+--------------+----------+
|                                           chunk|     ner_label|confidence|
+------------------------------------------------+--------------+----------+
|                                         Majezik|          DRUG|0.64671576|
|                                 severe headache|       PROBLEM| 0.5526346|
|                                    colon cancer|       PROBLEM| 0.8898498|
|                                    27 years old|   PATIENT_AGE| 0.6943085|
|                                         Sep 1st|ADMISSION_DATE|0.95646095|
|a right-sided pleural effusion for thoracentesis|       PROBLEM|0.50026613|
+------------------------------------------------+--------------+----------+

{%- endcapture -%}

{%- capture model_scala_finance -%}

import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val textsplitter = new TextSplitter()
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val zero_shot_ner = ZeroShotNerModel.pretrained("finner_roberta_zeroshot", "en", "finance/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("zero_shot_ner")
  .setEntityDefinitions(
    Map(
      "DATE" -> Seq('When was the company acquisition?', 'When was the company purchase agreement?'),
      "ORG" -> Seq("Which company was acquired?"),
      "PRODUCT" -> Seq("Which product?"),
      "PROFIT_INCREASE" -> Seq("How much has the gross profit increased?"),
      "REVENUES_DECLINED" -> Seq("How much has the revenues declined?"),
      "OPERATING_LOSS_2020" -> Seq("Which was the operating loss in 2020"),
      "OPERATING_LOSS_2019" -> Seq("Which was the operating loss in 2019")
    )
  )

val ner_converter = new NerConverterInternal()
  .setInputCols(Array("sentence", "token", "zero_shot_ner"))
  .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  textsplitter,
  tokenizer,
  zero_shot_ner,
  ner_converter
))

val text_list = Seq(
  "In March 2012, as part of a longer-term strategy, the Company acquired Vertro, Inc., which owned and operated the ALOT product portfolio.",
  "In February 2017, the Company entered into an asset purchase agreement with NetSeer, Inc.",
  "While our gross profit margin increased to 81.4% in 2020 from 63.1% in 2019, our revenues declined approximately 27% in 2020 as compared to 2019.",
  "We reported an operating loss of approximately $8,048,581 million in 2020 as compared to an operating loss of $7,738,193 in 2019."
).toDS.toDF("text")

val result = pipeline.fit(text_list).transform(text_list)

result.selectExpr("explode(arrays_zip(ner_chunk.result, ner_chunk.metadata)) as cols")
      .selectExpr("cols['0'] as chunk", "cols['1']['entity'] as ner_label").show(false)


+------------------+-------------------+
|chunk             |ner_label          |
+------------------+-------------------+
|March 2012        |DATE               |
|Vertro            |ORG                |
|ALOT              |PRODUCT            |
|February 2017     |DATE               |
|NetSeer           |ORG                |
|81.4%             |PROFIT_INCREASE    |
|27%               |REVENUES_DECLINED  |
|$8,048,581 million|OPERATING_LOSS_2020|
|$7,738,193        |OPERATING_LOSS_2019|
|2019              |DATE               |
+------------------+-------------------+

{%- endcapture -%}


{%- capture model_scala_legal -%}

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val textSplitter = new TextSplitter()
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val zeroShotNer = ZeroShotNerModel.pretrained("legner_roberta_zeroshot", "en", "legal/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("zero_shot_ner")
  .setEntityDefinitions(Map(
    "DATE" -> Seq("When was the company acquisition?", "When was the company purchase agreement?", "When was the agreement?"),
    "ORG" -> Seq("Which company?"),
    "STATE" -> Seq("Which state?"),
    "AGREEMENT" -> Seq("What kind of agreement?"),
    "LICENSE" -> Seq("What kind of license?"),
    "LICENSE_RECIPIENT" -> Seq("To whom the license is granted?")
  ))

val nerConverter = new NerConverterInternal()
  .setInputCols(Array("sentence", "token", "zero_shot_ner"))
  .setOutputCol("ner_chunk")


val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    textSplitter,
    tokenizer,
    zeroShotNer,
    nerConverter
  ))

val textList = Seq(
  "In March 2012, as part of a longer-term strategy, the Company acquired Vertro, Inc., which owned and operated the ALOT product portfolio.",
  "In February 2017, the Company entered into an asset purchase agreement with NetSeer, Inc.",
  "This INTELLECTUAL PROPERTY AGREEMENT, dated as of December 31, 2018 (the 'Effective Date') is entered into by and between Armstrong Flooring, Inc., a Delaware corporation ('Seller') and AFI Licensing LLC, a Delaware company (the 'Licensee')",
  "The Company hereby grants to Seller a perpetual, non-exclusive, royalty-free license"
).toDS.toDF("text")

val result = pipeline.fit(textList).transform(textList)

result.selectExpr("explode(arrays_zip(ner_chunk.result, ner_chunk.metadata)) as cols")
      .selectExpr("cols['0'] as chunk", "cols['1']['entity'] as ner_label").show(false)
+-------------------------------------+-----------------+
|chunk                                |ner_label        |
+-------------------------------------+-----------------+
|March 2012                           |DATE             |
|Vertro, Inc                          |ORG              |
|February 2017                        |DATE             |
|asset purchase agreement             |AGREEMENT        |
|NetSeer                              |ORG              |
|INTELLECTUAL PROPERTY                |AGREEMENT        |
|December 31, 2018                    |DATE             |
|Armstrong Flooring                   |LICENSE_RECIPIENT|
|Delaware                             |STATE            |
|AFI Licensing LLC, a Delaware company|LICENSE_RECIPIENT|
|Seller                               |LICENSE_RECIPIENT|
|perpetual                            |LICENSE          |
|non-exclusive                        |LICENSE          |
|royalty-free                         |LICENSE          |
+-------------------------------------+-----------------+

{%- endcapture -%}

{%- capture model_api_link -%}
[ZeroShotNerModel](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/finance/token_classification/ner/ZeroShotNerModel.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[ZeroShotNerModel](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/ner/zero_shot_ner/index.html#sparknlp_jsl.annotator.ner.zero_shot_ner.ZeroShotNerModel)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[ZeroShotNerModel](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ZeroShotNerModel.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_python_finance=model_python_finance
model_scala_medical=model_scala_medical
model_python_legal=model_python_legal
model_scala_legal=model_scala_legal
model_scala_finance=model_scala_finance
model_api_link=model_api_link
model_python_api_link=model_python_api_link
model_notebook_link=model_notebook_link
%}
