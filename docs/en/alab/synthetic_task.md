---
layout: docs
comment: no
header: true
seotitle: NLP Lab | John Snow Labs
title: Import Documents
permalink: /docs/en/alab/synthetic_task
key: docs-training
modify_date: "2023-08-19"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

## Synthetic task generation with ChatGPT 
With NLP Lab 5.2, you can harness the potential of synthetic documents generated by LLMs such as ChatGPT. This integration allows you to easily create diverse and customizable synthetic text for your annotation tasks, enabling you to balance any entity skewness in your data and to train and evaluate your models more efficiently. 

NLP Labs offers seamless integration with ChatGPT, enabling on-the-fly text generation. Additionally, NLP Labs provides the flexibility to manage multiple service providers key pairs for robust and flexible integration. These service providers can be assigned to specific projects, simplifying resource management. During the integration process, Each Service Provider Key can be validated via the UI (User Interface), ensuring seamless integration. 

Once the service provider integration is completed, it can be utilized in projects that can benefit from the robust capabilities of this new integration. Text generation becomes straightforward and effortless. Provide a prompt adapted to your data needs (you can test it via the ChatGPT app and copy/paste it to NLP Lab when ready) to initiate the generation process and obtain the required tasks. Users can further control the results by setting the "Temperature" and the "Number of text to generate." The "Temperature" parameter governs the "creativity" or randomness of the LLM-generated text. Higher temperature values (e.g., 0.7) yield more diverse and creative outputs, whereas lower values (e.g., 0.2) produce more deterministic and focused outputs. 

The NLP Lab integration delivers the generated text in a dedicated UI that allows users to review, edit, and tag it in place. After an initial verification and editing, the generated texts can be imported into the project as Tasks, serving as annotation tasks for model training. Additionally, the generated texts can be downloaded locally in CSV format, facilitating their reuse in other projects. 

NLP Labs will soon support integration with additional service providers, further empowering our users with more powerful capabilities for even more efficient and robust model generation. 

![Synthetic text](/assets/images/annotation_lab/5.2.2/1.gif)
