from mysql.connector import MySQLConnectionAbstract
from src.backend.config.db_settings.rsc import Cursor
from .plant import Plant

class Orders(Plant):

    def __create_orders_table(self, scnx: MySQLConnectionAbstract) -> None:
        with Cursor(scnx) as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS orders (
                    orders_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                    customer_id INT UNSIGNED NOT NULL,
                    purchase_date DATE NOT NULL,
                    online_purchase ENUM("ON", "OFF") NOT NULL,
                    store_id INT UNSIGNED NOT NULL,
                    shipped_date DATE,
                    catched_date DATE,
                    product_id INT UNSIGNED NOT NULL,
                    quantity_bought INT UNSIGNED NOT NULL,
                    employee_id INT UNSIGNED NOT NULL,
                    FOREIGN KEY (store_id) REFERENCES stores (store_id),
                    FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
                    FOREIGN KEY (product_id) REFERENCES products (product_id),
                    FOREIGN KEY (employee_id) REFERENCES employees (employee_id)
                )
            """)
    
    def initialize(self, scnx: MySQLConnectionAbstract) -> None:
        self.__create_orders_table(scnx) #Initializing the orders table