---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Pre-Annotation
permalink: /docs/en/alab/preannotation
key: docs-training
modify_date: "2022-12-02"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

<style>
bl {
  font-weight: 400;
}

es {
  font-weight: 400;
  font-style: italic;
}
</style>

<div class="h3-box" markdown="1">

Generative AI Lab offers out-of-the-box support for <es>Named Entity Recognition</es>, <es>Classification</es>, <es>Assertion Status</es>, and <es>Relations</es> preannotations. These are extremely useful for bootstrapping any annotation project as the annotation team does not need to start the labeling from scratch but can leverage the existing knowledge transfer from domain experts to models. This way, the annotation efforts are significantly reduced.

To run pre-annotation on one or several tasks, the <es>Project Owner</es> or the <es>Manager</es> must select the target tasks and click on the `Pre-Annotate` button from the top right side of the <es>Tasks</es> page. It will display a popup with information regarding the last deployment of the model server with the list of models deployed and the labels they predict.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/preannotation_ner.gif" style="width:100%;"/>
![Generative AI Lab](/assets/images/annotation_lab/4.10.0/add_video_type.png "lit_shadow")

This information is crucial, especially when multiple users are doing training and deployment in parallel. So before doing preannotations on your tasks, carefully check the list of currently deployed models and their labels.

If needed, users can deploy the models defined in the current project (based on the current Labeling Config) by clicking the _Deploy_ button. After the deployment is complete, the preannotation can be triggered.

<img class="image image__shadow image__align--center" src="/assets/images/annotation_lab/4.1.0/preannotate_dialog.png" style="width:40%;"/>
![Generative AI Lab](/assets/images/annotation_lab/4.10.0/add_video_type.png "lit_shadow")

Since <bl>Generative AI Lab 3.0.0</bl>, multiple preannotation servers are available to preannotate the tasks of a project. The dialog box that opens when clicking the _Pre-Annotate_ button on the <es>Tasks</es> page now lists available model servers in the options. <es>Project Owners</es> or <es>Managers</es> can now select the server to use. On selecting a model server, information about the configuration deployed on the server is shown on the popup so users can make an informed decision on which server to use.

In case a pre-annotation server does not exist for the current project, the dialog box also offers the option to deploy a new server with the current project's configuration. If this option is selected and enough resources are available (infrastructure capacity and a license if required) the server is deployed, and pre-annotation can be started. If there are no free resources, users can delete one or several existing servers from <es>Clusters</es> page under the <es>Settings</es> menu.

![preannotation_dialog](https://user-images.githubusercontent.com/26042994/161700555-1a46ef82-1ed4-41b8-b518-9c97767b1469.gif)

Concurrency is not only supported between pre-annotation servers but also between training and pre-annotation. Users can have training running on one project and pre-annotation running on another project at the same time.

</div><div class="h3-box" markdown="1">

## Pre-annotation Approaches

### Pretrained Models

On the <es>Predefined Labels</es> step of the <es>Project Configuration</es> page we can find the list of available models with their respective prediction labels. By selecting the relevant labels for your project and clicking the `Add Label` button you can add the predefined labels to your project configuration and take advantage of the Spark NLP auto labeling capabilities.

In the example below, we are reusing the `ner_posology` model that comes with 7 labels related to drugs.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/pretrained_models.png" style="width:100%;"/>
![Generative AI Lab](/assets/images/annotation_lab/4.10.0/add_video_type.png "lit_shadow")

</div><div class="h3-box" markdown="1">

In the same manner classification, assertion status or relation models can be added to the project configuration and used for pre-annotation purpose.

Starting from version 4.3.0, Finance and Legal models downloaded from the Models Hub can be used for pre-annotation of NER, assertion status and classification projects. Visual NER models can now be downloaded from the NLP Models Hub, and used for pre-annotating image-based documents. Once you download the models from the Models Hub page, you can see the model's label in the <es>Predefined Label</es> tab on the project configuration page.

<img class="image image__shadow" src="https://user-images.githubusercontent.com/45035063/203519370-04cd1b4a-d02d-43ee-aa1b-3b6adf10ebb7.gif" style="width:100%;"/>
![Generative AI Lab](/assets/images/annotation_lab/4.10.0/add_video_type.png "lit_shadow")

</div><div class="h3-box" markdown="1">

## Text Pre-annotation

Pre-annotation is available for projects with text contents as the tasks. When you setup a project to use existing Spark NLP models for pre-annotation, you can run the designated models on all of your tasks by pressing the `Pre-Annotate` button on the top-right corner of the <es>Tasks</es> page.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/text_preannotation.png" style="width:100%;"/>
![Generative AI Lab](/assets/images/annotation_lab/4.10.0/add_video_type.png "lit_shadow")

As a result, all predicted labels for a given task will be available in the <es>Prediction</es> widget on the Labeling page. The predictions are not editable. You can only view and navigate those or compare those with older predictions. However, you can create a new completion based on a given prediction. All labels and relations from such a new 

</div><div class="h3-box" markdown="1">

### Re-purpose text-based NER models for PDF and images 
Generative AI Lab 5.8 introduces a groundbreaking enhancement to Visual NER projects by allowing users to leverage the vast library of pre-trained NER models specific for text content [6,600+ models available on the Models Hub](https://nlp.johnsnowlabs.com/models?task=Named+Entity+Recognition), for the pre-annotation of PDF or image tasks. This addition not only expands pre-annotation options but also significantly streamlines the annotation process, saving users precious time and effort. 
With this game-changing enhancement, users can now:
- **Effortlessly Jumpstart Data Preparation Projects:** Quickly initiate data preparation projects for training small Visual NER models tailored to specific tasks, reducing the time and resources required for manual labeling.
- **Utilize Existing Domain-Specific Expertise** Leverage the extensive library of NER models, including domain-specialized models that were previously confined to text-based tasks. This opens up new possibilities for processing image and PDF documents with specialized NER models, enhancing the accuracy and effectiveness of pre-annotation.
- **Streamline Workflow with Pre-trained Models:** Eliminate the need for training Visual NER models just to predict specific labels when those are already available in existing text processing models. Simply select the relevant pre-trained NER model(s) you need directly from the Generative AI Lab library and seamlessly integrate them into your projects.

</div><div class="h3-box" markdown="1">

## Effortlessly Pre-annotate PDF or Image Documents with NER Models
Configuring your Visual NER project to use text-specific NER models for pre-annotation is a breeze:
- **Project Configuration:** Begin by creating a new project and selecting the Visual NER Template during configuration. This sets the stage for seamless integration of NER models into your project.
- **NER Model Selection:** From the Re-use Resource page, navigate through the vast library of NER models and choose the one that best suits your project's requirements. Once selected, save the project configuration to apply the chosen model.
- **OCR Document Import:** Import the OCR documents containing the data you wish to pre-annotate. These documents can be in PDF or image format, catering to a wide range of document types.
- **Pre-annotation Automation:** Leverage the selected NER model to automatically pre-annotate the imported OCR documents. This eliminates the need for manual labor and significantly expedites the pre-annotation process.
- **Accuracy Verification:** After pre-annotation, meticulously review the automatically generated annotations to ensure accuracy and address any discrepancies.

![1](/assets/images/annotation_lab/5.8.0/1.gif)

This new feature empowers users to seamlessly integrate NER models into their Visual NER projects, fostering greater flexibility and efficiency in document annotation workflows within Generative AI Lab. By leveraging the power of NER models, users can streamline pre-annotation processes, reduce training time, and achieve enhanced accuracy, ultimately accelerating their data preparation efforts.

</div><div class="h3-box" markdown="1">

### Rules

Pre-annotation of NER projects can also be done using <es>Rules</es>. Rules are used to speed up the manual annotation process. Once a rule is defined, it is available for use in any project. However, for defining and running the rules we will need a <bl>[Healthcare NLP](/docs/en/licensed_install)</bl> license.

In the example below, we are reusing the available rules for pre-annotation.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/available_rules.png" style="width:100%;"/>
![Generative AI Lab](/assets/images/annotation_lab/4.10.0/add_video_type.png "lit_shadow")

Read more on how to create rules and reuse them to speed up the annotation process [here](https://medium.com/annotation-lab/using-rules-to-jump-start-text-annotation-projects-1-3-john-snow-labs-8277a9c7fbcb).

completion are now editable.

</div><div class="h3-box" markdown="1">

## Visual Pre-annotation

For running pre-annotation on one or several tasks, the <es>Project Owner</es> or the <es>Manager</es> must select the target tasks and can click on the `Pre-Annotate` button from the upper right side of the <es>Tasks</es> Page. It will display a popup with information regarding the last deployment of the model server, including the list of models deployed and the labels they predict.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/visual_ner_preannotation.gif" style="width:100%;"/>
![Generative AI Lab](/assets/images/annotation_lab/4.10.0/add_video_type.png "lit_shadow")

**Known Limitations:**

1. When bulk pre-annotation runs on many tasks, the pre-annotation can fail due to memory issues.
2. Pre-annotation currently works at the token level, and does not merge all tokens of a chunk into one entity.

</div><div class="h3-box" markdown="1">

### Pre-annotation using Prompts in Visual NER project
Generative AI Lab 5.9.0 expands pre-annotation capabilities for Visual NER projects with added support for pre-annotation using Prompts. Users can now pre-annotate tasks in Visual NER projects using zero-shot prompts, significantly enhancing the scope for pre-annotation along with efficiency and accuracy.

In previous versions, the use of prompts was limited to only in text-based projects. With this version, the scope has been expanded, allowing users to leverage prompts for pre-annotation in their PDF and image-based projects as well.

By incorporating zero-shot prompts, users can achieve efficient and accurate pre-annotation without the need for manual intervention.

</div><div class="h3-box" markdown="1">

### Configure and Pre-annotate tasks using Prompts:
- Create a Visual NER Project
- Navigate to Reuse-Resource Page and add desired zero shot prompts (relation prompts and external prompts are not supported, currently)
- Once project configuration is saved, pre-annotate the tasks using the prompt.

![PromptInVisner](/assets/images/annotation_lab/5.9.0/11.gif)

This new feature streamlines the pre-annotation process and extends the benefits of prompts to Visual NER projects, empowering users to annotate tasks more effectively across various document types.

</div><div class="h3-box" markdown="1">

### Pre-annotation using and Rules Visual NER project
Version 5.9.0 introduces support for using Rules for pre-annotation capabilities of Visual NER projects. Users can now pre-annotate tasks in Visual NER projects using rules, extending the benefits of automated pre-annotation to a wider range of document types.

Previously, rules were only available for use in text-based projects. However, with this version, the scope has been expanded to include Visual NER projects. Users can now leverage rules for pre-annotation in PDF and image-based projects, providing greater flexibility and efficiency in annotation workflows, allowing users to utilize rules to automatically annotate tasks in Visual NER projects.

</div><div class="h3-box" markdown="1">

### Configure and Pre-annotate tasks using Rules:
- Create a Visual NER Project
- Navigate to Reuse-Resource Page and add desired rules.
- Once project configuration is saved, pre-annotate the tasks using the rules.

![RulesInVisner](/assets/images/annotation_lab/5.9.0/12.gif)

</div><div class="h3-box" markdown="1">

## Pipeline Limitations

Loading too many models in the pre-annotation server is not memory efficient and may not be practically required. Starting from version <bl>1.8.0</bl>, Generative AI Lab supports maximum of five different models to be used for the pre-annotation server deployment.

Another restriction for Generative AI Lab versions older than 4.2.0 is that two models trained on different embeddings cannot be used together in the same project. The Labeling Config will throw validation errors in any of the cases above, and we cannot save the configuration preventing pre-annotation server deployment.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/5_models.png" style="width:100%;"/>
![Generative AI Lab](/assets/images/annotation_lab/4.10.0/add_video_type.png "lit_shadow")

</div>