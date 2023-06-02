---
layout: docs
comment: no
header: true
seotitle: Annotation Lab | John Snow Labs
title: Productivity
permalink: /docs/en/alab/productivity
key: docs-training
modify_date: "2022-12-11"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

<style>
bl {
  font-weight: 400;
}

es {
  font-weight: 400;
  font-style: italic;
}
</style>

## Analytics Charts

By default, the Analytics page is disabled for every project because computing the analytical charts is a resource-intensive task and might temporarily influence the responsiveness of the application, especially when triggered in parallel with other training/preannotation jobs. However, users can file a request to enable the Analytics page which can be approved by any [admin user](/docs/en/alab/user_management#user-groups). The request is published on the [Analytics Requests](/docs/en/alab/analytics_permission) page, visible to any <es>admin</es> user. Once the <es>admin</es> user approves the request, any team member can access the Analytics page.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/analytics/enable_analytics.gif" style="width:100%;"/>

A refresh button is present on the top-right corner of the Analytics page. The Analytics charts doesn't automatically reflect the changes made by the annotators (like creating tasks, adding new completion, etc.). Updating the analytics to reflect the latest changes can be done using the refresh button.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/analytics/refresh.png" style="width:100%;"/>

### Task Analytics

To access Task Analytics, navigate on the first tab of the <es>Analytics</es> Dashboard, called <bl>Tasks</bl>. The following blog post explains how to [Improve Annotation Quality using Task Analytics in the Annotation Lab](https://www.johnsnowlabs.com/improving-annotation-quality-using-analytics-in-the-annotation-lab/).

Below are the charts included in the Tasks section.

**Total number of tasks in the Project**

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/analytics/total_tasks.png" style="width:100%;"/>

**Total number of task in a Project in last 30 days**

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/analytics/total_tasks_last_30_days.png" style="width:100%;"/>

**Breakdown of task in the Project by Status**

This chart visually represents the number of tasks that are submitted, in progress, reviewed, and incomplete.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/analytics/tasks_by_status.png" style="width:100%;"/>

**Breakdown of task by author**

This chart represents the distribution of the tasks **created** by each author of the project.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/analytics/tasks_created_by.png" style="width:100%;"/>

**Summary of task status for each annotator**

This chart gives a detailed summary of the status of the tasks for each annotator. For example, in the image below, Eric has a few tasks in progress, but no incomplete tasks. Meanwhile, Jenny has no task in progress but has a few incomplete tasks.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/analytics/annotator_summary.png" style="width:100%;"/>

**Total number of label occurrences across all completions**

This bar chart represents the total number of labels across all the tasks in the project. There are markers on this chart signifying the labels with maximum and minimum occurrences.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/analytics/total_label_frequency_across_completions.png" style="width:100%;"/>

**Average number of label occurrences for each completion**

This bar chart represents the average number of labels for each task in the project. There are markers on this chart signifying the labels with maximum and minimum occurrences in a task.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/analytics/average_label_frequency_per_completion.png" style="width:100%;"/>

**Total number of label occurrences across all completions for each annotator**

This chart signifies the number of labelled entities by each annotator. For example, in the image below, Eric has labelled 99 entities, while Jenny has labelled 77 entities.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/analytics/label_frequency_by_annotator.png" style="width:100%;"/>

**Total vs distinct count of labels across all completions**

This chart shows the total number of occurrences of a particular label across all completions vs the sum of the number of distinct entities which are marked with that label across all completions. 

<img class="image image__shadow" src="/assets/images/annotation_lab/4.9.0/total_vs_distinct_values.png" style="width:100%;"/>

**Average number of tokens by label**

This chart represents the average number of chunks covered under one label. For example, in each of the tasks, the label "MONEY" was assigned to an entity with two tokens, such as, 250 euros, etc. Hence the average number of tokens for "MONEY" is 2.0.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/analytics/average_number_of_tokens_by_label.png" style="width:100%;"/>

**Total number of label occurrences that include numeric values**

This bar chart shows the total occurrences of a label across all completions vs the total occurrences which contain numeric values within that particular label.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.9.0/numeric_values_across_labels.png" style="width:100%;"/>

**Average length of tasks completed by each Annotator**

<img class="image image__shadow" src="/assets/images/annotation_lab/4.9.0/average_task_length.png" style="width:100%;"/>

<br />

### Team Productivity

To access Team Productivity charts, navigate on the second tab of the <es>Analytics</es> Dashboard, called <bl>Team Productivity</bl>. The following blog post explains how to [Keep Track of Your Team Productivity in the Annotation Lab](https://www.johnsnowlabs.com/keep-track-of-your-team-productivity-in-the-annotation-lab/).

Below are the charts included in the Team Productivity section.

<!-- **Total number of completions in the Project**

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/analytics/total_completions.png" style="width:100%;"/>

**Total number of completions in the Project in the last 30 days**

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/analytics/total_completions_in_last_30_days.png" style="width:100%;"/> -->

**Visual Representation of the completions**

The image below shows the status of completions, and the representation is divided into three three partitions. The left part shows the total number of completions in the project. The middle part shows a pie chart representing the status of the completions, i.e, whether the completion is starred or is in draft. The right part shows the time period over which you want the completion history to be displayed.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.9.0/team_productivity_analytics.png" style="width:100%;"/>

**Total completions vs Ground Truth completions per Annotator**

This bar graph shows the total number of completions by each annotator vs the number of completions which are marked as the ground truth. If an annotator manually labels all the tasks in the project, then the total number of completions and the ground truth completions will be the same. They would differ in the cases if the user uses pre-annotation and the tasks seem to have been labeled accurately based on pre-annotation.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.9.0/total_completions_vs_ground_truth.png" style="width:100%;"/>

**Total number of completions submitted over time for each Annotator**

The productivity of the team can be analysed by looking at the number of completions submitted by each annotator over time. 

<img class="image image__shadow" src="/assets/images/annotation_lab/4.9.0/total_submissions_each_annotator.png" style="width:100%;"/>

**Average time spent by the Annotator in each task**

This chart shows the average time spent on a task by each annotator. The time on the vertical axis is in minutes.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.9.0/average_time_per_task.png" style="width:100%;"/>

**Total number of completions submitted over time**

This chart shows the total number of completions submitted by the user over time. Note that this is different than the one we saw above, because this is does not contain the progress information of other annotators.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.9.0/total_submissions_over_time.png" style="width:100%;"/>

<br />

### Inter-Annotator Agreement (IAA)

Starting from version 2.8.0, Inter Annotator Agreement(IAA) charts allow the comparison between annotations produced by <es>Annotators</es>, <es>Reviewers</es>, or <es>Managers</es>.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.9.0/iaa_analytics.gif" style="width:100%;"/>

Inter Annotator Agreement charts can be used by <es>Annotators</es>, <es>Reviewers</es>, and <es>Managers</es> for identifying contradictions or disagreements within the starred completions (Ground Truth). When multiple annotators work on same tasks, IAA charts are handy to measure how well the annotations created by different annotators align. IAA chart can also be used to identify outliers in the labeled data, or to compare manual annotations with model predictions.

To access IAA charts, navigate on the third tab of the <es>Analytics</es> Dashboard of NER projects, called <bl>Inter-Annotator Agreement</bl>. Several charts should appear on the screen with a default selection of annotators to compare. The dropdown selections on top-left corner of each chart allow you to change annotators for comparison purposes. There is another dropdown to select the label type for filtering between NER labels and Assertion Status labels for projects containing both NER and Assertion Status entities. It is also possible to download the data generated for some chart in CSV format by clicking the download button just below the dropdown selectors.

> **Note:** Only the <es>Submitted</es> and <es>starred (Ground Truth)</es> completions are used to render these charts.

The following blog post explains how your team can [Reach Consensus Faster by Using IAA Charts in the Annotation Lab](https://www.johnsnowlabs.com/reach-consensus-faster-by-using-iaa-charts-in-the-annotation-lab/).

Below are the charts included in the Inter-Annotator Agreement section.

**High-level IAA between annotators on all common tasks**

The image below shows a pie chart for the disagreement between Eric and Jenny. This is crucial to analyse since ideally, all the annotators want to be on the same page regarding labeling entities.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/analytics/high_level_iaa_between_annotators_on_all_common_tasks.png" style="width:100%;"/>

**IAA between annotators for each label on all common tasks**

This chart gives an even more refined representation of the inter-annotator agreement between annotators, because it can be broken down to each label as shown below.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/analytics/iaa_between_annotators_on_all_common_tasks.png" style="width:100%;"/>

**Comparison of annotations by annotator on each chunk**

This table shows the comparison for each chunk between two annotators specified by the user. The table makes it convenient to pin-point the location of disagreement between annotators by looking at the 'Context' column.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.9.0/annotators_comparison_by_chunks.png" style="width:100%;"/>

**Comparison of annotations by model and annotator (Ground Truth) on each chunk**

This table shows the comparison for each chunk betweent the pre-annotation model and the annotator. 

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/analytics/prediction_vs_groundtruth.png" style="width:100%;"/>

**All chunks annotated by an annotator**

This table shows all the chunks extracted by an annotator which the user can choose from the dropdown. Additionally, the user can also see where the chunk occurred in the task by looking at the 'Context' column.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/analytics/all_chunks_extracted_by_annotator.png" style="width:100%;"/>

**Frequency of labels on chunks annotated by an annotator**

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/analytics/chunks_extracted_by_annotator.png" style="width:100%;"/>

**Frequency of a label on chunks annotated by each annotator**

This table shows the frequency of the chunks extracted by each annotator for a specific label. The user can choose the label from the dropdown.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/analytics/chunks_extracted_by_label.png" style="width:100%;"/>

## Download data used for charts

CSV file for specific charts can be downloaded using the new download button which will call specific API endpoints: /api/projects/{project_name}/charts/{chart_type}/download_csv

![Screen Recording 2022-03-08 at 3 47 49 PM](https://user-images.githubusercontent.com/17021686/158564836-691a2b79-f3ca-4317-ad31-51cfbc9d71df.gif)
