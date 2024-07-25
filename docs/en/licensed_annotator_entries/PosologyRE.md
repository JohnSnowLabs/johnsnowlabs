{%- capture title -%}
PosologyREModel
{%- endcapture -%}


{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
Instantiated RelationExtractionModel for extracting relationships between different recognized drug entitites.
This class is not intended to be directly used, please use the RelationExtractionModel instead.
Possible values are "DRUG-DOSAGE", "DRUG-ADE", "DRUG-FORM", "DRUG-FREQUENCY",
"DRUG-ROUTE", "DRUG-REASON", "DRUG-STRENGTH", "DRUG-DURATION".



{%- endcapture -%}

{%- capture model_input_anno -%}
WORD_EMBEDDINGS, POS, CHUNK, DEPENDENCY
{%- endcapture -%}

{%- capture model_output_anno -%}
CATEGORY
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

documenter = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentencer = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentences")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentences"])\
    .setOutputCol("tokens")

words_embedder = nlp.WordEmbeddingsModel()\
    .pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentences", "tokens"])\
    .setOutputCol("embeddings")

pos_tagger = nlp.PerceptronModel()\
    .pretrained("pos_clinical", "en", "clinical/models") \
    .setInputCols(["sentences", "tokens"])\
    .setOutputCol("pos_tags")

ner_tagger = medical.NerModel()\
    .pretrained("ner_posology", "en", "clinical/models")\
    .setInputCols("sentences", "tokens", "embeddings")\
    .setOutputCol("ner_tags")

ner_chunker = medical.NerConverterInternal()\
    .setInputCols(["sentences", "tokens", "ner_tags"])\
    .setOutputCol("ner_chunks")

dependency_parser = nlp.DependencyParserModel()\
    .pretrained("dependency_conllu", "en")\
    .setInputCols(["sentences", "pos_tags", "tokens"])\
    .setOutputCol("dependencies")

reModel = medical.RelationExtractionModel()\
    .pretrained("posology_re")\
    .setInputCols(["embeddings", "pos_tags", "ner_chunks", "dependencies"])\
    .setOutputCol("relations")\
    .setMaxSyntacticDistance(4)

pipeline = nlp.Pipeline(stages=[
    documenter,
    sentencer,
    tokenizer,
    words_embedder,
    pos_tagger,
    ner_tagger,
    ner_chunker,
    dependency_parser,
    reModel
])

text = """
The patient was prescribed 1 unit of Advil for 5 days after meals. The patient was also
given 1 unit of Metformin daily.
He was seen by the endocrinology service and she was discharged on 40 units of insulin glargine at night ,
12 units of insulin lispro with meals , and metformin 1000 mg two times a day.
"""
df = spark.createDataFrame([[text]]).toDF("text")
result = pipeline.fit(df).transform(df)

# Show results
result.select(F.explode(F.arrays_zip(
                              result.relations.result,
                              result.relations.metadata)).alias("cols"))\
.select(
    F.expr("cols['1']['chunk1']").alias("chunk1"),
    F.expr("cols['1']['chunk2']").alias("chunk2"),
    F.expr("cols['1']['entity1']").alias("entity1"),
    F.expr("cols['1']['entity2']").alias("entity2"),
    F.expr("cols['0']").alias("relations"),
    F.expr("cols['1']['confidence']").alias("confidence")).show(5, truncate=False)

+---------+----------------+-------+---------+--------------+----------+
|chunk1   |chunk2          |entity1|entity2  |relations     |confidence|
+---------+----------------+-------+---------+--------------+----------+
|1 unit   |Advil           |DOSAGE |DRUG     |DOSAGE-DRUG   |1.0       |
|Advil    |for 5 days      |DRUG   |DURATION |DRUG-DURATION |1.0       |
|1 unit   |Metformin       |DOSAGE |DRUG     |DOSAGE-DRUG   |1.0       |
|Metformin|daily           |DRUG   |FREQUENCY|DRUG-FREQUENCY|1.0       |
|40 units |insulin glargine|DOSAGE |DRUG     |DOSAGE-DRUG   |1.0       |
+---------+----------------+-------+---------+--------------+----------+

{%- endcapture -%}

{%- capture model_scala_medical -%}
import spark.implicits._

val documenter = new DocumentAssembler()
    .setInputCol("text") 
    .setOutputCol("document") 

val sentencer = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentences") 

val tokenizer = new Tokenizer()
    .setInputCols("sentences") 
    .setOutputCol("tokens") 

val words_embedder = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models") 
    .setInputCols(Array("sentences","tokens")) 
    .setOutputCol("embeddings") 

val pos_tagger = PerceptronModel.pretrained("pos_clinical","en","clinical/models") 
    .setInputCols(Array("sentences","tokens")) 
    .setOutputCol("pos_tags") 

val ner_tagger = MedicalNerModel.pretrained("ner_posology","en","clinical/models") 
    .setInputCols("sentences","tokens","embeddings") 
    .setOutputCol("ner_tags") 

val ner_chunker = new NerConverterInternal()
    .setInputCols(Array("sentences","tokens","ner_tags")) 
    .setOutputCol("ner_chunks") 

val dependency_parser = DependencyParserModel.pretrained("dependency_conllu","en") 
    .setInputCols(Array("sentences","pos_tags","tokens")) 
    .setOutputCol("dependencies") 

val reModel = RelationExtractionModel.pretrained("posology_re") 
    .setInputCols(Array("embeddings","pos_tags","ner_chunks","dependencies")) 
    .setOutputCol("relations") 
    .setMaxSyntacticDistance(4) 

val pipeline = new Pipeline().setStages(Array(
                                             documenter, 
                                             sentencer, 
                                             tokenizer,
                                             words_embedder, 
                                             pos_tagger, 
                                             ner_tagger, 
                                             ner_chunker, 
                                             dependency_parser, 
                                             reModel )) 

val text = " The patient was prescribed 1 unit of Advil for 5 days after meals. The patient was also given 1 unit of Metformin daily. He was seen by the endocrinology service and she was discharged on 40 units of insulin glargine at night , 12 units of insulin lispro with meals ,and metformin 1000 mg two times a day. " 

val df = Seq(text) .toDF("text") 
val result = pipeline.fit(df) .transform(df) 

// Show results

+---------+----------------+-------+---------+--------------+----------+
|chunk1   |chunk2          |entity1|entity2  |relations     |confidence|
+---------+----------------+-------+---------+--------------+----------+
|1 unit   |Advil           |DOSAGE |DRUG     |DOSAGE-DRUG   |1.0       |
|Advil    |for 5 days      |DRUG   |DURATION |DRUG-DURATION |1.0       |
|1 unit   |Metformin       |DOSAGE |DRUG     |DOSAGE-DRUG   |1.0       |
|Metformin|daily           |DRUG   |FREQUENCY|DRUG-FREQUENCY|1.0       |
|40 units |insulin glargine|DOSAGE |DRUG     |DOSAGE-DRUG   |1.0       |
+---------+----------------+-------+---------+--------------+----------+

{%- endcapture -%}


{%- capture model_api_link -%}
[RelationExtractionModel](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/re/RelationExtractionModel.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[RelationExtractionModel](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/re/relation_extraction/index.html#sparknlp_jsl.annotator.re.relation_extraction.RelationExtractionModel)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[RelationExtractionModelNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/RelationExtractionModel.ipynb)
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
