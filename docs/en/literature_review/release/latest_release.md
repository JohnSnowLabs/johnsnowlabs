---
layout: docs
header: true
seotitle: Release Notes | Literature Review Agent | John Snow Labs
title: Literature Review Agent Release Notes
permalink: /docs/en/literature_review/release/latest_release
key: docs-literature-review
modify_date: "2026-06-04"
show_nav: true
sidebar:
    nav: literature-review
---

<div class="h3-box" markdown="1">

<p style="text-align:center;" markdown="1">Release date: {{ page.modify_date | date: '%m-%d-%Y' }}</p>

## What's New

This is the initial public release of the **Literature Review Agent**. The full feature set is available from day one.

### Core workflow

- **5-step guided UI** — Search, Data Points & Criteria, Run & Monitor, Select Literatures, and Literature QA.
- **Multi-source search** — DeepLens medical knowledge bases, PubMed (NCBI), Semantic Scholar, Europe PMC, and OpenAlex, all queryable from a single screen.
- **Keyword, semantic, and document-ID search modes** with MeSH query expansion for PubMed and DeepLens sources.
- **Rich result filters** — date, article type, language, journal, author, open-access, impact factor, journal quartile, h-index, and citation count.

### Extraction & screening

- **Plain-language data points** — define what to extract using a label and a natural-language prompt; no fixed schema required.
- **Inclusion/exclusion criteria** — per-article verdicts with supporting explanations for every rule.
- **AI-assisted criteria generation** — describe your review in one sentence and get a drafted set of data points and rules to edit.
- **Evidence-backed extraction** — every extracted value is paired with the exact source sentence.

### Run management

- **Distributed extraction** with live progress monitoring (total / processed / succeeded / failed / % complete).
- **Delta processing** — add new articles to an existing run without reprocessing completed ones.
- **Copy into a new run** — clone a run's full configuration for reuse or experimentation.
- **Run history sidebar** — all previous runs accessible with a single click.
- **CSV export** — full result set with metadata, extracted values, evidence sentences, and verdicts.

### Literature QA

- **Select Literatures** — curate a focused article set from extraction results.
- **Streaming Q&A** — ask questions grounded in selected articles; answers stream in real time with source citations.

### Custom sources

- **ZIP upload** — ingest `.pdf`, `.txt`, and `.docx` files from a local archive.
- **S3 ingestion** — point to an S3 prefix and the worker fetches and indexes everything automatically.

### Deployment

- Ships as an **AWS Marketplace AMI** with a fully managed service stack.
- HTTPS support via CloudFront CloudFormation template.


</div>
