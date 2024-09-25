###### back to repo's main [README.md](../../README.md)
#### back to DB root page [db.md](./db.md)
#### PSQL specific hints
##### Configuration reload making changes to pg_hba.conf
```
SELECT pg_reload_conf();
```

##### Show the size of all tables in the schema *public*
```
select
  table_name,
  pg_size_pretty(pg_total_relation_size(quote_ident(table_name))),
  pg_total_relation_size(quote_ident(table_name))
from information_schema.tables
where table_schema = 'public'
order by 3 desc;
```

##### Show the size of all tables in multiple schemas
```
select 
  table_schema, 
  table_name,
  pg_relation_size('"'||table_schema||'"."'||table_name||'"')
from information_schema.tables
order by 3 desc;
```
