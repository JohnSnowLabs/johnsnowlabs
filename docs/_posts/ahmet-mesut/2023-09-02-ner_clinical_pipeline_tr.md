---
layout: model
title: Pipeline to Detect Problem, Test and Treatment (Turkish)
author: John Snow Labs
name: ner_clinical_pipeline
date: 2023-09-02
tags: [licensed, tr, clinical, pipeline, ner]
task: [Named Entity Recognition, Pipeline Healthcare]
language: tr
edition: Healthcare NLP 5.0.2
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [ner_clinical](https://nlp.johnsnowlabs.com/2023/08/29/ner_clinical_tr.html) model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_pipeline_tr_5.0.2_3.4_1693688823112.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_pipeline_tr_5.0.2_3.4_1693688823112.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_clinical_pipeline", "tr", "clinical/models")

result = ner_pipeline.annotate("""50 yaşında bir kadın hasta ortopedi kliniğine sağ dizinde sürekli ağrı, şişlik ve hareket kısıtlılığı şikâyetleriyle başvurdu. Hasta osteoartrit ve daha önce geçirilmiş diz yaralanması öyküsü bildirdi. Klinik muayene ve çekilen röntgenlerde eklem aralığında daralma, osteofit oluşumu ve kıkırdak dejenerasyonu bulguları tespit edildi. Tanıyı doğrulamak ve ciddiyetini değerlendirmek için bir MR taraması istendi. MRG, ileri osteoartrit ile uyumlu yoğun kıkırdak kaybı ve kemik değişiklikleri gösterdi. Hastanın durumu ve tercihleri göz önünde bulundurulduktan sonra  fizik tedavi ve eklem replasmanı ameliyatı olasılığını içeren bir tedavi planı tartışıldı.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_clinical_pipeline", "tr", "clinical/models")

val result = ner_pipeline.annotate("""50 yaşında bir kadın hasta ortopedi kliniğine sağ dizinde sürekli ağrı, şişlik ve hareket kısıtlılığı şikâyetleriyle başvurdu. Hasta osteoartrit ve daha önce geçirilmiş diz yaralanması öyküsü bildirdi. Klinik muayene ve çekilen röntgenlerde eklem aralığında daralma, osteofit oluşumu ve kıkırdak dejenerasyonu bulguları tespit edildi. Tanıyı doğrulamak ve ciddiyetini değerlendirmek için bir MR taraması istendi. MRG, ileri osteoartrit ile uyumlu yoğun kıkırdak kaybı ve kemik değişiklikleri gösterdi. Hastanın durumu ve tercihleri göz önünde bulundurulduktan sonra  fizik tedavi ve eklem replasmanı ameliyatı olasılığını içeren bir tedavi planı tartışıldı.""")

```
</div>

## Results

```bash
|    | chunks                           |   begin |   end | entities   |
|---:|:---------------------------------|--------:|------:|:-----------|
|  0 | sürekli ağrı                     |      58 |    69 | PROBLEM    |
|  1 | şişlik                           |      72 |    77 | PROBLEM    |
|  2 | hareket kısıtlılığı              |      82 |   100 | PROBLEM    |
|  3 | osteoartrit                      |     133 |   143 | PROBLEM    |
|  4 | geçirilmiş diz yaralanması       |     158 |   183 | PROBLEM    |
|  5 | eklem aralığında daralma         |     241 |   264 | PROBLEM    |
|  6 | osteofit oluşumu                 |     267 |   282 | PROBLEM    |
|  7 | kıkırdak dejenerasyonu bulguları |     287 |   318 | PROBLEM    |
|  8 | bir MR taraması                  |     388 |   402 | TEST       |
|  9 | MRG                              |     413 |   415 | TEST       |
| 10 | ileri osteoartrit                |     418 |   434 | PROBLEM    |
| 11 | yoğun kıkırdak kaybı             |     447 |   466 | PROBLEM    |
| 12 | kemik değişiklikleri             |     471 |   490 | PROBLEM    |
| 13 | fizik tedavi                     |     567 |   578 | TREATMENT  |
| 14 | eklem replasmanı ameliyatı       |     583 |   608 | TREATMENT  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_clinical_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.0.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|tr|
|Size:|1.2 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel