{%- capture title -%}
RegexMatcherInternal
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
The **`RegexMatcherInternal`** class implements an internal annotator approach to match a set of regular expressions with a provided entity. This approach is utilized for associating specific patterns within text data with predetermined entities, such as dates, mentioned within the text.

The class allows users to define rules using regular expressions paired with entities, offering flexibility in customization. These rules can either be directly set using the `setRules` method, with a specified delimiter, or loaded from an external file using the `setExternalRules` method.

Additionally, users can specify parameters such as the matching strategy (`MATCH_FIRST`, `MATCH_ALL`, or `MATCH_COMPLETE`) to control how matches are handled. The output annotation type is `CHUNK`, with input annotation types supporting `DOCUMENT`. This class provides a versatile tool for implementing entity recognition based on user-defined patterns within text data.


A rule consists of a regex pattern and an identifier, delimited by a character of choice. An example could be `"\\d{4}\\/\\d\\d\\/\\d\\d,date"` which will match strings like `"1970/01/01"` to the identifier `"date"`.

Parametres:

- `strategy`: Can be either `MATCH_FIRST`, `MATCH_ALL`, `MATCH_COMPLETE`, by default `MATCH_ALL`.
- `rules`: Regex rules to match the identifier with.
- `delimiter`: Delimiter for rules provided with setRules.
- `externalRules`: external resource to rules, needs `delimiter` in options.


See [Spark NLP Workshop](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/40.Rule_Based_Entity_Matchers.ipynb) for more examples of usage.
{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR #719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com."""

data = spark.createDataFrame([[text]]).toDF("text")

rules = '''
(\d{1,3}\.){3}\d{1,3}~IPADDR
\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{2}|\d{2}/\d{2}/\d{2}~DATE
'''

with open('./rules/regex_rules.txt', 'w') as f:
    f.write(rules)

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

regex_matcher_internal = medical.RegexMatcherInternal()\
    .setInputCols('document')\
    .setStrategy("MATCH_ALL")\
    .setOutputCol("regex_matches")\
    .setExternalRules(path='./rules/regex_rules.txt', delimiter='~')

nlpPipeline = nlp.Pipeline(
    stages=[
        document_assembler,
        regex_matcher_internal
])

result = nlpPipeline.fit(data).transform(data)

# result
+--------------+-----+---+---------+
|  regex_result|begin|end|ner_label|
+--------------+-----+---+---------+
|    2093-01-13|   38| 47|     DATE|
|203.120.223.13|   97|110|   IPADDR|
|      01/13/93|  188|195|     DATE|
+--------------+-----+---+---------+
{%- endcapture -%}


{%- capture model_scala_medical -%}

//rules = '''
//(\d{1,3}\.){3}\d{1,3}~IPADDR
//\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{2}|\d{2}/\d{2}/\d{2}~DATE
//'''
//
//with open('./rules/regex_rules.txt', 'w') as f:
//    f.write(rules)

val text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR #719435.
  |Dr. John Green, ID: 1231511863, IP 203.120.223.13
  |He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93
  |Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
  |Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com.""".stripMargin

import spark.implicits._

val data = Seq(text).toDF("text")

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val regexMatcher = new RegexMatcher()
  .setInputCols("document")
  .setStrategy("MATCH_ALL")
  .setOutputCol("regex_matches")
  .setExternalRulesPath("./rules/regex_rules.txt")
  .setDelimiter("~")

val nlpPipeline = new Pipeline()
  .setStages(Array(documentAssembler, regexMatcher))

val result = nlpPipeline.fit(data).transform(data)

# result
+--------------+-----+---+---------+
|  regex_result|begin|end|ner_label|
+--------------+-----+---+---------+
|    2093-01-13|   38| 47|     DATE|
|203.120.223.13|   97|110|   IPADDR|
|      01/13/93|  188|195|     DATE|
+--------------+-----+---+---------+

{%- endcapture -%}


{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical%}
