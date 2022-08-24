from selenium.webdriver.common.by import By


class Fourthiphone_Page:
    """"Locators"""
    BUY_NOW = (By.ID ,"buy-now-button")
    
    def __init__(self, driver):
        self.driver = driver

    """"Switch to a new tab"""   
    def switch_to_new_tab(self):
        windows_open = self.driver.window_handles
        return self.driver.switch_to.window(windows_open[1])

    """"Click on buy now button"""
    def click_on_buy_now(self):
        return self.driver.find_element(*Fourthiphone_Page.BUY_NOW).click()
