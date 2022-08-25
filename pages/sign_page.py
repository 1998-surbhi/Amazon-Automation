from selenium.webdriver.common.by import By


class Sign_Page:
    #Locators
    EMAIL_ID = (By.ID ,"ap_email")
    PASSWORD = (By.ID, "ap_password")
    CONTINUE_BUTTON = (By.XPATH, "//input[@class = 'a-button-input']")
    SIGN_BUTTON = (By.ID, "signInSubmit")
    INCORRECT_ALERT_POPUP = (By.XPATH, "//div[@class='a-box-inner a-alert-container']/div/ul/li/span[@class= 'a-list-item']")
    # INCORRECT_ALERT_EMAIL_POPUP = (By.XPATH, "//body/div/div/div[@id = 'authportal-center-section']/div/div/div/div/div/div/ul/li/span[@class = 'a-list-item']")
    INCORRECT_ALERT_EMAIL_POPUP = (By.XPATH, "//div[@class='a-box-inner a-alert-container']/div/ul/li/span[@class= 'a-list-item']")
   
    def __init__(self, driver, user_name, password):
        self.driver = driver
        self.user_name = user_name
        self.password = password
    
    #Enter Email Id
    def enter_email_id(self):
        return self.driver.find_element(*Sign_Page.EMAIL_ID).send_keys(self.user_name)

    #Clck on continue button
    def click_continue_button(self):
        return self.driver.find_element(*Sign_Page.CONTINUE_BUTTON).click()

    #Enter password
    def enter_password(self):
        return self.driver.find_element(*Sign_Page.PASSWORD).send_keys(self.password)

    #Click on sign button
    def click_sign_button(self):
        return self.driver.find_element(*Sign_Page.SIGN_BUTTON).click()

    #Get error message for password
    def incorrect_password_popup(self):
        alert_message = self.driver.find_element(*Sign_Page.INCORRECT_ALERT_POPUP).text
        return alert_message
    
    #Close new tabs
    def close_new_tab(self):
        self.driver.close()
        windows_open = self.driver.window_handles
        return self.driver.switch_to.window(windows_open[0])

    




