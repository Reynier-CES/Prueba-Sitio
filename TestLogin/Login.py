import unittest
import csv
import time
from lib2to3.pgen2 import driver
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.expected_conditions import alert_is_present, element_located_selection_state_to_be
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from Pages.Page_Login import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'C:\chromedriver_win32\chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)

    def test_Login(self):
        driver = self.driver
        driver.get("http://localhost:8000/login")
        time.sleep(3)

        login = LoginPage(driver)
        self.assertIn('Sistema de Gestión de Actividades Deportivas | Entrada', 'Sistema de Gestión de Actividades '
                                                                                'Deportivas | Entrada')
        login.enter_username("admin@jd.com")
        login.enter_password("admin2019")
        login.esperar_boton(5)
        login.check_box()

        time.sleep(2)
        login.click_login()

    def TearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
