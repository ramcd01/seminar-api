import mysql.connector
import os

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "1234"),
        database=os.getenv("DB_NAME", "seminar_db")
    )
