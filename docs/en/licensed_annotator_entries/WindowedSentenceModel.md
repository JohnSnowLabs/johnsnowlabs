{%- capture title -%}
WindowedSentenceModel
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
This annotator that helps you to merge the previous and following sentences of a given piece of text, so that you add the context surrounding them. This is super useful for especially context-rich analyses that require a deeper understanding of the language being used.

Inferring the class from sentence X may be a much harder task sometime, due to the lack of context, than to infer the class of sentence X-1 + sentence X + sentence X+1. In this example, the window is 1, that’s why we augment sentence with 1 neighbour from behind and another from ahead. Window size can be configured so that each piece of text/sentence get a number of previous and posterior sentences as context, equal to the windows size.

Parameters:

- `setWindowSize`: Sets size of the sliding window.

- `setGlueString`: Sets string to use to join the neighboring elements together. 
{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_output_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_python_medical -%}

from johnsnowlabs import medical, nlp

documentAssembler =  nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector =  nlp.SentenceDetector()\
    .setInputCols("document")\
    .setOutputCol("sentence")

windowedSentence1 =  medical.WindowedSentenceModel()\
    .setWindowSize(1)\
    .setInputCols("sentence")\
    .setOutputCol("window_1")

windowedSentence2 =  medical.WindowedSentenceModel()\
    .setWindowSize(2)\
    .setInputCols("sentence")\
    .setOutputCol("window_2")

pipeline = nlp.Pipeline(stages=[
    documentAssembler, 
    sentenceDetector, 
    windowedSentence1, 
    windowedSentence2
    ])


sample_text = """The patient was admitted on Monday. 
She has a right-sided pleural effusion for thoracentesis. 
Her Coumadin was placed on hold.
A repeat echocardiogram was checked. 
She was started on prophylaxis for DVT. 
Her CT scan from March 2006 prior to her pericardectomy. 
It already shows bilateral plural effusions."""

data = spark.createDataFrame([[sample_text]]).toDF("text")

result = pipeline.fit(data).transform(data)

# Example results

result.select(F.explode('window_1')).select('col.result').show(truncate=False)

+---------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------+
|The patient was admitted on Monday. She has a right-sided pleural effusion for thoracentesis.                                                |
|The patient was admitted on Monday. She has a right-sided pleural effusion for thoracentesis. Her Coumadin was placed on hold.               |
|She has a right-sided pleural effusion for thoracentesis. Her Coumadin was placed on hold. A repeat echocardiogram was checked.              |
|Her Coumadin was placed on hold. A repeat echocardiogram was checked. She was started on prophylaxis for DVT.                                |
|A repeat echocardiogram was checked. She was started on prophylaxis for DVT. Her CT scan from March 2006 prior to her pericardectomy.        |
|She was started on prophylaxis for DVT. Her CT scan from March 2006 prior to her pericardectomy. It already shows bilateral plural effusions.|
|Her CT scan from March 2006 prior to her pericardectomy. It already shows bilateral plural effusions.                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------+

result.select(F.explode('window_2')).select('col.result').show(truncate=False)

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|The patient was admitted on Monday. She has a right-sided pleural effusion for thoracentesis. Her Coumadin was placed on hold.                                                                                                  |
|The patient was admitted on Monday. She has a right-sided pleural effusion for thoracentesis. Her Coumadin was placed on hold. A repeat echocardiogram was checked.                                                             |
|The patient was admitted on Monday. She has a right-sided pleural effusion for thoracentesis. Her Coumadin was placed on hold. A repeat echocardiogram was checked. She was started on prophylaxis for DVT.                     |
|She has a right-sided pleural effusion for thoracentesis. Her Coumadin was placed on hold. A repeat echocardiogram was checked. She was started on prophylaxis for DVT. Her CT scan from March 2006 prior to her pericardectomy.|
|Her Coumadin was placed on hold. A repeat echocardiogram was checked. She was started on prophylaxis for DVT. Her CT scan from March 2006 prior to her pericardectomy. It already shows bilateral plural effusions.             |
|A repeat echocardiogram was checked. She was started on prophylaxis for DVT. Her CT scan from March 2006 prior to her pericardectomy. It already shows bilateral plural effusions.                                              |
|She was started on prophylaxis for DVT. Her CT scan from March 2006 prior to her pericardectomy. It already shows bilateral plural effusions.                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


{%- endcapture -%}


{%- capture model_scala_medical -%}

import spark.implicits._

val documentAssembler =  new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector =  new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val windowedSentence1 =  new WindowedSentenceModel()
    .setWindowSize(1)
    .setInputCols("sentence")
    .setOutputCol("window_1")

val windowedSentence2 =  new WindowedSentenceModel()
    .setWindowSize(2)
    .setInputCols("sentence")
    .setOutputCol("window_2")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, 
    sentenceDetector, 
    windowedSentence1, 
    windowedSentence2
))


val testDataset = Seq("The patient was admitted on Monday. 
She has a right-sided pleural effusion for thoracentesis. 
Her Coumadin was placed on hold.
A repeat echocardiogram was checked. 
She was started on prophylaxis for DVT. 
Her CT scan from March 2006 prior to her pericardectomy. 
It already shows bilateral plural effusions.").toDF("text")

val result = pipeline.fit(testDataset).transform(testDataset)

// Result

// window 1

+---------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------+
|The patient was admitted on Monday. She has a right-sided pleural effusion for thoracentesis.                                                |
|The patient was admitted on Monday. She has a right-sided pleural effusion for thoracentesis. Her Coumadin was placed on hold.               |
|She has a right-sided pleural effusion for thoracentesis. Her Coumadin was placed on hold. A repeat echocardiogram was checked.              |
|Her Coumadin was placed on hold. A repeat echocardiogram was checked. She was started on prophylaxis for DVT.                                |
|A repeat echocardiogram was checked. She was started on prophylaxis for DVT. Her CT scan from March 2006 prior to her pericardectomy.        |
|She was started on prophylaxis for DVT. Her CT scan from March 2006 prior to her pericardectomy. It already shows bilateral plural effusions.|
|Her CT scan from March 2006 prior to her pericardectomy. It already shows bilateral plural effusions.                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------+

// window 2

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|The patient was admitted on Monday. She has a right-sided pleural effusion for thoracentesis. Her Coumadin was placed on hold.                                                                                                  |
|The patient was admitted on Monday. She has a right-sided pleural effusion for thoracentesis. Her Coumadin was placed on hold. A repeat echocardiogram was checked.                                                             |
|The patient was admitted on Monday. She has a right-sided pleural effusion for thoracentesis. Her Coumadin was placed on hold. A repeat echocardiogram was checked. She was started on prophylaxis for DVT.                     |
|She has a right-sided pleural effusion for thoracentesis. Her Coumadin was placed on hold. A repeat echocardiogram was checked. She was started on prophylaxis for DVT. Her CT scan from March 2006 prior to her pericardectomy.|
|Her Coumadin was placed on hold. A repeat echocardiogram was checked. She was started on prophylaxis for DVT. Her CT scan from March 2006 prior to her pericardectomy. It already shows bilateral plural effusions.             |
|A repeat echocardiogram was checked. She was started on prophylaxis for DVT. Her CT scan from March 2006 prior to her pericardectomy. It already shows bilateral plural effusions.                                              |
|She was started on prophylaxis for DVT. Her CT scan from March 2006 prior to her pericardectomy. It already shows bilateral plural effusions.                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}


{%- capture model_python_legal -%}

from johnsnowlabs import nlp, legal
from pyspark.sql import functions as F

doc_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("isolated_sentence")

context_window = legal.WindowedSentenceModel()\
    .setInputCols(["isolated_sentence"])\
    .setOutputCol("window")\
    .setWindowSize(1)

window_splitting_pipeline = nlp.Pipeline(stages=[doc_assembler, sentence_detector, context_window])

window_splitting_model = window_splitting_pipeline.fit(df)

window_splitting_lp = nlp.LightPipeline(window_splitting_model)

## Result

['1  \nMUTUAL NONDISCLOSURE AGREEMENT  \nThis Mutual Nondisclosure Agreement (the “Agreement”) is made on _________ (“Effective  \nDate”) by and between:  \n(1) John Snow Labs, a Delaware corporation, registered at 16192 Coastal Highway,  \nLewes, Delaware 19958 (“John Snow Labs”), and   \n(2) Achiles, S.L, a Spanish corporation, registered at Gran Via, 2º floor, Offices 9\nand 10.(“Company”),  \n(each a “party” and together the “parties”). Recitals:  \nJohn Snow Labs and Company intend to explore the possibility of a business relationship  \nbetween each other, whereby each party (“Discloser”) may disclose sensitive information to the  \nother party (“Recipient”).',
 '1  \nMUTUAL NONDISCLOSURE AGREEMENT  \nThis Mutual Nondisclosure Agreement (the “Agreement”) is made on _________ (“Effective  \nDate”) by and between:  \n(1) John Snow Labs, a Delaware corporation, registered at 16192 Coastal Highway,  \nLewes, Delaware 19958 (“John Snow Labs”), and   \n(2) Achiles, S.L, a Spanish corporation, registered at Gran Via, 2º floor, Offices 9\nand 10.(“Company”),  \n(each a “party” and together the “parties”). Recitals:  \nJohn Snow Labs and Company intend to explore the possibility of a business relationship  \nbetween each other, whereby each party (“Discloser”) may disclose sensitive information to the  \nother party (“Recipient”). The parties agree as follows:',
 'Recitals:  \nJohn Snow Labs and Company intend to explore the possibility of a business relationship  \nbetween each other, whereby each party (“Discloser”) may disclose sensitive information to the  \nother party (“Recipient”). The parties agree as follows: 1. Definition.',]

{%- endcapture -%}


{%- capture model_api_link -%}
[WindowedSentenceModel](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/windowed/WindowedSentenceModel.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[WindowedSentenceModel](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/windowed/windowed_sentence/index.html#sparknlp_jsl.annotator.windowed.windowed_sentence.WindowedSentenceModel)
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
model_api_link=model_api_link
model_python_api_link=model_python_api_link
%}
