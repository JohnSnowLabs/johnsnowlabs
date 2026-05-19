---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Analytics Dashboard
permalink: /docs/en/alab/analytics_dashboard
key: docs-training
modify_date: "2026-05-19"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## Analytics Dashboard

The Analytics Dashboard provides a centralized workspace for monitoring annotation progress, team productivity, annotation quality, inter-annotator agreement, and LLM evaluation metrics across Generative AI Lab projects.

The dashboard is organized into dedicated analytics pages and contextual tabs, allowing project managers, reviewers, and annotation teams to efficiently navigate operational and quality metrics across large-scale annotation workflows.

Analytics capabilities include:

- Task and project monitoring
- Annotation quality analysis
- Team productivity tracking
- Inter-Annotator Agreement (IAA) analysis
- LLM response comparison and evaluation analytics
- Exportable charts and operational reporting

Most analytics charts support filtering, provider selection, annotator comparison, and data export directly from the dashboard interface.

![Analytics Dashboard overview with multi-tab navigation](/assets/images/annotation_lab/8.1.0/analytics_dashboard.gif)
*<center>The Analytics Dashboard provides a centralized workspace for monitoring project progress, productivity, annotation quality, inter-annotator agreement, and LLM evaluation metrics.</center>*

</div>

<div class="h3-box" markdown="1">

## Dashboard Navigation

The Analytics section is accessible directly from the project sidebar and is divided into multiple analytics categories depending on the project type and workflow configuration.

Available sections may include:

- Overview
- Labels & Data Quality
- Team Productivity
- Inter-Annotator Agreement
- LLM Response Comparison

![Analytics sidebar navigation structure](/assets/images/annotation_lab/8.1.0/6.png)
*<center>The Analytics sidebar provides structured navigation across multiple analytics categories, enabling faster access to project insights and operational metrics.</center>*


</div>

<div class="h3-box" markdown="1">

## Overview Dashboard

The Overview dashboard provides high-level operational metrics for monitoring project progress and annotation workflow status.

Overview widgets and charts include:

- Total Tasks
- Completion Rate
- Reviewed Rate
- Total Completions
- Task Status Distribution
- Progress Summary

The dashboard combines summary metrics with visual charts to provide quick visibility into annotation throughput and workflow progression.

![Overview dashboard with task summary and progress metrics](/assets/images/annotation_lab/8.1.0/overview.gif)
*<center>The Overview dashboard provides high-level visibility into project progress, completion metrics, and task distribution across annotation workflows.</center>*

</div>

<div class="h3-box" markdown="1">

## Labels & Data Quality

The Labels & Data Quality section focuses on annotation consistency, label usage patterns, and dataset-level quality analysis.

Available analytics may include:

- Label frequency distribution
- Label variability analysis
- Label usage across annotators
- Average tokens per label
- Distinct versus total label counts

These analytics help identify annotation inconsistencies, taxonomy imbalance, and labeling trends across datasets and annotation teams.

![Label frequency analytics across annotators](/assets/images/annotation_lab/8.1.0/label_data_quality.gif)
*<center>Labels & Data Quality analytics provide visibility into label distribution, annotation consistency, and dataset composition across annotation teams.</center>*

</div>

<div class="h3-box" markdown="1">

## Team Productivity Dashboard

The **Team Productivity** dashboard organizes operational metrics into dedicated analytics tabs focused on completion activity, review performance, and time-based productivity analysis.

Available tabs include:

- **Completions**
- **Review**
- **Time Metrics**

![Team Productivity Dashboard with completion and review analytics](/assets/images/annotation_lab/8.1.0/team_productivity.gif)
*<center>The Team Productivity dashboard provides visibility into completion trends, review activity, editing behavior, and annotation throughput across teams.</center>*

### Completion Analytics

The Completions section focuses on:
- Completion trend analysis
- Annotator throughput
- Submission activity over time
- Team-wide annotation volume

### Review Analytics

Review analytics provide visibility into:
- Average tokens for submitted and reviewed tasks
- Average reviews per annotator
- Submitted vs reviewed task ratios
- Total token volume across reviews

### Time Metrics

The Time Metrics section includes:
- Average time spent per task
- Average edit time per task
- Average number of edits per task

Together, these metrics help teams identify annotation bottlenecks, uneven workload distribution, and review inefficiencies.

</div>

<div class="h3-box" markdown="1">

## Inter-Annotator Agreement Dashboard

The **Inter-Annotator Agreement (IAA)** dashboard provides detailed agreement analysis and disagreement tracking across annotation teams.

The redesigned dashboard separates agreement analytics into structured analytical sections, improving visibility into annotation consistency across large projects.

![Inter-Annotator Agreement dashboard with chunk-level comparison analytics](/assets/images/annotation_lab/8.1.0/iaa.gif)
*<center>The Inter-Annotator Agreement dashboard provides detailed agreement analysis, disagreement tracking, and chunk-level comparison metrics across annotation teams.</center>*

### Agreement Overview

The Overview section includes:
- Annotator comparison filters
- Entity type selection
- NER agreement analysis
- Assertion agreement analysis
- Chunk-level agreement visualizations
- Detailed agreement tables for common tasks

### Chunk-Level Analysis

Chunk-level analytics provide:
- Chunk extraction tables by annotator
- Chunk frequency analysis
- Label-based cross-reference tables
- Disagreement identification support

These tools help project managers and reviewers identify annotation inconsistencies and improve annotation guideline alignment across teams.

</div>

<div class="h3-box" markdown="1">

## LLM Response Comparison Dashboard

The **LLM Response Comparison** dashboard provides dedicated analytics for projects evaluating and comparing Large Language Model outputs.

The dashboard uses dynamic tabs to organize evaluation metrics into focused analytical sections.

Available tabs include:

- **LLM Choices**
- **Labels**
- **Quality Ratings**

The active tab updates dynamically without requiring a page refresh.

![LLM Response Comparison dashboard with LLM choice analytics](/assets/images/annotation_lab/8.1.0/llm_response.gif)
*<center>The LLM Choices tab visualizes annotator preferences across multiple LLM responses through result summaries and provider selection frequency analytics.</center>*

### LLM Choices Tab

The LLM Choices section includes:

#### Result Summary
- Donut chart visualization of selected LLM responses
- Annotator preference distribution across providers

#### Choice Frequency by Annotator
- Dynamic bar charts comparing annotator selections across providers
- Interactive provider selection filters
- Automatic chart refresh when providers change

![LLM Response Comparison dashboard with LLM choice analytics](/assets/images/annotation_lab/8.1.0/11.png)
*<center>The LLM Choices tab visualizes annotator preferences across multiple LLM responses through result summaries and provider selection frequency analytics.</center>*

### Labels Tab

The Labels tab centralizes hallucination analysis, citation tracking, and label-based evaluation metrics across compared LLM providers.

![LLM label insights analytics dashboard](/assets/images/annotation_lab/8.1.0/12.png)
*<center>The Labels tab centralizes hallucination analysis, citation tracking, and label-based evaluation metrics across compared LLM providers.</center>*

### Quality Ratings Tab

The Quality Ratings section groups quality evaluation metrics into a dedicated analytics view.

![LLM quality score analytics dashboard](/assets/images/annotation_lab/8.1.0/13.png)
*<center>The Quality Scores tab provides structured analytics for reference quality, coherence, relevance, and coverage ratings across evaluated LLM providers.</center>*

The dashboard supports analytics for:
- Relevance
- Coverage
- Organization and coherence
- Reference quality
- Overall helpfulness

This enables teams to analyze qualitative evaluation trends across compared LLM providers.

</div>

<div class="h3-box" markdown="1">

## User Benefits

### Improved Analytics Discoverability

Structured navigation and contextual tabs make it easier to locate relevant operational insights, KPIs, and quality metrics.

### Better Scalability for Large Projects

Dedicated analytics sections reduce clutter and improve usability for projects containing large volumes of annotation and evaluation data.

### Cleaner and More Focused User Experience

Simplified layouts, optimized chart density, and standardized visual components reduce cognitive overhead during dashboard analysis.

### Faster Operational Decision-Making

Interactive filtering and centralized analytics provide quicker access to annotation progress, productivity trends, and quality insights.

### Improved Annotation Oversight

Project managers can monitor:
- Team productivity
- Review performance
- Annotation throughput
- Agreement trends
- LLM evaluation metrics

from a unified analytics environment.

### Enhanced Quality Monitoring

Dedicated analytics for label variability and agreement analysis help identify annotation inconsistencies and potential taxonomy issues earlier in the workflow.

### Optimized LLM Evaluation Workflows

Specialized dashboards for response comparison projects provide clearer visibility into annotator preferences and LLM evaluation behavior.

### More Efficient Navigation

The redesigned multi-tab layout eliminates excessive scrolling and improves movement between analytics categories and operational views.

</div>

<div class="h3-box" markdown="1">

## Example Workflow

A project manager overseeing a large healthcare annotation project requests Analytics access for their project. Once Analytics is approved and enabled by an administrator, the project manager can access the Analytics Dashboard directly from the project sidebar.

For more information about enabling Analytics access and permission management, see the [Analytics Permission Management](/docs/en/alab/analytics_permission) documentation.

Using the sidebar navigation, the manager switches between:

- **Overview** to review task completion and productivity metrics
- **Team Productivity** to analyze annotator throughput and review activity
- **Labels & Data Quality** to identify annotation imbalance and variability
- **Inter-Annotator Agreement** to investigate disagreement trends between reviewers
- **LLM Response Comparison** to evaluate annotator preferences across multiple LLM responses

Instead of navigating through a single long analytics page, the manager can move directly between focused dashboard sections and contextual tabs to locate specific operational insights quickly.

This enables:

- Faster operational analysis
- Improved annotation oversight
- Better quality monitoring
- More efficient reviewer coordination
- Streamlined large-scale project management workflows
</div>