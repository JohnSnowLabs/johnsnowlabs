{%- capture title -%}
ContextualParser
{%- endcapture -%}

{%- capture approach -%}
approach
{%- endcapture -%}

{%- capture approach_description -%}
Creates a model, that extracts entity from a document based on user defined rules.
Rule matching is based on a RegexMatcher defined in a JSON file. It is set through the parameter setJsonPath()
In this JSON file, regex is defined that you want to match along with the information that will output on metadata
field. Additionally, a dictionary can be provided with `setDictionary` to map extracted entities
to a unified representation. The first column of the dictionary file should be the representation with following
columns the possible matches.

Parametres;

- `inputCols`: The name of the columns containing the input annotations. It can read either a String column or an Array.
- `outputCol`: The name of the column in Document type that is generated. We can specify only one column here.
- `jsonPath`: Path to json file containing regex patterns and rules to match the entities.
- `dictionary`: Path to dictionary file in tsv or csv format.
- `caseSensitive`: Whether to use case sensitive when matching values.
- `prefixAndSuffixMatch`: Whether to match both prefix and suffix to annotate the match.
- `optionalContextRules`: When set to true, it will output regex match regardless of context matches.
- `shortestContextMatch`: When set to true, it will stop finding for matches when prefix/suffix data is found in the text.
- `completeContextMatch`: Whether to do an exact match of prefix and suffix.

All the parameters can be set using the corresponding set method in camel case. For example, `.setInputcols()`.

{%- endcapture -%}

{%- capture approach_input_anno -%}
DOCUMENT, TOKEN
{%- endcapture -%}

{%- capture approach_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture approach_python_medical -%}
from johnsnowlabs import nlp, medical

# An example JSON file `regex_token.json` can look like this:
#
# {
#    "entity": "Stage",
#    "ruleScope": "sentence",
#    "regex": "[cpyrau]?[T][0-9X?][a-z^cpyrau]",
#    "matchScope": "token"
#  }
#
# Which means to extract the stage code on a sentence level.
# An example pipeline could then be defined like this
# Pipeline could then be defined like this

documentAssembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector() \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

contextualParser = medical.ContextualParserApproach() \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("entity") \
    .setJsonPath("/path/to/regex_token.json") \
    .setCaseSensitive(True) \
    .setContextMatch(False)

pipeline = nlp.Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    contextualParser
  ])

# Define the parser (json file needs to be provided)
data = spark.createDataFrame([["A patient has liver metastases pT1bN0M0 and the T5 primary site may be colon or... "]]).toDF("text")

result = pipeline.fit(data).transform(data)

# Show Results
result.selectExpr("explode(entity)").show(5, truncate=False)
+-------------------------------------------------------------------------------------------------------------------------+
|col                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------+
|{chunk, 32, 39, pT1bN0M0, {field -> Stage, normalized -> , confidenceValue -> 0.13, hits -> regex, sentence -> 0}, []}   |
|{chunk, 49, 50, T5, {field -> Stage, normalized -> , confidenceValue -> 0.13, hits -> regex, sentence -> 0}, []}         |
|{chunk, 148, 156, cT4bcN2M1, {field -> Stage, normalized -> , confidenceValue -> 0.13, hits -> regex, sentence -> 1}, []}|
|{chunk, 189, 194, T?N3M1, {field -> Stage, normalized -> , confidenceValue -> 0.13, hits -> regex, sentence -> 2}, []}   |
|{chunk, 316, 323, pT1bN0M0, {field -> Stage, normalized -> , confidenceValue -> 0.13, hits -> regex, sentence -> 3}, []} |
+-------------------------------------------------------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture approach_python_legal -%}
from johnsnowlabs import nlp, legal

# An example JSON file `regex_token.json` can look like this:
#
# {
#    "entity": "Stage",
#    "ruleScope": "sentence",
#    "regex": "[cpyrau]?[T][0-9X?][a-z^cpyrau]",
#    "matchScope": "token"
#  }
#
# Which means to extract the stage code on a sentence level.
# An example pipeline could then be defined like this
# Pipeline could then be defined like this

documentAssembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector() \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

contextualParser = legal.ContextualParserApproach() \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("entity") \
    .setJsonPath("/path/to/regex_token.json") \
    .setCaseSensitive(True) \
    .setContextMatch(False)

pipeline = nlp.Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    contextualParser
  ])

# Define the parser (json file needs to be provided)
data = spark.createDataFrame([["Peter Parker is a nice guy and lives in New York . Bruce Wayne is also a nice guy and lives in San Antonio and Gotham City ."]]).toDF("text")

result = pipeline.fit(data).transform(data)

# Show Results
result.selectExpr("explode(entity)").show(5, truncate=False)

+---------------------------------------------------------------+
|result                                                         |
+---------------------------------------------------------------+
|[Peter Parker, New York, Bruce Wayne, San Antonio, Gotham City]|
+---------------------------------------------------------------+
{%- endcapture -%}

{%- capture approach_python_finance -%}
from johnsnowlabs import nlp, finance

# An example JSON file `regex_token.json` can look like this:
#
# {
#    "entity": "Stage",
#    "ruleScope": "sentence",
#    "regex": "[cpyrau]?[T][0-9X?][a-z^cpyrau]",
#    "matchScope": "token"
#  }
#
# Which means to extract the stage code on a sentence level.
# An example pipeline could then be defined like this
# Pipeline could then be defined like this

documentAssembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector() \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

# Define the parser (json file needs to be provided)

contextualParser = finance.ContextualParserApproach() \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("entity") \
    .setJsonPath("/path/to/regex_token.json") \
    .setCaseSensitive(True) \
    .setContextMatch(False)

pipeline = nlp.Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    contextualParser
  ])

# Define the parser (json file needs to be provided)
data = spark.createDataFrame([["Peter Parker is a nice guy and lives in New York . Bruce Wayne is also a nice guy and lives in San Antonio and Gotham City ."]]).toDF("text")

result = pipeline.fit(data).transform(data)

# Show Results
result.selectExpr("explode(entity)").show(5, truncate=False)

+---------------------------------------------------------------+
|result                                                         |
+---------------------------------------------------------------+
|[Peter Parker, New York, Bruce Wayne, San Antonio, Gotham City]|
+---------------------------------------------------------------+
{%- endcapture -%}

{%- capture approach_scala_medical -%}
import spark.implicits._

// An example JSON file `regex_token.json` can look like this:
//
// {
//    "entity": "Stage",
//    "ruleScope": "sentence",
//    "regex": "[cpyrau]?[T][0-9X?][a-z^cpyrau]",
//    "matchScope": "token"
//  }
//
// Which means to extract the stage code on a sentence level.
// An example pipeline could then be defined like this

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val contextualParser = new ContextualParserApproach()
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("entity")
    .setJsonPath("/path/to/regex_token.json")
    .setCaseSensitive(true)
    .setContextMatch(false)

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    contextualParser
  ))

// Define the parser (json file needs to be provided)
val data = Seq("A patient has liver metastases pT1bN0M0 and the T5 primary site may be colon or... ").toDF("text")

val result = pipeline.fit(data).transform(data)

// Show Results
//
// result.selectExpr("explode(entity)").show(5, truncate=false)
// +-------------------------------------------------------------------------------------------------------------------------+
// |col                                                                                                                      |
// +-------------------------------------------------------------------------------------------------------------------------+
// |{chunk, 32, 39, pT1bN0M0, {field -> Stage, normalized -> , confidenceValue -> 0.13, hits -> regex, sentence -> 0}, []}   |
// |{chunk, 49, 50, T5, {field -> Stage, normalized -> , confidenceValue -> 0.13, hits -> regex, sentence -> 0}, []}         |
// |{chunk, 148, 156, cT4bcN2M1, {field -> Stage, normalized -> , confidenceValue -> 0.13, hits -> regex, sentence -> 1}, []}|
// |{chunk, 189, 194, T?N3M1, {field -> Stage, normalized -> , confidenceValue -> 0.13, hits -> regex, sentence -> 2}, []}   |
// |{chunk, 316, 323, pT1bN0M0, {field -> Stage, normalized -> , confidenceValue -> 0.13, hits -> regex, sentence -> 3}, []} |
// +-------------------------------------------------------------------------------------------------------------------------+
//
{%- endcapture -%}

{%- capture approach_scala_legal -%}
import spark.implicits._

// An example JSON file `regex_token.json` can look like this:
//
// {
//    "entity": "Stage",
//    "ruleScope": "sentence",
//    "regex": "[cpyrau]?[T][0-9X?][a-z^cpyrau]",
//    "matchScope": "token"
//  }
//
// Which means to extract the stage code on a sentence level.
// An example pipeline could then be defined like this

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val contextualParser = new ContextualParserApproach()
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("entity")
    .setJsonPath("/path/to/regex_token.json")
    .setCaseSensitive(true)
    .setContextMatch(false)

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    contextualParser
  ))

// Define the parser (json file needs to be provided)
val data = Seq("Peter Parker is a nice guy and lives in New York . Bruce Wayne is also a nice guy and lives in San Antonio and Gotham City .").toDF("text")

val result = pipeline.fit(data).transform(data)

// Show Results
result.selectExpr("explode(entity)").show(5, truncate=False)

+---------------------------------------------------------------+
|result                                                         |
+---------------------------------------------------------------+
|[Peter Parker, New York, Bruce Wayne, San Antonio, Gotham City]|
+---------------------------------------------------------------+
{%- endcapture -%}

{%- capture approach_scala_finance -%}
import spark.implicits._

// An example JSON file `regex_token.json` can look like this:
//
// {
//    "entity": "Stage",
//    "ruleScope": "sentence",
//    "regex": "[cpyrau]?[T][0-9X?][a-z^cpyrau]",
//    "matchScope": "token"
//  }
//
// Which means to extract the stage code on a sentence level.
// An example pipeline could then be defined like this

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val contextualParser = new ContextualParserApproach()
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("entity")
    .setJsonPath("/path/to/regex_token.json")
    .setCaseSensitive(true)
    .setContextMatch(false)

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    contextualParser
  ))

// Define the parser (json file needs to be provided)
val data = Seq("Peter Parker is a nice guy and lives in New York . Bruce Wayne is also a nice guy and lives in San Antonio and Gotham City .").toDF("text")

val result = pipeline.fit(data).transform(data)

// Show Results

+---------------------------------------------------------------+
|result                                                         |
+---------------------------------------------------------------+
|[Peter Parker, New York, Bruce Wayne, San Antonio, Gotham City]|
+---------------------------------------------------------------+
{%- endcapture -%}

{%- capture approach_api_link -%}
[ContextualParserApproach](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/context/ContextualParserApproach.html)
{%- endcapture -%}

{%- capture approach_python_api_link -%}
[ContextualParserApproach](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/context/contextual_parser/index.html#sparknlp_jsl.annotator.context.contextual_parser.ContextualParserApproach)
{%- endcapture -%}

{%- capture approach_notebook_link -%}
[Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ContextualParserApproach.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
approach=approach
approach_description=approach_description
approach_input_anno=approach_input_anno
approach_output_anno=approach_output_anno
approach_python_medical=approach_python_medical
approach_python_legal=approach_python_legal
approach_python_finance=approach_python_finance
approach_scala_medical=approach_scala_medical
approach_scala_legal=approach_scala_legal
approach_scala_finance=approach_scala_finance
approach_api_link=approach_api_link
approach_python_api_link=approach_python_api_link
approach_notebook_link=approach_notebook_link
%}
