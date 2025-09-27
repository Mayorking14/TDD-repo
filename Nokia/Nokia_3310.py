class PhoneBook:
    def __init__(self):
        self.search = None
        self.service_Nos = None
        self.add_Name = []
        self.erase = None
        self.edit = None
        self.assign_Tone = None
        self.send_B_Card = None
        self.options = []
        self.speed_dials = []
        self.voice_Tags = []

    def set_add_Name(self, name):
        self.add_Name.append(name)

    def get_add_Name(self):
        return self.add_Name



