{%- capture title -%}
MetadataAnnotationConverter
{%- endcapture -%}

{%- capture title_with_article -%}
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
Converts metadata fields in annotations into actual begin, end, or result values.

`MetadataAnnotationConverter` enables users to override fields in Spark NLP annotations using
values from their `metadata` dictionary. This is especially useful when metadata contains normalized
values, corrected character offsets, or alternative representations of the entity or phrase.

The transformation is handled on the Scala side and is compatible with Spark NLP pipelines.

Parameters:

- `inputType`: Type of the input annotation (e.g., "chunk", "token").
- `resultField`: Name of the metadata key to override the `result` value.
- `beginField`: Name of the metadata key to override the `begin` offset.
- `endField`: Name of the metadata key to override the `end` offset.


{%- endcapture -%}


{%- capture model_input_anno -%}
ANY
{%- endcapture -%}

{%- capture model_output_anno -%}
ANY
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical
from sparknlp_jsl.annotator import AnnotationConverter

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel\
    .pretrained("sentence_detector_dl_healthcare", "en", "clinical/models") \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

text_matcher = TextMatcherInternal()\
    .setInputCols(["sentence","token"])\
    .setOutputCol("matched_text")\
    .setEntities("./test-phrases.txt")\
    .setEnableLemmatizer(True) \
    .setEnableStemmer(True) \
    .setCleanStopWords(True) \
    .setBuildFromTokens(False)\
    .setReturnChunks("original")\

metadata_annotation_converter = MetadataAnnotationConverter()\
    .setInputCols("matched_text")\
    .setInputType("chunk") \
    .setResultField("original_or_matched") \
    .setOutputCol("new_chunk")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_assertion_dl = AssertionDLModel.pretrained("assertion_dl", "en", "clinical/models") \
    .setInputCols(["sentence", "new_chunk", "embeddings"]) \
    .setOutputCol("assertion_dl")\


text_matcher_pipeline= Pipeline(
    stages=[
        document_assembler,
        sentence_detector,
        tokenizer,
        word_embeddings,
        text_matcher,
        metadata_annotation_converter,
        clinical_assertion_dl
])

text_matcher_model = text_matcher_pipeline.fit(empty_data)
text_matcher_result_df = text_matcher_model.transform(data)




# result

+------+-----+---+----------------------------+
|entity|begin|end|result                      |
+------+-----+---+----------------------------+
|entity|69   |99 |evaluation psychiatric state|
|entity|52   |60 |stressor                    |
|entity|114  |132|difficulty sleep            |
+------+-----+---+----------------------------+


{%- endcapture -%}



{%- capture model_api_link -%}
[MetadataAnnotationConverter](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/MetadataAnnotationConverter.html)
{%- endcapture -%}
{%- capture model_python_api_link -%}

[MetadataAnnotationConverter](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/metadata_annotation_converter/index.html)
{%- endcapture -%}


{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_api_link=model_api_link
model_python_api_link=model_python_api_link
%}
