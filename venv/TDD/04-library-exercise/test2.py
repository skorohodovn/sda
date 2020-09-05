import unittest
from library import Book

#is library empty
#add a non+book object
#init)pretty name), borrow, return )succesfully or not=
#init, add remove book

class BookFundamentalsTestCase(unittest.TestCase):
    def test_unit_default(self):
        book = Book("Book", "Nikolai")
        self.assertEqual(book.title, "Book")
        self.assertEqual(book.author, "Nikolai")
        self.assertEqual(book.copies, 1)
        self.assertEqual(book.available, 1)

    def test_unit(self):
        book = Book("Book", "Nikolai", 5, 5)
        self.assertEqual(book.title, "Book")
        self.assertEqual(book.author, "Nikolai")
        self.assertEqual(book.copies, 5)
        self.assertEqual(book.available, 5)

    def test_is_available(self):
        book = Book("Book", "Nikolai", 5, 5)
        self.assertTrue(book.is_available())

    def test_not_available(self):
        book = Book("Book", "Nikolai", 5, 0)
        self.assertFalse(book.is_available())

    def test_pretty_name(self):
        book = Book("Book", "Nikolai")
        self.assertEqual(book.pretty_name(), '"Book" by Nikolai')


class BookBorrowTestCase(unittest.TestCase):
