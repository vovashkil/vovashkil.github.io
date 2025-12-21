# Deploying Containerized Applications to Amazon EKS

* back to AWS Cloud Institute repo's root [aci.md](../../aci.md)
* back to [AWS Cloud Fundamentals 2](../aws-cloud-fundamentals-2.md)
* back to repo's main [README.md](../../../../README.md)

## Lab overview

In this hands-on lab, you deploy and run a pre-built containerized application on an Amazon Elastic Kubernetes Service (Amazon EKS) cluster using an AWS Code Editor development environment. Over the previous four labs, you progressively explored different deployment methods, starting with a manual deployment on an Amazon Elastic Compute Cloud (Amazon EC2) instance, followed by serverless computing with AWS Lambda, containerization with Docker, and running containers on AWS Fargate and Amazon Elastic Container Service (Amazon ECS). Building upon that foundation, you now learn how to create an Amazon EKS cluster and managed node group using eksctl, and deploy containerized applications to the cluster using kubectl. This includes creating pods both imperatively with kubectl run and declaratively by applying YAML specifications. By the end of this lab, you would have gained practical experience with Amazon EKS, AWS Code Editor, Amazon Elastic Container Registry (Amazon ECR), and deploying containerized applications to a Kubernetes cluster using various kubectl commands. You would also understand the workflow of managing Kubernetes on AWS using multiple tools and approaches.

Objectives
By the end of this lab, you should be able to do the following:

Install and configure command line utilities for Amazon EKS.
Create and configure an Amazon EKS cluster and node group.
Deploy containerized applications from Amazon ECR to your Amazon EKS cluster using AWS Code Editor.
Create pods on the Kubernetes cluster using kubectl run (imperative approach).
Create pods on the Kubernetes cluster using kubectl apply -f (declarative approach).
View logs of running pods on the Kubernetes cluster using kubectl logs.
Technical knowledge prerequisites
Familiarity with container concepts and basic knowledge of networking is required for this lab. You should also be comfortable using the Linux command line.

Duration
This lab requires 60 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Caution: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Command: A command that you must run.
 Consider: A moment to pause to consider how you might apply a concept in your own environment or to initiate a conversation about the topic at hand.
 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Note: A hint, tip, or important guidance.
 Learn more: Where to find more information.
 Task complete: A conclusion or summary point in the lab.
 Warning: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made).
Start lab
To launch the lab, at the top of the page, choose Start Lab.

 Caution: You must wait for the provisioned AWS services to be ready before you can continue.

To open the lab, choose Open Console .

You are automatically signed in to the AWS Management Console in a new web browser tab.

 Warning: Do not change the Region unless instructed.

Common sign-in errors
Error: Choosing Start Lab has no effect
In some cases, certain pop-up or script blocker web browser extensions might prevent the Start Lab button from working as intended. If you experience an issue starting the lab:

Add the lab domain name to your pop-up or script blocker’s allow list or turn it off.
Refresh the page and try again.
Lab environment
Here is a brief overview of the architecture that is pre-provisioned as part of the lab start process:

Virtual Private Cloud (VPC): The template creates a new VPC with public and private subnets across multiple Availability Zones. This VPC will host the EKS cluster and its associated resources.

Security Groups: Several security groups are created to control inbound and outbound traffic for the EKS control plane, worker nodes, and the Code Editor development environment.

Identity and Access Management (IAM) Roles and Policies: The template defines various IAM roles and policies required for EKS, worker nodes, and the Code Editor environment. These roles provide the necessary permissions for creating and managing the EKS cluster, worker nodes, and other AWS resources.

Elastic Container Registry (ECR): An ECR repository named url-checker is created to store the Docker image for the containerized application that will be deployed to the EKS cluster.

Code Editor Environment: An AWS Code Editor development environment is provisioned within the VPC. The Code Editor instance is configured with the required permissions and tools (for example, kubectl, eksctl) to interact with the EKS cluster. Additionally, an SSM Automation document is included to bootstrap the Code Editor instance with necessary configurations and setup steps.

Amazon EKS Cluster: The template creates an EKS cluster named eks-lab-cluster with a managed node group. The cluster is configured to use the specified Kubernetes version, and the node group consists of three t3.medium instances initially.

Services used in this lab
AWS Code Editor
AWS Code Editor allows you to write, run, and debug your code with just a browser. With AWS Code Editor, you have immediate access to a rich code editor, integrated debugger, and built-in terminal with pre-configured AWS Command Line Interface (AWS CLI). You can get started in minutes and no longer have to spend the time to install local applications or configure your development machine.

Elastic Kubernetes Service (Amazon EKS)
Amazon EKS is a managed service that makes it easy for you to use Kubernetes on AWS without needing to install and operate your own Kubernetes control plane.

Task 1: Connecting to the AWS Code Editor environment
In this task, you connect to your AWS Code Editor development environment.

Copy the LabInstanceURL value URL link from the Lab Information section to the left of these instructions and paste it into a new browser tab.

 Expected output: The browser takes you to the AWS Code Editor environment that you use during this lab.

 Learn more: Refer to AWS Code Editor Features in the Additional resources section for more information on AWS Code Editor interface.

Observe the AWS Code Editor user interface (UI).

You will notice the Welcome page with provides an overview of the service. For the purpose of this lab, we will close the Welcome page as we will be working of the bash terminal located in the bottom of the page.

The bottom of the page is a Bash terminal. Commands will be entered or run from this default terminal for the rest of this lab, unless otherwise instructed.

The left side of the screen is the navigation pane, which shows the file system.

Task 2: Deploy an Amazon EKS cluster and managed node group
In this task, you use two utilities to bootstrap your Kubernetes application: kubectl and eksctl. Kubectl is a command-line tool that allows you to interact with resources inside your Kubernetes clusters. Among other things, you can use kubectl to deploy applications, create namespaces, scale deployments, and view logs. On the other hand, eksctl is a CLI tool for creating and managing clusters on EKS - Amazon’s managed Kubernetes service. While both tools enable you to work with Kubernetes clusters, they have different scopes and uses. Kubectl provides control over resources inside of a cluster, whereas eksctl helps you to manage the cluster itself.

Let’s start by installing kubectl.

 Command: To download the Kubernetes kubectl utility, enter the following command:

sudo curl --location -o /usr/local/bin/kubectl https://s3.us-west-2.amazonaws.com/amazon-eks/1.30.0/2024-05-12/bin/linux/amd64/kubectl
 Expected output:


************************
**** EXAMPLE OUTPUT ****
************************

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 49.0M  100 49.0M    0     0  92.7M      0 --:--:-- --:--:-- --:--:-- 92.5M
 Learn more: Refer to Installing or updating kubectl in the Additional resources section for more information.

 Command: To make kubectl an executable file, enter the following command:

sudo chmod +x /usr/local/bin/kubectl
 Expected output:

None, unless there is an error.

 Command: To display the version of the kubectl utility and verify it is installed properly, enter the following command:

kubectl version --output=yaml --client
 Expected output: The output should look similar to this:


************************
**** EXAMPLE OUTPUT ****
************************

clientVersion:
  buildDate: "2024-04-30T23:56:29Z"
  compiler: gc
  gitCommit: 59ddf7809432afedd41a880c1dfa8cedb39e5a1c
  gitTreeState: clean
  gitVersion: v1.30.0-eks-036c24b
  goVersion: go1.22.2
  major: "1"
  minor: 30+
  platform: linux/amd64
kustomizeVersion: v5.0.4-0.20230601165947-6ce0bf390ce3
Next, you install the eksctl command line utility.

In this lab, you use eksctl to create a clusters, but administrators can also use the AWS Management Console to create, update, and manage clusters.

 Command: To download and unzip eksctl, enter the following command:

curl --location "https://github.com/eksctl-io/eksctl/releases/download/v0.183.0/eksctl_Linux_amd64.tar.gz" | tar xz -C /tmp
 Expected output:


************************
**** EXAMPLE OUTPUT ****
************************

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100 32.9M  100 32.9M    0     0  19.8M      0  0:00:01  0:00:01 --:--:-- 23.9M
 Command: To move eksctl to the /usr/local/bin directory enter the following command:

sudo mv -v /tmp/eksctl /usr/local/bin
 Expected output:


‘/tmp/eksctl’ -> ‘/usr/local/bin/eksctl’
 Note: By moving the downloaded file to the /usr/local/bin folder, you can call the eksctl command without including its full filepath because the directory is already in your PATH.

 Command: To verify eksctl is installed, enter the following command:

eksctl version
 Expected output:


0.183.0
Now that you installed the utilities required to create and manage Amazon EKS and Kubernetes, you create your first Amazon EKS cluster.

 Command: To save the region you are working in and your account ID to shell variables, enter the following command:

TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
export AWS_REGION=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/dynamic/instance-identity/document | jq -r '.region')
ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)
echo "Your AWS Account ID is $ACCOUNT_ID and you are working in the $AWS_REGION region"
 Expected output:


************************
**** EXAMPLE OUTPUT ****
************************

Your AWS Account ID is 1234567890 and you are working in the us-west-2 region
 Note: In the following step, you deploy an Amazon EKS cluster called eks-lab-cluster, along with a managed node group. Creating a new cluster can take 10–15 minutes to complete. To demonstrate the process of creating an Amazon EKS cluster without waiting the full 10-15 minutes, this lab guides you through starting a new Amazon EKS cluster deployment called eks-lab-cluster with a managed node group. You initiate the creation, observe it begin, then cancel the process before completion. This approach provides insight into standing up a new Amazon EKS cluster without needing to wait for the full build time. Instead of the new cluster, you connect to a prebuilt cluster that has already been created so you can continue with the lab without delay. The prebuilt cluster allows you to experience the remainder of the lab without waiting for cluster creation.

 Command: To initiate the deployment of eks-lab-cluster, enter the following command, and after the process begins, press Ctrl+C to cancel the deployment.

eksctl create cluster \
--name eks-lab-cluster \
--nodegroup-name worknodes-1 \
--node-type t3.medium \
--nodes 2 \
--nodes-min 1 \
--nodes-max 3 \
--managed \
--version 1.30 \
--region ${AWS_REGION}
 Expected output:

None, unless there is an error.

 Learn more: When you create an Amazon EKS cluster using eksctl, the utility builds a new Virtual Private Cloud (VPC), three public subnets, and three new private subnets for use with the Amazon EKS control plane cluster and nodes. However, there are additional command flags you can use to specify the use of an existing VPC and subnets. Refer to Amazon EKS networking in the Additional resources section for more information.

The following list describes each flag used on the command you just entered:

eksctl create cluster: Creates a new Amazon EKS cluster.
–name eks-lab-cluster: Specifies a name for the Amazon EKS cluster.
–nodegroup-name worknodes-1: Specifies a name for the Amazon EKS node group.
–node-type t3.medium: Designates the instance type used for the worker nodes.
–nodes 2: Sets the desired number of worker nodes in the Auto Scaling configuration.
–nodes-min 1: Sets the minimum number of worker nodes Auto Scaling configuration.
–nodes-max 3: Sets the maximum number of worker nodes in the Auto Scaling configuration.
–managed: Creates a fully managed node group. For more information, refer to the Additional resources section at the end of the lab.
–version 1.30: Specifies the version of Kubernetes to deploy in the Amazon EKS cluster.
–region ${AWS_REGION}: Specifies the region into which the cluster and node group will be deployed.
 Expected output:


************************
**** EXAMPLE OUTPUT ****
************************

2024-07-30 23:09:37 [ℹ]  eksctl version 0.183.0
2024-07-30 23:09:37 [ℹ]  using region us-west-2
2024-07-30 23:09:37 [ℹ]  setting availability zones to [us-west-2c us-west-2a us-west-2d]
2024-07-30 23:09:37 [ℹ]  subnets for us-west-2c - public:192.168.0.0/19 private:192.168.96.0/19
2024-07-30 23:09:37 [ℹ]  subnets for us-west-2a - public:192.168.32.0/19 private:192.168.128.0/19
2024-07-30 23:09:37 [ℹ]  subnets for us-west-2d - public:192.168.64.0/19 private:192.168.160.0/19
2024-07-30 23:09:37 [ℹ]  nodegroup "worknodes-1" will use "" [AmazonLinux2/1.30]
2024-07-30 23:09:37 [ℹ]  using Kubernetes version 1.30
2024-07-30 23:09:37 [ℹ]  creating EKS cluster "eks-lab-cluster" in "us-west-2" region with managed nodes
2024-07-30 23:09:37 [ℹ]  will create 2 separate CloudFormation stacks for cluster itself and the initial managed nodegroup
2024-07-30 23:09:37 [ℹ]  if you encounter any issues, check CloudFormation console or try 'eksctl utils describe-stacks --region=us-west-2 --cluster=eks-lab-cluster'
2024-07-30 23:09:37 [ℹ]  Kubernetes API endpoint access will use default of {publicAccess=true, privateAccess=false} for cluster "eks-lab-cluster" in "us-west-2"
2024-07-30 23:09:37 [ℹ]  CloudWatch logging will not be enabled for cluster "eks-lab-cluster" in "us-west-2"
2024-07-30 23:09:37 [ℹ]  you can enable it with 'eksctl utils update-cluster-logging --enable-types={SPECIFY-YOUR-LOG-TYPES-HERE (e.g. all)} --region=us-west-2 --cluster=eks-lab-cluster'
2024-07-30 23:09:37 [ℹ]  
2 sequential tasks: { create cluster control plane "eks-lab-cluster", 
    2 sequential sub-tasks: { 
        wait for control plane to become ready,
        create managed nodegroup "worknodes-1",
    } 
}
2024-07-30 23:09:37 [ℹ]  building cluster stack "eksctl-eks-lab-cluster-cluster"
2024-07-30 23:09:37 [ℹ]  deploying stack "eksctl-eks-lab-cluster-cluster"
^C
If you had allowed the new cluster to finish building, eksctl would have saved a configuration file to ~/.kube/config. This file is commonly referred to as the kubeconfig and, among other things, contains the authentication credentials used to connect to the cluster.

 Note: In the following step, you create a Kubernetes kubeconfig file to connect to the existing dev-cluster.

 Command: To create a kubeconfig file for the existing dev-cluster, enter the following command:

aws eks update-kubeconfig --region $AWS_REGION --name dev-cluster
 Expected output



************************
**** EXAMPLE OUTPUT ****
************************

Added new context arn:aws:eks:us-west-2:123456789012:cluster/dev-cluster to /home/ec2-user/.kube/config
 Command: To view the contents of the kubeconfig file, enter the following command:

cat /home/ec2-user/.kube/config
 Expected output:


************************
**** EXAMPLE OUTPUT ****
************************

apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURCVENDQWUyZ0F3SUJBZ0lJVXRwT2V5T1I3Rjh3RFFZSktvWklodmNOQVFFTEJRQXdGVEVUTUJFR0ExVUUKQXhNS2EzVmlaWEp1WlhSbGN6QWVGdzB5TkRBM016QXlNak0xTWpKYUZ3MHpOREEzTWpneU1qUXdNakphTUJVeApFekFSQmdOVkJBTVRDbXQxWW1WeWJtVjBaWE13Z2dFaU1BMEdDU3FHU0liM0RRRUJBUVVBQTRJQkR3QXdnZ0VLCkFvSUJBUUMyVHhrOUtMaFBOWk5DSG9Lb1U5Z2pHMVpvelZPdzhNbmgreUtzWXh6MXJHd2VRQzY5cll0N0FHK1AKcUJqOC9NeHVHSko4bUpqYnZDNzYwRzVXbFNlRnMyQlNRcjBPV3ZSOG00dzdZUm9JSFo4MXE1TitJVzY2STd6QwpBU0tJTE54MnJxaVd2MzFReW9IcHFjQnpzZGxpRU5UblRZdWRxTzV4U2N2Y3Q5L1dsMjBKOVVaSTNrYkxVSnlFCkQ1WDV2Z2JldFpKQVpJYWp2TnJ4Zys2VWxrajArcFJrNlJ5cEpacFJIR0hVYWI1aS96R29QUXBBN0tiL0lWWXQKQTNkSDQwSXBTUlo4R0gvcmFjV3FPWnJhc2p0cUtuMUNTcXJ3d2VwRjgwaW9vNGtRRVQwemJsT0Z0SWtBTkw5aQp4SklyaHlNV0didUlzMGRreEcyUFRMZE5SckVoQWdNQkFBR2pXVEJYTUE0R0ExVWREd0VCL3dRRUF3SUNwREFQCkJnTlZIUk1CQWY4RUJUQURBUUgvTUIwR0ExVWREZ1FXQkJReXdRNkVtRnZ6dy85YXdBd3VuM0tzUytsMzBEQVYKQmdOVkhSRUVEakFNZ2dwcmRXSmxjbTVsZEdWek1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQ3NhbmxPbTNUWApSSkFFbE9wRGNVeHNHRXlrMjhZOTVRZjh2MHFCZnVmbWJyWUtRd0JiRk1sSjQ0YmxQVjRhUDBWYitDMDhrSG95CmxINXBLVVNEWlBNWDRhUk94bW9zKzJkUUFYNGpERHVoeko0QkUxZnhmOVVXNStRd2tVSFQzZXo1aFVlbVMrU3cKT3ozSldVcjc1RHY5b2FPRUJ5d2hRTmpudnAyRnRld2lLWjFtRTlhMlBhbk5NQkRHOXh3TEhyV0UrL2hPSm45Zgp1VHhHa3REZE44TFhKZDNTRFk0dVEvSmEyN25hdGsrbWk2bFhSZ1d2NjdZTHhMWkREWVh0cEdVcnRBcSt6Mkd3Ckc5MWQyeWRlcEp3am9IeHJxVVpSYm5ySGk1SkIrRjNIdGtuek96NmxNdytRUkdKRU92STVFb2xPMmZlN2ZUdngKZjlmcHZsVnhoRWtFCi0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS0K
    server: https://F1D1BC96FD8AA6D52F383CA52F4BB311.gr7.us-west-2.eks.amazonaws.com
  name: dev-cluster.us-west-2.eksctl.io
contexts:
- context:
    cluster: dev-cluster.us-west-2.eksctl.io
    user: i-05b201f4b4e4ce01d@dev-cluster.us-west-2.eksctl.io
  name: i-05b201f4b4e4ce01d@dev-cluster.us-west-2.eksctl.io
current-context: i-05b201f4b4e4ce01d@dev-cluster.us-west-2.eksctl.io
kind: Config
preferences: {}
users:
- name: i-05b201f4b4e4ce01d@dev-cluster.us-west-2.eksctl.io
  user:
    exec:
      apiVersion: client.authentication.k8s.io/v1beta1
      args:
      - eks
      - get-token
      - --output
      - json
      - --cluster-name
      - dev-cluster
      - --region
      - us-west-2
      command: aws
      env:
      - name: AWS_STS_REGIONAL_ENDPOINTS
        value: regional
      provideClusterInfo: false
The following list explains key information contained in the kubeconfig file:

apiVersion: This field indicates the version of the Kubernetes API that the kubeconfig file is written in.
clusters: This section contains information about the Kubernetes clusters that the kubeconfig file can be used to access. In this case, there is only one cluster, eks-lab-cluster.us-west-2.eksctl.io.
certificate-authority-data: This field contains the certificate authority data for the cluster, which is used to verify the server’s certificate.
current-context: This field indicates the current context, which is the context that commands will be run against by default.
users: This section contains information about the users that can be used to authenticate to the clusters.
exec: This field contains a command to be executed to fetch user credentials. In this case, the command is aws eks get-token, which fetches a token for the specified cluster and region.
Now you should be able to connect to the cluster. Let us start by finding the cluster name.

 Command: To retrieve the cluster name, enter the following command:

eksctl get cluster --region $AWS_REGION
 Expected output:


************************
**** EXAMPLE OUTPUT ****
************************

NAME            REGION          EKSCTL CREATED
dev-cluster     us-west-2       True
eks-lab-cluster us-west-2       True
 Note: The eks-lab-cluster you started creating in the preceding steps may also appear in the output. As you continue through this lab, only use the cluster called eks-lab-cluster.

 Command: To fetch the details and verify the status of nodes running in your Kubernetes cluster, enter the following command:

kubectl get nodes
 Expected output:


************************
**** EXAMPLE OUTPUT ****
************************

NAME                                          STATUS   ROLES    AGE   VERSION
ip-10-10-108-191.us-west-2.compute.internal   Ready    <none>   21m   v1.30.0-eks-036c24b
ip-10-10-150-223.us-west-2.compute.internal   Ready    <none>   21m   v1.30.0-eks-036c24b
ip-10-10-72-255.us-west-2.compute.internal    Ready    <none>   21m   v1.30.0-eks-036c24b
 Command: To find the nodegroup associated with the cluster, enter the following command:

eksctl get nodegroup --cluster=eks-lab-cluster --region $AWS_REGION
 Expected output:


************************
**** EXAMPLE OUTPUT ****
************************

CLUSTER         NODEGROUP       STATUS  CREATED                 MIN SIZE        MAX SIZE        DESIRED CAPACITY        INSTANCE TYPE   IMAGE ID                ASG NAME                                             TYPE
eks-lab-cluster     worknodes-1      ACTIVE  2024-07-30T22:47:40Z    2               4               3                       t3.medium       AL2023_x86_64_STANDARD  eks-dev-nodes-e8c882e9-f0c6-3ff3-8bf8-8b8f28db6cff   managed
The nodegeroup is called dev-nodes and has a desired capacity of 3 nodes. For the purposes of our lab, this is more nodes than required. Let us reduce the desired node count to 2.

 Command: To reduce the desired node count to 2, enter the following command:

eksctl scale nodegroup --cluster=eks-lab-cluster --nodes=2 --name=worknodes-1 --region $AWS_REGION
 Expected output:


************************
**** EXAMPLE OUTPUT ****
************************

2024-07-30 23:11:09 [ℹ]  scaling nodegroup "dev-nodes" in cluster eks-lab-cluster
2024-07-30 23:11:10 [ℹ]  initiated scaling of nodegroup
2024-07-30 23:11:10 [ℹ]  to see the status of the scaling run `eksctl get nodegroup --cluster eks-lab-cluster --region us-west-2 --name dev-nodes`
 Command: To verify that the cluster has been updated, enter the following command:

eksctl get nodegroup --cluster eks-lab-cluster --region $AWS_REGION --name worknodes-1
 Expected output: You notice that the desired node count has been reduced to 2.


************************
**** EXAMPLE OUTPUT ****
************************

CLUSTER         NODEGROUP       STATUS  CREATED                 MIN SIZE        MAX SIZE        DESIRED CAPACITY        INSTANCE TYPE   IMAGE ID                ASG NAME                                             TYPE
eks-lab-cluster     worknodes-1      ACTIVE  2024-07-30T22:47:40Z    2               4               2                       t3.medium       AL2023_x86_64_STANDARD  eks-dev-nodes-e8c882e9-f0c6-3ff3-8bf8-8b8f28db6cff   managed
Well done! Now that you have observed how eksctl can be utilized to create and update a cluster, let us confirm that kubectl is able to communicate with resources inside the cluster.

 Command: To retrieve the cluster state, enter the following command:

kubectl cluster-info
 Expected output: The output should be similar to the following:


************************
**** EXAMPLE OUTPUT ****
************************

Kubernetes control plane is running at https://F1D1BC96FD8AA6D52F383CA52F4BB311.gr7.us-west-2.eks.amazonaws.com
CoreDNS is running at https://F1D1BC96FD8AA6D52F383CA52F4BB311.gr7.us-west-2.eks.amazonaws.com/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
The output returns two URLs. The first points to the managed cluster control plane and the second points to a DNS proxy running inside the cluster. This confirms that the cluster is up and running and that kubectl can connect to the resources inside of it.

 Task complete: You successfully installed eksctl and kubectl and confirmed that the eks-lab-cluster is ready to host your application.

Task 3: Deploying Containerized Tasks to Amazon EKS Using Imperative and Declarative Approaches
In Kubernetes, there are two main approaches to managing resources: imperative and declarative.

Imperative approach: This involves using commands that directly tell the Kubernetes API what to do. For example, using kubectl run to create a pod or deployment.

Declarative approach: This involves defining the desired state of the resources in a YAML or JSON file and applying that configuration to the Kubernetes cluster. The cluster reconciles the desired state with the current state and make the necessary changes.

In this task, you learn to deploy containerized tasks onto an Amazon EKS cluster using both the imperative and declarative approaches. You create a pod and a Kubernetes Job, both running a container image designed to check URLs. By the end of this task, you understand the differences between these two approaches and how to view the logs of running or completed containers.

Task 3.1 List available container images in Amazon ECR
 Command: To list the available container images in Amazon ECR for your account, enter the following command:

aws ecr describe-repositories --region $AWS_REGION
 Expected output: The output shows an Amazon ECR repository named url-checker containing a pre-built container image you use in this task.


************************
**** EXAMPLE OUTPUT ****
************************

{
    "repositories": [
        {
            "repositoryArn": "arn:aws:ecr:us-west-2:1234567890:repository/url-checker",
            "registryId": "042087554446",
            "repositoryName": "url-checker",
            "repositoryUri": "1234567890.dkr.ecr.us-west-2.amazonaws.com/url-checker",
            "createdAt": "2024-07-25T13:00:01.527000+00:00",
            "imageTagMutability": "MUTABLE",
            "imageScanningConfiguration": {
                "scanOnPush": false
            },
            "encryptionConfiguration": {
                "encryptionType": "AES256"
            }
        }
    ]
}
Task 3.2: Imperative Approach Using kubectl run
To create and run a new pod in Kubernetes using the imperative approach with the kubectl run command, follow these steps:

 Command: To retrieve the Amazon ECR authentication token, run the following command.

aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
 Expected output:


WARNING! Your password will be stored unencrypted in /home/ec2-user/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
 Command: To create a pod named url-checker using the url-checker image from Amazon ECR, run the following command.

 Note: It will take 1-2 minutes for the command to be executed and the output to be generated.


kubectl run url-checker  --rm -q -it  --image=$ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/url-checker:latest -- https://www.example.com https://aws.amazon.com http://invalid-url
This command creates a pod named url-checker and runs a container from the url-checker image. The – syntax is used to pass arguments to the container’s entrypoint. In this case, it runs https://www.example.com https://aws.amazon.com http://invalid-url as an argument, which checks the availability of the specified URL.

 Expected output: The output shows the results of the URL checks performed by the Job.


-----------------------  ---------------
https://www.example.com  200
https://aws.amazon.com   200
http://invalid-url       ConnectionError
-----------------------  ---------------
Task 3.3: Declarative Approach Using kubectl apply -f
 Command: To create a new Job in Kubernetes using a declarative approach by applying a YAML file with the kubectl apply -f command, enter the following:

cat <<EOF > job.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: url-checker
spec:
  template:
    spec:
      containers:
      - name: url-checker
        image: $ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/url-checker:latest
        command: ["python", "/app/url_checker.py", "https://www.example.com", "https://aws.amazon.com", "http://invalid-url"]
      restartPolicy: Never
EOF

kubectl apply -f job.yaml
This creates a YAML file job.yaml that defines a Job named url-checker with a pod running the url-checker container image from Amazon ECR. The command field in the YAML file specifies the entrypoint to run when the container starts, which is a Python script that checks the provided URLs.

The restartPolicy: Never tells Kubernetes not to restart the pod if it exits successfully.

 Note: By using kubectl apply -f, you are instructing Kubernetes to create or update the Job resource based on the declarative configuration defined in the job.yaml file. This is considered a declarative approach because you are defining the desired state of the resource, and Kubernetes takes care of reconciling the actual state with the desired state.

The declarative approach is generally preferred over the imperative approach because it provides a more consistent and repeatable way of managing Kubernetes resources. It also makes it easier to version control and manage the resource configurations.

 Expected output:


job.batch/url-checker created
 **Command:**To fetch the details and status of the Job, enter the following command:

kubectl get jobs
 Expected output: The output shows the Job has completed successfully (1/1 COMPLETIONS).


NAME          COMPLETIONS   DURATION   AGE
url-checker   1/1           10s        18s
 Command: To view the logs of the completed Job, enter the following command:

kubectl logs job/url-checker
 Expected output: The output shows the results of the URL checks performed by the Job.


-----------------------  ---------------
https://www.example.com  200
https://aws.amazon.com   200
http://invalid-url       ConnectionError
-----------------------  ---------------
 Command: To delete the Job running in your Kubernetes cluster, enter the following command:

kubectl delete job url-checker
 Expected output:


job.batch "url-checker" deleted
 Task complete: You successfully demonstrated how kubectl run (imperative approach) and kubectl apply -f (declarative approach) can be used to deploy containerized tasks onto the Kubernetes cluster. You also learned how to view the logs of running or completed containers using kubectl logs.

Conclusion
You have successfully done the following:

Installed and configured command line utilities for Amazon EKS.
Created and configured an Amazon EKS cluster and node group.
Deployed containerized applications from Amazon ECR to your Amazon EKS cluster using AWS Code Editor.
Created pods on the Kubernetes cluster using kubectl run (imperative approach).
Created pods on the Kubernetes cluster using kubectl apply -f (declarative approach).
Viewed logs of running pods on the Kubernetes cluster using kubectl logs.

### Additional resources

* [Set up kubectl and eksctl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html)
* [Set up to use Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html)
* [Simplify node lifecycle with managed node groups](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html)
* [Amazon EKS networking](https://docs.aws.amazon.com/eks/latest/userguide/eks-networking.html)

### End lab

Follow these steps to close the console and end your lab.

28. Return to the **AWS Management Console**.
29. At the upper-right corner of the page, choose **AWSLabsUser**, and then choose Sign out.
30. Choose **End Lab** and then confirm that you want to end your lab.
