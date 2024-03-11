import os
import subprocess
from db_info import db_backup_info

def backup_database(config, backup_file_name):
    try:
        env = dict(PGPASSWORD=config['password'], **os.environ)
        command = [
            "pg_dump",
            "-U", config['username'],
            "-h", config['host'],
            "-d", config['database_name'],
            "-F", "c",
            "-f", backup_file_name + ".dump"
        ]

        # Using subprocess.run with a timeout of 600 seconds (10 minutes)
        subprocess.run(command, shell=False, env=env, check=True, timeout=600)
        print(f"Backup of {config['database_name']} was successful. File saved as {backup_file_name}.dump")
    except subprocess.TimeoutExpired:
        print(f"Backup process timed out after 10 minutes.")
    except subprocess.CalledProcessError as e:
        print(f"Backup failed with error code {e.returncode}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    config = db_backup_info.db_backup_info
    backup_file_name = "remote_database_backup"

    # Ensure environment variable for security
    if 'password' not in config:
        print("Database password is not provided in the configuration. Please check your db_backup_info.py file.")
    else:
        backup_database(config, backup_file_name)


