# db_info Directory

This directory contains database configuration files. 
Rename `db_backup_info_template.py` to `db_backup_info.py` and fill in your database details.
Rename `remote_con_template.py` to `remote_con.py` and fill in your database details.


# data_migration/db_info/db_backup_info.py

db_backup_info = {
    'username': 'your_database_username',
    'password': 'your_database_password',
    'host': 'your_database_host',
    'database_name': 'your_database_name',
}

# data_migration/db_info/remote_con.py
DB_NAME = "database_name"
USER = "username"
PASSWORD = "password!"
HOST = "host"