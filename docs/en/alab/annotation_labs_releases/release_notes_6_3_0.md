---
layout: docs
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Generative AI Lab Release Notes 6.3.0
permalink: /docs/en/alab/annotation_labs_releases/release_notes_6_3_0
key: docs-licensed-release-notes
modify_date: 2024-06-21
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## 6.3.0

Release date: **06-21-2024**

## Generative AI Lab – No-Code Environment for Building Task-Specific AI Models with LLMs for Azure Marketplace
We are happy to announce the release of Generative AI Lab 6.3, marking the transition from the previous NLP Lab to a state-of-the-art No-Code platform that enables domain experts to train task-specific AI models using large language models (LLMs). This new product introduces a suite of advanced features and functionalities designed to facilitate the creation, management, and deployment of AI-driven solutions efficiently and accurately. With robust integration capabilities, comprehensive model training tools, and enhanced security measures tailored for high-compliance sectors such as healthcare, Generative AI Lab sets a new standard in the generative AI platform landscape. John Snow Labs is committed to democratizing AI tool interaction and making it more accessible, especially within the healthcare sector. We aim to equip healthcare professionals, from clinicians to researchers, with the tools to construct bespoke AI models. These models are pivotal in analyzing extensive datasets, discerning patterns, aiding in diagnosis, and enhancing patient care, all achievable without in-depth coding expertise. This opens new avenues in personalized medicine, accelerates research, and improves patient outcomes, thereby revolutionizing the healthcare landscape.

In this release, Generative AI Lab enhances its capabilities by integrating seamlessly with the OpenAI API, enabling the effortless training, testing, and refinement of task-specific models tailored to the distinct needs of your domain and use case. Whether your focus is on refining document processing, orchestrating AI assets, or fortifying regulatory compliance, Generative AI Lab delivers a comprehensive, secure, and effective framework to transform your AI ambitions into tangible outcomes. 

Generative AI Lab 6.3 marks a significant leap forward in hardware architecture and performance optimization for model training and Visual Document understanding. Now available on the Azure marketplace with a GPU-enabled template, this release simplifies license provisioning and unlocks immediate access to all features, including prompts, Rules, pre-trained medical models, medical resolvers, medical model training, model testing and visual document understanding. This enhancement not only accelerates performance but also broadens your access to a plethora of AI capabilities, reaffirming our commitment to advancing the NLP community's capabilities. 

## Use LLMs to bootstrap task-specific models 
Generative AI Lab facilitates seamless integration with the OpenAI API, empowering domain experts to easily define prompts for classification or entity extraction. This integration allows Generative AI Lab to process the LLM's responses, adjust the indexes of the extracted segments, and overlay pre-annotation results directly onto the original documents. 

 ![GenaiImage](/assets/images/annotation_lab/6.3.0/1.png)

Once pre-annotations are generated, domain experts can step in and review these results through a user-friendly interface, offering their expertise in the form of adjustments or corrections. This refined data can then be employed to develop smaller, more specialized models that are optimized for processing the document of interest.

Furthermore, Generative AI Lab supports comprehensive training experiments and provides access to benchmarking data to evaluate the performance during the model training process. For continuous model enhancement, users can augment the training dataset with additional examples and reinitiate the training process, ensuring sustained improvement and adaptation.

The final step is iterative refinement. Here, users can assess the model's performance metrics and introduce more data as needed. This process ensures that the model can be adapted and improved, as a response to new information and evolving requirements in the healthcare domain.

## Private, on-premise, high-compliance prompt engineering
In the healthcare sector, protecting Personal Health Information (PHI) is paramount. To this end, Generative AI Lab provides support for Zero-Shot models that can process PHI directly within your infrastructure, thus ensuring privacy and compliance. Mirroring the workflow used for integrating LLMs via external APIs, you can now utilize Zero-Shot Learning for the pre-annotation of your documents. This functionality is available directly within the Generative AI Lab, eliminating the need for external API calls to LLMs.

By adopting this approach, you can ensure adherence to stringent healthcare regulations, providing reassurance and peace of mind.

 ![GenaiImage](/assets/images/annotation_lab/6.3.0/2.png)

## Organize and share models, test models, prompts, and rules within one private enterprise hub
The Models Hub acts as a centralized platform where users from your organization can easily manage their AI development lifecycle. It supports operations like the secure sharing, searching, filtering, testing, publishing, importing, and exporting of AI models, prompts, and rules. This functionality simplifies the management of proprietary AI assets, enabling teams to efficiently collaborate and leverage these assets for their projects.

 ![GenaiImage](/assets/images/annotation_lab/6.3.0/3.png)

The Models Hub implements role-based access control (RBAC), allowing you to define who in your organization has access to your assets, who can experiment with prompts or rules or who can export your models. Versioning and backup features are available to keep a record of changes made to your assets, ensuring that you can always revert to previous versions if needed. 

Finally, the playground allows for easy editing and testing of prompts, rules or models without coding.

Generative AI Lab is integrated with the NLP Models Hub, which gives access to an extensive library of over 40,000 models and pipelines, ready to be integrated into your projects. This integration not only enhances your capabilities but also provides easy access to model benchmarking data, model documentation, and one-click downloads.

**Models:**

Within the Models page, you'll find a private repository tailored to your organization's needs, including models you've trained, uploaded, or downloaded from the NLP Models Hub. This centralized management system ensures your AI assets are organized and readily available.

**LangTest**

With the integration of John Snow Labs LangTest framework. Test case generation, test execution, and model testing across various categories are now part of Generative AI Lab. This integration offers data augmentation and seamlessly fits into the project flow of Generative AI Lab, supporting numerous test types and effectively identifying and addressing model issues.

**Rules:** 

The Rules page offers a dedicated space for creating and managing the rules you can define and use in your projects. With an intuitive editing interface and practical examples, crafting custom rules becomes a straightforward process.

**Prompts:** 

Lastly, the Prompts page allows you to curate a collection of prompts, essential for preannotating your documents and for training your AI models. Through an easy-to-use editing and testing interface, you can ensure your prompts are effective and achieve the intended responses.

## Deployment

**Azure Marketplace**

Generative AI lab is available on Azure Marketplace as a one-click deployment within your security parameter. The one-click deployment is done in Azure Kubernetes Service (AKS) offering a fully managed Kubernetes solution that simplifies the deployment, management, and scaling of containerized applications.  I ensure high availability and security through built-in features and compliance capabilities. AKS supports automatic scaling and a consistent environment to fully utilize all the capabilities and features of Generative AI Lab. The deployed cluster can be auto This subscription offers immediate access to Visual document understanding features including tools for Optical Character Recognition, PDF preannotations, or Visual Model Training. For healthcare professionals, the platform offers specialized resources such as embeddings and models designed and tuned for healthcare data, covering tasks like entity recognition, assertion status detection, relation extraction, or entity resolution. 

And, you’re never alone in this process; professional support is always at your fingertips to assist with any questions or integrations.

### Migrate your NLP Lab Backup to Generative AI Lab 

Migrating to the new version is easy! Users using the NLP Lab can migrate their annotated data and configured settings to Generative AI Lab through our Backup and Restore feature. This process enables users to back up their projects (including data and files) from an NLP Lab server to Azure Blob or AWS S3 and then restore the configurations to a Generative AI server. For this, the following steps need to be taken: 

<iframe src="/assets/images/annotation_lab/6.0.0/BackupAndRestore.mp4" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

**Follow these steps to migrate your data**:
#### 1. Backup Data:
- Navigate to the Backup page of your Generative AI Lab instance.
- Enter backup details.
- Schedule an immediate backup via "Backup now" feature

- Monitor the backup pod status: 
```bash
kubectl get pods
```
#### 2. Verify Backup:
- Upon completion, your backed-up database and files will be visible in cloud storage.

#### 3. Restore Data:
- Download the 6.3.0 artifact and untar the contents
- Access the Kubernetes cluster of your target Generative AI Lab instance.
- Download the backed-up data from cloud storage to "artifacts/restore/database".
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

## Resource configuration
### GPU Resource Availability
If the Generative AI Lab is equipped with a GPU, the following message will be displayed on the infrastructure page:  

"**GPU Resource Available**".
 ![GenaiImage](/assets/images/annotation_lab/6.3.0/4.png)

### Visual NER Training with GPU
The Training & Active Learning page now includes a new option "**Use available GPU**" for Visual NER projects. Selecting this option enables Visual NER model training using GPU.
 
 ![GenaiImage](/assets/images/annotation_lab/6.3.0/5.png)
 
**Note**:Find CPU vs GPU Benchmarks for Visual NER model training here.
<!--- insert link to Benchmark article here --->

## Using Healthcare and Visual Document Understanding Features 

The Generative AI Lab brings support for the PAYG (Pay-As-You-Go) license option offered by John Snow Labs for the use of pre-trained medical and visual models. This comes as an additional option on top of the support for floating licenses and airgap licenses and was added for enhanced flexibility, reducing costs, and providing the mechanism for paying only for the utilized resources.

## PAYG License Features:
- **PAYG License Included in AMI Installation:** The Generative AI Lab Azure product includes a PAYG license key generated at subscription time and readily available on the License page within the AMI environment. Users do not need to worry about manually adding the license. Therefore, concerns regarding expiration or accidental deletion are eliminated. 
- **BYOL for on-premise deployments:** For on-premise deployments of the Generative AI Lab, users can buy a PAYG license from my.johnsnowlabs.com, download it, and import it to Generative AI Lab via the License page. Note that the deployment server needs to allow license heartbeat to be sent to johnsnowlabs services to validate license usage.
- **Flexible Billing:** With the PAYG license, users are billed based on only the resources they use, offering a more tailored and cost-effective pricing model.
- **Support for Multiple Servers:** PAYG license also comes with support for running multiple training and pre-annotation servers in parallel. PAYG license enables users to deploy and utilize multiple pre-annotation servers and training instances in parallel. This boosts workflow efficiency and productivity, allowing the execution of tasks simultaneously and accelerating project completion.

 ![GenaiImage](/assets/images/annotation_lab/6.3.0/6.png)

### Cost Awareness Banner for PAYG License
With the introduction of PAYG license support, proactive measures have been taken to inform users about the potential costs associated with the use of licensed features. Users will now be presented with a noticeable message banner at the top of the page, stating: "Continuous Server Usage Incurs Costs! Please check the deployed server." The message is always shown when a (preannotation/training)server is deployed in the cluster. It helps users to be aware of the fact that they are billed based on application and resource usage.

 ![GenaiImage](/assets/images/annotation_lab/6.3.0/7.gif)

By presenting this message, users are reminded to monitor their server usage and associated costs, promoting cost-conscious behavior. This feature enhances user awareness and ensures transparency regarding the cost implications of utilizing the PAYG license within Generative AI Lab.


</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

{%- include docs-annotation-pagination.html -%}
