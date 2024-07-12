---
layout: model
title: Legal Text Generation (MPRE)
author: John Snow Labs
name: leggen_flant5_mpre
date: 2023-09-04
tags: [legal, text_generation, mpre, en, licensed, tensorflow]
task: Text Generation
language: en
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MedicalTextGenerator
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This Text generation model has been fine-tuned on FLANT5 using legal MPRE data. MPRE stands for Multistate Professional Responsibility Examination. The dataset contains examples of questions from past MPRE exams along with their answers and explanations. This model provides a powerful and efficient solution for accurately generating answers and delivering insightful information.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/leggen_flant5_mpre_en_1.0.0_3.0_1693847631770.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/leggen_flant5_mpre_en_1.0.0_3.0_1693847631770.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.MultiDocumentAssembler()\
    .setInputCols("question", "context")\
    .setOutputCols("document_question", "document_context")

leg_gen = legal.TextGenerator.pretrained('leggen_flant5_mpre,'en','legal/models')\
    .setInputCols(["question"])\
    .setOutputCol("generated_text")\
    .setMaxNewTokens(150)\
    .setStopAtEos(True)

pipeline = nlp.Pipeline(stages=[document_assembler, leg_gen])

data = spark.createDataFrame([
   [1, """question:
Conglomerate Corporation owns a little more than half the stock of Giant Company. Conglomerate’s stock, in turn, is public, available on the public stock exchange, as is the remainder of the stock in Giant Company. The president of Conglomerate Corporation has asked Attorney Stevenson to represent Giant Company in a deal by which Giant would make a proposed transfer of certain real property to Conglomerate Corporation. The property in question is unusual because it contains an underground particle collider used for scientific research, but also valuable farmland on the surface, as well as some valuable mineral rights in another part of the parcel. These factors make the property value difficult to assess by reference to the general real-estate market, which means it is difficult for anyone to determine the fairness of the transfer price in the proposed deal. Would it be proper for Attorney Stevenson to facilitate this property transfer at the behest of the president of Conglomerate, if Attorney Stevenson would be representing Giant as the client in this specific matter? Yes, because Conglomerate Corporation owns more than half of Giant Company, so the two corporate entities are one client for purposes of the rules regarding conflicts of interest. Yes, because the virtual impossibility of obtaining an appraisal of the fair market value of the property means that the lawyer does not have actual knowledge that the deal is unfair to either party. No, because the attorney would be unable to inform either client fully about whether the proposed transfer price would be in their best interest. No, not unless the attorney first obtains effective informed consent of the management of Giant Company, as well as that of Conglomerate, because the ownership of Conglomerate and Giant is not identical, and their interests materially differ in the proposed transaction."""]]).toDF('id', 'text')

results = pipeline.fit(data).transform(data)

results.select("generated.result").show(truncate=False)
```

</div>

## Results

```bash
+-----------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------+
|[Not if the attorney first obtainses efficient informed consent of the administration of Giants, as well and of Conglomerate]|
+-----------------------------------------------------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|leggen_flant5_mpre|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.6 GB|

## References

In house annotated dataset