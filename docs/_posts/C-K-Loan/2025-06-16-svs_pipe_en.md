---
layout: model
title: SVS DEID Pipeline
author: John Snow Labs
name: svs_pipe
date: 2025-06-16
tags: [svs, dicom_wsi, en, licensed]
task: De-identification
language: en
edition: Visual NLP 5.5.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to deidentify SVS files. It removes Protected Health Information (PHI) from metadata tags and pixels. This requires healthcare nlp as well has visual nlp installed.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/svs_pipe_en_5.5.0_3.4_1750116076010.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/svs_pipe_en_5.5.0_3.4_1750116076010.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparkocr.utils.svs.draw_bbox_on_tile import deidentify_svs_tile
from sparkocr.utils.svs.extract_tiles import process_folder
raw_svs_path = './svs_input'
output_deid_tags_path = "./svs_output_deid_tags"
output_tiles_path = "./svs_output_tiles"
output_deid_tags_and_pixels_path = './svs_output_deid_tags_and_pixels'
deid_tags = ['ImageDescription.ScanScope ID', 'ImageDescription.Time Zone', 'ImageDescription.ScannerType']
NUM_WORKERS = 4

# 1. Create new SVS file where Tags DEID
remove_phi(raw_svs_path, output_deid_tags_path, verbose=True, append_tags=deid_tags)

# 2. Generate Frames from Raw SVS
process_folder(raw_svs_path, output_tiles_path, NUM_WORKERS)

# 3. Load the Raw Frames as Spark DF
image_df = spark.read.format("binaryFile").load(output_tiles_path).cache()

# 4. Get Pipe and process it
pipe = PretrainedPipeline("dicom_deid_generic_augmented_minimal", "en", "clinical/ocr")
result = pipe.transform(image_df).cache()

# 5. Create the final SVS File with TAGs and Pixels DEID
deid_info = result.select("path", "coordinates").distinct()
deidentify_svs_tile(output_deid_tags_path, deid_info, output_svs_path=output_deid_tags_and_pixels_path,create_new_svs_file = True)

```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|svs_pipe|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.2 GB|

## Included Models

- BinaryToImage
- ImageTextDetectorCraft
- ImageToTextV2
- DocumentAssembler
- DocumentNormalizer
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- RegexMatcherModel
- ChunkConverter
- NerConverterInternalModel
- ChunkMergeModel
- PositionFinder
- ImageDrawRegions
