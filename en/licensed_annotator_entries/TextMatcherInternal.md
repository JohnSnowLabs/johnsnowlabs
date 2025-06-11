{%- capture title -%}
TextMatcherInternal
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
This annotator match exact phrases provided in a file against a Document.

Parametres:

- `entities` *(str)*: external resource for the entities.
        path : str
            Path to the external resource
        read_as : str, optional
            How to read the resource, by default ReadAs.TEXT
        options : dict, optional
            Options for reading the resource, by default {"format": "text"}
- `caseSensitive` *(Boolean)*: whether to match regardless of case. (Default: True)

- `mergeOverlapping` *(Boolean)*: whether to merge overlapping matched chunks. (Default: False)

- `entityValue` *(str)*: value for the entity metadata field. If any entity value isn't set in the file, we need to set it for the entity value.

- `buildFromTokens` *(Boolean)*: whether the TextMatcherInternal should take the CHUNK from TOKEN.

- `delimiter` *(str)*: value for the delimiter between Phrase, Entity.

- `enableLemmatizer` *(Boolean)*: whether to enable lemmatization. (Default: False)

- `enableStemmer` *(Boolean)*: whether to enable stemming. (Default: False)

- `cleanStopWords` *(Boolean)*: whether to clean stop words. (Default: False)

- `shuffleEntitySubTokens` *(Boolean)*: whether to use permutations of entity phrase tokens to improve matching. (Default: False)

- `safeKeywords` *(List[str])*: list of critical terms that should never be removed, even if they are stop words or noise words.

- `excludePunctuation` *(Boolean)*: whether to remove all punctuation characters during matching. (Default: False)

- `cleanKeywords` *(List[str])*: list of domain-specific noise words to be removed from entities.

- `excludeRegexPatterns` *(List[str])*: list of regex patterns; if a matched chunk fits one of these patterns, it will be discarded.

- `returnChunks` *(str)*: whether to return the matched phrase in its original form or normalized version. Accepted values: `"original"`, `"matched"`.

- `skipMatcherAugmentation` *(Boolean)*: whether to disable augmentation on the matcher side (e.g., token permutations). (Default: False)

- `skipSourceTextAugmentation` *(Boolean)*: whether to disable augmentation on the source text side. (Default: False)



See [Spark NLP Workshop](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/40.Rule_Based_Entity_Matchers.ipynb) for more examples of usage.
{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, TOKEN 
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

matcher_drug = """
Aspirin 100mg#Drug
aspirin#Drug
paracetamol#Drug
amoxicillin#Drug
ibuprofen#Drug
lansoprazole#Drug
"""

with open ('matcher_drug.csv', 'w') as f:
  f.write(matcher_drug)

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

entityExtractor = medical.TextMatcherInternal()\
    .setInputCols(["document", "token"])\
    .setEntities("matcher_drug.csv")\
    .setOutputCol("matched_text")\
    .setCaseSensitive(False)\
    .setDelimiter("#")\
    .setMergeOverlapping(False)

mathcer_pipeline = nlp.Pipeline().setStages([
                  documentAssembler,
                  tokenizer,
                  entityExtractor])

data = spark.createDataFrame([["John's doctor prescribed aspirin 100mg for his heart condition, along with paracetamol for his fever, amoxicillin for his tonsilitis, ibuprofen for his inflammation, and lansoprazole for his GORD."]]).toDF("text")

matcher_model = mathcer_pipeline.fit(data)
result = matcher_model.transform(data)

# result
+-------------+-----+---+-----+
|        chunk|begin|end|label|
+-------------+-----+---+-----+
|      aspirin|   25| 31| Drug|
|aspirin 100mg|   25| 37| Drug|
|  paracetamol|   75| 85| Drug|
|  amoxicillin|  102|112| Drug|
|    ibuprofen|  134|142| Drug|
| lansoprazole|  170|181| Drug|
+-------------+-----+---+-----+
{%- endcapture -%}


{%- capture model_scala_medical -%}
import spark.implicits._

//matcher_drug = """
//Aspirin 100mg#Drug
//aspirin#Drug
//paracetamol#Drug
//amoxicillin#Drug
//ibuprofen#Drug
//lansoprazole#Drug
//"""
//
//with open ('matcher_drug.csv', 'w') as f:
//  f.write(matcher_drug)

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols(Array("document"))
  .setOutputCol("token")

val entityExtractor = new EntityExtractor()
  .setInputCols(Array("document", "token"))
  .setOutputCol("matched_text")
  .setEntities("matcher_drug.csv")
  .setCaseSensitive(false)
  .setDelimiter("#")
  .setMergeOverlapping(false)

val matcherPipeline = new Pipeline()
  .setStages(Array(documentAssembler, 
                   tokenizer, 
                   entityExtractor))

val data = Seq("John's doctor prescribed aspirin 100mg for his heart condition, along with paracetamol for his fever, amoxicillin for his tonsilitis, ibuprofen for his inflammation, and lansoprazole for his GORD.")
  .toDF("text")

val matcherModel = matcherPipeline.fit(data)
val result = matcherModel.transform(data)


# result
+-------------+-----+---+-----+
|        chunk|begin|end|label|
+-------------+-----+---+-----+
|      aspirin|   25| 31| Drug|
|aspirin 100mg|   25| 37| Drug|
|  paracetamol|   75| 85| Drug|
|  amoxicillin|  102|112| Drug|
|    ibuprofen|  134|142| Drug|
| lansoprazole|  170|181| Drug|
+-------------+-----+---+-----+

{%- endcapture -%}

{%- capture model_api_link -%}
[TextMatcherInternal](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/matcher/TextMatcherInternalModel.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[TextMatcherInternal](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/matcher/text_matcher_internal/index.html)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[TextMatcherInternalNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/40.1.Text_Matcher_Internal.ipynb)
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
