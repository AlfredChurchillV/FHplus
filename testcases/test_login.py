import pytest
from selenium import webdriver
from pageObjects.loginpage import Login
from utilities.readproperties import ReadConfig
# import  conftest

class Test_001:
    BaseUrl=ReadConfig.GetApplicationURL()
    username=ReadConfig.GetUsername()
    password=ReadConfig.GetPassword()

    def testhomepage(self,setup):
        self.driver= setup
        self.driver.get(self.BaseUrl)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="FHPLUS :: Member details,Claims,Ecard,Network hospitals":
            assert True
        else:
            assert False

    def testlogin(self,setup):
        self.driver= setup
        self.driver.get(self.BaseUrl)
        self.lp=Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpwd(self.password)
        self.lp.clickonlogin()
        act_itle=self.driver.title

        if act_itle=="FHPLUS :: Employee":
            assert True
            self.driver.close()
        else:

            self.driver.save_screenshot(".\\Screenshots\\"+"testlogin.png")
            self.driver.close()
            assert False




