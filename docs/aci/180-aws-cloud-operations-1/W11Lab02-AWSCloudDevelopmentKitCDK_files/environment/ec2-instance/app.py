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