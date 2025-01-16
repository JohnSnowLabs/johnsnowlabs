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
