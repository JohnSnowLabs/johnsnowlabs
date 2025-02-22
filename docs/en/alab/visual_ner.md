---
layout: docs
comment: no
header: true
seotitle: Visual NER | John Snow Labs
title: Visual NER
# permalink: /docs/en/alab/visual_ner
key: docs-training
modify_date: "2022-04-06"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
    nav: annotation-lab
---

Annotating text included in image documents (e.g. scanned documents) is a common use case in many verticals but comes with several challenges. With the new Visual NER Labeling config, we aim to ease the work of annotators by allowing them to simply select text from an image and assign the corresponding label to it.
This feature is powered by Spark OCR 3.5.0; thus a valid Spark OCR license is required to get access to it.

Here is how this can be used:
1.  Upload a valid Spark OCR license. See how to do this [here](https://nlp.johnsnowlabs.com/docs/en/alab/byol).
2.  Create a new project, specify a name for your project, add team members if necessary, and from the list of predefined templates (Default Project Configs) choose “Visual NER Labeling”.
3.  Update the configuration if necessary. This might be useful if you want to use other labels than the currently defined ones. Click the save button. While saving the project, a confirmation dialog is displayed to let you know that the Spark OCR pipeline for Visual NER is being deployed.
4.  Import the tasks you want to annotate (images).
5.  Start annotating text on top of the image by clicking on the text tokens or by drawing bounding boxes on top of chunks or image areas.
6.  Export annotations in your preferred format.

The entire process is illustrated below: 

<img class="image image__shadow" src="/assets/images/annotation_lab/2.1.0/invoice_annotation.gif" style="width:100%;"/>

## Support for multi-page PDF documents

When a valid Saprk OCR license is available, Generative AI Lab offers support for multi-page PDF annotation. The complete flow of import, annotation, and export for multi-page PDF files is currently supported.

Users have two options for importing a new PDF file into the Visual NER project
- Import PDF file from local storage;
- Add a link to the PDF file in the file attribute.

<img class="image image__shadow" src="/assets/images/annotation_lab/2.3.0/import_pdf.png" style="width:100%;"/>

After import, the task becomes available on the `Tasks Page`. The title of the new task is the name of the imported file. 

<img class="image image__shadow" src="/assets/images/annotation_lab/2.3.0/import_pdf_2.png" style="width:100%;"/>

On the labeling page, the PDF file is displayed with pagination so that annotators can annotate on the PDF document one page at a time.


## OCR and Visual NER servers

Just like (preannotation servers)[], Generative AI Lab 3.0.0 also supports the deployment of multiple OCR servers. If a user has uploaded a Spark OCR license, be it airgap or floating, OCR inference is enabled. 

To create a Visual NER project, users have to deploy at least one OCR server. Any OCR server can perform preannotation. To select the OCR server, users have to go to the Import page, toggle the OCR option and from the popup, choose one of the available OCR servers. In no suitable OCR server is available, one can be created by choosing the “Create Server” option.

![ocr_dialog](https://user-images.githubusercontent.com/26042994/161700598-fd2c8887-3bf9-4c71-9cb2-c47fc065a42a.gif)

## Visual NER Training And Preannotation

With release 3.4.0 came support for Visual NER Automated Preannotation and Model Training. 

### Visual NER Training Support

Version 3.4.0 of the Generative AI Lab offers the ability to train Visual NER models, apply active learning for automatic model training, and preannotate image-based tasks with existing models in order to accelerate annotation work.

#### License Requirements

Visual NER annotation, training and preannotation features are dependent on the presence of a Spark OCR license. Floating or airgap licenses with scope ocr: inference and ocr: training are required for preannotation and training respectively.
![licenseVisualNER](https://user-images.githubusercontent.com/33893292/181743592-62b705d5-5730-4225-9541-e1d96d997e7d.png)

### Model Training

The training feature for Visual NER projects can be activated from the Setup page via the “Train Now” button (See 1). From the Training Settings sections, users can tune the training parameters (e.g. Epoch, Batch) and choose the tasks to use for training the Visual NER model (See 3).

Information on the training progress is shown in the top right corner of the Model Training tab (See 2). Users can check detailed information regarding the success or failure of the last training.

Training Failure can occur because of:
* Insufficient number of completions
* Poor quality of completions
* Insufficient CPU and Memory
* Wrong training parameters

![VisualNERTraining](https://user-images.githubusercontent.com/33893292/181743623-c3c62d98-7cda-41a1-9d4f-0951a35b8027.png)

When triggering the training, users can choose to immediately deploy the model or just train it without deploying. If immediate deployment is chosen, then the labeling config is updated with references to the new model so that it will be used for preannotations.

![VisualNERConfig](https://user-images.githubusercontent.com/33893292/181781047-0d1e68ea-a88d-40d2-a557-11b81a459aaa.png)

#### Training Server Specification

The minimal required training configuration is 64 GB RAM, 16 Core CPU for Visual NER Training.

### Visual NER Preannotation

For running preannotation on one or several tasks, the Project Owner or the Manager must select the target tasks and can click on the Preannotate button from the upper right side of the Tasks Page. This will display a popup with information regarding the last deployment including the list of models deployed and the labels they predict.

![VisualNERPreannotationGIF](https://user-images.githubusercontent.com/33893292/181766298-28643f8f-dc6e-4ef6-a426-b454ab0a1db3.gif)

Known Limitations:

* When bulk preannotation is run on a lot of tasks, the preannotation can fail due to memory issues.
* Preannotation currently works at token level, and does not merge all tokens of a chunk into one entity.

#### Preannotation Server Specification

The minimal required training configuration is 32 GB RAM, 2 Core CPU for Visual NER Model.

### Optimized Visual NER loading for Large PDF Tasks
We’ve made improvements to how JSON data is loaded when working with PDF tasks. Previously, every time you opened a new page in a PDF, the system would load JSON data for all pages, which could slow down performance, especially with larger documents.

With this update, JSON data is now loaded more efficiently:

- **Initial Load:** JSON data is fetched and loaded only once when the task is first opened (i.e., when the first page is accessed).

- **Dynamic Loading:** When navigating to other pages, JSON data is loaded only for the page you’re viewing, rather than loading data for the entire PDF.

This update brings significant performance improvements, especially when working with larger PDFs. For example, with a 3785-page PDF, the first page now loads about 1.2 times faster, Before, moving to the second page or jumping to the 50th page would often result in an empty screen. Now, these actions are 8 times faster, taking just under 2 seconds each.

**Key Benefits:**
- Faster navigation between pages.
- Reduced memory usage by loading only the required data.
- Resolved issues with empty screens when navigating large PDFs.

This update ensures a smoother and more responsive experience when working with PDF tasks, especially for larger documents.

**Improved Zooming in Visual NER**

We've made significant improvements to the zooming functionality in Visual NER to enhance usability and give you better control over how documents are displayed.

- **More Efficient Zooming Out**
  Previously, when zooming out, both the horizontal and vertical dimensions shrank, often leaving a lot of empty white space at the top. This made it frustrating to position the page properly, requiring extra scrolling. With this update, zooming out now happens only horizontally, ensuring a better fit without unnecessary space. Now, you can get a proper view of your document without extra scrolling.

- **Better Scaling for Larger Screens**
  On larger screens, PDFs and images used to be displayed at full width (100%), making them too large and hard to view in their entirety. With this fix, documents are now automatically zoomed out so that you can see more of the page at once, making it easier to work with your data.

![6110image](/assets/images/annotation_lab/6.11.0/4.gif)
