# Using AWS CodePipeline for Integration Testing

## Lab overview

This lab focuses on integrating automated integration testing into a continuous integration and continuous delivery (CI/CD) pipeline using AWS CodePipeline. You will gain hands-on experience in configuring the pipeline to include an integration testing stage, which validates the application’s functionality before deployment. The lab covers creating a build configuration file, configuring the pipeline’s integration test stage, reviewing integration test code, reviewing test results, and making necessary code updates to verify an application’s conformance to expected functionality. By the end, you will have practical experience in setting up and using integration testing in a CI/CD pipeline, enabling early detection and resolution of issues during the development cycle.

## Objectives

By the end of this lab, you should be able to do the following:

Gain an overview of the CI/CD pipeline and its components.
Add an integration test stage to an existing AWS CodePipeline.
Configure an integration test stage with an AWS CodeBuild project for running tests.
Prepare a code base for integration testing in the CI/CD pipeline.
Review integration test failure and resolve issues.
Directly interact with an application deployed through the CI/CD pipeline to observe its functionality and frontend interface.
Prerequisites
This lab requires the following prerequisites:

Basic understanding of software development and testing concepts
Familiarity with AWS services like AWS CodePipeline, AWS CodeBuild, and AWS CodeCommit
Basic knowledge of Git for cloning repositories and pushing code changes
Familiarity with YAML syntax for understanding build configuration files
Duration
This lab requires approximately 60 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Command: A command that you must run.
 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Note: Additional information or elaboration on a point.
 Task complete: A conclusion or summary point in the lab.
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
AWS services used in this lab
AWS Cloud9
AWS Cloud9 is an integrated development environment (IDE). The AWS Cloud9 IDE offers a rich code-editing experience with support for several programming languages and runtime debuggers, and a built-in terminal. It contains a collection of tools that you can use to code, build, run, test, and debug software, and it helps you release software to the cloud. You access the AWS Cloud9 IDE through a web browser. You can configure the IDE to your preferences. You can switch color themes, bind shortcut keys, enable programming language-specific syntax coloring and code formatting, and more.

AWS CodePipeline
AWS CodePipeline is a continuous delivery service that you can use to model, visualize, and automate the steps required to release software. You can quickly model and configure the stages of a software release process. CodePipeline automates the steps required to release your software changes continuously.

Task 1: Review the CI/CD pipeline
In this task, you will review the source code repository of an existing Python application. Then, you will review the CI/CD pipeline that deploys the application.

Task 1.1: Find the code in AWS CodeCommit
In this task, you will find the application code in CodeCommit.

At the top of the AWS Management Console, in the search bar, search for and choose CodeCommit.

In the Repositories list, choose the name of the python-app-code code repository.

 Note: The application has the following directory structure.

python-app-code/: This is the root directory of the application code repository.

scripts/: Contains shell scripts used for various stages of the deployment process, such as installing, starting, and stopping the application.

after_install.sh
application_start.sh
application_stop.sh
before_install.sh
templates/: Holds HTML template files used by the application.

dashboard.html
index.html
tests/: Contains test scripts for both unit and integration tests.

__init __.py
test_integration.py
test_unit.py
utils/: Includes utility modules with helper functions for the application.

__init __.py
validate_form_data.py
Configuration and other files:

.gitignore: File that specifies files and directories to be ignored by Git
app.py: Main application file
appspec.yml: File that defines the deployment instructions for AWS CodeDeploy
aws_controller.py: Script that manages specific operations for AWS
buildspec.yml: File that contains build instructions for AWS CodeBuild
flaskapp.conf: Configuration file for the Flask application
flaskapp.service: Service configuration file for running the application as a service
gunicorn_config.py: Configuration script for the Gunicorn WSGI server
requirements.txt: File that lists the Python dependencies needed for the application
startapp.sh: Script to start the application
In the left navigation pane, under Repositories, choose Branches.

 Note: Notice that your application has one branch, main, which is the default branch.

Task 1.2: Review the code pipeline
In this task, you will review the CI/CD pipeline that is configured for the application.

In the left navigation pane, select Pipeline - CodePipeline, and choose Pipelines.

 Note: You can safely ignore the message that prompts you about leaving the site. There is no data to save.

In the Pipelines list, choose the name of the ApplicationPipeline.

Notice that the pipeline has three stages: source, build, and deploy.

Source: The source stage pulls the source code from the CodeCommit repository.
Build: The build stage builds and packages the code, and runs unit tests.
Deploy: The deploy stage installs the application into the application environment.
 Task complete: You reviewed the code repository and the code pipeline.

Task 2: Create the CodeBuild Project for Integration Testing
In this task, you create a dedicated CodeBuild project tailored for running the Python application’s integration tests as part of the CI/CD pipeline. Setting up a separate project allows you to define the appropriate build environment, configurations, and settings required for executing the integration test suite, ensuring proper validation of the application’s functionality across components before proceeding to subsequent pipeline stages.

At the top of the AWS Management Console, in the search bar, search for and choose CodeBuild.

In the left navigation pane, select Build and choose Build projects.

Choose Create project.

For Project name, enter IntegrationProject.

In the Source section,

For Source provider, choose AWS CodeCommit.

Fpr Repository, choose python-app-code.

For Reference type, choose Branch.

For Branch, select main from the dropdown menu.

In the Environment section,

For Service role, choose Existing service role.

For Role ARN, choose -ApplicationBuildProjectRole- .

 Note: The ApplicationBuildProjectRole Role ARN may occasionally appear truncated as ApplicationBuildProjectRo due to character limitations, but this does not affect its functionality.

In the Buildspec section, select Use a buildspec file and enter integration_buildspec.yml for Buildspec name.

Leave the remaining settings as default and choose Create build project.

You will observe the message at the top of the page that the project has been successfully created.

 Task complete: You have successfully created the IntegrationProject CodeBuild project that will be used for running the integration tests in the CI/CD pipeline.

Task 3: Add an integration test stage to the pipeline
In this task, you will extend the existing CI/CD pipeline by adding a dedicated stage for running integration tests. Integration testing is a crucial step in the software development lifecycle, ensuring that different components of the application, such as the backend Python code, HTML templates, and utility modules, work together as expected. By incorporating an integration test stage in the pipeline, you can catch potential issues early and prevent them from propagating to later stages or production environments, thereby ensuring the overall functionality and reliability of the application.

At the top of the AWS Management Console, in the search bar, search for and choose CodePipeline.

In the Pipelines list, choose the name of the ApplicationPipeline.

At the top of the page, choose Edit.

Scroll to the bottom of the page, and choose + Add Stage after the Deploy stage.

For Stage name, enter IntegrationTest.

Choose Add Stage.

Observe that a new IntegrationTest stage is in the pipeline.

 Task complete: You successfully added an integration test stage to the CI/CD pipeline. This stage acts as a checkpoint, running integration tests on the code base before proceeding to the next stage.

Task 4: Configure the integration test stage
In this task, you will configure the integration test stage by creating a CodeBuild project to execute the integration tests, specifying necessary parameters like input artifacts, build specifications, and output artifacts.

Choose + Add action group.

On the Edit action page, configure the following:

For Action name, enter Integration.

Expand this section for additional information
This step names the action in the integration test stage as Integration. For example, in the pipeline, this label helps clearly identify that this action is responsible for running the integration tests on the application code.

For Action provider, select Test/AWS CodeBuild.

Expand this section for additional information
This specifies that AWS CodeBuild will be used to perform the action. For example, selecting AWS CodeBuild ensures that the build and test process is managed by CodeBuild, which is designed to compile source code, run tests, and produce artifacts.

For Input artifacts, select SourceArtifact.

Expand this section for additional information
This step specifies that the source code and related files from the previous stage in the pipeline (usually the source stage) will be used as the input for the integration test action. For example, the SourceArtifact includes the Python application code and test scripts stored in CodeCommit, which are needed to run the integration tests.

For Project name, choose IntegrationProject from the dropdown menu.

Expand this section for additional information
This option allows you to choose the CodeBuild project created specifically for the integration test.

Scroll to the end of the page, and for Output artifacts, enter IntegrationTestOutput.

Expand this section for additional information
The purpose of entering IntegrationTestOutput for Output artifacts is to specify where the results of the integration tests will be stored. This allows the CI/CD pipeline to capture and retain the test results, logs, and any other artifacts generated during the integration test stage, enabling subsequent stages or users to review and analyze these outputs for validation and troubleshooting.

Choose Done.

Scroll to the top of the page, and choose Save.

On the Save pipeline changes page, select No resource updates needed for this source action change, and choose Save.

 Task complete: You successfully configured the integration test stage with a CodeBuild project to run integration tests defined in integration_buildspec.yml.

Task 5: Prepare the code base for integration testing in the CI/CD pipeline
In this task, you will set up the necessary components for running integration tests as part of a CI/CD pipeline. This involves cloning the repository, creating a build configuration file, adding integration test code to the project, and pushing the updated code back to the repository.

Task 5.1: Clone the repository
Copy the Cloud9Environment URL link from the Lab Information section to the left of these instructions, and paste it into a new browser tab.

 Note: The browser opens the AWS Cloud9 environment that you will use during this lab.

Close the Welcome tab, and expand the terminal session pane for more viewing area.

To open a new terminal window, select Window at the top of the screen, and choose New Terminal.

 Command: To clone the python-app-code repository, run the following command.

 Note: Replace the INSERT_REGION placeholder value with the AWSRegion value that is listed to the left of these instructions.


git clone codecommit::INSERT_REGION://python-app-code
 Expected output


Cloning into 'python-app-code'...
remote: Counting objects: 23, done.
Unpacking objects: 100% (23/23), 4.86 KiB | 382.00 KiB/s, done.
 Command: To navigate to the source code directory and create a feature branch for maintenance, enter the following command in the terminal.


cd python-app-code
 Expected output

None unless there is an error

Now that you cloned the repository, you are ready to create a build configuration file.

Task 5.2: Create a build configuration file
In the AWS Cloud9 IDE, create a new file as follows:

On the File menu, choose New File.
On the File menu, choose Save As.
Choose the python-app-code folder.
In the Filename text box, enter integration_buildspec.yml, and then choose Save.
Copy and paste the following code into the integration_buildspec.yml editor window.



version: 0.2 # Specifies the version of the buildspec file format being used

phases: # Defines the phases of the build process
  install: # The install phase where dependencies and runtime are set up
    runtime-versions: # Specifies the runtime environments needed for the build
      python: 3.12 # Indicates that Python 3.12 should be used

  pre_build: # The pre-build phase where initial setup occurs before the actual build happens
    commands: # List of commands to run in the pre-build phase
      - echo Installing dependencies... # Print a message indicating the start of dependency installation
      - pip install -r requirements.txt # Install the required Python packages listed in requirements.txt

  build: # The build phase where the actual build and tests are executed
    commands: # List of commands to run in the build phase
      - echo Building application... # Print a message indicating the start of the build process
      - echo Testing the application # Print a message indicating the start of testing
      - python -m pytest --junitxml=test_reports/integration_test_report.xml tests/test_integration.py # Run integration tests using pytest and generate a JUnit XML report

artifacts: # Specifies the files to be collected and stored as artifacts after the build
  files: # List of files to include in the artifacts
    - '**/*' # Include all files from the build
  name: tests # Name the artifacts as 'tests'
  
reports: # Defines the reports to be generated from the build
  integration_reports: # A specific report named "integration_reports"
    files: # List of files to include in the report
      - integration_test_report.xml # Include the XML file generated by pytest in the report
    base-directory: test_reports # The base directory where the report file is located
    file-format: JUNITXML # Specifies the format of the report file as JUnit XML
 Note: The integration_buildspec.yml file is used by AWS CodeBuild to set up the Python 3.12 runtime environment, install project dependencies, run integration tests using pytest, and generate a JUnit XML report for the integration test results. The generated artifacts and reports can be used in subsequent stages or actions of the AWS CodePipeline for further processing or deployment.

On the File menu, choose Save.
Now that you created a build configuration file, you are ready to explore the integration test script.

Task 5.3: Explore the integration test script
In the python-app-code root directory, navigate to the tests directory.

Open the test_integration.py file to examine its contents.

 Note: The primary purpose of this file is to verify the functionality of an application hosted on an Amazon Elastic Compute Cloud (Amazon EC2) instance through integration tests.

However, test_register_user_redirects_to_dashboard has an incorrect assertion that introduces an error, causing the integration test stage of the pipeline to fail initially.

The file consists of integration tests that make HTTP requests to the EC2 instance’s public IP address and assert the expected behavior. It includes tests for the default page, dashboard page, and user registration process. The test_register_user_redirects_to_dashboard function simulates a user registration by sending a POST request to the /register_user URL.

After the registration, the test checks if the request was redirected to the correct URL (/dashboard). However, the last assertion in this test incorrectly asserts that the final URL should be /register_user instead of /dashboard.

You must identify the intentional error in the test_register_user_redirects_to_dashboard function by examining the error message displayed in the IntegrationTest stage of the pipeline. Once the error is identified, correct the last assertion by changing the expected URL from /register_user to /dashboard. After making this correction, you can rerun the pipeline, and the integration tests should pass successfully.

Close the file.

Now that you explored the integration test script, you are ready to push code to the repository.

Task 5.4: Push code to a repository
Navigate to the terminal window.

 Command: To obtain the status of your local repository, run the following command.


git status
 Expected output


    On branch main
    Your branch is up to date with 'origin/main'.

    Untracked files:
    (use "git add <file>..." to include in what will be committed)
    integration_buildspec.yml

    nothing added to commit but untracked files present (use "git add" to track)
 Command: To stage the changes and commit them to your local repository, run the following commands.


git add -A
git commit -m "Check in integration_buildspec.yml file"
Tip:
 Expected output


    [main e98c81e] Check in integration_buildspec.yml file
    Committer: Ubuntu <ubuntu@ip-10-0-1-106.us-west-2.compute.internal>
    Your name and email address were configured automatically based
    on your username and hostname. Please check that they are accurate.
    You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

    After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

    1 file changed, 34 insertions(+)
    create mode 100644 integration_buildspec.yml
 Command: To push your changes to the python-app-code repository, run the following command.


git push
 Expected output


Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 2 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 639 bytes | 639.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Validating objects: 100%
To codecommit::us-west-2://python-app-code
03ef7c0..e98c81e main -> main
 Task complete: By cloning the repository, creating a build configuration file (integration_buildspec.yml), adding integration test code (test_integration.py) to the project, and pushing the updated code back to the repository, you have prepared the code base for running integration tests as part of a CI/CD pipeline.

Task 6: Review integration test failure and resolve issues
In this task, you will review the issues or failures uncovered during the integration tests run in the previous stage of the CI/CD pipeline. Based on the test results, you will make the necessary code changes to fix the identified issues. After making the required updates, you will push the updated code base to the repository, triggering a new pipeline execution. This will allow you to verify that the integration tests pass successfully with the fixed code.

Task 6.1: Review and fix the integration test failure
Navigate to the browser window with CodePipeline.

While the Build stage might already be in progress, allow a few minutes for the subsequent pipeline stages to complete. Monitor the code release progress through the pipeline.

Observe that the release fails the IntegrationTest stage, which is expected behavior for this step.

Choose View details.

Locate the error message in the log files. You must scroll close to the end of the page to locate the error. The error message should be similar to the one provided.



  
   =================================== FAILURES ===================================
__________________ test_register_user_redirects_to_dashboard ___________________

host_url = '34.230.38.15'
        def test_register_user_redirects_to_dashboard(host_url):
               host = get_public_ip_by_tag("EC2ApplicationServer")
    
               # make an http request to the public ip of the ec2 instance
               response = requests.post(f"http://{host}/register_user", allow_redirects=True, data={"id": str(uuid.uuid4()), "username": "XXXXXXXXXXXXX", "email": "test@anycompany.com", 
"password": "test_password"})
                if response.history:
                     print("Request was redirected")
                     for resp in response.history:
                           print(resp.status_code, resp.url)
                     print("Final destination:")
                     print(response.status_code, response.url)
                else:
                     print("Request was not redirected")
                     print(response.status_code, response.url)
                # Introduce an error by asserting an incorrect status code
                assert response.status_code == 200
    >           assert response.url == f"http://{host}/register_user"
    E           AssertionError: assert 'http://34.23....15/dashboard' == 'http://34.23...register_user' 
    E   
    E               - http://34.230.38.15/register_user
    E               + http://34.230.38.15/dashboard

tests/test_integration.py:50: AssertionError
Analyze the error message.

The error occurs in the test_register_user_redirects_to_dashboard function, specifically in the last assertion.
The assertion assert response.url == f"http://{host}/register_user" is failing.
The expected URL is http://34.230.38.15/register_user, but the actual URL is http://34.230.38.15/dashboard.
Understand the issue.

The test_register_user_redirects_to_dashboard function is intended to test the user registration process and the subsequent redirection to the /dashboard URL.
However, the last assertion is checking for an incorrect URL (/register_user) instead of the expected /dashboard URL.
Fix the error.

Open the test_integration.py file in the AWS Cloud9 IDE.
Locate the test_register_user_redirects_to_dashboard function.
In the last line, change the assertion from assert response.url == f"http://{host}/register_user" to assert response.url == f"http://{host}/dashboard"
On the File menu, choose Save.

Now that you corrected the failing test case in the test_integration.py file, you can proceed to push the updated code to the repository, triggering a new deployment pipeline.

Task 6.2: Push updated code to a repository
Navigate to the terminal window.

 Command: To obtain the status of your local repository, run the following command.


git status
 Expected output


On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git restore <file>..." to discard changes in working directory)
        modified: tests/test_integration.py

no changes added to commit (use "git add" and/or "git commit -a")
 Command: To stage the changes and commit them to your local repository, run the following commands.


git add -A
git commit -m "Check in test_integration.yml file"
 Expected output


    [main 5752f86] Check in test_integration.py file
    Committer: Ubuntu <ubuntu@ip-10-0-1-135.ec2.internal>
    Your name and email address were configured automatically based
    on your username and hostname. Please check that they are accurate.
    You can suppress this message by setting them explicitly:

        git config --global user.name "Your Name"
        git config --global user.email you@example.com

    After doing this, you may fix the identity used for this commit with:

        git commit --amend --reset-author

    1 file changed, 1 insertion(+), 1 deletion(-)
 Command: To push your changes to the python-app-code repository, run the following command.


git push
 Expected output


    Enumerating objects: 7, done.
    Counting objects: 100% (7/7), done.
    Delta compression using up to 2 threads
    Compressing objects: 100% (4/4), done.
    Writing objects: 100% (4/4), 444 bytes | 444.00 KiB/s, done.
    Total 4 (delta 2), reused 0 (delta 0), pack-reused 0
    remote: Validating objects: 100%
    To codecommit::us-east-1://python-app-code
    608374d..5752f86 main -> main
Navigate to the browser window with CodePipeline.

You can see the progress of your code release through the code pipeline.

Notice that the release now passes the IntegrationTest stage after fixing the issue.

The integration failed due to an incorrect assertion in the integration test script, where the expected URL after user registration was incorrectly set to /register_user instead of /dashboard. This error caused the integration test to fail, which is designed to validate that the application behaves correctly after deployment.

The failure occurred after the deployment stage in the pipeline because integration tests need the application to be deployed and running in its environment to verify that all components work together as expected in a real-world scenario.

After fixing the incorrect assertion in the integration test script (changing the expected URL from /register_user to /dashboard), the integration tests were rerun. This time, the tests passed successfully, indicating that the application correctly redirects to the /dashboard URL after user registration. As a result, the integration test stage in the CI/CD pipeline completed without errors, validating that the deployed application components functioned as intended.

 Task complete: You successfully reviewed integration test results, fixed identified issues in the code base, pushed updates, and verified successful integration test execution through the CI/CD pipeline.

Task 7: View the application
In this task, you will directly interact with the application deployed through the CI/CD pipeline to observe its functionality and frontend interface. This hands-on experience allows you to understand how the various components, such as the backend Python code, HTML templates, and utility modules, work together to deliver the expected behavior and user experience.

In the AWS Management Console, in the search bar, search for and choose EC2.

In the left navigation pane, choose Instances.

Select the instance with the Name tag EC2ApplicationServer.

On the Details tab, copy the Public IPv4 DNS address of the selected instance.

Open a new browser tab or window, and enter the copied public IP address in the address bar to display the Register User webpage.

Explore the application by entering a Username, Email, and Password, and choose Submit.

 Note: The email does not have to be a valid email address.

You will be redirected to the Users dashboard with more information on user ID, email, username, and passwords.

Observing the application running and interacting with its user interface helps you to understand how the different components of the code base work together to deliver the intended functionality. This experience ties the coding and testing efforts to a more tangible and practical outcome, reinforcing the importance of thorough integration testing in the CI/CD pipeline.

Close the webpage.

 Task complete: You successfully accessed and interacted with the deployed application, gaining a more comprehensive understanding of how the code base components work together to provide the expected user experience and functionality.

Conclusion
 Congratulations! You successfully completed the following:

Gained an overview of the CI/CD pipeline and its components.
Added an integration test stage to an existing AWS CodePipeline.
Configured an integration test stage with a CodeBuild project for running tests.
Prepared a code base for integration testing in the CI/CD pipeline.
Reviewed integration test failure and resolved issues.
Directly interacted with an application deployed through the CI/CD pipeline to observe its functionality and frontend interface.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.
