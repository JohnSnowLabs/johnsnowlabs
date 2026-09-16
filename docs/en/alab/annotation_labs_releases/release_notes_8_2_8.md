---
layout: docs
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Generative AI Lab 8.2.8
permalink: /docs/en/alab/annotation_labs_releases/release_notes_8_2_8
key: docs-licensed-release-notes
modify_date: 2026-09-16
show_nav: true
sidebar:
    nav: annotation-lab
---

<div class="h3-box" markdown="1">

**Generative AI Lab 8.2.8** is a maintenance release focused on platform stability and reliability under high workloads. This release improves resource allocation and request handling for the Annotation Lab pod to maintain availability during increased API traffic, while also addressing the display of pre-annotation suggestions in Visual NER projects.

## Improvements

### Improved Annotation Lab Pod Stability Under High API Load

**What's Improved**

Annotation Lab pod resource management and request handling have been improved to provide greater stability under sustained or high-volume API traffic.

CPU and memory requests are now configured for the Annotation Lab pod, providing Kubernetes with clearer resource requirements for scheduling and reducing the risk of resource starvation under load.

Additional improvements to application concurrency and outbound request handling help prevent long-running requests from exhausting available request-processing capacity. This reduces the likelihood of readiness probe failures during periods of increased activity and helps maintain application availability.

The updated configuration has been validated through stress testing with 100 concurrent users across the available load-test scenarios, without observed readiness probe failures.

**User Benefits**

- Improved platform availability during periods of high API traffic
- More reliable Kubernetes scheduling through defined CPU and memory requests
- Reduced risk of readiness probe failures caused by resource contention
- Better handling of concurrent and long-running requests
- Improved stability for production deployments under increased workload

## Bug Fixes

- **Pre-Annotation Suggestions Not Displayed in Visual NER Projects**

  Pre-annotation results could exist for a Visual NER task without being rendered on the labeling page. The annotations became visible only after copying the pre-annotation completion into a new completion, even though the original pre-annotation data was already available.

  Pre-annotation suggestions are now displayed directly in the original completion on the Visual NER labeling page, allowing users to review and work with generated annotations without creating an additional completion.

---
## Versions

</div>

{%- include docs-annotation-pagination.html -%}