
import multiprocessing
import time
import unittest
from flask import url_for
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from app.config import TestConfig
from app.controllers import try_to_login_user
from app.models import Student
from app import create_application, db

localHost = "http://localhost:5000/"

class SystemTests(unittest.TestCase):

    def setUp(self):
        self.testApp = create_application(TestConfig)
        self.app_context = self.testApp.app_context()
        self.app_context.push()
        db.create_all()

        self.server_thread = multiprocessing.Process(target=self.testApp.run)
        self.server_thread.start()


        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=options)

    def test_successful_login(self):
        student = Student(id=1)
        student.set_password("a")
        db.session.add(student)
        db.session.commit()

        self.driver.get(localHost)
        id_input = self.driver.find_element(By.ID, 'student_id')
        id_input.send_keys("1")

        password_input = self.driver.find_element(By.ID, 'password')
        password_input.send_keys("a")

        login_btn = self.driver.find_element(By.ID, 'submitBtn')
        login_btn.click()

        WebDriverWait(self.driver, 5).until(expected_conditions.url_changes(self.driver.current_url))

        self.assertEqual(self.driver.current_url, localHost + 'projects')

    def tearDown(self):
        self.server_thread.terminate()
        self.driver.close()
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

if __name__ == '__main__':
    unittest.main()