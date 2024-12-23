
class Book:
    _instanse = {}

    def __new__(cls, title, author):
        key = (title, author)
        if key in cls._instanse:
            print('книга уже существует')
            return cls._instanse[key]
        instanse = super().__new__(cls)
        cls._instanse[key] = instanse
        return instanse

    def __init__(self,author, title):
        self.author = author
        self.title = title
        self.counter = 0

    def __str__(self):
        return f'книга {self.title}, автора {self.author} '

ex = Book('python', 'bob')
ex2 = Book('python', 'bob')
print(ex)
print(ex2)
print(id(ex), id(ex2))
print(locals())

