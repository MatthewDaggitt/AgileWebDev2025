
import time
import unittest
import multiprocessing

from app.controllers import try_to_login_user
from app.models import Student
from app import create_application, db
from app.config import TestingConfig

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

localHost = "http://127.0.0.1:5000/"

class SystemTests(unittest.TestCase):

    def setUp(self):
        testApplication = create_application(TestingConfig)
        self.app_ctx = testApplication.app_context()
        self.app_ctx.push()
        db.create_all()

        self.server_thread = multiprocessing.Process(target=testApplication.run)
        self.server_thread.start()

        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=options)

        return super().setUp()
    
    def addStudent(self, id, password):
        student = Student(id=1)
        student.set_password("a")
        db.session.add(student)
        db.session.commit()
        return student
    
    def test_login_page(self):
        student1 = self.addStudent(1, "a")

        self.driver.get(localHost)

        student_id_field = self.driver.find_element(By.ID, "student_id")
        password_field = self.driver.find_element(By.ID, "password")
        submit_btn = self.driver.find_element(By.ID, "submit_btn")

        student_id_field.send_keys("1")
        password_field.send_keys("a")
        
        
        submit_btn.click()

        WebDriverWait(self.driver, 5).until(
            expected_conditions.url_changes(localHost)
        )

        self.assertEqual(localHost + "projects", self.driver.current_url)

    def tearDown(self):
        self.server_thread.terminate()
        self.driver.close()
        db.session.remove()
        db.drop_all()
        self.app_ctx.pop()
        return super().tearDown()
