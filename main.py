from storage import INFO_BOOKS
from hash_table import HashTable
from open_address_hash_table import OpenAddressHashTable


def run():
    hash_table: HashTable = OpenAddressHashTable()

    for book in INFO_BOOKS:
        hash_table.insert(book['isbn'], book['author'], book['title'])
    print(hash_table)


if __name__ == '__main__':
    run()
