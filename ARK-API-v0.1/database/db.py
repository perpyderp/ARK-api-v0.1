
import mysql.connector
import os
from dotenv import load_dotenv

connection = None
cursor = None

# Connects to MySQL Database
def connect():
    global connection, cursor
    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    load_dotenv(dotenv_path=dotenv_path)
    HOST = os.getenv('DB_HOST')
    # port = os.getenv('DB_PORT')
    USERNAME = os.getenv('DB_USER')
    PASSWORD = os.getenv('DB_PASSWORD')
    DATABASE = os.getenv('DB_NAME')
    connection = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        password=PASSWORD,
        database=DATABASE
    )
    cursor = connection.cursor()

# Closes connection to database
def disconnect():
    global connection, cursor
    cursor.close()
    connection.close()
