import unittest

from oop import (
    Book, Library, UniversityStudent, UndergraduateStudent, PostgraduateStudent
)
from test_helper import (create_library, new_book, add_book_to_library,
new_book1, new_book2, new_book3, borrow_from_library, create_book)


class UniversityStudentTestSuite(unittest.TestCase):
    def setUp(self):
         self.university_student = UniversityStudent("Bolatito Ekundayo", 150968)

    def test_init(self):
        self.assertEqual(self.university_student.name, "Bolatito Ekundayo")
        self.assertEqual(self.university_student.matric_no, 150968)
        self.assertEqual(self.university_student.borrowed_books, [])

    def test_get_student_info(self):
        student_info = self.university_student.get_student_info()
        self.assertEqual(student_info,
                         'name: Bolatito Ekundayo matric_no: 150968')


class UndergraduateStudentTest(unittest.TestCase):
    def setUp(self):
        self.under_student = UndergraduateStudent("Ajayi Crowther", 250705)

    def test_undergraduate_student(self):
        self.assertEqual(self.under_student.name, "Ajayi Crowther")
        self.assertEqual(self.under_student.matric_no, 250705)


    def test_undergraduate_cannot_borrow_from_research_lib(self):
        res_library = create_library("ilesanmi", "research")
        log = self.under_student.borrow_from_library(res_library, new_book)
        self.assertEqual(log, 'Hey pal, this is a research library. Research libraries are for PG students')

    def test_undergraduate_student_borrow(self):
        res_library = create_library("ilesanmi", "thesis")
        add_book_to_library(res_library, new_book)
        self.under_student.borrow_from_library(res_library, new_book)
        self.assertEqual(new_book, self.under_student.borrowed_books[0])

    def test_undergraduate_student_return(self):
        res_library = create_library("ilesanmi", "thesis")
        add_book_to_library(res_library, new_book)
        self.under_student.borrow_from_library(res_library, new_book)   
        self.under_student.return_to_library(res_library, new_book)
        self.assertEqual(len(self.under_student.borrowed_books), 0)    
        
    def test_borrowed_books_limit(self):
        res_library = create_library("ilesanmi", "thesis")
        add_book_to_library(res_library, new_book)
        add_book_to_library(res_library, new_book1)
        add_book_to_library(res_library, new_book2)
        add_book_to_library(res_library, new_book3)
        borrow_from_library(self.under_student, res_library, new_book)
        borrow_from_library(self.under_student, res_library, new_book1)
        borrow_from_library(self.under_student, res_library, new_book2)
        log = self.under_student.borrow_from_library(res_library, new_book3)
        self.assertEqual(log, "You can only borrow 3 books from the library")

    def test_book_not_found(self):
        res_library = create_library("ilesanmi", "thesis")
        log = self.under_student.borrow_from_library(res_library, new_book)
        self.assertEqual(log, "Book not found")

    def test_initial_borrowed_books_count(self):
        self.assertEqual(len(self.under_student.borrowed_books), 0)

    def test_borrowed_books_increase(self):
        res_library = create_library("ilesanmi", "thesis")
        add_book_to_library(res_library, new_book)
        borrow_from_library(self.under_student, res_library, new_book)
        self.assertEqual(len(self.under_student.borrowed_books), 1)


class PostgraduateStudentTest(unittest.TestCase):
    def setUp(self):
         self.post_student=PostgraduateStudent("Akande Imisioluwa", 250705)

    def test_postgraduate_student(self):
        self.assertEqual(self.post_student.name, "Akande Imisioluwa")
        self.assertEqual(self.post_student.matric_no, 250705)

    def test_postgraduate_student_borrow(self):
        res_library = create_library("Hezekiah", "research")
        add_book_to_library(res_library, new_book)
        self.post_student.borrow_from_library(res_library, new_book)
        self.assertEqual(new_book, self.post_student.borrowed_books[0])


class LibraryTest(unittest.TestCase):
    def setUp(self):
         self.Library= Library("research", "Hezekiah")

    def test_initial_books_value(self):
        res_library = create_library("British", "Modern Education")
        self.assertEqual(len(res_library.books), 0)

    def test_add_book_to_library(self):
        res_library = create_library("British", "Modern Education")
        add_book_to_library(res_library, new_book)
        self.assertEqual(len(res_library.books), 1)

    def test_remove_book_from_library(self):
        res_library = create_library("British", "Modern Education")
        add_book_to_library(res_library, new_book)
        res_library.remove_book(new_book)
        self.assertEqual(len(res_library.books), 0)


class BookTest(unittest.TestCase):
    def setUp(self):
        self.Book= create_book("kenneth", "Wole Soyinka","Literature", 500)

    def test_add_library_ref_no_to_book(self):
        res_library = create_library("Macaulay", "learning")
        add_book_to_library(res_library, new_book)
        self.assertEqual(res_library.ref_no, new_book.lib_ref_no)

if __name__ == "__main__":
     unittest.main()
