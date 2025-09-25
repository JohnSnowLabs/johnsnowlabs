---
layout: docs
header: true
seotitle: Release Notes  | Terminology Server | John Snow Labs
title: v3 Release Notes
permalink: /docs/en/terminology_server/release_notes/release_notes_v3
key: docs-term-server
modify_date: "2025-09-30"
show_nav: true
sidebar:
    nav: term-server
---


<p style="text-align:center;">Release date: {{ page.modify_date | date: '%m-%d-%Y' }}</p>

## Authorization and User Management

**Authenticated appilcation access** 

A secure login mechanism ensures user authentication prior to granting access to the Terminology Server.
  ![Screenshot of login](/assets/images/term_server/v3/login_page.png)

**User Management**

Basic user management features are present in the Terminology Server application. The user with the admin privilege can add or remove other users from the system or can edit user information if necessary. This feature is available by selecting the Manage Users option menu from the navigation panel when clikinng on the user account name.

Admin users can create and manage user accounts.
  ![Screenshot of user management](/assets/images/term_server/v3/user_management.png)

**ValueSet access Management**

Terminolgy Server implements user roles and permissions to control access to different features and valuesets within the Terminology Server.
- Regular users can access the terminology search and value set management features based on their assigned permissions
- Users can share created value sets with other users, facilitating collaboration and consistency in terminology usage.
- Shared value sets can be accessed and utilized by authorized users based on their permissions.
  ![value set sharing](/assets/images/term_server/v3/valueset_share.gif)
 

**Secured API Access** 

- API access is secured through API keys linked to user accounts, ensuring that only authorized users can interact with the API endpoints.

## Improvements

* Hierarchy Display improvements for better visualization and navigation of concept hierarchies.
  ![hierarchy display improvements](/assets/images/term_server/v3/hierarchy.gif)
* Enhanced query performance for quicker search results.
* Improved the deployment script for faster setup and configuration.
* Added a Search button to the UI for better user experience.
* Spell Checker Improvements - Enhanced spell checker to provide more accurate suggestions and corrections for misspelled terms.
