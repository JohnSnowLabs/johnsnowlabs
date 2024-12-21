---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Benchmarks LLM
permalink: /docs/en/benchmark-llm
key: docs-benchmark-llm
modify_date: "2024-11-27"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---
<div class="h3-box" markdown="1">

##  Medical Benchmarks

### Benchmarking

{:.table-model-big}
| Model           | Avarega | MedMCQA | MedQA  | MMLU <br>anotomy | MMLU<br>clinical<br>knowledge | MMLU<br>college<br>biology | MMLU<br>college<br>medicine  | MMLU<br>medical<br>genetics  | MMLU<br>professional<br>medicine  | PubMedQA |
|-----------------|---------|---------|--------|------------------|-------------------------------|----------------------------|------------------------------|------------------------------|-----------------------------------|----------|
| jsl_medm_q4_v3  | 0.6884  | 0.6421  | 0.6889 | 0.7333           | 0.834                         | 0.8681                     | 0.7514                       | 0.9                          | 0.8493                            | 0.782    |
| jsl_medm_q8_v3  | 0.6947  | 0.6416  | 0.707  | 0.7556           | 0.8377                        | 0.9097                     | 0.7688                       | 0.9                          | 0.8713                            | 0.79     |
| jsl_medm_q16_v3 | 0.6964  | 0.6436  | 0.7117 | 0.7481           | 0.8453                        | 0.9028                     | 0.7688                       | 0.87                         | 0.8676                            | 0.794    |
| jsl_meds_q4_v3  | 0.5522  | 0.5104  | 0.48   | 0.6444           | 0.7472                        | 0.8333                     | 0.6532                       | 0.68                         | 0.6691                            | 0.752    |
| jsl_meds_q8_v3  | 0.5727  | 0.53    | 0.4933 | 0.6593           | 0.7623                        | 0.8681                     | 0.6301                       | 0.76                         | 0.7647                            | 0.762    |
| jsl_meds_q16_v3 | 0.5793  | 0.5482  | 0.4839 | 0.637            | 0.7585                        | 0.8403                     | 0.6532                       | 0.77                         | 0.7022                            | 0.766    |

</div><div class="h3-box" markdown="1">

### Benchmark Summary

We evaluated six Johnsnow Lab LLM models across ten task categories: MedMCQA, MedQA, MMLU Anatomy, MMLU Clinical Knowledge, MMLU College Biology, MMLU College Medicine, MMLU Medical Genetics, MMLU Professional Medicine, and PubMedQA.

Each model's performance was measured based on accuracy, reflecting how well it handled medical reasoning, clinical knowledge, and biomedical question answering. 

</div><div class="h3-box" markdown="1">

<div class="h3-box" markdown="1">

##  JSL-MedS

### Benchmarking

We have generated a total of 400 questions, 100 from each category. These questions were labeled and reviewed by 3 physician annotators. `%` indicates the preference rate

```bash
## Overall
| Model      | Factuality % | Clinical Relevancy % | Conciseness % |
|------------|--------------|----------------------|---------------|
| JSL-MedS   | 0.24         | 0.25                 | 0.38          |
| GPT4o      | 0.19         | 0.26                 | 0.27          |
| Neutral    | 0.43         | 0.36                 | 0.18          |
| None       | 0.14         | 0.13                 | 0.17          |
| Total      | 1.00         | 1.00                 | 1.00          |

## Summary 
| Model      | Factuality % | Clinical Relevancy % | Conciseness % |
|------------|--------------|----------------------|---------------|
| JSL-MedS   | 0.47         | 0.48                 | 0.42          |
| GPT4o      | 0.25         | 0.25                 | 0.25          |
| Neutral    | 0.22         | 0.22                 | 0.25          |
| None       | 0.07         | 0.05                 | 0.08          |
| Total      | 1.00         | 1.00                 | 1.00          |

## QA
| Model      | Factuality % | Clinical Relevancy % | Conciseness % |
|------------|--------------|----------------------|---------------|
| JSL-MedS   | 0.35         | 0.36                 | 0.42          |
| GPT4o      | 0.24         | 0.24                 | 0.29          |
| Neutral    | 0.33         | 0.33                 | 0.18          |
| None       | 0.09         | 0.07                 | 0.11          |
| Total      | 1.00         | 1.00                 | 1.00          |

## BioMedical
| Model      | Factuality % | Clinical Relevancy % | Conciseness % |
|------------|--------------|----------------------|---------------|
| JSL-MedS   | 0.33         | 0.24                 | 0.57          |
| GPT4o      | 0.12         | 0.08                 | 0.16          |
| Neutral    | 0.45         | 0.57                 | 0.16          |
| None       | 0.10         | 0.10                 | 0.10          |
| Total      | 1.00         | 1.00                 | 1.00          |

## OpenEnded
| Model      | Factuality % | Clinical Relevancy % | Conciseness % |
|------------|--------------|----------------------|---------------|
| JSL-MedS   | 0.35         | 0.30                 | 0.39          |
| GPT4o      | 0.30         | 0.33                 | 0.41          |
| Neutral    | 0.19         | 0.20                 | 0.02          |
| None       | 0.17         | 0.17                 | 0.19          |
| Total      | 1.00         | 1.00                 | 1.00          |
```

</div><div class="h3-box" markdown="1">

### Benchmark Summary

We evaluated two models, JSL-MedS and GPT4o, across four task categories: Summary, QA, Biomedical, and Open-Ended. Each model's preference rate represents the percentage of cases where it was preferred over the other or over a neutral/no-preference choice. These metrics reflect how often each model was favored based on Factuality, Clinical Relevance, and Conciseness.

</div><div class="h3-box" markdown="1">

#### Overall Performance Analysis:
Across all the categories, JSL-MedS overall outperforms the GPT4o in two out of three metrics: factuality by 26% (0.24 vs 0.19) and conciseness by 41% (0.38 vs 0.27). However, GPT4o edges out JSL-MedS in clinical relevance by a slight 4% (0.26 vs 0.25). The "neutral" and "none" responses are quite high for these models, indicating that the participants often found no clear preference between the two models.

</div><div class="h3-box" markdown="1">

#### Category-Wise Insights

1. Summary Tasks:
JSL-MedS has a clear advantage over GPT4o in all three metrics of summary tasks. It is preferred about 88% more for Factuality and Clinical Relevance, with scores of 0.47 and 0.48 respectively compared to GPT4o with scores of 0.25 for both. For the metric of Conciseness, JSL-MedS still is ahead of GPT4o by 68%. The Neutral responses are about 22-25% and "None" responses are lower, which proves unanimously that JSL-MedS is superior for summarizing tasks.

2. QA Tasks:
In QA task, the lead of JSL-MedS is less severe compared to summary tasks but still clear. It outperforms GPT4o in Factuality by 46% (0.35 vs 0.24), Clinical Relevance by 50% (0.36 vs 0.24), and in Conciseness by 45% (0.42 vs 0.29). Similar to the summary tasks, high neutral and lower "None" responses indicate JSL-MedS is more preferred for QA tasks.

3. Biomedical Tasks:
JSL-MedS outperforms GPT4o significantly in Biomedical tasks. It leads in Factuality by 175% (0.33 vs 0.12). The same is true for Clinical Relevance where it surpasses GPT4o by 200% (0.24 vs 0.08). In terms of Conciseness, JSL-MedS is preferred 3.56 times (or 256%) more than GPT4o (0.57 vs 0.16). The high "Neutral" responses indicate room for improvement for both models in biomedical tasks.

4. Open-Ended Tasks:
For open-ended tasks, the two models are more evenly matched. JSL-MedS barely exceeds GPT4o in Factuality by 17% (0.35 vs 0.30), and is less preferred than GPT4o in Clinical Relevance by 10% (0.33 vs 0.30). On the other hand, GPT4o is marginally more preferred in Conciseness, leading JSL-MedS by 5% (0.41 vs 0.39).

#### Conclusion:
JSL-MedS shows superior performance in the categories of summary, QA, and Biomedical tasks for all three metrics: Factuality, Clinical Relevance, and Conciseness. Only in the open-ended tasks category does GPT4o show a slightly better result than JSL-MedS in Clinical Relevance and Conciseness. This indicates JSL-MedS to be an overall more robust model, especially in tasks needing precise and concise responses. GPT4o, while falling behind in most areas, exhibits stronger performance in open-ended tasks, which may indicate a better ability to tackle more abstract or diverse problems. High neutral responses across all tasks and categories suggest that there are significant opportunities for either model to improve.

</div><div class="h3-box" markdown="1">

## JSL-MedM

### Benchmarking

We have generated a total of 400 questions, 100 from each category. These questions were labeled and reviewed by 3 physician annotators. `%` indicates the preference rate

```bash
## Overall
| Model    | Factuality % | Clinical Relevancy % | Conciseness % |
|----------|--------------|----------------------|---------------|
| JSL-MedM | 0.29         | 0.25                 | 0.50          |
| ChatGPT  | 0.21         | 0.30                 | 0.26          |
| Neutral  | 0.43         | 0.38                 | 0.17          |
| None     | 0.07         | 0.07                 | 0.08          |
| total    | 1.00         | 1.00                 | 1.00          |

## Summary 
| Model    | Factuality % | Clinical Relevancy % | Conciseness % |
|----------|--------------|----------------------|---------------|
| JSL-MedM | 0.42         | 0.42                 | 0.50          |
| GPT4o    | 0.33         | 0.33                 | 0.28          |
| Neutral  | 0.17         | 0.17                 | 0.12          |
| None     | 0.08         | 0.08                 | 0.10          |
| Total    | 1.00         | 1.00                 | 1.00          |

## QA
| Model    | Factuality % | Clinical Relevancy % | Conciseness % |
|----------|--------------|----------------------|---------------|
| JSL-MedM | 0.40         | 0.36                 | 0.60          |
| GPT4o    | 0.15         | 0.19                 | 0.19          |
| Neutral  | 0.38         | 0.38                 | 0.11          |
| None     | 0.08         | 0.08                 | 0.09          |
| Total    | 1.00         | 1.00                 | 1.00          |

## BioMedical
| Model    | Factuality % | Clinical Relevancy % | Conciseness % |
|----------|--------------|----------------------|---------------|
| JSL-MedM | 0.22         | 0.14                 | 0.55          |
| GPT4o    | 0.21         | 0.36                 | 0.23          |
| Neutral  | 0.49         | 0.44                 | 0.14          |
| None     | 0.07         | 0.06                 | 0.07          |
| Total    | 1.00         | 1.00                 | 1.00          |

## OpenEnded
| Model    | Factuality % | Clinical Relevancy % | Conciseness % |
|----------|--------------|----------------------|---------------|
| JSL-MedM | 0.21         | 0.19                 | 0.38          |
| GPT4o    | 0.18         | 0.30                 | 0.31          |
| Neutral  | 0.55         | 0.46                 | 0.26          |
| None     | 0.05         | 0.05                 | 0.06          |
| Total    | 1.00         | 1.00                 | 1.00          |

```

</div><div class="h3-box" markdown="1">

### Benchmark Summary
We evaluated two models, JSL-MedM and GPT4o, across four task categories: Summary, QA, Biomedical, and Open-Ended. Each model's preference rate represents the percentage of cases where it was preferred over the other or over a neutral/no-preference choice. These metrics reflect how often each model was favored based on Factuality, Clinical Relevance, and Conciseness.

</div><div class="h3-box" markdown="1">

#### Overall Performance

JSL-MedM leads in Conciseness (50%), being nearly twice as preferred as ChatGPT (26%).
In Factuality, JSL-MedM (29%) is 38% more preferred than ChatGPT (21%).
For Clinical Relevance, ChatGPT (30%) slightly outperforms JSL-MedM (25%), showing a modest edge in generating contextually relevant clinical content.
A significant share of responses was Neutral (43% factuality, 38% clinical relevance), suggesting areas where neither model had a clear advantage.

</div><div class="h3-box" markdown="1">

#### Category-Wise Insights

1. Summary Tasks
JSL-MedM leads in Factuality and Clinical Relevance, with 42% preference for each, while GPT4o scores 33% in both.
JSL-MedM is 27% more preferred in these categories.
In Conciseness, JSL-MedM (50%) is nearly twice as preferred as GPT4o (28%), highlighting its ability to produce succinct summaries.
Neutral ratings (17%) indicate relatively few cases where the models were evenly matched.

2. QA Tasks
JSL-MedM has a commanding lead in all attributes:
Factuality (40%): Over 2.5 times more preferred than GPT4o (15%).
Clinical Relevance (36%): Nearly 2 times more preferred than GPT4o (19%).
Conciseness (60%): Over 3 times more preferred than GPT4o (19%).
These results underscore JSL-MedM's superiority in question-answering tasks across all benchmarks.

3. Biomedical Tasks
In Conciseness, JSL-MedM (55%) is 2.4 times more preferred than GPT4o (23%).
In Factuality, JSL-MedM (22%) narrowly leads GPT4o (21%), showing parity in factual content.
GPT4o (36%) is 2.6 times more preferred in Clinical Relevance than JSL-MedM (14%), suggesting its strength in contextual alignment within biomedical discussions.
Neutral ratings (49% factuality, 44% clinical relevance) highlight room for improvement for both models.

4. Open-Ended Tasks
JSL-MedM performs better in Conciseness (38%), with a 22% higher preference rate than GPT4o (31%).
For Factuality, JSL-MedM (21%) narrowly edges out GPT4o (18%), being 16% more preferred.
GPT4o leads in Clinical Relevance (30%), being 58% more preferred than JSL-MedM (19%).
High neutral responses (55% factuality, 46% clinical relevance) indicate that open-ended tasks often lack a clear preference.

</div><div class="h3-box" markdown="1">

#### Conclusion
JSL-MedM consistently outperforms GPT4o in Conciseness, often being 2-3 times more preferred.
It maintains a strong edge in Factuality, particularly in QA and Summary tasks.
GPT4o demonstrates strength in Clinical Relevance, especially in Biomedical and Open-Ended tasks.
Neutral and "None" ratings across categories highlight areas for further optimization for both models.
This analysis underscores the strengths of JSL-MedM in producing concise and factual outputs, while GPT4o shows a stronger contextual understanding in certain specialized tasks.

</div>
