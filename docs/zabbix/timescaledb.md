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
NOTICE:  PostgreSQL version 13.10 (Debian 13.10-1.pgdg110+1) is valid
NOTICE:  TimescaleDB extension is detected
NOTICE:  TimescaleDB version 2.10.1 is valid
NOTICE:  migrating data to chunks
DETAIL:  Migration might take a while depending on the amount of data.
```
