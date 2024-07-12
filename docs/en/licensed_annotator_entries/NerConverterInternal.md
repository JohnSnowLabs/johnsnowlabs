{%- capture title -%}
NerConverterInternal
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
Converts a IOB or IOB2 representation of NER to a user-friendly one,
by associating the tokens of recognized entities and their label.
Chunks with no associated entity (tagged "O") are filtered out.

Parametres;

- `setThreshold`: Confidence threshold.

- `setWhiteList`: If defined, list of entities to process.

- `setBlackList`:  If defined, list of entities to ignore.   

- `setReplaceLabels`: If defined, contains a dictionary for entity replacement.

- `setPreservePosition`: Whether to preserve the original position of the tokens in the original document or use the modified tokens.

- `setReplaceDictResource`: If defined, path to the file containing a dictionary for entity replacement.

- `setIgnoreStopWords`: If defined, list of stop words to ignore.

- `setGreedyMode`: (Boolean) Whether to ignore B tags for contiguous tokens of same entity same .

This licensed annotator adds extra functionality to the open-source version by adding the following parameters: `blackList`, `greedyMode`,  `threshold`, and `ignoreStopWords` that are not available in the [NerConverter](https://nlp.johnsnowlabs.com/docs/en/annotators#nerconverter) annotator.

See also [Inside–outside–beginning (tagging)](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) for more information.
{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, TOKEN, NAMED_ENTITY
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import * 
# Annotator that transforms a text column from dataframe into an Annotation ready for NLP
document_assembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetector() \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

# Tokenizer splits words in a relevant format for NLP
tokenizer = nlp.Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

# Clinical word embeddings trained on PubMED dataset
embeddings  = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

# NER model
nerModel = medical.NerModel.pretrained("ner_posology", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

# NER Converter
nerConverter = medical.NerConverterInternal() \
   .setInputCols(["sentence", "token", "ner"]) \
   .setOutputCol("ner_chunk")

nlpPipeline = nlp.Pipeline(stages = [document_assembler,
                              sentence_detector,
                              tokenizer,
                              embeddings,
                              nerModel,
                              nerConverter
                              ])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = nlpPipeline.fit(empty_data)

sample_text = """The patient was prescribed 1 capsule of Advil for 5 days.
He was seen by the endocrinology service and she was discharged on 40 units of insulin glargine at night, 12 units of insulin lispro with meals, metformin 1000 mg two times a day.
"""

data = spark.createDataFrame([[sample_text]]).toDF("text")

result = model.transform(data)
result.select('text', 'ner.result', 'ner_chunk.result').show(truncate = 50)

+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|                                              text|                                            result|                                            result|
+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|The patient was prescribed 1 capsule of Advil f...|[O, O, O, O, B-DOSAGE, B-FORM, O, B-DRUG, B-DUR...|[1, capsule, Advil, for 5 days, 40 units, insul...|
+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+

{%- endcapture -%}

{%- capture model_scala_medical -%}
import spark.implicits._

// Annotator that transforms a text column from dataframe into an Annotation ready for NLP 
val document_assembler = new DocumentAssembler()
 .setInputCol("text") 
 .setOutputCol("document")

val sentence_detector = new SentenceDetector()
 .setInputCols(Array("document")) 
 .setOutputCol("sentence") 
 
// Tokenizer splits words in a relevant format for NLP 
val tokenizer = new Tokenizer()
 .setInputCols(Array("sentence")) 
 .setOutputCol("token") 
 
// Clinical word embeddings trained on PubMED dataset 
val embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
 .setInputCols(Array("sentence","token")) 
 .setOutputCol("embeddings") 
 
// NER model 
val nerModel = MedicalNerModel.pretrained("ner_posology","en","clinical/models")
 .setInputCols(Array("sentence","token","embeddings")) 
 .setOutputCol("ner") 
 
// NER Converter 
val nerConverter = new NerConverterInternal()
 .setInputCols(Array("sentence","token","ner")) 
 .setOutputCol("ner_chunk") 

val nlpPipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector, 
    tokenizer, 
    embeddings, 
    nerModel, 
    nerConverter )) 

val empty_data = Seq("") .toDF("text") 
val model = nlpPipeline.fit(empty_data) 

val sample_text = "The patient was prescribed 1 capsule of Advil for 5 days.He was seen by the endocrinology service and she was discharged on 40 units of insulin glargine at night,12 units of insulin lispro with meals,metformin 1000 mg two times a day." 

val data = Seq(sample_text) .toDF("text") 
val result = model.transform(data) result.select("text","ner.result","ner_chunk.result") 

+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|                                              text|                                            result|                                            result|
+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|The patient was prescribed 1 capsule of Advil f...|[O, O, O, O, B-DOSAGE, B-FORM, O, B-DRUG, B-DUR...|[1, capsule, Advil, for 5 days, 40 units, insul...|
+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
{%- endcapture -%}


{%- capture model_python_legal -%}
from johnsnowlabs import * 
# Annotator that transforms a text column from dataframe into an Annotation ready for NLP
document_assembler = nlp.DocumentAssembler() \
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetector() \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

# Tokenizer splits words in a relevant format for NLP
tokenizer = nlp.Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

embeddings  = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

# NER model
nerModel = legal.NerModel.pretrained("legner_org_per_role_date", "en", "legal/models")\
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

# NER Converter
nerConverter = legal.NerConverterInternal() \
   .setInputCols(["sentence", "token", "ner"]) \
   .setOutputCol("ner_chunk")

nlpPipeline = nlp.Pipeline(stages = [document_assembler,
                              sentence_detector,
                              tokenizer,
                              embeddings,
                              nerModel,
                              nerConverter
                              ])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = nlpPipeline.fit(empty_data)

sample_text = """Jeffrey Preston Bezos is an American entrepreneur, founder and CEO of Amazon
"""

data = spark.createDataFrame([[sample_text]]).toDF("text")

result = model.transform(data)
result.select('text', 'ner.result', 'ner_chunk.result').show(truncate = 50)

+--------------------------------------------------+--------------------------------------------------+---------------------------------------------+
|                                              text|                                            result|                                       result|
+--------------------------------------------------+--------------------------------------------------+---------------------------------------------+
|Jeffrey Preston Bezos is an American entreprene...|[B-PERSON, I-PERSON, I-PERSON, O, O, O, O, O, B...|[Jeffrey Preston Bezos, founder, CEO, Amazon]|
+--------------------------------------------------+--------------------------------------------------+---------------------------------------------+
{%- endcapture -%}



{%- capture model_scala_legal -%}
import spark.implicits._

// Annotator that transforms a text column from dataframe into an Annotation ready for NLP 
val document_assembler = new DocumentAssembler()
 .setInputCol("text") 
 .setOutputCol("document") 

val sentence_detector = new SentenceDetector()
 .setInputCols(Array("document")) 
 .setOutputCol("sentence") 

// Tokenizer splits words in a relevant format for NLP 
val tokenizer = new Tokenizer()
 .setInputCols(Array("sentence")) 
 .setOutputCol("token") 

val embeddings = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en")
 .setInputCols(Array("sentence","token")) 
 .setOutputCol("embeddings") 
 
// NER model 
val nerModel = LegalNerModel.pretrained("legner_org_per_role_date","en","legal/models")
 .setInputCols(Array("sentence","token","embeddings")) 
 .setOutputCol("ner") 
 
// NER Converter 
val nerConverter = new NerConverterInternal()
 .setInputCols(Array("sentence","token","ner")) 
 .setOutputCol("ner_chunk") 

val nlpPipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector, 
    tokenizer, 
    embeddings, 
    nerModel, 
    nerConverter )) 

val empty_data = Seq("") .toDF("text") 
val model = nlpPipeline.fit(empty_data) 

val sample_text = "Jeffrey Preston Bezos is an American entrepreneur,founder and CEO of Amazon" 

val data = Seq(sample_text) .toDF("text") 
val result = model.transform(data) result.select("text","ner.result","ner_chunk.result") 

+--------------------------------------------------+--------------------------------------------------+---------------------------------------------+
|                                              text|                                            result|                                       result|
+--------------------------------------------------+--------------------------------------------------+---------------------------------------------+
|Jeffrey Preston Bezos is an American entreprene...|[B-PERSON, I-PERSON, I-PERSON, O, O, O, O, O, B...|[Jeffrey Preston Bezos, founder, CEO, Amazon]|
+--------------------------------------------------+--------------------------------------------------+---------------------------------------------+
{%- endcapture -%}


{%- capture model_python_finance -%}
from johnsnowlabs import * 
# Annotator that transforms a text column from dataframe into an Annotation ready for NLP
document_assembler = nlp.DocumentAssembler() \
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetector() \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

# Tokenizer splits words in a relevant format for NLP
tokenizer = nlp.Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")\
    .setContextChars(['.', ',', ';', ':', '!', '?', '*', '-', '(', ')', '"', "'", '%', '&'])

embeddings  = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

# NER model
nerModel = finance.NerModel.pretrained("finner_responsibility_reports_md", "en", "finance/models")\
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

# NER Converter
nerConverter = finance.NerConverterInternal() \
   .setInputCols(["sentence", "token", "ner"]) \
   .setOutputCol("ner_chunk")

nlpPipeline = nlp.Pipeline(stages = [document_assembler,
                              sentence_detector,
                              tokenizer,
                              embeddings,
                              nerModel,
                              nerConverter
                              ])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = nlpPipeline.fit(empty_data)

sample_text = """The company has reduced its direct GHG emissions from 12,135 million tonnes of CO2e in 2017 to 4 million tonnes of CO2e in 2021. The indirect GHG emissions (scope 2) are mainly from imported energy, including electricity, heat, steam, and cooling, and the company has reduced its scope 2 emissions from 3 million tonnes of CO2e in 2017-2018 to 4 million tonnes of CO2e in 2020-2021. The scope 3 emissions are mainly from the use of sold products, and the emissions have increased from 377 million tonnes of CO2e in 2017 to 408 million tonnes of CO2e in 2021.
"""

data = spark.createDataFrame([[sample_text]]).toDF("text")

result = model.transform(data)
result.select('text', 'ner.result', 'ner_chunk.result').show(truncate = 50)

+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|                                              text|                                            result|                                            result|
+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|The company has reduced its direct GHG emission...|[O, O, O, O, O, B-ENVIRONMENTAL_KPI, I-ENVIRONM...|[direct GHG emissions, 12,135 million, tonnes o...|
+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+

{%- endcapture -%}


{%- capture model_scala_finance -%}
import spark.implicits._

// Annotator that transforms a text column from dataframe into an Annotation ready for NLP 
val document_assembler = new DocumentAssembler()
 .setInputCol("text") 
 .setOutputCol("document") 

val sentence_detector = new SentenceDetector()
 .setInputCols(Array("document")) 
 .setOutputCol("sentence") 

// Tokenizer splits words in a relevant format for NLP 
val tokenizer = new Tokenizer()
 .setInputCols(Array("sentence")) 
 .setOutputCol("token") 
 .setContextChars(Array(".",",",";",":","!","?","*","-","(",") ",""",""","%","&")) 

val embeddings = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en")
 .setInputCols(Array("sentence","token")) 
 .setOutputCol("embeddings") 

// NER model 
val nerModel = FinanceNerModel.pretrained("finner_responsibility_reports_md","en","finance/models")
 .setInputCols(Array("sentence","token","embeddings")) 
 .setOutputCol("ner") 
 
// NER Converter 
val nerConverter = new NerConverterInternal()
 .setInputCols(Array("sentence","token","ner")) 
 .setOutputCol("ner_chunk") 

val nlpPipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    tokenizer, 
    embeddings,
    nerModel, 
    nerConverter )) 

val empty_data = Seq("") .toDF("text") 
val model = nlpPipeline.fit(empty_data) 

val sample_text = "The company has reduced its direct GHG emissions from 12,135 million tonnes of CO2e in 2017 to 4 million tonnes of CO2e in 2021. The indirect GHG emissions (scope 2) are mainly from imported energy,including electricity,heat,steam,and cooling,and the company has reduced its scope 2 emissions from 3 million tonnes of CO2e in 2017-2018 to 4 million tonnes of CO2e in 2020-2021. The scope 3 emissions are mainly from the use of sold products,and the emissions have increased from 377 million tonnes of CO2e in 2017 to 408 million tonnes of CO2e in 2021." 
val data = Seq(sample_text) .toDF("text") 

val result = model.transform(data) result.select("text","ner.result","ner_chunk.result") 

+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|                                              text|                                            result|                                            result|
+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|The company has reduced its direct GHG emission...|[O, O, O, O, O, B-ENVIRONMENTAL_KPI, I-ENVIRONM...|[direct GHG emissions, 12,135 million, tonnes o...|
+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
{%- endcapture -%}

{%- capture model_api_link -%}
[NerConverterInternal](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/ner/NerConverterInternal.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[NerConverterInternal](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/ner/ner_converter_internal/index.html#sparknlp_jsl.annotator.ner.ner_converter_internal.NerConverterInternal)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/NerConverterInternal.ipynb)
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
