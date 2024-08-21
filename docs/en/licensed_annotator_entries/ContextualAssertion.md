{%- capture title -%}
ContextualAssertion
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
An annotator model for contextual assertion analysis. This model identifies  contextual cues within text data, such as negation, uncertainty etc. It is used
clinical assertion detection. It annotates text chunks with assertions based on configurable rules, prefix and suffix patterns, and exception patterns.

Parametres:

- `inputCols`: Input annotations.
- `caseSensitive`: Whether to use case sensitive when matching values, by default `False`.
- `prefixAndSuffixMatch`: Whether to match both prefix and suffix to annotate the hit, by default `False`.
- `prefixKeywords`: Prefix keywords to match.
- `suffixKeywords`: Suffix keywords to match
- `exceptionKeywords`: Exception keywords not to match.
- `prefixRegexPatterns`: Prefix regex patterns to match
- `suffixRegexPatterns`: Suffix regex pattern to match
- `exceptionRegexPatterns`: Exception regex pattern not to match
- `scopeWindow`: The scope window of the assertion expression
- `assertion`: Assertion to match
- `scopeWindowDelimiter`: Delimiters used to limit the scope window.
- `includeChunkToScope`: Whether to include chunk to scope when matching values
- `ConfidenceCalculationDirection`: Indicates the direction for calculating assertion confidence (left, right, or both; default is left).


See [Spark NLP Workshop](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/2.3.Contextual_Assertion.ipynb) for more examples of usage.
{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, TOKEN, CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
ASSERTION
{%- endcapture -%}

{%- capture model_scala_medical -%}
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetector() \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel \
    .pretrained("embeddings_clinical", "en", "clinical/models") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

clinical_ner = nlp.MedicalNerModel \
    .pretrained("ner_clinical", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = nlp.NerConverter() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")

contextual_assertion = medical.ContextualAssertion() \
    .setInputCols(["sentence", "token", "ner_chunk"]) \
    .setOutputCol("assertion") \
    .setPrefixKeywords(["no", "not"]) \
    .setSuffixKeywords(["unlikely","negative"]) \
    .setPrefixRegexPatterns(["\\b(no|without|denies|never|none|free of|not include)\\b"]) \
    .setSuffixRegexPatterns(["\\b(free of|negative for|absence of|not|rule out)\\b"]) \
    .setExceptionKeywords(["without"]) \
    .setExceptionRegexPatterns(["\\b(not clearly)\\b"]) \
    .addPrefixKeywords(["negative for","negative"]) \
    .addSuffixKeywords(["absent","neither"]) \
    .setCaseSensitive(False) \
    .setPrefixAndSuffixMatch(False) \
    .setAssertion("absent") \
    .setScopeWindow([2, 2])\
    .setIncludeChunkToScope(True)\
    .setScopeWindowDelimiters([","])

flattener = medical.Flattener() \
    .setInputCols("assertion") \
    .setExplodeSelectedFields({"assertion":["metadata.ner_chunk as ner_chunk",
                                            "begin as begin",
                                            "end as end",
                                            "metadata.ner_label as ner_label",
                                            "result as result"]})

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    clinical_ner,
    ner_converter,
    contextual_assertion,
    flattener])

text = """Patient resting in bed. Patient given azithromycin without any difficulty. Patient has audible wheezing, states chest tightness.
No evidence of hypertension. Patient denies nausea at this time. zofran declined. Patient is also having intermittent sweating
associated with pneumonia. Patient refused pain but tylenol still given. Neither substance abuse nor alcohol use however cocaine
once used in the last year. Alcoholism unlikely. Patient has headache and fever. Patient is not diabetic. Not clearly of diarrhea.
Lab reports confirm lymphocytopenia. Cardaic rhythm is Sinus bradycardia. Patient also has a history of cardiac injury.
No kidney injury reported. No abnormal rashes or ulcers. Patient might not have liver disease. Confirmed absence of hemoptysis.
Although patient has severe pneumonia and fever, test reports are negative for COVID-19 infection. COVID-19 viral infection absent.
"""
data = spark.createDataFrame([[text]]).toDF("text")

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = pipeline.fit(empty_data)

result = model.transform(data)
result.show(truncate=False)

# result
+------------------+-----+---+---------+------+
|ner_chunk         |begin|end|ner_label|result|
+------------------+-----+---+---------+------+
|nausea            |173  |178|PROBLEM  |absent|
|Alcoholism        |413  |422|PROBLEM  |absent|
|diabetic          |481  |488|PROBLEM  |absent|
|kidney injury     |639  |651|PROBLEM  |absent|
|abnormal rashes   |666  |680|PROBLEM  |absent|
|liver disease     |716  |728|PROBLEM  |absent|
|COVID-19 infection|843  |860|PROBLEM  |absent|
|viral infection   |872  |886|PROBLEM  |absent|
+------------------+-----+---+---------+------+
{%- endcapture -%}


{%- capture model_scala_medical -%}

import spark.implicits._

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
    .setInputCols(Array("document"))
    .setOutputCol("sentences")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentences"))
    .setOutputCol("tokens")

val embedder = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentences", "tokens"))
    .setOutputCol("embeddings")

val nerTagger = MedicalNerModel .pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentences", "tokens", "embeddings"))
    .setOutputCol("nerTags")

val nerConverter = new NerConverterInternal()
    .setInputCols(Array("sentences", "tokens", "nerTags"))
    .setOutputCol("nerChunks")

val contextualAssertion = new ContextualAssertion()
  .setInputCols(Array("sentences", "tokens","nerChunks"))
  .setOutputCol("assertion")
  .setScopeWindow(2,2)
  .setPrefixRegexPatterns(Array("\\b(no|without|denies|never|none|free of|negative for|not include)\\b"))
  .setSuffixRegexPatterns(Array("\\b(free of|negative for|absence of|absence|not|neither|rule out)\\b"))
  .setPrefixKeywords(Array("not","never"))
  .setSuffixKeywords(Array("no","never"))
  .setCaseSensitive(false)
  .setIncludeChunkToScope(true)
  .addPrefixKeywords(Array("negative for","no evidence of"))
  .addSuffixKeywords(Array("declined"))
  .setAssertion("absent")
  .setScopeWindowDelimiter(Array(","))



val flattener = new Flattener()
  .setInputCols("assertion")
  .setExplodeSelectedFields(Map("assertion" -> Array( "metadata.ner_chunk as ner_chunk ","begin as begin","end as end"," "metadata.ner_label as ner_label","result as result",
) ) )

val pipeline = new Pipeline()
  .setStages(Array(documentAssembler,
                  sentenceDetector,
                  tokenizer,
                  embedder,
                  nerTagger,
                  nerConverter,
                  contextualAssertion,
                  flattener
                  ))

val text = "Patient resting in bed. Patient given azithromycin without any difficulty. Patient has audible wheezing, states chest tightness." +
" No evidence of hypertension. Patient denies nausea at this time. zofran declined. Patient is also having intermittent sweating " +
"associated with pneumonia. Patient refused pain but tylenol still given. Neither substance abuse nor alcohol use however cocaine " +
"once used in the last year. Alcoholism unlikely. Patient has headache and fever. Patient is not diabetic. Not clearly of diarrhea. " +
"Lab reports confirm lymphocytopenia. Cardaic rhythm is Sinus bradycardia. Patient also has a history of cardiac injury." +
" No kidney injury reported. No abnormal rashes or ulcers. Patient might not have liver disease. Confirmed absence of hemoptysis." +
" Although patient has severe pneumonia and fever, test reports are negative for COVID-19 infection. COVID-19 viral infection absent."

val dataSet = Seq(text).toDS.toDF("text")

val result = pipeline.fit(dataSet).transform(dataSet)

# result
+------------------+-----+---+---------+------+
|ner_chunk         |begin|end|ner_label|result|
+------------------+-----+---+---------+------+
|nausea            |173  |178|PROBLEM  |absent|
|Alcoholism        |413  |422|PROBLEM  |absent|
|diabetic          |481  |488|PROBLEM  |absent|
|kidney injury     |639  |651|PROBLEM  |absent|
|abnormal rashes   |666  |680|PROBLEM  |absent|
|liver disease     |716  |728|PROBLEM  |absent|
|COVID-19 infection|843  |860|PROBLEM  |absent|
|viral infection   |872  |886|PROBLEM  |absent|
+------------------+-----+---+---------+------+

{%- endcapture -%}

{%- capture model_api_link -%}
[ContextualAssertion](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/assertion/context/ContextualAssertion.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[ContextualAssertion](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/assertion/contextual_assertion/index.html#sparknlp_jsl.annotator.assertion.contextual_assertion)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[ContextualAssertion](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/2.3.Contextual_Assertion.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical
model_api_link=model_api_link
model_python_api_link=model_python_api_link
%}
