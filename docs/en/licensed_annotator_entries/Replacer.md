{%- capture title -%}
Replacer
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
`Replacer` allows to replace entities in the original text with the ones extracted by the annotators `NameChunkObfuscatorApproach` or `DateNormalizer`. 

`Replacer` is most often used in conjunction with the `DateNormalizer` annotator or in deidentification pipelines.

With the dates, the `Replacer` annotator is used to replace specific tokens in a text with another token or string. The `DateNormalizer` annotator, on the other hand, is used to normalize dates and times to a standardized format.

Obfuscation in healthcare is the act of making healthcare data difficult to understand or use without authorization. This can be done by replacing or removing identifying information, such as names, dates of birth, and Social Security numbers. Obfuscation can also be used to hide the contents of healthcare records, such as diagnoses, medications, and treatment plans.

In the **deidentification** process, the `Replacer` annotator is used to replace certain tokens or patterns in the text with specified values. For example, it can be used to replace all instances of a person's name with a placeholder like "PERSON".

The `NameChunkObfuscatorApproach` annotator is used to identify and obfuscate sensitive named entities in the text, such as people's names, addresses, dates of birth, SSNs etc.

Parameter:

- `setUseReplacement`: (Boolean) Select what output format should be used. By default it will use the current day.   

{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

names = """Mitchell#NAME
Clifford#NAME
Jeremiah#NAME
Lawrence#NAME
Brittany#NAME
Patricia#NAME
Samantha#NAME
Jennifer#NAME
Jackson#NAME
Leonard#NAME
Randall#NAME
Camacho#NAME
Ferrell#NAME
Mueller#NAME
Bowman#NAME
Hansen#NAME
Acosta#NAME
Gillespie#NAME
Zimmerman#NAME
Gillespie#NAME
Chandler#NAME
Bradshaw#NAME
Ferguson#NAME
Jacobson#NAME
Figueroa#NAME
Chandler#NAME
Schaefer#NAME
Matthews#NAME
Ferguson#NAME
Bradshaw#NAME
Figueroa#NAME
Delacruz#NAME
Gallegos#NAME
Villarreal#NAME
Williamson#NAME
Montgomery#NAME
Mclaughlin#NAME
Blankenship#NAME
Fitzpatrick#NAME
"""

with open('names_test.txt', 'w') as file:
    file.write(names)


# Annotator that transforms a text column from dataframe into an Annotation ready for NLP
documentAssembler = nlp.DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("sentence")\

# Tokenizer splits words in a relevant format for NLP
tokenizer = nlp.Tokenizer()\
  .setInputCols("sentence")\
  .setOutputCol("token")\

# Clinical word embeddings trained on PubMED dataset
word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

# NER model trained on n2c2 (de-identification and Heart Disease Risk Factors Challenge) datasets)
clinical_ner = medical.NerModel.pretrained("ner_deid_generic_augmented", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter_name = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")

nameChunkObfuscator = medical.NameChunkObfuscatorApproach()\
  .setInputCols("ner_chunk")\
  .setOutputCol("replacement")\
  .setRefFileFormat("csv")\
  .setObfuscateRefFile("names_test.txt")\
  .setRefSep("#")\

replacer_name = medical.Replacer()\
  .setInputCols("replacement","sentence")\
  .setOutputCol("obfuscated_document_name")\
  .setUseReplacement(True)

nlpPipeline = nlp.Pipeline(stages=[
    documentAssembler, 
    tokenizer,
    word_embeddings,
    clinical_ner,
    ner_converter_name,
    nameChunkObfuscator,
    replacer_name
    ])

sample_text = "John Davies is a 62 y.o. patient admitted. Mr. Davies was seen by attending physician Dr. Lorand and was scheduled for emergency assessment."

data = spark.createDataFrame([[sample_text]]).toDF("text")
result = nlpPipeline.fit(data).transform(data)

## Result

Original text.  :  John Davies is a 62 y.o. patient admitted. Mr. Davies was seen by attending physician Dr. Lorand and was scheduled for emergency assessment.

Obfuscated text :  Joseeduardo is a 62 y.o. patient admitted. Mr. Teigan was seen by attending physician Dr. Mayson and was scheduled for emergency assessment.

{%- endcapture -%}


{%- capture model_scala_medical -%}
import spark.implicits._

/* names.txt file

names = """Mitchell#NAME
Clifford#NAME
Jeremiah#NAME
Lawrence#NAME
Brittany#NAME
Patricia#NAME
Samantha#NAME
Jennifer#NAME
Jackson#NAME
Leonard#NAME
Randall#NAME
Camacho#NAME
Ferrell#NAME
Mueller#NAME
Bowman#NAME
Hansen#NAME
Acosta#NAME
Gillespie#NAME
Zimmerman#NAME
Gillespie#NAME
Chandler#NAME
Bradshaw#NAME
Ferguson#NAME
Jacobson#NAME
Figueroa#NAME
Chandler#NAME
Schaefer#NAME
Matthews#NAME
Ferguson#NAME
Bradshaw#NAME
Figueroa#NAME
Delacruz#NAME
Gallegos#NAME
Villarreal#NAME
Williamson#NAME
Montgomery#NAME
Mclaughlin#NAME
Blankenship#NAME
Fitzpatrick#NAME
"""
*/

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
    .setInputCols(Array("sentence","token"))
    .setOutputCol("embeddings")

val clinical_ner = MedicalNerModel.pretrained("ner_deid_generic_augmented","en","clinical/models")
    .setInputCols(Array("sentence","token","embeddings"))
    .setOutputCol("ner")

val ner_converter_name = new NerConverterInternal()
    .setInputCols(Array("sentence","token","ner"))
    .setOutputCol("ner_chunk")

val nameChunkObfuscator = new NameChunkObfuscatorApproach()
    .setInputCols("ner_chunk")
    .setOutputCol("replacement")
    .setRefFileFormat("csv")
    .setObfuscateRefFile("names_test.txt")
    .setRefSep("//")

val replacer_name = new Replacer()
    .setInputCols("replacement","sentence")
    .setOutputCol("obfuscated_document_name")
    .setUseReplacement(true)

val nlpPipeline = new Pipeline().setStages(Array(
    documentAssembler, 
    tokenizer, 
    word_embeddings, 
    clinical_ner, 
    ner_converter_name, 
    nameChunkObfuscator, 
    replacer_name))


val test_data = Seq("""John Davies is a 62 y.o. patient admitted. Mr. Davies was seen by attending physician Dr. Lorand and was scheduled for emergency assessment.""").toDF("text")

val res = mapperPipeline.fit(test_data).transform(test_data)

// Show results

Original text.  :  John Davies is a 62 y.o. patient admitted. Mr. Davies was seen by attending physician Dr. Lorand and was scheduled for emergency assessment.

Obfuscated text :  Joseeduardo is a 62 y.o. patient admitted. Mr. Teigan was seen by attending physician Dr. Mayson and was scheduled for emergency assessment.

{%- endcapture -%}

{%- capture model_api_link -%}
[Replacer](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/deid/Replacer.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[Replacer](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/deid/replacer/index.html#sparknlp_jsl.annotator.deid.replacer.Replacer)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[ReplacerNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/Replacer.ipynb)
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
