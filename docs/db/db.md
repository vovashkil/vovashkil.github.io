###### back to repo's main [README.md](../../README.md)
#### DB Types
##### SQLite Types
* TEXT
* NUMERIC
* INTEGER
* REAL
* BLOB
##### MySQL Types
* CHAR(size)
* VARCHAR(size)
* SMALLINT
* INT
* BIGINT
* FLOAT
* DOUBLE
* ...
#### Create Table
```
CREATE TABLE table_name  (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    column2 TEXT NOT NULL,
    column3 TEXT NOT NULL,
    column4 INTEGER NOT NULL
);
```
##### Constraints
* CHECK
* DEFAULT
* NOT NULL
* PRIMARY KEY
* UNIQUE
* ...
##### Insert Data
```
INSERT INTO table_name
    (column2, column3, column4)
    VALUES ("value2", "value3", value4);
```
##### Retrive Data
```
SELECT column2, column3 FROM table_name;
```
###### Retrieving more specific date
```
SELECT * FROM table_name WHERE column1 = value ;
SELECT * FROM table_name WHERE column2 IN ("some_value", "some_other_value");
SELECT * FROM table_name WHERE column2 LIKE "%pattern%";
```
###### Formatting output
```
sqlite> .mode columds
sqlite> .headers yes
```
###### Functions
* AVERAGE
* COUNT
* MAX
* MIN
* SUM
* ...
##### Update Data
```
UPDATE table_name
    SET column4 = value
    WHERE column2 = "somevalue"
    AND column3 = "othervalue";
```
##### Delete Data
```
DELETE FROM table_name WHERE column3 = "somevalue";
```
##### Other Clauses
* LIMIT
* ORDER BY
* GROUP BY
* HAVING
* ...
##### Foreign keys
```
SELECT column2, column3, column4
    FROM table1 JOIN table2
ON table2.table1_id = table1.id;
```
###### JOINs
* JOIN / INNER JOIN
* LEFT OUTER JOIN
* RIGHT OUTER JOIN
* FULL OUTER JOIN
##### CREATE INDEX
```
CREATE INDEX index_name ON table2 (column3);
```
##### SQL Injection
```
SELECT * FROM users
WHERE username = username AND password = password;
```
##### username = user"--, password field doesn't matter, '--' means a comment after it
```
SELECT * FROM users
WHERE username = "user"--" AND password = "";
```
This quesry becomes:
```
SELECT * FROM users
WHERE username = "user"
```
##### Race Condition
