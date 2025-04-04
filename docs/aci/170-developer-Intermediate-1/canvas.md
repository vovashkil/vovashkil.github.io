# Canvas - Development Intermediate 1

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)
* back to [Developer Intermediate 1 main page](./developer-intermediate-1.md)

## Welcome to AWS Cloud Institute

Instructor(s) Information

Fernando Teixeira
<teiferna@amazon.com>

## Additional Resources, Links, Diagrams, Examples

### Demo Companion Guide for weeks 8, 9, 10, 11

This document describes steps used in the demos provided in the second part of the course. Although this has a similar format to the guide provide for the "Pet App" example in the first part of the course, there is one critical difference. The "Pet App" application could be run in the standard practice environment, so learners have an environment available to execute these steps. The second part of the course involves multiple AWS service, and the practice environment does not support that. The practice environment exists to practice Python, and it's not feasible to have an environment indefinitely opened with multiple AWS services provisioned. The official module Labs are the official place for learners to practice with AWS services.

Given that, the **guide below is meant as documentation of what will be shown in class demos. There is no ACI Lab environment explicitly created to execute them**, which is normal for an instructor demo. The steps are shown here, primarily so that learners can follow along, and review later. There is no expectation that learners would execute these demos on their own.

* [TuckerMoviesDemo-v6.docx](./canvas_files/TuckerMoviesDemo-v6.docx)

### Week  9

* This ZIP file has the Jupyter notebooks created for SQS. 
  * [sqs.zip](./canvas_files/sqs.zip)
* This ZIP file has the Lambda functions for the end-end-end Tucker Movies SNS/SQS demo
  * [add_movie_flow.zip](./canvas_files/add_movie_flow.zip)

### Week  8

* This ZIP file has all of the examples for DynamoDB I demoed today (plus a couple extra ones).
  * [dynamodb_demos.zip](./canvas_files/dynamodb_demos.zip)
* For each Notebook example, I'm sharing two files:
  * The *Jupyter Notebook version* with all the formatting. That's the file with the "*.ipynb*" extension.
    * This can only be viewed and/or executed in an environment that supports Jupyter Notebooks.
  * The equivalent *Python version*. That's the file with the ".py" extension.
    * This is plain Python code that can run in any normal Python environment
    * The formatted content becomes regular Python comments in this version

### Weeks 4, 5, 6 and 7

#### Demo Companion Guide to the eLearning Pet App examples

Based on popular request, I'm sharing my own personal step-by-step demo for creating the Pet App used in the eLearning examples. These are the steps I'm using as I walk through the modules in the live sessions.

As I explained in session, this is not an official ACI training material, and **does NOT replace** the very good explanations eLearning has on the Django concepts.  In fact, my demo code samples are 95% copied from the text boxes provided in the **eLearning** material, and all of the demos are explicitly mapped to the eLearning section they belong to. I simply streamlined it to include only those steps needed to get the project working, in the correct order.

I will update this file with new versions, as I complete each module walk through during our live sessions.

* [DjangoPetShopDemo-v10.docx](./canvas_files/DjangoPetShopDemo-v10.docx)
* The following archive contains the static files (images and css) used in some of the week 5 examples:
  * [static.zip](./canvas_files/static.zip)
* This file is a backup of full versions of the pets project. You should be able to use this file to recover an environment following the instructions in Appendix 5 of the companion guide. Please note that I add a "-p1" or "-p2" at the end of the file name, to differentiate between different snapshots of the project at different times. But when you run the steps in Appendix 5, the need to be renamed to plain pets_project.zip 
  * [pets_project-p1.zip](./canvas_files/pets_project-p1.zip) - This is the project at the end of Week 5, when we only had the basic list view
  * [pets_project-p2.zip](./canvas_files/pets_project-p2.zip) - This is the final version of the project at the beginning of Week 6

### Week 3

#### Links to resources shared in session

* Resources for JavaScript syntax and basic examples:
  * [https://www.w3schools.com/js/](https://www.w3schools.com/js/)

#### Demo files

ZIP file with progressive demos:

* [week3.zip](./canvas_files/week3.zip)

### Week 2

#### Links to resources shared in session

* Resources for CSS syntax and basic examples:
  * [https://developer.mozilla.org/en-US/docs/Web/HTML](https://developer.mozilla.org/en-US/docs/Web/CSS)
  * [https://www.w3schools.com/Html/](https://www.w3schools.com/css/default.asp)

#### Demo files

ZIP file with demos (open README file in top folder for important information):

* [week2.zip](./canvas_files/week2.zip)

### Week 1

#### Links to resources shared in session

* Resources for HTML tag syntax and basic examples:
  * [https://developer.mozilla.org/en-US/docs/Web/HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
  * [https://www.w3.org/TR/2012/WD-html-markup-20121025/elements.html](https://www.w3.org/TR/2012/WD-html-markup-20121025/elements.html)
  * [https://www.w3schools.com/Html/](https://www.w3schools.com/Html/)
* Validating HTML code:
  * [https://validator.w3.org/](https://validator.w3.org/)
* AI Code Generation:
  * [https://partyrock.aws/](https://partyrock.aws/)

#### Demo files

* ZIP file with week 1 demos: [week1-demos.zip](./canvas_files/week1-demos.zip)

### Capstone Resources

#### Introduction to AWS SDK

This is the Notebook I shared with a simple example of how to use the AWS Python SDK (boto).

* Jupyter Notebook version with all the formatting: [S3_List_Objects.ipynb](./canvas_files/S3_List_Objects.ipynb)
* Python version: [S3_List_Objects.py](./canvas_files/S3_List_Objects.py)
* PDF version for viewing only: [S3_List_Objects.pdf](./canvas_files/S3_List_Objects.pdf)

#### Jupyter Notebook information

* [https://jupyter.org/](https://jupyter.org/) - The official Jupyter site. You can download and run Jupyter Lab (that's what you see me using) from the site. That's free open source software. This is not an AWS product, so I don't want to get into installation steps, but you can see everything on their site.
* [https://jupyter.org/try-jupyter/lab/](https://jupyter.org/try-jupyter/lab/) - This is a free simple online version of Jupyter Notebooks, available inside the [Jupyter.org](http://jupyter.org/) site. I haven't played around with it much, but it seems to work for most notebooks I've tried.
* [https://studiolab.sagemaker.aws/](https://studiolab.sagemaker.aws/) - SageMaker Studio Lab, which is an Amazon supported Jupyter Lab environment in the Cloud. This is currently free for anyone (no credit card required). Check the website for registration and all details
* Others - Multiple IDEs, including VS Code, will support Jupyter Notebooks
