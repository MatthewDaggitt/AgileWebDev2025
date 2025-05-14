
import unittest

from app.controllers import try_to_login_user
from app.models import Student
from app import create_application, db
from app.config import TestingConfig

class StudentTests(unittest.TestCase):

    def setUp(self):
        testApplication = create_application(TestingConfig)
        self.app_ctx = testApplication.app_context()
        self.app_ctx.push()
        db.create_all()

        return super().setUp()
    
    def addStudent(self, id, password):
        student = Student(id=1)
        student.set_password("a")
        db.session.add(student)
        db.session.commit()
        return student

    def test_database_student_model(self):
        self.addStudent(1, "a")

        self.assertIsNotNone(Student.query.get(1))

    
    def test_login_method(self):
        student1 = self.addStudent(3, "a")

        self.assertEqual(
            student1, 
            try_to_login_user(1,"a",False), 
            'Expected to successfully login and return `Student 1`'
        )
        self.assertEqual('Wrong password', try_to_login_user(1,"b",False))

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_ctx.pop()
        return super().tearDown()
