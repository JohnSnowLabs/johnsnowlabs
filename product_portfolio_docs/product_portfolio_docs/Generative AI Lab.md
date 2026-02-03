# Generative AI Lab Product Description

## Overview

Generative AI Lab is John Snow Labs’ enterprise no-code platform for
document annotation, AI model training, and deployment, specifically
engineered for high-compliance environments. The platform enables domain
experts to **extract structured information from unstructured
documents** and train custom language models without requiring coding
expertise or data science knowledge. Generative AI Lab addresses a
critical enterprise challenge: training/tuning task-specific AI models
with speed and transparency through **regulatory-grade**
human-in-the-loop workflows essential for industries like healthcare,
finance, and legal.

**Built on Kubernetes architecture**, Generative AI Lab emphasizes
**enterprise readiness** and **robust governance**. It provides
comprehensive model lifecycle management from annotation through
production deployment while maintaining **data sovereignty** and
**regulatory compliance**. The system supports processing of text,
images, audio, video, PDF, and HTML content across 250+ languages, with
access to over 130,000 pre-trained models from the NLP Models Hub. It
provides built-in audit trails, role-based access control, immutable
logs that support regulatory reviews and internal compliance checks
through dedicated audit dashboards. All stages of the LLM lifecycle –
from prompt engineering and fine-tuning to validation and deployment –
occur in a **secure, HIPAA-compliant environment**.

Core differentiators include zero data sharing with external parties,
air-gapped deployment capabilities, and **state-of-the-art accuracy**
with built-in **regulatory-grade compliance features**. The platform
integrates seamlessly with existing enterprise infrastructure through
RESTful APIs and supports unlimited users, projects, and models without
usage restrictions.

## Use Cases

**Document** **De-identification:** Remove PHI/PII from medical records
by combining automated detection with expert review to meet regulatory
standards. The platform allows processing of any type of medical text
document (patient notes, discharge summaries, radiology reports,
pathology documents, etc.) while maintaining data utility for downstream
analytics via its entity level configurations for **obfuscation** or
**masking**. HIPAA-compliant workflows support both safe harbor and
expert determination methods with comprehensive audit trails and
validation reporting. This empowers use cases like clinical data
sharing, population health research, or internal analytics **without
privacy risk**, as demonstrated by Providence Health’s use-case (see
below).

**Clinical Data Curation:** Generative AI Lab allows teams to automate
the extraction of structured information from unstructured clinical
narratives including patient notes, EHRs, and clinical trial documents.
Via the built-in integration with NLP Models Hub, it supports AI-based
extraction of over 400 types of medical entities (diagnosis, treatments,
medication, cancer staging, social determinants of health, etc),
assertion tags for the entities (e.g. past, present, hypothetical),
relationships, standard coding alignment (e.g. ICD-10, Snomed, RxNorm,
LOINC, CPT). In addition, users have the option to define and use
**prompt-based extraction** of data points via LLM analysis (e.g.
ZeroShot Models, Open AI, Claude) and custom **rules** (syntactic and
dictionary).

**LLM Evaluation and Comparison**: Generative AI Lab offers native LLM
evaluation capabilities, enabling complete end-to-end workflows for
importing prompts, generating responses via external providers (OpenAI,
Azure OpenAI, Claude, Amazon SageMaker), and collecting human feedback
within a unified interface. It supports both single-model assessment and
side-by-side comparative analysis, with dedicated analytics dashboards
providing statistical insights and visual summaries of evaluation
results.

**No-Code Healthcare Model Development:** Generative AI Lab provides
domain experts with intuitive interfaces for custom model training,
fine-tuning, and deployment without programming requirements.
Pre-configured templates support common healthcare NLP tasks including
clinical named entity recognition, assertion detection, and relation
extraction. **Human-in-the-loop annotation workflows** accelerate model
development through AI-assisted pre-labeling, active learning, and
consensus-based quality assurance with medical expert validation.

**Annotation as a** **Service**: Generative AI Lab's comprehensive
annotation workflow capabilities accelerate data preparation through
AI-assisted pre-annotation, active learning, model training and prompt
based pre-annotations. The platform's AI-assisted pre-labeling
automatically annotates documents using pre-trained models, reducing
manual annotation time by up to 80% while maintaining accuracy through
human validation. **Custom annotation workflows** support role-based
collaboration with distinct manager, annotator, and reviewer permissions
ensuring quality control and efficient task distribution. Analytics
dashboards provide real-time **consensus analysis**, inter-annotator
agreement metrics, and performance tracking to facilitate team
coordination and quality assurance. Side-by-side annotation comparison
views enable annotators to learn from reviewer feedback through visual
difference highlighting and comment-based guidance, accelerating skill
development and consistency improvement. Project-based access control
ensures users only access authorized projects while maintaining data
security and compliance requirements. Automated task assignment and
serving capabilities distribute workload efficiently based on annotator
expertise and availability. The platform processes enterprise-scale
datasets while maintaining HIPAA compliance and regulatory submission
requirements with comprehensive **audit trails** and immutable logging
dashboards.

## Key Features & Capabilities

Generative AI Lab offers a rich set of features purpose-built for
**healthcare AI development**:

- **High Throughput Document Annotation** eliminates manual spreadsheet
  workflows and enables processing of thousands of documents daily
  through built-in quality assurance mechanisms. The platform provides
  high productivity user interfaces with shareable annotation
  guidelines, reviewer comment systems, and consensus analysis tools
  that accelerate team agreement on complex labeling decisions. Quality
  control features include inter-annotator agreement tracking, duplicate
  task identification, and real-time collaboration capabilities.

- **AI-Powered Labeling and Pre-Annotation** accelerates annotation
  workflows without compromising quality through automatic text
  pre-labeling for medical records analysis, diagnosis coding, or
  training data preparation. The system integrates with existing
  workflows via comprehensive APIs, enabling seamless data exchange with
  EHRs, data lakes, and ML pipelines. Zero-shot prompts support
  classification, named entity recognition, and relation extraction
  tasks directly within secure environments.

- **No-Code Model Training and** **Tuning** enables domain experts to
  fine-tune models based on domain-specific data without ML engineering
  expertise. Active learning is built-in: the Lab can auto-train
  improved model versions as new labeled examples are added, while
  built-in performance metrics facilitate model comparison and
  evaluation. Transfer learning capabilities leverage pre-trained models
  from the extensive NLP Models Hub, with automated model improvement
  through continuous feedback loops.

- **Regulatory-Grade De-identification** removes PHI from medical
  records through automated detection combined with expert human review
  to meet regulatory standards. The platform supports both
  **obfuscation** and **masking** approaches with **entity-level
  configuration** and consistent de-identification across entire
  annotation tasks. Human-in-the-loop validation ensures compliance with
  HIPAA safe harbor and expert determination methods.

- **Model and Prompt Management** provides access to ready-to-deploy NLP
  models and pipelines through searchable interfaces filtered by task or
  domain. Private model hubs enable secure sharing of custom models,
  rules, and prompts within organizational boundaries. Live playground
  environments support data experimentation and model testing before
  production deployment.

- **LLM Integration and Bootstrap Capabilities** leverage large language
  models to experiment and prepare training examples for classification,
  NER, and relation detection tasks. Generative AI Lab currently
  integrates with OpenAI, Anthropic and SageMaker endpoints to enable
  text classification and NER, while custom prompt engineering
  interfaces support domain-specific model adaptation.

- **Advanced Document Processing** supports flexible document splitting
  into sentences, paragraphs, or pages for precise section-level
  labeling. Adaptive taxonomy features enable customization of
  annotation schemas to match specific section requirements, reducing
  noise and improving annotation accuracy on long documents.

- **Enterprise Data Curation and Governance** support complex workflows
  with comprehensive transparency and auditability features. Custom
  review workflows with role-based access control ensure appropriate
  data handling, while version tracking monitors all changes with
  complete audit trails. Quality metrics dashboards provide real-time
  monitoring of team output and annotation consistency.

- **Multi-Project and Team Management** enable coordination of complex
  annotation workflows across multiple teams and projects. Advanced
  analytics provide insights into annotation progress and quality, while
  entity and project-level guidelines integration ensure consistency
  across teams. Custom workflow configuration supports comment systems,
  feedback mechanisms, and approval processes tailored to organizational
  requirements.

- **Enterprise Security Architecture** provides role-based access
  control, multi-factor authentication, and integration with Active
  Directory and LDAP systems. The platform supports cloud, on-premise,
  and air-gapped deployment options to meet diverse security
  requirements across healthcare, finance, and legal organizations.

<!-- -->

- **Support for Multiple Input Formats** enables annotation and
  processing across diverse document types including text, PDF, image
  (PNG and JPEG), HTML, and audio/video. Integrated Visual NLP pipelines
  allow text extraction from PDF and image documents for manual and
  AI-powered annotations.

## Performance & Benchmarks

- **PHI De-Identification Accuracy:** Generative AI Lab’s solution holds
  the state-of-the-art in automated patient data de-identification. In a
  recent benchmark study, it achieved **96% F1-score** on identifying
  protected health information – outperforming Azure’s health NLP (91%),
  AWS Comprehend Medical (83%), and even OpenAI’s GPT-4-based model
  (79%). This highlights Generative AI Lab’s **precision in critical
  compliance tasks**. The JSL de-identification model also makes far
  fewer errors: 50% fewer than AWS, 475% fewer than Azure, and 575%
  fewer than Google’s service, while **outperforming ChatGPT by 33%** on
  a large real-world clinical note dataset. Such benchmarks underscore
  the platform’s focus on **high factual accuracy and reliability** over
  hype.

## Deployment & Compliance

**Cloud Platform Integration** supports one-click deployment through AWS
Marketplace with AMI-based installations, Azure Marketplace deployment
via AKS with auto-scaling capabilities.

**On-Premise Architecture** enables air-gapped deployments with complete
network isolation after initial setup. Minimum system requirements
include 8-Core CPU, 32GB RAM, and 512GB SSD storage, with **recommended
configurations scaling to 4-GPU instances** with 48 CPU cores and 192GB
RAM for visual document processing workloads.

**Security Framework** implements zero data sharing policies with all
processing occurring within customer infrastructure. The platform
provides **multi-factor authentication, role-based access control**, and
integration with enterprise identity providers including LDAP and Active
Directory. Point-to-point encryption protects all data transmission with
comprehensive vulnerability scanning and network segmentation
capabilities.

**Regulatory Compliance** includes native HIPAA compliance through
air-gapped deployment options and PHI handling with full audit
capabilities. The platform supports FDA AI/ML Action Plan requirements
with lifecycle monitoring and human oversight controls.

**Enterprise Governance** features provide full audit trails with
time-stamped, tamper-proof logging and compliance reporting through
built-in dashboards. **Data lineage tracking** covers complete
processing workflows with change management controls for deployment and
rollback procedures.

**Infrastructure Requirements** support deployment across multi-cloud
environments with hybrid architecture capabilities. Container-based
deployment ensures consistent environments with Docker portability and
**Kubernetes orchestration for elastic scaling**. Private model hub
capabilities enable secure resource sharing within organizational
boundaries.

## Real-World Use Cases

**GE Healthcare Radiology Report Processing Use Case** demonstrates
large-scale clinical document analysis for patient cohort identification
in pharmaceutical partnerships. The implementation processes radiology
reports to extract structured clinical entities, relationships, and
normalized representations from unstructured narratives containing
patient symptoms, procedures, and findings. Complex annotation workflows
handle over 100 different entity types with multi-layer NER, assertion
detection, and relation extraction across 500+ reports. In this project
Generative AI Lab served as a human in the loop tool for tuning the used
models and for results validation. The obtained solution enables
accurate patient selection from larger radiology datasets while
maintaining HIPAA-compliant de-identification through automated PHI
removal and masking capabilities. **  **

**Novartis Pharmaceutical Document Migration** showcases
enterprise-scale document classification and entity extraction for
regulatory submission workflows. The platform processes 48 different
artifact types from unstructured legacy systems, extracting 25+ metadata
attributes including investigator information, dates, and regulatory
identifiers. In this usecase, the AI-assisted data preparation achieved
99% classification accuracy and 97% entity extraction accuracy, reducing
processing time from 100 days to 20 days for one million documents while
maintaining regulatory compliance standards and audit trails required
for pharmaceutical submissions. Generative AI Lab was used to validate
results and to tune the AI models included in the final processing
pipeline.

**Coda Oncology Data Curation** enables regulatory-grade real-world
evidence generation from EMR data across patient treatment journeys. The
platform abstracts complex oncology information including molecular
markers, treatment regimens, adverse events, and outcomes from
fragmented multi-modal data sources. Clinical expertise integration
combines NLP model outputs with Generative AI Lab human validation
workflows to ensure data quality standards required for clinical trial
research and pharmaceutical applications, supporting treatment
decision-making across healthcare providers.

**FDA Opioid Safety Surveillance** use case demonstrates regulatory
agency adoption for pharmacovigilance activities using MIMIC-III
database discharge summaries. The implementation combines rule-based
algorithms with deep learning methods to identify opioid-related adverse
drug events (ORADE) with accuracy metrics of 0.61/0.6/0.64/0.62 for
accuracy/recall/precision/F1 scores. Drug safety signal detection maps
extracted drug-event pairs to standardized terminologies while providing
interactive visualization dashboards for regulatory review and emerging
safety issue identification.

## Customer Proof Points

Generative AI Lab is powering the future of AI with 7.5+ Million
expert-led annotation hours recorded over the last 3 years, across the
500+ leading pharma and healthcare organizations. The platform supports
thousands of documents processed daily with built-in quality assurance
workflows, enabling enterprise-scale data preparation for regulated
industries requiring HIPAA compliance and audit trail documentation.

Platform Utilization Metrics show high scalability with no restrictions
on users, projects, or documents within customer deployments. The
Kubernetes-based auto-scaling architecture automatically adjusts
computational resources based on demand, supporting concurrent
multi-user access while maintaining consistent performance across
varying workloads. Pay-as-you-go billing charges only for active feature
usage, optimizing cost efficiency for enterprise teams.

Deployment Flexibility encompasses availability through AWS Marketplace
and Azure Marketplace with one-click deployment capabilities. Air-gapped
and on-premise deployment options support high-compliance industries,
including healthcare, life sciences, finance, and insurance, where data
sovereignty requirements mandate local processing. Zero data sharing
architecture ensures all processing occurs within customer
infrastructure with no external data transmission.

Security and Compliance Validation include **enterprise-grade security**
with role-based access control, multi-factor authentication, and
tamper-proof audit logs. HIPAA-compliant operations feature
Human-in-the-Loop workflows with expert validation, identity provider
integration, and real-time monitoring dashboards. Full audit trails and
encryption capabilities meet regulatory requirements for healthcare,
legal, and financial sector applications.
