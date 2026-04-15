---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Cluster Management
permalink: /docs/en/alab/cluster_management
key: docs-training
modify_date: "2025-11-27"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

### Management of Preannotation and Training Servers

Generative AI Lab gives users the ability to view the list of all active servers. Any user can access the _Clusters_ page by navigating to `Settings > Clusters`. This page provides the following details.

- A summary of the status/limitations of the current infrastructure to run Spark NLP for Healthcare training jobs and/or pre-annotation servers.
- Ability to delete a server and free up resources when required, so that another training job and/or pre-annotation server can be started.
- Shows details of the server
  - **Server Name:** The name of server that can help identify it while running pre-annotation or importing files.
  - **License Used/Scope:** The license that is being used in the server and its scope.
  - **Usage:** Let the user know the usage of the server. A server can be used for pre-annotation, training, or OCR.
  - **Status:** Status of training and pre-annotation servers.
  - **Deployed By:** The user who deployed the server. This information might be useful for contacting the user who deployed a server before deleting it.
  - **Deployed At:** Shows when the server was deployed.

![server_page](/assets/images/annotation_lab/4.1.0/server_management.gif)

By default, only 1 server can be initialized for either pre-annotation or training even if there are multiple licenses present. To enable more than 1 servers to be initialized update the below configuration parameter in `annotationlab-updater.sh` script inside the artifacts folder and then re-run it.

```bash
model_server.count=<NUMBER_OF_SERVER_TO_INITIALIZE>
airflow.model_server.count=<NUMBER_OF_SERVER_TO_INITIALIZE>
```

To run the script:

```
sudo ./annotationlab-updater.sh
```

<br>

#### Status of Training and Preannotation Server

A new column, status, is added to the Clusters page that gives the status of training and pre-annotation servers. The available pre-annotation server statuses are:

- Idle
- Busy
- Stopped

Users can visualize which servers are busy and which are idle. It is very useful information when the user intends to deploy a new server in replacement of an idle one. In this situation, the user can delete an idle server and deploy another pre-annotation/ training server.
This information is also available on the pre-annotation popup when the user selects the deployed server to use for pre-annotation.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/server_status.png" style="width:100%;"/>

Also, if any issues are encountered during server initialization, those are displayed on the tooltip accessible via mouse-over. Depending on the issue, changes might be required in the infrastructure settings, and the user will have to manually redeploy the training/pre-annotation server.

<img class="image image__shadow" src="/assets/images/annotation_lab/serverStatus2.png" style="width:100%;"/>

### Enhanced Cluster Management Dashboard 

Version 8.0 introduces an enhanced Cluster Management Dashboard with improved visibility into system resources and deployed configurations.

#### System Resource Summary

A new resource summary section appears at the top of the Cluster page, displaying real-time usage for:
- **Memory:** Consumed vs. total capacity
- **CPU:** Core usage across active deployments
- **Storage:** Storage consumption and availability

Resource metrics are calculated dynamically across all active servers, enabling at-a-glance capacity monitoring.

![Cluster Management Dashboard showing system resources and deployed servers](/assets/images/annotation_lab/8.0.0/3.png "lit_shadow")

#### Configuration Visibility

Server configurations are now displayed directly in the Cluster table using inline tags:
- **Pre-annotation servers:** Show deployed models, rules, and prompts
- **Medical Terminology servers:** Show deployed terminologies (ICD-10, LOINC, CPT, etc.)

This provides immediate visibility into which assets are deployed on each server without requiring additional navigation.

#### Enhanced License Information

The license banner provides contextual information based on license type:
- **Airgap License:** No deployment limit (constrained by system resources only)
- **Floating License:** Shows concurrent job slots with real-time usage
- **Universal License:** Displays credit-based usage with consumed and available credits

> **Note:** License metrics reflect only servers deployed within the current instance. Usage from other instances is not included.

#### Resource Allocation Details

Each server entry now includes explicit resource allocation:
- Assigned memory
- Allocated CPU cores
- Storage capacity

Combined with the resource summary, this enables administrators to understand how resources are distributed and plan capacity effectively.