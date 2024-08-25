---
layout: model
title: Financial 10K Filings NER
author: John Snow Labs
name: finner_sec_10k_summary
date: 2024-08-25
tags: [finance, ner, annual, reports, 10k, filings, en, licensed]
task: Named Entity Recognition
language: en
edition: Finance NLP 1.0.0
spark_version: 3.0
supported: true
annotator: FinanceNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

IMPORTANT: Don't run this model on the whole financial report. Instead:
- Split by paragraphs;
- Use the `finclf_form_10k_summary_item` Text Classifier to select only these paragraphs;

This Financial NER Model is aimed to process the first summary page of 10K filings and extract the information about the Company submitting the filing, trading data, address / phones, CFN, IRS, etc.

## Predicted Entities

`ADDRESS`, `CFN`, `FISCAL_YEAR`, `IRS`, `PHONE`, `ORG`, `STOCK_EXCHANGE`, `STATE`, `TICKER`, `TITLE_CLASS`, `TITLE_CLASS_VALUE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finner_sec_10k_summary_en_1.0.0_3.0_1724598275571.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finner_sec_10k_summary_en_1.0.0_3.0_1724598275571.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetector() \
    .setInputCols(["document"]) \
    .setOutputCol("sentence") \
    .setCustomBounds(["\n\n"])

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = nlp.WordEmbeddingsModel.pretrained("finance_word_embeddings","en","finance/models")\
	.setInputCols(["sentence","token"])\
	.setOutputCol("embeddings")

ner_model = finance.NerModel.pretrained("finner_10k_summary_fe","en","finance/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")\

ner_converter = nlp.NerConverter()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    sentence_detector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter   
    ])

model = pipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

data = spark.createDataFrame([["""ANNUAL REPORT PURSUANT TO SECTION 13 OR 15(d) OF THE SECURITIES AND EXCHANGE ACT OF 1934
For the annual period ended January 31, 2021
or
TRANSITION REPORT PURSUANT TO SECTION 13 OR 15(d) OF THE SECURITIES EXCHANGE ACT OF 1934
For the transition period from________to_______
Commission File Number: 001-38856
PAGERDUTY, INC.
(Exact name of registrant as specified in its charter)
Delaware
27-2793871
(State or other jurisdiction of
incorporation or organization)
(I.R.S. Employer
Identification Number)
600 Townsend St., Suite 200, San Francisco, CA 94103
(844) 800-3889
(Address, including zip code, and telephone number, including area code, of registrant’s principal executive offices)
Securities registered pursuant to Section 12(b) of the Act:
Title of each class
Trading symbol(s)
Name of each exchange on which registered
Common Stock, $0.000005 par value,
PD
New York Stock Exchange"""]]).toDF("text")

result = model.transform(data)

```

</div>

## Results

```bash
+----------------------------------------------+-----------------+
|ticker                                        |label            |
+----------------------------------------------+-----------------+
|January 31, 2021                              |FISCAL_YEAR      |
|001-38856                                     |CFN              |
|PAGERDUTY, INC                                |ORG              |
|Delaware                                      |STATE            |
|27-2793871                                    |IRS              |
|600 Townsend St., Suite 200, San Francisco, CA|ADDRESS          |
|(844) 800-3889                                |PHONE            |
|Common Stock                                  |TITLE_CLASS      |
|$0.000005                                     |TITLE_CLASS_VALUE|
|PD                                            |TICKER           |
|New York Stock Exchange                       |STOCK_EXCHANGE   |
+----------------------------------------------+-----------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finner_sec_10k_summary|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.8 MB|

## References

Manual annotations on 10-K Filings

## Benchmarking

```bash
label	 tp	 fp	 fn	 prec	 rec	 f1
B-TITLE_CLASS	 16	 0	 1	 1.0	 0.9411765	 0.969697
I-ORG	 62	 16	 17	 0.7948718	 0.7848101	 0.789809
B-STOCK_EXCHANGE	 13	 0	 1	 1.0	 0.9285714	 0.9629629
B-PHONE	 15	 0	 1	 1.0	 0.9375	 0.9677419
B-STATE	 10	 0	 1	 1.0	 0.90909094	 0.95238096
B-IRS	 11	 1	 0	 0.9166667	 1.0	 0.95652175
I-PHONE	 46	 1	 0	 0.9787234	 1.0	 0.9892473
I-TITLE_CLASS	 22	 0	 1	 1.0	 0.95652175	 0.9777778
B-CFN	 15	 0	 1	 1.0	 0.9375	 0.9677419
B-ADDRESS	 12	 0	 2	 1.0	 0.85714287	 0.9230769
I-ADDRESS	 118	 5	 1	 0.9593496	 0.99159664	 0.9752066
I-STOCK_EXCHANGE	 45	 0	 3	 1.0	 0.9375	 0.9677419
B-TICKER	 13	 0	 1	 1.0	 0.9285714	 0.9629629
I-FISCAL_YEAR	 131	 3	 45	 0.97761196	 0.7443182	 0.84516126
B-TITLE_CLASS_VALUE	 16	 0	 0	 1.0	 1.0	 1.0
B-ORG	 55	 20	 9	 0.73333335	 0.859375	 0.79136693
B-FISCAL_YEAR	 51	 1	 17	 0.9807692	 0.75	 0.85

Macro-average	 prec: 0.9612545, rec: 0.90962785, f1: 0.9347289
Micro-average	 prec: 0.93266475, rec: 0.8656915, f1: 0.897931
```