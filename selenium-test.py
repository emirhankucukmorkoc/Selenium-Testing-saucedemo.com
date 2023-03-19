from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(ChromeDriverManager().install())

class Test_Saucedemo:

    def test_invalid_login():
      driver.maximize_window()
      driver.get(url="https://www.saucedemo.com/")

    def test_empty_message():
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"Test Sonucu : {testResult}")

    def test_password_empty_message():
        input_userName = driver.find_element(By.ID,"user-name")
        input_userName.send_keys("locked_out_user")
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Test Sonucu : {testResult}")

    def test_locked_out_message():
        input_userName = driver.find_element(By.ID,"user-name")
        input_userName.send_keys("locked_out_user")
        input_password = driver.find_element(By.ID,"password")
        input_password.send_keys("secret_sauce")
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test Sonucu : {testResult}")

    def test_icon():
         loginBtn = driver.find_element(By.ID,"login-button")
         loginBtn.click()
         errorBtn = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
         errorBtn.click()   
   

    def test_success_login():
        input_userName = driver.find_element(By.ID,"user-name")
        input_userName.send_keys("standard_user")

        input_password = driver.find_element(By.ID,"password")
        input_password.send_keys("secret_sauce")
        
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"   

    def test_number_of_product():
       input_userName = driver.find_element(By.ID,"user-name")
       input_userName.send_keys("standard_user")
       input_password = driver.find_element(By.ID,"password")
       input_password.send_keys("secret_sauce")
       loginBtn = driver.find_element(By.ID,"login-button")
       loginBtn.click()
       inventoryItems = driver.find_elements(By.CLASS_NAME,"inventory_item")
       numberOfInventory = len(inventoryItems)
       print(f"Number of invertory: {numberOfInventory}")

testClass = Test_Saucedemo
testClass.test_invalid_login()
# testClass.test_empty_message()
# testClass.test_icon()
# testClass.test_locked_out_message()
# testClass.test_password_empty_message()
# testClass.test_success_login()
# testClass.test_number_of_product()
while True:
   continue