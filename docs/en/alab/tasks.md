---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Tasks
permalink: /docs/en/alab/tasks
key: docs-training
modify_date: "2023-06-09"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

The **Tasks** screen shows a list of all documents that have been imported into the current project.

Under each task you can see meta data about the task: the time of import, the user who imported the task and the annotators and reviewers assigned to the task.

![Task Assignment](/assets/images/annotation_lab/4.2.0/tasks.png "lit_shadow")

</div><div class="h3-box" markdown="1">

## Task Assignment

Project Owners/Managers can assign tasks to annotator(s) and reviewer(s) in order to better plan/distribute project work. Annotators and Reviewers can only view tasks that are assigned to them which means there is no chance of accidental work overlap.

For assigning a task to an annotator, from the task page select one or more tasks and from the `Assign` dropdown choose an annotator.

![Task Assignment](/assets/images/annotation_lab/4.1.0/task_assignment.gif "lit_shadow")

You can only assign a task to annotators that have already been added to the project team. For adding an annotator to the project team, select your project and navigate to the `Setup > Team` menu item. On the `Add Team Member` page, search for the user you want to add, select the role you want to assign to him/her and click on `Add To Team` button.

Project Owners can also be explicitly assigned as annotators and/or reviewers for tasks. It is useful when working in a small team and when the Project Owners are also involved in the annotation process. A new option `Only Assigned` checkbox is now available on the labeling page that allows Project Owners to filter the tasks explicitly assigned to them when clicking the `Next` button.

![Task Assignment](https://user-images.githubusercontent.com/17021686/204805373-4e5a5a7b-a520-4e9f-ad08-452bec165ef8.gif "lit_shadow")

> **NOTE:** When upgrading from an older version of the Generative AI Lab, the annotators will no longer have access to the tasks they worked on unless they are assigned to those explicitely by the admin user who created the project. Once they are assigned, they can resume work and no information is lost.

</div><div class="h3-box" markdown="1">

## Task Status

At high level, each task can have one of the following statuses:

- **Incomplete**, when none of the assigned annotators has started working on the task.
- **In Progress**, when at least one of the assigned annotators has submitted at least one completion for this task.
- **Submitted**, when all annotators which were assigned to the task have submitted a completion which is set as ground truth (starred).
- **Reviewed**, in the case there is a reviewer assigned to the task, and the reviewer has reviewed and accepted the submited completion.
- **To Correct**, in the case the assigned reviewer has rejected the completion created by the Annotator.

The status of a task varies according to the type of account the logged in user has (his/her visibility over the project) and according to the tasks that have been assigned to him/her.

</div><div class="h3-box" markdown="1">

### For Project Owner, Manager and Reviewer

On the Analytics page and Tasks page, the Project Owner/Manager/Reviewer will see the general overview of the projects which will take into consideration the task level statuses as follows:

- **Incomplete** - Assigned annotators have not started working on this task
- **In Progress** - At least one annotator still has not starred (marked as ground truth) one submitted completion
- **Submitted** - All annotators that are assigned to the task have starred (marked as ground truth) one submitted completion
- **Reviewed** - Reviewer has approved all starred submitted completions for the task

</div><div class="h3-box" markdown="1">

### For Annotators

On the Annotator's Task page, the task status will be shown with regards to the context of the logged-in Annotator's work. As such, if the same task is assigned to two annotators then:

- if annotator1 is still working and not submitted the task, then he/she will see task status as _In-progress_

![Task Assignment](/assets/images/annotation_lab/4.1.0/task_in_progress.png "lit_shadow")

- if annotator2 submits the task from his/her side then he/she will see task status as _Submitted_

![Task Assignment](/assets/images/annotation_lab/4.1.0/task_submitted.png "lit_shadow")

The following statuses are available on the Annotator's view.

- **Incomplete** – Current logged-in annotator has not started working on this task.
- **In Progress** - At least one saved/submitted completions exist, but there is no starred submitted completion.
- **Submitted** - Annotator has at least one starred submitted completion.
- **Reviewed** - Reviewer has approved the starred submitted completion for the task.
- **To Correct** - Reviewer has rejected the submitted work. In this case, the star is removed from the reviewed completion. The annotator should start working on the task and resubmit.

![Task Assignment](/assets/images/annotation_lab/4.1.0/task_reject_completion.gif "lit_shadow")

> **Note:** The status of a task is maintained/available only for the annotators assigned to the task.

When multiple Annotators are assigned to a task, the reviewer will see the task as submitted when all annotators submit and star their completions. Otherwise, if one of the assigned Annotators has not submitted or has not starred one completion, then the Reviewer will see the task as _In Progress_.

</div><div class="h3-box" markdown="1">

### Annotators Can View Completions Submitted by Reviewers
In version 6.4, of the Generative AI Lab, a new feature has been added that allows annotators to view the completion submitted by the reviewer. This enhancement fosters better collaboration and quality control in the annotation process. Previously, reviewers could only provide feedback on annotations, but now they can clone annotator submissions, make corrections, and add comments directly within the text using meta information. The updated submissions are then visible to the original annotator, providing clear insights into the reviewer's expectations and suggestions.

**How to Enable**:
- The project manager must enable the option **“Allow annotators to view completions from reviewers”** in the project settings.

![GenaiImage](/assets/images/annotation_lab/6.4.0/6.png)>

#### Workflow:
1.	**Reviewer Clones Submission:** Reviewers can clone the annotator's submission and make necessary corrections or add comments directly in the text using the meta option for the annotated chunks.
2.	**Submit Reviewed Completion:** The reviewer submits the cloned completion with corrections and comments.
3.	**Annotator Reviews Feedback:** The annotator whose submission was reviewed can view the reviewer's cloned completion and see the comments and corrections made.
4.	**Implement Changes:** The annotator can then make the required changes based on the detailed feedback provided by the reviewer.
   
![GenaiImage](/assets/images/annotation_lab/6.4.0/7.gif)

**Benefits**:
- **Enhanced Feedback**: Reviewers can now make precise corrections and add detailed comments on individual labels, helping annotators understand exactly what changes are needed.
- **Improved Collaboration**: Annotators can better align their work with the reviewer’s expectations by viewing the reviewer's cloned submission.
- **Quality Control**: This feature helps in maintaining a higher standard of annotations by ensuring that feedback is clear and actionable.

This feature significantly enhances the annotation process, making it more transparent and collaborative, and ensuring that annotators have a clear understanding of the reviewer's feedback.

## Task Filters

As normally annotation projects involve a large number of tasks, the Task page includes filtering and sorting options which will help the user identify the tasks he/she needs faster.
Tasks can be sorted by time of import ascending or descending.

![Task Assignment](/assets/images/annotation_lab/4.1.0/task_sort.png "lit_shadow")

Tasks can be filtered by the assigned tags, by the user who imported the task and by the status.

![Task Assignment](/assets/images/annotation_lab/4.1.0/task_tag.png "lit_shadow")

There is also a search functionality which will identify the tasks having a given string on their name.

![Task Assignment](/assets/images/annotation_lab/4.1.0/task_search.png "lit_shadow")

The number of tasks visible on the screeen is customizable by selecting the predefined values from the Tasks per page drop-down.

![Task Assignment](/assets/images/annotation_lab/4.1.0/task_filters.gif "lit_shadow")

From version 4.10 onwards, filtering tasks has been updated to allow users to select multiple tags from the Tags dropdown. This allows users to filter tasks based on multiple tags. Additionally, the same improved filter behaviour can be found in project page too. This provides users with increased flexibility and efficiency in filtering tasks based on multiple tags, thereby improving task and project management and facilitating a more streamlined workflow.

![filter](/assets/images/annotation_lab/4.10.0/7.gif)

</div><div class="h3-box" markdown="1">

## Task Search by Text, Label and Choice

Generative AI Lab offers advanced search features that help users identify the tasks they need based on the text or based on the annotations defined so far. Currently supported search queries are:

- text: patient -> returns all tasks which contain the string "patient";
- label: ABC -> returns all tasks that have at least one completion containing a chunk with label ABC;
- label: ABC=DEF -> returns all tasks that have at least one completion containing the text DEF labeled as ABC;
- choice: Sport -> returns all tasks that have at least one completion which classified the task as Sport;
- choice: Sport,Politics -> returns all tasks that have at least one completion containing multiple choices Sport and Politics.

Search functionality is case insensitive, thus the following queries `label: ABC=DEF` , `label: Abc=Def` or `label: abc=def` are considered equivalent.

**Example:**

Consider a project with 3 tasks which are annotated as below:

![Task Assignment](/assets/images/annotation_lab/4.1.0/task_search_task1.png "lit_shadow")

![Task Assignment](/assets/images/annotation_lab/4.1.0/task_search_task2.png "lit_shadow")

![Task Assignment](/assets/images/annotation_lab/4.1.0/task_search_task3.png "lit_shadow")

Search-query "label:LOC" will list as results Task 1 and Task 3.

![Task Assignment](/assets/images/annotation_lab/4.1.0/task_search_loc.png "lit_shadow")

Search-query "label:WORK_OF_ART" will list as result Task 1 and Task 2.

![Task Assignment](/assets/images/annotation_lab/4.1.0/task_search_work_of_art.png "lit_shadow")

Search-query "label:PERSON=Leonardo" will list as result Task 1.

![Task Assignment](/assets/images/annotation_lab/4.1.0/task_search_person_leonardo.png "lit_shadow")

</div><div class="h3-box" markdown="1">

## Comments

Comments can be added to each task by any team member. This is done by clicking the `View comments` link present on the rightmost side of each Task in the Tasks List page. It is important to notice that these comments are visible to everyone who can view the particular task.

![Task Assignment](/assets/images/annotation_lab/4.1.0/task_comment.png "lit_shadow")

</div>