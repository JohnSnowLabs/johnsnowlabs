---
layout: docs
header: true
title: GPU vs CPU benchmark
permalink: /docs/en/CPUvsGPUbenchmark_healthcare
key: docs-concepts
modify_date: "2021-08-31"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

This section includes a benchmark for MedicalNerApproach(), comparing its performance when running in `m5.8xlarge` CPU vs a `Tesla V100 SXM2` GPU, as described in the `Machine Specs` section below.

Big improvements have been carried out from version 3.3.4, so please, make sure you use at least that version to fully levearge Spark NLP capabilities on GPU.

</div>
<div class="h3-box" markdown="1">

### Machine specs

#### CPU
An AWS `m5.8xlarge` machine was used for the CPU benchmarking. This machine consists of `32 vCPUs` and `128 GB of RAM`, as you can check in the official specification webpage available [here](https://aws.amazon.com/ec2/instance-types/m5/)

</div>
<div class="h3-box" markdown="1">

#### GPU
A `Tesla V100 SXM2` GPU with `32GB` of memory was used to calculate the GPU benchmarking.

</div>
<div class="h3-box" markdown="1">

### Versions
The benchmarking was carried out with the following Spark NLP versions:

Spark version: `3.0.2`

Hadoop version: `3.2.0`

SparkNLP version: `3.3.4`

SparkNLP for Healthcare version: `3.3.4`

Spark nodes: 1

</div>
<div class="h3-box" markdown="1">

### Benchmark on MedicalNerDLApproach()

This experiment consisted of training a Name Entity Recognition model (token-level), using our class NerDLApproach(), using Bert Word Embeddings and a Char-CNN-BiLSTM Neural Network. Only 1 Spark node was used for the training.

We used the Spark NLP class `MedicalNer` and it's method `Approach()` as described in the [documentation](https://nlp.johnsnowlabs.com/docs/en/licensed_annotators#medicalner).

The pipeline looks as follows:
![](/assets/images/CPUvsGPUbenchmarkpic4.png)

</div>
<div class="h3-box" markdown="1">

#### Dataset
The size of the dataset was small (17K), consisting of:

Training (rows): `14041`

Test (rows): `3250`

</div>
<div class="h3-box" markdown="1">

#### Training params
Different batch sizes were tested to demonstrate how GPU performance improves with bigger batches compared to CPU, for a constant number of epochs and learning rate.

Epochs: `10`

Learning rate:  `0.003`

Batch sizes: `32`, `64`, `256`,  `512`, `1024`, `2048`

</div>
<div class="h3-box" markdown="1">

#### Results
Even for this small dataset, we can observe that GPU is able to beat the CPU machine by a `62%` in `training` time and a `68%` in `inference` times. It's important to mention that the batch size is very relevant when using GPU, since CPU scales much worse with bigger batch sizes than GPU.

</div>
<div class="h3-box" markdown="1">

#### Training times depending on batch (in minutes)

![](/assets/images/CPUvsGPUbenchmarkpic6.png)

{:.table-model-big}
| Batch size | CPU | GPU |
| :---: | :---: | :--: |
| 32 | 9.5 | 10 |
| 64 | 8.1 | 6.5 |
| 256 | 6.9 | 3.5 |
| 512 | 6.7 | 3 |
| 1024 | 6.5 | 2.5 |
| 2048 | 6.5 | 2.5 |

</div>
<div class="h3-box" markdown="1">

#### Inference times (in minutes)
Although CPU times in inference remain more or less constant regardless the batch sizes, GPU time experiment good improvements the bigger the batch size is.

CPU times: `~29 min`

{:.table-model-big}
| Batch size |  GPU |
| :---: | :--: |
| 32 | 10 |
| 64 | 6.5 |
| 256 | 3.5 |
| 512 | 3 |
| 1024 | 2.5 |
| 2048 | 2.5 |

![](/assets/images/CPUvsGPUbenchmarkpic7.png)

</div>
<div class="h3-box" markdown="1">

#### Performance metrics
A macro F1-score of about `0.92` (`0.90` in micro) was achieved, with the following charts extracted from the `MedicalNerApproach()` logs:

![](/assets/images/CPUvsGPUbenchmarkpic8.png)

</div>
<div class="h3-box" markdown="1">

### Takeaways: How to get the best of the GPU
You will experiment big GPU improvements in the following cases:

{:.list1}
1. Embeddings and Transformers are used in your pipeline. Take into consideration that GPU will performance very well in Embeddings / Transformer components, but other components of your pipeline may not leverage as well GPU capabilities;
2. Bigger batch sizes get the best of GPU, while CPU does not scale with bigger batch sizes;
3. Bigger dataset sizes get the best of GPU, while may be a bottleneck while running in CPU and lead to performance drops;

</div>
<div class="h3-box" markdown="1">

### MultiGPU Inference on Databricks
In this part, we will give you an idea on how to choose appropriate hardware specifications for Databricks. Here is a few different hardwares, their prices, as well as their performance:
![image](https://user-images.githubusercontent.com/25952802/158796429-78ec52b1-c036-4a9c-89c2-d3d1f395f71d.png)

Apparently, GPU hardware is the cheapest among them although it performs the best. Let's see how overall performance looks like:

![image](https://user-images.githubusercontent.com/25952802/158799106-8ee03a8b-8590-49ae-9657-b9663b915324.png)

Figure above clearly shows us that GPU should be the first option of ours. 

In conclusion, please find the best specifications for your use case since these benchmarks might depend on dataset size, inference batch size, quickness, pricing and so on.

Please refer to this video for further info: https://events.johnsnowlabs.com/webinar-speed-optimization-benchmarks-in-spark-nlp-3-making-the-most-of-modern-hardware?hsCtaTracking=a9bb6358-92bd-4cf3-b97c-e76cb1dfb6ef%7C4edba435-1adb-49fc-83fd-891a7506a417

### MultiGPU training
Currently, we don't support multiGPU training, meaning training 1 model in different GPUs in parallel. However, you can train different models in different GPUs.

</div>
<div class="h3-box" markdown="1">

### MultiGPU inference
Spark NLP can carry out MultiGPU inference if GPUs are in different cluster nodes. For example, if you have a cluster with different GPUs, you can repartition your data to match the number of GPU nodes and then coalesce to retrieve the results back to the master node. 

Currently, inference on multiple GPUs on the same machine is not supported.

### Where to look for more information about Training
Please, take a look at the [Spark NLP](https://nlp.johnsnowlabs.com/docs/en/training) and [Spark NLP for Healthcare](https://nlp.johnsnowlabs.com/docs/en/licensed_training) Training sections, and feel free to reach us out in case you want to maximize the performance on your GPU.

</div>
