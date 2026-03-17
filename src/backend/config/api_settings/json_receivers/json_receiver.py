from abc import ABC, abstractmethod
from flask_restful import reqparse

class JsonReceiver(ABC):

    @abstractmethod
    def __create_args(self) -> None: pass

    @abstractmethod
    def __set_arguments(self) -> None: pass

    @abstractmethod
    def get_args(self) -> reqparse.RequestParser: pass