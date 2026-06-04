---
layout: docs
header: true
seotitle: Literature Review Agent | John Snow Labs
title: Literature Review Agent
permalink: /docs/en/literature_review/api_service
key: docs-literature-review
modify_date: "2026-06-04"
show_nav: true
sidebar:
    nav: literature-review
---

<div class="h3-box" markdown="1">

## API Service Access

Everything you can do in the web UI, you can also do via the REST API. That includes creating projects, triggering extraction runs, polling for results, streaming Q&A responses, and managing custom sources. If you want to integrate Literature Review Agent into an existing pipeline or automate recurring reviews, the API is where to start.

The API is served by the `api` FastAPI service. Interactive docs (Swagger UI / OpenAPI) are hosted on the appliance itself:

```
http://<INSTANCE_IP>/docs
```

</div><div class="h3-box" markdown="1">

## Authentication

All endpoints require the workspace **login password**. First, exchange the password for a session token:

```
POST /setup/login
```

Then pass the returned token as a Bearer in the `Authorization` header for all subsequent requests:

```
Authorization: Bearer <token>
```

</div><div class="h3-box" markdown="1">

## Endpoint Reference

Endpoints are grouped by router below. All routes are relative to the `api` service base URL.

### Extraction Runs — `/literature-review`

| Method & path | Purpose |
|---|---|
| `POST /jobs` | Create an extraction run (search config + data points + criteria + filters) |
| `GET /jobs/{run_id}` | Job status and live progress counters |
| `GET /jobs/{run_id}/config` | Stored request config (used for clone / delta) |
| `GET /jobs` | List all runs |
| `DELETE /jobs/{run_id}` | Stop a specific run |
| `DELETE /jobs` | Cancel all active runs |

### Results — `/literature-review`

| Method & path | Purpose |
|---|---|
| `GET /reports/{run_id}` | Paginated extraction results; add `?format=CSV` to download CSV |
| `GET /reports/{run_id}/all` | Full result set (used for Step 4 article selection) |
| `DELETE /reports/{run_id}` | Delete results for a run |
| `GET /run-history` | List recent runs with metadata |

### Literature QA — `/literature-review`

| Method & path | Purpose |
|---|---|
| `POST /lit-qa/stream` | Streaming Literature QA over a selected article set (SSE) |

### DeepLens Search — `/literature-review/search`

| Method & path | Purpose |
|---|---|
| `POST /docs` | Keyword search |
| `POST /query` | Semantic search |
| `POST /docs_by_id` | Fetch articles by ID |
| `POST /find_docs` | Combined search |
| `GET /filters` | Available filter options |
| `GET /author_names` | Author name autocomplete |
| `POST /expand_query` | MeSH query expansion |

### External Search — `/external-search`

| Method & path | Purpose |
|---|---|
| `POST /docs` | Search NCBI / Semantic Scholar / Europe PMC / OpenAlex |

### Custom Sources — `/custom-sources`

| Method & path | Purpose |
|---|---|
| `GET ""` | List all custom sources |
| `GET /{id}` | Get a single source |
| `GET /space` | Storage usage |
| `POST /upload` | Upload a ZIP archive |
| `POST /s3` | Add an S3-prefix source |
| `POST /{id}/search` | Search within a specific custom source |
| `DELETE /{id}` | Delete a custom source |

### Search Sources Config — `/sources`

| Method & path | Purpose |
|---|---|
| `GET /types` | Available source types |
| `GET ""` | List configured sources |
| `POST ""` | Add a source |
| `PATCH /{id}` | Update a source |
| `DELETE /{id}` | Remove a source |

### Authentication — `/setup`

| Method & path | Purpose |
|---|---|
| `POST /login` | Authenticate and receive a session token |

</div>
