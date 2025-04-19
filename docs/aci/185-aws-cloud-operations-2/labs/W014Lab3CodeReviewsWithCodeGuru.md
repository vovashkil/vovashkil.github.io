# Automating Code Reviews with Amazon CodeGuru

## Lab overview

In this lab, the learner utilizes Amazon CodeGuru to perform a code review on existing code.

## Objectives

By the end of this lab, you will be able to do the following:

Review the existing application, branch structure, and CI/CD pipeline.
Associate Amazon CodeGuru with the repository and branch to run a code analysis.
Review Amazon CodeGuru findings and update the codebase.
Prerequisites
This lab requires:

Access to a computer with Microsoft Windows, Mac OS X, or Linux (Ubuntu, SuSE, or Red Hat)
A modern internet browser such as Chrome or Firefox
Duration
This lab requires approximately 60 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Caution: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Expected output: A sample output that you can use to verify the output of a command or edited file
 Note: Additional information or elaboration on a point
 Command: A command that you must run
 Refresh: A time when you might need to refresh a web browser page or list to show new information
 Task complete: A conclusion or summary point in the lab
Start lab
To launch the lab, at the top of the page, choose Start lab.

 Caution: You must wait for the provisioned AWS services to be ready before you can continue.

To open the lab, choose Open Console .

You are automatically signed in to the AWS Management Console in a new web browser tab.

 Warning: Do not change the Region unless instructed.

Common sign-in errors
Error: Choosing Start Lab has no effect
In some cases, certain pop-up or script blocker web browser extensions might prevent the Start Lab button from working as intended. If you experience an issue starting the lab:

Add the lab domain name to your pop-up or script blocker’s allow list or turn it off.
Refresh the page and try again.
AWS services used in this lab
AWS Cloud9
AWS Cloud9 is an integrated development environment, or IDE. The AWS Cloud9 IDE offers a rich code-editing experience with support for several programming languages and runtime debuggers, and a built-in terminal. It contains a collection of tools that you use to code, build, run, test, and debug software, and helps you release software to the cloud.

You access the AWS Cloud9 IDE through a web browser. You can configure the IDE to your preferences. You can switch color themes, bind shortcut keys, enable programming language-specific syntax coloring and code formatting, and more.

Amazon CodeGuru Reviewer
Amazon CodeGuru Reviewer is a service that uses program analysis and machine learning to detect potential defects that are difficult for developers to find and offers suggestions for improving your Java and Python code.

By proactively detecting code defects, CodeGuru Reviewer can provide guidelines for addressing them and implementing best practices to improve the overall quality and maintainability of your code base during the code review stage.

AWS CodePipeline
AWS CodePipeline is a continuous delivery service you can use to model, visualize, and automate the steps required to release your software. You can quickly model and configure the different stages of a software release process. CodePipeline automates the steps required to release your software changes continuously.

Task 1: Review the existing application, branch structure, and CI/CD pipeline
In this task, you review the source code repository of an existing Python application. Then, you review the CI/CD pipeline that deploys the application.

Task 1.1: Find the code in AWS CodeCommit
In this task, you find the application code in CodeCommit.

At the top of the AWS Management Console, in the search bar, search for and choose CodeCommit.

In the Repositories list, choose the name of the python-app-code code repository.

 Note: The application has the following directory structure.


.
└── python-app-code/
    ├── scripts/
    │   ├── after_install.sh
    │   ├── application_start.sh
    │   ├── application_stop.sh
    │   └── before_install.sh
    ├── templates/
    │   ├── dashboard.html
    │   └── index.html
    ├── tests/
    │   ├── __init__.py
    │   ├── test_integration.py
    │   └── test_unit.py
    ├── utils/
    │   ├── __init__.py
    │   └── validate_form_data.py
    ├── .gitignore
    ├── app.py
    ├── appspec.yml
    ├── aws_controller.py
    ├── buildspec.yml
    ├── gunicorn_config.py
    └── requirements.txt
The Python application is a simple Flask application that allows a user to enter data which is stored in an Amazon DynamoDB table. Users are able to view the data from that table in a list. The scripts folder contains shell scripts that handle events for AWS CodeDeploy to start, stop, and install the application. The templates folder contains the Flask HTML templates for the web application. The tests folder contains both unit and integration tests to help verify the application in a CI/CD pipeline. The utils folder contains some utility functions used by the application.

app.py: The entry point for the Flask application defining the basic structure.
appspec.yml: Used by AWS CodeDeploy to install the application.
aws_controller.py: Contains logic to access the Amazon DynamoDB table.
buildspec.yml: Defines the what happens during the build phase of the CI/CD pipeline.
gunicorn_config.py: Configures Gunicorn which allows the app to run on Linux.
requrements.txt: Used by Python to install the required modules to run the application.
In the left navigation pane under Repositories, choose Branches.

 Note: Notice that your application has one branch, main, which is the default branch.

Task 1.2: Review the Code Pipeline
In this task, you review the CI/CD pipeline that is configured for the application.

In the left navigation pane, select Pipeline - CodePipeline and choose Pipelines.

 Caution: You can safely ignore the message that prompts you about leaving the site. There is no data to save.

 Caution: The ApplicationPipeline has a Latest execution status of Failed when the lab starts. You can safely ignore this error for now.

In the Pipelines list, choose the name of the ApplicationPipeline.

 Note: Notice that the pipeline has 3 stages: Source, Build, and Deploy.

Source: The source stage pulls the source code from the CodeCommit repository.
Build: The build stage builds and packages the code and runs unit tests.
Deploy: The deploy stage installs the application into the application environment.
 Task complete: You have reviewed the code repository and the code pipeline.

Task 2: Associate CodeGuru Reviewer with the repository and branch
In this task, you associate the application code repository with CodeGuru Reviewer to perform a full analysis on the code.

At the top of the AWS Management Console, in the search bar, search for and choose CodeGuru.

In the getting started panel, select CodeGuru Reviewer from the dropdown and then choose Get Started.

On the Associate repository and create a code review page, configure the following:

In the Associate repository section:

For Select source provider, choose AWS CodeCommit.
For Repository location, select python-app-code.
In Run a repository analysis section:

For Source branch, select main.
For Code review name, keep the supplied default value.
Choose Associate repository and run analysis.

 Note: CodeGuru Reviewer is creating an association with python-app-code. After the repository is associated, a full repository analysis python-app-code-first-review will start.

 Refresh: It may take up to 10 minutes for the repository association to complete and the code review to be ready. The status of your code review will change from Pending to Completed. Choose the refresh button every few seconds until the status changes to Completed.

In the Full repository analysis panel, choose the name of the code review that you created.

On the Python-app-code-first-review details page, scroll down to the Recommendations section.

 Note: CodeGuru Reviewer found 3 recommendations based on the code in the repository.

app.py Line 51
aws_controller.py Line 7
aws_controller.py Line 7
The recommendations give an explanation of potential problems found in the code as well as links documentation further describing the findings.

To see the code causing the problem, choose the link. A new window opens in the CodeCommit console with the problematic code highlighted.

 Task complete: You have successfully associated CodeGuru Reviewer with your CodeCommit repository.

Task 3: Review CodeGuru Reviewer findings and update the codebase
In this task, you review the findings from CodeGuru Reviewer and modify the code based on the recommendations from CodeGuru Reviewer. Next, you commit and push your code changes to the repository and create a pull request. The pull request triggers an incremental code review. Finally, you merge your code into the main branch of the repository.

Task 3.1: View the recommendations
In this task, you review the recommendations from CodeGuru Reviewer.

Read the text in each of the recommendations from the code analysis.

 Note: Take note of the potential problems that each of these recommendations calls out. Next, you make changes to the code according to the recommendations.

Task 3.2: Clone the code repository and make code changes
In this task, you clone the repository to AWS Cloud9. Then, you make code changes based on the recommendations from CodeGuru Reviewer.

Copy the Cloud9Environment URL link from the Lab Information section to the left of these instructions and paste it into a new browser tab.

 Note: The browser takes you to the AWS Cloud9 environment that you use during this lab.

To open a new terminal window, select Window at the top of the screen and choose New Terminal.

 Command: To clone the python-app-code repository, run the following command:


git clone codecommit::us-west-2://python-app-code
 Expected output:


************************
**** EXAMPLE OUTPUT ****
************************

Cloning into 'python-app-code'...
remote: Counting objects: 23, done.
Unpacking objects: 100% (23/23), 4.86 KiB | 382.00 KiB/s, done.
 Command: To navigate to the source code directory and create a feature branch for maintenance, enter the following commands in the terminal.


cd python-app-code
git checkout -b my_code_update
 Expected output:


************************
**** EXAMPLE OUTPUT ****
************************

Switched to a new branch 'my_code_update'
To see the contents of the code folder, in the panel to the left, expand the python-app-code folder.

Open the app.py file.

Modify the last line of the app.py file by removing the parameter debug=True.

 Note: After you make the change, the last line of app.py should look like the following:


    app.run(host=host, port=port)
Save the file and close it.

Open the aws_controller.py file.

Modify line 6 of aws_controller.py by removing the hard-coded credentials in the call to create a DynamoDB client.

 Note: After you make the change, line 6 of the aws_controller.py file should look like the following. Lines 7, 8, and 9 should be removed. The credentials do not need to be supplied in app.py. The EC2 Instance profile of the instance where the code is deployed has the appropriate credentials.


dynamo_client = boto3.client('dynamodb')
Save the file and close it.

 Command: To stage the changes and commit them to your local repository, run the following commands:


git add -A
git commit -m "Modified files to implement CodeGuru Reviewer recommendations"
 Expected output:


************************
**** EXAMPLE OUTPUT ****
************************

[my_code_update 06af7e1] Modified files to implement CodeGuru Reviewer recommendations
Committer: Ubuntu <ubuntu@ip-10-0-1-148.us-west-2.compute.internal>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

2 files changed, 2 insertions(+), 5 deletions(-)
 Command: To push your changes to the python-app-code repository, run the following command:


git push --set-upstream origin my_code_update
 Expected output:


************************
**** EXAMPLE OUTPUT ****
************************

Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 2 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 400 bytes | 400.00 KiB/s, done.
Total 4 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Validating objects: 100%
To codecommit::us-west-2://python-app-code
* [new branch]      my_code_update -> my_code_update
Branch 'my_code_update' set up to track remote branch 'my_code_update' from 'origin'.
Task 3.3: Create a pull request
In this task, you create a pull request to merge your code into the main branch. In CodeGuru Reviewer, you verify that no more recommendations exist for the code. Finally, you merge the code into the main branch.

At the top of the AWS Management Console, in the search bar, search for and choose CodeCommit.

In the Repositories list, choose the name of the python-app-code code repository.

In the left navigation panel under Repositories, choose Pull requests.

Choose the Create pull request button.

On the Create pull request page, configure the following:

For Destination, select main.
For Source, select my_code_update.
Choose Compare.

Choose Create pull request.

 Note: Creating a pull request to the main branch triggers CodeGuru Reviewer to run an incremental code review on the changes.

On the AWS Management Console, in the search bar, search for and choose CodeGuru.

In the left navigation pane under Reviewer, choose Code reviews.

 Note: The new code review is in the Incremental code reviews tab.

 Refresh: The code review may be in pending status. Choose the refresh button every 30 seconds until the code review is in the Completed status.

Choose the name of the code review in the Incremental code reviews panel.

 Note: Notice in the Recommendations panel that there are no recommendations.

Task 3.3: Merge the pull request to update the main branch of the python-app-code repository
At the top of the AWS Management Console, in the search bar, search for and choose CodeCommit.

In the Repositories list, choose the name of the python-app-code code repository.

In the left navigation panel under Repositories, choose Pull requests.

In the list of pull requests, choose the pull request that you created.

Choose Merge.

Choose Merge pull request.

In the left navigation pane, select Pipeline - CodePipeline and choose Pipelines.

In the Pipelines list, choose the name of the ApplicationPipeline.

Verify that all stages of the pipeline complete successfully.

 Task complete: You have successfully reviewed and implemented the CodeGuru Reviewer recommendations.

Conclusion
 Congratulations! You have successfully done the following:

Reviewed an existing application, branch structure, and CI/CD pipeline.
Associated CodeGuru Reviewer with the repository and branch to run a code analysis.
Reviewed CodeGuru Viewer findings and updated the codebase.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.

Additional resources
For more information about how to use Amazon CodeGuru Reviewer, see What is Amazon CodeGuru Reviewer?.
For More information about how to use AWS CodePipeline, see What is AWS CodePipeline?.
