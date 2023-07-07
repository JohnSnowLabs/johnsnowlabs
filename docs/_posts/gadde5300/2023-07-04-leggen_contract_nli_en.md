---
layout: model
title: Legal Contract NLI
author: John Snow Labs
name: leggen_contract_nli
date: 2023-07-04
tags: [legal, en, text_generation, contract_nli, licensed, tensorflow]
task: Text Generation
language: en
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: LegalTextGenerator
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a text-to-text generation model (encode-decoder architecture) that has undergone fine-tuning on flan-t5 using the Contract-NLI dataset. The ContractNLI dataset is designed for document-level natural language inference (NLI) on contracts, aiming to streamline and expedite the contract review process. The objective of this task is to provide a system with a set of hypotheses, like "Some obligations of Agreement may survive termination," along with a contract, and task it with classifying whether each hypothesis is entailed, contradicted, or not mentioned (neutral) by the contract.

## Predicted Entities

`Contradiction`, `Entailment`, `Neutral`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/leggen_contract_nli_en_1.0.0_3.0_1688441488610.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/leggen_contract_nli_en_1.0.0_3.0_1688441488610.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

flant5 = legal.TextGenerator.pretrained('leggen_contract_nli','en','legal/models')\
    .setInputCols(["document"])\
    .setMaxNewTokens(256)\
    .setStopAtEos(True)\
    .setOutputCol("generated")

pipeline = nlp.Pipeline(stages=[document_assembler, flant5])

data = spark.createDataFrame([
   [1, '''mnli hypothesis:
Receiving Party shall not use any Confidential Information for any purpose other than the purposes stated in Agreement.
premise:
(a) furnish only that portion of the Proprietary Information which in its reasonable opinion, based upon advice of counsel, it is legally compelled to disclose, and (b) at the other Party's cost, cooperate with the efforts of the Party to obtain order or other reliable assurance that confidential treat will he accorded to such portion of the Proprietary Information as may be disclosed.
''']]).toDF('id', 'text')

results = pipeline.fit(data).transform(data)

results.select("generated.result").show(truncate=False)
```

</div>

## Results

```bash
+---------+
|result   |
+---------+
|[Neutral]|
+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|leggen_contract_nli|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.6 GB|

## References

This model has been fine tuned using [Stanford ContractNLI](https://stanfordnlp.github.io/contract-nli/) dataset.

Reference:
```bibtex
@inproceedings{koreeda-manning-2021-contractnli-dataset,
    title = "{C}ontract{NLI}: A Dataset for Document-level Natural Language Inference for Contracts",
    author = "Koreeda, Yuta  and Manning, Christopher",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2021",
    month = nov,
    year = "2021",
    address = "Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-emnlp.164",
    pages = "1907--1919",
}

```
