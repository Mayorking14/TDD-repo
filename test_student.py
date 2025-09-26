import unittest

from OOP import student
from .student import Student

class TestStudent(unittest.TestCase):
    def setUp(self):
        student = Student(name="john", age=25)

    def test_something(self):
        self.assertEqual(self.student.name, "john")
        self.assertEqual(self.student.age, 25)


if __name__ == '__main__':
    unittest.main()
