from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.LoginPage import LoginPage


class Test_001_Login:
    baseURL = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    def test_login_PositiveCase(self):
        # self.driver = setup
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Swag Labs":
            assert True
        else:
            assert False
        self.lp = LoginPage(self.driver)
        self.lp.enterUserName("standard_user")
        self.lp.enterPassword("secret_sauce")
        self.lp.clickLogin()
        urlAfterLogin = self.driver.current_url
        if urlAfterLogin == "https://www.saucedemo.com/inventory.html":
            assert True
        else:
            assert False
        self.driver.close()

    def test_login_NegativeCase(self):
        # self.driver = setup
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Swag Labs":
            assert True
        else:
            assert False
        self.lp = LoginPage(self.driver)
        self.lp.enterUserName("wrongUser")
        self.lp.enterPassword("wrongPassword")
        self.lp.clickLogin()
        errorMsg = self.driver.find_element(By.XPATH, self.lp.text_loginError_xpath).text
        if errorMsg == "Epic sadface: Username and password do not match any user in this service":
            assert True
        else:
            assert False
        urlAfterFailuer = self.driver.current_url
        if urlAfterFailuer == self.baseURL:
            assert True
        else:
            assert False
        self.driver.close()
