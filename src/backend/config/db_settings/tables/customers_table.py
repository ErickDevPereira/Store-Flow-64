from mysql.connector import MySQLConnectionAbstract
from src.backend.config.db_settings.rsc import Cursor
from .plant import Plant

class Customers(Plant):

    def __create_customers_table(self, scnx: MySQLConnectionAbstract) -> None:
        with Cursor(scnx) as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS customers (
                    customer_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                    first_name VARCHAR(50) NOT NULL,
                    last_name VARCHAR(50) NOT NULL,
                    city VARCHAR(30),
                    country VARCHAR(20),
                    adress VARCHAR(255),
                    phone VARCHAR(30),
                    sex ENUM("M", "F"),
                    store_id INT UNSIGNED NOT NULL,
                    FOREIGN KEY (store_id) REFERENCES stores (store_id)
                )
            """)
    
    def initialize(self, scnx: MySQLConnectionAbstract) -> None:
        self.__create_customers_table(scnx) #Initializing the customers table