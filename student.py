class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        @property
        def age(self):
            return self._age

        @age.setter
        def age(self, value):
            if value < 5:
                raise ValueError('age must be greater than or equal to 5')
            self._age = value

        @property
        def name(self):
            return self.__name

        @name.setter
        def name(self, value):
            self.__name = value

s1 = Student(name='Alex', age=25)
print(s1.age())