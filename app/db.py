import mariadb
import os

def get_db_connection():
    try:
        conn = mariadb.connect(
            host=os.getenv("DB_HOST", "db"),
            port=3306,
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "mysecretpassword"),
            database=os.getenv("DB_NAME", "seminar_db")
        )
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")
        raise e
