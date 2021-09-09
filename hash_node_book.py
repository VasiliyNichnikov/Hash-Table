class HashNodeBook(object):
    @property
    def isbn(self) -> int:
        return self.__isbn

    @property
    def author(self) -> str:
        return self.__author

    @property
    def title(self) -> str:
        return self.__title

    def __init__(self, isbn: int, author: str, title: str) -> None:
        self.__isbn = isbn
        self.__author = author
        self.__title = title
