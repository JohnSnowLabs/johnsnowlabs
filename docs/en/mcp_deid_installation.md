---
layout: docs
header: true
seotitle: MCP De-identification Server | John Snow Labs
title: MCP De-identification Server
permalink: /docs/en/mcp_deid_installation
key: docs-mcp-deid
modify_date: 2025-04-03
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## Overview

**Available since Healthcare NLP 6.3.0**

The Model Context Protocol (MCP) De-identification Servers enable AI coding assistants (such as Cursor and VS Code Copilot) to access state-of-the-art clinical de-identification pipelines directly as tools. This integration allows you to sanitize clinical text instantly within your IDE while maintaining strict HIPAA compliance through local, secure execution.

</div><div class="h3-box" markdown="1">

### Key Features

* Direct integration with Cursor and VS Code
* Local execution for HIPAA compliance
* Support for both masking and obfuscation modes
* Detection of 30+ PHI entity types
* Two deployment architectures for different use cases

</div><div class="h3-box" markdown="1">

## Architecture Options

Two architectures are available to accommodate different deployment requirements:

</div><div class="h3-box" markdown="1">

### Lightweight Architecture (v2) - Recommended

A thin, instant-startup Python server that connects your IDE to a robust backend de-identification service.

**Specifications:**
* Startup Time: < 1 second
* Memory: ~100MB (MCP server)
* Ports: 8001 (MCP) + 9000 (backend)
* Best For: Teams sharing a backend GPU server; frequent IDE restarts

</div><div class="h3-box" markdown="1">

**Architecture Diagram:**

```
IDE (Cursor/VSCode) → MCP Server v2 → Deid Service Container → Spark NLP Healthcare
```
</div><div class="h3-box" markdown="1">

### Monolithic Architecture (v1)

Battery-included approach with the Spark NLP pipeline embedded directly inside the MCP server container.

**Specifications:**
* Startup Time: 2-5 minutes (pipeline loading)
* Memory: 8GB+ reserved
* Port: 8000
* Best For: Air-gapped environments; single-container deployments

**Architecture Diagram:**

```
IDE (Cursor/VSCode) → MCP Server v1 (containing embedded Spark NLP Pipeline)
```

</div><div class="h3-box" markdown="1">

### Architecture Comparison

| Aspect | v1 Monolithic | v2 Lightweight |
|--------|---------------|----------------|
| **Port** | 8000 | 8001 (MCP) + 9000 (backend) |
| **Memory** | 8GB+ reserved | ~100MB (MCP server only) |
| **Startup Time** | 2-5 minutes | Instant (<1 second) |
| **Docker Required** | Yes | MCP: No, Backend: Yes |
| **Use Case** | Standalone deployment | Shared backend, multiple clients |

</div><div class="h3-box" markdown="1">

## Prerequisites

* Docker and Docker Compose installed
* Valid John Snow Labs Healthcare NLP license
* 8GB+ available memory for pipeline container
* Cursor or VS Code with GitHub Copilot

</div><div class="h3-box" markdown="1">

## License Configuration

Both architectures require a valid John Snow Labs Healthcare NLP license provided via a `spark_jsl.json` file.

</div><div class="h3-box" markdown="1">

### Required License Keys

```json
{
  "SPARK_NLP_LICENSE": "eyJ...",
  "SECRET": "x.x.x-xxxxxxxxx"
}
```

| Key | Description |
|-----|-------------|
| `SPARK_NLP_LICENSE` | JWT license token for Spark NLP Healthcare |
| `SECRET` | PyPI token for private package installation |

</div><div class="h3-box" markdown="1">

### Optional License Keys

```json
{
  "SPARK_OCR_LICENSE": "eyJ...",
  "AWS_ACCESS_KEY_ID": "AKIA...",
  "AWS_SECRET_ACCESS_KEY": "...",
  "AWS_SESSION_TOKEN": "..."
}
```

These keys are required for OCR capabilities or S3 model downloads.

</div><div class="h3-box" markdown="1">

### Security: Docker Secrets

The license file is mounted as a Docker secret at `/run/secrets/spark_jsl.json` to keep credentials secure and prevent them from being baked into Docker images.

```yaml
# docker-compose.yml
secrets:
  spark_jsl:
    file: ./spark_jsl.json

services:
  deid-service:
    secrets:
      - source: spark_jsl
        target: spark_jsl.json
```

> **Note:** If you do not have a JSL Healthcare NLP license, visit [johnsnowlabs.com](https://www.johnsnowlabs.com/) to request a trial.

</div><div class="h3-box" markdown="1">

## Installation Steps

### Step 1: Clone the Repository

```bash
git clone https://github.com/JohnSnowLabs/spark-nlp-workshop.git
cd spark-nlp-workshop/agents/mcp_servers/deidentification
```

</div><div class="h3-box" markdown="1">

### Step 2: Configure License File

**Option A: Copy example and edit**

```bash
cp spark_jsl.json.example spark_jsl.json
# Edit spark_jsl.json with your actual JSL license credentials
```

**Option B: Copy existing license**

```bash
cp /path/to/your/spark_jsl.json ./deid-service/spark_jsl.json
```

</div><div class="h3-box" markdown="1">

### Step 3: Start Backend Service

```bash
cd deid-service

# Set JSL secret for Docker build
export JSL_SECRET=$(jq -r '.SECRET' spark_jsl.json)

# Build and start
docker compose up --build
```

Wait for the service to report "Application startup complete". First startup takes 2-5 minutes for model download; subsequent starts are faster due to caching.

**Test the backend:**

```bash
curl -X POST http://localhost:9000/deidentify \
  -H "Content-Type: application/json" \
  -d '{"text":"Dr. John Lee treated patient Emma Wilson","mode":"both"}'
```

</div><div class="h3-box" markdown="1">

### Step 4: Start MCP Server

**Option A: Lightweight v2 (Recommended)**

```bash
cd jsl-deid-mcp-server-v2
pip install -e .
python -m src.server
```

Server starts on `http://localhost:8001/mcp`

**Option B: Monolithic v1**

```bash
cd jsl-deid-mcp-server-v1
export JSL_SECRET=$(jq -r '.SECRET' spark_jsl.json)
docker compose up --build
```

Server starts on `http://localhost:8000/mcp`

</div><div class="h3-box" markdown="1">

### Step 5: Configure IDE Client

#### Cursor Configuration

Add to `~/.cursor/mcp.json` (macOS/Linux):

```json
{
  "mcpServers": {
    "jsl-deid": {
      "url": "http://localhost:8001/mcp",
      "transport": "streamable-http"
    }
  }
}
```

Restart Cursor after updating the configuration.

</div><div class="h3-box" markdown="1">

#### VS Code Copilot Configuration

Add to `project_folder/.vscode/mcp.json`:

```json
{
  "mcp.servers": {
    "jsl-deid": {
      "url": "http://localhost:8001/mcp",
      "type": "http"
    }
  }
}
```

Restart VS Code after updating the configuration.

</div><div class="h3-box" markdown="1">

## Verification (Optional)

### Initialize Session

```bash
curl -s -i -X POST http://localhost:8001/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}},"id":1}'
```

</div><div class="h3-box" markdown="1">

### Call De-identification Tool

Replace `<SESSION_ID>` with the `mcp-session-id` from the initialize response header:

```bash
curl -s -X POST http://localhost:8001/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Mcp-Session-Id: <SESSION_ID>" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "deidentify_text",
      "arguments": {
        "text": "Dr. John Lee treated patient Emma Wilson on 11/05/2024.",
        "mode": "both"
      }
    },
    "id": 2
  }'
```

</div><div class="h3-box" markdown="1">

## Usage

### Sample Clinical Text

```text
Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024.
The patient's medical record number is 56467890.
The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890.
```

</div><div class="h3-box" markdown="1">

### Output Modes

#### Mode: `masked`

PHI entities replaced with labels:

```text
Dr. <NAME>, from <HOSPITAL> in <CITY>, attended to the patient on <DATE>.
The patient's medical record number is <ID>.
The patient, <PATIENT>, is <AGE> years old, her Contact number: <PHONE>.
```

</div><div class="h3-box" markdown="1">

#### Mode: `obfuscated`

PHI entities replaced with realistic fake values:

```text
Dr. Vivia Ammon, from Baltimore Va Medical Center in Healdton, attended to the patient on 06/06/2024.
The patient's medical record number is 25958147.
The patient, Marla Sakai, is 40 years old, her Contact number: 999-925-8147.
```

</div><div class="h3-box" markdown="1">

#### Mode: `both`

Returns both masked and obfuscated versions in a single response:

```json
{
  "masked": "Dr. <DOCTOR>, from <HOSPITAL> in <CITY>, attended to the patient on <DATE>.\nThe patient's medical record number is <MEDICALRECORD>.\nThe patient, <PATIENT>, is <AGE> years old, her Contact number: <PHONE>.",
  "obfuscated": "Dr. Vivia Ammon, from Baltimore Va Medical Center in Healdton, attended to the patient on 06/06/2024.\nThe patient's medical record number is 25958147.\nThe patient, Marla Sakai, is 40 years old, her Contact number: 999-925-8147.",
  "error": null
}
```

</div><div class="h3-box" markdown="1">

### Using in Cursor

In the Cursor chat:

```
Use the Deid MCP to de-identify this clinical note with masked output.
"Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024..."
```

Cursor will automatically invoke the `deidentify_text` tool and return the result.

</div><div class="h3-box" markdown="1">

### Using in VS Code Copilot

In VS Code Copilot Chat:

```
Utilize the Deid MCP to anonymize this clinical note, employing both masked and obfuscated output modes.
"Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024..."
```

</div><div class="h3-box" markdown="1">

## Supported PHI Entity Types

The pipeline detects and processes 30+ PHI entity types including:

**Personal Identifiers:**
* `PATIENT`, `DOCTOR`, `USERNAME`
* `AGE`, `DATE`
* `SSN`, `DLN` (Driver's License), `LICENSE`

**Contact Information:**
* `PHONE`, `FAX`, `EMAIL`, `URL`

**Location Data:**
* `HOSPITAL`, `CITY`, `STATE`, `COUNTRY`, `ZIP`
* `STREET`, `LOCATION`

**Medical Identifiers:**
* `MEDICALRECORD`, `HEALTHPLAN`, `ACCOUNT`
* `IDNUM`, `BIOID`

**Organization:**
* `ORGANIZATION`, `PROFESSION`

**Vehicle/Device:**
* `DEVICE`, `PLATE`, `VIN`

The underlying pipeline is `clinical_deidentification` from Spark NLP Healthcare, which combines NER models, rule-based matchers, and contextual parsers for high-accuracy PHI detection.

</div><div class="h3-box" markdown="1">

## Technical Details

### Privacy by Design

The servers log request metadata (text size, mode, latency) but **never log clinical content**:

```python
# What is logged
logger.info(f"Deidentify request: {len(text)} chars, mode={mode}")
logger.info(f"Deidentify completed: {elapsed_ms:.0f}ms")

# What is never logged
# logger.info(f"Processing: {text}")  # NEVER
```

</div><div class="h3-box" markdown="1">

### Streamable HTTP Transport

The implementation uses FastMCP's `streamable_http_app()` with uvicorn for IDE compatibility, providing the HTTP-based transport expected by Cursor and VS Code Copilot.

</div><div class="h3-box" markdown="1">

### Pipeline Warmup

On startup, the pipeline processes a sample text to trigger JVM JIT compilation and lazy initialization. This ensures consistent latency for actual requests:

* Without warmup: First request can take 10-30 seconds
* With warmup: Typical latency is 100-500ms depending on text length

</div><div class="h3-box" markdown="1">

## Resources

* **GitHub Repository:** [spark-nlp-workshop/agents/mcp_servers/deidentification](https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/deid-mcp-server/agents/mcp_servers/deidentification)
* **Spark NLP Healthcare Documentation:** [nlp.johnsnowlabs.com](https://nlp.johnsnowlabs.com/)
* **Clinical De-identification Model:** [clinical_deidentification_docwise_benchmark_optimized](https://nlp.johnsnowlabs.com/2025/07/03/clinical_deidentification_docwise_benchmark_optimized_en.html)
* **MCP Protocol Specification:** [modelcontextprotocol.io](https://modelcontextprotocol.io/)

</div><div class="h3-box" markdown="1">

## Future Additions

This de-identification MCP server is the first in a planned series of healthcare NLP tools for AI assistants:

* **Data Curation MCP Server** - Clinical entity extraction and structuring
* **Medical Coding MCP Server** - ICD-10, CPT code assignment

</div><div class="h3-box" markdown="1">

## Getting Started

Clone the repository, configure your license, and bring clinical de-identification to your IDE. The v2 lightweight architecture enables you to start in under 10 minutes with post-installation response times of less than a second.

</div>