---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Audit Logs Dashboard
permalink: /docs/en/alab/audit_logs_dashboard
key: docs-training
modify_date: "2026-02-13"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

## System-Wide Visibility, Accountability, and Compliance 
Since version [7.8](/docs/en/alab/annotation_labs_releases/release_notes_7_8.md), Generative AI Lab introduces the Audit Logs Dashboard, a HIPAA-compliant, system-wide auditing solution that provides centralized visibility into platform activity across projects and users. This feature enables organizations to track critical actions, support compliance requirements, and maintain accountability in regulated environments.

### Audit Logging Overview 

The Audit Logs Dashboard captures and displays system events related to user activity, data access, and platform operations. Logged events include:

- User actions across projects.

- Data access, modifications, deletions, and exports.

- Project lifecycle events (creation and deletion).

- API usage and system response codes. 

All events are recorded with timestamps and associated user information to ensure traceability.

![78image](/assets/images/annotation_lab/7.8/1.png)

### Dashboards and Filtering

Audit data is presented through built-in dashboards and visualizations that help users review activity at both project and system levels. Available views include:

- Project activity and lifecycle trends.

- Export monitoring and tracking.

- User behavior and access patterns.

- System-level usage insights.

Users can filter audit data by project, user, event type, and date range to create targeted views for investigation or review.  

![78image](/assets/images/annotation_lab/7.8/2.png)

### Data Retention and Configuration
Audit Logs Dashboard retention is configurable, allowing organizations to align with internal policies and regulatory requirements. Audit logging can be enabled globally during installation or upgrade using an installer flag. Required backend services, including Elasticsearch, are automatically provisioned if not already present.



</div>