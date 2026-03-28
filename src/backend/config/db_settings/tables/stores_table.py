from mysql.connector import MySQLConnectionAbstract
from mysql.connector.errors import ProgrammingError
from src.backend.config.db_settings.rsc import Cursor
from .plant import Plant

class Stores(Plant):

    def __create_stores_table(self, scnx: MySQLConnectionAbstract) -> None:
        with Cursor(scnx) as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS stores (
                    store_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                    company_name VARCHAR(50) NOT NULL,
                    uid INT UNSIGNED NOT NULL,
                    registration_date DATE NOT NULL,
                    FOREIGN KEY(uid) REFERENCES users(uid)
                )
            """)
    
    def initialize(self, scnx: MySQLConnectionAbstract) -> None:
        self.__create_stores_table(scnx) #Initializing the stores table