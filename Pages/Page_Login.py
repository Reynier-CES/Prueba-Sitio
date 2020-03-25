from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present, element_located_selection_state_to_be



class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.user_textbox_id = "email"
        self.password_id = "password"
        self.login_button_id = "/html/body/div[1]/div[2]/form/div[3]/div[2]/button"
        self.checkbox = "/html/body/div[1]/div[2]/form/div[3]/div[1]/div/label/input"

    #   self.lgo.ico = "/html/body/div[1]/div[1]/img"
    #   self.login_box_msg = "login-box-msg"
    #   self.icon_email = "glyphicon glyphicon-envelope form-control-feedback"
    #   self.icon_pass = "glyphicon glyphicon-lock form-control-feedback"
    #   # def lgo_icon(self):
    # self.driver.find_element_by_class_name(self.lgo_icon)

    # def login_msg(self):
    #   self.driver.find_element_by_class_name(self.login_box_msg)

    # def icon_email(self):
    #   self.driver.find_element_by_class_name(self.icon_email)

    def enter_username(self, username):
        self.driver.find_element_by_id(self.user_textbox_id).send_keys(username)

    def icon_pass(self):
        self.driver.find_element_by_class(self.icon_pass)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def check_box(self):
        self.driver.find_element_by_xpath(self.checkbox).click()

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_id).click()

    # Method's de Espera
    def esperar_boton(self, time):
        WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.XPATH, self.login_button_id)))
