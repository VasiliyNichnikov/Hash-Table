import typing
from hash_table import HashTable
from hash_node_book import HashNodeBook
from deleted_node_book import DeletedNodeBook


class OpenAddressHashTable(HashTable):
    __size: int = 0
    __capacity: int = 10
    __C: int = 11
    __REHASH = 1
    __table: typing.List[HashNodeBook] = []

    def __init__(self):
        self.__size = 0
        for i in range(self.__capacity):
            self.__table.append(None)

    def insert(self, isbn: int, author: str, title: str) -> None:
        if self.__REHASH <= (self.__size / self.__capacity):
            self.__rehash()

        hash_result: int = (isbn * self.__C) % self.__capacity
        while self.__table[hash_result] is not None and not isinstance(self.__table[hash_result], DeletedNodeBook):
            hash_result = (hash_result + 1) % self.__capacity
        self.__table[hash_result] = HashNodeBook(isbn, author, title)
        self.__size += 1

    def __rehash(self):
        new_capacity: int = self.__capacity * 2
        new_table: typing.List[HashNodeBook] = []
        for i in range(self.__capacity):
            if self.__table[i] is not None:
                hash_result: int = (self.__table[i].isbn * self.__C) % new_capacity
                while new_table[hash_result] is not None and not isinstance(self.__table[hash_result], DeletedNodeBook):
                    hash_result = (hash_result + 1) % self.__capacity
                new_table[hash_result] = HashNodeBook(self.__table[i].isbn, self.__table[i].author,
                                                      self.__table[i].author)
        self.__capacity = new_capacity
        self.__table = new_table

    def delete(self, isbn: int) -> None:
        hash_result: int = (isbn * self.__C) % self.__capacity
        while self.__table[hash_result] is not None:
            if self.__table[hash_result].isbn == isbn:
                self.__table[hash_result] = DeletedNodeBook.get()
                self.__size -= 1
                return
            hash_result = (hash_result + 1) % self.__capacity

    def __str__(self) -> str:
        output: str = ""
        for element in self.__table:
            if element is not None:
                output += f'Book. ISBN: {element.isbn}; Author: {element.author}; Title: {element.title} \n'
        return output

    def output_all_elements(self) -> None:
        pass
