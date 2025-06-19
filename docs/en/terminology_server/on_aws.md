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

One of the most straight forward method to start using Terminology Server is using the AWS Marketplace. Using AWS Marketplace, the Terminology Server will be deployed on your AWS EC2 instance with just a few clicks. There is a Software Price and AWS Infrastructure price associated this with this installation method (Details are in the product page in AWS Marketplac)


Visit the [product page on AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-qvxkeeied2ze6) and follow the instructions on the video to subscribe and deploy

**Steps to get started:**
- Subscribe to the product on the AWS Marketplace
- Deploy it on a new machine
- Wait for the services to be active. This might take few minutes for the initial boot. 
<br/>
    To check the status, login to the instance and run this command
<br/>
`sudo systemctl status terminology-server.service`


    ![Terminology Service Staus](/assets/images/term_server/terminology_service_status.png)
- Once all the status is active, access the terminology server on http://INSTANCE_IP
