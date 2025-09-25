---
layout: docs
header: true
seotitle: Release Notes  | Terminology Server | John Snow Labs
title: v3 Release Notes
permalink: /docs/en/terminology_server/release_notes
key: docs-term-server
modify_date: "2025-09-30"
show_nav: true
sidebar:
    nav: term-server
---

<p style="text-align:center;">Release date: {{ page.modify_date | date: '%m-%d-%Y' }}</p>

## Authorization and User Management

- A secure login page is implemented to authenticate users before they can access the Terminology Server.
  ![Screenshot of login](/assets/images/term_server/v3/login_page.png)
- Implement user roles and permissions to control access to different features and valuesets within the Terminology Server.
- Admin users can create and manage user accounts.
  ![Screenshot of user management](/assets/images/term_server/v3/user_management.png)
- Regular users can access the terminology search and value set management features based on their assigned permissions
- API access is secured through API keys linked to user accounts, ensuring that only authorized users can interact with the API endpoints.

## Share valuesets among users

- Users can share created value sets with other users, facilitating collaboration and consistency in terminology usage.
- Shared value sets can be accessed and utilized by authorized users based on their permissions.
  ![value set sharing](/assets/images/term_server/v3/valueset_share.gif)

## Improvements

* Hierarchy Display improvements for better visualization and navigation of concept hierarchies.
  ![hierarchy display improvements](/assets/images/term_server/v3/hierarchy.gif)
* Enhanced query performance for quicker search results.
* Improved the deployment script for faster setup and configuration.
* Added a Search button to the UI for better user experience.
* Spell Checker Improvements - Enhanced spell checker to provide more accurate suggestions and corrections for misspelled terms.


## Versions
<ul class="pagination pagination_big">
    <li><a href="release_notes_v3">v3</a></li>
    <li><a href="release_notes_v2">v2</a></li>
    <li><a href="release_notes_v1">v1</a></li>
</ul>
