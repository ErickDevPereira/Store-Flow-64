from .rsc import WeakConnection, StrongConnection, Cursor
import os
from mysql.connector.errors import ProgrammingError
from mysql.connector.abstracts import MySQLConnectionAbstract

class Database:

    def __init__(self,
                user: str = os.getenv("MYSQL_USER"),
                password: str = os.getenv("MYSQL_PASSWORD"),
                db_name: str = os.getenv("DB_NAME")):
        self.__user: str = user
        self.__password: str = password
        self.__db_name: str = db_name
    
    def start_db(self) -> None:
        self.__create_database()
        with StrongConnection(self.__user, self.__password, self.__db_name) as scnx:
            self.__create_user_table(scnx)
            self.__create_indexes_user_table(scnx)

    def __create_database(self) -> None:
        with WeakConnection(self.__user, self.__password) as wcnx:
            with Cursor(wcnx) as cursor:
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.__db_name}")
    
    def __create_user_table(self, scnx: MySQLConnectionAbstract) -> None:
        with Cursor(scnx) as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    uid INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                    wzg_password VARCHAR(500) NOT NULL,
                    first_name VARCHAR(100) NOT NULL,
                    last_name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) NOT NULL,
                    birthdate DATE NOT NULL,
                    CONSTRAINT email_checker CHECK (email LIKE "%_@_%.com"),
                    CONSTRAINT email_uni UNIQUE( email )
                )
            """)
    
    def __create_indexes_user_table(self, scnx: MySQLConnectionAbstract) -> None:
        for field in ("email",):
            with Cursor(scnx) as cursor:
                try:
                    cursor.execute(f"CREATE INDEX ind_{field} ON users({field})") #Creating indexes over users table
                except ProgrammingError:
                    pass #We reach this region if the index already exists, so we don't need to do nothing