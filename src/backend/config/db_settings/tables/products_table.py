from mysql.connector.abstracts import MySQLConnectionAbstract
from src.backend.config.db_settings.rsc import Cursor
from .plant import Plant

class Products(Plant):

    def __create_products_table(self, scnx: MySQLConnectionAbstract) -> None:
        with Cursor(scnx) as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    product_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                    product_name VARCHAR(50) NOT NULL,
                    description VARCHAR(255),
                    category_id INT UNSIGNED NOT NULL,
                    price DECIMAL(8, 2) NOT NULL,
                    supplier_id INT UNSIGNED NOT NULL,
                    store_id INT UNSIGNED NOT NULL,
                    stock_units INT NOT NULL,
                    FOREIGN KEY (store_id) REFERENCES stores (store_id),
                    FOREIGN KEY (category_id) REFERENCES categories (category_id),
                    FOREIGN KEY (supplier_id) REFERENCES suppliers (supplier_id)
                )
            """)
    
    def initialize(self, scnx: MySQLConnectionAbstract) -> None:
        self.__create_products_table(scnx) #Initializing the products table