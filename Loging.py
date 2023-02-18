import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Login(webdriver.Chrome):
    # Initial set-up for the loging page
    def __init__(self, driver=r"/home/balor/Documents/Pyp/EVERYTHING_ELSE/Chrome_Drive"):
        try:
            self.driver = driver
            os.environ['PATH'] += self.driver
            super(Login, self).__init__()
            self.implicitly_wait(10)
            self.maximize_window()
            f = open("Test", "a")
            f.write("Setup-LOGIN - PASS\n")
            f.close()
        except:
            f = open("Test", "a")
            f.write("Setup - FAIL\n")
            f.close()

    def loging_page_open(self):
        # Open the browser
        try:
            self.get("https://qa-practice.netlify.app/auth_ecommerce.html")
            f = open("Test", "a")
            f.write("LogIN - PASS\n")
            f.close()
            time.sleep(5)
        except:
            f = open("Test", "a")
            f.write("LogIN - FAIL\n")
            f.close()
        return self

    def loging_page_credentials(self, username="admin@admin.com", password="admin123"):
        """
        Inputs the username and password
        Presses the submit button if no problems emerge

        :param username: the username or email
        :param password: the password
        :return: self
        """
        if not isinstance(username, str) or not isinstance(password, str):
            f = open("Test", "a")
            f.write("Credentials - Fail\n")
            f.close()
            raise AttributeError("both params must be type<str>")
        else:
            element_user = self.find_element(By.NAME, "emailAddress")
            element_user.clear()
            element_user.send_keys(username)

            element_password = self.find_element(By.NAME, "password")
            element_password.clear()
            element_password.send_keys(password)

            element_submit = self.find_element(By.ID, "submitLoginBtn")
            element_submit.click()

            f = open("Test", "a")
            f.write("Credentials - PASS\n")
            f.close()
        time.sleep(5)
        return self
