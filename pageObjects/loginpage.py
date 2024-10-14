from selenium import webdriver
from selenium.webdriver.common.by import By
class Login:
    textboxusername_id="txtUserId"
    textboxpwd_id="txtPassword"
    liginbtn_id="btnLogin"

    def __init__(self,driver):
        self.driver=driver
    def setusername(self,username):
        self.driver.find_element(By.ID,self.textboxusername_id).clear()
        self.driver.find_element(By.ID,self.textboxusername_id).send_keys(username)


    def setpwd(self, password):
        self.driver.find_element(By.ID,self.textboxpwd_id).clear()
        self.driver.find_element(By.ID,self.textboxpwd_id).send_keys(password)
    def clickonlogin(self):
        self.driver.find_element(By.ID,self.liginbtn_id).click()
