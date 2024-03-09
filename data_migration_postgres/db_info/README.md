# Database Configuration Information

This directory facilitates the setup of database connections necessary for the application's operation, encompassing both local and remote database configurations.

## Configuration Instructions

Within this directory, you'll find template and example files intended to guide you in configuring your database connections. For security reasons, actual configuration files containing sensitive information should not be committed to version control.

### Steps to Configure Database Connections

#### 1. Database Backup Configuration

- **Template File**: `db_backup_info_template.py`
   - Duplicate this file and rename the copy to `db_backup_info.py`.
   - Edit `db_backup_info.py` to include your database backup credentials:
     ```python
     db_backup_info = {
         'username': '<your_username>',
         'password': '<your_password>',
         'host': '<your_host>',
         'database_name': '<your_database_name>',
     }
     ```

#### 2. Remote Database Connection

- **Example Configuration**: `remote_con_template.py`
   - This file is a placeholder illustrating how a remote database connection configuration might look. **Do not use real credentials** in this or any file committed to version control.
   - Create a new file named `remote_con.py` and populate it with actual connection details relevant to your environment.
       ```python
    DB_NAME = "<database_name>"
    USER = "<database_user>"
    PASSWORD = "<database_password>"
    HOST = "<database_host>"
    ```

## Security Notice

- **DO NOT COMMIT SENSITIVE DATA**: Ensure that files containing real credentials (`db_backup_info.py`, `remote_con.py`) are listed in your `.gitignore` to prevent them from being accidentally committed to the repository.
- The `remote_con_template.py` serves as an example. Replace placeholder values with actual data in a securely managed `remote_con.py` file, which should never be shared or committed.

