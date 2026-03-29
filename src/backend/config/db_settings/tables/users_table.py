from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.errors import ProgrammingError
from src.backend.config.db_settings.rsc import Cursor
from .plant import Plant

class Users(Plant):

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
    
    def initialize(self, scnx: MySQLConnectionAbstract) -> None:
        self.__create_user_table(scnx) #Initializing the users table
        self.__create_indexes_user_table(scnx) #Initializing the indexes of the user table.