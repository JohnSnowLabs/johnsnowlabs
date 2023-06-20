---
layout: docs
comment: no
header: true
seotitle: NLP Lab | John Snow Labs
title: Audio
permalink: /docs/en/alab/tags_audio
key: docs-training
modify_date: "2023-06-19"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

The audio template is split into three parts: audio classification, Emotion segmentation, and transcription. To play the audio, you need an `Audio` tag which requires a **name** and a **value** parameter.

### Audio Classification

Suppose you have a sample JSON which contains some audio that you wish to classify (This input is set as default when you click on the template in NLP Lab):

```bash
{
    "audio": "/static/samples/game.wav",
    "title": "MyTestTitle"
}
```
The configuration for classification task can look as shown below.

![Audio-classification](/assets/images/annotation_lab/xml-tags/audio_classification.png)

The preview should look as shown below.

![Audio-preview-classification](/assets/images/annotation_lab/xml-tags/audio_preview_1.png)

### Emotion Segmentation

This is a labeling task, and requires the `Label` tags to assign variables. The configuration is very straightforward, as shown below.

![Emotion-segment](/assets/images/annotation_lab/xml-tags/emotion_segment.png)

### Audio Transcription

The transcription task is further divided into two parts - either by transcription per region or transcripting whole audio. If you are transcripting per region then it will become both labeling and transcription task. For this case the configuration would look as shown below.

![Audio-transcription](/assets/images/annotation_lab/xml-tags/audio_transcription.png)

As shown in the image above, audio transcription requires a `TextArea` tag to enable a text box. The parameters **name** and **toName** are mandatory. For transcription of whole audio, the `Label` tags from the above image will disappear.