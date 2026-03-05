---
layout: docs
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Generative AI Lab 7.8.2
permalink: /docs/en/alab/annotation_labs_releases/release_notes_7_8_2
key: docs-licensed-release-notes
modify_date: 2026-03-05
show_nav: true
sidebar:
    nav: annotation-lab
---

<div class="h3-box" markdown="1">



### Important Change

- **Kibana Authentication Requirement**

   Access to Kibana now requires authentication.
   Use the elastic username and retrieve the password from the Kubernetes secret using the following command:

   ```bash
   kubectl get secret annotationlab-elasticsearch-master-credentials --template={{.data.password}} | base64 --decode; echo
   ```


### Bug Fixes

- **Kibana Dashboard Access After Upgrade**

   In certain scenarios, access to Kibana dashboards could become unavailable after upgrading the platform. Dashboard access behavior has been corrected to ensure Kibana remains accessible following upgrades.

- **Secured Kibana Ingress Configuration**

   The Kibana ingress configuration has been updated to strengthen deployment security and ensure safer access to Kibana services within the platform.



---
## Versions

</div>

{%- include docs-annotation-pagination.html -%}