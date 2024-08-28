---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Overview
permalink: /docs/en/alab/tags_overview
key: docs-training
modify_date: "2023-06-20"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

<div class="h3-box" markdown="1">

Generative AI Lab enables the utilization of XML-like tags to configure the labeling interface. Generative AI Lab contains three distinct tag types for labeling management:

- `Object tags` serve for data types, presenting labeled elements within a task, which can be labeled as video, audio, HTML, images, PDF, and text.
- `Control tags` facilitate the annotation of objects. For instance, labels are employed in semantic and named entity tasks, and choices for classification tasks inside Generative AI Lab.
- `Visual tags` allow for changes to the visual elements of the labelling interface, giving control over the presentation of particular labeling choices or the presence of a header.

</div><div class="h3-box" markdown="1">

## Custom Labeling Configuration

A name parameter is required for each `Control` and `Object tag`. Every `Control tag` also needs a toName parameter that matches the name parameter of the object tag in the configuration. Suppose you wish to assign labels to text for a Named Entity Recognition task. In that case, you could use the following labeling configuration:

![NER-xml-tag](/assets/images/annotation_lab/xml-tags/NER_labels.png)

In this case, text is annotated using the `Label tags` in combination with the `Text tag`. Multiple control and `Object tags` may be used in the same configuration by creating linkages between them using names.

</div><div class="h3-box" markdown="1">

### Variables

All `Object tags`, as well as some `Control` and `Visual tags`, support variables within their arguments. Using variables enables for the creation of a labeling configuration, while also allowing for the control of given information on the labeling interface based on data in a given task.
To use a variable, define it with the value parameter of a tag and specify it using the $ sign and the name of the field that you want to reference. For example, if you have a sample task which contains some partial JSON, then the configuration should look something like this:

![Headers-tag](/assets/images/annotation_lab/xml-tags/header_variables.png)

When you look on the preview window, you can see the header set on top of the labels/choices. 

</div><div class="h3-box" markdown="1">

## Configure project using Visual Menu Builder

This version of Generative AI Lab introduces a new way for configuring your projects, removing the need for manual XML configuration. With the Visual Menu Builder, users can easily create, edit, and manage project configurations through a user-friendly interface. This makes the configuration process much more straightforward, especially for those unfamiliar with XML syntax, while also reducing the risk of errors associated with manual coding.

To see the structure of a project configuration XML file and the definitions of the supported tag types and various parameters and variables, and to better understand how Visual Menu Builder maps and creates these elements when configuring your project, see [Project Configuration Overview](https://nlp.johnsnowlabs.com/docs/en/alab/tags_overview).

**Key Features:**

**Add New Element**

The new menu user interface allows users to easily add new elements to their project configurations. Users can click on the plus icon ("+") within the Visual Menu Builder interface to add a new element. Once the element is added, users can further customize it by configuring additional parameters directly in the interface. This might include setting attributes, defining properties, or linking to other project components.

![genAI650](/assets/images/annotation_lab/6.5.0/6.gif)

**Edit an Element**

Users can modify the properties and configurations of existing elements within the project. By clicking on the edit icon (a pencil icon), users can access the settings for an existing element. This opens an editable interface where users can adjust the element's parameters to suit the evolving needs of the project.

![genAI650](/assets/images/annotation_lab/6.5.0/7.gif)

**Delete an Element**

Users can remove unwanted elements from the project configuration. Users can click on the cross button ("x") associated with a specific element to remove it from the project. This feature helps in keeping the project configuration clean and relevant by allowing users to easily remove elements that are no longer needed.

![genAI650](/assets/images/annotation_lab/6.5.0/8.gif)

**Drag and Move Element**

The new visual menu builder allows users to easily rearrange elements within the project configuration using a drag-and-drop interface. To move an element, users can click and hold on the "Handle" icon, which is represented by a set of six dots (three parallel dots in two vertical rows) next to the element. After clicking on the Handle, users can drag the element to the desired position within the project configuration. Release the mouse button to drop the element in its new location. This feature provides flexibility in organizing the project structure, allowing users to quickly and intuitively reorder elements.

![genAI650](/assets/images/annotation_lab/6.5.0/9.gif)

**Show Element Boundaries**

The **Show element Boundaries** button in the visual menu builder highlights the borders of each element within the project configuration, making it easier to visualize and distinguish the different components. By clicking on the "**Show element Boundaries**" button, users can toggle the visibility of the boundaries for all elements in the configuration. When enabled, a visible border will appear around each element, clearly outlining its scope and separation from other elements. This feature is particularly helpful when working with complex configurations where multiple elements are closely positioned. By showing the boundaries, users can easily identify and select the correct element they want to edit, move, or delete.

![genAI650](/assets/images/annotation_lab/6.5.0/10.gif)

**Show Parent Action Buttons on Hover**

The **Show parent action buttons on hover** button in the Visual Menu Builder allows users to quickly access action buttons (such as edit, delete, or add) for parent elements by hovering over them. By hiding the action buttons until needed, it reduces visual clutter and allows users to concentrate on their current tasks. The ability to quickly access these buttons by hovering ensures that they remain easily accessible without overwhelming the interface.

![genAI650](/assets/images/annotation_lab/6.5.0/11.gif)

**Fullscreen Mode**

The "**Fullscreen**" button in the visual menu builder allows users to expand the workspace to occupy the entire screen, providing a larger and more focused view of the project configuration. Clicking on the "**Fullscreen**" button maximizes the Visual Menu Builder, hiding other UI elements so the entire screen is dedicated to the project configuration. To exit fullscreen mode, users can click the "**Fullscreen**" button again or use the Esc key to return to the normal view with all standard UI elements visible.

![genAI650](/assets/images/annotation_lab/6.5.0/12.gif)

</div>