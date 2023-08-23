---
layout: model
title: Legal Finetuned FLAN-T5 Summarization 
author: John Snow Labs
name: legsum_flant5_legal_augmented
date: 2023-04-14
tags: [en, licensed, summarization, legal, agreements, tensorflow]
task: Summarization
language: en
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: LegalSummarizer
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This language model has been fine-tuned on the FLANT5 using Legal Information. FLAN-T5 is a state-of-the-art language model developed by Facebook AI that utilizes the T5 architecture for text summarization tasks.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legsum_flant5_legal_augmented_en_1.0.0_3.0_1681502326217.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legsum_flant5_legal_augmented_en_1.0.0_3.0_1681502326217.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("documents")

flant5 = legal.Summarizer().pretrained('legsum_flant5_legal_augmented','en','legal/models')\
    .setInputCols(["documents"])\
    .setOutputCol("summary")\
    .setMaxNewTokens(1000)

pipeline = nlp.Pipeline(stages=[document_assembler, flant5])

data = spark.createDataFrame([
  [1, """ 
3.1           Organization and Authorization. ONTARIO is a corporation duly organized and validly existing and in good standing under the laws of the Ontario. ONTARIO has the full power and authority to enter into this Agreement and to consummate the transactions contemplated under this Agreement. The making and performance of this Agreement and the agreements and other instruments required to be executed by ONTARIO have been, or at the Closing will have been, duly authorized by all necessary corporate actions and will be duly executed by a person authorized by ONTARIO to do so. ONTARIO shall deliver to FOX duly approved and executed resolutions of the directors and shareholders approving ONTARIO’s execution and delivery of this Agreement and the performance of its obligations under this Agreement.
 
3.2           No Breach of Laws or Contracts. The consummation by ONTARIO of the transactions contemplated by this Agreement will not result in the breach of any term or provision of, or constitute a default under any applicable law or regulation, its articles of organization or operating agreement, or under any other agreement or instrument to which ONTARIO is a party, by which it is bound, or which affects the Assets.  
3.3           Binding Obligations. When executed and delivered, this Agreement and all instruments executed and delivered by ONTARIO pursuant to this Agreement will constitute legal and binding obligations of ONTARIO and will be valid and enforceable in accordance with their respective terms.  
3.4           Compliance with Laws. ONTARIO has not received notice from any governmental agency, of any physical or environmental condition existing on the Land or any access to the Land or created by ONTARIO or of any action or failure to act by ONTARIO which is a material violation of any applicable law, regulation or ordinance. To ONTARIO’s knowledge, there are currently no off-site improvement requirements that any governmental authority has imposed or threatened to impose on the Land.  
3.5           No Litigation. There is no suit, action, arbitration or legal, administrative or other proceeding or governmental investigation pending or, to the knowledge of ONTARIO without inquiry, threatened against, or affecting the Assets or the ability of ONTARIO to perform its covenants and obligations under this Agreement.  
3.6.1 Title to the Land. ONTARIO represents and warrants that ONTARIO’s title to the Assets is good and marketable and on the Closing shall be free and clear of any lien, claim or encumbrance, except the following (the “Permitted Exceptions”):  
(a)           Liens for taxes and mortgages acknowledged by FOX on the Assets not yet due and payable or which are being contested in good faith;  
(b)           Any items listed in the Title Commitment or any amendment or update to the Title Commitment to which FOX does not timely deliver to ONTARIO a Notice of Objection pursuant to Section 3.9.5.  
3.6.2           Encroachments. To ONTARIOS’s knowledge, the improvements on the Land lie entirely within the boundaries of the Land and no structure of any kind encroaches on or over the Land."""]]).toDF('id', 'text')

results = pipeline.fit(data).transform(data)

results.select("summary.result").show(truncate=False)
```

</div>

## Results

```bash
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[Ontario is a corporation that is duly organized and validly existing and in good standing under the laws of the Ontario. It has the full power and authority to enter into this Agreement and to consummate the transactions contemplated under this Agreement. The consummation of this Agreement will not result in the breach of any term or provision of, or constitute a default under any applicable law or regulation, its articles of organization or operating agreement, or under any other agreement or instrument to which Ontario is a party, by which it is bound, or which affects the Assets. This Agreement and all instruments executed and delivered by Ontario pursuant to this Agreement will constitute legal and binding obligations of Ontario and will be valid and enforceable in accordance with their respective terms. There is no suit, action, arbitration or legal, administrative or other proceeding or governmental investigation pending or, to the knowledge of Ontario, threatened against, or affecting the Assets or the ability of Ontario to perform its covenants and obligations under this Agreement. Ontario's title to the Assets is good and marketable and on the Closing shall be free and clear of any lien, claim or encumbrance, except the permitted exceptions.]|
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legsum_flant5_legal_augmented|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.6 GB|

## References

In house annotated dataset
