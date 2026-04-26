from abc import ABC, abstractmethod
from flask import Response

class EndpointsEntity(ABC):

    @abstractmethod
    def get(self) -> Response: pass

    @abstractmethod
    def post(self) -> Response: pass

    @abstractmethod
    def patch(self) -> Response: pass

    @abstractmethod
    def delete(self) -> Response: pass