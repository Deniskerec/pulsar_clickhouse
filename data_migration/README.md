
# `db_info` Directory Setup Instructions

This directory is crucial for configuring the database connections required for the application's data operations. Follow these steps to set up the database configuration files properly.

## Configuration Steps

1. **Database Connection Information**:
   - Copy `remote_con_template.py` to a new file named `remote_con.py`.
   - Edit `remote_con.py` with the actual remote database connection details.

2. **Database Backup Configuration**:
   - Duplicate `db_backup_info_template.py` to create `db_backup_info.py`.
   - Modify `db_backup_info.py` to include your database backup settings.

Ensure you do not commit the actual configuration files (`remote_con.py`, `db_backup_info.py`) to the repository. These files should be listed in your `.gitignore` to prevent accidental inclusion.

# Project Scripts Documentation

This project includes several Python scripts to handle database backups and data migration. Below is a brief overview of each script's purpose and functionality.

## `db_backup.py`

- **Purpose**: Backs up the company database.
- **Usage**:
  ```bash
  python db_backup.py
  ```
- This script utilizes the PostgreSQL `pg_dump` utility to create a backup of the database. Ensure that the database connection details are correctly set up in `db_backup_info.py`.

## `migrate_local_psql_to_clickhouse.py`

- **Purpose**: Migrates data from a local PostgreSQL database to ClickHouse.
- **Usage**:
  ```bash
  python migrate_local_psql_to_clickhouse.py
  ```
- Before running this script, ensure that both your local PostgreSQL and ClickHouse database connection details are configured correctly. The script reads data from PostgreSQL, processes it, and inserts it into ClickHouse, adhering to the ClickHouse schema.

## `migrate_remote_psql_data_specific_table.py`

- **Purpose**: Migrates data from a specific table in a remote PostgreSQL database.
- **Usage**:
  ```bash
  python migrate_remote_psql_data_specific_table.py
  ```
- This script is designed for targeted data migration, focusing on a specific table. It requires proper configuration of the remote database connection parameters in `remote_con.py`.

---
## pg_dump 

  ```bash
pg_dump -U postgres -h localhost -d database_name -F c -f backup_file_name.dump
  ```

## scp
  ```bash
scp razvoj@IP:/home/razvoj/backup_file_name.dump /Users/denis/Documents/newAFC_end_2_end
  ```


## pg_restore

If your backup file is in the custom format (.dump), use pg_restore:

  ```bash
pg_restore -U postgres -d new_database_name -h localhost -F c /path/to/your/backup_file_name.dump
  ```bash
in my case 
  ```bash
pg_restore -U pulsar -d afc_restored_database -h localhost -F c /Users/denis/Documents/newAFC_end_2_end/backup_file_name.dump
  ```

If your backup is a plain SQL file, use psql:

  ```bash
  psql -U postgres -d new_database_name -h localhost -f /path/to/your/backup_file_name.sql
  ```

# Additional Notes

- **Security**: Keep your database credentials secure and confidential. Do not commit sensitive information to the repository.
- **Dependencies**: Install all required dependencies as specified in the project's root `README.md` or `requirements.txt` file.
- **Support**: If you encounter any issues or require further assistance, please refer to the main project documentation or contact the development team.
```


pg_restore -U pulsar -d afc_restored_database -h localhost -F c /Users/denis/Documents/newAFC_end_2_end/backup_file_name.dump

