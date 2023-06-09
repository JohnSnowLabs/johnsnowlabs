---
layout: model
title: Financial Finetuned FLAN-T5 Summarization  ( SEC 10k Filings )
author: John Snow Labs
name: finsum_flant5_finetuned_sec10k
date: 2023-04-13
tags: [en, summarization, flant5, t5, finance, licensed, tensorflow]
task: Summarization
language: en
edition: Finance NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: FinanceSummarizer
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This language model has been fine-tuned on the FLANT5 using the SEC 10K Filings data. FLAN-T5 is a state-of-the-art language model developed by Facebook AI that utilizes the T5 architecture for text summarization tasks.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finsum_flant5_finetuned_sec10k_en_1.0.0_3.0_1681385689906.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finsum_flant5_finetuned_sec10k_en_1.0.0_3.0_1681385689906.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("documents")

flant5 = finance.Summarizer().pretrained('finsum_flant5_finetuned_sec10k','en','finance/models')\
    .setInputCols(["documents"])\
    .setOutputCol("summary")\
    .setMaxNewTokens(1000)

pipeline = nlp.Pipeline(stages=[document_assembler, flant5])

data = spark.createDataFrame([
  [1, """Intelligent process automation, or IPA, combines task automation with process automation to orchestrate coordination across systems, humans, and digital workforce in a unified workflow. According to IDC, the market for worldwide IPA software totaled $16.3 billion in 2019 and is expected to grow at a compound annual growth rate of 13% to $30.5 billion by 2024. We were included as a "Leader" based on the strength of our current offering, our strategy, and our market presence in The Forrester Wave Gartner Magic Quadrant for Enterprise Low-Code Application Platforms , Published 30 September 2020; Authored by: Paul Vincent, Yefim Natis, Jason Wong, Saikat Ray, et al. Gartner, Forecast: Public Cloud Services, Worldwide, 2018-2024, 4Q20 Update, Colleen Graham, Neha Gupta, et al., 21 December 2020. Gartner Forecast Analysis: Robotic Process Automation, Worldwide; Published 2 September 2020; Authored by: Fabrizio Biscotti, Cathy Tornbohm, Arthur Villa, et. al). IDC: Worldwide Intelligent Process Automation Software Forecast, 2020-2024; Published 15 July 2020; Authored by Maureen Fleming. Taken together, these current core software markets are expected to represent a combined $70.1 billion market opportunity currently and a combined $209.5 billion market opportunity in the near term. In addition to our current core software markets, we believe our platform better addresses certain needs of enterprise companies that have historically used manually-developed custom software. The global enterprise application software market is expected to reach $231 billion in 2021, according to Gartner. Based on approximately 166,000 global companies and government institutions in relevant industries and revenue-based size segments as well as our industry- and size-specific average annual recurring revenue for customers as of December 31, 2020, we internally estimate our market opportunity to have been approximately $37 billion in 2020. We determined relevant global companies and government institutions by industry and size by referencing certain independent industry data from S&P Global Market Intelligence. We calculated industry-and size-specific average annual recurring revenue as of December 31, 2020 by adding the aggregate annual recurring revenue from all existing customers within each industry and size segment and dividing the total by the number of our existing customers in each industry and size segment. Gartner, Forecast: Enterprise Application Software, Worldwide, 2018-2024, 4Q20 Update, Neha Gupta, Chris Pang, et al., 18 December 2020. With our platform, organizations can rapidly and easily design, build, and implement powerful, enterprise-grade custom applications through our intuitive, visual interface, with little or no coding required. We also enable organizations to easily modify and enhance applications and automatically disseminate these updates across device types to ensure all users benefit from the most up-to-date functionality. Through the speed and power of our platform, organizations can make their digital transformations happen more effectively and efficiently than could be achieved through building an application with standard programming languages. Our heritage as a BPM company provides us with a differentiated understanding and ability to automate complex processes, and we have incorporated that expertise into our platform to enable the development of powerful business software. Appian applications can leverage our complete automation capabilities, applying the right automation approach for each specific use case: At the core of our platform is an advanced engine that enables the modeling, modification, and management of complex processes. Appian combines people, technologies, and data into a single workflow to maximize resources and improve business results. Workflow can include any worker (people, RPA, AI) or any resource (data and system). Appian includes a declarative environment for defining and executing business logic or rules. These rules can be highly complex and applied within the Appian platform to many use cases, ranging from automated decision making to user experience personalization."""]
]).toDF('id', 'text')

results = pipeline.fit(data).transform(data)

results.select("summary.result").show(truncate=False)
```

</div>

## Results

```bash
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[Appian is a BPM company that provides intelligent process automation (IPA) software to organizations to orchestrate coordination across systems, humans, and digital workforce in a unified workflow. The market for worldwide IPA software totaled $16.3 billion in 2019 and is expected to grow at a compound annual growth rate of 13% to $30.5 billion by 2024. Appian was included as a "Leader" based on the strength of its current offering, strategy, and market presence in The Forrester Wave Gartner Magic Quadrant for Enterprise Low-Code Application Platforms, Gartner Magic Quadrant for Public Cloud Services, Worldwide, 2018-2024, 4Q20 Update, Colleen Graham, Neha Gupta, et al., Gartner Forecast Analysis: Robotic Process Automation, Worldwide, Published 2 September 2020; Fabrizio Biscotti, Cathy Tornbohm, Arthur Villa, et. al., IDC: Worldwide Intelligent Process Automation Software Forecast, 2020-2024; Published 15 July 2020; Maureen Fleming. The global enterprise application software market is expected to reach $231 billion in 2021, and Appian internally estimates its market opportunity to have been approximately $37 billion in 2020. Appian's platform combines people, technologies, and data into a single workflow to maximize resources and improve business results. Appian includes a declarative environment for defining and executing business logic or rules.]|
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finsum_flant5_finetuned_sec10k|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.6 GB|

## References

In house annotated dataset
