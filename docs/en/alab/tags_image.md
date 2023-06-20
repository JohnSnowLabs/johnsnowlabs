---
layout: docs
comment: no
header: true
seotitle: NLP Lab | John Snow Labs
title: Image
permalink: /docs/en/alab/tags_image
key: docs-training
modify_date: "2023-06-19"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

The `Image` tag shows an image on the page. Use it for all image annotation tasks to display an image on the labeling interface. The **name** and **value** parameters in the `Image` tag are mandatory.

Suppose you have an image sample in a JSON file as shown.
```bash
{
    "image": "/static/samples/sample.jpg",
    "title": "MyTestTitle"
}
```
There are many templates within image annotation to choose from. Visual NER and Image classification are the most used among all.

### Image Classification

This task mainly uses the `Image` and `Choices` tags. You can optionally provide headers to the choices using the `Headers` tag.

![Image-classification](/assets/images/annotation_lab/xml-tags/image_classification.png)

### Visual NER Labeling

To label entities in an image, you need to create rectangular labels spanning across the entity to be labeled. To enable this, you have to use `RectangleLabels` tag that creates labeled rectangles.They are used to apply labels to bounding box semantic segmentation tasks. The **name** and **toName** parameters are mandatory.

![Visual-NER](/assets/images/annotation_lab/xml-tags/visual_ner.png)

The **zoom** and **zoomControl** parameters in the `Image` tag enable you too zoom in or out the image.