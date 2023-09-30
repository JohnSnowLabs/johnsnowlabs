---
layout: model
title: dsadsad
author: John Snow Labs
name: assertion_manualassertion541
date: 2023-09-30
tags: [en, licensed]
task: Assertion Status
language: en
edition: Spark NLP 5.0.2
spark_version: 3.2
supported: true
annotator: AssertionDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

dsadas

## Predicted Entities

`Someoneelse`, `ManualFix`, `SomeoneElse`, `Family`, `Hypothetical`, `Possible`, `Past`, `Planned`, `Absent`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/models-hub-auxdata/clinical/models/assertion_manualassertion541_en_5.0.2_3.2_1696088565199.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://models-hub-auxdata/clinical/models/assertion_manualassertion541_en_5.0.2_3.2_1696088565199.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()
            .setInputCol("text")
            .setOutputCol("document")
            
sentence_detector = SentenceDetector()
                .setInputCols(["document"])
                .setOutputCol("sentence")
                .setCustomBounds([""])
            
tokenizer = Tokenizer() 
            .setInputCols(["sentence"]) 
            .setOutputCol("token")
            .setSplitChars(['-'])
            
word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")
            .setInputCols(["sentence", "token"]) 
            .setOutputCol("embeddings")   
        
ner = MedicalNerModel.pretrained("Medical_Device", "en","clinical/models") 
            .setInputCols(["sentence", "token", "embeddings"]) 
            .setOutputCol("ner")
        
ner_converter = NerConverter() 
            .setInputCols(["sentence", "token", "ner"]) 
            .setOutputCol("ner_chunk")

assertion = AssertionDLModel.pretrained("assertion_2023-09-30-15-06-46_manualassertion541", "en", "clinical/models")
            .setInputCols(["sentence", "ner_chunk", "embeddings"])
            .setOutputCol("assertion")
        
pipeline = Pipeline(stages=[document_assembler,
                            sentence_detector,
                            tokenizer,
                            word_embeddings,
                            ner,
                            ner_converter,
                            assertion])
        
data = spark.createDataFrame([["SAMPLE TEXT"]]).toDF("text")
        
result = pipeline.fit(data).transform(data)
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|assertion_manualassertion541|
|Compatibility:|Spark NLP 5.0.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, chunk, embeddings]|
|Output Labels:|[assertion]|
|Language:|en|
|Size:|1.9 MB|
|Dependencies:|embeddings_clinical|