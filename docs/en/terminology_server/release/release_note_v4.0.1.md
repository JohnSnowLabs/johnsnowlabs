---
layout: docs
header: true
seotitle: Release Notes  | Terminology Server | John Snow Labs
title: Terminology Server Release Notes
permalink: /docs/en/terminology_server/release/release_note_v4.0.1
key: docs-term-server
modify_date: "2026-04-01"
show_nav: true
sidebar:
    nav: term-server
---

## Terminology Server v4.0.1 Release Notes

<p style="text-align:center;">Release date: {{ page.modify_date | date: '%m-%d-%Y' }}</p>

## Improvements

* Added assertion results display to Document Search functionality

  ![Assertions Results](/assets/images/term_server/assertion_result.png)

* Migrated public valueset download scripts to Celery worker for improved performance
* Dynamic client secret creation during installation

## Bugfixes

* Fixed issue where running setup scripts multiple times would reset admin user credentials

<div class="prev_ver h3-box" markdown="1">

## Versions

</div>

{%- include docs-terminology-pagination.html -%}
