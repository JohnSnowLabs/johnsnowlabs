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

<div class="h3-box" markdown="1">

## Backup and Restore

Generative AI Lab includes a comprehensive **Backup and Restore** feature that enables administrators to safeguard and migrate all critical system components — including projects, annotated data, models, and configurations — to secure cloud storage such as **AWS S3** or **Azure Blob**.  
This functionality is essential for disaster recovery, system migration, and long-term data retention. All operations can be performed directly through the user interface, without requiring manual scripts or CLI commands.

Recent improvements make the backup process more reliable and interactive:
- **Immediate input validation** ensures that all fields (e.g., storage credentials, paths, frequency) are verified before saving, preventing misconfigured schedules.
- The **Backup page now auto-refreshes** whenever a new backup is created, modified, or completed, so administrators always see the most up-to-date backup list and status without manual reloading.
- Administrators can also perform **ad-hoc (on-demand) backups** at any time — without relying solely on a scheduled run. This is useful when you want to create a one-time snapshot before making system changes or updates.

---

### Scheduling Backups

To create a recurring backup schedule:

1. Navigate to **System Settings → Backup**.
2. Enter the necessary configuration details such as:
   - **Target Storage Type:** Choose between **AWS S3** or **Azure Blob**.
   - **Storage Credentials:** Provide access credentials, or if running on AWS with IAM role permissions, simply specify the bucket/container path (no keys required).
   - **Backup Frequency:** Set how often backups should run automatically (e.g., daily, weekly).
   - **Backup Retention:** Optionally configure how many past backups to keep.
3. The system now validates your inputs instantly, highlighting any missing or invalid fields before you can save or start a backup.
4. Once the configuration is valid, click **Save Schedule**.

The new real-time validation helps prevent scheduling issues by ensuring that all required parameters are properly defined before activation.

---

### Running an Immediate (On-Demand) Backup

In addition to scheduled backups, admins can manually trigger an immediate backup at any time:

1. Go to **System Settings → Backup**.
2. Click **Run Backup Now**.
3. Monitor the progress of the backup in the same view — the page automatically refreshes to show the new entry once the process starts or completes.

This capability makes it simple to perform a quick backup before applying upgrades, restoring data, or modifying configurations.

---

### Restoring from a Backup

Restoration follows a similarly intuitive process:

1. Navigate to **System Settings → Restore**.
2. Choose your backup source (**AWS S3** or **Azure Blob**) and enter the path to the desired backup.
3. Click **Restore Now**.
4. The restore status updates automatically on the page as the process runs.

Once complete, all projects, models, data, and configurations from the backup become available in the environment, allowing you to resume work immediately.

---

### Typical Migration Workflow (NLP Lab → Generative AI Lab)

For users migrating from **NLP Lab**, this feature enables full transfer of models, annotations, and settings to the Generative AI Lab environment.  
The process involves backing up data in NLP Lab, uploading it to cloud storage, and restoring it in Generative AI Lab.  
<iframe width="800" height="450" src="https://www.youtube.com/embed/wUiDq5peZK4?si=v2Q6XCtK01KmcKJa&hd=1" title="NLP Lab to Generative AI Lab migration - Step 1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="800" height="450" src="https://www.youtube.com/embed/8JihFXLfHGc?si=hczRk74snB9cP8Es&hd=1" title="NLP Lab to Generative AI Lab migration - Step 2" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

With these enhancements, the Backup and Restore system now offers a smoother, safer, and more responsive experience — ensuring administrators can protect their data with minimal effort and complete confidence.


</div>