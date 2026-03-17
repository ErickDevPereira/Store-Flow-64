from .rsc import WeakConnection, StrongConnection, Cursor

class DatabaseInitializer:

    def __init__(self, user: str, password: str, db_name: str = "store_data_manager_db"):
        self.__user: str = user
        self.__password: str = password
        self.__db_name: str = db_name
        self.__create_database()
        self.__create_user_table()

    def __create_database(self) -> None:
        with WeakConnection(self.__user, self.__password) as wcnx:
            with Cursor(wcnx) as cursor:
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.__db_name}")
    
    def __create_user_table(self) -> None:
        with StrongConnection(self.__user, self.__password, self.__db_name) as scnx:
            with Cursor(scnx) as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        uid INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                        wkz_password VARCHAR(500) NOT NULL,
                        first_name VARCHAR(100) NOT NULL,
                        last_name VARCHAR(100) NOT NULL,
                        email VARCHAR(100) NOT NULL,
                        birthdate DATE NOT NULL,
                        CONSTRAINT email_checker CHECK (email LIKE "%_@_%.com"),
                        CONSTRAINT email_uni UNIQUE( email )
                    )
                """)