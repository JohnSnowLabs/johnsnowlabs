{%- capture title -%}
AverageEmbeddings
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
`AverageEmbeddings` computes the mean of vector embeddings for two sentences of equal size, producing a unified representation. 

Parameters:

- `inputCols`: The name of the columns containing the input annotations. It can read either a String column or an Array.

- `outputCol`: The name of the column in Document type that is generated. We can specify only one column here.

All the parameters can be set using the corresponding set method in camel case. For example, `.setInputcols()`.
{%- endcapture -%}

{%- capture model_input_anno -%}
SENTENCE_EMBEDDINGS, SENTENCE_EMBEDDINGS, CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
EMBEDDINGS
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

document_assembler =  nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")\

sentence_detector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

doc2Chunk = nlp.Doc2Chunk() \
    .setInputCols("sentence") \
    .setOutputCol("chunk") \
    .setIsArray(True)

sbiobert_base_cased_mli = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols("sentence")\
    .setOutputCol("sbiobert_base_cased_mli")

sent_biobert_clinical_base_cased = nlp.BertSentenceEmbeddings.pretrained("sent_biobert_clinical_base_cased", "en") \
    .setInputCols("sentence") \
    .setOutputCol("sent_biobert_clinical_base_cased")

avg_embeddings = medical.AverageEmbeddings()\
    .setInputCols(["sent_biobert_clinical_base_cased","sbiobert_base_cased_mli","chunk"])\
    .setOutputCol("embeddings")

pipeline = nlp.Pipeline(
    stages=[
        document_assembler,
        sentence_detector,
        doc2Chunk,
        sbiobert_base_cased_mli,
        sent_biobert_clinical_base_cased,
        avg_embeddings
    ])

data = spark.createDataFrame([[" The patient was prescribed 1 capsule of Advil for 5 days "]]).toDF("text")

result = pipeline.fit(data).transform(data)

result_df = result.select(F.explode(F.arrays_zip(result.chunk.result,
                                                 result.chunk.metadata,
                                                 result.sentence.result,
                                                 result.embeddings.embeddings,
                                                 result.sent_biobert_clinical_base_cased.embeddings,
                                                 result.sbiobert_base_cased_mli.embeddings,)).alias("cols"))\
                  .select(F.expr("cols['0']").alias("sentence"),
                          F.expr("cols['1']").alias("sentence_metadata"),
                          F.expr("cols['2']").alias("chunk"),
                          F.expr("cols['3']").alias("embeddings"),
                          F.expr("cols['4']").alias("sent_biobert_clinical_base_cased"),
                          F.expr("cols['5']").alias("sbiobert_base_cased_mli"))

result_df.show(50, truncate=1000)

## Result

+--------------------------------------------------+---------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|                                          sentence|          sentence_metadata|                                             chunk|                                        embeddings|                  sent_biobert_clinical_base_cased|                           sbiobert_base_cased_mli|
+--------------------------------------------------+---------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|The patient was prescribed 1 capsule of Advil f...|{sentence -> 0, chunk -> 0}|The patient was prescribed 1 capsule of Advil f...|[0.32466835, 0.12497781, -0.20237188, 0.3716198...|[-0.07857181, -0.061015874, -0.020198729, 0.177...|[0.7279085, 0.3109715, -0.38454503, 0.5657965, ...|
+--------------------------------------------------+---------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+


{%- endcapture -%}


{%- capture model_scala_medical -%}

import spark.implicits._

val document_assembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document") 

val sentence_detector = new SentenceDetector()
  .setInputCols("document")
  .setOutputCol("sentence")

val doc2Chunk = new Doc2Chunk()
  .setInputCols("sentence")
  .setOutputCol("chunk")
  .setIsArray(true)

val sbiobert_base_cased_mli = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
  .setInputCols("sentence")
  .setOutputCol("sbiobert_base_cased_mli")

val sent_biobert_clinical_base_cased = BertSentenceEmbeddings.pretrained("sent_biobert_clinical_base_cased","en")
  .setInputCols("sentence")
  .setOutputCol("sent_biobert_clinical_base_cased")

val avg_embeddings = new AverageEmbeddings()
  .setInputCols(Array("sent_biobert_clinical_base_cased","sbiobert_base_cased_mli","chunk"))
  .setOutputCol("embeddings") 

val pipeline = Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector, 
    doc2Chunk, 
    sbiobert_base_cased_mli, 
    sent_biobert_clinical_base_cased, 
    avg_embeddings)) 

val data = Seq(" The patient was prescribed 1 capsule of Advil for 5 days").toDF("text")

val result = pipeline.fit(data).transform(data)

// Show results
+--------------------------------------------------+---------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|                                          sentence|          sentence_metadata|                                             chunk|                                        embeddings|                  sent_biobert_clinical_base_cased|                           sbiobert_base_cased_mli|
+--------------------------------------------------+---------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|The patient was prescribed 1 capsule of Advil f...|{sentence -> 0, chunk -> 0}|The patient was prescribed 1 capsule of Advil f...|[0.32466835, 0.12497781, -0.20237188, 0.3716198...|[-0.07857181, -0.061015874, -0.020198729, 0.177...|[0.7279085, 0.3109715, -0.38454503, 0.5657965, ...|
+--------------------------------------------------+---------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+


{%- endcapture -%}

{%- capture model_api_link -%}
[AverageEmbeddings](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/embeddings/AverageEmbeddings.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[AverageEmbeddings](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/embeddings/average_embeddings/index.html#sparknlp_jsl.annotator.embeddings.average_embeddings.AverageEmbeddings)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[AverageEmbeddingsNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/AverageEmbeddings.ipynb)
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
model_notebook_link=model_notebook_link
%}
