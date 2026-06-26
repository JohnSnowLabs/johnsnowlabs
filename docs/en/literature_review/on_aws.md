---
layout: docs
header: true
seotitle: Literature Review Agent | John Snow Labs
title: Literature Review Agent
permalink: /docs/en/literature_review/on_aws
key: docs-literature-review
modify_date: "2026-06-04"
show_nav: true
sidebar:
    nav: literature-review
---

<div class="h3-box" markdown="1">

## AWS Marketplace

The quickest way to get up and running is through the **AWS Marketplace**. A few clicks and the full appliance is deployed on an EC2 instance in **your own AWS account** — nothing leaves your environment.

Visit the [product page on AWS Marketplace](https://aws.amazon.com/marketplace/) and follow the steps below.

**Getting started:**

1. **Subscribe** to the product on the AWS Marketplace.

2. **Launch** the AMI on a new EC2 instance from the Marketplace console.
   - We recommend **m5.2xlarge** or larger (8 vCPU / 32 GB RAM) for most workloads.
   - Only **port 80** needs to be open in the security group — the UI runs on port 80.

3. **Wait for the services to come up.** The first boot pulls Docker images and initialises the database. Expect around **10–15 minutes**, depending on your region. You'll see a loading screen until everything is ready.

4. **Open the workspace** in your browser:
   - Navigate to `http://<INSTANCE_PUBLIC_IP>`.
   - The default **password is the EC2 instance ID** — you'll find it in the AWS EC2 console.

5. **Run the setup wizard** (`/setup`):
   - Pick your LLM provider: **Amazon SageMaker** (models running in your own account) or the **DeepLens API** (`api.deeplens.health`).
   - Enter your API key.
   - Optionally configure keys for external search sources — NCBI, Semantic Scholar, Europe PMC, and OpenAlex are all supported but none are required.

</div><div class="h3-box" markdown="1">

## Recommended Instance Types

| Use | Instance type | vCPU | RAM |
|---|---|---|---|
| Evaluation / small teams | `m5.xlarge` | 4 | 16 GB |
| Standard workloads | `m5.2xlarge` | 8 | 32 GB |
| Large / parallel runs | `m5.4xlarge` | 16 | 64 GB |

</div><div class="h3-box" markdown="1">

## Configuration

All configuration is managed through the in-app setup wizard. On first boot, the wizard walks you through connecting your LLM and search API keys — no manual file editing required.

**API keys configured through the setup wizard:**

| Key | Purpose |
|---|---|
| DeepLens API key | LLM and search access (required) |
| NCBI / PubMed API key | Higher rate limits for PubMed searches (optional) |
| Semantic Scholar API key | Higher rate limits (optional) |
| Europe PMC API key | Higher rate limits (optional) |
| OpenAlex API key | Higher rate limits (optional) |

</div><div class="h3-box" markdown="1">

## Secure HTTPS Access via CloudFront

Out of the box, the appliance listens on HTTP port 80. If you need HTTPS access from the public internet, the simplest option is to put a CloudFront distribution in front of your EC2 instance. The CloudFront resources involved are Free Tier Eligible, and the setup takes only a few minutes.

1. Create the CloudFormation stack YAML:

   ```yaml
   AWSTemplateFormatVersion: '2010-09-09'
   Description: >
     Expose Literature Review over HTTPS via CloudFront.
     Provide the EC2 instance hostname as input.
   Parameters:
     LrInstanceHostName:
       Description: Public hostname or IP of the Literature Review EC2 instance
       Type: String
   Resources:
     CloudFront:
       Type: AWS::CloudFront::Distribution
       Properties:
         DistributionConfig:
           Enabled: true
           DefaultCacheBehavior:
             AllowedMethods: [DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT]
             DefaultTTL: 0
             MaxTTL: 0
             ForwardedValues:
               QueryString: true
               Cookies:
                 Forward: all
             TargetOriginId: LrOrigin
             ViewerProtocolPolicy: redirect-to-https
           Origins:
             - Id: LrOrigin
               DomainName: !Ref LrInstanceHostName
               CustomOriginConfig:
                 HTTPPort: 80
                 OriginProtocolPolicy: http-only
   ```

2. Deploy the stack through the AWS Console or CLI, passing in your EC2 instance's public hostname.
3. Once the stack is deployed, access Literature Review Agent using the CloudFront distribution domain name over HTTPS.

</div>
