---
layout: docs
header: true
seotitle: Visual NLP | John Snow Labs
title: Speed Benchmarks
permalink: /docs/en/ocr_benchmark
key: docs-benchmark
modify_date: "2024-06-24"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## Speed Benchmarks

### PDF De-identification Benchmark

- **Dataset:** 1000 scanned PDF pages.
- **Instance :** 
  - m5n.4xlarge (16 vCPUs, 64 GiB memory) 
  - m5n.8xlarge (32 vCPUs, 128 GiB memory)
- **AMI:** ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-20240411
- **Versions:**
  - **spark-nlp Version:** v5.4.0
  - **visual-nlp Version:** v5.3.2
  - **spark-nlp-jsl Version :** v5.3.2
  - **Spark Version :** v3.4.1
- **Visual NLP Pipeline:** 'pdf_deid_subentity_context_augmented_pipeline'

</div><div class="h3-box" markdown="1">

#### Benchmark Table

{:.table-model-big}
| Instance      | memory | cores | input\_data\_pages| partition     | second per page | timing  |
| ------------- | ------ | ----- | ----------------- | ------------- | --------------- | ------- |
| m5n.4xlarge   | 64 GB  | 16    | 1000              | 10            | 0.24            | 4 mins  |
| m5n.8xlarge   | 128 GB | 32    | 1000              | 32            | 0.15            | 2.5 mins|


### Dicom De-identification Benchmark
This section contains benchmarks for de-ideintification of dicom files, both for GPU and CPU. 
Note: file sizes are included as reference, but *they are not* the best proxy for estimating running time, as the final figures will depend on image size than in turn depends on the actual compression that is being used in the file.
In this test we used 17 files, with an average size of XYZ, and using XYZ compression which is very popular in dicom. The average image dimensions are XYZ, and every dicom file contained a single frame.
The numbers reported are average *time per file*.


| **Model**                                                   | **Google Colab GPU** | **Databricks Standalone GPU** | **Google Colab CPU** | **Databricks Standalone CPU** |
|------------------------------------------------------------|----------------------|------------------------------|----------------------|------------------------------|
| **ImageTextDetector - MemOpt (Scala) + ImageToTextV2 - Base (Scala)**  | **3.63**            | **4.66**                     | **11.87**            | **6.11**                     |
| **ImageTextDetector - MemOpt (Scala) + ImageToTextV2 - Large (Scala)** | **4.06**            | **5.39**                     | **22.85**            | **19.48**                    |
| **ImageTextDetector - MemOpt (Scala) + ImageToTextV3 (Scala)**         | **0.68**            | **1.15**                     | **2.73**             | **1.64**                     |
| **ImageToText (Python)**                                   | **0.31**            | **1.21**                     | **1.12**             | **0.3**                      |




* **Google Colab GPU**: Utilized a single A100 GPU (40 GB) – 7.62 Credits/hr.
* **Databricks Standalone GPU**: DB Standalone Driver (64 GB, Single GPU, g4dn.4xLarge [T4]) – 2.85 DBU/h.
* **Google Colab CPU**: HIGH RAM [8 Cores] instance – 0.18 Credits/hr.
* **Databricks Standalone CPU**: Driver with 64 GB [16 Cores] (m4.4xlarge) – 3 DBU/h.


#### How to use this data
##### GPU vs. CPU
These are the models you want to use for a serious project:
* **ImageTextDetector - MemOpt (Scala) + ImageToTextV2 - Base (Scala)**
* **ImageTextDetector - MemOpt (Scala) + ImageToTextV3 (Scala)**

Don't be confused by the average times between GPU and CPU, for example for Databricks Standalone, the cost per dicom file is what matters. Let's take 1000 studies to make numbers more easy to digest,


**Cost Per 1K doc(DB/CPU)**:
1000 * (6.11/3600) * 3 DBU/h = **5.09 DBU**

**Cost Per 1K doc(DB/GPU)**:
1000 * (4.66/3600) * 2.85 DBU/h = **3.68 DBU**

Here we see that for this workload the cheaper option is to go with GPU.

#### Using the data as a proxy for estimation
What governs the processing time is image size. Let's take a look at some figures for this dataset,
* *Transfer Syntax:* 1.2.840.10008.1.2.1(Uncompressed).
* *Average Width:* 558.20 pixels
* *Average Height:* 599.00 pixels
* *Average Size:* 690503 bytes

You need to compute the *average number of pixels per image* in your dataset. For us: 334361.</br>
_Your linear projections should be based on that value_.
*Example:* I have 100 single frame 1024x1024 images, we have 1048576 pixels per image, and you will need, (1048576/334361)*3.63 seconds on average on Google Colab GPU per image. And you can do the remaining math for dollar figures.

Note: don't forget to count multi-frame images.

#### I don't know the dimensions of my images
s




</div>
