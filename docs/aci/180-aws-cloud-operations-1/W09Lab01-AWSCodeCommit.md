# Working with AWS CodeCommit

## Lab overview

AWS CodeCommit is a highly scalable, managed source control service that hosts private Git repositories. CodeCommit stores your data in Amazon Simple Storage Service (Amazon S3) and Amazon DynamoDB, giving your repositories high scalability, availability, and durability. You create a repository to store your code. There is no hardware to provision and scale or software to install, configure, and operate.

In this lab, you first create a code repository in AWS CodeCommit. Then you create a local repository on a Linux instance running in Amazon Elastic Compute Cloud (Amazon EC2). After you create the local repo, you make changes to it and synchronize (commit) your changes to the CodeCommit repository.

Objectives
By the end of this lab, you will be able to do the following:

Create a code repository by using the AWS CodeCommit console.
Create a local code repository on the Linux instance by using Git.
Synchronize a local repository with a CodeCommit repository.
Prerequisites
To complete this lab, you should have some development experience and understand the principles of source code repositories. You should be comfortable with making Secure Shell (SSH) connections to instances running in Amazon EC2 and using Linux commands and editors from the command line in Linux.

Duration
This lab requires 45 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Command: A command that you must run
 Expected output: A sample output that you can use to verify the output of a command or edited file
 Note: A hint, tip, or important guidance
 Additional information: Where to find more information
 CAUTION: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but that could result in the need to repeat certain steps)
 WARNING: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made)
 Congratulations! You have successfully completed a task
Start lab
To launch the lab, at the top of the page, choose Start lab.
 Caution: You must wait for the provisioned AWS services to be ready before you can continue.

To open the lab, choose Open Console.
You are automatically signed in to the AWS Management Console in a new web browser tab.

 WARNING: Do not change the Region unless instructed.

Common sign-in errors
Error: You must first sign out


If you see the message, You must first log out before logging into a different AWS account:

Choose the click here link.
Close your Amazon Web Services Sign In web browser tab and return to your initial lab page.
Choose Open Console again.
Error: Choosing Start Lab has no effect
In some cases, certain pop-up or script blocker web browser extensions might prevent the Start Lab button from working as intended. If you experience an issue starting the lab:

Add the lab domain name to your pop-up or script blocker’s allow list or turn it off.
Refresh the page and try again.
Task 1: Creating a CodeCommit repository
In this task, you use the console to create an AWS CodeCommit repository.

On AWS Management Console, in the search box, search for and choose CodeCommit.

On the AWS CodeCommit page, choose Create repository.

On the Create repository page, configure the following settings:

For Repository name, enter My-First-Repo.
For Description, enter My first repository.
Choose Create.
An empty repository named My-First-Repo is created.

You should now be on the My-First-Repo page, which contains the details to connect to the repository.

 Congratulations! You have successfully created a new CodeCommit repository.

Copy the Ec2InstanceSessionUrl value from the list to the left of these instructions, and paste it into a new web browser tab. It should display an example similar to this:

cd HOME; pwd; bash
sh-4.2$ cd HOME; bash; pwd
/home/ec2-user
[ec2-user@ip-10-0-1-137 ~]$
Task 2: Using Git to create a local repository
This task provides an example of how you would use CodeCommit to synchronize to any local code repository that you might create in your normal production development environment.

 Command: In the terminal session, to install the Git client, run the following command:

sudo yum install -y git
 Note: On a Windows-based computer, you might need to press Ctrl + Shift + V or open the context menu (right-click) to paste text into the terminal window Session Manager, a capability of AWS Systems Manager.

 Command: Run the following commands to configure the Git credential helper with the AWS credential profile and allow the Git credential helper to send the path to repositories:

git config --global credential.helper '!aws codecommit credential-helper $@'
git config --global credential.UseHttpPath true
git config --global init.defaultBranch main
 Expected output: These commands have no output.

Next, obtain the HTTPS URL of your AWS CodeCommit repository.

Return to your web browser tab with the AWS CodeCommit console, which should be on the My-First-Repo page.

In the upper right of the page, choose Clone URL , and then choose Clone HTTPS.

The repository URL is copied to your clipboard and should look similar to this: https://git-codecommit.us-east-1.amazonaws.com/v1/repos/My-First-Repo.

 Copy edit: Paste the copied URL into a text editor.

Copy and paste the following command into your text editor:


git clone CLONE_HTTPS_URL
Replace the CLONE_HTTPS_URL placeholder value with the Clone HTTPS URL that you copied previously.

 Command: Return to your web browser tab with the terminal session, and run the updated command to clone the My-First-Repo repository to the instance.

 Expected output: The output should be similar to this, indicating that you are cloning the My-First-Repo repository, and that the repository is empty:


Cloning into 'My-First-Repo'...
warning: You appear to have cloned an empty repository.
 Congratulations! You have successfully connected to and synchronized with the CodeCommit repository.

Next, you conclude with a short demonstration of making a change and synchronizing the repositories. This is a mini example of the workflow of synchronizing code changes during the development process.

Task 3: Making a code change and first commit to the repo
In this task, you create your first commit in your local repo. You create two example files in your local repo, use Git to stage the changes to your local repo, and then commit the changes.

 Command: To change to the My-First-Repo directory, run the following command:

cd ~/My-First-Repo
 Command: To create two files in your local repo, run the following command:

echo "The domestic cat (Felis catus or Felis silvestris catus) is a small, usually furry, domesticated, and carnivorous mammal." >cat.txt
echo "The domestic dog (Canis lupus familiaris) is a canid that is known as man's best friend." >dog.txt
 Expected output: These commands have no output.

 Command: To list the files in the current directory, run the following command:

ls
 Expected output: The output should show the two files you created, similar to this:


cat.txt  dog.txt
 Command: To stage the changes in your local repo, run the following command:

git add cat.txt dog.txt
 Expected output: This command has no output.

 Command: To view the status of your repo, run the following command:

git status
 Expected output: The output should show the branch that you are current working in (main) and that the two files are ready to be committed to the repository, similar to this:


On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   cat.txt
        new file:   dog.txt
 Command: To commit the changes in your local repo, run the following command:

git commit -m "Added cat.txt and dog.txt"
 Expected output: The output displays a message stating that the name and email address of the committer were configured automatically. In a production environment, you would use the commands listed to set your name and email address, which are then applied to each commit you do. The output also shows that two files were changed and inserted, similar to this:


Committer: EC2 Default User <ec2-user@ip-10-1-12-142.ec2.internal>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 2 files changed, 2 insertions(+)
 create mode 100644 cat.txt
 create mode 100644 dog.txt
 Command: To view details about the commit that you just made, run the following command:

git log
 Expected output: The output should be similar to this. It shows that there is one commit to the main branch. It also shows the name of the author, the date that the commit was made, and the files that were added:


commit 772d16037b2e0d7ee7e97aa9218e571346bebe0e (HEAD -> main)
Author: EC2 Default User <ec2-user@ip-10-1-12-142.ec2.internal>
Date:   Wed Jul 20 19:20:06 2022 +0000

    Added cat.txt and dog.txt
Now that you have an initial commit in your local repo, you can push the commit from your local repo to your CodeCommit repository.

 Congratulations! You have successfully added files to a local repository.

Task 4: Pushing your first commit
In this task, you push the commit from your local repo to your CodeCommit repository.

 Command: To push your commit through the default remote name that Git uses for your CodeCommit repository (origin) from the default branch in your local repo (main), run the following command:

git push -u origin main
 Expected output: The output displays the details of the process to create the branch and push the files to the remote repository, similar to this:


Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 2 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 447 bytes | 447.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
To https://git-codecommit.us-east-1.amazonaws.com/v1/repos/My-First-Repo
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
After you have pushed code to your CodeCommit repository, you can view the contents on the AWS CodeCommit console.

Return to your web browser tab with the CodeCommit console, which should be on the My-First-Repo page.

Choose your web browser’s refresh button to refresh the page.

The two files that you added to your repository should be displayed.

Choose the link for each file to view its contents.
 Congratulations! You have successfully pushed the changes from your local repository to the remote CodeCommit repository.

Conclusion
Congratulations! You now have successfully done the following:

Created a code repository by using the AWS CodeCommit console
Created a local code repository on the Linux instance by using Git
Synchronized a local repository with a CodeCommit repository
Consider how to bring the AWS CodeCommit features and capabilities to your development workflow, including the following:

Collaboration: AWS CodeCommit is designed for collaborative software development. With CodeCommit, you can commit, diff, and merge your code to help you maintain control of your team’s projects. You can create a repository from the AWS Management Console, AWS Command Line Interface (AWS CLI), or AWS SDKs and start working with the repository by using Git.
Encryption: You can transfer your files to and from CodeCommit by HTTPS and SSH. Your repositories are also automatically encrypted at rest through AWS Key Management Service (AWS KMS) using customer-specific keys.
Access control: CodeCommit uses AWS Identity and Access Management (IAM) to control and monitor who can access your data as well as how, when, and where they can access it.
High availability and durability: CodeCommit stores your repositories in Amazon S3 and DynamoDB. Your data is redundantly stored across multiple facilities. This architecture increases the availability and durability of your repository data.
Unlimited repositories: With CodeCommit, you can create as many repositories as you need, with no size limits. You can store and version any kind of file alongside your code, including application assets such as images and libraries.
Easy access and integration: You can use the console, AWS CLI, and AWS SDKs to manage your repositories. You can also use Git commands or Git graphical tools to interact with your repository source files. CodeCommit supports all Git commands and works with your existing Git tools. You can integrate with your development environment plugins or continuous integration and continuous delivery (CI/CD) systems.
Additional resources
For more information about AWS CodeCommit, see AWS CodeCommit.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.