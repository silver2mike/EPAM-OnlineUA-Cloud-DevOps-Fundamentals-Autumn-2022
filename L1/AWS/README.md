## AWS Cloud Basic. Home task

### Register and pass free courses on AWS Skillbuilder. AWS Cloud Practitioner Essentials: Core Services, AWS Cloud Practitioner Essentials: 
Cloud Concepts. Try AWS Cloud Quest: Cloud Practitioner

![skillbuilder]()

### Pass free courses on Amazon qwiklabs

### Review Getting Started with Amazon EC2. Log Into Your AWS Account, Launch, Configure, Connect and Terminate Your Instance. 
Do not use Amazon Lightsail. It is recommended to use the t2 or t3.micro instance and the CentOS operating system.

![account]()

![aws1]()

### Create a snapshot of your instance to keep as a backup.

![aws2]()
![aws3]()

### Create and attach a Disk_D (EBS) to your instance to add more storage space. Create and save 
some file on Disk_D.

create volume
![volumes]()
EBS attached to Epam-test (98db)
![volume2]()
CReate File system, mount and create file test.txt
![volume3]()

### Launch the second instance from backup.
Create AMI image from snapshot
![AMI from snapshot]()

### Detach Disk_D from the 1st instance and attach disk_D to the new instance.
![ebs2]()

mount fs and list the files
![ebs3]()

### Review the 10-minute example. Explore the possibilities of creating your own domain and 
domain name for your site. Note, that Route 53 not free service. Alternatively you can free 
register the domain name .PP.UA and use it.

domain name mikedzn.pp.ua was registered. But also have expireenses with using Route53 before.

jenkins.mikedzn.pp.ua 

### Launch and configure a WordPress instance with Amazon Lightsail link
![wordpress]()
![wordpress1]()
![wordpress2]()
![wordpress3]()
![wordpress4]()

### Review the 10-minute Store and Retrieve a File. Repeat, creating your own repository.
![s3]()

### Review the 10-minute example Batch upload files to the cloud to Amazon S3 using the AWS CLI.
Create a user AWS IAM, configure CLI AWS and upload any files to S3. 
![s3_user]()
![s3_cli1]()
![s3_cli2]()


### Review the 10-minute example Deploy Docker Containers on Amazon Elastic Container Service 
(Amazon ECS). Repeat, create a cluster, and run the online demo application or better other
application with custom settings.
![ecs]()
![ecs1]()
![ecs2]()

### Run a Serverless "Hello, World!" with AWS Lambda.
![lambda]()
![lambda1]()
![lambda2]()
![lambda3]()

### Create a static website on Amazon S3, publicly available (link1 or link2 - using a custom domain 
registered with Route 53). Post on the page your own photo, the name of the educational 
program (EPAM Cloud&DevOps Fundamentals Autumn 2022), the list of AWS services with 
which the student worked within the educational program or earlier and the full list with links 
of completed labs (based on tutorials or qwiklabs). Provide the link to the website in your report
and CV

![static]()
![static1]()
![static2]()
![static3]()

http://silver2mike.static.s3-website-us-east-1.amazonaws.com/

http://epam.mikedzn.pp.ua/
