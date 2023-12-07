{%- capture title -%}
InternalDocumentSplitter
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
`InternalDocumentSplitter` splits large documents into small documents. `InternalDocumentSplitter` has setSplitMode method to decide how to split documents.

If splitMode is `recursive`, It takes the separators in order and splits subtexts if they are over the chunk length, considering optional overlap of the chunks.

Additionally, you can set
- custom patterns with setSplitPatterns
- whether patterns should be interpreted as regex with setPatternsAreRegex
- whether to keep the separators with setKeepSeparators
- whether to trim whitespaces with setTrimWhitespace
- whether to explode the splits to individual rows with setExplodeSplits

Parametres:

- `chunkSize`: Size of each chunk of text. This param is applicable only for "recursive" splitMode.
- `chunkOverlap`: Length of the overlap between text chunks, by default `0`. This param is applicable only for `recursive` splitMode.
- `splitPatterns`: Patterns to split the document.
patternsAreRegex. Whether to interpret the split patterns as regular expressions, by default `True`.
- `keepSeparators`: Whether to keep the separators in the final result , by default `True`. This param is applicable only for "recursive" splitMode.
- `explodeSplits`: Whether to explode split chunks to separate rows , by default `False`.
- `trimWhitespace`: Whether to trim whitespaces of extracted chunks , by default `True`.
- `splitMode`: The split mode to determine how text should be segmented. Default: 'regex'. It should be one of the following values:
  - "char": Split text based on individual characters.
  - "token": Split text based on tokens. You should supply tokens from inputCols.
  - "sentence": Split text based on sentences. You should supply sentences from inputCols.
  - "recursive": Split text recursively using a specific algorithm.
  - "regex": Split text based on a regular expression pattern.
- `sentenceAwareness`: Whether to split the document by sentence awareness if possible.
  - If true, it can stop the split process before maxLength.
  - If true, you should supply sentences from inputCols. Default: False.
  - This param is not applicable only for `regex` and `recursive` splitMode.
- `maxLength`: The maximum length allowed for spitting. The mode in which the maximum length is specified:
  - "char": Maximum length is measured in characters. Default: `512`
  - "token": Maximum length is measured in tokens. Default: `128`
  - "sentence": Maximum length is measured in sentences. Default: `8`
- `customBoundsStrategy`: The custom bounds strategy for text splitting using regular expressions. This param is applicable only for `regex` splitMode.
- `caseSensitive`: Whether to use case sensitive when matching regex, by default `False`. This param is applicable only for `regex` splitMode.
-  `metaDataFields`: Metadata fields to add specified data in columns to the metadata of the split documents.         You should set column names to read columns.

{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_output_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_python_medical -%}

from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

document_splitter = medical.InternalDocumentSplitter()\
    .setInputCols("document")\
    .setOutputCol("splits")\
    .setSplitMode("recursive")\
    .setChunkSize(100)\
    .setChunkOverlap(3)\
    .setExplodeSplits(True)\
    .setPatternsAreRegex(False)\
    .setSplitPatterns(["\n\n", "\n", " "])\
    .setKeepSeparators(False)\
    .setTrimWhitespace(True)

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    document_splitter
])

df = spark.createDataFrame([[(
    "The patient is a 28-year-old, who is status post gastric bypass surgery"
    " nearly one year ago. \nHe has lost about 200 pounds and was otherwise doing well"
    " until yesterday evening around 7:00-8:00 when he developed nausea and right upper quadrant pain,"
    " which apparently wrapped around toward his right side and back. He feels like he was on it"
    " but has not done so. He has overall malaise and a low-grade temperature of 100.3."
    " \n\nHe denies any prior similar or lesser symptoms. His last normal bowel movement was yesterday."
    " He denies any outright chills or blood per rectum."
)]]).toDF("text")


pipeline_df = pipeline.fit(df).transform(df).select("splits").show(truncate=False)

## Result

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
|splits                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[{document, 0, 92, The patient is a 28-year-old, who is status post gastric bypass surgery nearly one year ago., {sentence -> 0, document -> 0}, []}]          |
|[{document, 94, 192, He has lost about 200 pounds and was otherwise doing well until yesterday evening around 7:00-8:00, {sentence -> 0, document -> 1}, []}]  |
|[{document, 193, 291, when he developed nausea and right upper quadrant pain, which apparently wrapped around toward his, {sentence -> 0, document -> 2}, []}] |
|[{document, 288, 387, his right side and back. He feels like he was on it but has not done so. He has overall malaise and, {sentence -> 0, document -> 3}, []}]|
|[{document, 384, 421, and a low-grade temperature of 100.3., {sentence -> 0, document -> 4}, []}]                                                              |
|[{document, 424, 520, He denies any prior similar or lesser symptoms. His last normal bowel movement was yesterday. He, {sentence -> 0, document -> 5}, []}]   |
|[{document, 518, 568, He denies any outright chills or blood per rectum., {sentence -> 0, document -> 6}, []}]                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}


{%- capture model_scala_medical -%}

import spark.implicits._

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val document_splitter = new InternalDocumentSplitter()
    .setInputCols("document")
    .setOutputCol("splits")
    .setSplitMode("recursive")
    .setChunkSize(100)
    .setChunkOverlap(3)
    .setExplodeSplits(true)
    .setPatternsAreRegex(false)
    .setSplitPatterns(Array("\n\n", "\n", " "))
    .setKeepSeparators(false)
    .setTrimWhitespace(true)

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    document_splitter ))


val test_data = Seq( "The patient is a 28-year-old, who is status post gastric bypass surgery"
    " nearly one year ago. \nHe has lost about 200 pounds and was otherwise doing well"
    " until yesterday evening around 7:00-8:00 when he developed nausea and right upper quadrant pain,"
    " which apparently wrapped around toward his right side and back. He feels like he was on it"
    " but has not done so. He has overall malaise and a low-grade temperature of 100.3."
    " \n\nHe denies any prior similar or lesser symptoms. His last normal bowel movement was yesterday."
    " He denies any outright chills or blood per rectum.").toDF("text")

val res = mapperPipeline.fit(test_data).transform(test_data)

// Show results

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
|splits                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[{document, 0, 92, The patient is a 28-year-old, who is status post gastric bypass surgery nearly one year ago., {sentence -> 0, document -> 0}, []}]          |
|[{document, 94, 192, He has lost about 200 pounds and was otherwise doing well until yesterday evening around 7:00-8:00, {sentence -> 0, document -> 1}, []}]  |
|[{document, 193, 291, when he developed nausea and right upper quadrant pain, which apparently wrapped around toward his, {sentence -> 0, document -> 2}, []}] |
|[{document, 288, 387, his right side and back. He feels like he was on it but has not done so. He has overall malaise and, {sentence -> 0, document -> 3}, []}]|
|[{document, 384, 421, and a low-grade temperature of 100.3., {sentence -> 0, document -> 4}, []}]                                                              |
|[{document, 424, 520, He denies any prior similar or lesser symptoms. His last normal bowel movement was yesterday. He, {sentence -> 0, document -> 5}, []}]   |
|[{document, 518, 568, He denies any outright chills or blood per rectum., {sentence -> 0, document -> 6}, []}]                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}


{%- capture model_notebook_link -%}
[InternalDocumentSplitterNotebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/38.InternalDocumentSplitter.ipynb)
{%- endcapture -%}


{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical
model_notebook_link=model_notebook_link
%}
