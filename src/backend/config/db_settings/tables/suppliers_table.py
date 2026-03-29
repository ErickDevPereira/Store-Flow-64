from mysql.connector import MySQLConnectionAbstract
from src.backend.config.db_settings.rsc import Cursor
from .plant import Plant

class Suppliers(Plant):

    def __create_sup_table(self, scnx: MySQLConnectionAbstract) -> None:
        with Cursor(scnx) as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS suppliers (
                    supplier_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                    company_name VARCHAR(50) NOT NULL,
                    country VARCHAR(20) NOT NULL,
                    city VARCHAR(30) NOT NULL,
                    phone VARCHAR(30) NOT NULL,
                    address VARCHAR(255) NOT NULL,
                    store_id INT UNSIGNED NOT NULL,
                    FOREIGN KEY (store_id) REFERENCES stores (store_id)
                )
            """)
    
    def initialize(self, scnx: MySQLConnectionAbstract) -> None:
        self.__create_sup_table(scnx) #Initializing the suppliers table