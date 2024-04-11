---
layout: docs
header: true
seotitle: NLP Lab | John Snow Labs
title: NLP Lab Release Notes 6.0.0
permalink: /docs/en/alab/annotation_labs_releases/release_notes_6_0_0
key: docs-licensed-release-notes
modify_date: 2024-04-11
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## 6.0.0

Release date: **04-11-2024**

## Generative AI Lab 6 – Train Visual NER using GPU and Support for PAYG License
We are delighted to announce the launch of Generative AI Lab 6.0.0, bringing significant updates around hardware architecture, focusing on boosting performance for model training and Visual NER processing. This version introduces a GPU template now accessible in the AWS marketplace improving the general experience around license provisioning, unlocking all the features of Generative AI Lab immediately. 
The added boost in performance alongside with seamless access to a wide array of AI capabilities, including Prompts, Rules, Resolvers, Task Generation, Training, and pre-annotation, underscores our dedication to meeting the evolving needs of the NLP community. Discover the limitless possibilities with Generative AI Lab 6.0 and elevate your NLP projects to new levels of excellence.

## Get the Generative AI Lab with GPU support 

As part of this update, GPU-based AMI will only be available enabling users to experience the enhanced performance and capabilities of GPU.

**Installation on Dedicated Servers:**

Use `gpu` (case-insensitive) **optional** parameter with annotationlab-installer.sh script to enable usage of GPU resources. This will only work if your host has GPU resources. This parameter is used as a flag, it will enable GPU resources when used, otherwise, the installer will ignore anything related to GPU.

```bash
$ ./annotationlab-installer.sh gpu
```

**Notice:** GPU usage can be disabled at a later time, by simply editing the annotationlab-updater.sh script and set `useGPU` variable to false. However, this will only prevent the app from using GPU resources, it will not remove the already installed Nvidia drivers and plugins.

### Migrate your NLP Lab Backup to Generative AI Lab 6

Migrating to the new version is easy! Users who are using an older version of the NLP Lab can migrate their annotated data and configured settings to the new Generative AI Lab 6 through our Backup and Restore feature. This process enables users to back up their data and files from a CPU-based instance to the cloud of their choice (Azure Blob/AWS S3) and then restore the configurations to a GPU-based instance. You must follow the steps outlined below to seamlessly back up and restore all your data from an old instance to the new Generative AI Lab 6.

<iframe src="/assets/images/annotation_lab/6.0.0/BackupAndRestore.mp4" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

**Follow these steps to migrate your data**:
#### 1. Backup Data:
- Navigate to the Backup page of your CPU-based instance.
- Enter backup details.
- Schedule an immediate backup via backend modification: 
```bash
kubectl edit cronjob
```
- Monitor the backup pod status: 
```bash
kubectl get pods
```
#### 2. Verify Backup:
- Upon completion, your backed-up database and files will be visible in cloud storage.

#### 3. Restore Data:
- Access the backend of your target GPU-based instance.
- Transfer backed-up data from cloud storage to artifacts/restore/database.
- Perform database restoration: 
```bash
sudo ./restore_all_databases.sh <backed-up_database_name>
```
- Copy backed-up files from cloud storage to artifacts/restore/files.
- Execute file restoration: 
```bash
sudo ./restore_files.sh <backed-up_files_name>
```
#### 4. Verify Restoration:
- Access the UI, all data and files should now be successfully restored.

### GPU Resource Availability
If the Generative AI Lab is equipped with a GPU, the following message will be displayed on the infrastructure page:  

"**GPU Resource Available**".
![infra](/assets/images/annotation_lab/6.0.0/1.png)

### Visual NER Training with GPU
The Training & Active Learning page now includes a new option "**Use available GPU**" for Visual NER projects. Selecting this option enables Visual NER model training using GPU.

![infra](/assets/images/annotation_lab/6.0.0/2.png)

### Boost performance with the use of GPU- side by side CPU - GPU Benchmark for Visual Named Entity Recognition (NER) Project

In this section we dive into a side-by-side comparison between CPUs and GPUs for a specific task: recognizing names in images (Visual NER). Two powerful machines were used for comparison, one with CPU only (central processing unit), and the second one equipped with GPU (graphics processing unit). The goal of the test was to measure and compare the time required for training an AI model based on the different hardware architectures of the servers.

#### Understanding CPU vs GPU for NLP Tasks:

One of the important differences between CPU and GPU architecture is in how they deliver performance for AI training and inference with GPU delivering leading performance in this context. CPUs, with their adeptness in sequential tasks and single-threaded performance, stand in contrast to GPUs, which thrive in highly parallelized environments, excelling at simultaneous large-scale computations crucial for NLP tasks, especially those entailing intensive matrix operations as encountered in deep learning models.

#### Hardware Configuration:

##### CPU Machine (m4.4xlarge):
        CPU: Intel Xeon E5-2676 v3 (Haswell) processors (16 cores)
        Memory: 64 GiB
        Storage: EBS only
        Network Performance: Moderate
##### GPU Machine (g4dn.2xlarge):
        GPU: NVIDIA T4 Tensor Core GPU
        vCPUs: 8
        GPU Memory: 16 GiB
        Memory: 32 GiB
        Storage: EBS only
        Network Performance: High

#### Versions:

The benchmarking was carried out using the following Spark NLP versions:

Spark version: 3.4.0

SparkNLP version: 5.3.0

SparkOCR version: 5.3.0

#### Benchmark Setup:

Our benchmarking focuses on a Visual Named Entity Recognition (NER) project. Visual data (images) was processed to identify named entities like people, locations, and brands within them. Visual NER training employs advanced NLP techniques and deep learning architectures, demanding significant computational resources for efficient execution. To assess the performance training of our Visual NER model GPU-enabled instance, the benchmark experiments were conducted using a batch size of 8, with 1 core CPU allocated for the GPU training. In addition to the GPU's dedicated 16GB memory, 24 GB of system memory was allocated for the training pod.

For Visual NER model training without GPU, we conducted benchmark experiments using a batch size of 8, with 14 cores CPU allocation and 58 GB of memory for training.

The time taken for model training for both cases was measured, and the results were compared. 

#### Dataset:

The benchmark utilizes a dataset containing 714 tasks. Each task is an image with corresponding labels for the named entities present. 

#### Training params:

Eval Size: 0.4 (percentage of data used for evaluation)

Learning rate: 0.001 (controls how quickly the model learns)

Batch size: 8 (number of images processed together during training)

#### Benchmark Results:

The training pod specifications were:

    For instance, without GPU: 14 CPU cores and 58GB RAM
    For instance, with both GPU and CPU: 1 CPU core, 24GB RAM, and 1 GPU


| Batch Size | Only CPU Training Time | With GPU Training Time | Speedup (With GPU vs Only CPU) |
|------------|-------------------|-------------------|----------------------|
| 8          | 225 mins          | 26 mins           | 8.6x                 |

The benchmarking experiment was aimed to offer insights into the performance differences between CPU and GPU architectures for Visual NER projects. The results showed 225 minutes of execution time for CPU training alone, whereas GPU training only took 26 minutes, resulting in an 8.6x speedup. Even with just a 1-core CPU and 24GB of RAM, training with a GPU significantly surpasses the performance of a 14-core CPU with 58GB of RAM. Just using 1 GPU, we could decrease the number of CPU cores from 14 cores to 1 core and reduce the memory allocation by 30 percent for the training. The results underscore the superior performance of GPUs in parallel computations, which considerably accelerates training processes for NLP tasks.

## Support for PAYG License
With the release of version 6.0.0, Generative AI Lab now offers support for the PAYG (Pay-As-You-Go) license option alongside the existing license options. The PAYG license introduces a flexible pay-per-usage billing model, reducing costs and providing the mechanism for paying only for the utilized resources.

**Key Features and Current Implementation of PAYG License:**
- **Opt-In Option for manually installed application:** For manually installed Generative AI Lab, users can choose the PAYG license when purchasing licenses from my.johnsnowlabs.com, download it, and import it to Generative AI Lab from the License page. Currently, importing PAYG License directly from the license page by logging into my.johnsnowlabs.com from within the application is not possible.
- **Flexible Billing:** With the PAYG license, users are billed based on only the resources they use, offering a more tailored and cost-effective pricing model.
- **Support for Multiple Servers:** PAYG license also comes with support for running multiple training and pre-annotation servers in parallel. PAYG license enables users to deploy and utilize multiple pre-annotation servers and training instances in parallel. This boosts workflow efficiency and productivity, allowing the execution of tasks simultaneously and accelerating project completion.

![MultipleServerDeploymentWithPayG](/assets/images/annotation_lab/6.0.0/3.png)


### PAYG License Included in AMI Installation

With the release of version 6.0.0, Generative AI Lab's AMI installation comes equipped with the PayG (Pay-As-You-Go) license. This license is autogenerated and readily available on the License page within the AMI environment, eliminating the need for users to manually add the license.

**Features of PAYG License in AMI:**
- **Automated License Generation and Simplified Management:** The PAYG license is autogenerated and readily available on the License page of the AMI installation. Users no longer need to worry about manually adding the license. Therefore, concerns regarding expiration or accidental deletion are eliminated. The license renewal process is smooth, the PayG license doesn't need to be renewed and a new license gets generated automatically once the existing one expires. 
- **Exclusive Support:** Generative AI Lab in AWS AMI exclusively supports the PAYG license. Users cannot upload any other types of licenses. The license page in AMI only shows the current PayG license and users cannot add or delete licenses from this page.
  
![LicensePageInAMI](/assets/images/annotation_lab/6.0.0/4.png)


This enhancement streamlines the licensing process for AMI users, ensuring continuous access to a valid license without any manual intervention or risk of license issues.

### Cost Awareness Banner for PAYG License
In this version, with the introduction of the PAYG license, proactive measures have been introduced to inform users about the potential costs associated with the new license. Users will now be presented with a noticeable message banner at the top of the page, stating: "Continuous Server Usage Incurs Costs! Please check the deployed server." The message is always shown even if no server is deployed on the cluster page. It helps users to be aware of the fact that they are billed based on application and resource usage.

![LicensePageInAMI](/assets/images/annotation_lab/6.0.0/5.gif)

By presenting this message, users are reminded to monitor their server usage and associated costs, promoting cost-conscious behavior. This feature enhances user awareness and ensures transparency regarding the cost implications of utilizing the PAYG license within Generative AI Lab.

It's important to note that there is no change in the existing functionality of Generative AI Lab. Users can continue to access and use all features and functionalities as before.

This introduction of the PAYG (Pay-As-You-Go) license option reflects our commitment to providing users with flexible licensing options that best suit their needs and usage patterns.

## Improvements

### Support for multiple spaces and tabs in Label Metadata
Previously, within the label metadata, multiple spaces were considered as a single space, and tabs were not supported. Pressing the tab key would render the text area inactive. Now within label metadata, users can utilize multiple spaces and tabs, both of which are preserved when adding metadata to labeled texts.

### Bug Fixes

- **Pre-annotation using Text Classification model with HC license is not working**

  Previously, healthcare classification models such as "classifierml_ade" were not deployed in pre-annotation even with a healthcare license. However, this issue has now been rectified.
 
- **Zoom Feature not working in predictions and submitted completions in Visual NER Project**

  Before, the zoom-in and zoom-out functionalities for submitted completions and predictions in the Visual NER project were not functioning properly. However, this issue has been resolved.
 
</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

{%- include docs-annotation-pagination.html -%}
