{%- capture title -%}
TextGenerator
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
The Medical, Financial, and Legal Text Generators are specialized tools designed for text abstraction in their respective fields. The `MedicalTextGenerator`, based on the BioGPT model, excels in medical text abstraction, allowing users to provide prompts and contexts for tasks like disease explanation, paraphrasing medical context, or creating clinical notes for cancer patients. This model is adept at extracting relevant information due to its training on extensive medical data.

Similarly, the Financial and Legal Text Generators utilize the Flan-T5 model, an advanced version of the T5 model, for tasks in financial and legal text abstraction. Users can input prompts and contexts to receive high-quality summaries, document abstractions, and other text-based outputs. The Flan-T5 model's training on a diverse range of texts ensures the generation of coherent and accurate content in these domains.

Parameters:

- `maxNewTokens`: Maximum number of of new tokens to generate, by default 30

- `maxContextLength`: Maximum length of context text

- `configProtoBytes`: ConfigProto from tensorflow, serialized into byte array.

- `doSample`: Whether or not to use sampling; use greedy decoding otherwise, by default False

- `topK`: The number of highest probability vocabulary tokens to consider, by default 1

- `noRepeatNgramSize`: The number of tokens that can’t be repeated in the same order. Useful for preventing loops. The default is 0.

- `ignoreTokenIds`: A list of token ids which are ignored in the decoder’s output, by default []

- `randomSeed`: Set to positive integer to get reproducible results, by default None.

- `customPrompt`: The only available variable is {DOCUMENT} and it is populated with the contents of the input document

Available models can be found at the [Models Hub](https://nlp.johnsnowlabs.com/models?task=Text+Generation&language=en&type=model).

For more extended examples on document pre-processing see the [Spark NLP Workshop](https://github.com/JohnSnowLabs/spark-nlp-workshop).
{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_python_medical -%}

from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("prompt")\
    .setOutputCol("document_prompt")

med_text_generator  = medical.TextGenerator.pretrained("text_generator_biomedical_biogpt_base", "en", "clinical/models")\
    .setInputCols("document_prompt")\
    .setOutputCol("answer")\
    .setMaxNewTokens(256)\
    .setDoSample(True)\
    .setTopK(3)\
    .setRandomSeed(42)\
    .setStopAtEos(True)

pipeline = nlp.Pipeline(stages=[document_assembler, med_text_generator])

data = spark.createDataFrame([['Covid 19 is']]).toDF("prompt")

result = pipeline.fit(data).transform(data)

result.select("answer.result").show(truncate=False)

+--------------------------------------------------------------------------+
|result                                                                    |
+--------------------------------------------------------------------------+
|[Covid 19 is a pandemic that has affected the world's economy and health.]|
+--------------------------------------------------------------------------+
{%- endcapture -%}


{%- capture model_scala_medical -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("prompt")
  .setOutputCol("document_prompt")

val medTextGenerator = TextGenerator.pretrained("text_generator_biomedical_biogpt_base", "en", "clinical/models")
  .setInputCols(Array("document_prompt"))
  .setOutputCol("answer")
  .setMaxNewTokens(256)
  .setDoSample(true)
  .setTopK(3)
  .setRandomSeed(42)
  .setStopAtEos(true)

val pipeline = new Pipeline().setStages(Array(documentAssembler, medTextGenerator))

val data = Seq("Covid 19 is").toDS.toDF("prompt")

val result = pipeline.fit(data).transform(data)

result.selectExpr("answer.result").show(false)

+--------------------------------------------------------------------------+
|result                                                                    |
+--------------------------------------------------------------------------+
|[Covid 19 is a pandemic that has affected the world's economy and health.]|
+--------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_python_legal -%}
from johnsnowlabs import nlp, legal

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("prompt")

flant5 = legal.TextGenerator.pretrained("leggen_flant5_finetuned","en","legal/models")\
    .setInputCols(["prompt"])\
    .setOutputCol("answer")\
    .setMaxNewTokens(200)\
    .setTopK(3)\
    .setRandomSeed(42)\
    .setNoRepeatNgramSize(3)\
    .setStopAtEos(True)
 
pipeline = nlp.Pipeline(stages=[document_assembler, flant5])

data = spark.createDataFrame([["This exhibit has been redacted and is the subject of a confidential treatment request. Redacted material is marked with [* * *] and has been filed separately with the securities and exchange commission."]]).toDF("text")

pipeline.fit(data).transform(data)

result = pipeline.fit(data).transform(data)

result.select("answer.result").show(truncate=False)

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| result                                                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This exhibit has been redacted and is the subject of a confidential treatment request. Redacted material is marked with [* * *] and has been filed separately with the securities and exchange commission. The redacted material is confidential |
| and will not be disclosed to any third party without the prior written consent of the parties.                                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}

{%- capture model_scala_legal -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("prompt")

val flanT5 = TextGenerator.pretrained("leggen_flant5_finetuned", "en", "legal/models")
  .setInputCols(Array("prompt"))
  .setOutputCol("answer")
  .setMaxNewTokens(200)
  .setTopK(3)
  .setRandomSeed(42)
  .setNoRepeatNgramSize(3)
  .setStopAtEos(true)

val pipeline = new Pipeline().setStages(Array(documentAssembler, flanT5))

val data = Seq("This exhibit has been redacted and is the subject of a confidential treatment request. Redacted material is marked with [* * *] and has been filed separately with the securities and exchange commission.").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)

result.selectExpr("answer.result").show(false)

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| result                                                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This exhibit has been redacted and is the subject of a confidential treatment request. Redacted material is marked with [* * *] and has been filed separately with the securities and exchange commission. The redacted material is confidential |
| and will not be disclosed to any third party without the prior written consent of the parties.                                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}

{%- capture model_python_finance -%}
from johnsnowlabs import nlp, finance 

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("prompt")

flant5 = finance.TextGenerator.pretrained("fingen_flant5_base","en","finance/models")\
    .setInputCols(["prompt"])\
    .setOutputCol("answer")\
    .setMaxNewTokens(150)\
    .setStopAtEos(True)\
  
pipeline = nlp.Pipeline(stages=[document_assembler, flant5])

data = spark.createDataFrame([["Explain what is Sec 10-k filing"]]).toDF('text')

result = pipeline.fit(data).transform(data)

result.select("answer.result").show(truncate=False)

result = pipeline.fit(data).transform(data)

+--------------------------------------------------------------------------------------------------------------------+
|result                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------+
|[Sec 10k filing is a form of tax filing that requires a party to file jointly or several entities for tax purposes.]|
+--------------------------------------------------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_scala_finance -%}

import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("prompt")

val flanT5 = TextGenerator.pretrained("fingen_flant5_base", "en", "finance/models")
  .setInputCols(Array("prompt"))
  .setOutputCol("answer")
  .setMaxNewTokens(150)
  .setStopAtEos(true)

val pipeline = new Pipeline().setStages(Array(documentAssembler, flanT5))

val data = Seq("Explain what is Sec 10-k filing").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)

result.selectExpr("answer.result").show(false)

+--------------------------------------------------------------------------------------------------------------------+
|result                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------+
|[Sec 10k filing is a form of tax filing that requires a party to file jointly or several entities for tax purposes.]|
+--------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}

{%- capture model_api_link -%}
[MedicalTextGenerator](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/seq2seq/MedicalTextGenerator.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[MedicalTextGenerator](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/seq2seq/medical_text_generator/index.html)
{%- endcapture -%}

{%- capture model_notebook_link -%}

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
model_notebook_link=model_notebook_link%}
