{%- capture title -%}
TextGenerator
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
TextGenerator uses the basic BioGPT model to perform various tasks related to medical text abstraction. With this annotator, a user can provide a prompt and context and instruct the system to perform a specific task, such as explaining why a patient may have a particular disease or paraphrasing the context more directly. In addition, this annotator can create a clinical note for a cancer patient using the given keywords or write medical texts based on introductory sentences. The BioGPT model is trained on large volumes of medical data allowing it to identify and extract the most relevant information from the text provided.

Available models can be found at the [Models Hub](https://nlp.johnsnowlabs.com/models?annotator=MedicalTextGenerator).

For more extended examples on document pre-processing see the [Spark NLP Workshop](https://github.com/JohnSnowLabs/spark-nlp-workshop).
{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import * 

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("documents")


med_text_generator   = medical.TextGenerator\
    .pretrained("medical_text_generator","en","clinical/models")\
    .setInputCols("documents")\
    .setOutputCol("summary")\
    .setMaxNewTokens(20)\
    .setDoSample(True)\
    .setTopK(3)\
    .setRandomSeed(42)


pipeline = nlp.Pipeline(stages=[document_assembler, med_text_generator ])


data = spark.createDataFrame([
    ["Covid 19 is"],
    ["The most common cause of stomach pain is"]
]).toDF("text")


pipeline.fit(data).transform(data)
{%- endcapture -%}


{%- capture model_scala_medical -%}
from johnsnowlabs import * 

val document_assembler = new nlp.DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("documents")


val med_text_generator = medical.TextGenerator
    .pretrained("medical_text_generator", "en", "clinical/models")
    .setInputCols("documents")
    .setOutputCol("summary")
    .setMaxNewTokens(20)
    .setDoSample(true)
    .setTopK(3)
    .setRandomSeed(42)


val pipeline = new nlp.Pipeline().setStages(Array(document_assembler, med_text_generator ))


val data = Seq(Array( "Covid 19 is", "The most common cause of stomach pain is")).toDS.toDF("text")


val result = pipeline.fit(data).transform(data)
{%- endcapture -%}


{%- capture model_python_legal -%}
from johnsnowlabs import * 

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("documents")


med_text_generator   = legal.TextGenerator\
    .pretrained("medical_text_generator","en","clinical/models")\
    .setInputCols("documents")\
    .setOutputCol("summary")\
    .setMaxNewTokens(20)\
    .setDoSample(True)\
    .setTopK(3)\
    .setRandomSeed(42)


pipeline = nlp.Pipeline(stages=[document_assembler, med_text_generator ])


data = spark.createDataFrame([
    ["Covid 19 is"],
    ["The most common cause of stomach pain is"]
]).toDF("text")


pipeline.fit(data).transform(data)
{%- endcapture -%}



{%- capture model_scala_legal -%}
from johnsnowlabs import * 

val document_assembler = new nlp.DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("documents")


val med_text_generator = legal.TextGenerator
    .pretrained("medical_text_generator", "en", "clinical/models")
    .setInputCols("documents")
    .setOutputCol("summary")
    .setMaxNewTokens(20)
    .setDoSample(true)
    .setTopK(3)
    .setRandomSeed(42)


val pipeline = new nlp.Pipeline().setStages(Array(document_assembler, med_text_generator ))


val data = Seq(Array( "Covid 19 is", "The most common cause of stomach pain is")).toDS.toDF("text")


val result = pipeline.fit(data).transform(data)
{%- endcapture -%}




{%- capture model_python_finance -%}
from johnsnowlabs import * 

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("documents")


med_text_generator   = finance.TextGenerator\
    .pretrained("medical_text_generator","en","clinical/models")\
    .setInputCols("documents")\
    .setOutputCol("summary")\
    .setMaxNewTokens(20)\
    .setDoSample(True)\
    .setTopK(3)\
    .setRandomSeed(42)


pipeline = nlp.Pipeline(stages=[document_assembler, med_text_generator ])


data = spark.createDataFrame([
    ["Covid 19 is"],
    ["The most common cause of stomach pain is"]
]).toDF("text")


pipeline.fit(data).transform(data)
{%- endcapture -%}


{%- capture model_scala_finance -%}
from johnsnowlabs import * 

val document_assembler = new nlp.DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("documents")


val med_text_generator = finance.TextGenerator
    .pretrained("medical_text_generator", "en", "clinical/models")
    .setInputCols("documents")
    .setOutputCol("summary")
    .setMaxNewTokens(20)
    .setDoSample(true)
    .setTopK(3)
    .setRandomSeed(42)


val pipeline = new nlp.Pipeline().setStages(Array(document_assembler, med_text_generator ))


val data = Seq(Array( "Covid 19 is", "The most common cause of stomach pain is")).toDS.toDF("text")


val result = pipeline.fit(data).transform(data)
{%- endcapture -%}

{%- capture model_api_link -%}
[MedicalTextGenerator]()
{%- endcapture -%}

{%- capture model_python_api_link -%}
[MedicalTextGenerator]()
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical
model_python_legal=model_python_legal
model_scala_legal=model_scala_legal
model_python_finance=model_python_finance
model_scala_finance=model_scala_finance
model_api_link=model_api_link
model_python_api_link=model_python_api_link
%}
