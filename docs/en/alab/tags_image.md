---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Image
permalink: /docs/en/alab/tags_image
key: docs-training
modify_date: "2023-06-21"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

The `Image` tag shows an image on the page. Use it for all image annotation tasks to display an image on the labeling interface. The **name** and **value** parameters in the `Image` tag are mandatory.

Suppose you have an image sample in a JSON file as shown.
```bash
{
    "image": "/static/samples/sample.jpg",
    "title": "MyTestTitle"
}
```
There are many templates within image annotation to choose from. Visual NER and Image classification are the most used among all.

</div><div class="h3-box" markdown="1">

### Image Classification

This task mainly uses the `Image` and `Choices` tags. You can optionally provide headers to the choices using the `Headers` tag.

![Image-classification](/assets/images/annotation_lab/xml-tags/image_classification.png)

</div><div class="h3-box" markdown="1">

### Visual NER Labeling

To label entities in an image, you need to create rectangular labels spanning across the entity to be labeled. To enable this, you have to use `RectangleLabels` tag that creates labeled rectangles.They are used to apply labels to bounding box semantic segmentation tasks. The **name** and **toName** parameters are mandatory.

![Visual-NER](/assets/images/annotation_lab/xml-tags/visual_ner.png)

The **zoom** and **zoomControl** parameters in the `Image` tag enable you too zoom in or out the image.

</div>

### Identify and Validate Checkboxes with Precision
Version 6.9.0 introduces a new project type called **Checkbox Detection**. With the new update, users can now use the model offered by Generative AI Lab to identify checkboxes in the tasks, including the **checked** and **unchecked** status in the respective tasks.

This project type can be selected from the **Content Type** page under the **Image** tab during project setup. The default model associated with Checkbox Detection is automatically downloaded from the **Models Hub** page and added to the project configuration.

![690image](/assets/images/annotation_lab/6.9.0/1.png)

After the project is configured, users can add relevant tasks and leverage the model to detect checkboxes and their respective checked and unchecked statuses.

![690image](/assets/images/annotation_lab/6.9.0/2.png)

This new update integrates seamlessly with the existing workflow, ensuring no changes or disruptions to the current application processes.

This model can not currently be combined with other models.

### Detect and Validate Handwritten Text and Signatures
This update continues with the **Handwritten Text and Signature Detection** project type. This new feature enables the automatic identification and annotation of handwritten text and signatures within documents, using John Snow Lab's Visual NLP Library. The new project type can be selected from the **Content Type** page under **Image** tab during project configuration. Upon selection, the default model for Handwritten Text and Signature Detection is automatically downloaded from the **Models Hub** and integrated into the project configuration.

![690image](/assets/images/annotation_lab/6.9.0/3.png)

Users can then add relevant tasks to the project and use the model to identify and annotate handwritten content and signatures in documents efficiently.

![690image](/assets/images/annotation_lab/6.9.0/4.png)

This feature doesn't change the existing application workflow, and can not be combined with other models at this time.

## View Text alongside images, and Optimized Image Loading in Visual NER
Generative AI Lab 6.11 brings an Image-Text Side-by-Side Annotation project, allowing users to view the original image or PDF alongside its OCR-extracted text for easier annotation. It also includes optimized Visual NER for faster PDF processing, enhanced zoom functionality, and a new licensing model for on-premises deployments. 

Other minor improvements have been made to Generative AI Lab, specifically to model training and de-identification.

## Annotate while referencing Orginal Documents
This feature improves visibility for image-based documents by displaying both the image/PDF and its OCR-extracted text side by side. Users can now annotate more efficiently while maintaining a visual reference. While Generative AI Lab has offered annotation on top of Image and PDF formats for quite some time, there was a gap in annotating large amounts of data on top of the original document, as there was not enough space to adequately address more robust annotation projects.

**Image on the Left, OCR Text on the Right**: By Selecting this project type, users can now view the image/PDF document on the left side of the interface and its corresponding OCR-extracted text on the right side.  

 **Paginated Documents**: All document pages are paginated, allowing users to navigate the document effortlessly. 

Image and PDF documents now support all text-based annotation features—including NER, assertion, relations, resolvers, and lookup code annotation—and allow OCR text annotation.
### Key Features  

### How to Configure the Project  
1. **Select the Project Template**:  
   - Navigate to the **Image** tab and choose the **Image & Text Side-By-Side Annotation** template.  
   - Save the configuration to proceed.  

2. **Add Models to the Reuse Resource Page**:  
   - Click **Next** to move to the Reuse Resource page.  
   - Add the required models, such as NER, relation, and assertion models, to the project.  

3. **Configure Individual Labels**:  
   - Click **Next** again to access the label configuration page.  
   - Click on individual labels to add lookup data or resolver models.  

4. **Save and Deploy the Preannotation Server**:  
   - Once all configurations are complete, save the project.  
   - Deploy the preannotation server to start using the project.  

For a visual guide, refer to the GIF below that demonstrates the configuration process step-by-step:  

![6110image](/assets/images/annotation_lab/6.11.0/1.gif)


### How to Use Preannotation  

After deploying the preannotation server, follow these steps to preannotate your documents:  

1. **Import a PDF or Image**:  
   - Go to the **Task Page** and navigate to the **Import Page**.  
   - Import the PDF or image you wish to annotate.  

2. **Automatic OCR Processing**:  
   - The imported document will automatically pass through our OCR process.  
   - Once OCR is complete, a task will be generated for the document.  

3. **Preannotate the Task**:  
   - Use the deployed preannotation server to preannotate the task.  
   - Alternatively, click on the task to annotate it manually.  

4. **Automatic NER Label Projection**:  
   - As you annotate the text side, NER labels are automatically projected onto the image side for visual reference.  
   - This ensures a seamless and intuitive annotation experience.  

For a visual guide, refer to the GIF below that demonstrates the pre-annotation/annotation process step-by-step:  

![6110image](/assets/images/annotation_lab/6.11.0/2.gif)


#### **Image with Text Annotation (Performance-Optimized)**

The second project template is similar to the first but is optimized for speed and larger multi-page PDFs. It maintains the side-by-side view found in the above project without the NER labels appearing on the image. This is to improve annotation speed and reduce server resources. This will work better for high-volume document processing. 

![6110image](/assets/images/annotation_lab/6.11.0/3.png)

### Advanced Capabilities
- **Model Training:** Train NER, assertion, and relation models seamlessly in both project types.
- **Rule-Based & Prompt-Based Annotation:** Utilize rules and prompts for efficient labeling.
- **Support for Resolvers & ICD-10 Coding:** Ensures compatibility with all text-based annotation features.
