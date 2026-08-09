"""
Basic tests for ContactBook class.
Run with: python -m unittest test_contact_book.py
"""

import unittest
import os
from contact_book import ContactBook


class TestContactBook(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_contacts.json"
        self.book = ContactBook(data_file=self.test_file)
        self.book.contacts = []

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_contact_success(self):
        result = self.book.add_contact("John Doe", "9876543210", "john@example.com", "Delhi")
        self.assertTrue(result)
        self.assertEqual(len(self.book.contacts), 1)

    def test_add_contact_invalid_phone(self):
        result = self.book.add_contact("Jane Doe", "abc123")
        self.assertFalse(result)

    def test_add_contact_empty_name(self):
        result = self.book.add_contact("", "9876543210")
        self.assertFalse(result)

    def test_update_contact(self):
        self.book.add_contact("Alice", "9876543210")
        cid = self.book.contacts[0]["id"]
        result = self.book.update_contact(cid, name="Alice Smith")
        self.assertTrue(result)
        self.assertEqual(self.book.contacts[0]["name"], "Alice Smith")

    def test_delete_contact(self):
        self.book.add_contact("Bob", "9876543210")
        cid = self.book.contacts[0]["id"]
        result = self.book.delete_contact(cid)
        self.assertTrue(result)
        self.assertEqual(len(self.book.contacts), 0)

    def test_search_contact(self):
        self.book.add_contact("Charlie Brown", "9876543210")
        results = self.book.search_contact("charlie")
        self.assertEqual(len(results), 1)

    def test_invalid_email(self):
        result = self.book.add_contact("Dave", "9876543210", email="not-an-email")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
