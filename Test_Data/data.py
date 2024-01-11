# This file consists of Test Information like username, password, XPATH etc

# Python Class for Username and Password
class TestData:
    username = "Admin"
    password = "admin123"

# Python Class for Selenium Selectors
class TestSelectors:
    input_box_username = "username"
    input_box_password = "password"
    login_xpath = "//button[@type='submit']"
    # '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'