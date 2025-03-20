---
layout: docs
header: true
seotitle: Visual NLP | John Snow Labs
title: Speed Benchmarks
permalink: /docs/en/ocr_benchmark
key: docs-benchmark
modify_date: "2025-02-04"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## Speed Benchmarks

### PDF De-identification Benchmark Experiment

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

| Instance      | memory | cores | input\_data\_pages| partition     | second per page | timing  |
| ------------- | ------ | ----- | ----------------- | ------------- | --------------- | ------- |
| m5n.4xlarge   | 64 GB  | 16    | 1000              | 10            | 0.24            | 4 mins  |
| m5n.8xlarge   | 128 GB | 32    | 1000              | 32            | 0.15            | 2.5 mins|

### DICOM De-identification Benchmark Experiment

- **Datasets:**
  - 15 files of 1 frame, uncompresses, 3.3 MB
  - 15 files of 1 frame, compresses, 1.1 MB
  - 1 file of 160 frames, 377,5 MB
- **Instance :** 
  - g5.4xlarge (16 vCPUs, 64 GiB memory) 
  - g5.8xlarge (32 vCPUs, 128 GiB memory)
- **Versions:**
  - **spark-nlp Version:** 5.5.1
  - **visual-nlp Version:** 5.5.0
  - **spark-nlp-jsl Version :** 5.5.1
  - **Spark Version :** 3.5.0
- **Visual NLP Pipeline:** [SparkOcrDicomDeIdentificationV2Streaming](https://github.com/JohnSnowLabs/visual-nlp-workshop/blob/master/jupyter/Dicom/SparkOcrDicomDeIdentificationV2Streaming.ipynb)

</div><div class="h3-box" markdown="1">

#### Benchmark Table

| Test                      | memory  | cores | files | frames | sec/frame | sec/frame 1 cpu |
| ------------------------- | ------  | ----- | ----- | ------ | --------- | --------------- |
| 1 frame, uncompressed     | 64 GB   | 16    | 15    | 1      | 11.6      | 185.6           |
| 1 frame, compressed       | 64 GB   | 16    | 15    | 1      | 11.6      | 185.6           |
| 160 frames, lossy compres | 128 GB  | 32    | 1     | 160    | 0.925     | 29,6            |

**"sec/frame 1 cpu"** column is rough estimation how much it'd take on 1 cpu machine. For your environment you may divide it on number of available cpus to get rough estimation.

#### Conclusions

- Compression doesn't affect performance due it is not so heavy operation in comparison with the rest
- Performance may depend on DICOM image's size abd quality

</div>
