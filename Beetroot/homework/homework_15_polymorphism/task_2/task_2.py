"""Task 2
Library
Write a class structure that implements a library. Classes:
1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []
Library class
Methods:
- new_book(name: str, year: int, author: Author) - returns an instance of Book
 class and adds the book to the books list for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the
 specified author
- group_by_year(year: int) - returns a list of all the books grouped by the
 specified year
All 3 classes must have a readable __repr__ and __str__ methods.
Also, the book class should have a class variable which holds the amount of
 all existing books
```
class Library:
    pass

class Book:
    pass

class Author:
    pass
```"""
import datetime

class Author:
    def __init__(self, name: str, gender: str,  country: str, birthday: datetime.date, books: list = None):
        self.name = name.title()
        self.gender = gender
        self.country = country.title()
        self.birthday = birthday
        self.birthday_ = birthday.strftime('%d-%m-%Y')
        self.age = datetime.date.today() - self.birthday
        if books is None:
            books = []
        self.books = books

    def write(self, book_name, year: int):
        book = Book(book_name, year, self, len(self.books) + 1)
        self.books.append(book)
        return book

    def show_all_books(self):
        for book in self.books:
            print(f'{book.number}. {book.name} - {book.year}.')

    def __str__(self):
        age = int((datetime.date.today() - self.birthday).total_seconds() // (3600*24*365))
        match self.gender:
            case 'man'|'male':
                sex = 'man'
                who = 'He'
            case 'woman'|'female':
                sex = 'woman'
                who = 'She'
            case _:
                sex = 'person'
                who = 'This person'
        return f'It is {self.name} a {sex} of ' \
               f'{age}' \
               f' years old. {who} is a writer from {self.country}, an author of {len(self.books)} books.'

    def __repr__(self):
        return f'Name: {self.name}\nGender: {self.gender}\n' \
               f'Birthday: {self.birthday_}\nNumber of books: {len(self.books)}'

    def show_annotation(self):
        print(self.__str__())

    def show_information(self):
        print(self.__repr__())

class Book:
    __books_number = 0
    __books = []
    id = None

    def __new__(cls,name: str, year: int, author: Author, number: int):
        cls.id = (name, author.name)
        if cls.id not in cls.__books:
            cls.__books_number += 1
            cls.__books.append(cls.id)
            return super().__new__(cls)
        else:
            print('The book already exists.')
            return None

    def __init__(self, name: str, year: int, author: Author, number: int):
        self.name = name
        self.year = year
        self.author = author
        self.number = number
        self.number_of_all = self.__books_number

    def __str__(self):
        return f'The book "{self.name}" has been wrote' \
               f' by {self.author.name} in {self.year} year. It is the {self.number} book from this author.'

    def __repr__(self):
        return f'Book: "{self.name}"\nAuthor: {self.author.name}\nYear: {self.year}\n' \
               f'Number of the author\'s books: {self.number}\n' \
               f'Number of all books: {self.number_of_all}'

    def show_annotation(self):
        print(self.__str__())

    def show_information(self):
        print(self.__repr__())

    @classmethod
    def get_number_of_books(cls):
        print(f'The total number of written books is {cls.__books_number}.')

class Library:
    def __init__(self, name: str, books: list[Book] = None, authors: list[Author] = None):
        if books is None:
            books = []
        if authors is None:
            authors = []
        self.name = name.title()
        self.books = books
        self.authors = authors

    def new_book(self, book: Book, author: Author) -> None:
        if book.author.name == author.name:
            self.books.append(book)
            self.books = list(set(self.books))
            self.authors.append(author)
            self.authors = list(set(self.authors))
        else:
            print(f'{author.name} did not write book "{book.name}".')

    def group_by_author(self, author: str) -> list[Book]:
        return [book for book in self.books if book.author.name == author]

    def show_by_author(self, author: str or Author) -> None:
        author_ = author.title() if isinstance(author, str) else author.name
        books = self.group_by_author(author_)
        print(f"There are {len(books)} {author_}'s books in our library:")
        for book in books:
            print(f' ~ "{book.name}".')

    def group_by_year(self, year: int) -> list[Book]:
        return [book for book in self.books if book.year == year]

    def show_by_year(self, year: int) -> None:
        books = self.group_by_year(year)
        print(f"There are {len(books)} books written in {year} in our library:")
        for book in books:
            print(f' ~ "{book.name}" ({book.author.name}).')

    def show_all_books(self):
        from prettytable import PrettyTable
        table = PrettyTable()
        table.field_names = ['Book', 'Year', 'Author']
        for book in self.books:
            table.add_row([book.name, book.year, book.author.name])
        print(table)

    def show_all_authors(self):
        from prettytable import PrettyTable
        table = PrettyTable()
        table.field_names = ['Author', 'Number of books in the library']
        for author in self.authors:
            table.add_row([author.name, len(self.group_by_author(author.name))])
        print(table)

    def __str__(self):
        return f'Our library is called "{self.name}".\n' \
               f'It contains {len(self.books)} books by {len(set(self.authors))} authors.'

    def __repr__(self):
        return f'Library: "{self.name}"\nNumber of books: {len(self.books)}' \
               f'\nNumber of authors: {len(set(self.authors))}'

    def show_annotation(self):
        print(self.__str__())

    def show_information(self):
        print(self.__repr__())
