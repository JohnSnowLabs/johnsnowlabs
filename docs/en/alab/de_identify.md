---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: De-Identification
permalink: /docs/en/alab/de_identify
key: docs-training
modify_date: "2025-11-27"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
    nav: annotation-lab
---

<div class="h3-box" markdown="1">

## Protect Sensitive Data While Preserving Value

Working with sensitive documents containing **Personally Identifiable Information (PII)** or **Protected Health Information (PHI)** doesn't have to be complicated. Generative AI Lab's **De-Identification** feature helps you automatically detect and anonymize sensitive data—ensuring compliance with privacy regulations like HIPAA and GDPR while keeping your data useful for analysis and model training.
<br/>
### Why De-Identification Matters

- **Stay Compliant:** Meet HIPAA, GDPR, and other privacy regulations without manual redaction
- **Share Data Safely:** Collaborate with external teams or researchers without exposing sensitive information
- **Accelerate AI Development:** Train models on realistic data without privacy risks
- **Reduce Risk:** Minimize data breaches by removing PII/PHI before sharing or storing documents

</div>

<div class="h3-box" markdown="1">
## How It Works: Three Simple Steps

### 1. Create a De-Identification Project

Start by selecting the **De-identification** template when creating a new project. The system automatically:
- Downloads the state-of-the-art clinical_deidentification pipeline
- Sets up optimized labels for common sensitive entities (names, dates, IDs, etc.)
- Configures privacy-preserving export settings

<br/>

![Create De-ID Project](/assets/images/annotation_lab/6.7.0/1.png)

<br/>
> **Quick Start:** Import the **Demo De-Identification Project** from the Import menu to explore the feature with sample data before working on real documents.

<br/>
### 2. Choose Your De-Identification Strategy
\
Select how you want to handle sensitive information—you can even use **different strategies for different entity types**:
\


| Strategy | What It Does | Example | Best For |
|----------|--------------|---------|----------|
| **Mask with Entity Labels** | Replaces text with label names | &lt;Patient&gt; is a &lt;Age&gt; y.o. | Maintaining document structure |
| **Mask with Characters** | Replaces each character with * | \*\*\*\* \*\*\*\*\*\* is a \*\* y.o. | Preserving text length |
| **Fixed Length Mask** | Replaces with fixed \*\*\*\* | \*\*\*\* \*\*\*\* is a \*\*\*\* y.o. | Uniform anonymization |
| **Obfuscation** | Replaces with realistic fake data | Mark Doe is a 48 y.o. | Maintaining data realism |

**Example:** For "John Davies is a 62 y.o. patient admitted to ICU after an MVA":
- Entity Labels → "&lt;Patient&gt; is a &lt;Age&gt; y.o. patient admitted to ICU after an MVA"
- Obfuscation → "Mark Doe is a 48 y.o. patient admitted to ICU after an MVA"

![Choose Strategy](/assets/images/annotation_lab/6.7.0/3.png)

**Pro Tip:** You can upload custom obfuscation rules in JSON format to reuse configurations across projects.

![Upload Config](/assets/images/annotation_lab/6.7.0/4.gif)

### 3. De-Identify and Export

Once your strategy is configured:

1. **Import your documents** - They'll be tagged as NonDeidentified for easy tracking
2. **Click "De-identify"** - The AI automatically detects and labels sensitive entities
3. **Review and adjust** - Make any corrections on the labeling page
4. **Submit completions** - Mark reviewed tasks with a star
5. **Export safely** - Only de-identified, human-verified data is exported

![De-ID Process](/assets/images/annotation_lab/6.7.0/6.gif)

</div><div class="h3-box" markdown="1">

## Advanced Features

### Multi-Source Detection

Combine multiple approaches for maximum accuracy:
- **Pre-trained models** for common entity types
- **Custom rules** for domain-specific patterns
- **Prompts** for contextual detection
- **John Snow Labs De-Identification Pipeline** for state-of-the-art performance

![Pipelines Tab](/assets/images/annotation_lab/6.7.0/2.png)

### Compare Original and De-Identified

View side-by-side comparisons of original and anonymized text to verify results before export.

![De-ID View](/assets/images/annotation_lab/6.7.0/8.gif)

### Re-Import for Further Processing

Export de-identified documents and re-import them into any text project for:
- Additional annotation by team members
- Model training on privacy-safe data
- Further analysis without compliance concerns

</div><div class="h3-box" markdown="1">

## Best Practices

✅ **Target Only Sensitive Entities:** Only label data that needs protection—everything labeled will be transformed during export

✅ **Verify Before Export:** Always review AI predictions to ensure accuracy. Only starred (submitted) completions are exported

✅ **Use Entity-Specific Strategies:** Apply obfuscation to names for realism, but mask IDs with fixed characters for simplicity

✅ **Test with Demo Project:** Familiarize yourself with workflows using the built-in demo before processing real data

✅ **Leverage Custom Rules:** Combine pre-trained models with custom rules to catch domain-specific patterns

</div><div class="h3-box" markdown="1">

## Quick Reference

### Creating a Project

From the Import menu:
1. Select **Import Demo Projects** for a pre-configured example, OR
2. Create a new project and select **De-identification** template under the **TEXT** tab

> **Tip:** Look for the de-identification icon in the bottom-left corner of project cards to quickly identify de-identification projects.

### Export Workflow

The export process automatically handles prioritization:

1. **Submitted completions** (starred by annotators) are exported first
2. If no submissions exist, **de-identified predictions** are exported
3. With multiple submissions, the **highest priority user's completion** is used (configured on the Teams page)

![Export](/assets/images/annotation_lab/6.7.0/9.gif)

### Tags and Status

- **NonDeidentified tag:** Automatically added to new imports for tracking
- **Status indicators:** Green (success), red (error), grey (pending) next to each task
- **(De-identified) label:** Shown next to completion IDs after de-identification

![Status](/assets/images/annotation_lab/6.7.0/5.gif)

</div><div class="h3-box" markdown="1">

## Important Notes

> **License Required:** A valid John Snow Labs license is needed to access de-identification features.

> **Project Type is Permanent:** Projects must be designated as de-identification projects during creation—you cannot convert existing projects to de-identification projects later.

> **Human Review Required:** Pre-annotations alone aren't exported. Each task must be reviewed and starred by a human to ensure quality.

> **Unified Workflow:** The **De-identify** button works consistently across all project types (pipelines, models, rules) for a predictable experience.

</div>

<div class="h3-box" markdown="1">

## Need Help?

- **Getting Started:** Import the Demo De-Identification Project from the Import menu
- **Custom Configurations:** Upload JSON obfuscation rules via the Customize Labels page
- **Pipeline Management:** View all downloaded pipelines on the dedicated Pipelines page
- **Support:** Contact [support@johnsnowlabs.com](mailto:support@johnsnowlabs.com) for assistance

</div>
