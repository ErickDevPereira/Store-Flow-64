from abc import ABC, abstractmethod

#I've created 3 interfaces in order to accomplish ISP from SOLID principles in a simple way

class Remover(ABC):

    @abstractmethod
    def rm(self) -> None: pass

class Loader(ABC):

    @abstractmethod
    def load(self) -> None: pass

class Getter(ABC):

    @abstractmethod
    def get_entity(self) -> None: pass