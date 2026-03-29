from .rsc import WeakConnection, StrongConnection, Cursor
import os
from mysql.connector.errors import ProgrammingError
from mysql.connector.abstracts import MySQLConnectionAbstract
from .tables import Users, Stores, Plant, Customers, Suppliers, Categories, Products
from typing import List

class Database:

    def __init__(self,
                user: str = os.getenv("MYSQL_USER"),
                password: str = os.getenv("MYSQL_PASSWORD"),
                db_name: str = os.getenv("DB_NAME")):
        self.__user: str = user
        self.__password: str = password
        self.__db_name: str = db_name
        self.__tables: List[Plant] = [
            Users(),
            Stores(),
            Customers(),
            Suppliers(),
            Categories(),
            Products()
            ] #Getting the tables. Note that the Liskov Principle has been followed here.
    
    def start_db(self) -> None:
        self.__create_database()
        with StrongConnection(self.__user, self.__password, self.__db_name) as scnx:
            for table in self.__tables:
                table.initialize(scnx)

    def __create_database(self) -> None:
        with WeakConnection(self.__user, self.__password) as wcnx:
            with Cursor(wcnx) as cursor:
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.__db_name}")