class PhoneBook:
    def __init__(self):
        self.contact = {}

    def is_empty(self):
        return self.contact

    def set_add_contact(self,name, contact):
        self.contact[name] = contact

    def get_contacts(self):
        return self.contact

    def delete_contact(self, name):
        if name in self.contact:
            del self.contact[name]
            return 'contact deleted'
        else:
            return "contact not found"

    def search_contact(self, name):
        if name in self.contact:
            return self.contact.get(name)
        else:
            return "contact not found"

    def edit_contact(self, name, contact):
        for details in self.contact:
            if details == name and contact:
                self.contact[name] = contact


class Messages:
    def __init__(self):
        self.inbox = {}
        self.outbox = {}



    def set_send_message(self, name, message):
        self.outbox[name] = [message]

    def set_receive_message(self, name, message):
        self.inbox[name] = [message]

    def get_inbox(self):
        return self.inbox

    def get_outbox(self):
        return self.outbox

    def delete_message(self, name):
        for receiver in self.outbox:
            if receiver == name:
                del self.outbox[name]










