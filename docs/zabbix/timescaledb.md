# Zabbix Server migrating to Postgres with TimescaleDB
## Install TimescaleDB extension
### Add the TimescaleDB third party repository:
```
echo "deb https://packagecloud.io/timescale/timescaledb/debian/ $(lsb_release -c -s) main" | sudo tee /etc/apt/sources.list.d/timescaledb.list
```
### Install TimescaleDB GPG key
```
wget --quiet -O - https://packagecloud.io/timescale/timescaledb/gpgkey | sudo apt-key add -
```
### Update your local repository list:
```
apt update
```
### Install TimescaleDB:
```
apt install timescaledb-2-postgresql-13
```
### Tune your postgres configuration to adopt TimescaleDB
```
timescaledb-tune
```
### Apply changes to postgres
```
systemctl restart postgresql@13-main.service
```
### Stop Zabbix Server
```
systemctl stop zabbix-server.service
systemctl stop php7.4-fpm.service
```
## Enable TimescaleDB extension
```
echo "CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;" | sudo -u postgres psql zabbix
```
Output:
```
WARNING:  
WELCOME TO
 _____ _                               _     ____________  
|_   _(_)                             | |    |  _  \ ___ \ 
  | |  _ _ __ ___   ___  ___  ___ __ _| | ___| | | | |_/ / 
  | | | |  _ ` _ \ / _ \/ __|/ __/ _` | |/ _ \ | | | ___ \ 
  | | | | | | | | |  __/\__ \ (_| (_| | |  __/ |/ /| |_/ /
  |_| |_|_| |_| |_|\___||___/\___\__,_|_|\___|___/ \____/
               Running version 2.10.1
For more information on TimescaleDB, please visit the following links:

 1. Getting started: https://docs.timescale.com/timescaledb/latest/getting-started
 2. API reference documentation: https://docs.timescale.com/api/latest
 3. How TimescaleDB is designed: https://docs.timescale.com/timescaledb/latest/overview/core-concepts

Note: TimescaleDB collects anonymous reports to better understand and assist our users.
For more information and how to disable, please see our docs https://docs.timescale.com/timescaledb/latest/how-to-guides/configuration/telemetry.

CREATE EXTENSION
```
## Run the timescaledb.sql script located in database/postgresql
```
cat /usr/share/zabbix-sql-scripts/postgresql/timescaledb.sql | sudo -u zabbix psql zabbix
```
Output:
```
NOTICE:  PostgreSQL version 13.10 (Debian 13.10-1.pgdg110+1) is valid
NOTICE:  TimescaleDB extension is detected
NOTICE:  TimescaleDB version 2.10.1 is valid
NOTICE:  migrating data to chunks
DETAIL:  Migration might take a while depending on the amount of data.
NOTICE:  migrating data to chunks
DETAIL:  Migration might take a while depending on the amount of data.
WARNING:  column type "character varying" used for "source" does not follow best practices
HINT:  Use datatype TEXT instead.
NOTICE:  migrating data to chunks
DETAIL:  Migration might take a while depending on the amount of data.
WARNING:  column type "character varying" used for "value" does not follow best practices
HINT:  Use datatype TEXT instead.
NOTICE:  migrating data to chunks
DETAIL:  Migration might take a while depending on the amount of data.
NOTICE:  migrating data to chunks
DETAIL:  Migration might take a while depending on the amount of data.
NOTICE:  migrating data to chunks
DETAIL:  Migration might take a while depending on the amount of data.
NOTICE:  TimescaleDB is configured successfully
DO
```
## Sidenotes
In my case with ~730GB DB size and 1TB DB partition size, available space was enought to perform migration to chunks.
```
/dev/sdb1      1007G  726G  230G  76% /pgsql
```
Postgres log:
```
2023-04-12 06:44:08.623 UTC [2939476] zabbix@zabbix ERROR:  could not extend file "base/370747/925157": No space left on device
2023-04-12 06:44:08.623 UTC [2939476] zabbix@zabbix HINT:  Check free disk space.
2023-04-12 06:44:08.623 UTC [2939476] zabbix@zabbix CONTEXT:  SQL statement "SELECT create_hypertable('history_str', 'clock', chunk_time_interval => 86400, migrate_data => true)"
```
Thus I added .5TB to the partition:
``` 
/dev/sdb1       1.5T  726G  709G  51% /pgsql
```
After the migrattion and a few hours working the DB size is:
```
/dev/sdb1       1.5T   29G  1.4T   2% /pgsql
```
The migration took time between two timestamps (in reality it was a bit less):
```
Thu Apr 13 00:09:06 UTC 2023
Thu Apr 13 05:46:49 UTC 2023
```
Postgres log from the time when the migration failed (no reason why I keep this):
```
2023-04-12 06:44:08.623 UTC [2939476] zabbix@zabbix ERROR:  could not extend file "base/370747/925157": No space left on device
2023-04-12 06:44:08.623 UTC [2939476] zabbix@zabbix HINT:  Check free disk space.
2023-04-12 06:44:08.623 UTC [2939476] zabbix@zabbix CONTEXT:  SQL statement "SELECT create_hypertable('history_str', 'clock', chunk_time_interval => 86400, migrate_data => true)"
        PL/pgSQL function inline_code_block line 63 at PERFORM
2023-04-12 06:44:08.623 UTC [2939476] zabbix@zabbix STATEMENT:  DO $$
        DECLARE
                minimum_postgres_version_major          INTEGER;
                minimum_postgres_version_minor          INTEGER;
                current_postgres_version_major          INTEGER;
                current_postgres_version_minor          INTEGER;
                current_postgres_version_full           VARCHAR;
        
                minimum_timescaledb_version_major       INTEGER;
                minimum_timescaledb_version_minor       INTEGER;
                current_timescaledb_version_major       INTEGER;
                current_timescaledb_version_minor       INTEGER;
                current_timescaledb_version_full        VARCHAR;
        BEGIN
                SELECT 10 INTO minimum_postgres_version_major;
                SELECT 2 INTO minimum_postgres_version_minor;
                SELECT 1 INTO minimum_timescaledb_version_major;
                SELECT 5 INTO minimum_timescaledb_version_minor;
        
                SHOW server_version INTO current_postgres_version_full;
        
                IF NOT found THEN
                        RAISE EXCEPTION 'Cannot determine PostgreSQL version, aborting';
                END IF;
        
                SELECT substring(current_postgres_version_full, '^(\d+).') INTO current_postgres_version_major;
                SELECT substring(current_postgres_version_full, '^\d+.(\d+)') INTO current_postgres_version_minor;
        
                IF (current_postgres_version_major < minimum_postgres_version_major OR
                                (current_postgres_version_major = minimum_postgres_version_major AND
                                current_postgres_version_minor < minimum_postgres_version_minor)) THEN
                                RAISE EXCEPTION 'PostgreSQL version % is NOT SUPPORTED (with TimescaleDB)! Minimum is %.%.0 !',
                                                current_postgres_version_full, minimum_postgres_version_major,
                                                minimum_postgres_version_minor;
                ELSE
                        RAISE NOTICE 'PostgreSQL version % is valid', current_postgres_version_full;
                END IF;
        
                SELECT extversion INTO current_timescaledb_version_full FROM pg_extension WHERE extname = 'timescaledb';
        
                IF NOT found THEN
                        RAISE EXCEPTION 'TimescaleDB extension is not installed';
                ELSE
                        RAISE NOTICE 'TimescaleDB extension is detected';
                END IF;
        
                SELECT substring(current_timescaledb_version_full, '^(\d+).') INTO current_timescaledb_version_major;
                SELECT substring(current_timescaledb_version_full, '^\d+.(\d+)') INTO current_timescaledb_version_minor;

        
                IF (current_timescaledb_version_major < minimum_timescaledb_version_major OR
                                (current_timescaledb_version_major = minimum_timescaledb_version_major AND
                                current_timescaledb_version_minor < minimum_timescaledb_version_minor)) THEN
                        RAISE EXCEPTION 'TimescaleDB version % is UNSUPPORTED! Minimum is %.%.0!',
                                        current_timescaledb_version_full, minimum_timescaledb_version_major,
                                        minimum_timescaledb_version_minor;
                ELSE
                        RAISE NOTICE 'TimescaleDB version % is valid', current_timescaledb_version_full;
                END IF;
                PERFORM create_hypertable('history', 'clock', chunk_time_interval => 86400, migrate_data => true);
                PERFORM create_hypertable('history_uint', 'clock', chunk_time_interval => 86400, migrate_data => true);
                PERFORM create_hypertable('history_log', 'clock', chunk_time_interval => 86400, migrate_data => true);
                PERFORM create_hypertable('history_text', 'clock', chunk_time_interval => 86400, migrate_data => true);
                PERFORM create_hypertable('history_str', 'clock', chunk_time_interval => 86400, migrate_data => true);
                PERFORM create_hypertable('trends', 'clock', chunk_time_interval => 2592000, migrate_data => true);
                PERFORM create_hypertable('trends_uint', 'clock', chunk_time_interval => 2592000, migrate_data => true);
                UPDATE config SET db_extension='timescaledb',hk_history_global=1,hk_trends_global=1;
                UPDATE config SET compression_status=1,compress_older='7d';
                RAISE NOTICE 'TimescaleDB is configured successfully';
        END $$;
```
