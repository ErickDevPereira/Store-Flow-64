from typing import Any
from mysql.connector import MySQLConnectionAbstract

class Cursor:

    def __init__(self, cnx: MySQLConnectionAbstract):
        self.__cnx: MySQLConnectionAbstract = cnx
    
    def __enter__(self) -> Any:
        self.__cursor: Any = self.__cnx.cursor()
        return self.__cursor
    
    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        self.__cursor.close()