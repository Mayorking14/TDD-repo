import unittest
from Nokia_3310 import PhoneBook


class TestNokiaPhoneBook(unittest.TestCase):
    def setUp(self):
        self.phonebook = PhoneBook()

    def test_that_phonebook_add_Name_is_Empty(self):
        name = self.phonebook.get_add_Name()
        self.assertEqual(name, [])

    def test_that_phonebook_Add_Name_Succesfully(self):
        self.phonebook.set_add_Name('Mike')
        self.assertEqual(self.phonebook.get_add_Name(), ['Mike'])


