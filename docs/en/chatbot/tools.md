---
layout: docs
header: true
seotitle: Medical Chatbot | John Snow Labs
title: Tools
permalink: /docs/en/chatbot/tools
key: docs-healthcare-gpt
modify_date: "2024-01-19"
show_nav: true
sidebar:
    nav: healthcare-gpt
---

The Medical Chatbot is equipped with three dynamic tools, each tailored to meet different information needs and research requirements. These tools are `MedResearch`, `Wikipedia`, and `John's Memory`, collectively providing a comprehensive solution for a wide range of queries.

## MedResearch: Your Gateway to Academic Medical Research

`MedResearch` stands as the cornerstone of the Medical Chatbot, offering exhaustive coverage of academic papers and research results. This tool is meticulously designed to query multiple prestigious databases:
- PubMed
- BioRxiv
- MedRxiv

along with specialized custom knowledge bases such as:
- Drug Leaflets - a Knowledge Base that indexes Drug data published by [FDA](www.fda.gov)
- Cigna Insurance Plans - a Knowledge base that indexes insurance plans (large PDF documents) offered by Cigna  

Whether you're looking for the latest findings in a specific medical field, detailed drug information, or comprehensive research outcomes, MedResearch provides direct access to a vast repository of academic resources. This feature is especially valuable for medical professionals, researchers, and students seeking to base their work on the most current and authoritative sources.

For questions targeting a certain KB, you can turn available KBs on and off according to your preference. 

![Select the KB you want to target with your question](\assets\images\chatbot\KBSelection.png)


> **_NOTE:_**  To enforce the use of this tool add the following sentence at the end of your query: **Ask MedResearch.**


## Wikipedia: Answering Short or Generic Questions

For users seeking quick answers to short or generic questions, the Medical Chatbot integrates seamlessly with Wikipedia. This feature is designed to fetch concise and reliable information from the vast expanse of Wikipedia's medical content. Whether it's a brief overview of a medical condition, historical context, or general health information, this tool ensures users can obtain quick answers efficiently. It's an excellent resource for those in need of rapid, accessible, and accurate information without the need for deep research.

> **_NOTE:_**  To enforce the use of this tool add the following sentence at the end of your query: **Ask Wikipedia.**

## John's Memory: Specialized in Summarization and General Queries

John's Memory is a versatile feature within the Medical Chatbot, dedicated to summarization tasks and answering general questions. This tool is particularly useful when users need a succinct summary of extensive information or when they have broad questions that do not require deep, research-level detail. John's Memory employs advanced NLP (Natural Language Processing) techniques to comprehend, interpret, and condense information, making it an invaluable asset for users who need quick insights or overviews.

