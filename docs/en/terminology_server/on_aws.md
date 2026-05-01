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


- Once the services are up, you can login to the Terminology Server UI using the following credentials:
  - Username: admin@term.server
  - Password: <<instance_id>> (You can find the instance id in the AWS EC2 console)

  ![Terminology Service UI](/assets/images/term_server/ui.png)

## Secure access to Terminology Server on AWS

1. When installed via the AWS Marketplace, Terminology Server has a private IP address and listens on an unsecured HTTP port. You can ask your DevOps department to incorporate the resource to your standard procedures to access from the internet in a secure manner. Alternatively, a Cloud Formation script is available that can be used to create a frontend proxy using (CloudFront). Those resources are Free Tier Eligible. 
2. Create the AWS Cloud Formation Script in YAML format, from the listed script cloudformation_https.yaml
   - ```console
        vi cloudformation_https.yaml
     ```
     ```yaml
         AWSTemplateFormatVersion: '2010-09-09'
         Metadata:
           License: Apache-2.0
         Description: 'AWS CloudFormation To access TerminologyServer via https:
          Create an Amazon EC2 instance running the TerminologyServer Linux/UNIX AMI. Once the
          TerminologyServer instance is created, provide instance hostname as input. This Cloudfromation
          Creates Cloudfront. You can use Cloudfront Domain URL to access TerminologyServer
          via https protocol.
          '
         Parameters:
          TsInstanceHostName:
            Description: HostName of the TerminologyServer InstanceID
            Type: String
            ConstraintDescription: HostName of the TerminologyServer InstanceID
        
         Resources:
          CloudFront:
            Type: AWS::CloudFront::Distribution
            Properties:
              DistributionConfig:
                Enabled: True
                DefaultCacheBehavior:
                  AllowedMethods:
                    - DELETE
                    - GET
                    - HEAD
                    - OPTIONS
                    - PATCH
                    - POST
                    - PUT
                  DefaultTTL: 0
                  MaxTTL: 0
                  MinTTL: 0
                  Compress: True
                  ForwardedValues:
                    QueryString: true
                    Headers:
                      - '*'
                    Cookies:
                      Forward: all
                  TargetOriginId: EC2CustomOrigin
                  ViewerProtocolPolicy: redirect-to-https
                Origins:
                  - DomainName: !Ref TsInstanceHostName
                    Id: EC2CustomOrigin
                    CustomOriginConfig:
                      HTTPPort: '80'
                      OriginProtocolPolicy: http-only
         Outputs:
           CloudfrontURL:
             Description: Cloudfront URL to access TerminologyServer
             Value: !Join ["", ['https://', !GetAtt [CloudFront, DomainName]]]
     ```
3. Click Create a stack, “Upload a template file”. Give the Stack a name and enter the TerminologyServer instance Hostname(from the EC2 console) as a parameter.
   - ![createStack](/assets/images/term_server/aws/create_stack.png)
4. Next -> Next -> Acknowledge that AWS CloudFormation might create IAM resources. -> Submit. Wait a few minutes until all resources are created.
   - ![ack](/assets/images/term_server/aws/ack.png)
5. Once created, go do the Outputs tab and click on the Terminology Server URL. You may need to refresh the view. 
   - ![output](/assets/images/term_server/aws/stack-output.png)
6. Copy the output url.
7. SSH into the ec2 instance where Terminology Server is running.
8. Cd to home dir, Replace the output_url in the cmd below with the url from step 6. Then Execute the cmd in your Terminology Service Instance.

```shell
curl -sSL https://s3.us-east-1.amazonaws.com/artifacts.terminologyservice.johnsnowlabs.com/upgrade.sh | bash -s "output_url"
```
