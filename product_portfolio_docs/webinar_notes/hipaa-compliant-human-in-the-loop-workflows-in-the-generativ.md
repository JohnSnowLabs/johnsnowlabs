# HIPAA-Compliant Human-in-the-Loop Workflows in the Generativ
HIPAA-Compliant Human-in-the-Loop Workflows in the Generative AI Lab

[<span class="mark">https://www.johnsnowlabs.com/hipaa-compliant-human-in-the-loop-workflows-in-the-generative-ai-lab/</span>](https://www.johnsnowlabs.com/hipaa-compliant-human-in-the-loop-workflows-in-the-generative-ai-lab/)

<span class="mark">https://youtu.be/5NttChUAXs4</span>

This response draws upon the excerpts from the transcript of the video "HIPAA Grade Auditability of Human-in-the-Loop Workflows in the Generative AI Lab."

## **I. Extraction of the Recording (Transcript Excerpts)**

hello everyone and thank you for joining today's session i'm Amit Rasha lead engineer for the generative air lab here at Johnson Labs let me show you how the generative air lab helps you implement HIPPA grade systemwide auditing that's both robust and easy to manage we're going to walk through the role of audit logs their importance in regulated environments like healthcare and how our platform provides real-time visibility into system activity uh whether you are a compliance officer or a product owner audit trails are crucial for understanding user activities and making sure your application is safe compliant and accountable uh we'll also look at specific HIPPA requirements for audit logs how we have addressed them in the application and I will finish with a live demos showing how easy it is to build a custom audit dashboard let's get started by looking at what audit logs actually are and why they matter so much let's begin with the basics uh what exactly are audit logs uh audit logs

are system generated records that capture who did what when and where uh in an application they document user actions like data access modifications login logouts uh deletions exports and more uh forming a digital trail of activity uh this trail is vital for both security monitoring and compliance auditing so why are audit logs important their primary purpose is to provide accountability traceability and visibility into how data and systems are being used they help detect unauthorized activity track changes to critical data investigate incidents and support internal audits uh if something goes wrong audit logs help us understand what happened uh who was involved and how to fix or prevent it in short they are essential for maintaining control and trust in in a system that handles sensitive data in the healthcare industry the importance of audit logs uh goes even deeper uh patient records clinical notes and health data are extremely sensitive unauthorized access or manipulation of this d

ata can have serious ethical and legal consequences audit logs ensure that every access to patient data is recorded and reviewable uh this helps in preventing breaches investigating suspicious activity and ensuring only authorized personals are accessing protected health informations or PHI uh they also play a key role in patient trust patients need assurance that their health data is secure and not being misused now let's talk briefly about HIPPA hippa requires healthcare systems to implement audit controls that record and examine activity in systems that contain or use PHI informations specifically HIPPA mandates tracking of access to patient records uh changes to PHI data login logouts data expose and transmissions uh audit logs must be retained for at least 6 years in many cases and must be uh available for audits and investigations when needed let's now look at how we have implemented these principles in the generative AI lab uh we have built a comprehensive audit dashboard that v

isualizes user and system activity across project and time u let me walk you through a few of the charts that make it easier to monitor users and detect anomalies uh the project activity heat map chart shows peak activity across dates and projects helping identify high users periods or unexpected spikes on specific projects as you can see the higher the activity within the project the more intense or saturated the collar appears on the heat map making it very easy to visually spot spikes in uses uh or periods of inactivity at a glance next we have uh new projects created over time this chart shows number of new projects created over time in the application it gives us a clear view of how uh frequently users are creating projects which can reflect platform engagement team productivity or even uh onboarding trends it also helps uh admins or project managers ensure that the creation of new project is aligned with the organizational goals and just random or duplicated next we have a chart

showing deleted projects over time this is especially important from a data governance and security perspective frequent deletions could indicate normal cleanup or they might signal risky behavior like accidental deletions or in rare cases uh malicious actions uh by visualizing this over time we can quickly detect spikes in deletion activity and identify the users responsible in an audit or incident investigation this chart provides valuable context helping us ask the right questions like uh was this deletion justified was it authorized uh was there any data loss involved uh it also supports enforcement of retention policies by showing how often and how early data is being removed next we have the project export table uh which tracks how often projects are exported from system exports typically involve transferring data out of the platform so this is critical area to monitor from a privacy and uh compliance standpoint uh this chart help us answer questions like who is exporting data an

d how frequently uh are these exports expected or is it unusual uh for example a spike in export activity after hours or by a user who does not typically handle such responsibilities might trigger a suspicion uh in regulated industries like healthcare data exfiltration risks are taken very seriously so this visualization provides early warning signals and audit ready evidence admins can also use the chart to monitor how frequently teams are generating outputs which helps in tracking deliverables uh and monitoring the users now let's take a look at one of the most insightful audit views in the application uh user activity within a project this dashboard captures all the key interactions uh user perform inside a specific project giving us granular visibility into how uh the system is being used uh some of the activities we track uh includes submission and deletions of annotations or completion uh import and export of the data uh adding and removing of team members and so on yeah each act

ion is uh time stamp and tied to a specific user so we can quickly answer questions like who made this change when was it done and what exactly happened uh in healthcare settings where uh auditability is a regulatory requirement this level of transparency is not just helpful it's essential uh it supports internal reviews team accountability error tracking and even uh investigations if a breach or compliance concern arises uh this view also helps uh team leads or project managers understand how actively a project is being worked on and by whom uh offering a datab view into collaborations and ownership uh whether it's a spike in completions a surge of exports or a sudden removal of assignees these dashboards make sure uh nothing goes unnoticed um on this slide I have grouped a few additional dashboards that provide a broader view of the system and user behavior uh at the top we have API requests over time the source trends in overall API traffic uh helping us monitor load detect services

and understand users patterns next we have the HTTP status code distribution this breaks down successful server side responses it's useful for spotting errors or performance uh issues quickly uh on the bottom left we have listed the top 10 users by API calls uh this highlights who is using the system the most which is helpful for both optimization and accountability uh and finally the application uses by hour and day heat map those uh when users are most active this helps inuling updates uh identifying peak users times and optimizing resource availability these dashboards uh together give a well-rounded picture of how the platform is being used and where we might uh need to investigate or improve uh and all charts can be filtered by project users date range event type uh giving teams the flexibility to audit any activity they need and uh quickly and clearly um enabling audit trails uh in generative lab is intensely simple uh and developer friendly uh all you need to do is uh modify yo

ur installer script uh to include two additional flags uh this will automatically enable audit logging and install the necessary elastic search backend if it's not already present uh here's what that looks like in your script uh the first line enables the audit logging globally and second one ensures the elastic search is deployed as part of your stack once this is set uh audit logs starts immediately uh you will begin capturing user actions data access uh events and system activity right away uh making it easier to monitor your environment and stay compliant this makes uh audit enablement not just powerful but also easy to integrate into your existing deployment flow uh now for the exciting part let me walk you through a quick live demo of how to create an audit dashboard uh using the tools uh we will recreate a user activity dashboard that tracks all the actions done inside a project uh by specific users in a specific time period uh let's go ahead and build one now so this is the lan

ding page and as you can see I already have bunch of dashboards created but let's create a new one uh on the top right you can see the create dashboard button here uh once you click on it you'll be navigated to this page so here we need to select the visualization first and uh when you click on the select type dropdown we'll be selecting lens and now you have a bunch of options to uh create different type of charts uh based on different types of metrics and informations uh since we are building a user activity table let's just select table from here now uh I would like to populate the table with the user actions so I'm going to select a row here and I'm going to select a field so since I am trying to show the user actions I'm just going to select actions here and I would like to see let's say top 100 values um in a given time frame so close this and now I want to add some matrix here the first thing that we would like to see is the time stamp and that is why I'm going to select time st

amp from the uh drop down in the field and I want the value of this so I'm going to click on minimum close this the other thing that I want to see is uh the user who actually performed that action so from the field here I'm going to select user which is under user keyword so select the user and I want the actual value of that user now let's close this now yeah we have the top 100 values of the actions along with the timestamp and the usernames uh let's just save and while it's been loaded what we can do is we can add bunch of controls uh to make our audit dashboard more granular so let's click on controls click on add control and now I would like to view the user activities uh for a specific project so I want to add project as a filter let's search for project name and select it uh I would like to see one project at a time so I'm going to disable multiple selection for this filter save and save and close uh I would like to add another control uh to view activities of specific users so

I'm going to look for user here and select on user keyword save and close and I would also like to uh view the activities uh for a specific time period so I'm just going to add a time slider control here okay now we are done let's make it a little bit uh bigger and yeah so this table shows like all of the user activities in the system uh but I would like to look for specific projects now and we have added these filters here so if we click here and select any of the project name the table will show the filtered data so the data that you see is for the specific project B3 isn'tic.qaite QA light and you can also see for example if I want to like uh see the actions of specific users let's say Andre and Dia we can filter it and we can see all of the informations here uh from the date July 31 to August 7 let's just narrow it down to August 1st to August 6 for a week now if we just change this as you can see the data is filtered And you can see the data between August 1 and August 6 uh this i

s very simple to create dash such dashboards like you can create any type of uh charts or dashboards based on your requirement from the uh data that is saved in the elastic search and this concludes the webinar uh I hope this gave you a clear understanding of how audit logs uh work uh why they are essential in healthcare and how we have made them actionable with realtime dashboards uh if you have any questions feel free to drop them in the chat or reach out to me over email or Slack uh I'll be happy to answer them thank you

## **II. Detailed Summarization**

The presentation, led by **Amit Rasha, lead engineer for the Generative AI Lab at John Snow Labs**, focuses on implementing **HIPAA grade system-wide auditing** that is robust and easily manageable within the Generative AI Lab platform.

### **A. Core Concepts and Importance of Audit Logs**

1.  **Definition and Function:** Audit logs are system-generated records that create a **digital trail of activity** by capturing *who* did *what*, *when*, and *where* within an application. They document crucial user actions such as data access, modifications, login/logout, deletions, and exports.

2.  **General Importance:** The primary purposes of audit logs are to provide **accountability, traceability, and visibility** into system and data usage. They are vital for security monitoring, compliance auditing, detecting unauthorized activity, tracking critical data changes, investigating incidents, and supporting internal reviews. They are essential for maintaining control and trust, especially in systems handling sensitive data.

### **B. HIPAA Requirements and Healthcare Compliance**

1.  **Criticality in Healthcare:** In the healthcare industry, the importance of audit logs is heightened because patient records, clinical notes, and health data are **extremely sensitive**. Unauthorized access or manipulation of this data carries serious ethical and legal consequences.

2.  **Protecting PHI:** Audit logs ensure that every instance of patient data access is recorded and reviewable, which helps prevent breaches, investigate suspicious activity, and guarantee that **only authorized personnel** are accessing Protected Health Information (PHI). They are also key to maintaining **patient trust**.

3.  **Specific HIPAA Mandates:** HIPAA requires healthcare systems to implement audit controls to record and examine activities in systems that use or contain PHI. This includes mandatory tracking of:

    1.  Access to patient records.

    2.  Changes to PHI data.

    3.  Login/logout events.

    4.  Data export and transmissions.

4.  **Retention:** Audit logs must be retained for **at least six years** in many cases and must be available for audits and investigations when required.

### **C. Implementation in the Generative AI Lab**

The Generative AI Lab provides a **comprehensive audit dashboard** that visualizes user and system activity across projects and time, making it easier to monitor users and detect anomalies.

**1. Key Visual Audit Charts:**

- **Project Activity Heat Map:** This chart shows peak activity across dates and projects, allowing users to visually spot high-use periods or unexpected spikes; higher activity results in a more intense color.

- **New Projects Created Over Time:** This tracks application engagement, team productivity, or onboarding trends, helping administrators ensure new project creation aligns with organizational goals.

- **Deleted Projects Over Time:** This is critical for data governance and security. Spikes in deletions can signal risky behavior, such as accidental or, in rare cases, malicious actions. It helps provide context for audits (e.g., was the deletion authorized?) and supports the enforcement of retention policies.

- **Project Export Table:** Since exports involve transferring data out of the platform, this is a critical monitoring area for privacy and compliance. This view tracks who is exporting data and how frequently. An unexpected spike in export activity, such as after hours or by an unusual user, provides early warning signals for data exfiltration risks in regulated industries.

**2. Granular User Activity Dashboard:**

- **User Activity within a Project:** This view provides granular visibility by capturing all key interactions a user performs within a specific project. Tracked actions include: submission and deletion of annotations or completions, importing/exporting data, and adding/removing team members.

- **Accountability:** Each action is **time-stamped and tied to a specific user**. This level of transparency is essential in healthcare settings for supporting internal reviews, team accountability, error tracking, and investigations.

**3. Broader System Dashboards:**

- **API Requests Over Time:** Shows trends in overall API traffic for monitoring load, detecting services, and understanding user patterns.

- **HTTP Status Code Distribution:** Useful for breaking down successful server-side responses and quickly spotting performance or server errors.

- **Top 10 Users by API Calls:** Highlights the users utilizing the system the most for optimization and accountability purposes.

- **Application Usage by Hour and Day Heat Map:** Shows when users are most active, which helps in scheduling updates and optimizing resource availability during peak times.

### **D. Enabling and Customizing Audit Trails**

1.  **Simple Enablement:** Enabling audit trails is described as intensely simple and developer-friendly. It only requires modifying the installer script to include two additional flags.

2.  **Backend Integration:** These flags automatically enable global audit logging and install the necessary **Elastic Search backend** if it is not already present, allowing logs to begin capturing user actions and system activity immediately.

3.  **Flexibility and Filtering:** All existing charts can be filtered by event type, project, users, and date range, offering teams flexibility in auditing specific activities.

### **E. Live Demo Summary**

The demo illustrated how to **create a custom user activity dashboard**.

- **Steps:** The creation process involved navigating to the dashboard creation page, selecting the *Lens* visualization, and then choosing the *Table* chart type.

- **Data Selection:** Metrics were populated with user actions (selecting the top 100 values), the minimum **timestamp** value, and the specific **user** keyword value.

- **Adding Granularity (Controls):** To make the dashboard specific and actionable, controls (filters) were added for:

  - **Project Name:** Allowing selection of one project at a time.

  - **User Keyword:** To view activities of specific individuals.

  - **Time Slider Control:** To narrow the focus to a specific time period.

- **Result:** The resulting filtered table allows users to quickly view all user activities for specific projects, specific users (e.g., Andre and Dia), and a specific date range (e.g., August 1 to August 6). The presenter noted that such dashboards are simple to create based on data saved in Elastic Search.

[https://youtu.be/OrogInyE2zg

](https://youtu.be/OrogInyE2zg)This response fulfills your request by first extracting the complete text from the provided source excerpts and then offering a detailed summarization of the content, citing all supporting source material.

## **I. Extraction of the Recording (Transcript Excerpts)**

hello everyone and thank you for joining today's session i'm Amit Rasha lead engineer for the generative air lab here at Johnson Labs let me show you how the generative air lab helps you implement HIPPA grade systemwide auditing that's both robust and easy to manage we're going to walk through the role of audit logs their importance in regulated environments like healthcare and how our platform provides real-time visibility into system activity uh whether you are a compliance officer or a product owner audit trails are crucial for understanding user activities and making sure your application is safe compliant and accountable uh we'll also look at specific HIPPA requirements for audit logs how we have addressed them in the application and I will finish with a live demos showing how easy it is to build a custom audit dashboard let's get started by looking at what audit logs actually are and why they matter so much let's begin with the basics uh what exactly are audit logs uh audit logs are system generated records that capture who did what when and where uh in an application they document user actions like data access modifications login logouts uh deletions exports and more uh forming a digital trail of activity uh this trail is vital for both security monitoring and compliance auditing so why are audit logs important their primary purpose is to provide accountability traceability and visibility into how data and systems are being used they help detect unauthorized activity track changes to critical data investigate incidents and support internal audits uh if something goes wrong audit logs help us understand what happened uh who was involved and how to fix or prevent it in short they are essential for maintaining control and trust in in a system that handles sensitive data in the healthcare industry the importance of audit logs uh goes even deeper uh patient records clinical notes and health data are extremely sensitive unauthorized access or manipulation of this d ata can have serious ethical and legal consequences audit logs ensure that every access to patient data is recorded and reviewable uh this helps in preventing breaches investigating suspicious activity and ensuring only authorized personals are accessing protected health informations or PHI uh they also play a key role in patient trust patients need assurance that their health data is secure and not being misused now let's talk briefly about HIPPA hippa requires healthcare systems to implement audit controls that record and examine activity in systems that contain or use PHI informations specifically HIPPA mandates tracking of access to patient records uh changes to PHI data login logouts data expose and transmissions uh audit logs must be retained for at least 6 years in many cases and must be uh available for audits and investigations when needed let's now look at how we have implemented these principles in the generative AI lab uh we have built a comprehensive audit dashboard that v isualizes user and system activity across project and time u let me walk you through a few of the charts that make it easier to monitor users and detect anomalies uh the project activity heat map chart shows peak activity across dates and projects helping identify high users periods or unexpected spikes on specific projects as you can see the higher the activity within the project the more intense or saturated the collar appears on the heat map making it very easy to visually spot spikes in uses uh or periods of inactivity at a glance next we have uh new projects created over time this chart shows number of new projects created over time in the application it gives us a clear view of how uh frequently users are creating projects which can reflect platform engagement team productivity or even uh onboarding trends it also helps uh admins or project managers ensure that the creation of new project is aligned with the organizational goals and just random or duplicated next we have a chart showing deleted projects over time this is especially important from a data governance and security perspective frequent deletions could indicate normal cleanup or they might signal risky behavior like accidental deletions or in rare cases uh malicious actions uh by visualizing this over time we can quickly detect spikes in deletion activity and identify the users responsible in an audit or incident investigation this chart provides valuable context helping us ask the right questions like uh was this deletion justified was it authorized uh was there any data loss involved uh it also supports enforcement of retention policies by showing how often and how early data is being removed next we have the project export table uh which tracks how often projects are exported from system exports typically involve transferring data out of the platform so this is critical area to monitor from a privacy and uh compliance standpoint uh this chart help us answer questions like who is exporting data an d how frequently uh are these exports expected or is it unusual uh for example a spike in export activity after hours or by a user who does not typically handle such responsibilities might trigger a suspicion uh in regulated industries like healthcare data exfiltration risks are taken very seriously so this visualization provides early warning signals and audit ready evidence admins can also use the chart to monitor how frequently teams are generating outputs which helps in tracking deliverables uh and monitoring the users now let's take a look at one of the most insightful audit views in the application uh user activity within a project this dashboard captures all the key interactions uh user perform inside a specific project giving us granular visibility into how uh the system is being used uh some of the activities we track uh includes submission and deletions of annotations or completion uh import and export of the data uh adding and removing of team members and so on yeah each act ion is uh time stamp and tied to a specific user so we can quickly answer questions like who made this change when was it done and what exactly happened uh in healthcare settings where uh auditability is a regulatory requirement this level of transparency is not just helpful it's essential uh it supports internal reviews team accountability error tracking and even uh investigations if a breach or compliance concern arises uh this view also helps uh team leads or project managers understand how actively a project is being worked on and by whom uh offering a datab view into collaborations and ownership uh whether it's a spike in completions a surge of exports or a sudden removal of assignees these dashboards make sure uh nothing goes unnoticed um on this slide I have grouped a few additional dashboards that provide a broader view of the system and user behavior uh at the top we have API requests over time the source trends in overall API traffic uh helping us monitor load detect services and understand users patterns next we have the HTTP status code distribution this breaks down successful server side responses it's useful for spotting errors or performance uh issues quickly uh on the bottom left we have listed the top 10 users by API calls uh this highlights who is using the system the most which is helpful for both optimization and accountability uh and finally the application uses by hour and day heat map those uh when users are most active this helps inuling updates uh identifying peak users times and optimizing resource availability these dashboards uh together give a well-rounded picture of how the platform is being used and where we might uh need to investigate or improve uh and all charts can be filtered by project users date range event type uh giving teams the flexibility to audit any activity they need and uh quickly and clearly um enabling audit trails uh in generative lab is intensely simple uh and developer friendly uh all you need to do is uh modify yo ur installer script uh to include two additional flags uh this will automatically enable audit logging and install the necessary elastic search backend if it's not already present uh here's what that looks like in your script uh the first line enables the audit logging globally and second one ensures the elastic search is deployed as part of your stack once this is set uh audit logs starts immediately uh you will begin capturing user actions data access uh events and system activity right away uh making it easier to monitor your environment and stay compliant this makes uh audit enablement not just powerful but also easy to integrate into your existing deployment flow uh now for the exciting part let me walk you through a quick live demo of how to create an audit dashboard uh using the tools uh we will recreate a user activity dashboard that tracks all the actions done inside a project uh by specific users in a specific time period uh let's go ahead and build one now so this is the lan ding page and as you can see I already have bunch of dashboards created but let's create a new one uh on the top right you can see the create dashboard button here uh once you click on it you'll be navigated to this page so here we need to select the visualization first and uh when you click on the select type dropdown we'll be selecting lens and now you have a bunch of options to uh create different type of charts uh based on different types of metrics and informations uh since we are building a user activity table let's just select table from here now uh I would like to populate the table with the user actions so I'm going to select a row here and I'm going to select a field so since I am trying to show the user actions I'm just going to select actions here and I would like to see let's say top 100 values um in a given time frame so close this and now I want to add some matrix here the first thing that we would like to see is the time stamp and that is why I'm going to select time st amp from the uh drop down in the field and I want the value of this so I'm going to click on minimum close this the other thing that I want to see is uh the user who actually performed that action so from the field here I'm going to select user which is under user keyword so select the user and I want the actual value of that user now let's close this now yeah we have the top 100 values of the actions along with the timestamp and the usernames uh let's just save and while it's been loaded what we can do is we can add bunch of controls uh to make our audit dashboard more granular so let's click on controls click on add control and now I would like to view the user activities uh for a specific project so I want to add project as a filter let's search for project name and select it uh I would like to see one project at a time so I'm going to disable multiple selection for this filter save and save and close uh I would like to add another control uh to view activities of specific users so I'm going to look for user here and select on user keyword save and close and I would also like to uh view the activities uh for a specific time period so I'm just going to add a time slider control here okay now we are done let's make it a little bit uh bigger and yeah so this table shows like all of the user activities in the system uh but I would like to look for specific projects now and we have added these filters here so if we click here and select any of the project name the table will show the filtered data so the data that you see is for the specific project B3 isn'tic.qaite QA light and you can also see for example if I want to like uh see the actions of specific users let's say Andre and Dia we can filter it and we can see all of the informations here uh from the date July 31 to August 7 let's just narrow it down to August 1st to August 6 for a week now if we just change this as you can see the data is filtered And you can see the data between August 1 and August 6 uh this i s very simple to create dash such dashboards like you can create any type of uh charts or dashboards based on your requirement from the uh data that is saved in the elastic search and this concludes the webinar uh I hope this gave you a clear understanding of how audit logs uh work uh why they are essential in healthcare and how we have made them actionable with realtime dashboards uh if you have any questions feel free to drop them in the chat or reach out to me over email or Slack uh I'll be happy to answer them thank you

## **II. Detailed Summarization**

The presentation, delivered by Amit Rasha, lead engineer for the Generative AI Lab at John Snow Labs, focuses on implementing **HIPAA grade system-wide auditing** that is both robust and easy to manage. The session covers the importance of audit logs, specific HIPAA requirements, how the Generative AI Lab addresses these requirements, and includes a live demo of building a custom audit dashboard.

### **A. The Role and Importance of Audit Logs**

1.  **Definition:** Audit logs are system-generated records that capture **who did what, when, and where** in an application. They form a **digital trail of activity**, documenting user actions such as data access, modifications, login/logout, deletions, and exports.

2.  **General Importance:** The primary function of audit logs is to provide **accountability, traceability, and visibility** into system and data usage. They are essential for detecting unauthorized activity, tracking changes to critical data, investigating incidents, and supporting internal audits. Ultimately, audit logs are crucial for maintaining control and trust in systems handling sensitive data.

3.  **Criticality in Healthcare (PHI):** In the healthcare industry, audit logs are even more critical because patient records, clinical notes, and health data are **extremely sensitive**. Unauthorized access or manipulation of this data can lead to serious ethical and legal consequences. Audit logs ensure that every access to patient data is recorded and reviewable, which helps prevent breaches, investigate suspicious activity, and ensure **only authorized personnel** access Protected Health Information (PHI). This capability also plays a key role in building patient trust.

### **B. HIPAA Requirements for Audit Controls**

HIPAA requires healthcare systems to implement audit controls to record and examine activity in systems that contain or use PHI. Specifically, HIPAA mandates tracking:

- Access to patient records.

- Changes to PHI data.

- Login/logout events.

- Data export and transmissions.

- Retention: Audit logs must be retained for **at least six years** in many cases and must be available for audits and investigations when needed.

### **C. Generative AI Lab's Audit Dashboard Implementation**

The Generative AI Lab has implemented these principles by building a **comprehensive audit dashboard** that visualizes user and system activity across project and time, aiding in monitoring users and detecting anomalies.

**1. Key Visual Monitoring Charts:**

- **Project Activity Heat Map:** Shows peak activity across dates and projects. Higher activity within a project makes the color more intense or saturated on the map, allowing easy visual spotting of usage spikes or periods of inactivity.

- **New Projects Created Over Time:** Tracks how frequently users create projects, reflecting platform engagement, team productivity, or onboarding trends. This helps administrators ensure project creation aligns with organizational goals.

- **Deleted Projects Over Time:** Important for **data governance and security**. Frequent deletions might signal **risky behavior**, such as malicious or accidental actions. This view helps detect spikes in deletion activity, identify responsible users during investigations, and supports the enforcement of retention policies.

- **Project Export Table:** Tracks how often projects are exported from the system. Since exports involve transferring data out of the platform, this is a critical area for monitoring privacy and compliance. This visualization provides **early warning signals** for data exfiltration risks in regulated industries like healthcare, especially if a spike occurs after hours or by an unusual user.

**2. Granular User Activity Dashboard:**

- **User Activity within a Project:** Provides **granular visibility** by capturing all key interactions users perform inside a specific project. Activities tracked include submission/deletion of annotations or completion, data import/export, and adding/removing team members.

- **Transparency and Accountability:** Each action is **time-stamped and tied to a specific user**, enabling quick answers to questions like *who made this change* and *when was it done*. This transparency is essential in healthcare settings for supporting internal reviews, team accountability, error tracking, and investigations related to breaches or compliance concerns.

**3. Broader System-Wide Dashboards:**

- **API Requests Over Time:** Tracks trends in overall API traffic to monitor load, detect services, and understand user patterns.

- **HTTP Status Code Distribution:** Useful for breaking down successful server-side responses and spotting performance issues or errors quickly.

- **Top 10 Users by API Calls:** Highlights the users utilizing the system the most, supporting optimization and accountability.

- **Application Usage by Hour and Day Heat Map:** Shows when users are most active, which helps in scheduling updates and optimizing resource availability during peak times.

### **D. Enabling Audit Trails and Customization**

1.  **Simple Enablement:** Enabling audit trails in the Generative AI Lab is described as **intensely simple and developer-friendly**.

2.  **Configuration:** It requires modifying the installer script to include **two additional flags**. The first flag enables audit logging globally, and the second ensures that the necessary **Elastic Search backend** is deployed as part of the stack. Once configured, audit logs start capturing user actions and system activity immediately.

3.  **Filtering:** All existing charts can be filtered flexibly by project, users, date range, and event type.

### **E. Live Demo of Dashboard Creation**

A live demo was given to show how to build a custom **user activity dashboard** that tracks actions done inside a project by specific users over a specific time period.

- **Visualization Steps:** The process involved selecting **"Lens"** as the visualization and **"Table"** as the chart type.

- **Populating Data:** The table was populated by selecting the top 100 values of **actions**, the minimum value of the **timestamp**, and the actual value of the **user** keyword.

- **Adding Filters (Controls):** To make the data granular, three controls were added:

  - **Project Name:** To view activities for a specific project (with multiple selection disabled).

  - **User Keyword:** To filter activities by specific users (e.g., Andre and Dia).

  - **Time Slider Control:** To filter activities for a specific date range (e.g., narrowed down from July 31-August 7 to August 1-August 6).

- **Data Source:** Custom charts and dashboards are created based on the data that is saved in the **Elastic Search**.