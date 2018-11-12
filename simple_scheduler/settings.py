"""Settings to override default settings."""

import logging

#
# Override settings
#
DEBUG = True

HTTP_PORT = 8888
HTTP_ADDRESS = '0.0.0.0'

# Rome TZ
TIMEZONE = 'Europe/Rome'


# Override persistence settings

# SQLite
#
DATABASE_CLASS = 'ndscheduler.core.datastore.providers.sqlite.DatastoreSqlite'
DATABASE_CONFIG_DICT = {
    'file_path': '/app/data/datastore.db'
}

# MySQL
#
# DATABASE_CLASS = 'ndscheduler.core.datastore.providers.mysql.DatastoreMysql'
# DATABASE_CONFIG_DICT = {
#     'user': 'ndscheduler',
#     'password': 'password',
#     'hostname': 'mysql',
#     'port': 3306,
#     'database': 'scheduler'
# }

#
# Set logging level
#
logging.getLogger().setLevel(logging.DEBUG)

JOB_CLASS_PACKAGES = ['simple_scheduler.jobs']
