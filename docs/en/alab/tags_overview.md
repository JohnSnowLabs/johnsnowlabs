---
layout: docs
comment: no
header: true
seotitle: NLP Lab | John Snow Labs
title: Overview
permalink: /docs/en/alab/tags_overview
key: docs-training
modify_date: "2023-06-19"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

NLP Lab enables the utilization of XML-like tags to configure the labeling interface. NLP Lab contains three distinct tag types for labeling management:

- Object tags serve for data types, presenting labeled elements within a task, which can be labeled as video, audio, HTML, images, PDF, and text.
- Control tags facilitate the annotation of objects. For instance, labels are employed in semantic and named entity tasks, and choices for classification tasks inside NLP Lab.
- Visual tags allow for changes to the visual elements of the labelling interface, giving control over the presentation of particular labeling choices or the presence of a header.

## Custom Labeling Configuration

A name parameter is required for each control and object tag. Every control tag also needs a toName parameter that matches the name parameter of the object tag in the configuration. Suppose you wish to assign labels to text for a named entity recognition task. In that case, you could employ the following labeling configuration:

![NER-xml-tag](/assets/images/annotation_lab/xml-tags/NER_labels.png)

In this case, text is annotated using the Label tags in combination with the Text tag. Multiple control and object tags may be used in the same configuration by creating linkages between them using names.

### Variables

All object tags, as well as some control and visual tags, support variables within their arguments. Using variables enables for the creation of a labeling configuration, while also allowing for the control of given information on the labeling interface based on data in a given task.
To use a variable, use it with the value parameter of a tag and specify it using the $ sign and the name of the field that you want to reference. For example, if you have a sample if you have a sample task which contains some partial JSON, then the configuration should look something like this:

![Headers-tag](/assets/images/annotation_lab/xml-tags/header_variables.png)

When you look on the preview window, you can see the header set on top of the labels/choices. 