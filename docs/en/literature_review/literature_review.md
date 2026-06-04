---
layout: docs
header: true
seotitle: Literature Review Agent | John Snow Labs
title: Literature Review Agent
permalink: /docs/en/literature_review/literature_review
key: docs-literature-review
modify_date: "2026-06-04"
show_nav: true
sidebar:
    nav: literature-review
---

Systematic literature reviews are slow. Teams spend weeks searching databases, screening abstracts, and hand-copying data into spreadsheets — work that is error-prone and hard to audit. The **Literature Review Agent** is built to change that.

It's a guided workspace that automates the heavy lifting of evidence synthesis. You search trusted medical and academic databases, define what you want to extract in plain language, and let John Snow Labs medical-grade LLMs pull **structured, evidence-backed data** from every article — with inclusion/exclusion screening applied automatically. The whole thing runs from a clean web UI, with no scripting required.

Literature Review Agent ships as a self-contained **AWS Marketplace AMI**. The entire stack runs in **your own AWS account** via `docker compose`, so your queries, uploaded documents, and extraction results never leave your infrastructure.

![Literature Review — multi-source search and results](/assets/images/literature_review/step1-search.png)

## Highlights

* **Hours, not weeks.** Automated search, screening, and extraction collapse the most time-consuming phases of a systematic review into a single afternoon.
* **Medical-grade understanding.** Powered by John Snow Labs medical LLMs specifically tuned for clinical and biomedical text. Models run on Amazon SageMaker in your own account, or you can access them through the DeepLens API (`api.deeplens.health`).
* **Everything in one query.** Search medical knowledge bases, **PubMed (NCBI)**, **Semantic Scholar**, **Europe PMC**, and **OpenAlex** (250 M+ scholarly works) simultaneously — or bring your **own documents** via ZIP upload or S3 prefix.
* **Rigour you can audit.** Every extracted value comes with the supporting sentence from the source article. Inclusion and exclusion decisions are applied consistently to every paper, not just the ones you happen to re-read.
* **Reproducible by design.** Save, clone, and delta-update runs. When new evidence is published, a single delta refresh brings your review current — no starting from scratch.
* **Your data stays yours.** Single-tenant, deployed inside your VPC. The workspace is password-gated and nothing leaves your environment.
* **Results you can use immediately.** Export the full result set as CSV and take it straight into your existing analysis tools.

---

## 5-Step Guided Workflow

Literature Review Agent walks you through a clear, repeatable pipeline. Steps 1–3 are the core review. Steps 4–5 are optional, but useful when you want to go beyond extraction and actually interrogate your evidence set.

### Step 1 — Search Articles

Everything starts with a search. You can query multiple sources at once — medical knowledge bases, PubMed, Semantic Scholar, Europe PMC, OpenAlex — and narrow the result set with rich filters before any extraction begins. Keeping that initial result set focused saves time and LLM cost downstream.

Search modes include keyword, semantic, and document-ID lookup. MeSH query expansion is available when searching PubMed or DeepLens knowledge bases, so papers indexed under controlled vocabulary terms don't fall through the cracks. You can also upload your own documents as a ZIP archive or point to an S3 prefix if you're working with proprietary material.

![Step 1 — multi-source search and filters](/assets/images/literature_review/step1-search.png)

### Step 2 — Data Points & Criteria

This is where you tell the agent what to look for. Data points are simple: a short label (like `sample_size`) and a plain-language description of what to extract (like “The number of participants enrolled in the study”). No rigid schemas, no fixed templates — just describe it the way you'd ask a colleague.

You also define inclusion and exclusion rules the same way. Each rule is a label plus a plain sentence: “The study must be a randomised controlled trial.” The LLM applies those rules to every article and records a verdict.

Not sure where to start? Use **Generate with AI**. Describe your review topic in a single sentence and the agent will draft a set of data points and criteria for you to review and edit.

![Step 2 — define data points and AI-generated criteria](/assets/images/literature_review/step2-criteria.png)

### Step 3 — Run & Monitor

Once you're happy with the setup, kick off extraction. The run is distributed across background workers, so even large result sets move quickly. A live dashboard shows you exactly where things stand — how many articles have been processed, how many succeeded, and how many hit an error.

Each article gets structured extraction with supporting evidence and a per-rule inclusion/exclusion verdict. If new papers appear after your initial run, **delta processing** lets you add them without re-extracting what's already done. You can also copy a run's configuration into a new project, or flip between previous runs using the run-history sidebar.

![Step 3 — run monitor with live progress](/assets/images/literature_review/step3-run-monitor.png)

Click into any article to see the full detail view: extracted values, evidence sentences, verdicts, and all the metadata and quality indicators for that paper.

![Article detail — extracted data points with evidence](/assets/images/literature_review/article-detail.png)

### Step 4 — Select Literatures *(optional)*

After extraction, you can hand-pick the articles most relevant to your questions and group them into a focused set for Q&A. Think of it as curating your evidence base before you start asking questions.

![Step 4 — select literatures](/assets/images/literature_review/step4-select.png)

### Step 5 — Literature QA *(optional)*

With a literature set selected, you can ask questions in plain language and get answers grounded in those specific articles. It's useful for summarising findings, spotting patterns, or quickly checking whether any paper in your set addresses a particular point.

---

## Example Use Cases & Target Audience

🎯 **Target audience:** Medical researchers, systematic and scoping review teams, evidence-synthesis and HEOR groups, guideline developers, and meta-analysis authors.

---

🧑‍🔬 **Use Case 1: Guideline Update — SGLT2 Inhibitors**

An evidence team is updating a heart-failure guideline — their last review is two years old and a lot has been published since. They search PubMed, Europe PMC, and medical knowledge bases in a single pass: a MeSH-expanded query filtered to randomised trials from the past 24 months. They describe the review in one sentence; the agent drafts the data points (sample size, primary endpoint, follow-up, funding) and inclusion rules. A few edits and they're ready.

From there, the agent does the grind. It screens every abstract, extracts each data point with the exact supporting sentence, and flags anything uncertain. The analyst skims only the borderline papers. No re-reading 300 abstracts. No copy-pasting into spreadsheets. By that afternoon the team exports a clean CSV — every included study, every field, every citation — ready for meta-analysis.

---

🧑‍🔬 **Use Case 2: Pharmacovigilance Signal Detection**

Researchers monitoring adverse-event signals run a Literature Review Agent project over PubMed case reports. They define data points for drug name, adverse event term, reported severity, and causality assessment. Semantic search picks up informal descriptions and misspellings that a keyword search would miss. Delta runs keep the signal database current as new reports are published — without reprocessing what's already been extracted.

---

🧑‍🔬 **Use Case 3: Scoping Review from Proprietary Documents**

A regulatory team needs to review a set of proprietary clinical study reports — documents that aren't in any public database. They upload them as a ZIP. No external API is touched; ingestion, indexing, and extraction all happen inside the appliance. They define extraction points aligned with their submission template, run the project, and export. The same configuration gets reused across the next submission package with minimal setup.

---

## Architecture

Literature Review Agent runs as a self-contained stack with four services that start automatically on the AMI.

| Service | Role |
|---|---|
| API | REST API and web UI |
| Worker | Background extraction and document ingestion |
| Database | Jobs, reports, and configuration |
| Queue | Task broker |

**DeepLens** serves as both the search provider and the LLM endpoint for search and extraction calls.


