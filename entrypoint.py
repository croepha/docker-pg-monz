#!/usr/bin/env python3

import os

PGHOST = os.environ.get('PGHOST', 'postgres')
PGPORT = os.environ.get('PGPORT', '5432')
PGROLE = os.environ.get('PGROLE', 'postgres')
PGDATABASE = os.environ.get('PGDATABASE', 'postgres')
PGPASS = os.environ.get('PGPASS', '')

ZBXHOST = os.environ.get('ZBXHOST', 'zabbix')
ZBXPORT = os.environ.get('ZBXPORT', '')

if ZBXPORT:
    ZBXPORT = ':' + ZBXPORT


PGPASSFILE = os.environ.get('PGPASSFILE', '/usr/local/etc/pgpass')
os.environ["PGPASSFILE"] = PGPASSFILE
pgsql_conf = '/usr/local/etc/pgsql_func.conf'
zbx_conf = '/etc/zabbix/zabbix_agentd.conf'

pgsql_conf_template = """
PGHOST=%s
PGPORT=%s
PGROLE=%s
PGDATABASE=%s
"""

if PGPASS:
    with open(PGPASSFILE, 'w') as f:
        f.write('%s:%s:%s:%s:%s\n' % (
            PGHOST, PGPORT, PGDATABASE, PGROLE, PGPASS
        ))

with open(pgsql_conf, 'w') as f:
    f.write(pgsql_conf_template % (
        PGHOST, PGPORT, PGROLE, PGDATABASE
    ))

with open(zbx_conf, 'r') as f:
    zbx_conf_data = f.readlines()

with open(zbx_conf, 'w') as f:
    for line in zbx_conf_data:
        if not line.strip().startswith((
            'Hostname=',
            'ServerActive=',
            'Server='
        )):
            f.write(line)
    f.write('ServerActive=%s%s\n' % (ZBXHOST, ZBXPORT))
    f.write('AllowRoot=1\n')
    f.write('LogType=console\n')
    f.write('Server=%s\n' % ZBXHOST)

os.makedirs('/var/run/zabbix', exist_ok=True)

os.execlp('zabbix_agentd', 'zabbix_agentd', '--foreground')
