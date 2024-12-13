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
