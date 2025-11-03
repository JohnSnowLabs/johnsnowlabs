---
layout: docs
header: true
seotitle: Release Notes  | Terminology Server | John Snow Labs
title: Terminology Server Release Notes
permalink: /docs/en/terminology_server/release/latest_release
key: docs-term-server
modify_date: "2025-09-30"
show_nav: true
sidebar:
    nav: term-server
---

<div class="h3-box" markdown="1">

<p style="text-align:center;" markdown="1">Release date: {{ page.modify_date | date: '%m-%d-%Y' }}</p>

## Authorization and User Management

**Authenticated appilcation access** 

A secure login mechanism ensures user authentication prior to granting access to the Terminology Server.
  ![Screenshot of login](/assets/images/term_server/v3/login_page.png)

**User Management**

The Terminology Server includes basic user management capabilities. Users with administrative privileges can add, remove, or update user accounts as needed. This functionality is available through the Manage Users option in the navigation panel when clicking on the user account name.

Administrators can create and manage accounts to ensure proper system access
  ![Screenshot of user management](/assets/images/term_server/v3/user_management.png)

**ValueSet Access Management**

Terminolgy Server implements user roles and permissions to control access to different features and valuesets within the Terminology Server.
- Regular users can access the terminology search and value set management features based on their assigned permissions
- Users can share created value sets with other users, facilitating collaboration and consistency in terminology usage.
- Shared value sets can be accessed and utilized by authorized users based on their permissions.
  ![value set sharing](/assets/images/term_server/v3/valueset_share.gif)
 

**Customize Search Results View**


The application provides a flexible search results table that can be customized to match each user’s needs. Columns can be selected or hidden, allowing users to focus on the information most relevant to their workflow. This configurable view reduces clutter, streamlines results, and highlights key data points for faster review and decision-making.
 ![Screenshot of column management](/assets/images/term_server/v3/column_management.gif)

**Secured API Access** 

- API access is secured through API keys linked to user accounts, ensuring that only authorized users can interact with the API endpoints.

</div><div class="h3-box" markdown="1">

## Improvements

* Improved hierarchy display for clearer visualization and navigation of concept hierarchies.
  ![hierarchy display improvements](/assets/images/term_server/v3/hierarchy.gif)
* Enhanced query performance for faster search results.
* Updated deployment script for quicker setup and configuration.
* Added a dedicated _Search_ button in the UI for a smoother user experience.
* Improved spell checker to deliver more accurate suggestions and corrections.


</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>

<ul class="pagination pagination_big">
  <li class="active"><a href="release_note_v3">v3</a></li>
  <li><a href="release_note_v2">v2</a></li>
  <li><a href="release_note_v1">v1</a></li>
</ul>