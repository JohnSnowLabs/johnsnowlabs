---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Analytics Permission
permalink: /docs/en/alab/analytics_permission
key: docs-training
modify_date: "2025-11-27"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab


<div class="h3-box" markdown="1">

## Analytics Permission

By default, dashboards in the Analytics page are disabled for each project.  
Users can request that an _admin_ enable Analytics access for their project. These requests are automatically logged and managed through the **Analytics Requests** system, ensuring controlled access to potentially resource-intensive analytics computations.

### Analytics Requests

When a user submits a request to enable Analytics for a project, the request appears on the **Analytics Requests** page under the **Settings** menu.  
This page is accessible only to _admin_ users and lists all pending, approved, and denied requests, including details such as:
- The name of the project for which analytics access was requested  
- The user who initiated the request  
- The date of submission  

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/analytics_requests.png" style="width:100%;"/>

In addition to appearing on the **Analytics Requests** page, administrators are now **instantly notified in-app** whenever a new request is made.  
This real-time notification system ensures that admins are alerted immediately, without requiring separate communication (such as emails or messages).  
Admins can open the notification to review the pending request and take action directly—significantly speeding up response times and improving collaboration between users and administrators.

### Granting a Request

All requests granted by the _admin_ are listed under the **Granted** tab.  
The table includes:
- Project name  
- Requesting user  
- Admin who granted the request  
- Date of approval  
- Date of the most recent analytics update  

Admins can also **revoke previously granted requests** at any time from the same list.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/ar_granted.png" style="width:100%;"/>

### Denying or Revoking a Request

Denied or revoked requests are displayed under the **Denied/Revoked** tab, which includes similar details—showing who denied the request, when, and for which project.  
This provides a clear audit trail of all analytics permission decisions.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/ar_revoked.png" style="width:100%;"/>

### Summary

With the addition of **real-time admin notifications**, Analytics access requests are now handled more efficiently:
- Users can submit requests directly from their project settings.
- Admins receive immediate in-app alerts for new requests.
- Approvals and revocations can be performed instantly from the notification or the **Analytics Requests** dashboard.

This enhancement ensures smoother collaboration and faster activation of Analytics features across teams.


</div>