arn:aws:secretsmanager:us-west-2:647614677309:secret:mydbsecret-1974-DSI3dN

aws secretsmanager get-secret-value --secret-id (SecretARN) --version-stage AWSCURRENT

aws secretsmanager get-secret-value --secret-id arn:aws:secretsmanager:us-west-2:647614677309:secret:mydbsecret-1974-DSI3dN --version-stage AWSCURRENT


secret=$(aws secretsmanager get-secret-value --secret-id arn:aws:secretsmanager:us-west-2:647614677309:secret:mydbsecret-1974-DSI3dN | jq .SecretString | jq fromjson)
user=$(echo $secret | jq -r .username)
password=$(echo $secret | jq -r .password)
endpoint=$(echo $secret | jq -r .host)
port=$(echo $secret | jq -r .port)




Insert succeeded at Sun Sep  1 03:02:08 2024 test_run_id: test_run_0, index_id:63
Insert succeeded at Sun Sep  1 03:02:08 2024 test_run_id: test_run_0, index_id:64
Insert succeeded at Sun Sep  1 03:02:09 2024 test_run_id: test_run_0, index_id:65
Insert succeeded at Sun Sep  1 03:02:09 2024 test_run_id: test_run_0, index_id:66
Insert succeeded at Sun Sep  1 03:02:10 2024 test_run_id: test_run_0, index_id:67
Insert succeeded at Sun Sep  1 03:02:11 2024 test_run_id: test_run_0, index_id:68
Insert succeeded at Sun Sep  1 03:02:11 2024 test_run_id: test_run_0, index_id:69
Insert succeeded at Sun Sep  1 03:02:12 2024 test_run_id: test_run_0, index_id:70
Insert succeeded at Sun Sep  1 03:02:12 2024 test_run_id: test_run_0, index_id:71
Insert succeeded at Sun Sep  1 03:02:13 2024 test_run_id: test_run_0, index_id:72
Insert succeeded at Sun Sep  1 03:02:13 2024 test_run_id: test_run_0, index_id:73
Insert succeeded at Sun Sep  1 03:02:14 2024 test_run_id: test_run_0, index_id:74
Insert succeeded at Sun Sep  1 03:02:14 2024 test_run_id: test_run_0, index_id:75
Insert succeeded at Sun Sep  1 03:02:15 2024 test_run_id: test_run_0, index_id:76
Insert succeeded at Sun Sep  1 03:02:15 2024 test_run_id: test_run_0, index_id:77
Insert succeeded at Sun Sep  1 03:02:16 2024 test_run_id: test_run_0, index_id:78
Insert succeeded at Sun Sep  1 03:02:16 2024 test_run_id: test_run_0, index_id:79
Insert succeeded at Sun Sep  1 03:02:17 2024 test_run_id: test_run_0, index_id:80
Insert succeeded at Sun Sep  1 03:02:18 2024 test_run_id: test_run_0, index_id:81
Insert succeeded at Sun Sep  1 03:02:18 2024 test_run_id: test_run_0, index_id:82
Insert succeeded at Sun Sep  1 03:02:19 2024 test_run_id: test_run_0, index_id:83
Insert succeeded at Sun Sep  1 03:02:20 2024 test_run_id: test_run_0, index_id:84
Insert succeeded at Sun Sep  1 03:02:20 2024 test_run_id: test_run_0, index_id:85
Insert succeeded at Sun Sep  1 03:02:21 2024 test_run_id: test_run_0, index_id:86
Insert succeeded at Sun Sep  1 03:02:21 2024 test_run_id: test_run_0, index_id:87
(2013, 'Lost connection to MySQL server during query (The read operation timed out)')
There was an error: Db Connection failed



Connection succeeded at Sun Sep  1 03:04:23 2024

========================================
Total Db connection attempts: 90
Successful Db connections: 89
Failed Db connections: 1
failure_start_time: Sun Sep  1 03:02:23 2024
failure_end_time: Sun Sep  1 03:04:23 2024
failure condition duration: 120 seconds
Last inserted sync record id on initial primary db node: 87
Pre-failure Db node hostname: ip-172-19-2-150
Post-failure Db node hostname: ip-172-19-0-34
Newest 5 sync records in current primary db node:
[ {'created': 1725159741, 'index_id': 87, 'test_run_id': 'test_run_0'},
  {'created': 1725159741, 'index_id': 86, 'test_run_id': 'test_run_0'},
  {'created': 1725159740, 'index_id': 85, 'test_run_id': 'test_run_0'},
  {'created': 1725159739, 'index_id': 84, 'test_run_id': 'test_run_0'},
  {'created': 1725159739, 'index_id': 83, 'test_run_id': 'test_run_0'}]


create_failover_sync_db.py
```
#!/usr/bin/env python3

import argparse
import logging

from db_test_meter.database import Database
from db_test_meter.util import init_logger, collect_user_input, AppConfig


def create_db(db: Database) -> None:
    """
    Utility to create the db and table for the sync check
    :param db:
    :return:
    """
    try:
        log.debug(f'creating database {AppConfig.TEST_DB_NAME}')
        db.run_query(f"DROP DATABASE IF EXISTS {AppConfig.TEST_DB_NAME}")
        db.run_query(f"CREATE DATABASE IF NOT EXISTS {AppConfig.TEST_DB_NAME}")
        log.debug(f'creating table {AppConfig.TEST_DB_TABLE}')
        db.run_query(
            f"CREATE TABLE {AppConfig.TEST_DB_NAME}.{AppConfig.TEST_DB_TABLE} (`test_run_id` varchar(50) NOT NULL, `index_id` int(10) unsigned NOT NULL, `created` int(8) NOT NULL)")
        print(f'Database {AppConfig.TEST_DB_NAME} created')
        print(f'Table {AppConfig.TEST_DB_NAME}.{AppConfig.TEST_DB_TABLE} created')
    except Exception as e:
        print(f'There was an error: {e}')


parser = argparse.ArgumentParser(
    'simple utility to create the db and table used by failover_test.py. Usage: ./create_failover_sync_db.py')
parser.add_argument('--debug', action='store_true')
init_logger(debug=parser.parse_args().debug)
log = logging.getLogger()

print('This will destroy and recreate sync database and tracking table')
if (input("enter y to continue, n to exit [n]: ") or 'n').lower() == 'y':
    db_connection_metadata = collect_user_input()
    db = Database(db_connection_metadata)
    create_db(db)
else:
    print('exiting...')
```

failover_test.py
```
#!/usr/bin/env python3

import argparse
import logging
import pprint
import sys
import time
import traceback

from db_test_meter.database import Database
from db_test_meter.test_run import TestRun
from db_test_meter.util import init_logger, collect_user_input

parser = argparse.ArgumentParser('This will gather metrics of a failover event')
parser.add_argument('--test_run_id', metavar='<test run id>', type=str, nargs='?', required=True,
                    help='a unique identifier for this test run')
parser.add_argument('--loop_time', metavar='<seconds>', type=float, nargs='?', default='.5',
                    help='sleep is used to insure this minimum loop time in sec. Can be decimal (defaults to .5')
parser.add_argument('--debug', action='store_true')
args = parser.parse_args()
test_run_id = args.test_run_id
loop_time = args.loop_time
if loop_time <= 0:
    print('Loop time must be >= 0, exiting...')
    exit(1)
init_logger(debug=args.debug)
log = logging.getLogger()

db_connection_metadata = collect_user_input()
db = Database(db_connection_metadata)
test_runner = TestRun(db)

if not test_runner.test_db_connection():
    log.fatal('Initial db connection failed.  Check you connection setup and try again. Exiting...')
    exit(1)

pre_failure_db_node_hostname = test_runner.get_db_node_hostname()
print(f'Test starting, initial Db node hostname: {pre_failure_db_node_hostname}')
post_failure_db_node_hostname = None

try:
    while True:
        loop_start_time = time.time()
        test_runner.ensure_minumum_loop_time(loop_time, loop_start_time, test_runner.prev_loop_end_time)
        if test_runner.db_node_heartbeat(test_run_id):
            if test_runner.recovery_detected():
                test_runner.failure_condition_end_time = time.time()
                post_failure_db_node_hostname = test_runner.get_db_node_hostname()
                test_runner.prev_loop_end_time = time.time()
                break
        test_runner.prev_loop_end_time = time.time()
except Exception as e:
    print(f'There was an unexpected exception: {e}')
    print("-" * 60)
    traceback.print_exc(file=sys.stdout)
    print("-" * 60)
    exit(1)
finally:
    test_runner.shutdown()


pp = pprint.PrettyPrinter(indent=2)
print('\n========================================')
print(f'Total Db connection attempts: {test_runner.success_connect_count + test_runner.failed_connect_count}')
print(f'Successful Db connections: {test_runner.success_connect_count}')
print(f'Failed Db connections: {test_runner.failed_connect_count}')
print(f'failure_start_time: {time.ctime(test_runner.failure_condition_start_time)}')
print(f'failure_end_time: {time.ctime(test_runner.failure_condition_end_time)}')
duration = int(test_runner.failure_condition_end_time - test_runner.failure_condition_start_time)
print(f'failure condition duration: {duration} seconds')
print(f'Last inserted sync record id on initial primary db node: {test_runner.last_inserted_heartbeat_index}')
print(f'Pre-failure Db node hostname: {pre_failure_db_node_hostname}')
print(f'Post-failure Db node hostname: {post_failure_db_node_hostname}')
print(f'Newest 5 sync records in current primary db node:')
pp.pprint(test_runner.get_last_sync_records(test_run_id, 5))
```