Really simple [pg_monz](https://github.com/pg-monz/pg_monz) implementation in docker

If you dont have auto-disovery configured, you are going to have to add a host manualy, in this example the Zabbix Agent's host is called `pg_monz`.  Then if you have zabbix running in a docker container named `zabbix` and a 
PostgreSQL server running in a container named `postgres` then you can run 
the container with something like this:

```
docker run -d --hostname pg_monz --name pg_monz \
 --link zabbix:zabbix \
 --link postgres:postgres \
 croepha/docker-pg-monz
```

Then in Zabbix web admin you need to import the template 
[Template_App_PostgreSQL.xml](./pg_monz/pg_monz/template/Template_App_PostgreSQL.xml).
Also, setup PostgreSQL template to the host.

For most people, that should be it.  By default it looks for zabbix and 
postgres instances linked as `zabbix`  and `postgres`.  But you can set these
environmental variables for customization:

|Variable Name| Description                                          | Default | 
|----------|---------------------------------------------------------|------------|
| `PGROLE` | Username for connecting to the postgres server | `postgres` |
| `PGPASS` | Password for connecting to the postgres server | None |
| `PGHOST` | Address of the postgres server if not using a linked container | `postgres` |
| `PGPORT` | Port for connecting to posgres | `5432` |
| `PGDATABASE` | Maintenace DB for postgres, Not the DB of your App | `postgres` |
| `ZBXHOST` | Address of the Zabbix server if not using a linked container | `zabbix` |
| `ZBXPORT` | Port of the Zabbix server if not using a linked container | Blank, but zabbix defaults to 10050 |


