# Week 9: AWS SimuLearn: Monitor and Analyze Network Traffic

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to [AWS Cloud Operations 2](../aws-cloud-operations-2.md)
* back to repo's main [README.md](../../../../README.md)

```text
Instance B Private IP 10.1.0.213
Spacestation-A-TGW tgw-attach-04debb34d7dff2b57
Spacestation_C_TGW_Attachment_VPC tgw-attach-0914480988a30522f
```

```shell
iperf3 -s
```

```shell
iperf3 -c 10.1.0.213 -P 2 -t 30
```

## Description

![Monitor and Analyze Network Traffic Description](./images/W090SimuLearn1Img10AnalyzeNetworkTrafficDescription.png)

![Monitor and Analyze Network Traffic Description 2](./images/W090SimuLearn1Img12AnalyzeNetworkTrafficDescription2.png)

## Learn

1. ![AWS Transit Gateway](./images/W090SimuLearn1Img20AwsTransitGateway.png)
2. ![VPC Flow Logs](./images/W090SimuLearn1Img22VpcFlowLogs.png)
3. ![AWS CloudWatch Insights](./images/W090SimuLearn1Img24AwsCloudWatchInsights.png)
4. ![AWS CloudWatch alarm](./images/W090SimuLearn1Img26AwsCloudWatchAlarm.png)
5. ![Amazon Simple Notification Service](./images/W090SimuLearn1Img28AwsCloudWarchAlarmSns.png)
6. ![Network Traffic Monitoring](./images/W090SimuLearn1Img30ArchitectureDiagram.png)

## Practice

![Practice Goals Architecture Diagram](./images/W090SimuLearn1Img32ArchitectureDiagramPracticeGoals.png)

## DIY

![Architecture Diagram](./images/W090SimuLearn1Img40ArchitectureDiagramDiy.png)

![Confirmation](./images/W090SimuLearn1Img50MonitorandAnalyzeNetworkTraffic.png)
