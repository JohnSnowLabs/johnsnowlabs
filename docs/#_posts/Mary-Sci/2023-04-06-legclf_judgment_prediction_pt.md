---
layout: model
title: Legal Court Judgment Prediction (Portuguese)
author: John Snow Labs
name: legclf_judgment_prediction
date: 2023-04-06
tags: [pt, licensed, legal, classification, tensorflow]
task: Text Classification
language: pt
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: LegalBertForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a Multiclass classification model which identifies the court decisions in the State Supreme Court, including the following classes;
		- no: The appeal was denied
		- partial: For partially favourable decisions
		- yes: For fully favourable decisions

## Predicted Entities

`no`, `partial`, `yes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legclf_judgment_prediction_pt_1.0.0_3.0_1680778981035.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legclf_judgment_prediction_pt_1.0.0_3.0_1680778981035.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler= nlp.DocumentAssembler() \
    .setInputCols(["text"]) \
    .setOutputCols("document")

tokenizer = nlp.Tokenizer() \
    .setInputCols("document") \
    .setOutputCol("token")

seq_classifier = legal.BertForSequenceClassification.pretrained("legclf_judgment_prediction", "pt", "legal/models") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("class")

pipeline = nlp.Pipeline(stages=[
    document_assembler, 
    tokenizer ,
    seq_classifier 
])

# simple examples
example = spark.createDataFrame([["PENAL. PROCESSO PENAL. APELAÇÃO. HOMICÍDIO QUALIFICADO. ARGUIÇÃO DE NULIDADE EM DECORRÊNCIA DA INSCONSTITUCIONALIDADE DO ARTIGO 457 DO CÓDIGO DE PROCESSO PENAL. AFASTADA. PLEITO DE REDIMENSIONAMENTO DA PENA. DOSIMETRIA QUE MERECE RETOQUES. AFASTADA A VALORAÇÃO DESFAVORÁVEL DAS CIRCUNSTÂNCIAS JUDICIAIS DOS ANTECEDENTES E DA PERSONALIDADE DO AGENTE. MANTIDA A CULPABILIDADE, CIRCUNSTÂNCIAS DO DELITO E CONSEQUÊNCIAS DO CRIME. APELO CONHECIDO E PARCIALMENTE PROVIDO. 1 Não há falar em ocorrência de nulidade não caso concreto, não existindo qualquer inconstitucionalidade em virtude do texto legal do ARTIGO 457 do Código de Processo Penal, não tendo ocorrido o adiamento da sessão do júri em virtude da ausência do acusado, conforme alegado. Pelo contrário, este foi devidamente intimado por edital e, mesmo assim, restou ausente. 2 A justificativa apresentada pelo magistrado singular acerca da culpabilidade considerou a alta reprovabilidade da conduta do réu, em virtude da premeditação e frieza na prática delitiva, considerando que o acusado foi até a casa da vítima com o intuito de ceifar a sua vida, experimentando assim a consequência da transgressão, estando acertada a valoração negativa desta circunstância judicial."]]).toDF("text")

result = pipeline.fit(example).transform(example)

# result is a DataFrame
result.select("text", "class.result").show(truncate=100)
```

</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+---------+
|                                                                                                text|   result|
+----------------------------------------------------------------------------------------------------+---------+
|PENAL. PROCESSO PENAL. APELAÇÃO. HOMICÍDIO QUALIFICADO. ARGUIÇÃO DE NULIDADE EM DECORRÊNCIA DA IN...|[partial]|
+----------------------------------------------------------------------------------------------------+---------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legclf_judgment_prediction|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[class]|
|Language:|pt|
|Size:|408.7 MB|
|Case sensitive:|true|
|Max sentence length:|512|

## Benchmarking

```bash
label         precision  recall  f1-score  support 
no            0.76       0.77    0.76      86      
partial       0.79       0.71    0.75      75      
yes           0.71       0.78    0.74      76      
accuracy      -          -       0.75      237     
macro-avg     0.75       0.75    0.75      237     
weighted-avg  0.75       0.75    0.75      237  
```