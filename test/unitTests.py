
import unittest

from app.controllers import try_to_login_user
from app.models import Student
from app import db

class UnitTests(unittest.TestCase):

    def test_successful_login(self):
        student = Student(id=1)
        student.set_password("a")
        db.session.add(student)
        db.session.commit()


        self.assertThat(try_to_login_user(1,"a",False))
