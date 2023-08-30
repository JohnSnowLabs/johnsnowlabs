---
layout: docs
comment: no
header: true
seotitle: NLP Lab | John Snow Labs
title: LLM Prompts
permalink: /docs/en/alab/llm_prompts
key: docs-training
modify_date: "2023-08-19"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

<style>
es {
    font-weight:400;
    font-style: italic;
}
</style>

## Entity Extraction and Pre-Annotation via GPT Prompting

The highlight of this release is the integration with an external service provider, Open AI, to expand and deepen the range of prompts available for pre-annotation (in addition to the Zero Shot entity and relation prompts already supported). This feature:.

- **Broadens Prompt Possibilities**: By integrating with Open AI LLM models, users can tap into a more diverse set of prompts, leveraging external expertise to craft pre-annotations, as an alternative pre-annotation solution or when pre-trained models are not available.

- **Efficient Entity Extraction**: As current LLMs, GPT family included, are not very good at entity recognition tasks, NLP Lab included a post-processing step on the result provided by LLM. This improves entity identification and helps precisely locate the entities in the given text. These entities, carefully curated and aligned with NLP Lab pre-annotation requirements pave the way for a more efficient and streamlined annotation experience.

The following sections explain in detail how to define and use GPT prompts. 

### Setting Up the Integration with Open AI service
Integrating “ChatGPT” into the NLP Lab has been designed to be a straightforward process, ensuring users can harness the power of external expertise seamlessly. It consists of three easy steps:

**Integrations Page**: Navigate to the Integrations Page located within the System Settings. This is the hub where all external service providers, including Open AI’s GPT Models, can be defined and managed.

![Integration](https://github.com/JohnSnowLabs/annotationlab/assets/57619662/7c1fa3b2-c472-488d-b8aa-b0a9be5e05d3)

**Define the Service Provider**: To initiate the integration, users are required to provide specific details:
- **Service Provider Name**: This is the identifier for the external service, which in this case would be “ChatGPT” or any other name you prefer to use.
- **Secret Key**: Every external service comes with a unique Secret Key that ensures secure communication between the platforms. Enter the Secret Key associated with your Open AI subscription here. To ensure the integration process is error-free, users can validate the provided Secret Key directly within the form. This validation step ensures that the connection is secure and that the key is correct.

**Project Association**: Once a successful connection with “ChatGPT” (or any external LLM service provider) is established, it doesn't end there. The integrated service will now be available for association with selected projects. This means users can decide which projects will benefit from the “ChatGPT” integration and enable it accordingly.
The Open AI integration allows users to tap into a vast reservoir of external expertise, enhancing the depth and breadth of their projects. We've ensured that the integration process is as intuitive as possible, allowing users to focus on what truly matters: crafting refined and effective pre-annotations.


### ChatGPT Prompt Definition and Testing
Users can generate LLM prompts on the dedicated Prompt page from the Hub of Resources. For ChatGPT Prompts, NLP Lab offers a dedicated definition interface. Here's what to expect when creating a new LLM prompt:

- **Name the Prompt**: Within this new tab, users will first be asked to provide a name for their prompt. This name will be used for pre-annotating identified entities. At this point, we recommend creating one prompt per target entity.

- **Select the Service Provider**: Next, users can choose the specific service provider they've previously set up via the Integrations Page.

- **Test in Real-time**: A standout feature is the ability to test ChatGPT prompts at creation time. As you craft your prompt, you can immediately see how it performs on some test data. This not only allows for immediate feedback but also ensures that the final prompt aligns perfectly with the user's objectives.

This streamlined approach ensures that integrating and testing external prompts is as intuitive and efficient as possible.


![TestingPrompt](https://github.com/JohnSnowLabs/annotationlab/assets/57619662/720eb4ac-0d73-4a06-8262-670abf01c94d)

### Consistent Workflow with LLM Prompts
Even with the introduction of new features in NLP Lab's 5.3.0 release, users can take comfort in the consistent experience offered when working with prompts. The addition of external service provider prompts brings a fresh layer to the annotation process, yet the core workflow you're familiar with stays the same.

- **Familiarity Amidst Innovation**: Despite the new integrations, the process of using available prompts remains as straightforward as ever. Whether you're working with traditional prompts or the newly introduced ones, the experience is smooth and consistent.

- **Seamless Transition**: Our commitment to user-centric design means that even as we innovate, we prioritize the ease of use you've come to expect. Transitioning to or incorporating external prompts is made effortless, with the interface and steps for prompt creation, selection, and integration remaining intuitive and unchanged.

With NLP Lab 5.3.0, you get the best of both worlds: exciting new features and the comfort of a familiar workflow.

![featureDis](https://github.com/JohnSnowLabs/annotationlab/assets/33893292/9cfdded6-abb5-4ef1-adea-7901c76877dc)

> **Note:** Pre-annotation of tasks using LLM Prompts does not require the deployment of the pre-annotation server. The pop-up to deploy the pre-annotation server is only shown if the project configuration consists of both LLM prompts and spark NLP models.