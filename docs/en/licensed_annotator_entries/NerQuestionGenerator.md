{%- capture title -%}
NerQuestionGenerator
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}

`NerQuestionGenerator` takes an NER chunk (obtained by, e.g., `NerConverterInternal`) and generates a questions based on two entity types, a pronoun and a strategy.

The question is generated in the form of `[QUESTIONPRONOUN] [ENTITY1] [ENTITY2] [QUESTIONMARK]`. The generated question can be used by `QuestionAnswerer` or `ZeroShotNer` annotators to answer the question or find NER entities. 

Parametres:

- `questionPronoun`: Pronoun to be used in the question. E.g., 'When', 'Where', 'Why', 'How', 'Who', 'What'.
- `strategyType`: Strategy for the proccess, either `Paired` (default) or `Combined`.
- `questionMark`: Whether to add a question mark at the end of the question.
- `entities1`: List with the entity types of entities that appear first in the question. 
- `entities2`: List with the entity types of entities that appear second in the question.


All the parameters can be set using the corresponding set method in camel case. For example, `.setQuestionPronoun(True)`.
{%- endcapture -%}

{%- capture model_input_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_python_medical -%}

from johnsnowlabs import nlp, medical
import json

entities = [
    {
    "label": "Person",
    "patterns": ["Jon", "John", "John's"]
    },
    {
    "label": "Organization",
    "patterns": ["St. Mary's Hospital", "St. Mary's"]
    },
    {
        "label": "Condition",
        "patterns": ["vital signs", "heartbeat", "oxygen saturation levels"]
    }
]

with open('./entities.json', 'w') as jsonfile:
    json.dump(entities, jsonfile)


document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

entity_ruler = nlp.EntityRulerApproach() \
    .setInputCols(["document"]) \
    .setOutputCol("entity") \
    .setPatternsResource("./entities.json")\
    .setCaseSensitive(False)

qagenerator = medical.NerQuestionGenerator()\
    .setInputCols(["entity"])\
    .setOutputCol("question")\
    .setQuestionPronoun("How is")\
    .setEntities1(["Person"])\
    .setEntities2(["Condition"])\
    .setStrategyType("Paired")\
    .setQuestionMark(True)

prep_pipeline = nlp.Pipeline(stages=[
    document_assembler,
    entity_ruler,
    qagenerator
])

example_text = """At St. Mary's Hospital, the healthcare team closely monitored John's vital signs with unwavering attention. They recorded his heartbeat and oxygen saturation levels, promptly addressing any deviations from normal. Their dedication and expertise at St. Mary's played a vital role in ensuring John's stability and fostering a swift recovery."""

df = spark.createDataFrame([[example_text]]).toDF("text")

result = prep_pipeline.fit(df).transform(df)

result.select("question").show(truncate=False)

## Result

+--------------------------------------------------------------------------------------------------------------------------------------------+
|question                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------+
|[{document, 62, 79, How is John's vital signs ?, {sentence -> 0}, []}, {document, 291, 134, How is John's heartbeat ?, {sentence -> 0}, []}]|
+--------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}


{%- capture model_scala_medical -%}

import spark.implicits._

/* entities.json file
entities = [
    {
    "label": "Person",
    "patterns": ["Jon", "John", "John's"]
    },
    {
    "label": "Organization",
    "patterns": ["St. Mary's Hospital", "St. Mary's"]
    },
    {
        "label": "Condition",
        "patterns": ["vital signs", "heartbeat", "oxygen saturation levels"]
    }
]
*/

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val entity_ruler = new EntityRulerApproach()
    .setInputCols("document")
    .setOutputCol("entity")
    .setPatternsResource("./entities.json")
    .setCaseSensitive(false)

val qagenerator = new NerQuestionGenerator()
    .setInputCols("entity")
    .setOutputCol("question")
    .setQuestionPronoun("How is")
    .setEntities1("Person")
    .setEntities2("Condition")
    .setStrategyType("Paired")
    .setQuestionMark(true)

val prep_pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    entity_ruler, 
    qagenerator )) 

val test_data = Seq("""At St. Mary's Hospital, the healthcare team closely monitored John's vital signs with unwavering attention. They recorded his heartbeat and oxygen saturation levels, promptly addressing any deviations from normal. Their dedication and expertise at St. Mary's played a vital role in ensuring John's stability and fostering a swift recovery.""").toDF("text")

val res = mapperPipeline.fit(test_data).transform(test_data)

// Show results

+--------------------------------------------------------------------------------------------------------------------------------------------+
|question                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------+
|[{document, 62, 79, How is John's vital signs ?, {sentence -> 0}, []}, {document, 291, 134, How is John's heartbeat ?, {sentence -> 0}, []}]|
+--------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}

{%- capture model_api_link -%}
[NerQuestionGenerator](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/qa/NerQuestionGenerator.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[NerQuestionGenerator](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/qa/qa_ner_generator/index.html#sparknlp_jsl.annotator.qa.qa_ner_generator.NerQuestionGenerator)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[NerQuestionGeneratorNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/NerQuestionGenerator.ipynb)
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
