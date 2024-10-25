{%- capture title -%}
MedicalLLM
{%- endcapture -%}


{%- capture model_description -%}

MedicalLLM was designed to load and run large language models (LLMs) in GGUF format with scalable performance. 
Ideal for clinical and healthcare applications, MedicalLLM supports tasks like medical entity extraction, summarization,
Q&A, Retrieval Augmented Generation (RAG), and conversational AI. With simple integration into Spark NLP pipelines,
it allows for customizable batch sizes, prediction settings, and chat templates. GPU optimization is also available,
enhancing its capabilities for high-performance environments. MedicalLLM empowers users to link medical entities and
perform complex NLP tasks with efficiency and precision.

To use GPU inference with this annotator, make sure to use the Spark NLP GPU package and set the number of GPU layers
with the setNGpuLayers method. When using larger models, we recommend adjusting GPU usage with setNCtx and setNGpuLayers 
according to your hardware to avoid out-of-memory errors.

Parameters:

- `inputPrefix` :  Prefix for infilling (default: empty)
- `inputSuffix` :  Suffix for infilling (default: empty)
- `cachePrompt` :  Whether to remember the prompt to avoid reprocessing it
- `nPredict`    :  Number of tokens to predict (default: -1, -1 = infinity, -2 = until context filled)
- `topK` :  Top-k sampling (default: 40, 0 = disabled)
- `topP` :  Top-p sampling (default: 0.9, 1.0 = disabled)
- `minP` :  Min-p sampling (default: 0.1, 0.0 = disabled)
- `tfsZ` :  Tail free sampling, parameter z (default: 1.0, 1.0 = disabled)
- `typicalP` :  Locally typical sampling, parameter p (default: 1.0, 1.0 = disabled)
- `temperature` :  The temperature (default: 0.8)
- `dynatempRange` :   Dynamic temperature range (default: 0.0, 0.0 = disabled)
- `dynatempExponent` :  Dynamic temperature exponent (default: 1.0)
- `repeatLastN` :  Last n tokens to consider for penalties (default: 64, 0 = disabled, -1 = ctx_size)
- `repeatPenalty` :  Penalty of repeated sequences of tokens (default: 1.0, 1.0 = disabled)
- `frequencyPenalty` :  Repetition alpha frequency penalty (default: 0.0, 0.0 = disabled)
- `presencePenalty` :  Repetition alpha presence penalty (default: 0.0, 0.0 = disabled)
- `mirostatTau` :  MiroStat target entropy, parameter tau (default: 5.0)
- `mirostatEta` :  MiroStat learning rate, parameter eta (default: 0.1)
- `penalizeNl` :  Whether to penalize newline tokens
- `nKeep` :  Number of tokens to keep from the initial prompt (default: 0, -1 = all)
- `seed` :  RNG seed (default: -1, use random seed for &lt; 0)
- `nProbs` :  Amount top tokens probabilities to output if greater than 0.
- `minKeep` :  Amount of tokens the samplers should return at least (0 = disabled)
- `grammar` :  BNF-like grammar to constrain generations (see samples in grammars/ dir)
- `penaltyPrompt` :  Override which part of the prompt is penalized for repetition. E.g. if original prompt is "Alice: Hello!" and penaltyPrompt is "Hello!", only the latter will be penalized if repeated. See <a href="https://github.com/ggerganov/llama.cpp/pull/3727">pull request 3727</a> for more details.
- `penaltyPromptTokens` :  PenaltyPromptTokens
- `ignoreEos` :  Whether to ignore end of stream token and continue generating (implies --logit-bias 2-inf)
- `stopStrings` :  Strings upon seeing which token generation is stopped
- `useChatTemplate` :  Whether or not generate should apply a chat template (default: false)

{%- endcapture -%}


{%- capture model_input_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_output_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_python_medical -%}


from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

medical_llm = medical.AutoGGUFModel.pretrained("jsl_meds_ner_q4_v2", "en", "clinical/models")\
    .setInputCols("document")\
    .setOutputCol("completions")\
    .setBatchSize(1)\
    .setNPredict(100)\
    .setUseChatTemplate(True)\
    .setTemperature(0)\
    #.setNGpuLayers(100) # if you have GPU


pipeline = nlp.Pipeline(
    stages = [
        document_assembler,
        medical_llm
    ])

med_ner_prompt = """
    ### Template:
    {
    "drugs": [
    {
    "name": "",
    "reactions": []
    }
    ]
    }
    ### Text:
    I feel a bit drowsy & have a little blurred vision , and some gastric problems .
    I 've been on Arthrotec 50 for over 10 years on and off , only taking it when I needed it .
    Due to my arthritis getting progressively worse , to the point where I am in tears with the agony.
    Gp 's started me on 75 twice a day and I have to take it every day for the next month to see how I get on , here goes .
    So far its been very good , pains almost gone , but I feel a bit weird , did n't have that when on 50.
    """

data = spark.createDataFrame([[med_ner_prompt]]).toDF("text")
data.show(truncate=100)



## Result

    {
    "drugs": [
    {
    "name": "Arthrotec",
    "reactions": [
    "drowsy",
    "blurred vision",
    "gastric problems"
    ]
    }
    ]
    }
    </s> #### Template:
    {"drugs": [{"name": "", "reaction": []}]}
    #### Text:
    The patient is a 65-year

{%- endcapture -%}

{%- capture model_scala_medical -%}
import com.johnsnowlabs.nlp.base.DocumentAssembler
import com.johnsnowlabs.nlp.annotators.seq2seq.MedicalLLM
import org.apache.spark.ml.Pipeline

import spark.implicits._

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val medicalLLM = MedicalLLM.pretrained("jsl_meds_ner_q4_v2", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("completions")
    .setBatchSize(1)
    .setNPredict(100)
    .setUseChatTemplate(true)
    .setTemperature(0)
//  .setNGpuLayers(100)  if you have GPU

val pipeline = new Pipeline().setStages(
    Array(
        documentAssembler,
        medicalLLM
))

val medPrompt =
    """
    |### Template:
    |{
    |"drugs": [
    |{
    |"name": "",
    |"reactions": []
    |}
    |]
    |}
    |### Text:
    |I feel a bit drowsy & have a little blurred vision , and some gastric problems .
    |I 've been on Arthrotec 50 for over 10 years on and off , only taking it when I needed it .
    |Due to my arthritis getting progressively worse , to the point where I am in tears with the agony.
    |Gp 's started me on 75 twice a day and I have to take it every day for the next month to see how I get on , here goes .
    |So far its been very good , pains almost gone , but I feel a bit weird , did n't have that when on 50.
    |""".stripMargin

val data = Seq(medPrompt).toDF("text")
data.select("completions.result").show(false)


## Result

    {
    "drugs": [
    {
    "name": "Arthrotec",
    "reactions": [
    "drowsy",
    "blurred vision",
    "gastric problems"
    ]
    }
    ]
    }
    </s> #### Template:
    {"drugs": [{"name": "", "reaction": []}]}
    #### Text:
    The patient is a 65-year


{%- endcapture -%}


{%- capture model_api_link -%}
[MedicalLLM](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/seq2seq/medicalLLM.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[MedicalLLM](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/medical_llm/MedicalLLM.html)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[MedicalLLMNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.Loading_Medical_and_Open-Souce_LLMs.ipynb)
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
%}
