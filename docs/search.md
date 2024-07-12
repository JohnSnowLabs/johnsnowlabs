---
layout: page
page:
    aside: false      
mode: immersivebg
pagetitle: Search - John Snow Labs
title: Search
permalink: /search
show_subtitle: false
key: search
license: false
show_date: false
modify_date: "2023-11-24"
---


<div class="grid--container learn-hub container">
    <div class="main-docs search-results-wrapper">
        <div class="search-wrapper">
            <div class="search-input-wrapper">
                <input type="text" onclick="fetchAndPopulate()" id="search-input" placeholder="Search starts from 4 letters...">
            </div>                    
            <h2>Search results</h2>
            <ul id="results-container" class="results-container"></ul>
        </div>
    </div>
</div>