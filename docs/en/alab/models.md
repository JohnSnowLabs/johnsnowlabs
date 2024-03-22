---
layout: docs
comment: no
header: true
seotitle: NLP Lab | John Snow Labs
title: Models
permalink: /docs/en/alab/models
key: docs-training
modify_date: "2022-10-18"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
    nav: annotation-lab
---


<div class="h3-box" markdown="1">

All the models available in the Annotation Lab are listed in this page. The models are either trained within the Annotation Lab, uploaded to Annotation Lab by _admin_ users, or downloaded from [NLP Models Hub](https://nlp.johnsnowlabs.com/models). General information about the models like labels/categories and the source (_downloaded/trained/uploaded_) is viewable. It is possible to delete any model, or redownload failed ones from the options available under the more action menu on each model.

![Model](/assets/images/annotation_lab/4.1.0/models.png)

All available models are listed in the Spark NLP Pipeline Config on the Setup Page of any project and are ready to be included in the Labeling Config for pre-annotation.


</div><div class="h3-box" markdown="1">

### Auto download of model dependencies

Starting from version 2.8.0, Annotation Lab automatically downloads all the necessary dependencies along with the model saving users valuable time from manually downloading the dependencies. Previously, users had to first download the model from the Models Hub page (e.g. `ner_healthcare_de`) and then again download the necessary embeddings required to train the model (e.g. `w2v_cc_300d`).
 
![Auto download dependencies](/assets/images/annotation_lab/4.1.0/auto_download_dependencies.gif)

</div><div class="h3-box" markdown="1">

## Custom Model Upload

Custom models can be uploaded using the Upload button present in the top right corner of the page. The labels predicted by this model need to be specified in the upload form.

![Upload models](/assets/images/annotation_lab/4.1.0/upload_models.png)

> **Note:** The models to upload need to be Spark NLP compatible.

</div>