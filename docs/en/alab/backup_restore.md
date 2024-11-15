---
layout: docs
comment: no
header: true
seotitle: Generative AI Lab | John Snow Labs
title: Backup and Restore
permalink: /docs/en/alab/backup_restore
key: docs-training
modify_date: "2022-10-14"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
  nav: annotation-lab
---

Generative AI Lab 6.8 introduces new features designed for users migrating from NLP Lab onto the newest version of Generative AI Lab. With the new Backup and Restore feature, you can transfer projects, annotated data, models, and configurations to the Generative AI Lab 6.8 and above. Simply back up your projects and resources to cloud storage services like Azure Blob or AWS S3, then restore them directly into the new environment, entirely through the user interface.

This release also introduces other small enhancements to existing features, including a “None” option in the de-identification dropdown, allowing you to label text without altering the original content. We’ve also added a helpful visual indicator for labels with associated annotation guidelines—now marked with a colored dot matching the label’s color. 

## Migrate your NLP Lab Backup to Generative AI Lab
Migration to the new version is now a seamless process. Users of the NLP Lab can transfer their models, projects, annotated data and configuration settings to the Generative AI Lab using our Backup and Restore feature. Once backed up, configurations can be easily restored to a Generative AI Lab server. To migrate your data, the process is as follows:

### Steps to Backup Data from NLP Lab
1. **Login** to your current NLP Lab deployment as the admin user.
2. Go to the **`System Settings`** page.
3. Navigate to the **`Backup`** tab.
4. Enter the required **backup details**.
5. Schedule an immediate backup using the **`Backup now`** feature.
6. Monitor the **backup pod status** to ensure the process completes successfully.
```bash
kubectl get pods
```
**Verify Backup:** Upon completion, your backed-up database and files will be visible in cloud storage.

<iframe src="/assets/images/annotation_lab/6.8.0/1.mp4" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

### Steps to Restore Data

1. **Deploy** a fresh instance of Generative AI Lab version 6.8.0 or higher from the marketplace.
2. **Login** to the UI as the admin user.
3. Go to the **`System Settings`** page.
4. Click on the **`Restore`** tab and fill in the necessary details.
5. Click on **`Restore Now`** to initiate the process.
6. Monitor the **restore pod status** to ensure successful completion.
```bash
kubectl get pods
```

**Verify Restoration:** Access the UI, all projects, models, data and files should now be successfully restored.

<iframe src="/assets/images/annotation_lab/6.8.0/2.mp4" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

    