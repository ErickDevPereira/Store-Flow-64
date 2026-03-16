from mysql.connector import connect, MySQLConnectionAbstract
from .connection import Connection

class StrongConnection(Connection):

    def __init__(self, user: str, password: str, db_name: str):
        super().__init__(user, password)
        self.__db_name: str = db_name
    
    def __enter__(self) -> MySQLConnectionAbstract:
        self.__cnx: MySQLConnectionAbstract = connect(
            user = self.user,
            password = self.password,
            host = "localhost",
            database = self.__db_name
        )
        return self.__cnx #Allocating a strong connection

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        self.__cnx.close() #Closing the strong connection