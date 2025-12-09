# Using Dockerfile with Amazon ECR

* back to AWS Cloud Institute repo's root [aci.md](../../aci.md)
* back to [AWS Cloud Fundamentals 2](../aws-cloud-fundamentals-2.md)
* back to repo's main [README.md](../../../../README.md)

## Lab overview

In this hands-on lab, you learn how to deploy a Docker container on an Amazon Elastic Compute Cloud (Amazon EC2) instance and push the container image to Amazon Elastic Container Registry (Amazon ECR). You follow a step-by-step guide to install Docker, create an Amazon ECR repository, build a Docker image from source code, and push the image to the Amazon ECR repository. Additionally, you gain experience in deploying the same Docker image across multiple Amazon EC2 instances, enabling consistent and repeatable application deployments.

Objectives
By the end of this lab, you will be able to:

Establish secure connections to Amazon EC2 instances using AWS Systems Manager Session Manager.
Configure the AWS environment and run a sample URL Checker application.
Create an Amazon Elastic Container Registry (Amazon ECR) repository.
Install Docker on an Amazon EC2 instance.
Build a Docker image from provided source code.
Push the Docker image to the Amazon ECR repository.
Deploy the Docker image on a separate Amazon EC2 instance, demonstrating consistent application deployment across multiple instances.
Technical knowledge prerequisites
Basic understanding of Amazon Web Services (AWS) and its core services, such as Amazon EC2, Amazon ECR, and CloudFormation.

Familiarity with Docker and containerization concepts, including building Docker images and pushing them to a registry.

Hands-on experience with the AWS Command Line Interface (CLI) and executing commands in a terminal environment.

Knowledge of Linux operating systems and basic command-line operations, as the lab involves working with an Amazon Linux EC2 instance.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Caution: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Command: A command that you must run.
 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Note: A hint, tip, or important guidance.
 Task complete: A conclusion or summary point in the lab.
 WARNING: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made).
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
Services used in this lab
Amazon Elastic Compute Cloud (Amazon EC2)
Amazon Elastic Compute Cloud (Amazon EC2) is a core service offered by Amazon Web Services (AWS) that provides scalable computing capacity in the cloud. Amazon EC2 allows users to launch and manage virtual servers, known as instances, with various configurations of CPU, memory, storage, and networking resources. Amazon EC2 instances are highly customizable and can be provisioned with different operating systems such as Amazon Linux, Ubuntu, Windows Server, and more. These instances can be used for a wide range of workloads, including web applications, databases, batch processing, and even machine learning or high-performance computing tasks.

Amazon Elastic Container Registry (Amazon ECR)
Amazon Elastic Container Registry (Amazon ECR) is a fully-managed Docker container registry service provided by Amazon Web Services (AWS). It allows users to store, manage, and deploy Docker container images securely and efficiently within the AWS ecosystem. Amazon ECR integrates seamlessly with other AWS services, such as Elastic Compute Cloud (Amazon EC2), Elastic Kubernetes Service (EKS), and Elastic Container Service (ECS), making it easier to build, deploy, and manage containerized applications on AWS infrastructure. It provides features like resource-based permissions, image vulnerability scanning, and lifecycle policies for managing images.

Task 1: Connect to the Amazon EC2 Instance using AWS Systems Manager Session Manager
In this task, you establish a secure connection to the pre-provisioned Amazon Elastic Compute Cloud (Amazon EC2) instance using the AWS Systems Manager Session Manager. This service provides an interactive browser-based shell and allows connecting to your Amazon EC2 instance without the need for an open inbound port or a bastion host.

At the top of the AWS Management Console, in the search bar, search for and choose EC2.

In the navigation pane, select Instances.

Select EC2 Instance.

Choose Connect from the top right of the page.

You are directed to the Connect to instance page and the Session Manager tab is highlighted.

Choose Connect.

A new browser window or tab opens with a connection window. This window provides an interactive shell session directly to the selected Amazon EC2 instance. You now have an interactive shell environment within the connected Amazon EC2 instance. You can run commands, navigate directories, view and edit files, and perform any other tasks as if you are directly logged into the instance through SSH.

The output appears similar to the following:


cd $HOME; pwd
sh-5.2$ cd $HOME; pwd
/home/ssm-user
sh-5.2$
 Task complete: In this task, you successfully established a secure connection to an Amazon EC2 instance using the AWS Systems Manager Session Manager.

Task 2: Configure AWS Environment and Run the URL Checker Application
In this task, you configure the AWS environment on the Amazon EC2 instance and run the URL Checker application. You retrieve the AWS account ID and region information, install the required Python dependencies, and then run the URL Checker application to test the functionality.

 Command: Retrieve the AWS account ID and region information by running the following commands in the terminal window.


TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
export AWS_REGION=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/dynamic/instance-identity/document | jq -r '.region')
ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)
echo "Your AWS Account ID is $ACCOUNT_ID and you are working in the $AWS_REGION region."
 Expected output:


******************************
**** SAMPLE OUTPUT ****
******************************

Your AWS Account ID is 111111111111 and you are working in the us-west-2 region.
 Command: Navigate to the directory containing the application source code and list the contents of the directory by running the following command.


cd /tmp/temp
ls -al
 Expected output:


total 12
drwxr-xr-x.  2 root root 100 Jul 12 21:26 .
drwxrwxrwt. 12 root root 240 Jul 12 21:51 ..
-rwxr-xr-x.  1 root root 161 Jan 10  2024 Dockerfile
-rwxr-xr-x.  1 root root  17 Jan 10  2024 requirements.txt
-rwxr-xr-x.  1 root root 435 Jan 10  2024 url_checker.py
These files are essential for building the Docker image because:

The Dockerfile provides the instructions for Docker to create the image layer by layer, starting from the base image and adding the application code and dependencies.

The requirements.txt file allows Docker to install the necessary Python packages and dependencies required by the application.

The url_checker.py file contains the actual application code that executes when the Docker container runs.

In the next task of building the Docker image, these files are referenced and used by the docker build command to construct the image with the application and its dependencies.

 Command: Run the URL Checker application with the following command.


python3 url_checker.py https://www.example.com https://aws.amazon.com http://invalid-url
 Expected output: This checks the availability of the provided URLs and displays the results in a tabular format.


-----------------------  ---------------
https://www.example.com  200
https://aws.amazon.com   200
http://invalid-url       ConnectionError
-----------------------  ---------------
 Task complete: In this task, you successfully configured the AWS environment by retrieving the account ID and region information and ran the URL Checker application to test the functionality of checking the availability of specified URLs.

Task 3: Install Docker on the Amazon EC2 Instance
In this task, you install Docker using the package manager on the Amazon Elastic Compute Cloud (Amazon EC2) instance. Docker is an open-source platform that allows the learner to build, deploy, and run applications inside containers.

 Command: To install Docker, run the following command.


sudo dnf install docker -y
 Expected output:


******************************
**** SAMPLE OUTPUT ****
******************************
Last metadata expiration check performed X minutes ago on ...
Dependencies resolved.
================================================================================
 Package             Arch              Version                  Repository     Size
================================================================================
Installing:
 docker              x86_64            <version>                <repo>        <size>
Transaction Summary
================================================================================
Install  1 Package
Total download size: <size>
Installed size: <size>
...
Complete!
 Command: To start the Docker service, run the following command.


sudo systemctl start docker
 Expected output:

None unless there is an error

 Command: To verify the Docker service status, run the following command.


systemctl status docker.service
 Expected output:


******************************
**** SAMPLE OUTPUT ****
******************************
● docker.service - Docker Application Container Engine
     Loaded: loaded (/usr/lib/systemd/system/docker.service; disabled; preset: disabled)
     Active: active (running) since ...
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
    Process: 26423 ExecStartPre=/bin/mkdir -p /run/docker(code=exited, status=0/SUCCESS)
    Process: 26424 ExecStartPre=/usr/libexec/docker/ docker-setup-runtimes.sh (code=exited, status=0/SUCCESS)
   Main PID: 26425 (dockerd)
      Tasks: 8
     Memory: 32.9M
        CPU: 357ms
     CGroup: /system.slice/docker.service
             └─26425 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock --default-ulimit nofile=32768:65536
 Task complete: You have successfully installed Docker on your Amazon EC2 instance and verified that the Docker service is running.

Task 4: Build the Docker image
In this task, you build a Docker image using the provided application code and Dockerfile. This Docker image packages the URL Checker application and its dependencies, making it easy to deploy and run the application in any environment that supports Docker containers.

 Command: Build the Docker image with the following command.


sudo docker build -t url-checker .
 Expected output: Output has been truncated.


******************************
**** SAMPLE OUTPUT ****
******************************

+] Building 8.2s (9/9) FINISHED

 => [3/4] WORKDIR / app                                                                                                                                                                                             0.0s
 => [4/4] RUN pip install -r /app/requirements. txt                                                                                                                                                              4.7s
 => exporting to    image                                                                                                                                                                                             0.2s
 => => exporting    layers                                                                                                                                                                                            0.2s
 => => writing image    sha256:c992ace657c9a279743693d76a19e73fd8d842a39a8bd23af3b34789769de863                                                                                                                       0.0s
 => => naming to docker.io/library/url-checker
 Command: To run the Docker container and pass the URLs to check with the url_checker application run the following command.


sudo docker run url-checker https://www.example.com https://aws.amazon.com http://invalid-url
 Expected output: This checks the availability of the provided URLs and display the results in a tabular format.


-----------------------  ---------------
https://www.example.com  200
https://aws.amazon.com   200
http://invalid-url       ConnectionError
-----------------------  ---------------
 Task complete: You have successfully built a Docker image containing the URL Checker application. This image can now be pushed to a container registry, such as Amazon Elastic Container Registry (Amazon ECR), and deployed to various environments for running the URL Checker application within Docker containers.

Task 5: Create an Amazon Amazon ECR Repository
In this task, you create an Amazon Elastic Container Registry (Amazon ECR) repository from the AWS Management Console to store your Docker container image.

At the top of the AWS Management Console, in the search bar, search for ECR and choose Elastic Container Registry.

From the left navigation pane, Private registry, choose Repositories.

Choose Create repository.

In the Create repository page, enter url-checker as the Repository name.

Leave the other settings as default, and choose Create at the bottom of the page.

The url-checker repository is created, and you are redirected to the repository details page.

In the following task, you build and push a Docker image to the repository created.

 Task complete: You have successfully created an Amazon ECR repository named url-checker from the AWS Management Console.

Task 6: Push the Docker image to Amazon ECR
In this task, you leverage the View Push Commands feature provided by Amazon Elastic Container Registry (Amazon ECR) to authenticate your Docker client, tag the Docker image with the Amazon ECR repository URI, and push the image to the Amazon ECR repository.

The View Push Commands feature is a convenient way to obtain pre-configured commands tailored to your specific repository and AWS environment. These commands streamline the process of authenticating your Docker client, building (if needed), tagging, and pushing your Docker image to the Amazon ECR repository.

 Caution: For the purposes of this lab, the commands obtained from the View Push Commands feature have been customized to incorporate dynamically populated values for the AWS_REGION and ACCOUNT_ID variables, as well as the inclusion of sudo to run the commands with elevated privileges within the lab environment. This customization ensures that the commands are correctly parameterized and executed with the required permissions, regardless of the specific AWS region or account ID assigned to you.

Follow these steps to push the Docker image to the Amazon ECR repository:

Open the url-checker repository by selecting the link.

You notice that there is no image available in the repository yet.

Choose View push commands.

A new window opens, displaying the push commands specific to your Amazon ECR repository.

 Note: The customized commands that follow are to be run in the terminal window of the Amazon EC2 instance.

Return to the browser tab opened to the Systems Manager session.

 Command: Authenticate with the Amazon ECR registry by running the following customized command.


sudo /usr/local/bin/aws ecr get-login-password --region ${AWS_REGION} | sudo docker login --username AWS --password-stdin ${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com
 Expected output:


WARNING! Your password will be stored unencrypted in /home/<user>/. docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/ #credentials-store
Login Succeeded
 Command: Tag the Docker image with the Amazon ECR repository URI by running the following customized command.


sudo docker tag url-checker:latest ${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/url-checker:latest
 Expected output:

None unless there is an error.

 Command: Push the Docker image to the Amazon ECR repository by running the following customized command.


sudo docker push ${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/url-checker:latest
 Expected output:


******************************
**** EXAMPLE OUTPUT ****
******************************

The push refers to repository [398349607143.dkr.ecr.us-west-2.amazonaws.com/url-checker]
694f47d02bbc: Pushed
5f70bf18a086: Pushed
85620a0ec6fc: Pushed
01121891541e: Pushed
878749ddc18e: Pushed
77862ab393ed: Pushed
eb869c3937a7: Pushed
63ca1fbb43ae: Pushed
latest: digest: sha256:c5561371e39979419d081940c6491ddabb56eac46c7d2ad57d8956a9692a2afa size: 1992
Verify that the Docker image has been successfully pushed to the Amazon ECR repository by refreshing the repository details in the AWS Management Console. You notice that an image with the tag latest is now available.

 Task complete: You have successfully built a Docker image, tagged it with the Amazon ECR repository URI, and pushed the image to the Amazon ECR repository using the customized commands obtained from the View Push Commands feature.

Tasks 6 and 7 guides you through pulling the Docker image from Amazon ECR and running the containerized application on a separate Amazon EC2 instance. This is a common scenario in real-world environments, enabling scalability, high availability, and load balancing. You gain practical experience in deploying containerized applications consistently across multiple instances, simplifying application distribution, updates, and maintenance.

Task 7: Connect to the TestEC2 Instance using AWS Systems Manager Session Manager
In this task, you establish a secure connection to a pre-provisioned Amazon EC2 instance, known as the TestEC2 Instance, using the AWS Systems Manager Session Manager. This prepares you for the next step, where you pull the Docker image from the Amazon ECR repository and run the containerized application on this separate instance. Consistent deployment across multiple instances is a crucial aspect of working with containerized applications in production environments.

At the top of the AWS Management Console, in the search bar, search for and choose EC2.

In the navigation pane, select Instances.

Un-select EC2 Instance.

Select TestEC2 Instance.

Choose Connect from the top right of the page.

You are directed to the Connect to instance page and the Session Manager tab is highlighted.

Choose Connect.

A new browser window or tab opens with a connection window. This window provides an interactive shell session directly to the selected Amazon EC2 instance. You now have an interactive shell environment within the connected Amazon EC2 instance. You can run commands, navigate directories, view and edit files, and perform any other tasks as if you were directly logged into the instance through SSH.

The output appears similar to the following snippet.


cd $HOME; pwd
sh-5.2$ cd $HOME; pwd
/home/ssm-user
sh-5.2$
 Task complete: In this task, you successfully established a secure connection to the TestEC2 instance using the AWS Systems Manager Session Manager.

Task 8: Deploy the Docker Image on a Separate Amazon EC2 Instance
In this task, you pull the Docker image that you pushed to the Amazon ECR repository onto the TestEC2 Instance. This demonstrates how to deploy the same Docker image across multiple Amazon EC2 instances, enabling consistent and repeatable application deployments. By leveraging Amazon ECR, you can ensure that the same application version runs on different instances, contributing to scalability and reliability.

 Command: Retrieve the AWS account ID and region information by running the following commands.


TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
export AWS_REGION=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/dynamic/instance-identity/document | jq -r '.region')
ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)
echo "Your AWS Account ID is $ACCOUNT_ID and you are working in the $AWS_REGION region."
 Expected output:


******************************
**** SAMPLE OUTPUT ****
******************************
Your AWS Account ID is 111111111111 and you are working in the us-west-2 region.
 Command: Authenticate with the Amazon ECR registry by running the following command.


sudo /usr/local/bin/aws ecr get-login-password --region ${AWS_REGION} | sudo docker login --username AWS --password-stdin ${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com
 Expected output:


******************************
**** SAMPLE OUTPUT ****
******************************
WARNING! Your password will be stored unencrypted in /home/<user>/.docker/  config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store
Login Succeeded
 Command: Retrieve the Docker image URI from Amazon ECR by running the following command.


aws ecr describe-repositories --repository-names url-checker --query 'repositories[0].repositoryUri' --output text
 Expected output:


******************************
**** SAMPLE OUTPUT ****
******************************
111111111111.dkr.ecr.us-west-2.amazonaws.com/url-checker
Copy the value of the URI field from the repository details in a text editor of your choice. This URI is used to reference the Docker image in the following steps.

 Command: Pull the Docker image from ECR to the TestEC2 instance by running the following command, replacing <image-uri> with the URI you copied from the Amazon ECR repository details:


sudo docker pull <image-uri>:latest
 Expected output:


******************************
**** SAMPLE OUTPUT ****
******************************
latest: Pulling from url-checker
ec99f8b99825: Pull complete
a0aab5935990: Pull complete
0017c34ace6c: Pull complete
704141445f22: Pull complete
7d353c5632ce: Pull complete
a5863513b209: Pull complete
4f4fb700ef54: Pull complete
33880510b3c6: Pull complete
Digest:  sha256:d07b4a0a0362dee6998e7bcd0239296440245d54bb53a5bc8d02506fd38e9d53
Status: Downloaded newer image for 111111111111.dkr.ecr.us-west-2.amazonaws.com/  url-checker:latest
111111111111.dkr.ecr.us-west-2.amazonaws.com/url-checker:latest
 Command: Run the url-checker application by executing the following command, replacing the <image-uri> with the URI you copied from the Amazon ECR repository details:


sudo docker run <image-uri>:latest https://www.example.com https://aws.amazon.com http://invalid-url
 Expected output: This checks the availability of the provided URLs and display the results in a tabular format.


-----------------------  ---------------
https://www.example.com  200
https://aws.amazon.com   200
http://invalid-url       ConnectionError
-----------------------  ---------------
 Task complete: You have successfully pulled the Docker image containing the url-checker application from the Amazon ECR repository onto a separate Amazon EC2 instance. This exercise showcased how you can consistently deploy the same Docker image across multiple instances, enabling scalability, high availability, and reliable application deployments.

### Conclusion

You have successfully:

* Connected to Amazon EC2 instances using AWS Systems Manager Session Manager (SSM).
* Configured the AWS environment and ran the URL Checker application.
* Created an Amazon Elastic Container Registry (Amazon ECR) repository.
* Installed Docker on an Amazon EC2 instance.
* Built a Docker image from provided source code.
* Pushed the Docker image to the Amazon ECR repository.
* Deployed the Docker image on a separate Amazon EC2 instance, demonstrating consistent application deployment across multiple instances.

### End lab

Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.

Python is property of the Python Software Foundation (PSF). Reference in this lab to any specific commercial product, process, or service, or the use of any trade, firm or corporation name is provided for informational purposes, and does not constitute endorsement, recommendation, or favoring by Amazon Web Services.
