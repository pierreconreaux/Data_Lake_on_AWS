# IN PROGRESS - AT THE MOMENT THE PROJECT IS A BUNCH OF NOTES

## 1. Create an EMR CLUSTER

***Why do you need EMR Cluster?***

"Since a Spark cluster includes multiple machines, in order to use Spark code on each machine, 
we would need to download and install Spark and its dependencies. 
This is a manual process. 
Elastic Map Reduce (EMR) is a service offered by AWS that negates the need for you, the user, 
to go through the manual process of installing Spark and its dependencies for each machine."

Udacity Course

***Create an Amazon EC2 Key Pair***

We'll need to create an SSH Key pair to securely to the cluster that we'll create.

To do this go to EC2 menu and find Key pair on the left.

Create a key pair with an explicit name.

Download the '.pem' file.

This one half of the key pair and Amazon will put the other on the cluster.

Only when you have both keys together you will be able to connect to the machine.

***Create an EMR Cluster***

From the AWS service menu go to EMR.

Create a cluster with an explicit name and enable loggins so we can track any errors.

You can keep the defaut S3 location.

Make sure you use the cluster setting which will create a long term cluster for you, 
ie the step execution will tear down your cluster once your Spark job finishes.
That's cost effective if you've already perfected your Spark job for your data, but now we'll exploring, testing and developping.

Select last EMR (here emr-5/30.0) version and make sur to select the option with Spark (here Spark 2.4.5)

Note we'll use YARN cluster mode (complet enext)

We'll use m5.xlarge (why) with one node because we'll use a small amount of data 

m indicate the multipurpose family vs r that is optimized for RAM or the C family that is optimized for CPU 
There's a family for each major component
In general is best to start with the M family and to precise when you understand what we want to optimize

More on instance type here :https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html

5 is for the 5 generation (more performance and cheaper than the older one)
large indicate the overall hardware quality (small will have less CPU, memory or storage)
If you want more https://www.ec2instances.info/

Princing for node is somthing as 0.05 per hour https://aws.amazon.com/fr/emr/pricing/

And leastn make sur to select the Key Pair you just created 





You must have an Amazon Elastic Compute Cloud (Amazon EC2) key pair to connect to the nodes in your cluster over a secure channel using the Secure Shell (SSH) protocol.

On the AWS management console go to the EC2 service

Source to Launch your AWS EMR CLUSTER

https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html
