---
layout: model
title: Pretrained Pipeline for Reading in Mixed Scanned and Digital PDF Documents
author: John Snow Labs
name: mixed_scanned_digital_pdf
date: 2023-11-06
tags: [en, licensed, ocr]
task: OCR Text Detection
language: en
nav_key: models
edition: Visual NLP 5.0.2
spark_version: 3.2.1
supported: true
recommended: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained pipeline for conducting Optical Character Recognition (OCR) on mixed scanned and digital PDF documents. It ensures precise and efficient text extraction from PDFs of various origins and formats, improving the overall OCR accuracy.

## Predicted Entities

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/ocr/PP_MIXED_SCANNED_DIGITAL_PDF/){:.button.button-orange.button-orange-trans.co.button-icon}
[Open in Colab](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/jupyter/Cards/SparkOcrPretrainedPipelinesMixedScannedDigitalPdf.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
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
"ROMINVENT\n\nINDUSTRIAL PROPERTY AGENCY - ESTABLISHED IN 1953\n\nRebecca Gritschke\n\nDate: 26-Nov-2021\n\nMERCK KGaA\n\nYour ref.: TM24134RO00\n\nGroup Legal & Compliance/Trademarks\n\nLE-TA\n\nOur ref.: 214766 / C/2-21243/SI/SI\n\nFrankfurter Str. 250\n\nClient ID: 1119\n\nD-64293 Darmstadt\n\nGERMANY\n\nVAT No: DE 811850788\n\nFax: +49 6151 72 3378\n\nE-mail: rebecca.gritschke@merckgroup.com\n\nRe\n\nRenewal application for CONCOR AM, reg. no. 118032 in class 5 in Romania.\n\nOwner: MERCK KGaA;\n\nINVOICE NO. M210695\n\nNo.\n\nDescription\n\nOfficial fees\n\nOur services\n\nEUR\n\ncharges\n\nEUR\n\nApplication for renewal of an individual trademark\n\n1\n\nTrademark renewal\n\n1 class black & white\n\nIncrease of 50% (grace period), 1 class black & white\n\n180\n\n180\n\nReporting of Renewal Certificate\n\nIssuing of Renewal Certificate\n\n50\n\n50\n\nSubtotal\n\n230\n\n230\n\nTotal\n\nEUR 460.00\n\n* Official and Rominvent's fees are in EURO; as such, the conversion from EURO to USD will generate amounts with decimal places.\n\nPayment deadline: within 30 days from issue. Currency: 1 EUR = 4.9490 RON. published on 2021-11-25\n\nVAT in accordance with Art 133(2) of the Romanian Law 571/2003. . VIES consultation number: WAPIAAAAX1 bnp!ICx\n\nThe supply is subject to the reverse charge procedure according Art 44, 196 of the Council Directive 2006/112/EC.\n\nIMPORTANT * When arranging the wire transfer, please make sure that the bank charges are debited to your account.\n\n* Please always refer to our Invoice no. in your Payment Order. (Please also send a remittance advice with all payments)\n\nBank name: BRD-GSG, MCC Branch. SWIFT: BRDEROBU\n\nBank name: BCR, Lipscani Branch. SWIFT: RNCBROBU\n\nAddress:1-7 lon Mihalache Blvd, Sector 1, Bucharest, 011171, RO\n\nAddress:5 Regina Elisabeta Blvd, Sector 3, Bucharest, RO\n\nIBAN Account No EUR:RO39BRDE450SV00768494500\n\nIBAN Account No EUR:RO69RNCB0090000505820005\n\nIBAN Account No USD:RO12BRDE450SV008 19474500\n\nIBAN Account No USD:RO53RNCB0090000505820002\n\nAddress: ROMINVENT S.A., 35, Ermil Pangratti Str., 1st Floor, Sector 1, Bucharest 011882, ROMANIA\n\nPhone: +4021-231 2515/-231 2353 Fax: +4021-231 2550/-231 2454 E-mail: office@rominvent.ro Internet: www.rominvent.ro\n\nTrade Register No.: J40/13380/1993 VAT: RO4140325 Assets: 330.000 Lei\n"
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
