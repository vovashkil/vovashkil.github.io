# Introduction to AWS Cloud Development Kit

## Lab overview

In this lab, you create a virtual private cloud (VPC) and add an Amazon Elastic Compute Cloud (Amazon EC2) instance with AWS Systems Manager enabled using AWS Cloud Development Kit (AWS CDK).

Objectives
In this lab, you do the following:

Create a directory and its resources.
Create the VPC and EC2 instance.
Review the resources created.
Clean up the environment.
Prerequisites
You should be familiar with the command line terminal and basic navigation of the AWS Management Console.
All coding is done from within an AWS Cloud9 environment. No prerequisites are necessary.
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
Lab Environment
AWS CDK
With AWS Cloud Development Kit (AWS CDK), you can build reliable, scalable, cost-effective applications in the cloud. AWS CDK supports TypeScript, JavaScript, Python, Java, C# for .Net, and Go. Developers can use one of these supported programming languages to define reusable cloud components known as constructs. You compose these together into stacks and apps.

 Additional information: For more information, see AWS Cloud Development Kit Documentation.

Task 1: Connect to and prepare your development environment
In this task, you connect to the AWS Cloud9 integrated development environment, and upgrade/install the required packages to work with AWS CDK in Python.

Task 1.1: Connect to the AWS Cloud9 IDE
Connect to your development environment.

On the AWS Management Console, in the  search box, search for and choose Cloud9.

On the Environments page, choose the Cloud9-Lab-IDE environment link.

When the AWS Cloud9 integrated development environment (IDE) is in the ready state, choose the Open in Cloud9 button.

Task 1.2: Installing the Python package installer
Install the Python package installer, pip, and virtual environment manager, virtualenv, which are all required to work with AWS CDK in Python.

To upgrade all packages, run the following command:

sudo dnf upgrade -y
 NOTE: For the purposes of this lab, there is no need to upgrade to a newer version of Amazon Linux.

To manually install pip and virtalenv, run the following commands:

python3 -m pip install --upgrade pip
python3 -m pip install --upgrade virtualenv
 Expected output: From the python3 -m pip install --upgrade pip command you should receive the successfully installed latest pip version number.

 Expected output: From the python3 -m pip install --upgrade virtualenv command you should receive the successfully installed latest virtualenv version number.

 Congratulations! You have successfully installed the Python package installer.

Task 2: Creating a project
In this task, you create a new AWS CDK project by invoking the cdk init command.

To create the empty directory, run the following commands:

    mkdir ec2-instance
    cd ec2-instance
    cdk init app --language python
 Expected output:


Initializing a new git repository...
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint: 
hint:   git config --global init.defaultBranch <name>
hint: 
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint: 
hint:   git branch -m <name>
Please run 'python3 -m venv .venv'!
Executing Creating virtualenv...
 All done!
 Note: The cdk init command uses the name of the project folder to name various elements of the project, including classes, subfolders, and files.

To activate the virtual environment, run the following command:

    source .venv/bin/activate
 Expected output: None

Run this command to update the branch name to the following:

    git branch -m main
To ensure that the branch name is changed by listing the current branches in your repository, run this code:

    git branch
 Expected output: You see the main branch listed in your repo.

This permits the project’s dependencies to be installed locally in the project folder, instead of globally.

Install the app’s standard dependencies by running the following command:

    python3 -m pip install -r requirements.txt
Task 3: Using AWS CDK to create the VPC and EC2 instance
In this task, you use AWS CDK to create the VPC and EC2 instance.

In the left pane of the AWS Cloud9 terminal, expand the > ec2-instance folder. Then expand the > ec2_instance folder under it, and double-click to open the ec2_instance_stack.py file.

Delete any existing code, copy and paste the following code in the ec2_instance_stack.py file:


```
import os.path

from aws_cdk.aws_s3_assets import Asset

from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    App, Stack
)

from constructs import Construct

dirname = os.path.dirname(__file__)


class Ec2InstanceStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        # create a new VPC
        vpc = ec2.Vpc(self, "Vpc", ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16"),
            nat_gateways=0,
            restrict_default_security_group=False,
            subnet_configuration=[ec2.SubnetConfiguration(name="public",subnet_type=ec2.SubnetType.PUBLIC)]
        )

        role = iam.Role.from_role_arn(self, "LabInstanceRole", f"arn:aws:iam::{Stack.of(self).account}:role/LabInstanceRole")

        # AMI
        amzn_linux = ec2.MachineImage.latest_amazon_linux2023(
            edition=ec2.AmazonLinuxEdition.STANDARD,
            )

        # Instance
        instance = ec2.Instance(self, "Instance",
            instance_type=ec2.InstanceType("t3.nano"),
            machine_image=amzn_linux,
            vpc = vpc,
            role = role
            )

app = App()
Ec2InstanceStack(app, "ec2-instance")

app.synth()
```

Navigate to the AWS Cloud9 toolbar and choose File > Save to apply the changes.

To initialize assets before they deploy, run the bootstrap command:

```
cdk bootstrap --template ../customized-bootstrap-template.yaml
```

Ouput:

```
(.venv) AWSLabsUser-6XL2PwCRUatMC74Agawqsi:~/environment/ec2-instance (main) $ cdk bootstrap --template ../customized-bootstrap-template.yaml
Using bootstrapping template from ../customized-bootstrap-template.yaml
 ⏳  Bootstrapping environment aws://747856204391/us-east-1...
Trusted accounts for deployment: (none)
Trusted accounts for lookup: (none)
Using default execution policy of 'arn:aws:iam::aws:policy/AdministratorAccess'. Pass '--cloudformation-execution-policies' to customize.
CDKToolkit: creating CloudFormation changeset...
CDKToolkit | 0/2 | 9:44:37 PM | REVIEW_IN_PROGRESS   | AWS::CloudFormation::Stack | CDKToolkit User Initiated
CDKToolkit | 0/2 | 9:44:43 PM | CREATE_IN_PROGRESS   | AWS::CloudFormation::Stack | CDKToolkit User Initiated
CDKToolkit | 0/2 | 9:44:45 PM | CREATE_IN_PROGRESS   | AWS::SSM::Parameter | CdkBootstrapVersion 
CDKToolkit | 0/2 | 9:44:46 PM | CREATE_IN_PROGRESS   | AWS::SSM::Parameter | CdkBootstrapVersion Resource creation Initiated
CDKToolkit | 1/2 | 9:44:47 PM | CREATE_COMPLETE      | AWS::SSM::Parameter | CdkBootstrapVersion 
CDKToolkit | 2/2 | 9:44:48 PM | CREATE_COMPLETE      | AWS::CloudFormation::Stack | CDKToolkit 
 ✅  Environment aws://747856204391/us-east-1 bootstrapped.
```


 Note: In AWS CDK V2, the default bootstrap template and synthesizer create and use resources including S3 buckets and highly privileged IAM roles. For the sake of this lab, the resource creation has already been done, and using a custom bootstrap template, your CDK configuration becomes aware of these resources.

To open the stack instantiation file, from ec2_instance, select (double-click) app.py.

To create a synthesizer object that uses the bootstrap resources and pass it to your stack object, replace the contents of the file with the following:

```
# Import the core AWS CDK module and the DefaultStackSynthesizer class
import aws_cdk as cdk
from aws_cdk import DefaultStackSynthesizer
# Import the Ec2InstanceStack class from your stack definition module
from ec2_instance.ec2_instance_stack import Ec2InstanceStack

# Create a new CDK application instance
app = cdk.App()

# Instantiate your stack and configure it to use a custom synthesizer
Ec2InstanceStack(app, "Ec2InstanceStack", 
    synthesizer=DefaultStackSynthesizer(
        # A unique identifier to differentiate resources created by this synthesizer
        qualifier="cdk8487",
        # Name of the repository for storing Docker images used in the application
        image_assets_repository_name="cdk-staging-assets-repository",
        # IAM role ARN used for looking up existing resources during the deployment
        lookup_role_arn="arn:aws:iam::${AWS::AccountId}:role/CDK-LabStack-Lookup-Role",
        # Name of the S3 bucket used for storing file assets (like Lambda function code)
        file_assets_bucket_name="cdk-staging-bucket-${AWS::AccountId}-${AWS::Region}",
        # IAM role ARN used for deploying resources defined in the stack
        deploy_role_arn="arn:aws:iam::${AWS::AccountId}:role/CDK-LabStack-Deploy-Role",
        # Optional external ID used for assuming the deploy role (not used here)
        deploy_role_external_id="",
        # IAM role ARN used for publishing file assets to the S3 bucket
        file_asset_publishing_role_arn="arn:aws:iam::${AWS::AccountId}:role/CDK-LabStack-File-Publishing-Role",
        # Optional external ID used for assuming the file asset publishing role (not used here)
        file_asset_publishing_external_id="",
        # IAM role ARN used for publishing Docker images to the repository
        image_asset_publishing_role_arn="arn:aws:iam::${AWS::AccountId}:role/CDK-LabStack-Image-Publishing-Role",
        # Optional external ID used for assuming the image asset publishing role (not used here)
        image_asset_publishing_external_id="",
        # IAM role ARN used for executing CloudFormation during the deployment
        cloud_formation_execution_role="arn:aws:iam::${AWS::AccountId}:role/CDK-LabStack-CFN-Execution-Role",
        # SSM parameter used to track the version of the bootstrap stack
        bootstrap_stack_version_ssm_parameter="/cdk-bootstrap/${Qualifier}/version",
        # Ensure that the synthesizer generates a rule to check for the correct bootstrap version
        generate_bootstrap_version_rule=True
    ))
# Synthesize the CloudFormation template for the CDK application
app.synth()
```

 Note: For this special use case, you must edit app.py to include the custom Synthesizer because the Bootstrap resources were already created. Typically, you can rely on the default synthesizer, but many use cases require a custom one.

Navigate to the AWS Cloud9 toolbar and choose File > Save to apply the changes.

In the terminal, to run the app and note that it synthesizes an empty stack, run this code:

```
cdk synth
```

Output:

```
Resources:
  Vpc8378EB38:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsHostnames: true
      EnableDnsSupport: true
      InstanceTenancy: default
      Tags:
        - Key: Name
          Value: Ec2InstanceStack/Vpc
    Metadata:
      aws:cdk:path: Ec2InstanceStack/Vpc/Resource
  VpcpublicSubnet1Subnet2BB74ED7:
    Type: AWS::EC2::Subnet
    Properties:
      AvailabilityZone:
        Fn::Select:
          - 0
          - Fn::GetAZs: ""
      CidrBlock: 10.0.0.0/17
      MapPublicIpOnLaunch: true
      Tags:
        - Key: aws-cdk:subnet-name
          Value: public
        - Key: aws-cdk:subnet-type
          Value: Public
        - Key: Name
          Value: Ec2InstanceStack/Vpc/publicSubnet1
      VpcId:
        Ref: Vpc8378EB38
    Metadata:
      aws:cdk:path: Ec2InstanceStack/Vpc/publicSubnet1/Subnet
  VpcpublicSubnet1RouteTable15C15F8E:
    Type: AWS::EC2::RouteTable
    Properties:
      Tags:
        - Key: Name
          Value: Ec2InstanceStack/Vpc/publicSubnet1
      VpcId:
        Ref: Vpc8378EB38
    Metadata:
      aws:cdk:path: Ec2InstanceStack/Vpc/publicSubnet1/RouteTable
  VpcpublicSubnet1RouteTableAssociation4E83B6E4:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId:
        Ref: VpcpublicSubnet1RouteTable15C15F8E
      SubnetId:
        Ref: VpcpublicSubnet1Subnet2BB74ED7
    Metadata:
      aws:cdk:path: Ec2InstanceStack/Vpc/publicSubnet1/RouteTableAssociation
  VpcpublicSubnet1DefaultRouteB88F9E93:
    Type: AWS::EC2::Route
    Properties:
      DestinationCidrBlock: 0.0.0.0/0
      GatewayId:
        Ref: VpcIGWD7BA715C
      RouteTableId:
        Ref: VpcpublicSubnet1RouteTable15C15F8E
    DependsOn:
      - VpcVPCGWBF912B6E
    Metadata:
      aws:cdk:path: Ec2InstanceStack/Vpc/publicSubnet1/DefaultRoute
  VpcpublicSubnet2SubnetE34B022A:
    Type: AWS::EC2::Subnet
    Properties:
      AvailabilityZone:
        Fn::Select:
          - 1
          - Fn::GetAZs: ""
      CidrBlock: 10.0.128.0/17
      MapPublicIpOnLaunch: true
      Tags:
        - Key: aws-cdk:subnet-name
          Value: public
        - Key: aws-cdk:subnet-type
          Value: Public
        - Key: Name
          Value: Ec2InstanceStack/Vpc/publicSubnet2
      VpcId:
        Ref: Vpc8378EB38
    Metadata:
      aws:cdk:path: Ec2InstanceStack/Vpc/publicSubnet2/Subnet
  VpcpublicSubnet2RouteTableC5A6DF77:
    Type: AWS::EC2::RouteTable
    Properties:
      Tags:
        - Key: Name
          Value: Ec2InstanceStack/Vpc/publicSubnet2
      VpcId:
        Ref: Vpc8378EB38
    Metadata:
      aws:cdk:path: Ec2InstanceStack/Vpc/publicSubnet2/RouteTable
  VpcpublicSubnet2RouteTableAssociationCCE257FF:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId:
        Ref: VpcpublicSubnet2RouteTableC5A6DF77
      SubnetId:
        Ref: VpcpublicSubnet2SubnetE34B022A
    Metadata:
      aws:cdk:path: Ec2InstanceStack/Vpc/publicSubnet2/RouteTableAssociation
  VpcpublicSubnet2DefaultRoute732F0BEB:
    Type: AWS::EC2::Route
    Properties:
      DestinationCidrBlock: 0.0.0.0/0
      GatewayId:
        Ref: VpcIGWD7BA715C
      RouteTableId:
        Ref: VpcpublicSubnet2RouteTableC5A6DF77
    DependsOn:
      - VpcVPCGWBF912B6E
    Metadata:
      aws:cdk:path: Ec2InstanceStack/Vpc/publicSubnet2/DefaultRoute
  VpcIGWD7BA715C:
    Type: AWS::EC2::InternetGateway
    Properties:
      Tags:
        - Key: Name
          Value: Ec2InstanceStack/Vpc
    Metadata:
      aws:cdk:path: Ec2InstanceStack/Vpc/IGW
  VpcVPCGWBF912B6E:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      InternetGatewayId:
        Ref: VpcIGWD7BA715C
      VpcId:
        Ref: Vpc8378EB38
    Metadata:
      aws:cdk:path: Ec2InstanceStack/Vpc/VPCGW
  InstanceInstanceSecurityGroupF0E2D5BE:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Ec2InstanceStack/Instance/InstanceSecurityGroup
      SecurityGroupEgress:
        - CidrIp: 0.0.0.0/0
          Description: Allow all outbound traffic by default
          IpProtocol: "-1"
      Tags:
        - Key: Name
          Value: Ec2InstanceStack/Instance
      VpcId:
        Ref: Vpc8378EB38
    Metadata:
      aws:cdk:path: Ec2InstanceStack/Instance/InstanceSecurityGroup/Resource
  InstanceInstanceProfileAB5AEF02:
    Type: AWS::IAM::InstanceProfile
    Properties:
      Roles:
        - LabInstanceRole
    Metadata:
      aws:cdk:path: Ec2InstanceStack/Instance/InstanceProfile
  InstanceC1063A87:
    Type: AWS::EC2::Instance
    Properties:
      AvailabilityZone:
        Fn::Select:
          - 0
          - Fn::GetAZs: ""
      IamInstanceProfile:
        Ref: InstanceInstanceProfileAB5AEF02
      ImageId:
        Ref: SsmParameterValueawsserviceamiamazonlinuxlatestal2023amikernel61x8664C96584B6F00A464EAD1953AFF4B05118Parameter
      InstanceType: t3.nano
      SecurityGroupIds:
        - Fn::GetAtt:
            - InstanceInstanceSecurityGroupF0E2D5BE
            - GroupId
      SubnetId:
        Ref: VpcpublicSubnet1Subnet2BB74ED7
      Tags:
        - Key: Name
          Value: Ec2InstanceStack/Instance
      UserData:
        Fn::Base64: "#!/bin/bash"
    Metadata:
      aws:cdk:path: Ec2InstanceStack/Instance/Resource
  CDKMetadata:
    Type: AWS::CDK::Metadata
    Properties:
      Analytics: v2:deflate64:H4sIAAAAAAAA/12OwW7CMAyGn4V7mm3lMO2IekDcohZxnVxjhEfroMQRqirefWnHVrSTf3/+JX+lfXtf23IFt1jg8VJ03NqxUcCLyehzJCzteLiiqU5ycJVxqe0Ym9QK6cSWVPuktIe2o4UvbBOjRwZlL3/lKexEKeTmFpRuMDzePLaNZpFzT6JmJ1FBkExDmALrsA0+XedP/8Fv9W4YevsEXPAn7jKvKfoUcBZwEKCnLDFrPR0qL0eefO/GDXr28rK2H7Z8XX1F5iIkUe7J1j/zG1xYSmxHAQAA
    Metadata:
      aws:cdk:path: Ec2InstanceStack/CDKMetadata/Default
    Condition: CDKMetadataAvailable
Parameters:
  SsmParameterValueawsserviceamiamazonlinuxlatestal2023amikernel61x8664C96584B6F00A464EAD1953AFF4B05118Parameter:
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64
  BootstrapVersion:
    Type: AWS::SSM::Parameter::Value<String>
    Default: /cdk-bootstrap/cdk8487/version
    Description: Version of the CDK Bootstrap resources in this environment, automatically retrieved from SSM Parameter Store. [cdk:skip]
Conditions:
  CDKMetadataAvailable:
    Fn::Or:
      - Fn::Or:
          - Fn::Equals:
              - Ref: AWS::Region
              - af-south-1
          - Fn::Equals:
              - Ref: AWS::Region
              - ap-east-1
          - Fn::Equals:
              - Ref: AWS::Region
              - ap-northeast-1
          - Fn::Equals:
              - Ref: AWS::Region
              - ap-northeast-2
          - Fn::Equals:
              - Ref: AWS::Region
              - ap-northeast-3
          - Fn::Equals:
              - Ref: AWS::Region
              - ap-south-1
          - Fn::Equals:
              - Ref: AWS::Region
              - ap-south-2
          - Fn::Equals:
              - Ref: AWS::Region
              - ap-southeast-1
          - Fn::Equals:
              - Ref: AWS::Region
              - ap-southeast-2
          - Fn::Equals:
              - Ref: AWS::Region
              - ap-southeast-3
      - Fn::Or:
          - Fn::Equals:
              - Ref: AWS::Region
              - ap-southeast-4
          - Fn::Equals:
              - Ref: AWS::Region
              - ca-central-1
          - Fn::Equals:
              - Ref: AWS::Region
              - ca-west-1
          - Fn::Equals:
              - Ref: AWS::Region
              - cn-north-1
          - Fn::Equals:
              - Ref: AWS::Region
              - cn-northwest-1
          - Fn::Equals:
              - Ref: AWS::Region
              - eu-central-1
          - Fn::Equals:
              - Ref: AWS::Region
              - eu-central-2
          - Fn::Equals:
              - Ref: AWS::Region
              - eu-north-1
          - Fn::Equals:
              - Ref: AWS::Region
              - eu-south-1
          - Fn::Equals:
              - Ref: AWS::Region
              - eu-south-2
      - Fn::Or:
          - Fn::Equals:
              - Ref: AWS::Region
              - eu-west-1
          - Fn::Equals:
              - Ref: AWS::Region
              - eu-west-2
          - Fn::Equals:
              - Ref: AWS::Region
              - eu-west-3
          - Fn::Equals:
              - Ref: AWS::Region
              - il-central-1
          - Fn::Equals:
              - Ref: AWS::Region
              - me-central-1
          - Fn::Equals:
              - Ref: AWS::Region
              - me-south-1
          - Fn::Equals:
              - Ref: AWS::Region
              - sa-east-1
          - Fn::Equals:
              - Ref: AWS::Region
              - us-east-1
          - Fn::Equals:
              - Ref: AWS::Region
              - us-east-2
          - Fn::Equals:
              - Ref: AWS::Region
              - us-west-1
      - Fn::Equals:
          - Ref: AWS::Region
          - us-west-2

```

 Note: The cdk synth command runs your app, which causes the resources defined in it to be translated into an AWS CloudFormation template.

To deploy the stack, run the following command. The cdk deploy command displays progress information as your stack is deployed. When it’s finished, the command prompt reappears.

```
cdk deploy
```

When the “Do you wish to deploy these changes (y/n)?” prompt appears, enter y.
 Note: This might take a few minutes to deploy.

 Expected output: You should see an output like the following:


Ec2InstanceStack: deploying... [1/1]
Ec2InstanceStack: creating CloudFormation changeset...

 ✅  Ec2InstanceStack

✨  Deployment time: 169.01s

Stack ARN:
arn:aws:cloudformation:us-west-2:155219894957:stack/Ec2InstanceStack/1f9993a0-3548-11ee-ba16-02f16785d2ef

✨  Total time: 177.01s
 Note: The following commands are used with AWS CDK:

cdk deploy - This command deploys this stack to your default AWS account/region.
cdk diff - This command compares a deployed stack with the current state of your stack.
cdk synth - This command emits the synthesized CloudFormation template.
cdk bootstrap - This command initializes assets before they deploy.
aws ssm start-session --target i-xxxxxxxxx - This command starts the remote session for shell access.
 Congratulations! You have successfully used AWS CDK to create a VPC and EC2 instance.

```

✨  Synthesis time: 10.89s

current credentials could not be used to assume 'arn:aws:iam::747856204391:role/CDK-LabStack-Deploy-Role', but are for the right account. Proceeding anyway.
Ec2InstanceStack: start: Building ade2ff9badb1fd9bc95ca9b6ad5f9f2a6cb00763ad120ea85e2440dcb578941f:current_account-current_region
Ec2InstanceStack: success: Built ade2ff9badb1fd9bc95ca9b6ad5f9f2a6cb00763ad120ea85e2440dcb578941f:current_account-current_region
Ec2InstanceStack: start: Publishing ade2ff9badb1fd9bc95ca9b6ad5f9f2a6cb00763ad120ea85e2440dcb578941f:current_account-current_region
current credentials could not be used to assume 'arn:aws:iam::747856204391:role/CDK-LabStack-File-Publishing-Role', but are for the right account. Proceeding anyway.
Ec2InstanceStack: success: Published ade2ff9badb1fd9bc95ca9b6ad5f9f2a6cb00763ad120ea85e2440dcb578941f:current_account-current_region
current credentials could not be used to assume 'arn:aws:iam::747856204391:role/CDK-LabStack-Lookup-Role', but are for the right account. Proceeding anyway.
Lookup role arn:aws:iam::747856204391:role/CDK-LabStack-Lookup-Role was not assumed. Proceeding with default credentials.
Stack undefined
This deployment will make potentially sensitive changes according to your current security approval level (--require-approval broadening).
Please confirm you intend to make the following modifications:

Security Group Changes
┌───┬───────────────────────────────────────────┬─────┬────────────┬─────────────────┐
│   │ Group                                     │ Dir │ Protocol   │ Peer            │
├───┼───────────────────────────────────────────┼─────┼────────────┼─────────────────┤
│ + │ ${Instance/InstanceSecurityGroup.GroupId} │ Out │ Everything │ Everyone (IPv4) │
└───┴───────────────────────────────────────────┴─────┴────────────┴─────────────────┘
(NOTE: There may be security-related changes not in this list. See https://github.com/aws/aws-cdk/issues/1299)

Do you wish to deploy these changes (y/n)? y
Ec2InstanceStack: deploying... [1/1]
current credentials could not be used to assume 'arn:aws:iam::747856204391:role/CDK-LabStack-Deploy-Role', but are for the right account. Proceeding anyway.
Ec2InstanceStack: creating CloudFormation changeset...
Ec2InstanceStack |  0/16 | 9:51:37 PM | REVIEW_IN_PROGRESS   | AWS::CloudFormation::Stack            | Ec2InstanceStack User Initiated
Ec2InstanceStack |  0/16 | 9:51:43 PM | CREATE_IN_PROGRESS   | AWS::CloudFormation::Stack            | Ec2InstanceStack User Initiated
Ec2InstanceStack |  0/16 | 9:51:45 PM | CREATE_IN_PROGRESS   | AWS::IAM::InstanceProfile             | Instance/InstanceProfile (InstanceInstanceProfileAB5AEF02) 
Ec2InstanceStack |  0/16 | 9:51:45 PM | CREATE_IN_PROGRESS   | AWS::EC2::VPC                         | Vpc (Vpc8378EB38) 
Ec2InstanceStack |  0/16 | 9:51:45 PM | CREATE_IN_PROGRESS   | AWS::EC2::InternetGateway             | Vpc/IGW (VpcIGWD7BA715C) 
Ec2InstanceStack |  0/16 | 9:51:45 PM | CREATE_IN_PROGRESS   | AWS::CDK::Metadata                    | CDKMetadata/Default (CDKMetadata) 
Ec2InstanceStack |  0/16 | 9:51:46 PM | CREATE_IN_PROGRESS   | AWS::CDK::Metadata                    | CDKMetadata/Default (CDKMetadata) Resource creation Initiated
Ec2InstanceStack |  0/16 | 9:51:46 PM | CREATE_IN_PROGRESS   | AWS::IAM::InstanceProfile             | Instance/InstanceProfile (InstanceInstanceProfileAB5AEF02) Resource creation Initiated
Ec2InstanceStack |  0/16 | 9:51:46 PM | CREATE_IN_PROGRESS   | AWS::EC2::InternetGateway             | Vpc/IGW (VpcIGWD7BA715C) Resource creation Initiated
Ec2InstanceStack |  1/16 | 9:51:46 PM | CREATE_COMPLETE      | AWS::CDK::Metadata                    | CDKMetadata/Default (CDKMetadata) 
Ec2InstanceStack |  1/16 | 9:51:47 PM | CREATE_IN_PROGRESS   | AWS::EC2::VPC                         | Vpc (Vpc8378EB38) Resource creation Initiated
Ec2InstanceStack |  1/16 | 9:51:47 PM | CREATE_IN_PROGRESS   | AWS::IAM::InstanceProfile             | Instance/InstanceProfile (InstanceInstanceProfileAB5AEF02) Eventual consistency check initiated
Ec2InstanceStack |  1/16 | 9:51:47 PM | CREATE_IN_PROGRESS   | AWS::EC2::InternetGateway             | Vpc/IGW (VpcIGWD7BA715C) Eventual consistency check initiated
Ec2InstanceStack |  2/16 | 9:51:57 PM | CREATE_COMPLETE      | AWS::EC2::VPC                         | Vpc (Vpc8378EB38) 
Ec2InstanceStack |  2/16 | 9:51:58 PM | CREATE_IN_PROGRESS   | AWS::EC2::RouteTable                  | Vpc/publicSubnet1/RouteTable (VpcpublicSubnet1RouteTable15C15F8E) 
Ec2InstanceStack |  2/16 | 9:51:58 PM | CREATE_IN_PROGRESS   | AWS::EC2::RouteTable                  | Vpc/publicSubnet2/RouteTable (VpcpublicSubnet2RouteTableC5A6DF77) 
Ec2InstanceStack |  2/16 | 9:51:58 PM | CREATE_IN_PROGRESS   | AWS::EC2::VPCGatewayAttachment        | Vpc/VPCGW (VpcVPCGWBF912B6E) 
Ec2InstanceStack |  2/16 | 9:51:58 PM | CREATE_IN_PROGRESS   | AWS::EC2::Subnet                      | Vpc/publicSubnet2/Subnet (VpcpublicSubnet2SubnetE34B022A) 
Ec2InstanceStack |  2/16 | 9:51:58 PM | CREATE_IN_PROGRESS   | AWS::EC2::SecurityGroup               | Instance/InstanceSecurityGroup (InstanceInstanceSecurityGroupF0E2D5BE) 
Ec2InstanceStack |  2/16 | 9:51:58 PM | CREATE_IN_PROGRESS   | AWS::EC2::Subnet                      | Vpc/publicSubnet1/Subnet (VpcpublicSubnet1Subnet2BB74ED7) 
Ec2InstanceStack |  2/16 | 9:51:59 PM | CREATE_IN_PROGRESS   | AWS::EC2::VPCGatewayAttachment        | Vpc/VPCGW (VpcVPCGWBF912B6E) Resource creation Initiated
Ec2InstanceStack |  2/16 | 9:51:59 PM | CREATE_IN_PROGRESS   | AWS::EC2::RouteTable                  | Vpc/publicSubnet2/RouteTable (VpcpublicSubnet2RouteTableC5A6DF77) Resource creation Initiated
Ec2InstanceStack |  2/16 | 9:51:59 PM | CREATE_IN_PROGRESS   | AWS::EC2::RouteTable                  | Vpc/publicSubnet1/RouteTable (VpcpublicSubnet1RouteTable15C15F8E) Resource creation Initiated
Ec2InstanceStack |  2/16 | 9:51:59 PM | CREATE_IN_PROGRESS   | AWS::EC2::Subnet                      | Vpc/publicSubnet1/Subnet (VpcpublicSubnet1Subnet2BB74ED7) Resource creation Initiated
Ec2InstanceStack |  2/16 | 9:51:59 PM | CREATE_IN_PROGRESS   | AWS::EC2::Subnet                      | Vpc/publicSubnet2/Subnet (VpcpublicSubnet2SubnetE34B022A) Resource creation Initiated
Ec2InstanceStack |  2/16 | 9:52:00 PM | CREATE_IN_PROGRESS   | AWS::EC2::RouteTable                  | Vpc/publicSubnet2/RouteTable (VpcpublicSubnet2RouteTableC5A6DF77) Eventual consistency check initiated
Ec2InstanceStack |  2/16 | 9:52:00 PM | CREATE_IN_PROGRESS   | AWS::EC2::RouteTable                  | Vpc/publicSubnet1/RouteTable (VpcpublicSubnet1RouteTable15C15F8E) Eventual consistency check initiated
Ec2InstanceStack |  3/16 | 9:52:00 PM | CREATE_COMPLETE      | AWS::EC2::VPCGatewayAttachment        | Vpc/VPCGW (VpcVPCGWBF912B6E) 
Ec2InstanceStack |  3/16 | 9:52:01 PM | CREATE_IN_PROGRESS   | AWS::EC2::SecurityGroup               | Instance/InstanceSecurityGroup (InstanceInstanceSecurityGroupF0E2D5BE) Resource creation Initiated
Ec2InstanceStack |  4/16 | 9:52:02 PM | CREATE_COMPLETE      | AWS::EC2::InternetGateway             | Vpc/IGW (VpcIGWD7BA715C) 
Ec2InstanceStack |  5/16 | 9:52:02 PM | CREATE_COMPLETE      | AWS::EC2::Subnet                      | Vpc/publicSubnet1/Subnet (VpcpublicSubnet1Subnet2BB74ED7) 
Ec2InstanceStack |  6/16 | 9:52:02 PM | CREATE_COMPLETE      | AWS::EC2::Subnet                      | Vpc/publicSubnet2/Subnet (VpcpublicSubnet2SubnetE34B022A) 
Ec2InstanceStack |  6/16 | 9:52:02 PM | CREATE_IN_PROGRESS   | AWS::EC2::SubnetRouteTableAssociation | Vpc/publicSubnet1/RouteTableAssociation (VpcpublicSubnet1RouteTableAssociation4E83B6E4) 
Ec2InstanceStack |  6/16 | 9:52:03 PM | CREATE_IN_PROGRESS   | AWS::EC2::SubnetRouteTableAssociation | Vpc/publicSubnet2/RouteTableAssociation (VpcpublicSubnet2RouteTableAssociationCCE257FF) 
Ec2InstanceStack |  6/16 | 9:52:04 PM | CREATE_IN_PROGRESS   | AWS::EC2::SubnetRouteTableAssociation | Vpc/publicSubnet1/RouteTableAssociation (VpcpublicSubnet1RouteTableAssociation4E83B6E4) Resource creation Initiated
Ec2InstanceStack |  6/16 | 9:52:04 PM | CREATE_IN_PROGRESS   | AWS::EC2::SubnetRouteTableAssociation | Vpc/publicSubnet2/RouteTableAssociation (VpcpublicSubnet2RouteTableAssociationCCE257FF) Resource creation Initiated
Ec2InstanceStack |  7/16 | 9:52:04 PM | CREATE_COMPLETE      | AWS::EC2::SubnetRouteTableAssociation | Vpc/publicSubnet1/RouteTableAssociation (VpcpublicSubnet1RouteTableAssociation4E83B6E4) 
Ec2InstanceStack |  8/16 | 9:52:04 PM | CREATE_COMPLETE      | AWS::EC2::SubnetRouteTableAssociation | Vpc/publicSubnet2/RouteTableAssociation (VpcpublicSubnet2RouteTableAssociationCCE257FF) 
Ec2InstanceStack |  9/16 | 9:52:08 PM | CREATE_COMPLETE      | AWS::EC2::SecurityGroup               | Instance/InstanceSecurityGroup (InstanceInstanceSecurityGroupF0E2D5BE) 
Ec2InstanceStack |  9/16 | 9:52:08 PM | CREATE_IN_PROGRESS   | AWS::EC2::Instance                    | Instance (InstanceC1063A87) 
Ec2InstanceStack | 10/16 | 9:52:09 PM | CREATE_COMPLETE      | AWS::EC2::RouteTable                  | Vpc/publicSubnet2/RouteTable (VpcpublicSubnet2RouteTableC5A6DF77) 
Ec2InstanceStack | 11/16 | 9:52:09 PM | CREATE_COMPLETE      | AWS::EC2::RouteTable                  | Vpc/publicSubnet1/RouteTable (VpcpublicSubnet1RouteTable15C15F8E) 
Ec2InstanceStack | 11/16 | 9:52:10 PM | CREATE_IN_PROGRESS   | AWS::EC2::Route                       | Vpc/publicSubnet2/DefaultRoute (VpcpublicSubnet2DefaultRoute732F0BEB) 
Ec2InstanceStack | 11/16 | 9:52:10 PM | CREATE_IN_PROGRESS   | AWS::EC2::Route                       | Vpc/publicSubnet1/DefaultRoute (VpcpublicSubnet1DefaultRouteB88F9E93) 
Ec2InstanceStack | 11/16 | 9:52:11 PM | CREATE_IN_PROGRESS   | AWS::EC2::Instance                    | Instance (InstanceC1063A87) Resource creation Initiated
Ec2InstanceStack | 11/16 | 9:52:11 PM | CREATE_IN_PROGRESS   | AWS::EC2::Route                       | Vpc/publicSubnet1/DefaultRoute (VpcpublicSubnet1DefaultRouteB88F9E93) Resource creation Initiated
Ec2InstanceStack | 11/16 | 9:52:11 PM | CREATE_IN_PROGRESS   | AWS::EC2::Route                       | Vpc/publicSubnet2/DefaultRoute (VpcpublicSubnet2DefaultRoute732F0BEB) Resource creation Initiated
Ec2InstanceStack | 12/16 | 9:52:11 PM | CREATE_COMPLETE      | AWS::EC2::Route                       | Vpc/publicSubnet1/DefaultRoute (VpcpublicSubnet1DefaultRouteB88F9E93) 
Ec2InstanceStack | 13/16 | 9:52:12 PM | CREATE_COMPLETE      | AWS::EC2::Route                       | Vpc/publicSubnet2/DefaultRoute (VpcpublicSubnet2DefaultRoute732F0BEB) 
Ec2InstanceStack | 13/16 | 9:52:12 PM | CREATE_IN_PROGRESS   | AWS::EC2::Instance                    | Instance (InstanceC1063A87) Eventual consistency check initiated
Ec2InstanceStack | 13/16 | 9:52:12 PM | CREATE_IN_PROGRESS   | AWS::CloudFormation::Stack            | Ec2InstanceStack Eventual consistency check initiated
Ec2InstanceStack | 14/16 | 9:52:21 PM | CREATE_COMPLETE      | AWS::EC2::Instance                    | Instance (InstanceC1063A87) 
14/16 Currently in progress: Ec2InstanceStack, InstanceInstanceProfileAB5AEF02
Ec2InstanceStack | 15/16 | 9:53:57 PM | CREATE_COMPLETE      | AWS::IAM::InstanceProfile             | Instance/InstanceProfile (InstanceInstanceProfileAB5AEF02) 
Ec2InstanceStack | 16/16 | 9:53:57 PM | CREATE_COMPLETE      | AWS::CloudFormation::Stack            | Ec2InstanceStack 

 ✅  Ec2InstanceStack

✨  Deployment time: 144.18s

Stack ARN:
arn:aws:cloudformation:us-east-1:747856204391:stack/Ec2InstanceStack/159cab40-c178-11ef-ae42-0edb2933a48b

✨  Total time: 155.07s


NOTICES         (What's this? https://github.com/aws/aws-cdk/wiki/CLI-Notices)

31885   (cli): Bootstrap stack outdated

        Overview: The bootstrap stack in aws://747856204391/us-east-1 is outdated.
                  We recommend at least version 21, distributed with CDK CLI
                  2.149.0 or higher. Please rebootstrap your environment by
                  runing 'cdk bootstrap aws://747856204391/us-east-1'

        Affected versions: bootstrap: <21

        More information at: https://github.com/aws/aws-cdk/issues/31885


If you don’t want to see a notice anymore, use "cdk acknowledge <id>". For example, "cdk acknowledge 31885".
```


Task 4: Reviewing the resources created in the AWS Management Console
In this task, you review the CloudFormation template that was created with the cdk synth command and review the VPC and EC2 resources.

On the AWS Management Console, in the  search box, search for and choose CloudFormation.

From the left navigation pane, choose Stacks.

Select the EC2InstanceStack that was created.

Choose the Resources tab and expand each resource to see the details of each resource.

On the AWS Management Console, in the  search box, search for and choose VPC.

From the left navigation pane, choose Your VPCs and review the Ec2InstanceStack/VPC that was created.

 NOTE: The following code within the myapp.py file creates a VPC with the Classless Inter-Domain Routing (CIDR) block of 10.0.0.0/16.

```
# create a new VPC
vpc = ec2.Vpc(self, "Vpc", ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16"),
    nat_gateways=0,
    restrict_default_security_group=False,
    subnet_configuration=[ec2.SubnetConfiguration(name="public",subnet_type=ec2.SubnetType.PUBLIC)]
    )
```

On the AWS Management Console, in the  search box, search for and choose EC2.

From the left navigation pane, choose Instances and review the Ec2InstanceStack/Instance it created.

 NOTE: The following code within the myapp.py file creates an EC2 instance with an AWS Identity and Access Management (IAM) role attached to it.

```
    # AMI
    amzn_linux = ec2.MachineImage.latest_amazon_linux2023(
        edition=ec2.AmazonLinuxEdition.STANDARD,
        )

# Instance
instance = ec2.Instance(self, "Instance",
    instance_type=ec2.InstanceType("t3.nano"),
    machine_image=amzn_linux,
    vpc = vpc,
    role = role
    )
```

 Congratulations! You have successfully reviewed the resources created in the AWS Management Console.

Task 5: Cleaning up the AWS CDK environment
In this task, you clean up the AWS CDK environment to delete all resources that are no longer needed. The AWS CDK use the cdk command coupled with the destroy action to clean up all resources created in the CloudFormation template.

With the terminal session still open in the IDE, run the cdk command with the destroy action.

```
cdk destroy
```

 Expected output: You will be prompted with:

Are you sure you want to delete: (y/n)?
 Command: Type y and then press Enter and the stack, along with all resources in the stack, will be deleted.
 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************
EC2InstanceStack: destroying...

EC2InstanceStack: destroyed
 Congratulations! The stack and resources have been deleted.

Conclusion
Congratulations! You have successfully done the following:

Created a directory and its resources
Created the VPC and EC2 instance
Reviewed the resources created
Cleaned up the environment
Additional resources
For more information about AWS CDK, see Getting started with the AWS CDK.
For more information about troubleshooting AWS CDK, see Troubleshooting common AWS CDK issues.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.