import secrets

class UniversityStudent:
    """
    A student of a university with an access to library management system.
    Student have the following properties:

    Attributes:
    name: A string representing the student's name.
    matric_no: An unique integer representing the student's matric number
    borrowed_books: A list of borrowed book(s)
    borrowed_books_count: An integer tracking the current number of books 
    borrowed and returned from the library
    """
    def __init__(self, name, matric_no):
        self.name = name
        self.matric_no = matric_no
        self.borrowed_books = []
        self.borrowed_books_count = 0

    def return_to_library(self, library_instance, book_instance):
        """
        It checks if a book with a particular ref no is in the list of 
        borrowed books. If found, it deletes the particular instance from the list
        borrowed books and decrements the count of books in the borrowed books. It
        then adds the book instance back to the library
        """
        if book_instance in self.borrowed_books:
            self.borrowed_books.remove(book_instance)
            library_instance.add_book(book_instance)

    def get_student_info(self):
        """
        Return student object whose name is *name* and matric number is 
        *matric_no*.
        """   
        return "name: {} matric_no: {}".format(self.name, self.matric_no)

    def check_book_in_library(self, library, book):
        """
        Checks if book exist in the library object else it throws an error
        """    
        if not (book in library.books):
            raise ValueError("Book not found")

    def set_borrowed_books(self, book):
        # Add books to a list of borrowed books   
        self.borrowed_books.append(book)

    def remove_book_from_library(self, library, book):
        # Remove book from library object    
        library.remove_book(book)

class UndergraduateStudent(UniversityStudent):
    """
    Inherits the attributes of an university student
    """
    def __init__(self, name, matric_no):
        super(UndergraduateStudent, self).__init__(name, matric_no)

    def borrow_from_library(self, library_instance, book_instance):
        # Checks if the student is accessing a research library,If true 
        # returns an error else checks if book is in library appends book to
        # the borrowed book list and increase count
    
        if library_instance.library_type == "research":
            return "Hey pal, this is a research library. Research libraries are for PG students"
        try:
            self.check_book_in_library(library_instance, book_instance)
            self.valid_borrowed_book_count()
            self.set_borrowed_books(book_instance)
            self.remove_book_from_library(library_instance, book_instance)
        except ValueError as e:
            return e.args[0]

class PostgraduateStudent(UniversityStudent):
    """
    Inherits the attributes of an university student
    """
    def __init__(self, name, matric_no):
    	super(PostgraduateStudent, self).__init__(name, matric_no)

    def borrow_from_library(self, library_instance, book_instance):
        # Checks if book is in library then appends book to the borrowed book list 
        # and increase count
        try:
            self.check_book_in_library(library_instance, book_instance)
            self.valid_borrowed_book_count()
            self.set_borrowed_books(book_instance)
            self.remove_book_from_library(library_instance, book_instance)
        except ValueError as e:
            return e.args

class Library():
    """
    A University Library class.
    Library have the following properties:

    Attributes:
    name: A string representing the library name.
    library_type: A string representing the category of the library
    borrowed_books: A list of borrowed book(s)
    ref_no: An integer tracking the library reference number
    """
    def __init__(self, name, library_type):
        self.books = []
        self.library_type = library_type
        self.name = name
        self.ref_no = secrets.randbits(32)

    def add_book(self, book_instance):
        # Add book instance to list of books 
        self.books.append(book_instance)
        book_instance.add_lib_ref(self.ref_no)

    def remove_book(self, book_instance):
        # Remove book from library
         self.books.remove(book_instance)


class Book():
    """
    A Book class.
    Book have the following properties:

    Attributes:
    name: A string representing the book name.
    author: A string representing the author
    page_no: An integer representing the number of book pages
    category: A string representing the category of the book
    """
    def __init__(self, name, author, category, no_of_pages):
        self.name = name
        self.author = author
        self.page_no = no_of_pages
        self.category = category

    def add_lib_ref(self, lib_ref_no):
        self.lib_ref_no = lib_ref_no

