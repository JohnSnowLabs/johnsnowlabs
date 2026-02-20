---
layout: docs
header: true
seotitle: Terminology Server | John Snow Labs
title: Terminology Server 
permalink: /docs/en/terminology_server/features/mcp_server
key: docs-term-server
modify_date: "2025-04-01"
show_nav: true
sidebar:
    nav: term-server
---
### MCP Server - Agent Connectivity and Tool Registration

Agents—software systems, automation bots, clinical support tools, and data analytics platforms—can connect directly to the Terminology Server, leveraging its Model Context Protocol (MCP) Server architecture for seamless interoperability and robust terminology operations. Since Terminology Server exposes all its search functionality through well-defined, programmable interfaces, agents are able to integrate, query, and utilize terminology resources in real time.

Every search feature supported by Terminology Server—including Concept Search, Context Resolution, Code Search, Document Search , can be registered as distinct tools within agent frameworks. This allows agents to systematically employ these features as callable modules for automating workflows, supporting clinical and research operations, or powering decision-support engines.

Agents can dynamically select, compose, or orchestrate these tools to build workflows such as medical concept lookup, code mapping, bulk document entity extraction, context-aware terminology research, and compliance checks. This tool registration framework maximizes flexibility, reliability, and scalability—agents perform tasks ranging from data enrichment and integration to knowledge discovery and regulatory monitoring, all by programmatically accessing the Terminology Server MCP endpoints.

By registering Terminology Server search modules as agent tools, organizations empower autonomous systems to take full advantage of advanced terminology intelligence, real-time mapping, and data-driven insights, ensuring operational consistency, precision, and interoperability.

Here is a sample notebook containing how you can use Terminology Server with an AI Agent.
