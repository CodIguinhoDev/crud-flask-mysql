import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

def conexao_bd():
        return pymysql.connect(
            host =os.getenv("BD_HOST"),
            port =int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DATABASE")
        )
        