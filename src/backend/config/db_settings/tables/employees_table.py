from mysql.connector.abstracts import MySQLConnectionAbstract
from src.backend.config.db_settings.rsc import Cursor
from .plant import Plant

class Employees(Plant):

    def __create_emp_table(self, scnx: MySQLConnectionAbstract) -> None:
        with Cursor(scnx) as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS employees (
                    employee_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                    first_name VARCHAR(50) NOT NULL,
                    last_name VARCHAR(50) NOT NULL,
                    city VARCHAR(30) NOT NULL,
                    country VARCHAR(20) NOT NULL,
                    adress VARCHAR(255) NOT NULL,
                    phone VARCHAR(30) NOT NULL,
                    sex ENUM("M", "F"),
                    store_id INT UNSIGNED NOT NULL,
                    hire_date DATE NOT NULL,
                    FOREIGN KEY (store_id) REFERENCES stores (store_id)
                )
            """)
    
    def initialize(self, scnx: MySQLConnectionAbstract) -> None:
        self.__create_emp_table(scnx) #Initializing the customers table