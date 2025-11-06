---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Synthetic Task Generation
permalink: /docs/en/alab/synthetic_task
key: docs-training
modify_date: "2024-03-19"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

Generative AI Lab allows you to create diverse and customizable synthetic documents using Large Language Models (LLMs) such as ChatGPT or Azure OpenAI. This feature helps balance entity distributions in your dataset, improve model performance, and generate high-quality examples for annotation, testing, and model evaluation.

Synthetic document generation supports multiple methods, including **Proportional Augmentation** and **Templatic Augmentation**, which expand dataset diversity and improve robustness.  
The use of these capabilities depends on having an LLM service provider configured in the system.

Once the integration is set up, synthetic data generation becomes a straightforward and efficient way to enrich your projects with automatically generated tasks. 

<div class="h3-box" markdown="1">

### Generate synthetic tasks using Azure OpenAI
You can generate synthetic tasks from any configured LLM provider (e.g., OpenAI or Azure OpenAI).  
Here’s a quick guide:

**Setting up and Validating the Service Provider:**

1.  From the **Tasks** page, click **Import** and navigate to the **Generate Synthetic Task** tab.
2.  Provide an appropriate prompt in the **Write Prompt** field and click the settings icon on the right side of the page.
3.  Enter the API endpoint URL and secret key, then click **Validate**.
4.  After validation, set the desired **Temperature** and **Number of Tasks to Generate**.
5.  Click **Generate** to create synthetic tasks.

![Synthetictaskgeneration](/assets/images/annotation_lab/5.5.0/4.gif)

</div>

For synthetic tasks, provide a prompt adapted to your data needs to initiate generation.  
The **Temperature** parameter controls the creativity or randomness of the LLM-generated text:
- Higher values (e.g., 0.7) yield more diverse and creative outputs.  
- Lower values (e.g., 0.2) produce more deterministic and focused outputs.  
The **Number of Texts to Generate** field determines how many tasks will be created.

![Synthetic text](/assets/images/annotation_lab/5.2.2/1.gif)

</div>

####  Proportional Augmentaiton

Proportional Augmentation enhances data quality by using testing and transformation techniques to generate new data based on an existing dataset.  
It is especially effective for improving model performance by addressing weaknesses such as case sensitivity, typos, or formatting inconsistencies.  
This approach is useful for **bias and robustness testing**, ensuring that your models produce reliable, high-quality results across diverse inputs.  
After selecting test types and defining `max_proportion`, click **Generate Results** to create augmented tasks. The system will enhance existing tasks and generate new ones accordingly.

![genAI650](/assets/images/annotation_lab/6.5.0/2.gif)

Another way to generate augmented tasks is through "**Templatic augmentation**".

####  Templatic Augementation
Templatic Augmentation creates new data by using templates or patterns that are similar in structure and context to the original input. This method depends a lot on the templates provided by the user. There are two options for using this approach:
 
 **A. Manually Add Templates**
 Users can manually choose templates along with the available labels. They can choose how many results to generate for each template using a scroll bar, which can be set from 1 to 50.

![genAI650](/assets/images/annotation_lab/6.5.0/3.gif)

**B. Import Templates from File**  
You can also bulk import templates instead of adding them manually.  
Use the **Import Templates** option to upload a file (JSON or CSV) containing predefined template–label mappings.  
This is ideal for teams who maintain large libraries of reusable templates or want to migrate existing augmentation setups from other projects.  
Once uploaded, all templates in the file will appear in the list and can be edited or adjusted before generating synthetic tasks.
