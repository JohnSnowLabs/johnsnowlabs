---
layout: docs
header: true
seotitle: Spark OCR | John Snow Labs
title: Spark OCR release notes
permalink: /docs/en/spark_ocr_versions/release_notes_5_5_0
key: docs-ocr-release-notes
modify_date: "2024-01-23"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 5.5.0

Release date: 23-01-2024

## Visual NLP 5.5.0 Release Notes 🕶️

**We are glad to announce that Visual NLP 5.5.0 has been released! This release comes with new Dicom pretrained pipelines, new features, and bug fixes. 📢📢📢**

</div><div class="h3-box" markdown="1">

## Highlights 🔴

* New Obfuscation Features in ImageDrawRegions.
* New obfuscation features in DicomMetadataDeidentifier.
* New Dicom Pretrained Pipelines.
* New VisualDocumentProcessor.

## New Obfuscation Features in ImageDrawRegions
ImageDrawRegions' main purpose is to draw solid rectangles on top of regions that typically come from NER or some other similar model. Many times, it is interesting not to only draw solid rectangles on top of detected entities, but some other values, like obfuscated values. For example, with the purpose of protecting patient's privacy, you may want to replace a name with another name, or a date with a modified date.

This feature, together with the Deidentification transformer from Spark NLP for Healthcare can be combined to create a 'rendering aware' obfuscation pipeline capable of rendering obfuscated values back to the source location where the original entities were present. The replacement must be 'rendering aware' because not every example of an entity requires the same space on the page to be rendered. So for example, 'Bob Smith' would be a good replacement for 'Rod Adams', but not for 'Alessandro Rocatagliata', simply because they render differently on the page. Let's take a look at a quick example,

![image](/assets/images/ocr/obfuscation_impainting.png)

to the left we see a portion of a document in which we want to apply obfuscation. We want to focus on the entities representing PHI, like patient name or phone number. On the right side, after applying the transformation, we have an image containing fake values.
You can see that the PHI in the source document has been replaced by similar entities, and these entities not only are of a similar category, but are also of a similar length.


## New obfuscation features in DicomMetadataDeidentifier
Now you can customize the way metadata is de-identified in DicomMetadataDeidentifier. Customization happens through a number of different actions you can apply to each tag, for example, replacing a specific tag with a literal, or shifting a date by a number of days randomly.
In order to feed the configuration for each of these actions, you need to pass a CSV file to DicomMetadataDeidentifier, like this,

```
DicomMetadataDeidentifier()\
setStrategyFile(path_to_your_csv_file)
```

The CSV you need to provide looks like this,
```
Tags,VR,Name,Status,Action,Options
"(0002,0100)",UI,Private Information Creator UID,,hashId
"(0002,0102)",OB,Private Information,,hashId
```

For example, the first line is an ID, and we are asking to hash the UID, and to replace the value in the output Dicom file with the new hash value.
Here is a more exhaustive list of actions, datatypes and parameters, you can use,

Key | Datatypes | Parameter examples
-- | -- | --
remove | DA, OB, SH, PN, LT, DT, UI, AS, LO, CS, ST, SQ | 
replaceWithLiteral | CS, PN | Susanita Smith, Chest
hashId | OB, SH, UI, LO, CS, SQ | coherent
shiftDateByRandomNbOfDays | DA, LO, AS, DT | coherent
ShiftTimeByRandomNbOfSecs | DT | coherent
replaceWithRandomName | PN, LO | coherent
shiftDateByFixedNbOfDays | DA | 112


### New Dicom Pretrained Pipelines
We are releasing three new Dicom Pretrained Pipelines:
* `dicom_deid_generic_augmented_minimal`: this pipeline will remove only PHI from images, and the minimal number of metadata tags.
* `dicom_deid_full_anonymization`: this pipeline will remove all text from images(not only PHI), and most metadata tags. This is the most aggressive de-identification pipeline.
* `dicom_deid_generic_augmented_pseudonym`: this pipeline will try to remove PHI from images, and will obfuscate most tags in metadata.

Check notebook [here](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/Dicom/SparkOcrDicomPretrainedPipelines.ipynb) for examples on how to use this.

### New Visual Document Processor
New VisualDocumentProcessor that produces OCR text and tables on a single pass!,
In plugs and play into any Visual NLP pipeline, it receives images, and it returns texts and tables following the same existing schemas for these datatypes,
```
proc = VisualDocumentProcessor() \
    .setInputCol("image") \
    .setOutputCols(["text", "tables"]) \
    .setFreeTextOnly(True) \
    .setOcrEngine(VisualDocumentProcessorOcrEngines.EASYOCR)
result = proc.transform(df)
```

Check this [sample notebook](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/SparkOcrVisualDocumentProcessor.ipynb) for an example on how to use it.

### Other Dicom Changes
* DicomDrawRegions support for setting compression quality, now you can pick different compression qualities for each of the different compression algorithms supported. The API receives an array with each element specifying the compression type like a key/value,
Example,
```
DicomDrawRegions()\
.setCompressionQuality(["8Bit=90","LSNearLossless=2"])
```

### Enhancements & Bug Fixes
* New parameter in SVS tool that specifies whether to rename output file or not,
```
from sparkocr.utils.svs.deidentifier import remove_phi
remove_phi(input_path, output_path, rename=True)
```
* Improved memory management in ImageTextDetectorCraft.
* Fixed a memory leak in ImageToTextV2.
* Fixed a bug in VisualDocumentNerLilt that happened when saving the model after fine tuning.
 

This release is compatible with Spark-NLP 5.5.2, and Spark NLP for Healthcare 5.5.2.

</div><div class="h3-box" markdown="1">

## Previous versions

</div>

{%- include docs-sparckocr-pagination.html -%}
