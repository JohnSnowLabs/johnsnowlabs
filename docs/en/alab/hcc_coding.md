---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: HCC Coding Projects
permalink: /docs/en/alab/hcc_coding
key: docs-training
modify_date: "2025-11-27"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

## Overview

Generative AI Lab provides specialized **HCC Coding** project types for **Hierarchical Condition Category (HCC)** risk adjustment coding.  
These templates are designed to help healthcare organizations and coders efficiently map clinical findings or diagnoses to the correct **HCC codes**, ensuring accurate documentation for reimbursement and compliance workflows.

HCC Coding projects integrate medical entity recognition, code lookup, and reviewer validation within the annotation interface — linking each identified ICD-10 diagnosis to its corresponding HCC category.  
This automation supports human-in-the-loop validation while maintaining transparency and control.

## Available Templates

Two project templates are available for HCC coding tasks:

1. **HCC Coding (Text)** – for coding clinical narratives and structured text data.  
2. **HCC Coding (PDF + Text Side-by-Side)** – for coding scanned or PDF documents while viewing both the original source and its extracted OCR text simultaneously.

Both templates include preconfigured entity labels and code mappings, enabling annotators to assign and validate codes directly during annotation.

## How It Works

When annotating medical entities such as diagnoses or conditions, the system automatically suggests the most relevant **HCC category code** based on the annotated **ICD-10 code**.  
These mappings are powered by integrated lookup datasets and medical coding pipelines.

Within the labeling interface, annotators can:

- **Accept or modify HCC code suggestions** using the **“Accept HCC Suggestion”** button beside each detected entity.  
- **Manually edit** the suggested HCC code from a searchable dropdown or code panel.  
- **Mark codes as confirmed** once verified, signaling that the assigned HCC mapping is clinically and administratively valid.  
- **Tag findings as “Non-Billable”** when a diagnosis is present but not eligible for billing, using the **Non-Billable toggle** in the entity detail view.

Each entity displays its ICD-10 label and HCC mapping inline, allowing for quick visual review.

## Typical Workflow

1. **Project Setup**
   - Navigate to **Projects → New Project**.  
   - Under the **Text** or **PDF** content type, select one of the available **HCC Coding** templates.  
   - A valid **Healthcare NLP license** is required for HCC Coding projects, as they use domain-specific clinical models and code lookups.

2. **Label Customization**
   - On the **Customize Labels** page, link your label set to a preloaded **lookup dataset** (containing ICD-10 and HCC mappings).  
   - You can apply the lookup globally across all labels or individually per label for granular control.  
   - Lookup datasets can also include CPT or other medical code sets if procedure-level coding is needed.

3. **Annotation and Review**
   - Annotate entities in the document using the standard text or PDF+Text view.  
   - The system automatically proposes matching HCC codes.  
   - Use the **Accept HCC Suggestion** button to confirm mappings, or modify them manually.  
   - Mark entities as **Confirmed** or **Non-Billable** as applicable.

4. **Reviewer Confirmation**
   - Reviewers validate the assigned HCC codes and can accept, remove, or mark labels as non-billable directly from the annotation widget.  
   - Review status is visible inline, ensuring clarity and auditability throughout the workflow.

## Exporting and Reporting

When exporting tasks, only completions marked as **Ground Truth** are included in the de-identified, coded output.  
Exports retain ICD-10 and HCC associations for downstream billing analysis or quality audits.  
The HCC-coded data can also be re-imported into other annotation or review projects to support iterative validation and continuous model improvement.

## Summary

HCC Coding projects in Generative AI Lab provide a structured, human-in-the-loop environment for healthcare risk adjustment and coding accuracy.  
By combining ICD-10 detection, automatic HCC mapping, and manual validation, these projects empower healthcare teams to:

- Improve coding quality and compliance  
- Streamline risk adjustment workflows  
- Reduce manual effort and rework  
- Maintain full transparency and audit traceability

