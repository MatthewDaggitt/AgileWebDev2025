
import unittest

from app.config import TestConfig
from app.controllers import try_to_login_user
from app.models import Student
from app import create_application, db

class UnitTests(unittest.TestCase):

    def setUp(self):
        self.testApp = create_application(TestConfig)
        self.app_context = self.testApp.app_context()
        self.app_context.push()
        db.create_all()

    def test_successful_login(self):
        student = Student(id=1)
        student.set_password("a")
        db.session.add(student)
        db.session.commit()

        self.assertEqual(student, try_to_login_user(1,"a",False))
        self.assertEqual('Wrong password', try_to_login_user(1,"b",False))

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

if __name__ == '__main__':
    unittest.main()