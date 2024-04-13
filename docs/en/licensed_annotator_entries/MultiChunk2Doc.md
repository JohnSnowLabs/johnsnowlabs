{%- capture title -%}
MultiChunk2Doc
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}

MultiChunk2Doc annotator merges a given chunks to create a document.
During document creation, a specific whitelist and blacklist filter can be applied, and case sensitivity can be adjusted.
Additionally, specified prefix and suffix texts can be placed before and after the merged chunks in the resulting document.
And a separator can be placed between the chunks.



Parameters:

- `separator` *(str)*: Separator to add between the chunks

- `prefix` *(str)*: Prefix to add to the result

- `suffix` *(str)*: Suffix to add to the result

- `blackList` *(list[str])*: If defined, list of entities to ignore. The rest will be processed. Do not include IOB prefix on labels

- `whiteList` *(list[str])*: If defined, list of entities to process. The rest will be ignored. Do not include IOB prefix on labels

- `caseSensitive` *(Bool)*: Determines whether the definitions of the white listed entities are case sensitive or not.



{%- endcapture -%}

{%- capture model_input_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_python_medical -%}

from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models") \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

clinical_ner = medical.NerModel.pretrained("ner_clinical_large_langtest", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")

multi_chunk2_doc = medical.MultiChunk2Doc() \
    .setInputCols(["ner_chunk"]) \
    .setOutputCol("new_document") \
    .setWhiteList(["test"]) \
    .setCaseSensitive(False) \
    .setPrefix("<") \
    .setSeparator("><") \
    .setSuffix(">") \

nlpPipeline = nlp.Pipeline(stages=[document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    clinical_ner,
    ner_converter,
    multi_chunk2_doc])

model = nlpPipeline.fit(self.spark.createDataFrame([[""]]).toDF("text"))

data = spark.createDataFrame([
["""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation
and subsequent type two diabetes mellitus (T2DM),
one prior episode of HTG-induced pancreatitis three years prior to presentation,
and associated with an acute hepatitis, presented with a one-week history of polyuria, poor appetite, and vomiting.
She was on metformin, glipizide, and dapagliflozin for T2DM and atorvastatin and gemfibrozil for HTG.
She had been on dapagliflozin for six months at the time of presentation.
Physical examination on presentation was significant for dry oral mucosa ;
significantly , her abdominal examination was benign with no tenderness, guarding, or rigidity."""]
]).toDF("text")

result = model.transform(data)

## Result

+-------------------------------------------------------------------------------------------------------------------------------+-------------+-----------+-------------------------+----------------------------+
|new_doc_result                                                                                                                 |new_doc_begin|new_doc_end|new_doc_metadata_document|new_doc_metadata_chunk_count|
+-------------------------------------------------------------------------------------------------------------------------------+-------------+-----------+-------------------------+----------------------------+
|<Physical examination> <her abdominal examination> <serum glucose> <creatinine> <triglycerides> <total cholesterol> <venous pH>|0            |126        |0                        |7                           |
+-------------------------------------------------------------------------------------------------------------------------------+-------------+-----------+-------------------------+----------------------------+

{%- endcapture -%}

{%- capture model_scala_medical -%}
import spark.implicits._

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner = MedicalNerModel.pretrained("ner_clinical_large_langtest", "en", "clinical/models")
    .setInputCols("sentence", "token", "embeddings")
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val multi_chunk2_doc = new MultiChunk2Doc()
    .setInputCols("ner_chunk").setOutputCol("new_doc")
    .setWhiteList(Array("test"))
    .setCaseSensitive(false)
    .setPrefix("<")
    .setSuffix(">")
    .setSeparator("> <")

val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner,
    ner_converter,
    multi_chunk2_doc))

val data = Seq("""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, and associated with an acute hepatitis, presented with a one-week history of polyuria, poor appetite, and vomiting. She was on metformin, glipizide, and dapagliflozin for T2DM and atorvastatin and gemfibrozil for HTG. She had been on dapagliflozin for six months at the time of presentation. Physical examination on presentation was significant for dry oral mucosa; significantly, her abdominal examination was benign with no tenderness, guarding, or rigidity. Pertinent laboratory findings on admission were: serum glucose 111 mg/dl,  creatinine 0.4 mg/dL, triglycerides 508 mg/dL, total cholesterol 122 mg/dL, and venous pH 7.27.""").toDS().toDF("text")

val result = pipeline.fit(emptyDF).transform(data)

// Result

+-------------------------------------------------------------------------------------------------------------------------------+-------------+-----------+-------------------------+----------------------------+
|new_doc_result                                                                                                                 |new_doc_begin|new_doc_end|new_doc_metadata_document|new_doc_metadata_chunk_count|
+-------------------------------------------------------------------------------------------------------------------------------+-------------+-----------+-------------------------+----------------------------+
|<Physical examination> <her abdominal examination> <serum glucose> <creatinine> <triglycerides> <total cholesterol> <venous pH>|0            |126        |0                        |7                           |
+-------------------------------------------------------------------------------------------------------------------------------+-------------+-----------+-------------------------+----------------------------+


{%- endcapture -%}


{%- capture model_api_link -%}
[MultiChunk2Doc](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/MultiChunk2Doc.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[MultiChunk2Doc](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/multi_chunk2_doc/index.html)
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
