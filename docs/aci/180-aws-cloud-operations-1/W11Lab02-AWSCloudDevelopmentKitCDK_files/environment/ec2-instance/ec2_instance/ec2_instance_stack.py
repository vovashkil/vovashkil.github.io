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