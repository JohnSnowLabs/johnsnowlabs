{%- capture title -%}
DateNormalizer
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}

This annotator transforms date mentions to a common standard format: YYYY/MM/DD. It is useful when using data from different sources, some times from different countries that has different formats to represent dates.

For the relative dates (next year, past month, etc.), you can define an achor date to create the normalized date by setting the parameters `anchorDateYear`, `anchorDateMonth`, and `anchorDateDay`.

The resultant chunk date will contain a metada indicating whether the normalization was successful or not (True / False). 

Parametres:

- `anchorDateYear`: (Int) Sets an anchor year for the relative dates such as a day after tomorrow. If not set it will use the current year.

- `anchorDateMonth`: (Int) Sets an anchor month for the relative dates such as a day after tomorrow. If not set it will use the current month.

- `anchorDateDay`: (Int) Sets an anchor day of the day for the relative dates such as a day after tomorrow. If not set it will use the current day.

- `outputDateformat`: (string) Select what output format to use. If not set, the dates will be formatted as  `YYYY/MM/DD`. Options are:
  - `eu`: Format the dates as `DD/MM/YYYY`
  - `us`: Format the dates as `MM/DD/YYYY`

- `defaultReplacementDay`: (Int) Defines which value to use for creating the Day Value when original Date-Entity has no Day Information. Defaults to 15.

- `defaultReplacementMonth`: (Int) Defines which value to use for creating the Month Value when original Date-Entity has no Month Information. Defaults to 06.

- `defaultReplacementYear`: (Int) Defines which value to use for creating the Year Value when original Date-Entity has no Year Information. Defaults to 2020.

{%- endcapture -%}

{%- capture model_input_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("original_date")\
    .setOutputCol("document")

doc2chunk = nlp.Doc2Chunk()\
    .setInputCols("document")\
    .setOutputCol("date_chunk")

date_normalizer = medical.DateNormalizer()\
    .setInputCols("date_chunk")\
    .setOutputCol("date")\
    .setAnchorDateYear(2000)

pipeline = nlp.Pipeline(stages=[document_assembler, doc2chunk, date_normalizer])

dates = [
    "08/02/2018",
    "11/2018",
    "11/01/2018",
    "12Mar2021",
    "Jan 30, 2018",
    "13.04.1999",
    "3April 2020",
    "next monday",
    "today",
    "next week",
]
df = spark.createDataFrame(dates, StringType()).toDF("original_date")

result = pipeline.fit(df).transform(df)
result.selectExpr(
    "date.result as normalized_date",
    "original_date",
    "date.metadata[0].normalized as metadata",
).show()

+---------------+-------------+--------+
|normalized_date|original_date|metadata|
+---------------+-------------+--------+
|   [2018/08/02]|   08/02/2018|    true|
|   [2018/11/15]|      11/2018|    true|
|   [2018/11/01]|   11/01/2018|    true|
|   [2021/03/12]|    12Mar2021|    true|
|   [2018/01/30]| Jan 30, 2018|    true|
|   [1999/04/13]|   13.04.1999|    true|
|   [2020/04/03]|  3April 2020|    true|
|   [2000/12/11]|  next monday|    true|
|   [2000/12/06]|        today|    true|
|   [2000/12/13]|    next week|    true|
+---------------+-------------+--------+

{%- endcapture -%}


{%- capture model_scala_medical -%}
import spark.implicits._

val document_assembler = new DocumentAssembler()
    .setInputCol("original_date")
    .setOutputCol("document")

val doc2chunk = new Doc2Chunk()
    .setInputCols("document")
    .setOutputCol("date_chunk")

val date_normalizer = new DateNormalizer()
    .setInputCols("date_chunk")
    .setOutputCol("date")
    .setAnchorDateYear(2000)

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    doc2chunk, 
    date_normalizer
))

val df = Seq(("08/02/2018"),("11/2018"),("11/01/2018"),("next monday"),("today"),("next week")).toDF("original_date")

val result = pipeline.fit(df).transform(df)

+---------------+-------------+--------+
|normalized_date|original_date|metadata|
+---------------+-------------+--------+
|   [2018/08/02]|   08/02/2018|    true|
|   [2018/11/15]|      11/2018|    true|
|   [2018/11/01]|   11/01/2018|    true|
|   [2021/03/12]|    12Mar2021|    true|
|   [2018/01/30]| Jan 30, 2018|    true|
|   [1999/04/13]|   13.04.1999|    true|
|   [2020/04/03]|  3April 2020|    true|
|   [2000/12/11]|  next monday|    true|
|   [2000/12/06]|        today|    true|
|   [2000/12/13]|    next week|    true|
+---------------+-------------+--------+

{%- endcapture -%}

{%- capture model_python_legal -%}
from johnsnowlabs import nlp, legal

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("original_date")\
    .setOutputCol("document")

doc2chunk = nlp.Doc2Chunk()\
    .setInputCols("document")\
    .setOutputCol("date_chunk")

date_normalizer = legal.DateNormalizer()\
    .setInputCols("date_chunk")\
    .setOutputCol("date")\
    .setAnchorDateYear(2000)

pipeline = nlp.Pipeline(stages=[document_assembler, doc2chunk, date_normalizer])

dates = [
    "08/02/2018",
    "11/2018",
    "11/01/2018",
    "12Mar2021",
    "Jan 30, 2018",
    "13.04.1999",
    "3April 2020",
    "next monday",
    "today",
    "next week",
]
df = spark.createDataFrame(dates, StringType()).toDF("original_date")

result = pipeline.fit(df).transform(df)


+---------------+-------------+--------+
|normalized_date|original_date|metadata|
+---------------+-------------+--------+
|   [2018/08/02]|   08/02/2018|    true|
|   [2018/11/15]|      11/2018|    true|
|   [2018/11/01]|   11/01/2018|    true|
|   [2021/03/12]|    12Mar2021|    true|
|   [2018/01/30]| Jan 30, 2018|    true|
|   [1999/04/13]|   13.04.1999|    true|
|   [2020/04/03]|  3April 2020|    true|
|   [2000/12/11]|  next monday|    true|
|   [2000/12/06]|        today|    true|
|   [2000/12/13]|    next week|    true|
+---------------+-------------+--------+

{%- endcapture -%}


{%- capture model_scala_legal -%}
import spark.implicits._

val document_assembler = new DocumentAssembler()
    .setInputCol("original_date")
    .setOutputCol("document")

val doc2chunk = new Doc2Chunk()
    .setInputCols("document")
    .setOutputCol("date_chunk")

val date_normalizer = new DateNormalizer()
    .setInputCols("date_chunk")
    .setOutputCol("date")
    .setAnchorDateYear(2000)

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    doc2chunk, 
    date_normalizer
))
 
val df = Seq(("08/02/2018"),("11/2018"),("11/01/2018"),("next monday"),("today"),("next week")).toDF("original_date")

val result = pipeline.fit(df).transform(df)


+---------------+-------------+--------+
|normalized_date|original_date|metadata|
+---------------+-------------+--------+
|   [2018/08/02]|   08/02/2018|    true|
|   [2018/11/15]|      11/2018|    true|
|   [2018/11/01]|   11/01/2018|    true|
|   [2021/03/12]|    12Mar2021|    true|
|   [2018/01/30]| Jan 30, 2018|    true|
|   [1999/04/13]|   13.04.1999|    true|
|   [2020/04/03]|  3April 2020|    true|
|   [2000/12/11]|  next monday|    true|
|   [2000/12/06]|        today|    true|
|   [2000/12/13]|    next week|    true|
+---------------+-------------+--------+

{%- endcapture -%}

{%- capture model_python_finance -%}

from johnsnowlabs import nlp, finance

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("original_date")\
    .setOutputCol("document")

doc2chunk = nlp.Doc2Chunk()\
    .setInputCols("document")\
    .setOutputCol("date_chunk")

date_normalizer = finance.DateNormalizer()\
    .setInputCols("date_chunk")\
    .setOutputCol("date")\
    .setAnchorDateYear(2000)

pipeline = nlp.Pipeline(stages=[document_assembler, doc2chunk, date_normalizer])

dates = [
    "08/02/2018",
    "11/2018",
    "11/01/2018",
    "12Mar2021",
    "Jan 30, 2018",
    "13.04.1999",
    "3April 2020",
    "next monday",
    "today",
    "next week",
]
df = spark.createDataFrame(dates, StringType()).toDF("original_date")

result = pipeline.fit(df).transform(df)
result.selectExpr(
    "date.result as normalized_date",
    "original_date",
    "date.metadata[0].normalized as metadata",
).show()

+---------------+-------------+--------+
|normalized_date|original_date|metadata|
+---------------+-------------+--------+
|   [2018/08/02]|   08/02/2018|    true|
|   [2018/11/15]|      11/2018|    true|
|   [2018/11/01]|   11/01/2018|    true|
|   [2021/03/12]|    12Mar2021|    true|
|   [2018/01/30]| Jan 30, 2018|    true|
|   [1999/04/13]|   13.04.1999|    true|
|   [2020/04/03]|  3April 2020|    true|
|   [2000/12/11]|  next monday|    true|
|   [2000/12/06]|        today|    true|
|   [2000/12/13]|    next week|    true|
+---------------+-------------+--------+

{%- endcapture -%}


{%- capture model_scala_finance -%}
import spark.implicits._

val document_assembler = new DocumentAssembler()
    .setInputCol("original_date")
    .setOutputCol("document")

val doc2chunk = new Doc2Chunk()
    .setInputCols("document")
    .setOutputCol("date_chunk")

val date_normalizer = new DateNormalizer()
    .setInputCols("date_chunk")
    .setOutputCol("date")
    .setAnchorDateYear(2000)

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    doc2chunk, 
    date_normalizer
))
 
val df = Seq(("08/02/2018"),("11/2018"),("11/01/2018"),("next monday"),("today"),("next week")).toDF("original_date")

val result = pipeline.fit(df).transform(df)


+---------------+-------------+--------+
|normalized_date|original_date|metadata|
+---------------+-------------+--------+
|   [2018/08/02]|   08/02/2018|    true|
|   [2018/11/15]|      11/2018|    true|
|   [2018/11/01]|   11/01/2018|    true|
|   [2021/03/12]|    12Mar2021|    true|
|   [2018/01/30]| Jan 30, 2018|    true|
|   [1999/04/13]|   13.04.1999|    true|
|   [2020/04/03]|  3April 2020|    true|
|   [2000/12/11]|  next monday|    true|
|   [2000/12/06]|        today|    true|
|   [2000/12/13]|    next week|    true|
+---------------+-------------+--------+

{%- endcapture -%}

{%- capture model_api_link -%}
[DateNormalizer](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/normalizer/DateNormalizer.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[DateNormalizer](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/normalizer/date_normalizer/index.html#sparknlp_jsl.annotator.normalizer.date_normalizer.DateNormalizer)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[DateNormalizerNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/DateNormalizer.ipynb)
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
model_notebook_link=model_notebook_link
%}
