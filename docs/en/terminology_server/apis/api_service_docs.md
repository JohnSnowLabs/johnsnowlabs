---
layout: docs
header: true
seotitle: Terminology Server | John Snow Labs
title: Terminology Server 
permalink: /docs/en/terminology_server/api_docs
key: docs-term-server
modify_date: "2025-04-01"
show_nav: true
sidebar:
    nav: term-server
---

## API Usage and Dcumentation

The API service allows **seamless integration** with your applications, enabling you to leverage our platform’s capabilities.

After deploying the Terminology Server in your environment, you can access the API right away as described in the [API Service Access](api_service_access.md) 

Below are few examples of how to invoke the API, for the full documentation including respose sampls, visit the public online [Terminology Server API Code Sample Documentation](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/products/term_server/terminology_api.ipynb).

**Search API sample usage**
```
import requests
import json

def search(chunks, 
            search_type=None, 
            vocabulary_id=[], 
            validity=None,
            topk=20,
            standard_concept=[], 
            domain_id=[], 
            source=[], 
            concept_class_id=[], 
            filter_by_valueset=False,
            valueset_metadata_ids=[], 
            source_vocabulary=None,
            target_vocabulary=None):
    url = f"{base_url}/search"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    payload = {
        "chunks": chunks,
        "search_type": search_type,
        "vocabulary_id": vocabulary_id,
        "validity": validity,
        "topk": topk,
        "standard_concept": standard_concept,
        "domain_id": domain_id,
        "source": source,
        "concept_class_id": concept_class_id,
        "filter_by_valueset": filter_by_valueset,
        "valueset_metadata_ids": valueset_metadata_ids,
        "source_vocabulary": source_vocabulary,
        "target_vocabulary": target_vocabulary
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()
```
**Basic Search Example**
```
search(chunks=["diabetes"])
```

**Exact match search**
```
search(chunks=["viral hepatitis"], 
        topk=10, 
        search_type="exact",
        validity="true",
        domain_id=["Condition", "Observation"],
        vocabulary_id=["ICD10", "ICD9"],
        )
```

**Semantic Search**
```
search(chunks=["viral hepatitis"], 
        topk=10, 
        search_type="semantic",
        validity="true",
        domain_id=["Condition", "Observation"],
        vocabulary_id=["ICD10", "ICD9"],
        )
```

**Code to Code Mapping**

Provides mapping from one code system (source) to another code system (target).

```
import requests

def map_one_code_to_another(source_codes, source_vocabulary=None, target_vocabulary=None):
    url = f"{base_url}/code_map"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    payload = {
        "concept_codes": source_codes,
        "source_vocabulary": source_vocabulary,
        "target_vocabulary": target_vocabulary
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()
```
User can provide single or multiple codes as per their need.
```
source_codes = ["E11", "E14"]
map_one_code_to_another(source_codes=source_codes)
```
Filter by source and/or target code system
```
source_codes = ["E11", "E14"]
source_vocabulary = "ICD10"

map_one_code_to_another(source_codes=source_codes, source_vocabulary=source_vocabulary)
```
