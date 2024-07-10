{%- capture title -%}
LLMLoader
{%- endcapture -%}


{%- capture model_description -%}

LLMLoader is designed to interact with a LLMs that are converted into gguf format. This module allows using John Snow Labs' licensed LLMs at
various sizes that are finetuned on medical context for certain tasks. It provides various methods for setting parameters, loading models,
generating text, and retrieving metadata. The LLMLoader includes methods for setting various parameters such as input prefix, suffix,
cache prompt, number of tokens to predict, sampling techniques, temperature, penalties, and more. Overall, the LLMLoader provides a
flexible and extensible framework for interacting with language models in a Python and Scala environment using PySpark and Java.

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
- `penaltyPrompt` :  Override which part of the prompt is penalized for repetition.
  E.g. if original prompt is "Alice: Hello!" and penaltyPrompt is "Hello!", only the latter will be penalized if
  repeated. See <a href="https://github.com/ggerganov/llama.cpp/pull/3727">pull request 3727</a> for more details.
- `penaltyPromptTokens` :  PenaltyPromptTokens
- `ignoreEos` :  Whether to ignore end of stream token and continue generating (implies --logit-bias 2-inf)
- `stopStrings` :  Strings upon seeing which token generation is stopped
- `useChatTemplate` :  Whether or not generate should apply a chat template (default: false)

{%- endcapture -%}



{%- capture model_python_medical -%}

from sparknlp_jsl.llm import LLMLoader

llm_loader_pretrained = LLMLoader(spark).pretrained("llama3_160_gguf", remote_loc="clinical/models")

llm_loader_pretrained.generate("Hey, which is the capital of France?")



## Result

'The capital of France is Paris.'

{%- endcapture -%}

{%- capture model_scala_medical -%}

val llmLoader = new LLMLoader()
  .setSparkSession(spark)
  .pretrained("llama3_160_gguf", remoteLoc="clinical/models", lang = "en")
  .setTemperature(0.0f)
  .setNPredict(20)



val prompt = "Tell me five words about Microsoft."

val output = llmLoader.setUseChatTemplate(false).setStopStrings(Array.empty[String]).generate(prompt)

println(output)

## Result

1. Microsoft: Microsoft is a global technology company that develops, manufactures, and sells


{%- endcapture -%}


{%- capture model_api_link -%}
[LLMLoader](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/ml/gguf/rag/LLMLoader.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[LLMLoader](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/llm/llm_loader/index.html)
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
