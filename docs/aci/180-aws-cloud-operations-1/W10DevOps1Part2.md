# DevOps 1 Part 2

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## Transferring Code from One Repository to the Other

### Pre-assessment

#### Which action retrieves new code changes from a remote repository to a local repository? 

* Pull

Wrong answers:

* Push
* Clone
* Commit

Pull is the action that retrieves changes from a remote repository to a local repository.

Push sends changes from a local repository to remote. Cloning makes a copy of a remote repository locally. Commit is the action of saving changes to a local repository.

#### What does the git add command do?

* Stages changes for the next commit

Wrong answers:

* Commits changes to a repository
* Renames files in a repository
* Creates a new branch

The git add command is used to stage changes for the next commit.

Use the git commit command for committing changes to a repository. git mv can be used to rename files. A new branch is created with the git branch command.

#### Which AWS service can be used to host private Git repositories securely?

* AWS CodeCommit

Wrong answers:

* AWS CodeBuild
* Amazon Simple Storage Service (Amazon S3)
* AWS Lambda

AWS CodeCommit is a fully managed source-control service that is used to host secure and scalable Git repositories.

AWS CodeBuild can be used to compile, test, and package code. AWS CodeBuild doesn’t host Git repositories. While Amazon S3 is a storage service, it is not designed specifically for hosting Git repositories. AWS Lambda is a serverless computing service for running code in response to events.

### Git and AWS CodeCommit review

Git is a distributed version control system that you can use to manage source code throughout the software development process. With Git, multiple developers can work on a project at the same time. Git operates locally on a developer’s computer, and developers can commit changes, create branches, and track the project’s history independently.

AWS CodeCommit is an online code versioning system you can use to host private Git repositories securely. CodeCommit is designed to seamlessly integrate with other AWS services. It supports standard Git commands and workflows, and developers can use CodeCommit to clone repositories, create branches, commit changes, and merge code.

#### git pull

**git pull** is fetching and merging changes from a remote repository into the local repository to ensure synchronization.

It combines:

* **git fetch**
* **git merge**

#### git push

**git push** involves sending local commits to a remote repository, which updates the central repository with the changes made locally.

### Pulling and Pushing Code

### Demo: Pull code and push back into AWS CodeCommit

In this demo, the Windows environment is used. Let’s simulate your team member by having Git create a directory separate from the existing one you use as the main user.

Switch to the **c:\temp** directory.

Run the **git clone** command to pull down a copy of the repository into the new directory. The name of the CodeCommit repo is MyFirstRepo, and you are using the HTTPS method to connect to this remote repo. And you use the following command:

```
git clone https://git-codecommit.us-east- 2.amazonaws.com/v1/repos/MyFirstRepo shared-demo-repo
```

In this command, when you add a name after the HTTPS URL, you create a directory name called **shared-demo-repo**. Switch to the **shared-demo-repo directory**.

Run the **git config** command to add the team member’s user name and email address. This makes it more convenient to identify the commits the other user makes.

```
git config --local user.name "TeamMember"
git config --local user.email teammember@example.com
```

Now, let’s make some changes to this **shared-demo-repo**. A file named **hello.txt** is added in the **shared-demo-repo** directory.

Run the following **git add** command to stage the change to the **shared-demo-repo**:

```
git add hello.txt
```

Run the **git commit -m** command to commit the change to the **shared-demo-repo**. The **-m** option adds a log message describing the change in this commit. The following log message helps with collaboration in a coding project:

```
git commit -m "Team member added hello.txt"
```

After you run the command, you should see an output with a unique ID with the log description specified after the -m option. This unique ID is called a commit ID. A commit ID is automatically assigned to commits whenever a new commit is made to the repository. You can use this commit ID when you merge commits or check files from different commits.

Run the **git push** command to push your commit to the default remote CodeCommit repository from the default branch in your local **shared-demo-repo**.

```
git push -u origin main
```

**origin** is the shorthand name of the URL for the remote repository, and **main** is the name of the default branch in the local **shared-demo-repo**. The output displays the details of the process to push the file to the remote repository. If you see writing objects: **100%, done**, it means that you have pushed your commit successfully.

Now, let’s switch back to your main user repo to see which changes your team member made. You can run the **git pull** command to pull the commit that the **shared-demo-repo** made to the CodeCommit repository into your main user repo. Then, run the git log command to see the commit that was initiated from the shared-demo-repo.

You can see the changes made by the **Author: TeamMember** and the corresponding log message. This indicates that the change was pulled down successfully.

### Using Branching

#### git fetch

Use the git fetch command to retrieve the latest changes from a remote repository without merging them into your local repository. You can stay up to date with the remote repository and still review changes before integrating them. To merge the fetched changes into your local branch, use git merge after fetching. In the following example, you fetch updates from the default remote repository called origin.

```
git fetch origin
```

#### git branch

With branches, you can develop features that are isolated from each other. Branching helps software development teams work in parallel.

To list existing branches, use the **git branch** command.

To create a new branch, use the **git branch** command followed by the new branch name. For example, the following command creates a new branch called **new-feature**.

```
git branch new-feature
```

#### git status

Use the **git status** command to review the current state of your repository and staging area. You can see which files have changed, which are staged for commit, and so on. This is helpful to stay informed about the state of your repository and manage changes.

#### Demo: Pull code and push code with branching

If you need to work on a new feature and would like to separate your work in a new version, the best way is to create a branch in AWS CodeCommit. Let’s create a branch in your local main user repo, make a few changes, and then push the branch to your CodeCommit repository. Afterwards, your team member will check out this new branch that you created. Let’s get started.

First, you create the branch and then point it to the first commit you made. To find the first commit ID, you can run the git log command. Make sure the commit has your username and email address, not the username and email address of the other simulated team member. In this example, commit **fbd744...** is the ID of the first commit.

From your local main user repo, run **git checkout -b** command. This command creates a new branch with the name you provide after the **-b** flag. Let’s specify **MyNewBranch** as the name of the branch and the ID of the first commit you made in the local main user repo.

This is to simulate that **mai**n is a stable version of the CodeCommit repository and the **MyNewBranch** branch is for a new, relatively unstable feature. The command you will run is similar to the following:

```
git checkout -b MyNewBranch commit-ID
```

Run the following **git push** command to send the new branch from the local repo to the CodeCommit repository:

```
git push origin MyNewBranch
```

Now, your simulated team member wants to pull this new branch into the shared-demo-repo and check the results.

Switch to the directory that is named **shared-demo-repo**.

Now, as a simulated team member, you want to pull in the new branch and see which new feature the other developer is working on. You can do so by using the following command:

```
git fetch origin
```

You want to confirm that the branch has been pulled in. You can use the following command to display a list of all branches for the repository:

```
git branch --all
```

Now, you can use the following **git checkout** command with the branch name to switch to this new branch:

```
git checkout MyNewBranch
```

If you want to confirm that you have switched to the **MyNewBranch** branch successfully, you can run the **git status** or **git branch** command. The output shows which branch you are on. In this case, it should be **MyNewBranch**.

Finally, if you want to view a list of changes you made in the branch, you can run the **git log** command.

To practice using the git checkout command to switch around branches, you can try to switch back to the main branch and view its list of commits. The Git commands should look like following:

```
git checkout main 
```

and

```
git log
```

If you want to confirm again that you have switched to the main branch in your local shared repo successfully, you can run the **git status** or **git branch** command. The output shows which branch you are on. In this case, it should be **main**.

### Knowledge Check

#### What is the purpose of the git fetch command?

* Retrieve the latest changes from a remote repository without merging.

Wrong answers:

* Upload changes to a remote repository.
* Switch to a different branch.
* Download changes from a remote repository and automatically merge them.

Use the git fetch command to retrieve the latest changes from a remote repository without automatically merging them into the local working branch.

Upload changes to a remote repository with the git push command. git fetch does not switch branches. Although git fetch downloads changes, it doesn’t automatically merge them.

#### Which command is used to display a list of all local and remote branches for a repository? 

* git branch --all

Wrong answers:

* git show
* git commit
* git status

The git branch --all command is a way to display a list of all branches, including local and remote branches in a Git repository.

Use the git show command to display information about commits, not to list branches. Use the git commit command to record changes to the repository. The git status command provides information about the working directory and staging area, not a list of branches.

#### What does the pull action do?

* Fetches changes from a remote repository and merges them into the local repository

Wrong answers:

* Switches to a different branch and merges changes into the current branch
* Deletes the local repository and retrieves a copy of the remote repository
* Updates the remote repository with the changes made locally

Pull refers to fetching changes from a remote repository and merging them into the local repository. 

Pull does not delete the local repository and retrieve a copy of the remote repository. The pull command does not delete the local repository. The git push command is typically used to update the remote repository with changes made locally.

### Summary

#### Pull and push

*Pull* and *push* are actions related to updating and synchronizing code between local repositories and remote repositories:

* **Pull** refers to fetching changes from a remote repository and merging them into the local repository. Pull combines two actions: git fetch and git merge. This ensures that the local codebase is up to date with the latest changes made by other developers. 
* **Push** involves sending local commits to a remote repository. It updates the remote repository with the changes made locally. This is typically done after developers make changes, committing them locally, and wanting to share those changes with others, or update the central repository.

#### Git basic commands

* **Git clone**: Copy an existing git repository from a remote source to your local machine.
* **Git config**: Configure settings for your git installation, such as your name and email.
* **Git add**: Add file changes in your working directory to the staging area.
* **Git commit**: Create a new commit containing your staged changes. Note that only staged changes are included in a commit operation.
* **Git push**: Publish local changes to a shared repository after committing.
* **Git pull**: Fetch commits from a remote repository and integrates them into your local branch.
* **Git log**: Show the commit history in the repository.
* **Git fetch**: Retrieve the latest changes from a remote repository without merging them into your local repository.
* **Git branch**: List existing branches or create a new branch (when followed by new branch name).
* **Git status**: Review the current state of your repository and staging area.

## Using Automation Tools to Design a Pipeline

### Pre-assessment

#### What is continuous integration and continuous delivery (CI/CD)?

* A software development practice where code changes are automatically built, tested, and deployed to production frequently

Wrong answers:

* A process where software code is manually built, tested, and deployed by a development team
* A system where software code is reviewed by managers before deployment
* A tool for tracking bugs and new feature requests

CI/CD is a DevOps software development practice where developers regularly merge their code changes into a central repository, after which automated builds and tests are run.

#### Which AWS service is used to compile source code, run tests, and produce software packages?

* AWS CodeBuild

Wrong answers:

* AWS CodeCommit
* Amazon CloudWatch
* AWS Cloud9

CodeBuild automatically compiles source code, runs tests, and produces software packages that are ready to deploy.

#### What is AWS CodeDeploy used for?

* Deploying applications to a chosen compute service

Wrong answers:

* Storing application code in repositories
* Building Docker container images
* Setting up continuous integration pipelines

CodeDeploy is a fully managed service that automates software deployments so they deploy reliably and rapidly. It automates code deployment to a variety of compute services, including Amazon Elastic Compute Cloud (Amazon EC2), AWS Fargate, AWS Lambda, or on-premises servers.

### Introduction to CI/CD

CI and CD are processes that streamline your software delivery process within a development pipeline.

#### Continuous Integration (CI)

Continuous integration is a software development practice where developers regularly merge their code changes into a central repository. Automated builds and tests are then run. During a build, tests verify the code integrates correctly and checks for regressions, bugs, or issues. If an issue is found, the build fails and the commit that introduced the test failure is identified so developers know where to look. This way, teams can resolve merging issues and code defects early.

Continuous integration most often refers to the build or integration stage of the software release process. It requires both an automation component (for example, a CI or build service) and a cultural component (for example, learning to integrate frequently). The key goals of continuous integration are to find and address bugs quicker, improve software quality, and reduce the time it takes to validate and release new software updates.

#### Continuous delivery and continuous deployment (CD)

Continuous delivery is a software development practice where every code change is automatically built, tested, and then deployed to a non-production testing or staging environment. Manual approval is required before pushing to production. When properly implemented, developers will always have a deployment-ready build artifact that has passed through a standardized test process.

Continuous deployment is similar to continuous delivery, but with automatic deployment to production. Tested code does not need an explicit approval before being pushed to production.

### CI/CD best practices

1. Implement security checks at every stage of the CI/CD pipeline to find vulnerabilities early.
2. Build artifacts once and reuse them throughout the pipeline for consistency and efficiency.
3. Facilitate quick feedback to developers when issues occur so they can promptly roll back and fix code.
4. Commit code daily for early identification of issues while changes are still fresh.
5. Balance test coverage and performance. Avoid overly long testing cycles.
6. Clean pre-production environments between deployments to avoid outdated configurations.
7. Document release and rollback plans for transparency and identifying improvements.
8. Encourage ongoing feedback from monitoring, testing, and deployment to empower continuous improvements in the evolving CI/CD loop.

### Stages in a CI/CD pipeline

#### Code

Develop code in languages such as Java, C#, or Python. When ready, deliver this code to a central location. Peers review the new code.

#### Build

Creating builds of your software can include some of the following actions:

* Compile code.
* Check code styles and standards.
* Analyze code complexity and maintainability.
* Validate dependencies.
* Create container images.
* Run unit tests.

#### Test

Assess if the application meets the defined functional, performance, design, and implementation requirements.

#### Release

Prepare and package the tested code with a specific version number.

#### Deploy

Deploy the release to targeted environments, such as test, staging, alpha, beta, or production.

#### Monitor

Monitor the application in production to quickly detect unusual activity or errors.

The goal of DevOps is to follow a continuous delivery model that is repeatable, reliable, stable, resilient, and secure, and improves operational efficiency.

Teams must collaborate with each other and get involved in the development and delivery process. 

Relationships across teams are vital. Without cross-team communication and collaboration, processes are likely to fail.

The following are some ways a cloud developer can help improve cross-team communication and collaboration:

* Participate in daily standups or scrums with other teams like operations and quality assurance (QA) to share updates and risks. This helps increase visibility across teams.
* Work closely with operations teams during development to make sure infrastructure and operational needs are considered early. This avoids surprise changes late in the process.
* Use collaboration tools like Slack, Jira, or Confluence to centralize conversations and documentation. This creates a single source of truth.
* Promote a blameless culture focused on shared goals and outcomes, rather than individual roles. This reduces silos and finger pointing.

### Setting Up a CI/CD Pipeline with AWS Developer Tools

#### Developer tools

You can use AWS Cloud9 to write, run, and debug your code. Additional developer tools include SDKs and AWS Cloud Development Kit (AWS CDK). You can also make code changes to an AWS CodeCommit repository.

#### AWS CodeCommit

With AWS CodeCommit, you can securely store and source-control your code.

#### AWS CodeBuild

With AWS CodeBuild, you can automatically compile source code, run tests, and produce software packages that are ready to deploy.

#### AWS CodeDeploy

AWS CodeDeploy is a fully managed deployment service that automates software deployments to a variety of compute services. These services include Amazon Elastic Compute Cloud (Amazon EC2), AWS Fargate, AWS Lambda, and your on-premises servers.

#### AWS CodePipeline

AWS CodePipeline is a fully managed continuous delivery service that helps you automate your release pipelines for fast and reliable application and infrastructure updates. CodePipeline automates the build, test, and deploy phases of your release process every time there is a code change, based on the release model you define.

#### AWS X-Ray

AWS X-Ray is a service that collects data about requests that your application serves. It provides tools that you can use to view, filter, and gain insights into that data to identify issues and opportunities for optimization. For any traced request to your application, you can see detailed information about the request and response. Additionally, you can see information about calls that your application makes to downstream AWS resources, microservices, databases, and web APIs.

#### Amazon CloudWatch

Amazon CloudWatch monitors your AWS resources and the applications you run on AWS in real time. You can use CloudWatch to collect and track metrics, which are variables you can measure for your resources and applications. The CloudWatch homepage automatically displays metrics about every AWS service you use. Additionally, you can create custom dashboards to display metrics about your custom applications, and display custom collections of metrics that you choose.

### Source control

CodeCommit is a fully managed source control service that hosts secure Git-based repositories. A repository is a fundamental version control object in CodeCommit, and it stores your project files and source code.

CodeCommit can start the pipeline when a new code change is made on the configured CodeCommit repository and branch.

Additional version control systems include GitHub, GitLab, and Bitbucket.

#### Why use it

You can use CodeCommit to do the following:

* Eliminate the administrative overhead of managing your own hardware and software needed to store your code. CodeCommit is fully managed, highly available, and has no limits in the type or size of files it can store.
* Continue using Git commands that many developers are already familiar with. CodeCommit is a secure Git-based repository that can handle large numbers of files, code branches, and lengthy revision histories.
* Improve your existing workflow by integrating CodeCommit with other AWS services, integrated development environments (IDEs), and other software (for example, Jira).
* Create notifications and invoke actions based on events, such as when a branch is created or a commit is made.

#### How it works

In CodeCommit, you create a repository. Users clone it to their environments, creating their own copy of the repository. After making changes, they push those changes back to the CodeCommit repository.

The CodeCommit repository is managed with Git source control. Git commands (such as git add, git push, git branch) can be used to work and collaborate on the code.

If it’s part of a pipeline, CodeCommit can start the pipeline when a new code change is made on the configured CodeCommit repository and branch.

### Building and testing

AWS offers AWS CodeBuild to package your code for deployment. CodeBuild is a fully managed build service that automatically compiles source code, runs tests, and produces software packages.

Additional build tools include Jenkins(opens in a new tab), Gradle(opens in a new tab), Maven(opens in a new tab), and Travis CI(opens in a new tab), among others.

#### Why use it

You can use CodeBuild to do the following:

* Eliminate the need to set up, patch, update, and manage your own build servers. CodeBuild is fully managed.
* Automatically compile source code, run tests, and produce build artifacts.
* Specify build commands to run at each phase of the build.
* Process multiple builds concurrently. For example, developers can continuously build and test their code, catch errors early, and correct them early.
* Use out-of-the-box preconfigured build environments (such as .NET Core, Java, Ruby, Python, Go, Node.js, Android, and Docker). Build environments contain the operating system, programming language runtime, and build tools (such as Apache Maven and Gradle). You can also provide custom build environments suited to your needs by means of Docker images.
* Pull source code from CodeCommit, Amazon S3, GitHub, GitHub Enterprise, and Bitbucket.
* Integrate CodeBuild with Jenkins to streamline the build process.

#### How it works

CodeBuild uses a build project to compile source code, run tests, and produce software packages that are ready to deploy. A build project contains information needed to run the build, such as source repository location, runtime environment, build command, and where to store the build output.

In a CI/CD pipeline, when CodeBuild is notified that new code has been uploaded to CodeCommit, it starts a new build. It downloads the content, creates a new environment, puts everything together, and uploads the completed artifact to Amazon Simple Storage Service (Amazon S3).

Build logs are stored using Amazon CloudWatch Logs. When the build is complete, this can optionally prompt a message sent using an Amazon Simple Notification Service (Amazon SNS) topic.

##### An example of how CodeBuild integrates into a CI/CD pipeline

CodeCommit sends code to CodeBuild, which packages the code. The output is stored in Amazon S3. The successfully completed build invokes a message posted to an Amazon SNS topic. The build events are monitored by Amazon CloudWatch.

AWS CodeCommit -> AWS CodeBuild -> New container-based environment -> [Amazon S3, Amazon SNS topic, Amazon CloudWatch]

AWS CodeCommit sends code to AWS CodeBuild, which packages the code and stores in S3, invoking an SNS message and CloudWatch Logs.

### Deploying code

When your code is ready, you can use AWS CodeDeploy to deploy it to a compute service of your choice. CodeDeploy is a fully managed service that automates your software deployments, so you can deploy reliably and rapidly. It automates code deployment to a variety of compute services, including Amazon EC2, AWS Fargate, AWS Lambda, or on-premises servers.

Additional deployment tools include Jenkins, GitLab, and Octopus Deploy.

#### Why use it

You can use CodeDeploy to do the following:

* Deploy server, serverless, or container applications.
* Automate deployments and eliminate the need for manual, error-prone operations. With CodeDeploy you can reliably and rapidly release new features and updates.
* Deploy on a variety of compute platforms, including the following: AWS Lambda, Amazon Elastic Container Service (Amazon ECS), Amazon EC2, or on-premises. You can even configure CodeDeploy to deploy to an Amazon EC2 Auto Scaling group, which will prepare the environment before traffic is sent to it.
* Concurrently deploy to one or multiple instances as the service scales to fit your needs.
* Minimize production downtime for your application by specifying if an update will be applied on an existing instance, or a newly provisioned environment that will replace the previous environment. You can also control how to handle the traffic shifts from older to new versions. For example, consider an application that needs at least 50 percent of the instances in a deployment group to be up and serving traffic. You can specify that in your deployment configuration so that a deployment does not cause downtime.
* Automatically (or through user intervention) stop an unsuccessful deployment and roll back your deployment to a previous version.

#### How it works

To automate the deployment to the appropriate compute resources, CodeDeploy needs to know which files to copy, which scripts to run, and where to deploy.

During deployment, CodeDeploy looks for your AppSpec file in the root directory of the application's source. The AppSpec file specifies where to copy the code and how to get it running. For example, it tells CodeDeploy how to stop the application if it is already running, and how to install the code. It also tells CodeDeploy which command to run before and after the code is installed, and how to get the application running again.



A deployment group specifies the deployment targeted environment. The information it contains is specific to the target compute platform: AWS Lambda, Amazon ECS, Amazon EC2, or on-premises. For example, Amazon ECS lets you specify the Amazon ECS service, load balancer, and more. For Amazon EC2, it is a logical group of deployment target instances or physical environments.



The CodeDeploy agent is needed if you are deploying to Amazon EC2 or an on-premises compute platform. It is installed and configured on the target instances. It accepts and runs requests on behalf of CodeDeploy.

During deployment, a deployment configuration defines a set of deployment rules and deployment success and failure conditions. For an Amazon EC2 compute platform, it specifies the number or percentage of instances that must remain available during deployment. It also specifies if an instance in the deployment group is briefly taken offline and updated with the latest code revision, or if a new instance replaces the instances in the deployment group.


The AppSpec file tells CodeDeploy what to deploy. The deployment configuration defines how to deploy the application. The deployment group specifies the target compute environment.

### Pipeline orchestration

CodePipeline can be used to add actions at specific points within the overall CI/CD process. You can view a visual representation of the pipeline in the CodePipeline console and track the progress of updates as they move through each phase.

When a code change is committed to CodeCommit, this prompts CodeBuild to start the build phase. The code goes through a series of automated tests in a build environment before it is packaged for deployment and uploaded to an S3 bucket. This prompted CodeDeploy to retrieve the package and deploy it to an Amazon EC2 Auto Scaling group in a development environment. All of these stages occur automatically after the single action of committing the code is completed.

Considering additional automation that could be incorporated into the CI/CD pipeline, notifications could be automatically sent after each stage is completed successfully. Alternatively, a notification can be received if a stage fails. Maybe AWS Lambda functions could be incorporated to initiate additional automation.

#### CodePipeline actions

AWS CodePipeline includes a number of actions that help you configure build, test, and deploy resources for your automated release process. An action is a set of operations performed on application code and configured to run in the pipeline at a specified point. This can include things like a source action from a code change, an action for deploying the application to instances, and so on. For example, a deployment stage might contain a deployment action that deploys code to a compute service like Amazon EC2 or AWS Lambda.

You can use CodePipeline to add actions to stages in your CI/CD pipeline. Each action can be associated with a provider that performs the action.

CodePipeline provides support for six types of actions:

* Source
* Build
* Test
* Deploy
* Approval
* Invoke

#### Source

Specify where source code is stored.

For example: Amazon S3, CodeCommit, GitHub, or Amazon Elastic Container Registry (Amazon ECR).

#### Build

Specify how the application should be built.

For example: CodeBuild, CloudBees, Jenkins, or TeamCity.

#### Test

Specify how the application should be tested.

For example: CodeBuild, Jenkins, or Ghost Inspector.

#### Deploy

Specify how the application should be deployed.

For example: AWS CloudFormation, CodeDeploy, Amazon EC2, or Stacks.

#### Invoke

Specify a custom function to invoke.

For example: AWS Lambda.

#### Approval

Publish an Amazon SNS topic for manual approval.

### A quick look at CodePipeline

1. **Source**. When developers commit changes to a source repository, CodePipeline automatically detects the changes.
2. **Build**. The changes to the source code are built, and if any tests are configured, those tests are run.
3. **Staging**. After the tests are complete, the built code is deployed to staging servers for testing. From the staging server, CodePipeline runs more tests, such as integration or load tests.
4. **Manual approval**. Upon the successful completion of the tests in staging, a manual approval action must be approved for the pipeline to continue.
5. **Production**. CodePipeline deploys the tested and approved code to production instances.
6. **Customer feedback**. End users request changes, updates, and fixes as they interact with the deployed code.
7. **Developers**. The customer feedback is collected and developers implement the requested changes, updates, and fixes. This starts the pipeline over.

CodePipeline can deploy applications to EC2 instances by using CodeDeploy, AWS Elastic Beanstalk, or other integrated services. CodePipeline can also deploy container-based applications to services by using Amazon ECS. Developers can also use the integration points provided with CodePipeline to plug in other tools or services, including build services, test providers, or other deployment targets or systems.

## Pipeline Examples

### CodePipeline concepts

#### Pipeline

A *pipeline* is a workflow construct that describes how software changes go through a release process. Each pipeline is made up of a series of stages.

#### Stages

A *stage* is a logical unit you can use to isolate an environment and to limit the number of concurrent changes in that environment. Each stage contains actions that are performed on the application *artifacts*. Your source code is an example of an artifact. A stage might be a build stage, where the source code is built and tests are run. It can also be a deployment stage, where code is deployed to runtime environments. Each stage is made up of a series of serial or parallel *actions*.

#### Actions

An *action* is a set of operations performed on application code and configured so that the actions run in the pipeline at a specified point. This can include things like a source action from a code change, an action for deploying the application to instances, and so on. For example, a deployment stage might contain a deployment action that deploys code to a compute service like Amazon EC2 or AWS Lambda.

Valid CodePipeline action types are **source**, **build**, **test**, **deploy**, **approval**, and **invoke**.

Actions can run in series or in parallel.

#### Artifacts

*Artifacts* refers to the collection of data, such as application source code, built applications, dependencies, definitions files, templates, and so on, that is worked on by pipeline actions. Artifacts are produced by some actions and consumed by others. In a pipeline, artifacts can be the set of files worked on by an action (*input artifacts*) or the updated output of a completed action (*output artifacts*).

Actions pass output to another action for further processing using the pipeline artifact bucket. CodePipeline copies artifacts to the artifact store, where the action picks them up.

#### Transitions

A transition is the point where a pipeline operation moves to the next stage in the pipeline.

### Three-stage pipeline example

1. **Source**. Source actions are special actions. They continuously poll the source providers, such as AWS CodeCommit, GitHub, and Amazon S3 to detect changes. When a change is detected, the new pipeline is created and the new pipeline begins its run. The source actions retrieve a copy of the source information and place it in an Amazon S3 bucket.
2. **Build**. When the source actions are completed, the source stage is marked as successful and the process transitions to the build stage. The build stage contains one action: BuildMyApp. AWS CodeBuild is integrated into AWS CodePipeline as a native function. You can create the AWS CodeBuild project before or while you create your pipeline with AWS CodePipeline.
3. **Deploy**. When the build action is completed, the build stage is marked as successful, and the process transitions to the deploy stage. The deploy stage contains one action: AWS CodeDeploy deployment action. The AWS CodeDeploy action retrieves the build artifact from your Amazon S3 bucket and deploys it to the AWS CodeDeploy deployment group.

### Some options for customizing a pipeline

#### Parallel actions

There are alternatives to a basic pipeline. For example, at the Build stage, a parallel action to send a notification to the development team can be added to the build phase. Because BuildMyApp and NotifyDevelopers are parallel actions, they are initiated at the same time.

The following is an example of an automatic notification: “Hi, Dev team – this is a friendly note to let you know that a change was detected in the source code, and a new build has been initiated.”

#### Sequential actions

For example, a sequential action can be added to perform post-build tests. The TestAPI action is started only after the DeployMyApp action is completed successfully.

#### Manual approvals

Instead of an automated approval that occurs after all tests have been passed, you can add a manual approval. When a manual approval is added, the pipeline stops running when it has reached the point at which you set the approval action. It resumes only when someone approves or rejects the revision in progress. For example, you might want someone to perform a code review or change management review before a revision is allowed into the next stage of the pipeline.

Approval action is managed with AWS Identity and Access Management (IAM) permissions. You can notify approvers in several ways, including email, AWS Server Migration Service (AWS SMS), webhooks, and more.

Note that approval actions can't be added to the first stage of a pipeline. The first stage of a pipeline can contain only source actions.

### Fully automated CI/CD pipeline with CodePipeline example

The AWS services in this pipeline compile, build, and install an application onto a set of Amazon EC2 instances. The goal in this example is to promote a code commit or change to pass through various automated stage gates. The code commit passes all the way from development to production environments, across AWS accounts.

This example uses two separate AWS accounts: a Dev account and a Prod account.

The Dev account is used to deploy and set up the CI/CD pipeline, along with the source code repo. It also builds and tests the code locally and performs a test deploy.

After the application is deployed successfully in the Dev account, it is then deployed in the Prod account from the pipeline in the Dev account.

1. **CodeCommit initiates an EventBridge event**. A change or commit to the code in the CodeCommit application repository initiates CodePipeline with the help of an Amazon EventBridge event.
2. **Action: Build and test**. CodePipeline downloads the code from the CodeCommit repository, initiates the build and test action using CodeBuild, and securely saves the built artifact in an S3 bucket.
3. **Action: Deploy in Dev**. If the preceding step is successful, CodePipeline initiates the Deploy in Dev action using CodeDeploy and deploys the application in the dev account.
4. **Action: Deploy in Prod**. If successful, CodePipeline initiates the Deploy in Prod action using CodeDeploy and deploys the application in the prod account. CodePipeline in the dev account assumes a cross-account role in the prod account to deploy the application.

### Considerations when designing your CI/CD pipeline

* **Stages**: Which stages do you want in your pipeline?
* **Types of tests**: Which types of tests do you want to run at each stage?
* **Order of tests**: Which tests must be run sequentially? Can any be run in parallel?
* **Detect and report failures**: How will the system detect and report failures?
* **Regions**: Which AWS Regions will your AWS services be running in?
* **Provisioning and management**: How will you provision and manage the infrastructure for your test and production environments?
* **Rollbacks**: If problems are detected, how will you roll back to a previous version?

### [Lab: Introduction to AWS CodeDeploy](./W10Lab01-AWSCodeDeploy.md)

### Knowledge Check

#### What is the DevOps software development practice where developers regularly merge their code changes into a central repository, initiating automated builds and tests?

* Continuous integration

Wrong answers:

* Continuous deployment
* Manual approval
* Pipeline orchestration

Continuous integration is a DevOps software development practice where developers regularly merge their code changes into a central repository, after which automated builds and tests are run. This way, teams can resolve merging issues and code defects early, when they are convenient and more cost effective to resolve.

#### What is AWS CodeBuild used for?

* Building and testing code

Wrong answers:

* Automating the different stages of the software release process
* Creating a code repository
* Deploying server, serverless, or container applications

CodeBuild is a fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy.

#### Which AWS service can add actions to the stages in a continuous integration and continuous delivery (CI/CD) pipeline?

* AWS CodePipeline

Wrong answers:

* AWS CodeBuild
* AWS CodeDeploy
* AWS CodeCommit

CodePipeline is a continuous delivery service that can add actions to stages in a CI/CD pipeline. Each action can be associated with a provider that performs the action.

### Additional Resources

#### [DevOps Tools and Resources Free on AWS](https://aws.amazon.com/free/devops/)

#### [What is DevOps?](https://aws.amazon.com/devops/what-is-devops/)

#### [Complete CI/CD with AWS CodeCommit, AWS CodeBuild, AWS CodeDeploy, and AWS CodePipeline](https://aws.amazon.com/blogs/devops/complete-ci-cd-with-aws-codecommit-aws-codebuild-aws-codedeploy-and-aws-codepipeline/)

### Summary

#### Introduction to CI/CD

The goal of CI/CD is to speed up the software development lifecycle and make it more efficient. The following is a summary of the key points about CI/CD:

* Continuous integration (CI) is a development practice where developers frequently merge code changes into a shared repository. Automated builds and tests then run to catch issues early.
* Continuous delivery/deployment (CD) automatically builds, tests, and deploys code changes to staging and production environments. Manual approval might be required before production deployments.
* CI/CD best practices include frequent commits, automated testing, rapid deployments, infrastructure automation, and monitoring.
* A CI/CD pipeline has stages like code, build, test, release, deploy, and monitor that move code from development to production.
* Cross-team communication and collaboration between developers, operations, QA, and other teams is vital for CI/CD success. Without it, processes will likely fail.

#### Setting up a CI/CD pipeline

AWS supports CI/CD with a number of services that developers use at every stage of the application lifecycle. Your DevOps solution might comprise AWS and non-AWS services.

1. **AWS Cloud9**. You can use AWS Cloud9 to write, run, and debug your code. Additional developer tools include SDKs and AWS CDK. You can also make code changes to an AWS CodeCommit repository.
2. **AWS CodeCommit**. With AWS CodeCommit, you can securely store and source-control your code.
3. **AWS CodeBuild**. With AWS CodeBuild, you can automatically compile source code, run tests, and produce software packages that are ready to deploy.
4. **AWS CodeDeploy**. AWS CodeDeploy is a fully managed deployment service that automates software deployments to a variety of compute services, such as Amazon EC2, AWS Fargate, AWS Lambda, and your on-premises servers.
5. **AWS X-Ray**. AWS X-Ray is a service that collects data about requests that your application serves. It provides tools that you can use to view, filter, and gain insights into that data to identify issues and opportunities for optimization. For any traced request to your application, you can see detailed information about the request and response. Additionally, you can see calls that your application makes to downstream AWS resources, microservices, databases, and web APIs.
6. **Amazon CloudWatch**. Amazon CloudWatch monitors your AWS resources and the applications you run on AWS in real time. You can use CloudWatch to collect and track metrics, which are variables you can measure for your resources and applications. The CloudWatch homepage automatically displays metrics about every AWS service you use. You can additionally create custom dashboards to display metrics about your custom applications, and display custom collections of metrics that you choose.
7. **AWS CodePipeline**. AWS CodePipeline is a fully managed continuous delivery service that helps you automate your release pipelines for fast and reliable application and infrastructure updates. CodePipeline automates the build, test, and deploy phases of your release process every time there is a code change, based on the release model you define.

#### Pipeline orchestration with AWS CodePipeline

AWS CodePipeline is a continuous delivery service that you can use to model, visualize, and automate the different stages of your software release process. It can be integrated with the AWS developer tools you learned about in this module for building, testing, and deploying your software versions.

You can use CodePipeline to add actions to stages in your CI/CD pipeline, such as the following:

* Where source code is stored
* How the application is built
* How the application is tested
* How the application is deployed
* Custom functions to invoke
* Notifications for manual approval

#### Pipeline examples

A pipeline must contain at least two stages. An example of a three-stage pipeline consists of the source, build, and deploy stages.

##### Source

The first stage of the pipeline can only contain source actions, and it must contain at least one. Only the first stage can contain source actions.

Source actions continuously poll the source providers, such as AWS CodeCommit, GitHub, and Amazon S3, to detect changes. When a change is detected, the new pipeline is created, and it begins its run. The source actions retrieve a copy of the source information and place it in a customer-owned Amazon S3 bucket.

##### Build

When the source actions are completed, the source stage is marked as successful, and the process transitions to the build stage. The build stage contains one action: BuildMyApp. AWS CodeBuild is integrated into AWS CodePipeline as a native function. You can create the AWS CodeBuild project before or while you create your pipeline with AWS CodePipeline.

##### Deploy

When the build action is completed, the build stage is marked as successful, and the process transitions to the deploy stage. The deploy stage contains one action: AWS CodeDeploy deployment action. The AWS CodeDeploy action retrieves the build artifact from the customer-owned Amazon S3 bucket and deploys it to the AWS CodeDeploy deployment group.

#### Customizing a pipeline with additional features

* **Parallel actions**: Initiate multiple actions simultaneously, such as building the code and sending a notification.
* **Sequential actions**: Create actions that occur automatically after a previous action is completed successfully.
* **Manual approvals**: Stop the pipeline from running until someone approves or rejects the revision in progress.
