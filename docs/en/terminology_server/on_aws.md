---
layout: docs
header: true
seotitle: Terminology Server | John Snow Labs
title: Terminology Server 
permalink: /docs/en/terminology_server/on_aws
key: docs-term-server
modify_date: "2025-04-01"
show_nav: true
sidebar:
    nav: term-server
---

## AWS Marketplace

One of the most straight forward method to start using Terminology Server is using the AWS Marketplace. Using AWS Marketplace, the Terminology Server will be deployed on your AWS EC2 instance with just a few clicks. There is a Software Price and AWS Infrastructure price associated this with this installation method (Details are in the product page in AWS Marketplace)


Visit the [product page on AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-3hta3hebivvrk) and follow the instructions to subscribe and deploy

**Steps to get started:**
- Subscribe to the product on the AWS Marketplace.
    ![Terminology Service Subscription](/assets/images/term_server/subscribe.png)
- Once subscribed, deploy it on a new machine

    ![Terminology Service Launch](/assets/images/term_server/launch.png)

- After deployment, the application will be accessible on http://INSTANCE_IP.

  <b> It takes around 20 minutes (depending upon your region) for the services to be up and running. You will see a loading screen while the services are being configure.</b>

  ![Terminology Service Loading](/assets/images/term_server/loading.png)

  <b>Once the services are up, you will be automatically redirected to the Terminology Server UI where you can start using it.</b>

  ![Terminology Service UI](/assets/images/term_server/ui.png)
