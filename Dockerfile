FROM ubuntu

RUN \
  apt-get install -y zabbix-agent postgresql-client

COPY pg_monz/pg_monz/usr-local-bin/*  /usr/local/bin/
COPY pg_monz/pg_monz/zabbix_agentd.d/userparameter_pgsql.conf /etc/zabbix/zabbix_agentd.conf.d/pg_monz.conf


ENTRYPOINT
