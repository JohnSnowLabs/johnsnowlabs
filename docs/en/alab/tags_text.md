---
layout: docs
comment: no
header: true
seotitle: NLP Lab | John Snow Labs
title: Text
permalink: /docs/en/alab/tags_text
key: docs-training
modify_date: "2023-06-19"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

The `Text` tag shows text that can be labeled. The text template is divided into the following segments:
- Information extraction: Includes NER and extracting relations among entities.
- Classification: Includes text classification and multi-class classification.
- Text summarization.

### Information Extraction

For simple NER related tasks, the configuration just needs the `Text` and `Labels` tags. The `Labels` tag provides a set of labels for labeling regions in your tasks. Use the `Labels` tag to create a set of labels that can be assigned to identified region and specify the values of labels to assign to regions. For example, you have the following JSON to label, as shown below.

```bash
{
    "text": "The patient is a pleasant 17-year-old gentleman who was playing basketball today in gym. Two hours prior to presentation, he started to fall and someone stepped on his ankle and kind of twisted his right ankle and he cannot bear weight on it now. It hurts to move or bear weight. No other injuries noted. He does not think he has had injuries to his ankle in the past. He was given adderall and accutane.",
    "title": "MyTestTitle"
}
```
The configuration in this case looks as shown below.

![NER-labels](/assets/images/annotation_lab/xml-tags/NER_labels.png)

The **model** parameter in the `Label` tag must be specified whenever a pre-trained model is used in the project for pre-annotation purposes. It is automatically defined when a model is chosen from **Reuse Resources**.

For the case of relation extraction, the configuration additionally needs a `Relations` tag apart from `Text` and `Labels`. For the same input, the configuration would look as shown below.

![Relations-extraction](/assets/images/annotation_lab/xml-tags/relation_extraction.png)

### Classification

For a classification task, the configuration needs the `Text` and `Choices` tags. For instance, you have the input JSON as shown below. The `Choices` tag is used to create a group of choices (a set of `Choice` tags), with radio buttons or checkboxes. It can be used for single or multi-class classification.

```bash
{
    "text": "The patient is a pleasant 17-year-old gentleman who was playing basketball today in gym. Two hours prior to presentation, he started to fall and someone stepped on his ankle and kind of twisted his right ankle and he cannot bear weight on it now. It hurts to move or bear weight. No other injuries noted. He does not think he has had injuries to his ankle in the past. He was given adderall and accutane.",
    "title": "MyTestTitle"
}
```

For simple single-class classification, the configuration is shown below.

![Classification](/assets/images/annotation_lab/xml-tags/classification.png)

In the case of multi-class classification, the configuration would look as shown below.

![multi-class](/assets/images/annotation_lab/xml-tags/multi-class-classification.png)

### Text summarization

For a simple text summarization, the configuration just needs the `Text` and `TextArea` tags. The `TextArea` tag is used to display a text area for the user input. It is mainly used for transcription, paraphrasing, or captioning task.

![Text-summarization](/assets/images/annotation_lab/xml-tags/text_summarization.png)