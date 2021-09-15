import random
from storage import BOOKS
from hash_table import HashTable
from generation_isbn import GenerationISBN
from open_address_hash_table import OpenAddressHashTable


def get_info_book(generation_isbn: bool = True) -> (int, str, str):
    book = BOOKS[random.randint(0, len(BOOKS) - 1)]

    isbn = 0
    if generation_isbn:
        isbn = GenerationISBN.get()
    author = book["author"]
    title = book["title"]
    return isbn, author, title


def run():
    hash_table: HashTable = OpenAddressHashTable()

    while True:
        print("----------------------------------------------------------------")
        action: int = int(input("1) Add Book.\n"
                                "2) Delete Book.\n"
                                "3) Output all books.\n"
                                "4) Edit a book by ISBN.\n"
                                "5) Exit.\nSelect an actions: "))
        if 1 <= action <= 5:
            print()
            if action == 1:
                isbn, author, title = get_info_book()
                hash_table.insert(isbn, author, title)
                print(f"The book was added successfully.\nISBN: {isbn};\nAuthor: {author};\nTitle: {title};")
            elif action == 2:
                isbn: int = int(input("Enter the ISBN of the book you want to delete: "))
                delete_state = hash_table.delete(isbn)
                if delete_state is False:
                    print("Error when deleting the book.")
                else:
                    print("The book was successfully deleted.")
            elif action == 3:
                print(hash_table)
            elif action == 4:
                isbn: int = int(input("Enter the ISBN of the book you want to change: "))
                zero, author, title = get_info_book(False)
                hash_table.insert(isbn, author, title)
                print(f"The changes were successful. New data. Author: {author}; Title: {title};")
            elif action == 5:
                break
        else:
            print("Error there is no such command.")
    print("End")


if __name__ == '__main__':
    run()
