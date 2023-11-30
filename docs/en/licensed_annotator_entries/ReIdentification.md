{%- capture title -%}
ReIdentification
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
 This annotator can reidentifies obfuscated entities by DeIdentification. It requires the outputs from the deidentification as input. Input columns need to be the deidentified document and the deidentification mappings set with `DeIdentification.setMappingsColumn`.
{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT,CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

# Define the reidentification stage and transform the deidentified documents
reIdentification = medical.ReIdentification()\
    .setInputCols(["aux","deidentified"])\
    .setOutputCol("original")

reid_result = reIdentification.transform(result) # deidentified result

reid_result.select("original.result").show(truncate=False)

# Record date : 2093-01-13 , David Hale , M.D . , Name : Hendrickson Ora ,
# MR # 7194334 Date : 01/13/93 . PCP : Oliveira , 25 years-old , Record date : 2079-11-09 .
# Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[Record date : 2093-01-13 , David Hale , M.D ., , Name : Hendrickson Ora ,
MR # 7194334 Date : 01/13/93 ., PCP : Oliveira , 25 years-old , Record date : 2079-11-09 ., Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 .]|
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_scala_medical -%}

val reIdentification = new ReIdentification()
  .setInputCols(Array("aux", "deidentified"))
  .setOutputCol("original")

val reidResult = reIdentification.transform(result) // deidentified result

reidResult.selectExpr("original.result").show(false)

// Record date : 2093-01-13 , David Hale , M.D . , Name : Hendrickson Ora ,
// MR # 7194334 Date : 01/13/93 . PCP : Oliveira , 25 years-old , Record date : 2079-11-09 .
// Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555."""

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[Record date : 2093-01-13 , David Hale , M.D ., , Name : Hendrickson Ora ,
MR # 7194334 Date : 01/13/93 ., PCP : Oliveira , 25 years-old , Record date : 2079-11-09 ., Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 .]|
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_python_legal -%}
from johnsnowlabs import * 

# Define the reidentification stage and transform the deidentified documents
reIdentification = legal.ReIdentification()\
    .setInputCols(["aux","deidentified"])\
    .setOutputCol("original")

reid_result = reIdentification.transform(result)

reid_result.select('original.result').show(truncate=False)
# Original text:
# THIS STRATEGIC ALLIANCE AGREEMENT ("Agreement") is made and entered into as of December 14, 2016, by and between Hyatt Franchising Latin America, L.L.C. a limited liability company organized and  existing under the laws of the State of Delaware

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[THIS STRATEGIC ALLIANCE AGREEMENT ("Agreement") is made and entered into as of December 14, 2016 , by and between Hyatt Franchising Latin America, L.L.C. a limited liability company organized and existing under the laws of the State of Delaware]|
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_scala_legal -%}
from johnsnowlabs import * 
// Define the reidentification stage and transform the deidentified documents
val reideintification = new ReIdentification()
  .setInputCols(Array("aux", "deidentified"))
  .setOutputCol("original")

val reidResult = reIdentification.transform(result) // deidentified result

reidResult.selectExpr("original.result").show(false)

// Original text:
// THIS STRATEGIC ALLIANCE AGREEMENT ("Agreement") is made and entered into as of December 14, 2016, by and between Hyatt Franchising Latin America, L.L.C. a limited liability company organized and  existing under the laws of the State of Delaware

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[THIS STRATEGIC ALLIANCE AGREEMENT ("Agreement") is made and entered into as of December 14, 2016 , by and between Hyatt Franchising Latin America, L.L.C. a limited liability company organized and existing under the laws of the State of Delaware]|
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}

{%- capture model_python_finance -%}
from johnsnowlabs import nlp, finance

# Define the reidentification stage and transform the deidentified documents
reIdentification = finance.ReIdentification()\
    .setInputCols(["aux","deidentified"])\
    .setOutputCol("original")

reid_result = reIdentification.transform(result)

reid_result.select('original.result').show(truncate=False)

# Original text:
"""Commission file number 000-15867 
_____________________________________
 
CADENCE DESIGN SYSTEMS, INC. 
(Exact name of registrant as specified in its charter)
____________________________________ 
Delaware
 
00-0000000
(State or Other Jurisdiction ofIncorporation or Organization)
 
(I.R.S. EmployerIdentification No.)
2655 Seely Avenue, Building 5,
San Jose,
California
 
95134
(Address of Principal Executive Offices)
 
(Zip Code)
(408)
-943-1234 
(Registrant’s Telephone Number, including Area Code) 
Securities registered pursuant to Section 12(b) of the Act:
Title of Each Class
Trading Symbol(s)
Names of Each Exchange on which Registered
Common Stock, $0.01 par value per share
CDNS
Nasdaq Global Select Market
Securities registered pursuant to Section 12(g) of the Act:"""

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[Commission file number 000-15867 
_____________________________________
 
CADENCE DESIGN SYSTEMS, INC., (Exact name of registrant as specified in its charter)
____________________________________ 
Delaware
 
00-0000000
(State or Other Jurisdiction ofIncorporation or Organization)
 
(I.R.S., EmployerIdentification No., )
2655 Seely Avenue, Building 5,
San Jose,
California
 
95134
(Address of Principal Executive Offices)
 
(Zip Code)<(408)
-943-1234
(Registrant’s Telephone Number, including Area Code) 
Securities registered pursuant to Section 12, (b) of the Act:
Title of Each Class
Trading Symbol, (s)
Names of Each Exchange on which Registered
Common Stock, $0.01 par value per share
CDNS
Nasdaq Global Select Market
Securities registered pursuant to Section 12, (g) of the Act:]|
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}

{%- capture model_scala_finance -%}
// Define the reidentification stage and transform the deidentified documents
val reideintification = new ReIdentification()
  .setInputCols(Array("aux", "deidentified"))
  .setOutputCol("original")

val reidResult = reIdentification.transform(result) // deidentified result

reidResult.selectExpr("original.result").show(false)

# Original text:
"""Commission file number 000-15867 
_____________________________________
 
CADENCE DESIGN SYSTEMS, INC. 
(Exact name of registrant as specified in its charter)
____________________________________ 
Delaware
 
00-0000000
(State or Other Jurisdiction ofIncorporation or Organization)
 
(I.R.S. EmployerIdentification No.)
2655 Seely Avenue, Building 5,
San Jose,
California
 
95134
(Address of Principal Executive Offices)
 
(Zip Code)
(408)
-943-1234 
(Registrant’s Telephone Number, including Area Code) 
Securities registered pursuant to Section 12(b) of the Act:
Title of Each Class
Trading Symbol(s)
Names of Each Exchange on which Registered
Common Stock, $0.01 par value per share
CDNS
Nasdaq Global Select Market
Securities registered pursuant to Section 12(g) of the Act:"""

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[Commission file number 000-15867 
_____________________________________
 
CADENCE DESIGN SYSTEMS, INC., (Exact name of registrant as specified in its charter)
____________________________________ 
Delaware
 
00-0000000
(State or Other Jurisdiction ofIncorporation or Organization)
 
(I.R.S., EmployerIdentification No., )
2655 Seely Avenue, Building 5,
San Jose,
California
 
95134
(Address of Principal Executive Offices)
 
(Zip Code)<(408)
-943-1234
(Registrant’s Telephone Number, including Area Code) 
Securities registered pursuant to Section 12, (b) of the Act:
Title of Each Class
Trading Symbol, (s)
Names of Each Exchange on which Registered
Common Stock, $0.01 par value per share
CDNS
Nasdaq Global Select Market
Securities registered pursuant to Section 12, (g) of the Act:]|
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


{%- endcapture -%}

{%- capture model_api_link -%}
[ReIdentification](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/deid/ReIdentification.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[ReIdentification](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/deid/reIdentification/index.html#sparknlp_jsl.annotator.deid.reIdentification.ReIdentification)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ReIdentification.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical
model_python_finance=model_python_finance
model_scala_finance=model_scala_finance
model_python_legal=model_python_legal
model_scala_legal=model_scala_legal
model_api_link=model_api_link
model_python_api_link=model_python_api_link
model_notebook_link=model_notebook_link
%}
