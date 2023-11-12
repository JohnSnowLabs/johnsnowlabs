---
layout: docs
comment: no
header: true
seotitle: NLP Lab | John Snow Labs
title: Video
permalink: /docs/en/alab/tags_video
key: docs-training
modify_date: "2023-06-20"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

The video template is split into two parts: video classification and video timeline segmentation. To play a video, you need a `HyperText` tag which requires the **name** parameter and **value** parameter. 

### Video Classification

Since it is a classification type, the configuration should use `Choice` tags to assign variables. For example, say that you have a sample task and you wish to classify that video as awesome or groove, inscribed in a JSON like this:

```bash
{
    "title": "MyTestTitle",
    "video": "<video src='/static/samples/opossum_snow.mp4' width=100% controls>"
}
```
The simplest configuration in this case will look as shown below.

![video_classification](/assets/images/annotation_lab/xml-tags/vid_classification.png)

### Video Timeline Segmentation

This is a labeling task, and thus requires the use of `Label` tags to assign variables. For example, you have a sample task with a video and it's corresponding audio, and you wish to label segments. The sample JSON looks like this:

```bash
{
    "title": "MyTestTitle",
    "video": "<video src='/static/samples/opossum_snow.mp4' width=100% controls>",
    "videoSource": "/static/samples/game.wav"
}
```
The configuration in this case is shown below.

![video_timeline_segmentation](/assets/images/annotation_lab/xml-tags/vid_timeline_segment.png)

The `background` parameter refers to the color of the label. From above, you could see that the labels will work on the audio encryption since the name parameter in the `AudioPlus` tag is the same as the toName parameter in the `Labels` tag.