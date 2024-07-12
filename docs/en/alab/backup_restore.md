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

## Backup

You can enable daily backups by adding several variables with `--set` option to helm command in `annotationlab-updater.sh`:

```bash
backup.enable=true
backup.files=true
backup.s3_access_key="<ACCESS_KEY>"
backup.s3_secret_key="<SECRET_KEY>"
backup.s3_bucket_fullpath="<FULL_PATH>"
```

`<ACCESS_KEY>` - your access key for AWS S3 access

`<SECRET_KEY>` - your secret key for AWS S3 access

`<FULL_PATH>` - full path to your backup in s3 bucket (f.e. `s3://example.com/path/to/my/backup/dir`)

**Note:** File backup is enabled by default. If you don't need to backup files, you have to change

```bash
backup.files=true
```

to

```bash
backup.files=false
```

<br>

#### Configure Backup from the UI

In 2.8.0 release, Generative AI Lab added support for defining database and files backups via the UI. An _admin_ user can view and edit the backup settings under the **Settings** menu. Users can select different backup periods and can specify a target S3 bucket for storing the backup files. New backups will be automatically generated and saved to the S3 bucket following the defined schedule.

<img class="image image__shadow" src="/assets/images/annotation_lab/4.1.0/backupRestoreUI.png" style="width:100%;"/>

### Migrate your NLP Lab Backup to Generative AI Lab 6

Migrating to the new version is easy! Users who are using an older version of the NLP Lab can migrate their annotated data and configured settings to the new Generative AI Lab 6 through our Backup and Restore feature. This process enables users to back up their data and files from a CPU-based instance to the cloud of their choice (Azure Blob/AWS S3) and then restore the configurations to a GPU-based instance. You must follow the steps outlined below to seamlessly back up and restore all your data from an old instance to the new Generative AI Lab 6.

<iframe src="/assets/images/annotation_lab/6.0.0/BackupAndRestore.mp4" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

**Follow these steps to migrate your data**:
#### 1. Backup Data:
- Navigate to the Backup page of your CPU-based instance.
- Enter backup details.
- Schedule an immediate backup via backend modification: 
```bash
kubectl edit cronjob
```
- Monitor the backup pod status: 
```bash
kubectl get pods
```
#### 2. Verify Backup:
- Upon completion, your backed-up database and files will be visible in cloud storage.

#### 3. Restore Data:
- Access the backend of your target GPU-based instance.
- Transfer backed-up data from cloud storage to artifacts/restore/database.
- Perform database restoration: 
```bash
sudo ./restore_all_databases.sh <backed-up_database_name>
```
- Copy backed-up files from cloud storage to artifacts/restore/files.
- Execute file restoration: 
```bash
sudo ./restore_files.sh <backed-up_files_name>
```
#### 4. Verify Restoration:
- Access the UI, all data and files should now be successfully restored.


## Restore

#### Database

To restore Generative AI Lab from a backup you need a fresh installation of Generative AI Lab. Install it using `annotationlab-install.sh`. Now, download the latest backup from your S3 bucket and move the archive to `restore/database/` directory. Next, go to the `restore/database/` directory and execute script `restore_all_databases.sh` with the name of your backup archive as the argument.

For example:

```
cd restore/database/
sudo ./restore_all_databases.sh 2022-04-14-annotationlab-all-databases.tar.xz
```

> **Note:** <br>
>
> 1. You need `xz` and `bash` installed to execute this script. <br>
> 2. This script works only with backups created by Generative AI Lab backup system. <br>
> 3. Run this script with `sudo` command

After database restore complete you can check logs in `restore_log` directory created by restore script.

<br>

#### Files

Download your files backup and move it to `restore/files/` directory. Go to `restore/files/` directory and execute script `restore_files.sh` with the name of your backup archive as the argument. For example:

```
cd restore/files/
sudo ./restore_files.sh 2022-04-14-annotationlab-files.tar
```

> **Note:** <br>
>
> 1. You need `bash` installed to execute this script. <br>
> 2. This script works only with backups created by Generative AI Lab backup system. <br>
> 3. Run this script with `sudo` command

<br>

#### Reboot

After restoring database and files, reboot Generative AI Lab:

```
sudo reboot
```
