import mysql.connector as connector
import os 
from dotenv import load_dotenv
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_DIR / ".env")

def get_connection():
    connection = connector.connect(
        host = os.environ["MYSQL_HOST"],
        user = os.environ["MYSQL_USER"],
        password = os.environ["MYSQL_PASSWORD"],
        port = int(os.getenv("MYSQL_PORT", "3306")),
        database = os.environ["MYSQL_DATABASE"],
    )

    return connection
    



    