## 2. Create an EMR CLUSTER from terminal

Install AWS on terminal: ```pip install awscli```

Configure AWS :```aws configure``` and complete with your access key ID and secret access key.

Configure Sparkify Cluster :
```
aws emr create-cluster --name Sparkify_Cluster --use-default-roles --release-label emr-5.30.0 --instance-type m5.xlarge  --instance-count 1  --applications Name=Spark Name=Zeppelin --log-uri s3://Sparkify/  --ec2-attributes KeyName=Sparkify_Key
```
You will see this kind of output:

![alt text](/picture/terminal.png)


You can check if the cluster is showing up in AWS browser or you can type:
```
aws emr describe-cluster --clusterid <paste_your_id>
```
Source :
