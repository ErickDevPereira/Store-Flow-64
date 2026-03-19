from mysql.connector.abstracts import MySQLConnectionAbstract
from abc import ABC, abstractmethod

class Connection(ABC):

    def __init__(self, user: str, password: str):
        self.user: str = user
        self.password: str = password

    @abstractmethod
    def __enter__(self) -> MySQLConnectionAbstract: pass
    #Note that I've used MySQLConnectionAbstract as the returning type. This class is an interface at which the connection classes will inherit from.
    #It allows me to work with DIP (Dependency Inversion Principle) from SOLID principles.

    @abstractmethod
    def __exit__(self) -> None: pass