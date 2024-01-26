{%- capture title -%}
NameChunkObfuscator
{%- endcapture -%}

{%- capture approach -%}
approach
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
`NameChunkObfuscator` annotator allows to transform a dataset with an Input Annotation of type CHUNK, into its obfuscated version of by obfuscating the given CHUNKS. This module can replace name entities with consistent fakers, remain others same.

Obfuscation, refers to the process of de-identifying or removing sensitive patient information from clinical notes or other healthcare documents. The purpose of PHI obfuscation is to protect patient privacy and comply with regulations such as the Health Insurance Portability and Accountability Act (HIPAA).

It is important to note that the obfuscation should be done carefully to ensure that the de-identified data cannot be re-identified. Organizations must follow best practices and adhere to applicable regulations to protect patient privacy and maintain data security.

Parameters:

- `seed`:  The seed to select the names on obfuscation. With the seed, you can reply an execution several times with the same output..

- `obfuscateRefSource`: Sets mode for select obfuscate source [‘both’, ’faker’, ‘file’] Default: ‘both’.

- `language`: The language used to select some faker names. The values are the following: ‘en’(english),’de’(german), ‘es’(Spanish), ‘fr’(french) or ‘ro’(romanian) Default:’en’.

- `sameLength`: The sameLength used to select the same length names as original ones during obfuscation. Example: ‘John’ –> ‘Mike’. Default: true.

- `nameEntities`: The nameEntities used to select entities during obfuscation. The supported name entities are NAME, PATIENT, and DOCTOR. Default: 'NAME'

- `genderAwareness`: Whether to use gender-aware names or not during obfuscation. This param effects only names.
Default: False

{%- endcapture -%}

{%- capture model_input_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import medical, nlp

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_ner = medical.NerModel.pretrained("ner_deid_generic_augmented", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

nameChunkObfuscator = medical.NameChunkObfuscator()\
  .setInputCols("ner_chunk")\
  .setOutputCol("replacement")\
  .setObfuscateRefSource("faker")\
  .setNameEntities(["DOCTOR", "PATIENT"])\
  .setGenderAwareness(True)

replacer_name = medical.Replacer()\
  .setInputCols("replacement","sentence")\
  .setOutputCol("obfuscated_sentence_name")\
  .setUseReplacement(True)

nlpPipeline = nlp.Pipeline(stages=[
      documentAssembler,
      sentenceDetector,
      tokenizer,
      word_embeddings,
      clinical_ner,
      ner_converter,
      nameChunkObfuscator,
      replacer_name])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = nlpPipeline.fit(empty_data)

## sample data
text ='''
Record date : 2093-01-13 , David Hale , M.D . , Patient name : Michael  , MR # 7194334 Date : 01/13/93 . PCP : Oliveira , 25 years-old , Record date : 2079-11-09 . Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555. Analyzed by Dr. Jennifer  .
'''

result = model.transform(spark.createDataFrame([[text]]).toDF("text"))

result.select(F.explode(F.arrays_zip(result.sentence.result,
                                     result.obfuscated_sentence_name.result)).alias("cols")) \
      .select(F.expr("cols['0']").alias("sentence"), 
              F.expr("cols['1']").alias("obfuscated_sentence_name"))


| sentence                                          | obfuscated_sentence_name                                  |
| ------------------------------------------------- | --------------------------------------------------------- |
| Record date : 2093-01-13 , David Hale , M.D .     | Record date : 2093-01-13 , Richardson , M.D .             |
| , Patient name : Michael , MR # 7194334 Date ...	| , Patient name : Thaxter , MR # 7194334 Date ...          |
| PCP : Oliveira , 25 years-old , Record date : ... | PCP : Adelaida , 25 years-old , Record date : ...         |
| Cocke County Baptist Hospital , 0295 Keats Str... | Cocke County Baptist Hospital , 0295 Keats Str...         |
| Analyzed by Dr. Jennifer .                        | Analyzed by Dr. Morganne .                                |

{%- endcapture -%}


{%- capture model_scala_medical -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val clinical_ner = MedicalNerModel.pretrained("ner_deid_generic_augmented", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val nameChunkObfuscator = new NameChunkObfuscator()
    .setInputCols("ner_chunk")
    .setOutputCol("replacement")
    .setObfuscateRefSource("faker")
    .setNameEntities(Array("DOCTOR", "PATIENT"))
    .setGenderAwareness(true)

val replacer_name = new Replacer()
    .setInputCols(Array("replacement","sentence"))
    .setOutputCol("obfuscated_sentence_name")
    .setUseReplacement(true)

val nlpPipeline = new Pipeline().setStages(Array(
      documentAssembler,
      sentenceDetector,
      tokenizer,
      word_embeddings,
      clinical_ner,
      ner_converter,
      nameChunkObfuscator,
      replacer_name))

val data = Seq("Record date : 2093-01-13 , David Hale , M.D . , Name : Hendrickson Ora , MR # 7194334 Date : 01/13/93 . PCP : Oliveira , 25 years-old , Record date : 2079-11-09 . Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 .").toDF("text")

val result = nlpPipeline.fit(data).transfrom(data)


| sentence                                          | obfuscated_sentence_name                                  |
| ------------------------------------------------- | --------------------------------------------------------- |
| Record date : 2093-01-13 , David Hale , M.D .     | Record date : 2093-01-13 , Richardson , M.D .             |
| , Patient name : Michael , MR # 7194334 Date ...	| , Patient name : Thaxter , MR # 7194334 Date ...          |
| PCP : Oliveira , 25 years-old , Record date : ... | PCP : Adelaida , 25 years-old , Record date : ...         |
| Cocke County Baptist Hospital , 0295 Keats Str... | Cocke County Baptist Hospital , 0295 Keats Str...         |
| Analyzed by Dr. Jennifer .                        | Analyzed by Dr. Morganne .                                |

{%- endcapture -%}

{%- capture model_api_link -%}
[NameChunkObfuscator](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/deid/NameChunkObfuscator.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[NameChunkObfuscator](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/deid/name_obfuscator/index.html#sparknlp_jsl.annotator.deid.name_obfuscator.NameChunkObfuscator)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[NameChunkObfuscatorNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/NameChunkObfuscator.ipynb)
{%- endcapture -%}

{%- capture approach_description -%}
`NameChunkObfuscator` annotator that can be used in deidentification tasks for replacing doctor and patient names with fake names using a reference document.
{%- endcapture -%}

{%- capture approach_input_anno -%}
CHUNK
{%- endcapture -%}

{%- capture approach_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture approach_python_medical -%}

from johnsnowlabs import medical, nlp

names = """Mitchell-NAME
Clifford-NAME
Jeremiah-NAME
Lawrence-NAME
Brittany-NAME
Patricia-NAME
Jennifer-NAME
Jackson-NAME
Leonard-NAME
Randall-NAME
Camacho-NAME
Ferrell-NAME
Mueller-NAME
Bowman-NAME
Hansen-NAME
"""

with open('names_test2.txt', 'w') as file:
    file.write(names)

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_ner = medical.NerModel.pretrained("ner_deid_generic_augmented", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

nameChunkObfuscator = medical.NameChunkObfuscatorApproach()\
  .setInputCols("ner_chunk")\
  .setOutputCol("replacement")\
  .setObfuscateRefFile("names_test2.txt")\
  .setObfuscateRefSource("file")\
  .setRefFileFormat("csv")\
  .setRefSep("-")

replacer_name = medical.Replacer()\
  .setInputCols("replacement","sentence")\
  .setOutputCol("obfuscated_sentence_name")\
  .setUseReplacement(True)

nlpPipeline = nlp.Pipeline(stages=[
      documentAssembler, 
      sentenceDetector,
      tokenizer,
      word_embeddings,
      clinical_ner,
      ner_converter,
      nameChunkObfuscator,
      replacer_name])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = nlpPipeline.fit(empty_data)

## Results
text ='''
M.D . , Patient name : Michael  , MR # 7194334 Date : 01/13/93 . PCP : Oliveira , 25 years-old , Record date : 2079-11-09 . Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555. Analyzed by Dr. Jennifer  .
'''

result = model.transform(spark.createDataFrame([[text]]).toDF("text"))

result.select(F.explode(F.arrays_zip(result.sentence.result, 
                                     result.obfuscated_sentence_name.result)).alias("cols")) \
      .select(F.expr("cols['0']").alias("sentence"), F.expr("cols['1']").alias("obfuscated_sentence_name"))

| sentence                                          | obfuscated_sentence_name                          | 
| ------------------------------------------------- | ------------------------------------------------- |
| M.D .                                             | M.D .                                             |
| , Patient name : Michael , MR # 7194334 Date ...  | , Patient name : Ferrell , MR # 7194334 Date ...  |
| PCP : Oliveira , 25 years-old , Record date : ...	| PCP : Clifford , 25 years-old , Record date : ... |
| Cocke County Baptist Hospital , 0295 Keats Str... | Cocke County Baptist Hospital , 0295 Keats Str... |
| Analyzed by Dr. Jennifer .                        | Analyzed by Dr. Jennifer .                        |

{%- endcapture -%}


{%- capture approach_scala_medical -%}

val names = """Mitchell-NAME
Clifford-NAME
Jeremiah-NAME
Lawrence-NAME
Brittany-NAME
Patricia-NAME
Jennifer-NAME
Jackson-NAME
Leonard-NAME
Randall-NAME
Camacho-NAME
Ferrell-NAME
Mueller-NAME
Bowman-NAME
Hansen-NAME
"""
/*
with open("names_test2.txt", 'w') as file:
    file.write(names)
*/

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val clinical_ner = MedicalNerModel.pretrained("ner_deid_generic_augmented", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val nameChunkObfuscator = new NameChunkObfuscatorApproach()
    .setInputCols("ner_chunk")
    .setOutputCol("replacement")
    .setObfuscateRefFile("names_test2.txt")\
    .setObfuscateRefSource("file")
    .setRefFileFormat("csv")
    .setRefSep("-")

val replacer_name = new Replacer()
    .setInputCols(Array("replacement","sentence"))
    .setOutputCol("obfuscated_sentence_name")
    .setUseReplacement(true)

val nlpPipeline = new Pipeline().setStages((
      documentAssembler, 
      sentenceDetector,
      tokenizer,
      word_embeddings,
      clinical_ner,
      ner_converter,
      nameChunkObfuscator,
      replacer_nam))

val data = Seq("M.D . , Patient name : Michael  , MR # 7194334 Date : 01/13/93 . PCP : Oliveira , 25 years-old , Record date : 2079-11-09 . Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555. Analyzed by Dr. Jennifer  .").toDF("text")

val res = nlpPipeline.fit(data).transform(data)

| sentence                                          | obfuscated_sentence_name                          | 
| ------------------------------------------------- | ------------------------------------------------- |
| M.D .                                             | M.D .                                             |
| , Patient name : Michael , MR # 7194334 Date ...  | , Patient name : Ferrell , MR # 7194334 Date ...  |
| PCP : Oliveira , 25 years-old , Record date : ...	| PCP : Clifford , 25 years-old , Record date : ... |
| Cocke County Baptist Hospital , 0295 Keats Str... | Cocke County Baptist Hospital , 0295 Keats Str... |
| Analyzed by Dr. Jennifer .                        | Analyzed by Dr. Jennifer .                        |

{%- endcapture -%}


{%- capture approach_api_link -%}
[NameChunkObfuscatorApproach](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/deid/NameChunkObfuscatorApproach.html)
{%- endcapture -%}

{%- capture approach_python_api_link -%}
[NameChunkObfuscatorApproach](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/deid/name_obfuscator/index.html#sparknlp_jsl.annotator.deid.name_obfuscator.NameChunkObfuscatorApproach)
{%- endcapture -%}

{%- capture approach_notebook_link -%}
[NameChunkObfuscatorApproachNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/NameChunkObfuscatorApproach.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
approach=approach
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical
model_api_link=model_api_link
model_python_api_link=model_python_api_link
model_notebook_link=model_notebook_link
approach_description=approach_description
approach_input_anno=approach_input_anno
approach_output_anno=approach_output_anno
approach_python_medical=approach_python_medical
approach_scala_medical=approach_scala_medical
approach_api_link=approach_api_link
approach_python_api_link=approach_python_api_link
approach_notebook_link=approach_notebook_link
%}
