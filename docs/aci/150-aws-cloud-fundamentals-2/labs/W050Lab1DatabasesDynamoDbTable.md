# Working with Amazon DynamoDB Tables and Indexes

* back to AWS Cloud Institute repo's root [aci.md](../../aci.md)
* back to [AWS Cloud Fundamentals 2](../aws-cloud-fundamentals-2.md)
* back to repo's main [README.md](../../../../README.md)

## Lab overview

AnyCompany Video Games is looking to enhance its in-game experience by implementing a robust player database to support a friend service feature. You are tasked with creating the appropriate Amazon DynamoDB table and indexes tailored to meet the specific needs of this gaming environment.

In this lab, you learn how to create a DynamoDB table optimized for storing player data. You also create secondary indexes to provide fast and efficient access to player data, so your gaming platform can deliver seamless experiences for players connecting with friends in real time.

Objectives
By the end of this lab, you should be able to do the following:

Create a DynamoDB table.
Enter data into a DynamoDB table.
Query a DynamoDB table.
Create global secondary indexes.
Delete a DynamoDB table.
Technical knowledge prerequisites
This lab requires:

Familiarity of basic navigation of the AWS Management Console
Basic knowledge of NoSQL database concepts
Completion of the Cloud Fundamentals 1 (CLF1) course and the associated labs
Duration
This lab requires approximately 45 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Consider: A moment to pause to consider how you might apply a concept in your own environment or to initiate a conversation about the topic at hand
 Expected output: A sample output that you can use to verify the output of a command or edited file
 Note: A hint, tip, or important guidance
 Task complete: A conclusion or summary point in the lab
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
Amazon DynamoDB
DynamoDB is a NoSQL (nonrelational) database that supports key-value and document data models. With DynamoDB, you can start small and quickly scale globally as your application and user base grows. Amazon Web Services (AWS) manages the DynamoDB service, so there are no servers to update or maintain.

### Task 1: Create the Friends table

In this task, you create a new table named Friends. When you create a table, in addition to the table name, you must specify the primary key of the table. The primary key uniquely identifies each item in the table, so that no two items can have the same key.

DynamoDB supports two different kinds of primary keys:

Partition key: This is a simple primary key, composed of one attribute.
Partition key and sort key: Referred to as a composite primary key, this type of key is composed of two attributes.
 Note:

The partition key of an item is also known as its hash attribute. The term hash attribute derives from the use of an internal hash function in DynamoDB that evenly distributes data items across partitions, based on their partition key values.

The sort key of an item is also known as its range attribute. The term range attribute derives from the way that DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.

In a table that has a partition key and a sort key, it’s possible for multiple items to have the same partition key value. However, those items must have different sort key values.

On the AWS Management Console, in the search box, search for and choose DynamoDB.

On the Amazon DynamoDB getting started page, choose Create table.

On the Create table page, configure the following options in the Table details section:

For Table name, enter Friends.
For Partition key, enter playerId and choose String  from the dropdown menu.
For Sort key - optional, enter friendId and choose String  from the dropdown menu.
 Note: Using both a partition key and sort key gives additional flexibility when querying data.

Your table uses default settings for indexes and provisioned capacity.

Choose Create table.
 Expected output:

A  Creating the Friends table. It will be available for use shortly. message is displayed at the top of the page.

Wait for your table to be created and its status to be  Active.

 Task complete: You have successfully created a new table named Friends in DynamoDB.

Task 2: Add player data
In this task, you add data to the table that you created. Each table contains zero or more items. An item is a group of attributes that is uniquely identifiable among all the other items. Items in DynamoDB are similar in many ways to rows, records, or tuples in other database systems.

Each item is composed of one or more attributes. An attribute is a fundamental data element. For example, the items that you enter will contain a playerId attribute, which will hold the value of a string.

When you write an item to a DynamoDB table, only the primary key and sort key (if used) are required. Other than these fields, the table does not require a schema. This means that you can add attributes to one item that might be different from the attributes on other items.

In the left navigation pane, choose Explore items.

Select the  Friends table.

Choose Create item.

On the Create item page, configure the following options:

For playerId value, enter player1.

For friendId value, enter player2.

These are the only required attributes, but in this lab you also add additional attributes.

To create an additional attribute, choose Add new attribute , and from the dropdown list, choose String.
 Expected output:

A new String attribute row gets added.

For the new attribute, enter the following:
For Attribute name, enter playerName.
For Value, enter Juan.
To create an additional attribute, choose Add new attribute , and from the dropdown list, choose Number.
 Expected output:

A new Number attribute gets added.

For the new attribute, enter the following:
For Attribute name, enter level.
For Value, enter 10.
To create an additional attribute, choose Add new attribute , and from the dropdown list, choose Number.
 Expected output:

A new Number attribute gets added.

For the new attribute, enter the following:
For Attribute name, enter experience.
For Value, enter 500.
To store the new item with its five attributes, choose Create item.
 Expected output:

A  The item has been saved successfully. message is displayed at the top of the page.

The item now appears on the console.

Create a second item, using these attributes:
Attribute Name	Attribute Type	Attribute Value
playerId	String	player2
friendId	String	player1
playerName	String	Martha
level	Number	8
experience	Number	400
email	String	martha@example.com
 Note: This item has an additional attribute called email. This demonstrates the flexibility of a NoSQL database. Each item is capable of having different attributes without having to predefine a table schema.

Create a third item, using these attributes:
Attribute Name	Attribute Type	Attribute Value
playerId	String	player1
friendId	String	player3
playerName	String	Juan
level	Number	10
experience	Number	500
 Note: player1 has already been added to the table. In a table that has a partition key and a sort key, it’s possible for multiple items to have the same partition key value. However, those items must have different sort key values. This allows for players with more than one friend.

Create another item, using these attributes:
Attribute Name	Attribute Type	Attribute Value
playerId	String	player3
friendId	String	player1
playerName	String	Nikki
level	Number	12
experience	Number	600
There are also faster ways to load data into DynamoDB, such as using AWS Data Pipeline or programmatically loading data.

 Task complete: You have successfully added data to the Friends table.

Task 3: Query and Scan the table
In this task, you use the query and scan operations to retrieve items from the Friends table. A query operation finds items based on primary key values. You must provide the name of the partition key attribute and a single value for that attribute. A query returns all items with that partition key value. Optionally, you can provide a sort key attribute and use a comparison operator to refine the search results. Alternatively, you can scan for an item. This involves looking through every item in a table, so it is less efficient and can take significant time for larger tables.

Task 3.1 Query using only the partition key
A query is the most efficient way to retrieve data from a DynamoDB table.

To query or scan items, expand  Scan or query items in the top section.

Select  Query.

Fields for the partition key (which is the same as primary key) and sort key are now displayed.

For playerId (Partition key), enter player1.

Choose Run.

 Expected output:

Items with player1 as the playerId quickly appear in the list.

Task 3.2 Query using the partition key and sort key
In the expanded  Scan or query items section, configure the following for partition and sort keys:
For playerId (Partition key), enter player1.
For friendId (Sort key), enter player3.
Choose Run.
 Expected output:

A single item appears in the list with player1 as the playerId and player3 as the friendId.

Task 3.3 Scan the table
In this task, you scan using only the friendId attribute.

Select  Scan.

Expand the  Filters section, and configure the following:

For Attribute name, enter friendId.
For Condition, choose Equal to  from the dropdown menu.
For Type, choose String  from the dropdown menu.
For Value, enter player1.
Choose Run.
 Expected output:

The player2 and player3 items are displayed.

 Task complete: You have successfully used the query and scan operations to query the Friends table.

Task 4: Use a global secondary index
Suppose that your company’s application had to retrieve data based on players at a certain level or experience only, and it used a scan operation. As more items are added to the table, scans of all the data would become slow and inefficient.

Some applications might be required to perform many kinds of queries, using a variety of different attributes as query criteria. To support these requirements and speed up queries on non-key attributes, you can create one or more global secondary indexes and issue query requests against these indexes. A global secondary index contains a selection of attributes from the base table, but they are organized by a primary key that is different from that of the table.

Task 4.1: Create a global secondary index using the level and experience attributes
In the left navigation pane, choose Tables.

Choose the Friends table.

Choose the Indexes tab.

Choose Create index.

Configure the index settings:

For Partition key, enter level.
For Data type, choose Number  from the dropdown menu.
For Sort key - optional, enter experience.
For Data type, choose Number  from the dropdown menu.
The Index name field prepopulates to level-experience-index based on the values entered for the partition and sort keys.

Leave all other settings at the defaults.

Choose Create index.
 Expected output:

A  Successfully submitted the request to create your index. message is displayed at the top of the page.

 Note: This might take up to 5–10 minutes to complete. A global secondary index must manage partitioning the existing data. This means that the creation process can take a few minutes to complete, depending on the size of the database.

Use the refresh  option to confirm that your index is created and its status shows as  Active.

Task 4.2: Query using the global secondary index
In this task, you query the table with the global secondary index.

In the left navigation pane, choose Explore items.

Select the  Friends table.

To query or scan items, expand  Scan or query items.

Select  Query.

For Select a table or index, choose Index - level-experience-index  from the dropdown menu.

Fields for the level (Partition key) and experience (Sort key) are now displayed.

For level (Partition key), enter 12.
For experience (Sort key), choose Greater than  from the dropdown menu and enter 500.
 Note: If the Filters - optional section contains data from the previous step, remove it.

Choose Run.
 Expected output:

The player3 item appears in the list.

 Consider: A database full of thousands of players could now be queried quickly and efficiently on non-key attributes. If you need to access most of the non-key attributes on a frequent basis, you can project these attributes—or even the entire base table— into a global secondary index. This gives you maximum flexibility. However, your storage cost would increase or even double due to the data duplication.

 Task complete: You have successfully created a global secondary index and used it to query the table.

Task 5: Delete the table
In this task, you delete the Friends table, which also deletes all the data in the table.

In the left navigation pane, choose Tables.

Select the  Friends table.

Choose Delete.

On the Delete table pop-up window, in the To confirm this deletion, type “confirm”. text box, enter confirm.

Choose Delete.

 Expected output:

A  The request to delete the “Friends” table has been submitted successfully. message is displayed at the top of the page.

Use the refresh  option to confirm the table deletion.
 Task complete: You have successfully deleted the Friends table.

Conclusion
 You now have successfully done the following:

Created a DynamoDB table
Entered data into a DynamoDB table
Queried a DynamoDB table
Created global secondary indexes
Deleted a DynamoDB table
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.

---

### Additional resources

For more information about how to use Amazon DynamoDB, see [Amazon DynamoDB Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html).

---
