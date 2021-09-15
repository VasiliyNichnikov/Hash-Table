import random


class GenerationISBN:
    @staticmethod
    def get(length=12) -> int:
        return random.randint(10 ** (length - 1), 10 ** length - 1)
