---
layout: model
title: Legal Constitutional Judgment Court Decisions Classifier (Turkish)
author: John Snow Labs
name: legclf_constitutional_court_judgment_decisions
date: 2023-05-12
tags: [tr, classification, licensed, legal, tensorflow]
task: Text Classification
language: tr
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

This is a Binary classification model which identifies two constitutional judgment labels(	violation, no_violation) in Turkish-based court decisions.

## Predicted Entities

`violation`, `no_violation`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legclf_constitutional_court_judgment_decisions_tr_1.0.0_3.0_1683922167296.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legclf_constitutional_court_judgment_decisions_tr_1.0.0_3.0_1683922167296.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler() \
    .setInputCol('text') \
    .setOutputCol('document')

tokenizer = nlp.Tokenizer() \
    .setInputCols(['document']) \
    .setOutputCol('token')

sequenceClassifier = legal.BertForSequenceClassification.pretrained("legclf_constitutional_court_judgment_decisions", "tr", "legal/models")\
    .setInputCols(["document", "token"])\
    .setOutputCol("class")

pipeline = nlp.Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequenceClassifier  
])

# couple of simple examples
example = spark.createDataFrame([["başvuru formu ve eklerinde ifade edildiği şekliyle ilgili olaylar özetle şöyledir başvurucu tarihli dilekçe ile piraziz bolu çorum ve şişli asliye ceza mahkemelerinden almış olduğu cezalara ilişkin kararların kesinleşip yerine getirildiğini infaz tarihlerinin üzerinden yıla yakın bir sürenin geçtiğini ileri sürerek memnu hakların iadesi talebinde bulunmuştur bulancak asliye ceza mahkemesi tarihli kararı ile talebi reddetmiştir kararın gerekçesinin ilgili kısmı şöyledir başvuru numarası karar tarihi hükümlünün uyap kayıtlarının incelenmesinden hakkında bulancak asliye ceza mahkemesinde tarihli esas karar sayılı ilamıyla petrol kaçakçılığı suçundan yapılan yargılamada atılı suçu işlediğinin sabit olmaması nedeniyle karar verildiği dosyanın temyiz edilerek yargıtaya gönderildiği ve henüz dönmediği anlaşılmıştır yasaklanmış hakların geri verilmesini düzenleyen sayılı adli sicil maddesi ile sayılı türk ceza kanunu dışındaki kanunların belli bir suçtan dolayı veya belli bir cezaya mahkumiyete bağladığı hak yoksunluklarının giderilebilmesi için yasaklanmış hakların geri verilmesi yoluna gidilebilir bunun için türk ceza kanununun üncü maddesinin beşinci ve altıncı fıkraları saklı kalmak kaydıyla a mahkum olunan cezanın infazının tamamlandığı tarihten itibaren yıllık bir sürenin geçmiş olması b kişinin bu süre zarfında yeni bir suç işlememiş olması ve hayatını iyi halli olarak sürdürdüğü hususunda mahkemede bir kanaat oluşması gerektiği hükmü getirilmiştir yukarıda açıklandığı üzere talep eden hükümlünün yukarıda tarih ve sayıları belirtilen cezaların infaz tarihlerinden sonra yıllık süre içerisinde suç işlenmemiş ise de yıllarda hakkında soruşturma ve kovuşturma yapıldığı bu kapsamda hayatını iyi halli olarak sürdürdüğü hususunda mahkememizde yeterli kanaat oluşmadığından talep yerinde görülmeyerek aşağıdaki şekilde hüküm kurulmuştur başvurucunun anılan karara itirazı giresun ağır ceza mahkemesinin tarihli kararıyla reddedilmiştir kararın gerekçesi şöyledir dosya ve eklerinin incelenmesinden ilgilinin adli sicil kaydının bulunmaması sabıka kaydında geçen kayıtların arşiv kaydı olması sayılı kanunun maddesine göre anayasanın maddesinde belirtilen suçlar için arşiv kaydının silinmesinin mümkün olmama talep sahibinin sabıka kaydında geçen suçların anayasa maddede sayılan suçlardan olması karşısında netice olarak vardığı sonuca göre usul ve yasaya uygun ola bulancak asliye ceza mahkemesinin tarih ve diş sayılı kararına yapılan itirazın reddine karar verilmiştir ret kararı tarihinde başvurucuya tebliğ edilmiştir başvurucu tarihinde bireysel başvuruda bulunmuştur iv hukuk tarihli ve sayılı adli sicil kanununun maddesinin ilgili kısmı şöyledir sayılı türk ceza kanunu dışındaki kanunların belli bir suçtan dolayı veya belli bir cezaya mahkumiyete bağladığı hak yoksunluklarının giderilebilmesi için yasaklanmış hakların geri verilmesi yoluna gidilebilir bunun için türk ceza kanununun üncü maddesinin beşinci ve altıncı fıkraları saklı kalmak kaydıyla a mahkum olunan cezanın infazının tamamlandığı tarihten itibaren üç yıllık bü sürenin geçmiş olması b kişinin bu süre zarfında yeni bir suç işlememiş olması ve hayatını iyi halli olarak sürdürdüğü hususunda mahkemede bir kanaat oluşması gerekir il v "]]).toDF("text")

result = pipeline.fit(example).transform(example)

# result is a DataFrame
result.select("text", "class.result").show(truncate=100)
```

</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+-----------+
|                                                                                                text|     result|
+----------------------------------------------------------------------------------------------------+-----------+
|başvuru formu ve eklerinde ifade edildiği şekliyle ilgili olaylar özetle şöyledir başvurucu tarih...|[violation]|
+----------------------------------------------------------------------------------------------------+-----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legclf_constitutional_court_judgment_decisions|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[class]|
|Language:|tr|
|Size:|628.3 MB|
|Case sensitive:|true|
|Max sentence length:|512|

## Benchmarking

```bash
label         precision  recall  f1-score  support 
no_violation  0.71       0.71    0.71      14      
violation     0.88       0.88    0.88      34      
accuracy      -          -       0.83      48      
macro-avg     0.80       0.80    0.80      48      
weighted-avg  0.83       0.83    0.83      48      
```