import unittest
from Nokia_3310 import *

class TestNokiaPhoneBook(unittest.TestCase):
    def setUp(self):
        self.phonebook = PhoneBook()

    def test_that_phonebook_is_empty(self):
        self.assertEqual(self.phonebook.is_empty(), {})

    def test_that_phonebook_has_contact(self):
        self.phonebook.set_add_contact('Michael', 234567 )
        self.phonebook.set_add_contact('samuel', 56789)
        self.phonebook.get_contacts()
        self.assertEqual(self.phonebook.get_contacts(), {'Michael':234567, 'samuel':56789})

    def test_that_phonebook_contact_can_be_deleted(self):
        self.phonebook.set_add_contact('Michael', 234567 )
        self.phonebook.set_add_contact('samuel', 56789)
        self.phonebook.delete_contact('Michael')
        self.assertEqual(self.phonebook.get_contacts(), {'samuel':56789})

    def test_to_search_contact(self):
        self.phonebook.set_add_contact('Michael', 234567 )
        self.phonebook.set_add_contact('samuel', 56789)
        result = self.phonebook.search_contact('Michael')
        self.assertEqual(result, 234567)

    def test_to_delete_contact(self):
        self.phonebook.set_add_contact('Michael', 234567)
        self.phonebook.set_add_contact('samuel', 56789)
        result = self.phonebook.delete_contact('samuel')
        self.assertEqual(result, 'contact deleted')

class TestNokiaMessages(unittest.TestCase):
    def setUp(self):
        self.messages = Messages()

    def test_that_message_inbox_is_empty(self):
        self.assertEqual(self.messages.get_inbox(), {})

    def test_that_message_outbox_is_empty(self):
        self.assertEqual(self.messages.get_outbox(), {})

    def test_that_message_is_sent(self):
        self.messages.set_send_message('mike', 'how are you')
        self.assertEqual(self.messages.get_outbox(), {'mike':['how are you']})

    def test_that_phone_saves_received_messages(self):
        self.messages.set_receive_message('sam', 'Hi there')
        self.assertEqual(self.messages.get_inbox(), {'sam':['Hi there']})

    def test_that_message_can_be_deleted(self):
        self.messages.


