---
layout: docs
header: true
seotitle: Terminology Server | John Snow Labs
title: Terminology Server 
permalink: /docs/en/terminology_server/on_prem_deploy
key: docs-term-server
modify_date: "2025-04-01"
show_nav: true
sidebar:
    nav: term-server
---

## **On-Prem Installation Guide**

**Prerequisites:**

* Docker
* awscli (AWS command-line interface)
* jq (lightweight command-line JSON processor)

**Step 1: Get your license file or license key**

If license file is provided, place your license file in a local path. If license key is provided, you can directly use it in next step.

**Step 2: Run the Installation/Upgrade Command**

* Install `latest` version using your license file path or license key:

```bash
curl -sSL https://s3.us-east-1.amazonaws.com/artifacts.terminologyservice.johnsnowlabs.com/install.sh | bash -s "YOUR_LICENSE_FILE_PATH_OR_LICENSE_KEY"
```

For more information regarding installation of Terminology Server on a dedicated server please contact us at [support@johnsnowlabs.com](mailto:support@johnsnowlabs.com).

## Recommended Configurations

<table class="table2">
  <tr>
    <th>System requirements</th>
    <td>You can install Terminology Server on a Ubuntu 20+ machine.</td>
  </tr>
  <tr>
    <th>Port requirements</th>
    <td>The service uses port <bl>8000</bl>. So it expects the port to be unused.</td>
  </tr>
  <tr>
    <th>Server requirements</th>
    <td>The minimal required configuration is <bl>16GB RAM, 8 Core CPU, 300GB+ Storage</bl>.
        <br /><br />
    The ideal configuration for a smooth performance is <bl>32 GB RAM and 16 Core CPU</bl>.
    </td>
  </tr>
  <tr>
    <th>Web browser support</th>
    <td>Terminology Server is tested with the latest version of Google Chrome and is expected to work in the latest versions of:
      <ul>
      <li>Google Chrome</li>
      <li>Apple Safari</li>
      <li>Mozilla Firefox</li>
      </ul>
    </td>
  </tr>
</table>

