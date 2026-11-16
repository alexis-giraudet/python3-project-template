from abc import ABC, abstractmethod

__version__ = "1.0.0"


class AbstractDisplay(ABC):
    ENTRY_POINT_GROUP = "mynamespace.display"

    @property
    @abstractmethod
    def version(self) -> str: ...

    @abstractmethod
    def display(self, text: str) -> None: ...
