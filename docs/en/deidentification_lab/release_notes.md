---
layout: docs
seotitle: Release Notes | John Snow Labs
title: Release Notes
permalink: /docs/en/deidentification_lab/release_notes
key: docs-install
modify_date: "2023-04-13"
header: true
show_nav: true
sidebar:
    nav: deidentification_lab
---

<div class="h3-box" markdown="1">

## 1.0.0

Release date: **22-03-2023**

This is the first release and it comes with following features:
### Document Formats
<ul>
<li>Unstructured text (txt)</li>
<li>PDF (text and image)</li>
<li>DICOM files including the metadata</li>
</ul>

### Entities Supported
<img class="image image__shadow image__align--center" src="/assets/images/deidentification_lab/deid_supported_entities_1_0_0.png" style="width:100%;"/>
</div><div class="prev_ver h3-box" markdown="1">

### Techniques and Strategies
<ul>
    <li>Keep: When this strategy is selected for an entity, De-identification Lab will leave the entity as it is. </li>
    <li>Mask: This strategy essentially allows the PHI entities to be replaced either the ENTITY NAME or replace with a fixed lenght of asterics (*) or replace with a same lenght number of asterics as the lenght of the entity.</li>
    <li>Obfuscate: This strategy allows the PHIs to be replaced with values that are semantically and linguistically similar. </li>
</ul>

### Infrastructure

Currently it is supported on AWS Marketplace

## Versions

</div>

<ul class="pagination owl-carousel pagination_big">
    <li class="active"><a href="deidentification_labs_releases/release_notes_1_0_0">1.0.0</a></li>

<!-- <li><a href="deidentification_labs_releases/release_notes_0_0_1">0.0.1</a></li> -->
</ul>
