import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class demoQA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("https://demoqa.com/")
        cls.driver.maximize_window()

    // *[ @ id = "app"] / div / div / div[2] / div / div[1]
    // *[ @ id = "item-0"]
    def test_forms(self):
        self.BookStoreApplication = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[6]')
        self.driver.execute_script("arguments[0].click()", self.BookStoreApplication)
        time.sleep(5)
        self.loginbtn = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[6]/div/ul/li[1]')
        self.driver.execute_script("arguments[0].click()", self.loginbtn)
        time.sleep(5)
        self.loginbtn = self.driver.find_element(By.ID, 'newUser')
        self.driver.execute_script("arguments[0].click()", self.loginbtn)
        time.sleep(5)
        self.driver.find_element(By.ID, "firstname").clear()
        self.driver.find_element(By.ID, "firstname").send_keys("Shahzaib")
        self.driver.find_element(By.ID, "lastname").clear()
        self.driver.find_element(By.ID, "lastname").send_keys("Ansari")
        self.driver.find_element(By.ID, "userName").clear()
        self.driver.find_element(By.ID, "userName").send_keys("Shezi")
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "password").send_keys(
            "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})$")
        # self.recapctha = self.driver.find_element(By.XPATH, "//*[@id='recaptcha-anchor']/div[2]")
        # self.driver.execute_script("arguments[0].click()", self.recapctha)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()