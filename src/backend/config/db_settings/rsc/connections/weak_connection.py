from mysql.connector import connect
from mysql.connector.abstracts import MySQLConnectionAbstract
from .connection import Connection

class WeakConnection(Connection):

    def __init__(self, user: str, password: str):
        super().__init__(user, password)
    
    def __enter__(self) -> MySQLConnectionAbstract:
        self.__cnx: MySQLConnectionAbstract = connect(
            user = self.user,
            password = self.password,
            host = "localhost"
        )
        return self.__cnx #Allocating an weak connection

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        self.__cnx.close() #Closing the weak connection