---
layout: docs
seotitle: NLP | John Snow Labs
title: Utilities for Docker
permalink: /docs/en/jsl/docker-utils
key: docs-install
modify_date: "2020-05-26"
header: true
show_nav: true
sidebar:
    nav: jsl
---
<div class="main-docs" markdown="1"><div class="h3-box" markdown="1">

Build, run and serve any johnsnowlabs model with docker, using the `serve` utilities.  
It handles licenses and dependencies and comes with a simple fast-API server.
This enables you to package any johnsnowlabs model into a docker image and serve it as a REST API.

</div><div class="h3-box" markdown="1">

## Image creation
With `nlp.build_image` you can create a docker image with any johnsnowlabs model pre-packed and ready to serve.
You just need to specify the [nlu reference to the model](https://nlp.johnsnowlabs.com/docs/en/jsl/namespace) and the **name of the output image**
Additionally, you can set the `hardware_target` to `cpu`, `gpu`, `apple_silicon` or `aarch` to package with Jar's optimized for specific hardware.

</div><div class="h3-box" markdown="1">

### Create Spark-NLP Image 
Create a spark-nlp bert image
```python
from johnsnowlabs import nlp
nlp.build_image(preloaded_model='bert',image_name='bert_img')
```

Create an image with GPU optimized builds
```python
from johnsnowlabs import nlp
nlp.build_image(preloaded_model='bert',image_name='bert_gpu_img',hardware_target='gpu')
```

</div><div class="h3-box" markdown="1">

### Create Medical NLP Image 
To create an image with a **Medical NLP model** you must provide a license in one of the ways described by the [Authorization Flows Overview](https://nlp.johnsnowlabs.com/docs/en/jsl/install_advanced#authorization-flows-overview).
It will be stored in the container and used to pre-download licensed models & dependencies during the build proces.
```python
from johnsnowlabs import nlp
# In this example with authorize via a license.json file, but there are many other ways.
nlp.build_image(preloaded_model='en.med_ner.cancer_genetics.pipeline',image_name='cancer_img', json_license_path='path/to/my/license.json')
```

</div><div class="h3-box" markdown="1">

### Create Licensed Visual NLP Image
To create an image with a **Visual NLP model** you must provide a license in one of the ways described by the [Authorization Flows Overview](https://nlp.johnsnowlabs.com/docs/en/jsl/install_advanced#authorization-flows-overview).
It will be stored in the container and used to pre-download licensed models & dependencies during the build proces.
```python
from johnsnowlabs import nlp
nlp.build_image(preloaded_model='pdf2text',image_name="pdf2text_img",visual=True)
```

</div><div class="h3-box" markdown="1">

## Serve model image as container
With `nlp.serve_container` you can serve the image you created via `nlp.build_image` as a REST API.
You can head to [http://localhost:8548/docs](http://localhost:8548/docs) to see the fast-api docs for `/predict` and `/predict_batch`.
All parameters of the [.predict() function](https://nlp.johnsnowlabs.com/docs/en/jsl/predict_api) are supported.


```python
nlp.serve_container(image_name='bert_img',container_name='bert_container',host_port=8548)
```

You can run below code to deploy **the licensed cancer container**
```python
nlp.serve_container(image_name='cancer_img',container_name='cancer_container',host_port=8549)
```


You can run below code to deploy **the licensed visual container**
```python
nlp.serve_container(image_name='pdf2text_img',container_name='pdf2text_container',host_port=8547)
```

</div><div class="h3-box" markdown="1">

### Get predictions from endpoint
The following examples demonstrate how you can get predictions in 
real-time, batch and for files. 

</div><div class="h3-box" markdown="1">

### Single String Prediction Endpoint
We can hit `/predict` on the running server with **one string**
```python
import requests
endpoint = f"http://localhost:8548/predict"
params = {"text": "Your text that you want to predict with the model goes here",}
headers = {"accept": "application/json"}
response = requests.get(endpoint, params=params, headers={"accept": "application/json"})
print(response.json())
```

</div><div class="h3-box" markdown="1">

### Batch Prediction Endpoint
We can hit `/predict_batch` on the running server with **a list of strings**

```python
import requests
endpoint = f"http://localhost:8548/predict_batch"
params = {"text": ["Your text that you want to predict with the model goes here", 'It can also be a list of strings'],}
response = requests.post(endpoint, params=params, headers={"accept": "application/json"})
print(response.json())
```

</div><div class="h3-box" markdown="1">

### Parameterized Endpoint Prediction
All parameters of the [.predict() function](https://nlp.johnsnowlabs.com/docs/en/jsl/predict_api) are supported.

```python
import requests
# Parameterized Single String Prediction
endpoint = f"http://localhost:8548/predict"
params = {
    "text": "Your text that you want to predict with the model goes here",
    "output_level": "document",
    "positions": "false",
    "metadata": "false",
    "drop_irrelevant_cols": "false",
    "get_embeddings": "false",
    "keep_stranger_features": "true",
}
response = requests.get(endpoint, params=params, headers={"accept": "application/json"})
print(response.json())


# Parameterized Batch Prediction
endpoint = f"http://localhost:8548/predict_batch"
params = {
    "text": ["Your text that you want to predict with the model goes here",
             'It can also be a list of strings'],
    "output_level": "document",
    "positions": "false",
    "metadata": "false",
    "drop_irrelevant_cols": "false",
    "get_embeddings": "false",
    "keep_stranger_features": "true",
}
response = requests.post(endpoint, params=params, headers={"accept": "application/json"})
print(response.json())
```

</div><div class="h3-box" markdown="1">

### File Prediction for Visual NLP 

We can send files to `/predict_file` to get visual models predictions for any file like PDF's and images.
Use `nlp.send_file_to_server` to send files to the server. 
If file_path begins with `https://` or `http` it will be downloaded to current working directory 
and then sent to server.

```python
from johnsnowlabs import nlp 
# assuming pdf2text_container is on port 8547
! wget https://raw.githubusercontent.com/JohnSnowLabs/nlu/master/tests/datasets/ocr/pdf/haiku.pdf
endpoint = 'http://localhost:8547/predict_file'
response = nlp.send_file_to_server('haiku.pdf',endpoint)
print(response.json())
```

</div></div>