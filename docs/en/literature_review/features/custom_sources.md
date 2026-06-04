---
layout: docs
header: true
seotitle: Literature Review Agent | John Snow Labs
title: Literature Review Agent
permalink: /docs/en/literature_review/features/custom_sources
key: docs-literature-review
modify_date: "2026-06-04"
show_nav: true
sidebar:
    nav: literature-review
---

<div class="h3-box" markdown="1">

## Custom Sources

Not everything you need to review lives in PubMed or Semantic Scholar. Custom sources let you bring your own documents into a Literature Review Agent project — proprietary clinical study reports, internal research memos, regulatory submissions, or anything else that isn't publicly indexed. Once ingested, they're searchable and extractable alongside the standard databases.

</div><div class="h3-box" markdown="1">

## Uploading a ZIP Archive

This is the simplest option for most teams. Bundle your documents into a ZIP and upload it — that's it.

1. In the **Custom Sources** section, click **Upload ZIP**.
2. Select a ZIP archive containing `.pdf`, `.txt`, or `.docx` files.
3. The appliance extracts text from each file and indexes it for keyword and semantic search.
4. When ingestion is done, the source appears as a selectable option in Step 1 (Search Articles).

</div><div class="h3-box" markdown="1">

## Ingesting from an S3 Prefix

If your documents are already in S3, there's no need to download and re-upload them.

1. In the **Custom Sources** section, click **Add S3 Source**.
2. Enter your bucket name and prefix (e.g. `my-bucket/reports/2024/`).
3. The background worker fetches and ingests all supported files under that prefix automatically.
4. Make sure the IAM credentials used by the `worker` container have `s3:GetObject` and `s3:ListBucket` on the target bucket.

</div><div class="h3-box" markdown="1">

## Managing Custom Sources

| Action | UI | API |
|---|---|---|
| List sources | Custom Sources page | `GET /custom-sources` |
| View a source | Select from list | `GET /custom-sources/{id}` |
| Check storage usage | Sources page header | `GET /custom-sources/space` |
| Upload ZIP | Upload button | `POST /custom-sources/upload` |
| Add S3 source | S3 form | `POST /custom-sources/s3` |
| Search a source | Search panel | `POST /custom-sources/{id}/search` |
| Delete a source | Delete icon | `DELETE /custom-sources/{id}` |

</div><div class="h3-box" markdown="1">

## Privacy

Custom-source documents are stored and processed entirely inside the appliance. They're never sent to any external database or indexing service. The one exception is extraction itself: article text is sent to your configured LLM (SageMaker or DeepLens) for processing — which is the same behaviour as for articles from public databases.

</div>
