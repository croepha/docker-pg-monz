Really simple pg_monz implementation in docker

To build:

1. clone this repo
2. `docker build -t docker-pg-monz docker-pg-monz`

If you have zabbix running in a docker container named `zabbix` and a 
PostgreSQL server running in a container named `postgres` then you can run 
the container with something like this:

```
docker run -d --hostname pg_monz --name pg_monz \
 --link zabbix:zabbix \
 --link postgres:postgres \
 docker-pg-monz
```

Then in Zabbix web admin you need to import the template 
[Template_App_PostgreSQL.xml](./pg_monz/pg_monz/template/Template_App_PostgreSQL.xml) 

For most people, that should be it.  By default it looks for zabbix and 
postgres instances linked as `zabbix`  and `postgres`.  There are some 
environmental vars that can be set to override default behavior, such as 
ports and hostnames, see [entrypoint.py](entrypoint.py) for the details.
