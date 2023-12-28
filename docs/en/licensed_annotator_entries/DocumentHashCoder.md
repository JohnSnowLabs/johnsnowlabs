{%- capture title -%}
DocumentHashCoder
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}

This annotator can replace dates in a column of `DOCUMENT` type according with the hash code of any other column. It uses the hash of the specified column and creates a new document column containing the day shift information. In sequence, the `DeIdentification` annotator deidentifies the document with the shifted date information. 

If the specified column contains strings that can be parsed to integers, use those numbers to make the shift in the data accordingly.

Parametres:

- `PatientIdColumn` *(String)*: Name of the column containing patient ID.

- `setDateShiftColumn` *(String)*: Sets column to be used for hash or predefined shift.

- `setNewDateShift` *(String)*: Sets column that has a reference of where chunk begins.

- `setRangeDays` *(int)*: Sets the range of dates to be sampled from.

- `setSeed` *(int)*: Sets the seed for random number generator.

{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_output_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical
import pandas as pd

data = pd.DataFrame(
    {'patientID' : ['A001', 'A001', 
                    'A003', 'A003'],
     'text' : ['Chris Brown was discharged on 10/02/2022', 
               'Mark White was discharged on 10/04/2022', 
               'John was discharged on 15/03/2022',
               'John Moore was discharged on 15/12/2022'
              ],
     'dateshift' : ['10', '10', 
                    '30', '30']
    }
)

my_input_df = spark.createDataFrame(data)

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

documentHasher = medical.DocumentHashCoder()\
    .setInputCols("document")\
    .setOutputCol("document2")\
    .setPatientIdColumn("patientID")\
    .setNewDateShift("shift_days")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["document2"])\
    .setOutputCol("token")

embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["document2", "token"])\
    .setOutputCol("word_embeddings")

clinical_ner = medical.NerModel\
    .pretrained("ner_deid_subentity_augmented", "en", "clinical/models")\
    .setInputCols(["document2","token", "word_embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["document2", "token", "ner"])\
    .setOutputCol("ner_chunk")

de_identification = medical.DeIdentification() \
    .setInputCols(["ner_chunk", "token", "document2"]) \
    .setOutputCol("deid_text") \
    .setMode("obfuscate") \
    .setObfuscateDate(True) \
    .setDateTag("DATE") \
    .setLanguage("en") \
    .setObfuscateRefSource('faker') \
    .setUseShifDays(True)\
    .setRegion('us')

pipeline = nlp.Pipeline().setStages([
    documentAssembler,
    documentHasher,
    tokenizer,
    embeddings,
    clinical_ner,
    ner_converter,
    de_identification

])

empty_data = spark.createDataFrame([["", ""]]).toDF("text", "patientID")
pipeline_model = pipeline.fit(empty_data)

output = pipeline_model.transform(my_input_df)
output.select('patientID','text', 'deid_text.result').show(truncate = False)

+---------+----------------------------------------+---------------------------------------------+
|patientID|text                                    |result                                       |
+---------+----------------------------------------+---------------------------------------------+
|A001     |Chris Brown was discharged on 10/02/2022|[Aldona Bar was discharged on 05/18/2022]    |
|A001     |Mark White was discharged on 02/28/2020 |[Leta Speller was discharged on 10/14/2019]  |
|A002     |John was discharged on 03/15/2022       |[Lonia Blood was discharged on 01/19/2022]   |
|A002     |John Moore was discharged on 12/31/2022 |[Murriel Hopper was discharged on 11/06/2022]|
+---------+----------------------------------------+---------------------------------------------+

{%- endcapture -%}

{%- capture model_python_finance -%}
from johnsnowlabs import nlp, finance
import pandas as pd

data = pd.DataFrame(
    {'patientID' : ['A001', 'A001', 
                    'A003', 'A003'],
     'text' : ['Chris Brown was discharged on 10/02/2022', 
               'Mark White was discharged on 10/04/2022', 
               'John was discharged on 15/03/2022',
               'John Moore was discharged on 15/12/2022'
              ],
     'dateshift' : ['10', '10', 
                    '30', '30']
    }
)

my_input_df = spark.createDataFrame(data)

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

documentHasher = finance.DocumentHashCoder()\
    .setInputCols("document")\
    .setOutputCol("document2")\
    .setPatientIdColumn("patientID")\
    .setNewDateShift("shift_days")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["document2"])\
    .setOutputCol("token")

embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["document2", "token"])\
    .setOutputCol("word_embeddings")

clinical_ner = finance.NerModel\
    .pretrained("ner_deid_subentity_augmented", "en", "clinical/models")\
    .setInputCols(["document2","token", "word_embeddings"])\
    .setOutputCol("ner")

ner_converter = finance.NerConverterInternal()\
    .setInputCols(["document2", "token", "ner"])\
    .setOutputCol("ner_chunk")

de_identification = finance.DeIdentification() \
    .setInputCols(["ner_chunk", "token", "document2"]) \
    .setOutputCol("deid_text") \
    .setMode("obfuscate") \
    .setObfuscateDate(True) \
    .setDateTag("DATE") \
    .setLanguage("en") \
    .setObfuscateRefSource('faker') \
    .setUseShifDays(True)\
    .setRegion('us')

pipeline = nlp.Pipeline().setStages([
    documentAssembler,
    documentHasher,
    tokenizer,
    embeddings,
    clinical_ner,
    ner_converter,
    de_identification

])

empty_data = spark.createDataFrame([["", ""]]).toDF("text", "patientID")
pipeline_model = pipeline.fit(empty_data)

output = pipeline_model.transform(my_input_df)
output.select('patientID','text', 'deid_text.result').show(truncate = False)

+---------+----------------------------------------+----------------------------------------------+
|patientID|text                                    |result                                        |
+---------+----------------------------------------+----------------------------------------------+
|A001     |Chris Brown was discharged on 10/02/2022|[Andreas Newport was discharged on 04/09/2022]|
|A001     |Mark White was discharged on 02/28/2020 |[Kara Dies was discharged on 09/05/2019]      |
|A002     |John was discharged on 03/15/2022       |[Lane Hacker was discharged on 02/17/2022]    |
|A002     |John Moore was discharged on 12/31/2022 |[Orlena Sheldon was discharged on 12/05/2022] |
+---------+----------------------------------------+----------------------------------------------+

{%- endcapture -%}

{%- capture model_python_legal -%}
from johnsnowlabs import nlp, legal
import pandas as pd

data = pd.DataFrame(
    {'patientID' : ['A001', 'A001', 
                    'A003', 'A003'],
     'text' : ['Chris Brown was discharged on 10/02/2022', 
               'Mark White was discharged on 10/04/2022', 
               'John was discharged on 15/03/2022',
               'John Moore was discharged on 15/12/2022'
              ],
     'dateshift' : ['10', '10', 
                    '30', '30']
    }
)

my_input_df = spark.createDataFrame(data)

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

documentHasher = legal.DocumentHashCoder()\
    .setInputCols("document")\
    .setOutputCol("document2")\
    .setPatientIdColumn("patientID")\
    .setNewDateShift("shift_days")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["document2"])\
    .setOutputCol("token")

embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["document2", "token"])\
    .setOutputCol("word_embeddings")

clinical_ner = legal.NerModel\
    .pretrained("ner_deid_subentity_augmented", "en", "clinical/models")\
    .setInputCols(["document2","token", "word_embeddings"])\
    .setOutputCol("ner")

ner_converter = legal.NerConverterInternal()\
    .setInputCols(["document2", "token", "ner"])\
    .setOutputCol("ner_chunk")

de_identification = legal.DeIdentification() \
    .setInputCols(["ner_chunk", "token", "document2"]) \
    .setOutputCol("deid_text") \
    .setMode("obfuscate") \
    .setObfuscateDate(True) \
    .setDateTag("DATE") \
    .setLanguage("en") \
    .setObfuscateRefSource('faker') \
    .setUseShifDays(True)\
    .setRegion('us')

pipeline = nlp.Pipeline().setStages([
    documentAssembler,
    documentHasher,
    tokenizer,
    embeddings,
    clinical_ner,
    ner_converter,
    de_identification

])

empty_data = spark.createDataFrame([["", ""]]).toDF("text", "patientID")
pipeline_model = pipeline.fit(empty_data)

output = pipeline_model.transform(my_input_df)
output.select('patientID','text', 'deid_text.result').show(truncate = False)

+---------+----------------------------------------+----------------------------------------------+
|patientID|text                                    |result                                        |
+---------+----------------------------------------+----------------------------------------------+
|A001     |Chris Brown was discharged on 10/02/2022|[Andreas Newport was discharged on 04/09/2022]|
|A001     |Mark White was discharged on 02/28/2020 |[Kara Dies was discharged on 09/05/2019]      |
|A002     |John was discharged on 03/15/2022       |[Lane Hacker was discharged on 02/17/2022]    |
|A002     |John Moore was discharged on 12/31/2022 |[Orlena Sheldon was discharged on 12/05/2022] |
+---------+----------------------------------------+----------------------------------------------+

{%- endcapture -%}

{%- capture model_scala_medical -%}

import spark.implicits._
  
val data = Seq(
  ("A001", "Chris Brown was discharged on 10/02/2022"),
  ("A001", "Mark White was discharged on 02/28/2020"),
  ("A002", "John was discharged on 03/15/2022"),
  ("A002", "John Moore was discharged on 12/31/2022")
)

val columns = Seq("patientID", "text")
val myInputDF: DataFrame = spark.createDataFrame(data).toDF(columns: _*)


val my_input_df = spark.createDataFrame(data) 

val documentAssembler = new DocumentAssembler()
    .setInputCol("text") 
    .setOutputCol("document") 

val documentHasher = new DocumentHashCoder()
    .setInputCols("document") 
    .setOutputCol("document2") 
    .setPatientIdColumn("patientID") 
    .setNewDateShift("shift_days") 

val tokenizer = new Tokenizer()
    .setInputCols("document2") 
    .setOutputCol("token") 

val embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
    .setInputCols(Array("document2","token")) 
    .setOutputCol("word_embeddings") 

val clinical_ner = MedicalNerModel.pretrained("ner_deid_subentity_augmented","en","clinical/models")
    .setInputCols(Array("document2","token","word_embeddings")) 
    .setOutputCol("ner") 

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("document2","token","ner")) 
    .setOutputCol("ner_chunk") 

val de_identification = new DeIdentification()
    .setInputCols(Array("ner_chunk","token","document2")) 
    .setOutputCol("deid_text") 
    .setMode("obfuscate") 
    .setObfuscateDate(true) 
    .setDateTag("DATE") 
    .setLanguage("en") 
    .setObfuscateRefSource("faker") 
    .setUseShifDays(true) 
    .setRegion("us") 

val pipeline = new Pipeline().setStages(Array(
      documentAssembler,
      documentHasher,
      tokenizer,
      embeddings,
      clinicalNer,
      nerConverter,
      deIdentification
))

val emptyData = Seq(("", "")).toDF("text", "patientID")

val pipelineModel = pipeline.fit(emptyData)
val result = pipelineModel.transform(myInputDF)

+---------+----------------------------------------+----------------------------------------------+
|patientID|text                                    |result                                        |
+---------+----------------------------------------+----------------------------------------------+
|A001     |Chris Brown was discharged on 10/02/2022|[Andreas Newport was discharged on 04/09/2022]|
|A001     |Mark White was discharged on 02/28/2020 |[Kara Dies was discharged on 09/05/2019]      |
|A002     |John was discharged on 03/15/2022       |[Lane Hacker was discharged on 02/17/2022]    |
|A002     |John Moore was discharged on 12/31/2022 |[Orlena Sheldon was discharged on 12/05/2022] |
+---------+----------------------------------------+----------------------------------------------+

{%- endcapture -%}

{%- capture model_scala_finance -%}

import spark.implicits._
  
val data = Seq(
  ("A001", "Chris Brown was discharged on 10/02/2022"),
  ("A001", "Mark White was discharged on 02/28/2020"),
  ("A002", "John was discharged on 03/15/2022"),
  ("A002", "John Moore was discharged on 12/31/2022")
)

val columns = Seq("patientID", "text")
val myInputDF: DataFrame = spark.createDataFrame(data).toDF(columns: _*)

val my_input_df = spark.createDataFrame(data) 

val documentAssembler = new DocumentAssembler()
    .setInputCol("text") 
    .setOutputCol("document") 

val documentHasher = new DocumentHashCoder()
    .setInputCols("document") 
    .setOutputCol("document2") 
    .setPatientIdColumn("patientID") 
    .setNewDateShift("shift_days") 

val tokenizer = new Tokenizer()
    .setInputCols("document2")
    .setOutputCol("token") 

val embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
    .setInputCols(Array("document2","token")) 
    .setOutputCol("word_embeddings") 

val clinical_ner = FinanceNerModel.pretrained("ner_deid_subentity_augmented","en","clinical/models")
    .setInputCols(Array("document2","token","word_embeddings")) 
    .setOutputCol("ner") 

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("document2","token","ner")) 
    .setOutputCol("ner_chunk") 

val de_identification = new DeIdentification()
    .setInputCols(Array("ner_chunk","token","document2")) 
    .setOutputCol("deid_text") 
    .setMode("obfuscate") 
    .setObfuscateDate(true) 
    .setDateTag("DATE") 
    .setLanguage("en") 
    .setObfuscateRefSource("faker") 
    .setUseShifDays(true) 
    .setRegion("us") 

val pipeline = new Pipeline().setStages(Array(
      documentAssembler,
      documentHasher,
      tokenizer,
      embeddings,
      clinicalNer,
      nerConverter,
      deIdentification
))

val emptyData = Seq(("", "")).toDF("text", "patientID")
val pipelineModel = pipeline.fit(emptyData)
val result = pipelineModel.transform(myInputDF)

+---------+----------------------------------------+----------------------------------------------+
|patientID|text                                    |result                                        |
+---------+----------------------------------------+----------------------------------------------+
|A001     |Chris Brown was discharged on 10/02/2022|[Andreas Newport was discharged on 04/09/2022]|
|A001     |Mark White was discharged on 02/28/2020 |[Kara Dies was discharged on 09/05/2019]      |
|A002     |John was discharged on 03/15/2022       |[Lane Hacker was discharged on 02/17/2022]    |
|A002     |John Moore was discharged on 12/31/2022 |[Orlena Sheldon was discharged on 12/05/2022] |
+---------+----------------------------------------+----------------------------------------------+

{%- endcapture -%}

{%- capture model_scala_legal -%}

import spark.implicits._
  
val data = Seq(
  ("A001", "Chris Brown was discharged on 10/02/2022"),
  ("A001", "Mark White was discharged on 02/28/2020"),
  ("A002", "John was discharged on 03/15/2022"),
  ("A002", "John Moore was discharged on 12/31/2022")
)

val columns = Seq("patientID", "text")
val myInputDF: DataFrame = spark.createDataFrame(data).toDF(columns: _*)


val my_input_df = spark.createDataFrame(data) 

val documentAssembler = new DocumentAssembler()
    .setInputCol("text") 
    .setOutputCol("document") 

val documentHasher = new DocumentHashCoder()
    .setInputCols("document") 
    .setOutputCol("document2") 
    .setPatientIdColumn("patientID") 
    .setNewDateShift("shift_days") 

val tokenizer = new Tokenizer()
    .setInputCols("document2")
    .setOutputCol("token") 

val embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
    .setInputCols(Array("document2","token")) 
    .setOutputCol("word_embeddings") 

val clinical_ner = LegalNerModel.pretrained("ner_deid_subentity_augmented","en","clinical/models")
    .setInputCols(Array("document2","token","word_embeddings")) 
    .setOutputCol("ner") 

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("document2","token","ner")) 
    .setOutputCol("ner_chunk") 

val de_identification = new DeIdentification()
    .setInputCols(Array("ner_chunk","token","document2")) 
    .setOutputCol("deid_text") 
    .setMode("obfuscate") 
    .setObfuscateDate(true) 
    .setDateTag("DATE") 
    .setLanguage("en") 
    .setObfuscateRefSource("faker") 
    .setUseShifDays(true) 
    .setRegion("us") 

val pipeline = new Pipeline().setStages(Array(
      documentAssembler,
      documentHasher,
      tokenizer,
      embeddings,
      clinicalNer,
      nerConverter,
      deIdentification
))

val emptyData = Seq(("", "")).toDF("text", "patientID")

val pipelineModel = pipeline.fit(emptyData)
val result = pipelineModel.transform(myInputDF)

+---------+----------------------------------------+----------------------------------------------+
|patientID|text                                    |result                                        |
+---------+----------------------------------------+----------------------------------------------+
|A001     |Chris Brown was discharged on 10/02/2022|[Andreas Newport was discharged on 04/09/2022]|
|A001     |Mark White was discharged on 02/28/2020 |[Kara Dies was discharged on 09/05/2019]      |
|A002     |John was discharged on 03/15/2022       |[Lane Hacker was discharged on 02/17/2022]    |
|A002     |John Moore was discharged on 12/31/2022 |[Orlena Sheldon was discharged on 12/05/2022] |
+---------+----------------------------------------+----------------------------------------------+

{%- endcapture -%}

{%- capture model_api_link -%}
[DocumentHashCoder](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/deid/DocumentHashCoder.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[DocumentHashCoder](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/deid/doccument_hashcoder/index.html#sparknlp_jsl.annotator.deid.doccument_hashcoder.DocumentHashCoder)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[DocumentHashCoderNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/DocumentHashCoder.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_python_finance=model_python_finance
model_python_legal=model_python_legal
model_scala_medical=model_scala_medical
model_scala_finance=model_scala_finance
model_scala_legal=model_scala_legal
model_api_link=model_api_link
model_python_api_link=model_python_api_link
model_notebook_link=model_notebook_link
%}
