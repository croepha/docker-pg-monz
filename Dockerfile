FROM ubuntu

RUN apt-get install -y  wget postgresql-client \
  && wget http://repo.zabbix.com/zabbix/3.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_3.0-1+trusty_all.deb \
  && dpkg -i zabbix-release_3.0-1+trusty_all.deb \
  && rm -v zabbix-release_3.0-1+trusty_all.deb \
  && apt-get update \
  && apt-get install -y zabbix-agent zabbix-sender

COPY pg_monz/pg_monz/usr-local-bin/* entrypoint.py /usr/local/bin/
COPY pg_monz/pg_monz/zabbix_agentd.d/userparameter_pgsql.conf /etc/zabbix/zabbix_agentd.d/pg_monz.conf

ENTRYPOINT ["entrypoint.py"]
