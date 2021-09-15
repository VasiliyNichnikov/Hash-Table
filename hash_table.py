from abc import ABC, abstractmethod


class HashTable(ABC):
    @abstractmethod
    def insert(self, isbn: int, author: str, title: str) -> None:
        pass

    @abstractmethod
    def delete(self, isbn: int) -> None:
        pass
