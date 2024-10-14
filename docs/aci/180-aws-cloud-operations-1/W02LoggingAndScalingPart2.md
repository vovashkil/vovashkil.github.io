# Logging and Scaling Part 2

* **back to AWS Cloud Institute repo's root [aci.md](../aci.md)**
* **back to repo's main [README.md](../../../README.md)**

## Auto Scaling

## Vertical scaling and horizontal scaling

### Vertical scaling

Vertical scaling has the following characteristics:

* It involves increasing the specifications and resources of an existing server, for example, adding more RAM, CPU cores, and storage to a server to make it more powerful.
* It supports handling more load on the same server. It also reduces the need for more servers.
* It has hardware limitations in terms of how much a server can be upgraded.
* It requires downtime and migrations when upgrading server hardware.

### Horizontal scaling

Horizontal scaling has the following characteristics:

* It involves adding more servers that function together as one unit, for example, adding more application servers behind a load balancer.
* It supports handling more overall load by distributing it across more servers. It's more scalable than vertical scaling.
* It has no hardware limitations. More inexpensive commodity servers can be added whenever needed.
* It provides scaling with no downtime. New servers can be added to the resource pool seamlessly.
* It requires more complex architecture and testing to distribute load and tasks.

## Application Auto Scaling and Amazon EC2 Auto Scaling

### Target tracking scaling

With target tracking scaling policies, you specify an Amazon CloudWatch metric and a target value that represents the ideal average utilization or throughput level for your application.

A target tracking scaling policy is more aggressive in adding capacity when utilization increases than it is in removing capacity when utilization decreases. For example, if the policy's specified metric reaches its target value, the policy assumes that your application is already heavily loaded. So it responds by adding capacity proportional to the metric value as fast as it can. The higher the metric, the more capacity is added.

When the metric falls below the target value, the policy expects that utilization will eventually increase again. In this case, it slows down scaling by removing capacity only when utilization passes a threshold that is far enough below the target value (usually more than 10 percent lower) for utilization to be considered to have slowed. The intention of this more conservative behavior is to ensure that removing capacity only happens when the application is no longer experiencing demand at the same high level that it was previously.

#### Choosing metrics

You can create target tracking scaling policies with either predefined metrics or custom metrics. Consider the following when choosing a metric:

* AWS recommends that you only use metrics that are available at 1-minute intervals to help you scale faster in response to utilization changes. Target tracking will evaluate metrics aggregated at a 1-minute granularity for all predefined metrics and custom metrics. But the underlying metric might publish data less frequently. For example, all Amazon EC2 metrics are sent in 5-minute intervals by default, but they are configurable to 1 minute (known as detailed monitoring). This choice is up to the individual services. Most try to use the smallest interval possible.
* Not all custom metrics work for target tracking. The metric must be a valid utilization metric and describe how busy a scalable target is. The metric value must increase or decrease proportionally to the capacity of the scalable target so that the metric data can be used to proportionally scale the scalable target.
* To use the **ALBRequestCountPerTarget** metric, you must specify the **ResourceLabel** parameter to identify the load balancer target group that is associated with the metric.
* When a metric emits real 0 values to CloudWatch (for example, **ALBRequestCountPerTarget**), AWS Application Auto Scaling can scale in to 0 when there is no traffic to your application for a sustained period of time. To have your scalable target scale in to 0 when no requests are routed it, the scalable target's minimum capacity must be set to 0.
* Instead of publishing new metrics to use in your scaling policy, you can use metric math to combine existing metrics.

#### Defining target value

When you create a target tracking scaling policy, you must specify a target value. The target value represents the optimal average utilization or throughput for your application. To use resources cost efficiently, set the target value as high as possible with a reasonable buffer for unexpected traffic increases. When your application is optimally scaled out for a normal traffic flow, the actual metric value should be at or just below the target value.

When a scaling policy is based on throughput, such as the request count per target for an Application Load Balancer, network I/O, or other count metrics, the target value represents the optimal average throughput from a single entity (such as a single target of your Application Load Balancer target group), for a 1-minute period.

#### Considerations

The following considerations apply when working with target tracking scaling policies:

* Do not create, edit, or delete the CloudWatch alarms that are used with a target tracking scaling policy. Amazon EC2 Auto Scaling or Application Auto Scaling creates and manages the CloudWatch alarms that are associated with your target tracking scaling policies and deletes them when no longer needed.
* If the metric is missing data points, this causes the CloudWatch alarm state to change to **INSUFFICIENT_DATA**. When this happens, Amazon EC2 Auto Scaling or Application Auto Scaling cannot scale your scalable target until new data points are found.
* If the metric is sparsely reported by design, metric math can be helpful. For example, to use the most recent values, use the **FILL(m1,REPEAT)** function where **m1** is the metric.
* You might see gaps between the target value and the actual metric data points. This is because AWS acts conservatively by rounding up or down when it determines how much capacity to add or remove. This prevents it from adding insufficient capacity or removing too much capacity. However, for a scalable target with a small capacity, the actual metric data points might seem far from the target value. For a scalable target with a larger capacity, adding or removing capacity causes less of a gap between the target value and the actual metric data points.
* A target tracking scaling policy assumes that it should perform scale out when the specified metric is above the target value. You can't use a target tracking scaling policy to scale out when the specified metric is below the target value.

### Step scaling

Step scaling policies increase or decrease the current capacity of a scalable target based on a set of scaling adjustments, known as step adjustments. The adjustments vary based on the size of the alarm breach. The policy continues to respond to additional alarms while a scaling activity is in progress. Therefore, all alarms that are breached are evaluated by Amazon EC2 Auto Scaling or Application Auto Scaling as it receives the alarm messages.

#### Step adjustments

When you create a step scaling policy, you specify one or more step adjustments that automatically scale the capacity of the target dynamically based on the size of the alarm breach. Each step adjustment specifies the following:

* A lower bound for the metric value
* An upper bound for the metric value
* The amount by which to scale, based on the scaling adjustment type

CloudWatch aggregates metric data points based on the statistic for the metric that is associated with your CloudWatch alarm. When the alarm is breached, the appropriate scaling policy is invoked. Amazon EC2 Auto Scaling or Application Auto Scaling applies the aggregation type to the most recent metric data points from CloudWatch (as opposed to the raw metric data). It compares this aggregated metric value against the upper and lower bounds defined by the step adjustments to determine which step adjustment to perform.

You specify the upper and lower bounds relative to the breach threshold. For example, let's say that you have a scalable target that has a capacity of 10. You have CloudWatch alarms with metric high and metric low thresholds of 60 percent and 40 percent, respectively.

You have an adjustment type of **PercentChangeInCapacity** and scale-out and scale-in policies with the following step adjustments.

#### Example: Step adjustments for scale-out policy

| Lower bound | Upper bound | Adjustment |
| ----------- | ----------- | ---------- |
| 0 | 10 | 0 |
| 10 | 20 | 10 |
| 20 | Null | 30 |

#### Example: Step adjustments for scale-in policy

| Lower bound | Upper bound | Adjustment |
| ----------- | ----------- | ---------- |
| -10 | 0 | 0 |
| -20 | -10 | -10 |
| Null | -20 | -30 |

This creates the following scaling configuration:

```
Metric value

-infinity          30%    40%          60%     70%             infinity
-----------------------------------------------------------------------
          -30%      | -10% | Unchanged  | +10%  |       +30%        
-----------------------------------------------------------------------
```

#### Summary

* The original capacity is maintained while the aggregated metric value is greater than 40 and less than 60.
* If the metric value gets to 60, Application Auto Scaling increases the capacity of the scalable target by 1, to 11. That's based on the second step adjustment of the scale-out policy (add 10 percent of 10). After the new capacity is added, Application Auto Scaling increases the current capacity to 11. If the metric value rises to 70 even after this increase in capacity, Application Auto Scaling increases the target capacity by 3, to 14. That's based on the third step adjustment of the scale-out policy (add 30 percent of 11, 3.3, rounded down to 3). 
* If the metric value gets to 40, Application Auto Scaling decreases the capacity of the scalable target by 1, to 13, based on the second step adjustment of the scale-in policy (remove 10 percent of 14, 1.4, rounded down to 1). If the metric value falls to 30 even after this decrease in capacity, Application Auto Scaling decreases the target capacity by 3, to 10, based on the third step adjustment of the scale-in policy (remove 30 percent of 13, 3.9, rounded down to 3).

When you specify the step adjustments for your scaling policy, note the following:

* The ranges of your step adjustments can't overlap or have a gap.
* Only one step adjustment can have a null lower bound (negative infinity). If one step adjustment has a negative lower bound, then there must be a step adjustment with a null lower bound.
* Only one step adjustment can have a null upper bound (positive infinity). If one step adjustment has a positive upper bound, then there must be a step adjustment with a null upper bound.
* The upper and lower bound can't be null in the same step adjustment.
* If the metric value is above the breach threshold, the lower bound is inclusive and the upper bound is exclusive. If the metric value is below the breach threshold, the lower bound is exclusive and the upper bound is inclusive.

### Scheduled scaling

Scheduled scaling helps you to set up your own scaling schedule according to predictable load changes. To use scheduled scaling, you create scheduled actions. Scheduled actions are performed automatically as a function of date and time. When you create a scheduled action, you specify when the scaling activity should occur and the new desired minimum and maximum sizes for the scaling action. You can create scheduled actions that scale one time only or that scale on a recurring schedule.

You can use scheduled scaling and scaling policies together on the same resource to get the benefits of both. After a scheduled action runs, the scaling policy can continue to make decisions about whether to further scale capacity. This helps you ensure that you have sufficient capacity to handle the load for your application. While your application scales to match demand, current capacity must fall within the minimum and maximum capacity that was set by your scheduled action.

#### Considerations

When you create a scheduled action, keep the following in mind:

* A scheduled action sets the **MinCapacity** and **MaxCapacity** to what is specified by the scheduled action at the date and time specified. The request can optionally include only one of these sizes. For example, you can create a scheduled action with only the minimum capacity specified. In some cases, however, you must include both sizes to ensure that the new minimum capacity is not greater than the maximum capacity, or the new maximum capacity is not less than the minimum capacity.
* By default, the recurring schedules that you set are in Coordinated Universal Time (UTC). You can change the time zone to correspond to your local time zone or a time zone for another part of your network. When you specify a time zone that observes daylight saving time, the action automatically adjusts for Daylight Saving Time (DST).
* You can temporarily turn off scheduled scaling for a scalable target. This helps you prevent scheduled actions from being active without having to delete them. You can then resume scheduled scaling when you want to use it again.
* The order in which scheduled actions run is guaranteed for the same scalable target, but not for scheduled actions across scalable targets.
* To complete a scheduled action successfully, the specified resource must be in a scalable state in the target service. If it isn't, the request fails and returns an error message, for example: *Resource Id [ActualResourceId] is not scalable. Reason: The status of all DB instances must be 'available' or 'incompatible-parameters'*.
* A scheduled action generally runs within seconds. However, the action might be delayed for up to 2 minutes from the scheduled start time. Because scheduled actions are run in the order that they are specified, scheduled actions with start times close to each other can take longer to run.

#### Commonly used commands for scheduled action creation, management, and deletion

The following commands are commonly used for working with scheduled scaling:

* Use the [register-scalable-target](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/register-scalable-target.html) command to register AWS or custom resources as scalable targets (a resource that Application Auto Scaling can scale), and to suspend and resume scaling.
* Use the [put-scheduled-action](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/put-scheduled-action.html) command to add or modify scheduled actions for an existing scalable target.
* Use the [describe-scaling-activities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/describe-scaling-activities.html) command to return information about scaling activities in an AWS Region.
* Use the [describe-scheduled-actions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/describe-scaling-activities.html) command to return information about scheduled actions in an AWS Region.
* Use the [delete-scheduled-action](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/delete-scheduled-action.html) command to delete a scheduled action.

#### Limitations

The following are limitations when using scheduled scaling:

* The names of scheduled actions must be unique per scalable target.
* Application Auto Scaling doesn't provide second-level precision in schedule expressions. The finest resolution using a cron expression is 1 minute.
* The scalable target can't be an Amazon Managed Streaming for Apache Kafka (Amazon MSK) cluster. Scheduled scaling is not supported for Amazon MSK.
* Console access to view, add, update, or remove scheduled actions on scalable resources depends on the resource that you use.

## Auto Scaling with Amazon ECS

Amazon Elastic Container Service (Amazon ECS) is a fully managed container orchestration service that helps you deploy, manage, and scale containerized applications.

With Amazon ECS, your applications are containerized. An Amazon ECS cluster can run a containerized application as a task. Amazon ECS services are used to run and maintain your desired number of tasks.

Amazon ECS services are scaled by modifying the number of running tasks.

### Application Auto Scaling with Amazon ECS

Amazon ECS uses the Application Auto Scaling service to provide service auto scaling functionality. Application Auto Scaling is a web service for developers and system administrators who need a solution for automatically scaling their scalable resources for individual AWS services beyond Amazon EC2.

Amazon ECS publishes CloudWatch metrics with your service’s average CPU and memory usage. You can use these and other CloudWatch metrics to scale out your service (add more tasks) to deal with high demand at peak times, and to scale in your service (run fewer tasks) to reduce costs during periods of low utilization.

Amazon ECS supports target tracking scaling, step scaling, and scheduled scaling.

### Service auto scaling and deployments

Application Auto Scaling turns off scale-in processes while Amazon ECS deployments are in progress. However, scale-out processes continue to occur, unless suspended, during a deployment. If you want to suspend scale-out processes while deployments are in progress, take the following steps.

1. Call the [describe-scalable-targets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/describe-scalable-targets.html) command, specifying the resource ID of the service associated with the scalable target in Application Auto Scaling (for example: **service/default/sample-webapp**). Record the output. You will need it when you call the next command.
2. Call the [register-scalable-target](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/register-scalable-target.html) command, specifying the resource ID, namespace, and scalable dimension. Specify **true** for both **DynamicScalingInSuspended** and **DynamicScalingOutSuspended**.
3. After deployment is complete, you can call the [register-scalable-target](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/register-scalable-target.html) command to resume scaling.

### Considerations

When using scaling policies, consider the following:

* Amazon ECS sends metrics in 1-minute intervals to CloudWatch. Metrics are not available until the clusters and services send the metrics to CloudWatch, and you cannot create CloudWatch alarms for metrics that do not exist.
* The scaling policies support a cooldown period. This is the number of seconds to wait for a previous scaling activity to take effect. For scale-out events, the intention is to continuously (but not excessively) scale out. After service auto scaling successfully scales out using a scaling policy, it starts to calculate the cooldown time. The scaling policy won't increase the desired capacity again unless either a larger scale out is initiated or the cooldown period ends. While the scale-out cooldown period is in effect, the capacity added by the initiating scale-out activity is calculated as part of the desired capacity for the next scale-out activity. For scale-in events, the intention is to scale in conservatively to protect your application's availability, so scale-in activities are blocked until the cooldown period has expired. However, if another alarm initiates a scale-out activity during the scale-in cooldown period, service auto scaling scales out the target immediately. In this case, the scale-in cooldown period stops and doesn't complete.
* If a service's desired count is set below its minimum capacity value, and an alarm activates a scale-out activity, service auto scaling scales the desired count up to the minimum capacity value. It continues to scale out as required, based on the scaling policy associated with the alarm. However, a scale-in activity does not adjust the desired count because it is already below the minimum capacity value.
* If a service's desired count is set above its maximum capacity value, and an alarm activates a scale-in activity, service auto scaling scales the desired count out to the maximum capacity value. It continues to scale in as required, based on the scaling policy associated with the alarm. However, a scale-out activity does not adjust the desired count because it is already above the maximum capacity value.
* During scaling activities, the actual running task count in a service is the value that service auto scaling uses as its starting point, as opposed to the desired count. This is what processing capacity is supposed to be. This prevents excessive (runaway) scaling that might not be satisfied, for example, if there aren't enough container instance resources to place the additional tasks. If the container instance capacity is available later, the pending scaling activity might succeed, and then further scaling activities can continue after the cooldown period.
* If you want your task count to scale to zero when there's no work to be done, set a minimum capacity of 0. With target tracking scaling policies, when actual capacity is 0 and the metric indicates that there is workload demand, service auto scaling waits for one data point to be sent before scaling out. In this case, it scales out by the minimum possible amount as a starting point and then resumes scaling based on the actual running task count.
* Application Auto Scaling turns off scale-in processes while Amazon ECS deployments are in progress. However, scale-out processes continue to occur, unless suspended, during a deployment.
* You have several Application Auto Scaling options for Amazon ECS tasks. Target tracking is the easiest mode to use. With it, all you need to do is set a target value for a metric, such as CPU average utilization. Then the auto scaler automatically manages the number of tasks that are needed to attain that value. With step scaling, you can more quickly react to changes in demand, because you define the specific thresholds for your scaling metrics, and how many tasks to add or remove when the thresholds are crossed. And more importantly, you can react very quickly to changes in demand by minimizing the amount of time that a threshold alarm is in breach.

### Task scale-in protection

You can use Amazon ECS task scale-in protection to protect your tasks from being terminated by scale-in events from either service auto scaling or deployments. Certain applications require a mechanism to safeguard mission-critical tasks from termination by scale-in events during times of low utilization or during service deployments. Here are some examples:

* You have a queue-processing asynchronous application such as a video transcoding job where some tasks have to run for hours even when cumulative service utilization is low.
* You have a gaming application that runs game servers as Amazon ECS tasks that have to continue running even if all users have logged out, to reduce startup latency of a server reboot.
* When you deploy a new code version, you need tasks to continue running because it would be expensive to reprocess.

To protect tasks that belong to your service from terminating in a scale-in event, set the **protectionEnabled** attribute to **true**. By default, tasks are protected for 2 hours. You can customize the protection period by using the **expiresInMinutes** attribute. You can protect your tasks for a minimum of 1 minute and up to a maximum of 2,880 minutes (48 hours).

After a task finishes its requisite work, you can set the **protectionEnabled** attribute to **false**, allowing the task to be terminated by subsequent scale-in events.

#### Task scale-in protection mechanisms

You can set and get task scale-in protection using either the Amazon ECS container agent endpoint or the Amazon ECS API.

##### Amazon ECS container agent endpoint

AWS recommends using the Amazon ECS container agent endpoint for tasks that can self-determine the need to be protected. Use this approach for queue-based or job-processing workloads.

When a container starts processing work, for example by consuming an Amazon Simple Queue Service (Amazon SQS) message, you can set the **ProtectionEnabled** attribute through the task scale-in protection endpoint path **$ECS_AGENT_URI/task-protection/v1/state** from within the container. Amazon ECS will not terminate this task during scale-in events. After your task finishes its work, you can unset the **ProtectionEnabled** attribute using the same endpoint, making the task eligible for termination during subsequent scale-in events.

##### Amazon ECS API

You can use the Amazon ECS API to set task scale-in protection if your application has a component that tracks the status of active tasks. Use **UpdateTaskProtection** to mark one or more tasks as protected.

An example of this approach would be if your application is hosting game server sessions as Amazon ECS tasks. When a user logs in to a session on the server (task), you can mark the task as protected. After the user logs out, you can either clear the protection specifically for this task or periodically clear protection for similar tasks that no longer have active sessions, depending on your requirement to keep idle servers.

You can also combine both approaches. For example, use the Amazon ECS agent endpoint to set task protection from within a container and use the Amazon ECS API to remove task protection from your external controller service.

## Auto Scaling with DynamoDB

Amazon DynamoDB auto scaling uses the Application Auto Scaling service to dynamically adjust provisioned throughput capacity on your behalf, in response to actual traffic patterns. This makes it possible for a table or a global secondary index to increase its provisioned read and write capacity to handle sudden increases in traffic, without throttling. When the workload decreases, Application Auto Scaling decreases the throughput so that you don't pay for unused provisioned capacity.
DynamoDB auto scaling can increase read capacity or write capacity as often as necessary, in accordance with your auto scaling policy.

* DynamoDB auto scaling updates your table’s provisioned capacity within minutes. Factor this scaling time into your auto scaling settings to allow time for the capacity to be provisioned.
* DynamoDB auto scaling doesn't prevent you from manually modifying provisioned throughput settings. These manual adjustments don't affect any existing CloudWatch alarms that are related to DynamoDB auto scaling.
* If you enable DynamoDB auto scaling for a table that has one or more global secondary indexes, AWS highly recommends that you also apply auto scaling uniformly to those indexes. This will help ensure better performance for table writes and reads, and help avoid throttling. You can enable auto scaling by selecting **Apply same settings to global secondary indexes** in the AWS Management Console.
* When you delete a table or global table replica, any associated scalable targets, scaling polices, or CloudWatch alarms are not automatically deleted with it.
* When you create a global secondary index (GSI) for an existing table, auto scaling is not enabled for the GSI. You will have to manually manage the capacity while the GSI is being built. When the backfill on the GSI is complete and it reaches active status, auto scaling will operate as normal.

## Auto Scaling with Aurora

Before you can use Aurora auto scaling with an Aurora DB cluster, you must first create an Aurora DB cluster with a primary (writer) DB instance. Aurora auto scaling only scales a DB cluster if the DB cluster is in the available state.

When Application Auto Scaling adds a new Aurora replica, the new Aurora replica is the same DB instance class as the one used by the primary instance. Also, the promotion tier for new Aurora replicas is set to the last priority, which is 15 by default. This means that during a failover, a replica with a better priority, such as one created manually, would be promoted first.

Aurora auto scaling only removes Aurora replicas that it created.

To benefit from Aurora auto scaling, your applications must support connections to new Aurora replicas. To do so, AWS recommends using the Aurora reader endpoint. For Aurora MySQL-Compatible, you can use a driver such as the AWS JDBC Driver for MySQL.

Aurora global databases currently do not support Aurora auto scaling for secondary DB clusters.

## Amazon EC2 Auto Scaling

## Summary

## Week 2 Assessment

### A development team is architecting a scalable and fault-tolerant infrastructure for their e-commerce platform. The platform spans multiple Amazon Elastic Compute Cloud (Amazon EC2) instances in different AWS Regions to meet the needs of a global customer base. They want the incoming traffic to their platform to be evenly distributed across instances within each Region. Additionally, they want to implement a solution that allows for seamless failover in the event of an outage in any given Region. Which combination of AWS services would BEST meet the requirements? (Select TWO.)

* **AWS Route 53**
* **Elastic Load Balancing (ELB)**

AWS Route 53, in combination with ELB, provides an optimal solution for efficiently managing global DNS. They distribute incoming traffic only to the healthy instances for increased fault tolerance in the e-commerce application.

#### An environment has an Amazon Elastic Compute Cloud (Amazon EC2) Auto Scaling group across two Availability Zones. One Availability Zone has four Amazon EC2 instances, and the other has three EC2 instances. The Auto Scaling group uses a default termination policy. None of the instances are protected from a scale-in event. How will Amazon EC2 Auto Scaling first respond if there is a scale-in event?

* **Amazon EC2 Auto Scaling selects the Availability Zone with four EC2 instances, and then continues to evaluate.**

The default termination policy helps ensure that instances are distributed evenly across Availability Zones for high availability. This action is the starting point of the default termination policy, if the Availability Zones have an unequal number of instances and the instances are unprotected. 

The other options are incorrect because those actions are not the first action of the default termination policy. According to the default termination policy, Amazon EC2 Auto Scaling 

* first determines which Availability Zones have the most instances and then identifies at least one instance that is not protected from scale-in.
* If the Availability Zones have an equal number of instances, Amazon EC2 Auto Scaling checks for the oldest launch configuration.
* After applying all the preceding criteria, if there are multiple unprotected instances to terminate, Amazon EC2 Auto Scaling determines which instances are closest to the next billing hour.
* If there are multiple unprotected instances closest to the next billing hour, Amazon EC2 Auto Scaling terminates one of those instances at random.

#### A developer is architecting a microservices-based application on AWS, and their infrastructure includes Amazon Elastic Compute Cloud (Amazon EC2) instances managed by an Amazon EC2 Auto Scaling group. They want to implement a mechanism that invoke custom actions or workflows during specific points in the instance lifecycle, such as instance launch or termination. These actions include invoking serverless functions updating databases or notifying external systems. Which is the BEST AWS service to use as a target service?

* **Amazon EventBridge**

As a best practice, AWS recommends using EventBridge. The notifications sent to Amazon SNS and Amazon SQS contain the same information as the notifications that Amazon EC2 Auto Scaling sends to EventBridge.
Before EventBridge, the standard practice was to send a notification to Amazon SNS or Amazon SQS and integrate another service to perform programmatic actions. Today, EventBridge gives users more options for services that can be targeted, and makes it more convenient to handle events using serverless architecture.
