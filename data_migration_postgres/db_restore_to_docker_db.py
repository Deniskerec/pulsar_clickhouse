import os
import subprocess

def restore_database(username, dbname, dump_file_path, password):
    try:
        # Set up the environment with the database password
        env = os.environ.copy()
        env['PGPASSWORD'] = password

        # Construct the pg_restore command
        command = [
            "pg_restore",
            "-U", username,
            "-d", dbname,
            "-h", "localhost",
            dump_file_path
        ]

        # Execute the command and capture output
        result = subprocess.run(command, check=True, shell=False, env=env, text=True, capture_output=True)

        print(f"Database {dbname} restored successfully from {dump_file_path}.")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while restoring the database: {e}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    username = 'pulsar'
    dbname = 'postgres_migration'
    dump_file_path = '/Users/denis/Documents/newAFC_end_2_end/backup/remote_database_backup.dump'  
    password = 'pulsar'  

    restore_database(username, dbname, dump_file_path, password)



