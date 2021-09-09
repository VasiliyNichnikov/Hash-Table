class DeletedNodeBook:
    node = None

    @staticmethod
    def get():
        if DeletedNodeBook.node is None:
            DeletedNodeBook.node = DeletedNodeBook
        return DeletedNodeBook.node
