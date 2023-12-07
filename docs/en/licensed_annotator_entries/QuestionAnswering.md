{%- capture title -%}
QuestionAnswering
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
QuestionAnswering is a GPT-based model for answering questions given a context. Unlike span-based models, it generates the answers to the questions, rather than selecting phrases from the given context. The model is capable of answering various types of questions, including yes-no or full-text ones. Types of questions are supported: `"short"` (producing yes/no/maybe) answers and `"long"` (full answers).

Parameters:
- `questionType`: Question type, e.g. “short” or “long”. The question types depend on the model.

- `maxNewTokens`: Maximum number of of new tokens to generate, by default 30

- `maxContextLength`: Maximum length of context text

- `configProtoBytes`: ConfigProto from tensorflow, serialized into byte array.

- `doSample`: Whether or not to use sampling; use greedy decoding otherwise, by default False

- `topK`: The number of highest probability vocabulary tokens to consider, by default 1

- `noRepeatNgramSize`: The number of tokens that can’t be repeated in the same order. Useful for preventing loops. The default is 0.

- `ignoreTokenIds`: A list of token ids which are ignored in the decoder’s output, by default []

- `randomSeed`: Set to positive integer to get reproducible results, by default None.

- `customPrompt`: Custom prompt template. Available variables {QUESTION} and {CONTEXT}

Available models can be found at the [Models Hub](https://nlp.johnsnowlabs.com/models?task=Question+Answering)

For more extended examples on the document, pre-processing see the [Spark NLP Workshop](https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master)
{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, DOCUMENT
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

document_assembler = nlp.MultiDocumentAssembler()\
    .setInputCols("question", "context")\
    .setOutputCols("document_question", "document_context")

med_qa = medical.MedicalQuestionAnswering.pretrained("medical_qa_biogpt","en","clinical/models")\
    .setInputCols(["document_question", "document_context"])\
    .setOutputCol("answer")\
    .setMaxNewTokens(30)\
    .setTopK(1)\
    .setQuestionType("long") # "short"

pipeline = nlp.Pipeline(stages=[document_assembler, med_qa])

paper_abstract = [
    "In patients with Los Angeles (LA) grade C or D oesophagitis, a positive relationship has been established between the duration of intragastric acid suppression and healing.AIM: To determine whether there is an apparent optimal time of intragastric acid suppression for maximal healing of reflux oesophagitis. Post hoc analysis of data from a proof-of-concept, double-blind, randomized study of 134 adult patients treated with esomeprazole (10 or 40 mg od for 4 weeks) for LA grade C or D oesophagitis. A curve was fitted to pooled 24-h intragastric pH (day 5) and endoscopically assessed healing (4 weeks) data using piecewise quadratic logistic regression. Maximal reflux oesophagitis healing rates were achieved when intragastric pH>4 was achieved for approximately 50-70% (12-17 h) of the 24-h period. Acid suppression above this threshold did not yield further increases in healing rates."
]

question = ["Is there an optimal time of acid suppression for maximal healing?"]

data = spark.createDataFrame([ [paper_abstract[0],  question[0]] ]).toDF("context","question")

data.show(truncate = 60)

+------------------------------------------------------------+------------------------------------------------------------+
|                                                     context|                                                    question|
+------------------------------------------------------------+------------------------------------------------------------+
|In patients with Los Angeles (LA) grade C or D oesophagit...|Is there an optimal time of acid suppression for maximal ...|
+------------------------------------------------------------+------------------------------------------------------------+

result = pipeline.fit(data).transform(data)

result.selectExpr("document_question.result as Question", "answer.result as Long_Answer").show(truncate=False)

+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
|Question                                                           |Long_Answer                                                                                                                                          |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
|[Is there an optimal time of acid suppression for maximal healing?]|[in patients with reflux oesophagitis, maximal healing rates are obtained when intragastric pH is achieved for approximately 50 - 70 % ( 12 - 17 h )]|
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_scala_medical -%}
val documentAssembler = new DocumentAssembler()
  .setInputCols(Array("question", "context"))
  .setOutputCols(Array("document_question", "document_context"))

val medQA = MedicalQuestionAnswering.pretrained("medical_qa_biogpt", "en", "clinical/models")
  .setInputCols(Array("document_question", "document_context"))
  .setOutputCol("answer")
  .setMaxNewTokens(30)
  .setTopK(1)
  .setQuestionType("long") // "short"

val pipeline = new Pipeline().setStages(Array(documentAssembler, medQA))

val paperAbstract = "In patients with Los Angeles (LA) grade C or D oesophagitis, a positive relationship has been established between the duration of intragastric acid suppression and healing.AIM: To determine whether there is an apparent optimal time of intragastric acid suppression for maximal healing of reflux oesophagitis. Post hoc analysis of data from a proof-of-concept, double-blind, randomized study of 134 adult patients treated with esomeprazole (10 or 40 mg od for 4 weeks) for LA grade C or D oesophagitis. A curve was fitted to pooled 24-h intragastric pH (day 5) and endoscopically assessed healing (4 weeks) data using piecewise quadratic logistic regression. Maximal reflux oesophagitis healing rates were achieved when intragastric pH>4 was achieved for approximately 50-70% (12-17 h) of the 24-h period. Acid suppression above this threshold did not yield further increases in healing rates."

val question = "Is there an optimal time of acid suppression for maximal healing?"

val data = Seq(paperAbstract, question).toDF("context", "question")

data.show()

+------------------------------------------------------------+------------------------------------------------------------+
|                                                     context|                                                    question|
+------------------------------------------------------------+------------------------------------------------------------+
|In patients with Los Angeles (LA) grade C or D oesophagit...|Is there an optimal time of acid suppression for maximal ...|
+------------------------------------------------------------+------------------------------------------------------------+

val result = pipeline.fit(data).transform(data)

result.selectExpr("document_question.result as Question", "answer.result as Long_Answer").show(false)

+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
|Question                                                           |Long_Answer                                                                                                                                          |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
|[Is there an optimal time of acid suppression for maximal healing?]|[in patients with reflux oesophagitis, maximal healing rates are obtained when intragastric pH is achieved for approximately 50 - 70 % ( 12 - 17 h )]|
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_python_legal -%}
from johnsnowlabs import nlp, legal

context = ["""EXHIBIT 99.2 Page 1 of 3 DISTRIBUTOR AGREEMENT Agreement made this 19th day of March, 2020 Between: Co-Diagnostics, Inc. (herein referred to as "Principal") And PreCheck Health Services, Inc. (herein referred to as "Distributor"). In consideration of the mutual terms, conditions and covenants hereinafter set forth, Principal and Distributor acknowledge and agree to the following descriptions and conditions: DESCRIPTION OF PRINCIPAL The Principal is a company located in Utah, United States and is in the business of research and development of reagents. The Principal markets and sells it products globally through direct sales and distributors. DESCRIPTION OF DISTRIBUTOR The Distributor is a company operating or planning to operate in the United States of America, Latin America, Europe and Russia. The Distributor represents that the Distributor or a subsidiary of the Distributor is or will be fully licensed and registered in the Territory and will provide professional distribution services for the products of the Principal. CONDITIONS: 1. The Principal appoints the Distributor as a non-exclusive distributor, to sell Principal's qPCR infectious disease kits, Logix Smart COVID-19 PCR diagnostic test and Co-Dx Box™ instrument (the "Products"). The Products are described on Exhibit A to this Agreement. 2. The Principal grants Distributor non- exclusive rights to sell these products within the countries of Romania (the "Territory"), which may be amended by mutual written agreement."""]

questions = ["""Which company is referred to as 'Principal' in the Distributor Agreement?""",
             """What is the date of the distributor agreement between Co-Diagnostics, Inc. and PreCheck Health Services, Inc.?""",
             """What is the Territory in which the Distributor has non-exclusive rights to sell Principal's products according to the Agreement?"""]

data = spark.createDataFrame(
    [
        [context[0],  questions[0]],
        [context[0],  questions[1]],
        [context[0],  questions[2]],
    ]
).toDF("context","question")

data.show(truncate = 80)

+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
|                                                                         context|                                                                        question|
+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
|EXHIBIT 99.2 Page 1 of 3 DISTRIBUTOR AGREEMENT Agreement made this 19th day o...|       Which company is referred to as 'Principal' in the Distributor Agreement?|
|EXHIBIT 99.2 Page 1 of 3 DISTRIBUTOR AGREEMENT Agreement made this 19th day o...|What is the date of the distributor agreement between Co-Diagnostics, Inc. an...|
|EXHIBIT 99.2 Page 1 of 3 DISTRIBUTOR AGREEMENT Agreement made this 19th day o...|What is the Territory in which the Distributor has non-exclusive rights to se...|
+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

document_assembler = nlp.MultiDocumentAssembler()\
    .setInputCols("question", "context")\
    .setOutputCols("document_question", "document_context")

leg_qa = legal.QuestionAnswering.pretrained("legqa_flant5_finetuned","en","legal/models")\
    .setInputCols(["document_question", "document_context"])\
    .setCustomPrompt("question: {QUESTION} context: {CONTEXT}")\
    .setMaxNewTokens(40)\
    .setTopK(3)\
    .setOutputCol("answer")

pipeline = nlp.Pipeline(stages=[document_assembler, leg_qa])

result = pipeline.fit(data).transform(data)

result.selectExpr("document_question.result as Question", "answer.result as Answer").show(truncate=False)

+----------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
|Question                                                                                                                          |Answer                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
|[Which company is referred to as 'Principal' in the Distributor Agreement?]                                                       |[Co-Diagnostics, Inc. is referred to as 'Principal' in the Distributor Agreement. ]                                                     |
|[What is the date of the distributor agreement between Co-Diagnostics, Inc. and PreCheck Health Services, Inc.?]                  |[The date of the distributor agreement between Co-Diagnostics, Inc. and PreCheck Health Services, Inc. is the 19th day of March, 2020. ]|
|[What is the Territory in which the Distributor has non-exclusive rights to sell Principal's products according to the Agreement?]|[The Territory in which the Distributor has non-exclusive rights to sell Principal's products according to the Agreement is Romania. ]  |
+----------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_scala_legal -%}
val context = Seq("""EXHIBIT 99.2 Page 1 of 3 DISTRIBUTOR AGREEMENT Agreement made this 19th day of March, 2020 Between: Co-Diagnostics, Inc. (herein referred to as "Principal") And PreCheck Health Services, Inc. (herein referred to as "Distributor"). In consideration of the mutual terms, conditions and covenants hereinafter set forth, Principal and Distributor acknowledge and agree to the following descriptions and conditions: DESCRIPTION OF PRINCIPAL The Principal is a company located in Utah, United States and is in the business of research and development of reagents. The Principal markets and sells it products globally through direct sales and distributors. DESCRIPTION OF DISTRIBUTOR The Distributor is a company operating or planning to operate in the United States of America, Latin America, Europe and Russia. The Distributor represents that the Distributor or a subsidiary of the Distributor is or will be fully licensed and registered in the Territory and will provide professional distribution services for the products of the Principal. CONDITIONS: 1. The Principal appoints the Distributor as a non-exclusive distributor, to sell Principal's qPCR infectious disease kits, Logix Smart COVID-19 PCR diagnostic test and Co-Dx Box™ instrument (the "Products"). The Products are described on Exhibit A to this Agreement. 2. The Principal grants Distributor non- exclusive rights to sell these products within the countries of Romania (the "Territory"), which may be amended by mutual written agreement."""
)

val questions = Seq(
  """Which company is referred to as 'Principal' in the Distributor Agreement?""",
  """What is the date of the distributor agreement between Co-Diagnostics, Inc. and PreCheck Health Services, Inc.?""",
  """What is the Territory in which the Distributor has non-exclusive rights to sell Principal's products according to the Agreement?"""
)

val data = context.flatMap(c => questions.map(q => (c, q))).toDF("context", "question")

data.show()

+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
|                                                                         context|                                                                        question|
+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
|EXHIBIT 99.2 Page 1 of 3 DISTRIBUTOR AGREEMENT Agreement made this 19th day o...|       Which company is referred to as 'Principal' in the Distributor Agreement?|
|EXHIBIT 99.2 Page 1 of 3 DISTRIBUTOR AGREEMENT Agreement made this 19th day o...|What is the date of the distributor agreement between Co-Diagnostics, Inc. an...|
|EXHIBIT 99.2 Page 1 of 3 DISTRIBUTOR AGREEMENT Agreement made this 19th day o...|What is the Territory in which the Distributor has non-exclusive rights to se...|
+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

val documentAssembler = new DocumentAssembler()
  .setInputCols(Array("question", "context"))
  .setOutputCols(Array("document_question", "document_context"))

val legQA = LegalQuestionAnswering.pretrained("legqa_flant5_finetuned", "en", "clinical/models")
  .setInputCols(Array("document_question", "document_context"))
  .setCustomPrompt("question: {QUESTION} context: {CONTEXT}")
  .setMaxNewTokens(40)
  .setTopK(3)
  .setOutputCol("answer")

val pipeline = new Pipeline().setStages(Array(documentAssembler, legQA))

val result = pipeline.fit(data).transform(data)

result.selectExpr("document_question.result as Question", "answer.result as Answer").show(false)

+----------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
|Question                                                                                                                          |Answer                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
|[Which company is referred to as 'Principal' in the Distributor Agreement?]                                                       |[Co-Diagnostics, Inc. is referred to as 'Principal' in the Distributor Agreement. ]                                                     |
|[What is the date of the distributor agreement between Co-Diagnostics, Inc. and PreCheck Health Services, Inc.?]                  |[The date of the distributor agreement between Co-Diagnostics, Inc. and PreCheck Health Services, Inc. is the 19th day of March, 2020. ]|
|[What is the Territory in which the Distributor has non-exclusive rights to sell Principal's products according to the Agreement?]|[The Territory in which the Distributor has non-exclusive rights to sell Principal's products according to the Agreement is Romania. ]  |
+----------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_python_finance -%}
from johnsnowlabs import nlp, finance

document_assembler = nlp.MultiDocumentAssembler()\
    .setInputCols("question", "context")\
    .setOutputCols("document_question", "document_context")

fin_qa = finance.QuestionAnswering.pretrained("finqa_flant5_finetuned","en","finance/models")\
    .setInputCols(["document_question", "document_context"])\
    .setCustomPrompt("question: {QUESTION} context: {CONTEXT}")\
    .setMaxNewTokens(100)\
    .setOutputCol("answer")

pipeline = nlp.Pipeline(stages=[document_assembler, fin_qa])

context = """EXHIBIT 99.2 Page 1 of 3 DISTRIBUTOR AGREEMENT Agreement made this 19th day of March, 2020 Between: Co-Diagnostics, Inc. (herein referred to as "Principal") And PreCheck Health Services, Inc. (herein referred to as "Distributor"). In consideration of the mutual terms, conditions and covenants hereinafter set forth, Principal and Distributor acknowledge and agree to the following descriptions and conditions: DESCRIPTION OF PRINCIPAL The Principal is a company located in Utah, United States and is in the business of research and development of reagents. The Principal markets and sells it products globally through direct sales and distributors. DESCRIPTION OF DISTRIBUTOR The Distributor is a company operating or planning to operate in the United States of America, Latin America, Europe and Russia. The Distributor represents that the Distributor or a subsidiary of the Distributor is or will be fully licensed and registered in the Territory and will provide professional distribution services for the products of the Principal. CONDITIONS: 1. The Principal appoints the Distributor as a non-exclusive distributor, to sell Principal's qPCR infectious disease kits, Logix Smart COVID-19 PCR diagnostic test and Co-Dx Box™ instrument (the "Products"). The Products are described on Exhibit A to this Agreement. 2. The Principal grants Distributor non- exclusive rights to sell these products within the countries of Romania (the "Territory"), which may be amended by mutual written agreement."""

questions = ["""Which company is referred to as 'Principal' in the Distributor Agreement?""",
             """What is the date of the distributor agreement between Co-Diagnostics, Inc. and PreCheck Health Services, Inc.?""",
             """What is the Territory in which the Distributor has non-exclusive rights to sell Principal's products according to the Agreement?"""]

data = spark.createDataFrame(
    [
        [context[0],  questions[0]],
        [context[0],  questions[1]],
        [context[0],  questions[2]],
    ]
).toDF("context","question")

data.show(truncate = 80)

+------------------------------------------------------------------+--------------------------------------------------------------------------------+
|                                                          question|                                                                         context|
+------------------------------------------------------------------+--------------------------------------------------------------------------------+
|   What are the key components of the business strategy described?|Our business strategy has been to develop data processing and product technol...|
|What is the immediate strategy for scaling the IntentKey platform?|Our business strategy has been to develop data processing and product technol...|
|How does the company aim to provide differentiation in the market?|Our business strategy has been to develop data processing and product technol...|
+------------------------------------------------------------------+--------------------------------------------------------------------------------+

result = pipeline.fit(data).transform(data)

result.select('question', 'answer.result').show(truncate=False)

+------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|question                                                          |result                                                                                                                                                                                                                                                                                                            |
+------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|What are the key components of the business strategy described?   |[The key components of the business strategy described are proprietary demand (media spend) and supply side (media inventory) technologies, targeting technologies, on-page or in-app ad-unit technologies, proprietary data and data management technologies, and advertising fraud detection technologies. . . ]|
|What is the immediate strategy for scaling the IntentKey platform?|[The immediate strategy for scaling the IntentKey platform is to scale through the hiring of additional sales professionals, growing existing accounts and expanding the market size by concurrently selling the SaaS version of the IntentKey beginning in 2021. ]                                               |
|How does the company aim to provide differentiation in the market?|[The company aims to provide differentiation through the AI analytics and data products they own and protect through patents. ]                                                                                                                                                                                   |
+------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}

{%- capture model_scala_finance -%}
val documentAssembler = new DocumentAssembler()
  .setInputCols(Array("question", "context"))
  .setOutputCols(Array("document_question", "document_context"))

val finQa = new QuestionAnswering()
  .pretrained("finqa_flant5_finetuned", "en", "finance/models")
  .setInputCols(Array("document_question", "document_context"))
  .setCustomPrompt("question: {QUESTION} context: {CONTEXT}")
  .setMaxNewTokens(100)
  .setOutputCol("answer")

val pipeline = new Pipeline().setStages(Array(documentAssembler, finQa))

val context = "EXHIBIT 99.2 Page 1 of 3 DISTRIBUTOR AGREEMENT Agreement made this 19th day of March, 2020 Between: Co-Diagnostics, Inc. (herein referred to as "Principal") And PreCheck Health Services, Inc. (herein referred to as "Distributor"). In consideration of the mutual terms, conditions and covenants hereinafter set forth, Principal and Distributor acknowledge and agree to the following descriptions and conditions: DESCRIPTION OF PRINCIPAL The Principal is a company located in Utah, United States and is in the business of research and development of reagents. The Principal markets and sells it products globally through direct sales and distributors. DESCRIPTION OF DISTRIBUTOR The Distributor is a company operating or planning to operate in the United States of America, Latin America, Europe and Russia. The Distributor represents that the Distributor or a subsidiary of the Distributor is or will be fully licensed and registered in the Territory and will provide professional distribution services for the products of the Principal. CONDITIONS: 1. The Principal appoints the Distributor as a non-exclusive distributor, to sell Principal's qPCR infectious disease kits, Logix Smart COVID-19 PCR diagnostic test and Co-Dx Box™ instrument (the "Products"). The Products are described on Exhibit A to this Agreement. 2. The Principal grants Distributor non- exclusive rights to sell these products within the countries of Romania (the "Territory"), which may be amended by mutual written agreement."

val questions = Seq(
  "Which company is referred to as 'Principal' in the Distributor Agreement?",
  "What is the date of the distributor agreement between Co-Diagnostics, Inc. and PreCheck Health Services, Inc.?",
  "What is the Territory in which the Distributor has non-exclusive rights to sell Principal's products according to the Agreement?"
)

val data = questions.map(q => (context, q)).toDF("context", "question")

data.show(false)

+------------------------------------------------------------------+--------------------------------------------------------------------------------+
|                                                          question|                                                                         context|
+------------------------------------------------------------------+--------------------------------------------------------------------------------+
|   What are the key components of the business strategy described?|Our business strategy has been to develop data processing and product technol...|
|What is the immediate strategy for scaling the IntentKey platform?|Our business strategy has been to develop data processing and product technol...|
|How does the company aim to provide differentiation in the market?|Our business strategy has been to develop data processing and product technol...|
+------------------------------------------------------------------+--------------------------------------------------------------------------------+

val result = pipeline.fit(data).transform(data)

result.selectExpr("question.result", "answer.result").show(false)

+------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|question                                                          |result                                                                                                                                                                                                                                                                                                            |
+------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|What are the key components of the business strategy described?   |[The key components of the business strategy described are proprietary demand (media spend) and supply side (media inventory) technologies, targeting technologies, on-page or in-app ad-unit technologies, proprietary data and data management technologies, and advertising fraud detection technologies. . . ]|
|What is the immediate strategy for scaling the IntentKey platform?|[The immediate strategy for scaling the IntentKey platform is to scale through the hiring of additional sales professionals, growing existing accounts and expanding the market size by concurrently selling the SaaS version of the IntentKey beginning in 2021. ]                                               |
|How does the company aim to provide differentiation in the market?|[The company aims to provide differentiation through the AI analytics and data products they own and protect through patents. ]                                                                                                                                                                                   |
+------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_api_link -%}
[MedicalQuestionAnswering](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/qa/MedicalQuestionAnswering.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[MedicalQuestionAnswering](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/qa/medical_qa/index.html#sparknlp_jsl.annotator.qa.medical_qa.MedicalQuestionAnswering)
{%- endcapture -%}

{%- capture model_notebook_link -%}

{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical
model_python_legal=model_python_legal
model_scala_legal=model_scala_legal
model_python_finance=model_python_finance
model_scala_finance=model_scala_finance
model_api_link=model_api_link
model_python_api_link=model_python_api_link
model_notebook_link=model_notebook_link%}
