{%- capture title -%}
EntityRulerInternal
{%- endcapture -%}

{%- capture approach -%}
approach
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
This annotator match exact strings or regex patterns provided in a file against a Document and assigns them an named entity. The definitions can contain any number of named entities.

Parametres:
- `setPatternsResource` *(str)*: Sets Resource in JSON or CSV format to map entities to patterns.
        path : str
            Path to the resource
        read_as : str, optional
            How to interpret the resource, by default ReadAs.TEXT
        options : dict, optional
            Options for parsing the resource, by default {"format": "JSON"}

- `setSentenceMatch` *(Boolean)*: Whether to find match at sentence level. True: sentence level. False: token level.

- `setAlphabetResource` *(str)*: Alphabet Resource (a simple plain text with all language characters)

- `setUseStorage` *(Boolean)*: Sets whether to use RocksDB storage to serialize patterns.

See [Spark NLP Workshop](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/40.Rule_Based_Entity_Matchers.ipynb) for more examples of usage.

{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

entityRuler = medical.EntityRulerInternalApproach()\
    .setInputCols(["document", "token"])\
    .setOutputCol("entities")\
    .setPatternsResource("entities.json")\
    .setCaseSensitive(False)\

pipeline = nlp.Pipeline().setStages([
    documentAssembler,
    tokenizer,
    entityRuler
])

data = spark.createDataFrame([['''John's doctor prescribed aspirin for his heart condition, along with paracetamol for his fever and headache, amoxicillin for his tonsilitis, ibuprofen for his inflammation, and lansoprazole for his GORD on 2023-12-01.''']]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)

# Result
+---------------+-----+---+-------+
|          chunk|begin|end|  label|
+---------------+-----+---+-------+
|        aspirin|   25| 31|   Drug|
|heart condition|   41| 55|Disease|
|    paracetamol|   69| 79|   Drug|
|          fever|   89| 93|Symptom|
|       headache|   99|106|Symptom|
|     tonsilitis|  129|138|Disease|
|      ibuprofen|  141|149|   Drug|
|    lansoprazol|  177|187|   Drug|
|           GORD|  198|201|Disease|
+---------------+-----+---+-------+
{%- endcapture -%}


{%- capture model_scala_medical -%}
 
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols(Array("document"))
  .setOutputCol("token")

val entityRuler = new EntityRulerInternalApproach()
  .setInputCols(Array("document", "token"))
  .setOutputCol("entities")
  .setPatternsResource("entities.json")
  .setCaseSensitive(false)

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  tokenizer,
  entityRuler
))

val data = Seq(
  ("""John's doctor prescribed aspirin for his heart condition, along with paracetamol for his fever and headache, amoxicillin for his tonsillitis, ibuprofen for his inflammation, and lansoprazole for his GORD on 2023-12-01.""")
).toDF("text")

val model = pipeline.fit(data)

# Result
+---------------+-----+---+-------+
|          chunk|begin|end|  label|
+---------------+-----+---+-------+
|        aspirin|   25| 31|   Drug|
|heart condition|   41| 55|Disease|
|    paracetamol|   69| 79|   Drug|
|          fever|   89| 93|Symptom|
|       headache|   99|106|Symptom|
|     tonsilitis|  129|138|Disease|
|      ibuprofen|  141|149|   Drug|
|    lansoprazol|  177|187|   Drug|
|           GORD|  198|201|Disease|
+---------------+-----+---+-------+

{%- endcapture -%}

{%- capture approach_description -%}
EntityRulerInternal will handle the chunks output based on the patterns defined, as shown in the example below. We can define an id field to identify entities.

Parameters:

- `setPatternsResource` *(str)*: Sets Resource in JSON or CSV format to map entities to patterns.
        path : str
            Path to the resource
        read_as : str, optional
            How to interpret the resource, by default ReadAs.TEXT
        options : dict, optional
            Options for parsing the resource, by default {"format": "JSON"}

- `setSentenceMatch` *(Boolean)*: Whether to find match at sentence level. True: sentence level. False: token level.

- `setAlphabetResource` *(str)*: Alphabet Resource (a simple plain text with all language characters)

- `setUseStorage` *(Boolean)*: Sets whether to use RocksDB storage to serialize patterns.
{%- endcapture -%}

{%- capture approach_input_anno -%}
DOCUMENT, TOKEN
{%- endcapture -%}

{%- capture approach_output_anno -%}
CHUNK
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
approach=approach
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical
approach_description=approach_description
approach_input_anno=approach_input_anno
approach_output_anno=approach_output_anno
%}
