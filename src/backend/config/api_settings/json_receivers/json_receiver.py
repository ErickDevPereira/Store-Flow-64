from abc import ABC, abstractmethod
from flask_restful.reqparse import Namespace

class JsonReceiver(ABC):

    @abstractmethod
    def create_args(self) -> None: pass

    @abstractmethod
    def set_arguments(self) -> None: pass

    @abstractmethod
    def get_args(self) -> Namespace: pass