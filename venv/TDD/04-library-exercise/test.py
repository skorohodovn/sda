import unittest
from library import Book

#is library empty
#add a non+book object
#init)pretty name), borrow, return )succesfully or not=
#init, add remove book

class BookFundamentals(unittest.TestCase):
    def test_init_default(self):
        book = Book("Title 1", "basar")
        self.assertEqual(book.title, "Title 1")
        self.assertEqual(book.author, "basar")
        self.assertEqual(book.copies, 1)
        self.assertEqual(book.available, 1)

    def test_init_default(self):
        book = Book("Title 1", "basar", 5, 5)
        self.assertEqual(book.title, "Title 1")
        self.assertEqual(book.author, "basar")
        self.assertEqual(book.copies, 5)
        self.assertEqual(book.available, 5)

    def test_is_available_positive(self):
        book = Book("Title 1", "basar")
        self.assertEqual(book.is_available())

    def test_is_available_negative(self):
        book = Book("Title 1", "basar", 2, 0)
        self.assertEqual(book.is_available())

    def test_pretty_name(self):
        book = Book("Title 1", "basar")
        pretty_name = book.pretty_name()
        self.assertEqual(pretty_name, '"Title 1" by basar')

class BookBorrowTestCase(unittest.TestCase):
    def test_return_positive(self):
        book = Book("Title 1", "basar", 5, 4)
        resp = book.borrow()
        self.assertEqual((resp, 'You have borrowed "Title 1" by basar'))
        self.assertEqual(book.available, 3)
        self.assertEqual(book.copies, 5)



    def test_return_negative(self):
        pass

class BookReturnTestCase(unittest.TestCase):
    def test_return_positive(self):
        pass

    def test_return_negative(self):
        pass

class LibraryFundamentalTestCase(unittest.TestCase):
    def test_init(self):
        pass

    def test_is_available_positive(self):
        pass

    def test_is_available_negative(self):
        pass

    def test_pretty_name(self):
        pass


