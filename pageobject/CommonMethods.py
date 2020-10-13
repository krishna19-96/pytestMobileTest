from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class CommonMethods:

    def __init__(self, driver):
        self.driver = driver


    def clicks(self, locators):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locators)).click()
        except Exception as e:
            raise e    


    def send_keys(self, locators, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locators)).send_keys(text)    

    def get_element_text(self, locators):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locators))
        return element.text
       