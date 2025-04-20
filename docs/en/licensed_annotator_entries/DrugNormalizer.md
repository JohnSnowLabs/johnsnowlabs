{%- capture title -%}
DrugNormalizer
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
Normalizes drug mentions in clinical text.

Adds spaces between punctuation and words, as well as normalize the
drug mentions. The `policy` parameter controls what drug information
should be normalized, check the parameter documentation for details.

For usage examples and discussion, check out
[Blogpost](https://medium.com/spark-nlp/normalize-drug-names-and-dosage-units-with-spark-nlp-8b7ef606facf)

Parametres:

- `lowercase`: (boolean) whether to convert strings to lowercase. Default is False.

- `policy`: (str) rule to remove patterns from text.  Valid policy values are:
  - **`"all"`** – replaces both abbreviations and dosages
  - **`"abbreviations"`** – replaces all abbreviations with their full forms
      > e.g., `"oral sol"` → `"oral solution"`
  - **`"dosages"`** – converts dosages to a standardized format
      > e.g., `"10 million units"` → `"10000000 unt"`

  **Default:** `"all"`



See [Spark NLP Workshop](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/23.Drug_Normalizer.ipynb) for more examples of usage.
{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_output_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

# Sample data
data_to_normalize = spark.createDataFrame([
            ("A", "Sodium Chloride/Potassium Chloride 13bag", "Sodium Chloride / Potassium Chloride 13 bag"),
            ("B", "interferon alfa-2b 10 million unit ( 1 ml ) injec", "interferon alfa - 2b 10000000 unt ( 1 ml ) injection"),
            ("C", "aspirin 10 meq/ 5 ml oral sol", "aspirin 2 meq/ml oral solution")
        ]).toDF("cuid", "text", "target_normalized_text")

# Annotator that transforms a text column from dataframe into normalized text (with all policy)

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

drug_normalizer = medical.DrugNormalizer() \
    .setInputCols("document") \
    .setOutputCol("document_normalized") \
    .setPolicy("all")

drug_normalizer_pipeline = nlp.Pipeline(stages=[
    document_assembler,
    drug_normalizer
    ])

ds = drug_normalizer_pipeline.fit(data_to_normalize).transform(data_to_normalize)

ds = ds.selectExpr("document", "target_normalized_text", "explode(document_normalized.result) as all_normalized_text")
ds.show(truncate = False)

+-------------------------------------------------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
|document                                                                                   |target_normalized_text                              |all_normalized_text                                 |
+-------------------------------------------------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
|[{document, 0, 39, Sodium Chloride/Potassium Chloride 13bag, {sentence -> 0}, []}]         |Sodium Chloride / Potassium Chloride 13 bag         |Sodium Chloride / Potassium Chloride 13 bag         |
|[{document, 0, 48, interferon alfa-2b 10 million unit ( 1 ml ) injec, {sentence -> 0}, []}]|interferon alfa - 2b 10000000 unt ( 1 ml ) injection|interferon alfa - 2b 10000000 unt ( 1 ml ) injection|
|[{document, 0, 28, aspirin 10 meq/ 5 ml oral sol, {sentence -> 0}, []}]                    |aspirin 2 meq/ml oral solution                      |aspirin 2 meq/ml oral solution                      |
+-------------------------------------------------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
{%- endcapture -%}


{%- capture model_scala_medical -%}

import spark.implicits._

// Sample data 
val data_to_normalize = Seq(Array( ("A","Sodium Chloride/Potassium Chloride 13bag","Sodium Chloride / Potassium Chloride 13 bag") , ("B","interferon alfa-2b 10 million unit ( 1 ml ) injec","interferon alfa - 2b 10000000 unt ( 1 ml ) injection") , ("C","aspirin 10 meq/ 5 ml oral sol","aspirin 2 meq/ml oral solution") )) .toDF("cuid","text","target_normalized_text") 

// Annotator that transforms a text column from dataframe into normalized text (with all policy) 

val document_assembler = new DocumentAssembler()
 .setInputCol("text") 
 .setOutputCol("document") 

val drug_normalizer = new DrugNormalizer()
 .setInputCols("document") 
 .setOutputCol("document_normalized") 
 .setPolicy("all") 

val drug_normalizer_pipeline = new Pipeline().setStages(Array(
  document_assembler, 
  drug_normalizer)) 

val ds = drug_normalizer_pipeline.fit(data_to_normalize).transform(data_to_normalize) 

+-------------------------------------------------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
|document                                                                                   |target_normalized_text                              |all_normalized_text                                 |
+-------------------------------------------------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
|[{document, 0, 39, Sodium Chloride/Potassium Chloride 13bag, {sentence -> 0}, []}]         |Sodium Chloride / Potassium Chloride 13 bag         |Sodium Chloride / Potassium Chloride 13 bag         |
|[{document, 0, 48, interferon alfa-2b 10 million unit ( 1 ml ) injec, {sentence -> 0}, []}]|interferon alfa - 2b 10000000 unt ( 1 ml ) injection|interferon alfa - 2b 10000000 unt ( 1 ml ) injection|
|[{document, 0, 28, aspirin 10 meq/ 5 ml oral sol, {sentence -> 0}, []}]                    |aspirin 2 meq/ml oral solution                      |aspirin 2 meq/ml oral solution                      |
+-------------------------------------------------------------------------------------------+----------------------------------------------------+----------------------------------------------------+


{%- endcapture -%}



{%- capture model_api_link -%}
[DrugNormalizer](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/DrugNormalizer.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[DrugNormalizer](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/normalizer/drug_normalizer/index.html#sparknlp_jsl.annotator.normalizer.drug_normalizer.DrugNormalizer)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[DrugNormalizerNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/DrugNormalizer.ipynb)
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
model_notebook_link=model_notebook_link%}
