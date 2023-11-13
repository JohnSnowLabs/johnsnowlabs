---
layout: model
title: Pretrained Pipeline for Reading and Skewing Correction in Mixed Scanned and Digital PDF Documents
author: John Snow Labs
name: mixed_scanned_digital_pdf_skew_correction
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

Pretrained pipeline designed to correct skew in input printed documents, enhancing OCR readability for more accurate text extraction.

## Predicted Entities

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/ocr/PP_MIXED_SCANNED_DIGITAL_PDF_SKEW_CORRECTION/){:.button.button-orange.button-orange-trans.co.button-icon}
[Open in Colab](https://github.com/JohnSnowLabs/spark-ocr-workshop/blob/master/tutorials/SparkOcrPretrainedPipelinesMixedScannedDigitalPdfSkewCorrection.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/mixed_scanned_digital_pdf_skew_correction_en_4.3.4_3.0_1679597686000.zip){:.button.button-orange.button-orange-trans.arr.button-icon}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
pdf_pipeline = PretrainedPipeline('mixed_scanned_digital_pdf_skew_correction', 'en', 'clinical/ocr')

pdf_path = '/content/pdfs/'
pdf_example_df = spark.read.format("binaryFile").load(pdf_path).cache()

result = pdf_pipeline.transform(pdf_example_df)
```
```scala
val pdf_pipeline = new PretrainedPipeline("mixed_scanned_digital_pdf_skew_correction", "en", "clinical/ocr")

val pdf_path = "/content/pdfs/"
val pdf_example_df = spark.read.format("binaryFile").load(pdf_path).cache()

val result = pdf_pipeline.transform(pdf_example_df)
```
</div>

## Example

### Input
![Screenshot](/assets/images/examples_ocr/pp_skew.jpg)

### Output
![Screenshot](/assets/images/examples_ocr/pp_skew_out.jpg)
```bash
"PEMBERITAHUAN PERTANYAAN DEWAN RAKYAT\n\nPERTANYAAN\n\nBUKAN JAWAB LISAN\n\nDARIPADA\n\nTUAN BUDIMAN BIN MOHD. ZOHDI\n\nSOALAN\n\nNO. 3\n\nTuan Budiman bin Moh\n\nTI\n\nd. Zohdi [ Sun\n\nbidang\n\nlah terkini pelaj\n\nar kolej komuniti di seluruh\n\ngai Besar ] minta MENTERI PENDIDIKAN\n\ndan kursus serta a\n\nPakah tahap\n\nut\n\nkebolehpasaran lepasan kolej k\n\nomuniti ini\n\nJAWAPAN\n\nTuan Yang di-Pertua,\n\nUntuk makluman Ahli Yang Berhormat\n\nSeluruh negara sehingga 16 Ogos 2016\n\njJumlah terkini pelajar aktif Kolej Komuniti di\n\nadalah se\n\nfamai 19,933 orang yang mengikut\n\nPengajian di peringkat meliputi kursus dip\n\nloma dan sijil.\n\nBerdasarkan Kajian\n\nPengesanan Graduan tahun 2015 iaitu soal\n\nSelidik yang dijalankan ke atas graduan\n\nsemasa musim konvokesyen dapatan me\n\ngraduan Kolej Komuniti adalah 97.4%.\n\nnunjukkan kadar kebolehpasaran bagi\n"
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|mixed_scanned_digital_pdf_skew_correction|
|Type:|ocr|
|Compatibility:|Visual NLP 5.0.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
