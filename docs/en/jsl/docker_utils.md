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
<div class="main-docs" markdown="1">
Build, run and serve any johnsnowlabs model with docker, using the `serve` utilities.  
It handles licenses and dependencies and comes with a simple fast-API server.
This enables you to package any johnsnowlabs model into a docker image and serve it as a REST API.


## Create image
With `nlp.build_image` you can create a docker image with any johnsnowlabs model pre-packed and ready to serve.
You just need to specify the [nlu reference to the model](todo) and the **name of the output image**
```python
from johnsnowlabs import nlp
nlp.build_image(preloaded_model='bert',image_name='bert_img')
```

Additionally, you can set the `hardware_target` to `cpu`, `gpu`, `apple_silicon` or `aarch` to package with Jar's optimized for specific hardware. 
```python
from johnsnowlabs import nlp
nlp.build_image(preloaded_model='bert',image_name='bert_gpu_img',hardware_targert='gpu')
```

To Create image with a **licensed model**
To run licensed models in a container you must provide a license in one of the ways described by the [Authorization Flows Overview]
It will be stored in the container and used to pre-download licensed models & dependencies during the build proces.
```python
from johnsnowlabs import nlp
# In this example with authorize via a license.json file, but there are many other ways.
nlp.build_image(preloaded_model='en.med_ner.cancer_genetics.pipeline',image_name='cancer_img', json_license_path='path/to/my/license.json')
```


## Run image and serve

With `nlp.serve_container` you can serve the image you created via `nlp.build_image` as a REST API.
You can head to [http://localhost:8548/docs](http://localhost:8548/docs) to see the fast-api docs for `/predict` and `/predict_batch`.
All parameters of the [.predict() function](https://nlp.johnsnowlabs.com/docs/en/jsl/predict_api) are supported.


```python
nlp.serve_container(image_name='bert_img',container_name='bert_container',host_port=8548)
```

You can run below code to deploy **the licensed cancer container**
```python
nlp.serve_container(image_name='cancer_img',container_name='cancer_container',host_port=8548)
```


## Single String Prediction Endpoint
We can hit `/predict` on the running server with **one string**
```python
import requests
port = 8548
url = f"http://localhost:{port}/predict"
params = {"text": "Your text that you want to predict with the model goes here",}
headers = {"accept": "application/json"}
response = requests.get(url, params=params, headers={"accept": "application/json"})
print(response.json())
```

## Batch Prediction Endpoint
We can hit `/predict_batch` on the running server with **a list of strings**

```python
import requests
port = 8548
url = f"http://localhost:{port}/predict_batch"
params = {"text": ["Your text that you want to predict with the model goes here", 'It can also be a list of strings'],}
response = requests.post(url, params=params, headers={"accept": "application/json"})
print(response.json())
```

## Parameterized Endpoint Prediction
All parameters of the [.predict() function](https://nlp.johnsnowlabs.com/docs/en/jsl/predict_api) are supported.

```python
import requests
port = 8548

# Parameterized Single String Prediction
url = f"http://localhost:{port}/predict"
params = {
    "text": "Your text that you want to predict with the model goes here",
    "output_level": "document",
    "positions": "false",
    "metadata": "false",
    "drop_irrelevant_cols": "false",
    "get_embeddings": "false",
    "keep_stranger_features": "true",
}
response = requests.get(url, params=params, headers={"accept": "application/json"})
print(response.json())


# Parameterized Batch Prediction
url = f"http://localhost:{port}/predict_batch"
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
response = requests.post(url, params=params, headers={"accept": "application/json"})
print(response.json())
```



## Full Example

```python


```



</div>