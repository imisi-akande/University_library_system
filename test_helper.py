from oop import Book, Library, UndergraduateStudent, PostgraduateStudent

new_book = Book('Financial analysis','John grin', 'finance', 123)
new_book1 = Book('Wealth of Nations','John grin', 'economy', 190)
new_book2 = Book('The Art of War','John grin', 'war', 123)
new_book3 = Book('Good Times','John grin', 'philosophy', 123)

def create_library(name, library_type):
    return Library(name, library_type)

def create_book(name, author, category, number_of_pages):
    return Book(name, author, category, number_of_pages)

def add_book_to_library(library, book):
    library.add_book(book)
    
def borrow_from_library(student, library, book):
    student.borrow_from_library(library, book)
