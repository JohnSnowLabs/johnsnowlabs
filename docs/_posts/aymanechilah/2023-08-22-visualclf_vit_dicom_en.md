---
layout: model
title: Dicom Image Classification
author: John Snow Labs
name: visualclf_vit_dicom
date: 2023-08-22
tags: [classification, dicom, licensed, en, ocr, tensorflow]
task: Image Classification
language: en
edition: Healthcare NLP 5.0.1
spark_version: 3.2
supported: true
engine: tensorflow
annotator: ViTForImageClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is based on a Visual Transformer (ViT) architecture, specifically designed to perform classification tasks on DICOM images. Trained in-house with a diverse range of corpora, including DICOM data, COCO images, and in-house annotated documents, the model is capable of accurately classifying medical images and associated document notes.

By leveraging the power of Visual Transformers, the model captures complex relationships between image content and textual information, making it highly effective for analyzing both visual features and document annotations. Once images are classified, you can further integrate Visual NLP techniques to extract meaningful information, utilizing both the layout and textual features present in the document.

This model provides a comprehensive solution for tasks involving medical image classification, document analysis, and structured information extraction, making it ideal for healthcare applications, research, and document management systems.


## Predicted Entities

`'image'`, `'document_notes'`, `'others'`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/visualclf_vit_dicom_en_5.0.1_3.2_1692702752962.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/visualclf_vit_dicom_en_5.0.1_3.2_1692702752962.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use


<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = nlp.ImageAssembler() \
    .setInputCol("image") \
    .setOutputCol("image_assembler")

imageClassifier_loaded = nlp.ViTForImageClassification.pretrained("visualclf_vit_dicom", "en", "clinical/ocr")\
  .setInputCols(["image_assembler"])\
  .setOutputCol("class")

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    imageClassifier_loaded
])

test_image = spark.read\
    .format("image")\
    .option("dropInvalid", value = True)\
    .load("./dicom.JPEG")

result = pipeline.fit(test_image).transform(test_image)

result.select("class.result").show(1, False)
```

</div>

## Example

### Input:
![Screenshot](/assets/images/examples_ocr/dicom_example.png)

## Output text
```bash
+-------+
|label  |
+-------+
|image  |
+-------+
```


{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|visualclf_vit_dicom|
|Compatibility:|Healthcare NLP 5.0.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[image_assembler]|
|Output Labels:|[class]|
|Language:|en|
|Size:|321.6 MB|