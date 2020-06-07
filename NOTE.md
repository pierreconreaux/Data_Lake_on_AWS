# Create EMR Sparkify cluster

## 1. Create an EMR CLUSTER on AWS

***Why do you need EMR Cluster?***

Spark cluster includes multiple machines to use Spark code on each one, we need to download and install Spark as well as its dependencies on all machines. Elastic Map Reduce (EMR) allow us to use Spark on every single machine without the necessity to install Spark on each one.

***Create an Amazon EC2 Key Pair***

We need to create an SS Key pair to securely connect to the cluster we'll create.

Go to EC2 menu and click on Key pair on the left.

Create a key pair with an explicit name as ```Sparkify_Key```.

Download the '.pem' file.

This is one half of the key pair and Amazon will put the other on the cluster.

Only when we have both keys together we'll be able to connect to the machines.

***Create an EMR Cluster***

From the AWS service menu choose EMR.

- Create a cluster with an explicit name, as ```Sparkify_Cluster```. Don't forget to enable loggins so we can track any errors.
- You can keep the defaut S3 location but we'll choose something simpler to remember ```s3://sparkify/```
- Make sure to use cluster setting. The step execution option will tear down your cluster once your Spark job will finish. This woud be cost effective, but now we are here to exploring, testing and developping.
- Select last EMR version and select Spark option. Here we'll use emr-5/30.0 with Spark 2.4.5. Note that it'll use YARN cluser mode (```more```). 
- Choose a m5.xlarge. M for mulipurpose (the other one optimized a specific step, i.e c is optimized for CPU, more https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html). 5 to use the latest version whose are cheaper and more efficient that the older one. Large indicate the hardware quality, opposed to small which have less CPU, memory and storage. 
- To test we can use 1 node and increase it after. Note that the pricing for node is about 0.05 per hour https://aws.amazon.com/fr/emr/pricing/
- ***Make sure to select the Key Pair we've just created.***

Source to Launch your AWS EMR CLUSTER

https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html

## 2. Create an EMR CLUSTER from terminal

Install AWS on terminal: ```pip install awscli```

Configure AWS :```aws configure``` and complete with your access key ID and secret access key.

Configure Sparkify Cluster :
```
aws emr create-cluster --name Sparkify_ClusterII --use-default-roles --release-label emr-5.30.0 --instance-type m5.xlarge  --instance-count 1  --applications Name=Spark Name=Zeppelin --log-uri s3://Sparkify/  --ec2-attributes KeyName=Sparkify_Key
```

More : https://docs.aws.amazon.com/cli/latest/reference/emr/create-cluster.html

