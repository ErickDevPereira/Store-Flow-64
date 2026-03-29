from mysql.connector import MySQLConnectionAbstract
from src.backend.config.db_settings.rsc import Cursor
from .plant import Plant

class Categories(Plant):

    def __create_categories_table(self, scnx: MySQLConnectionAbstract) -> None:
        with Cursor(scnx) as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS categories (
                    category_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                    category_name VARCHAR(50) NOT NULL,
                    description VARCHAR(255) NOT NULL,
                    store_id INT UNSIGNED NOT NULL,
                    FOREIGN KEY (store_id) REFERENCES stores (store_id)
                )
            """)
    
    def initialize(self, scnx: MySQLConnectionAbstract) -> None:
        self.__create_categories_table(scnx) #Initializing the categories table