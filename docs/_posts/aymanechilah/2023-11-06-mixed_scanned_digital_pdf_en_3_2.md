---
layout: model
title: Pretrained Pipeline for Reading in Mixed Scanned and Digital PDF Documents
author: John Snow Labs
name: mixed_scanned_digital_pdf
date: 2023-11-06
tags: [en, licensed]
task: OCR Text Detection
language: en
nav_key: models
edition: Visual NLP 5.0.2
spark_version: 3.2.1
supported: true
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained pipeline for conducting Optical Character Recognition (OCR) on mixed scanned and digital PDF documents. It ensures precise and efficient text extraction from PDFs of various origins and formats, improving the overall OCR accuracy.

## Predicted Entities

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/ocr/PP_MIXED_SCANNED_DIGITAL_PDF/){:.button.button-orange.button-orange-trans.co.button-icon}
[Open in Colab](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/tutorials/SparkOcrPretrainedPipelinesMixedScannedDigitalPdf.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/mixed_scanned_digital_pdf_en_4.3.4_3.0_1679597686000.zip){:.button.button-orange.button-orange-trans.arr.button-icon}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
pdf_pipeline = PretrainedPipeline('mixed_scanned_digital_pdf', 'en', 'clinical/ocr')

pdf_path = '/content/pdfs/'
pdf_example_df = spark.read.format("binaryFile").load(pdf_path).cache()

result = pdf_pipeline.transform(pdf_example_df)
```
```scala
val pdf_pipeline = new PretrainedPipeline("mixed_scanned_digital_pdf", "en", "clinical/ocr")

val pdf_path = "/content/pdfs/"
val pdf_example_df = spark.read.format("binaryFile").load(pdf_path).cache()

val result = pdf_pipeline.transform(pdf_example_df)
```
</div>

## Example

### Input
![Screenshot](/assets/images/examples_ocr/pp_printed.jpg)

### Output
```bash
ROMINVENT

INDUSTRIAL PROPERTY AGENCY - ESTABLISHED IN 1953

Rebecca Gritschke

Date: 26-Nov-2021

MERCK KGaA

Your ref.: TM24134RO00

Group Legal & Compliance/Trademarks

LE-TA

Our ref.: 214766 / C/2-21243/SI/SI

Frankfurter Str. 250

Client ID: 1119

D-64293 Darmstadt

GERMANY

VAT No: DE 811850788

Fax: +49 6151 72 3378

E-mail: rebecca.gritschke@merckgroup.com

Re

Renewal application for CONCOR AM, reg. no. 118032 in class 5 in Romania.

Owner: MERCK KGaA;

INVOICE NO. M210695

No.

Description

Official fees

Our services

EUR

charges

EUR

Application for renewal of an individual trademark

1

Trademark renewal

1 class black & white

Increase of 50% (grace period), 1 class black & white

180

180

Reporting of Renewal Certificate

Issuing of Renewal Certificate

50

50

Subtotal

230

230

Total

EUR 460.00

* Official and Rominvent's fees are in EURO; as such, the conversion from EURO to USD will generate amounts with decimal places.

Payment deadline: within 30 days from issue. Currency: 1 EUR = 4.9490 RON. published on 2021-11-25

VAT in accordance with Art 133(2) of the Romanian Law 571/2003. . VIES consultation number: WAPIAAAAX1 bnp!ICx

The supply is subject to the reverse charge procedure according Art 44, 196 of the Council Directive 2006/112/EC.

IMPORTANT * When arranging the wire transfer, please make sure that the bank charges are debited to your account.

* Please always refer to our Invoice no. in your Payment Order. (Please also send a remittance advice with all payments)

Bank name: BRD-GSG, MCC Branch. SWIFT: BRDEROBU

Bank name: BCR, Lipscani Branch. SWIFT: RNCBROBU

Address:1-7 lon Mihalache Blvd, Sector 1, Bucharest, 011171, RO

Address:5 Regina Elisabeta Blvd, Sector 3, Bucharest, RO

IBAN Account No EUR:RO39BRDE450SV00768494500

IBAN Account No EUR:RO69RNCB0090000505820005

IBAN Account No USD:RO12BRDE450SV008 19474500

IBAN Account No USD:RO53RNCB0090000505820002

Address: ROMINVENT S.A., 35, Ermil Pangratti Str., 1st Floor, Sector 1, Bucharest 011882, ROMANIA

Phone: +4021-231 2515/-231 2353 Fax: +4021-231 2550/-231 2454 E-mail: office@rominvent.ro Internet: www.rominvent.ro

Trade Register No.: J40/13380/1993 VAT: RO4140325 Assets: 330.000 Lei
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|mixed_scanned_digital_pdf|
|Type:|ocr|
|Compatibility:|Visual NLP 5.0.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
