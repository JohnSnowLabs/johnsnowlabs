---
layout: docs
header: true
seotitle: Release Notes  | Terminology Server | John Snow Labs
title: Terminology Server Release Notes
permalink: /docs/en/terminology_server/release/latest_release
key: docs-term-server
modify_date: "2026-03-01"
show_nav: true
sidebar:
    nav: term-server
---

<div class="h3-box" markdown="1">

<p style="text-align:center;" markdown="1">Release date: {{ page.modify_date | date: '%m-%d-%Y' }}</p>

## Improvements

* Added assertion results display to Document Search functionality

  ![Assertions Results](/assets/images/term_server/assertion_result.png)

* Migrated public valueset download scripts to Celery worker for improved performance
* Dynamic client secret creation during installation

## Bugfixes

* Fixed issue where running setup scripts multiple times reset admin user credentials


<div class="prev_ver h3-box" markdown="1">

## Versions

</div>


<ul class="pagination pagination_big">
  <li class="active"><a href="release_note_v4">v4</a></li>
  <li><a href="release_note_v3">v3</a></li>
  <li><a href="release_note_v2">v2</a></li>
  <li><a href="release_note_v1">v1</a></li>
</ul>
