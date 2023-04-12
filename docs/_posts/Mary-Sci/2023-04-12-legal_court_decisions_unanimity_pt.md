---
layout: model
title: Legal Court Decisions Unanimity Prediction (Portuguese)
author: John Snow Labs
name: legal_court_decisions_unanimity
date: 2023-04-12
tags: [pt, legal, classification, licensed, tensorflow]
task: Text Classification
language: pt
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: RoBertaForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a Multiclass classification model which identifies the court decisions were unanimity, not_unanimity, or  not_determined in the State Supreme Court.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legal_court_decisions_unanimity_pt_1.0.0_3.0_1681308453103.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legal_court_decisions_unanimity_pt_1.0.0_3.0_1681308453103.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

seq_classifier = legal.BertForSequenceClassification.pretrained("legal_court_decisions_unanimity", "pt", "legal/models") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("class")

nlpPipeline= nlp.Pipeline(stages=[
    document_assembler, 
    tokenizer,
    seq_classifier 
])


# Example text
example = spark.createDataFrame([["ACÓRDÃO/SALVO-CONDUTO PENAL E PROCESSUAL PENAL HABEAS CORPUS. CRIMES CONTRA A HONRA. ALEGAÇÃO DE INCOMPETÊNCIA DO JUÍZO, MANIPULAÇÃO DAS PROVAS NA AÇÃO ORIGINÁRIA E DEFEITO DE REPRESENTAÇÃO. PRELIMINARES AFASTADAS. IMPOSIÇÃO DE MEDIDAS CAUTELARES DIVERSAS DE PRISÃO. NECESSIDADE DE DEMONSTRAÇÃO DA ADEQUAÇÃO E PROPORCIONALIDADE DAS MEDIDAS. PRECEDENTES DO STJ. DECISÃO DESPROVIDA DE FUNDAMENTAÇÃO. MERA REFERÊNCIA À GRAVIDADE DOS FATOS NARRADOS. NULIDADE. INTELIGÊNCIA DO ARTIGO 93, IX, DA CRFB. CONSTRANGIMENTO ILEGAL EVIDENCIADO. ORDEM CONCEDIDA. 1 Observando que as penas máximas cominadas aos crimes imputados aos querelantes, em concurso material, excedem a dois anos, não há que se falar em competência dos Juizados Especiais Criminais. 2 Na estreita via do mandamus, não se faz possível avaliar eventual manipulação de provas procedida pela vítima nos autos originários. 3 Embora menos gravosas que a segregação cautelar, as medidas cautelares possuem o condão de restringir direitos individuais, razão pela qual não dispensam fundamentação acerca da sua necessidade e adequação. 4 Estando a decisão atacada totalmente desprovida de fundamentação, forçoso declarar a sua nulidade, revogando as medidas cautelares impostas."]]).toDF("text")

empty_data = spark.createDataFrame([[""]]).toDF("text")
model = nlpPipeline.fit(empty_data)

result = model.transform(example)

# result is a DataFrame
result.select("text", "class.result").show(truncate=200)
```

</div>

## Results

```bash
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+
|                                                                                                                                                                                                    text|          result|
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+
|ACÓRDÃO/SALVO-CONDUTO PENAL E PROCESSUAL PENAL HABEAS CORPUS. CRIMES CONTRA A HONRA. ALEGAÇÃO DE INCOMPETÊNCIA DO JUÍZO, MANIPULAÇÃO DAS PROVAS NA AÇÃO ORIGINÁRIA E DEFEITO DE REPRESENTAÇÃO. PRELIM...|[not_determined]|
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legal_court_decisions_unanimity|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[class]|
|Language:|pt|
|Size:|309.1 MB|
|Case sensitive:|true|
|Max sentence length:|512|

## Benchmarking

```bash
label           precision  recall  f1-score  support 
not_determined  0.76       0.80    0.78      116     
not_unanimity   0.95       0.78    0.86      23      
unanimity       0.73       0.71    0.72      90      
accuracy        -          -       0.76      229     
macro-avg       0.81       0.77    0.79      229     
weighted-avg    0.77       0.76    0.76      229     
```