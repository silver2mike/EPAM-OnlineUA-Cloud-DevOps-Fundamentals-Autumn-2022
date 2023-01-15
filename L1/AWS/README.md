## AWS Cloud Basic. Home task

* ### Register and pass free courses on AWS Skillbuilder AWS Cloud Practitioner Essentials:   
Core Services, AWS Cloud Practitioner Essentials: Cloud Concepts. Try AWS Cloud Quest: Cloud Practitioner

![skillbuilder](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/skillbuilder.png)

* ### Pass free courses on Amazon qwiklabs

[to be later]

* ### Review Getting Started with Amazon EC2. Log Into Your AWS Account, Launch, Configure, Connect and Terminate Your Instance. 
Do not use Amazon Lightsail. It is recommended to use the t2 or t3.micro instance and the CentOS operating system.

2 instances created
![aws1](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/aws1.png)
1 terminated
![aws3](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/aws3.png)

* ### Create a snapshot of your instance to keep as a backup.
Snapshot created
![aws2](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/aws2.png)

* ### Create and attach a Disk_D (EBS) to your instance to add more storage space. Create and save some file on Disk_D.

EBS volume was created
![volumes](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/volumes.png)
EBS volume attached to **Epam-test** instance (98db)
![volume2](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/volume2.png)
File system created, mount and file test.txt created
![volume3](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/volume3.png)

* ### Launch the second instance from backup.
AMI was created from snapshot
![AMI from snapshot](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/AMI-from-snapshot.png)
Instance **Epam-test-from-snapshot-AMI** was created   

* ### Detach Disk_D from the 1st instance and attach disk_D to the new instance.   
EBS volume detached and attached to the new instance
![ebs2](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/ebs2.png)

File system was mounted and got a list of existing files
![ebs3](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/ebs3.png)

* ### Review the 10-minute example. Explore the possibilities of creating your own domain and domain name for your site. Note, that Route 53 not free service. Alternatively you can free register the domain name .PP.UA and use it.

Domain name [mikedzn.pp.ua](http://mikedzn.pp.ua) was registered. (_But also I have expireense with using Route53 before._)   
The domain is using for [Jenkins](http://jenkins.mikedzn.pp.ua) and [EPAM Task Profile](http://epam.mikedzn.pp.ua)

* ### Launch and configure a WordPress instance with Amazon Lightsail link   
Instance was created
![wordpress](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/wordpress.png)
![wordpress1](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/wordpress1.png)
![wordpress2](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/wordpress2.png)   

Site was launched
![wordpress3](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/wordpress3.png)
![wordpress4](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/wordpress4.png)

* ### Review the 10-minute Store and Retrieve a File. Repeat, creating your own repository.
![s3](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/s3.png)

* ### Review the 10-minute example Batch upload files to the cloud to Amazon S3 using the AWS CLI.   
Create a user AWS IAM, configure CLI AWS and upload any files to S3. 
![s3_user](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/s3_user.png)   

ls, cp (upload/download), rm  commands   

![s3_cli1](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/s3-cli1.png)
![s3_cli2](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/s3-cli2.png)


* ### Review the 10-minute example Deploy Docker Containers on Amazon Elastic Container Service (Amazon ECS). Repeat, create a cluster, and run the online demo application or better other application with custom settings.   
 
Service created   
![ecs](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/ecs.png)   

Target group   
![ecs1](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/ecs1.png)   

Web page   
![ecs2](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/ecs2.png)

* ### Run a Serverless "Hello, World!" with AWS Lambda.
Lambda function was created   
![lambda](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/lambda.png)
![lambda1](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/lambda1.png)   

Test the function   
![lambda2](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/lambda2.png)   

Monitoring   
![lambda3](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/lambda3.png)

* ### Create a static website on Amazon S3, publicly available (link1 or link2 - using a custom domain registered with Route 53). Post on the page your own photo, the name of the educational program (EPAM Cloud&DevOps Fundamentals Autumn 2022), the list of AWS services with which the student worked within the educational program or earlier and the full list with links of completed labs (based on tutorials or qwiklabs). Provide the link to the website in your report and CV   

Bucket created   
![static](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/static.png)   

Public access granted   
![static1](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/static1.png)
![static2](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/static2.png)   

Files [index.html](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/index.html) and [error.html](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/error.html) are uploaded
![static3](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/AWS/png/static3.png)   

[http://silver2mike.static.s3-website-us-east-1.amazonaws.com/](http://silver2mike.static.s3-website-us-east-1.amazonaws.com/)

[http://epam.mikedzn.pp.ua/](http://epam.mikedzn.pp.ua/) 
