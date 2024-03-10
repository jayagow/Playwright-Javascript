import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

url = "https://parabank.parasoft.com/parabank/register.htm;jsessionid=4CE150FCDB0CE3623E0C79D09E143958"
user_name = "jayasiva"
password = "Test@1"

def test_fund_transfer():
    # Login Validation
    driver.get(url)
    user_name_textbox = driver.find_element(By.NAME, "username")
    user_name_textbox.send_keys(user_name)
    password_textbox = driver.find_element(By.NAME, "password")
    password_textbox.send_keys(password)
    login_button = driver.find_element(By.XPATH, "//input[@value='Log In']")
    login_button.click()
    time.sleep(3) # wait time for login

    # Fund Transfer Validation
    fund_transfer_link = driver.find_element(By.LINK_TEXT, "Transfer Funds")
    fund_transfer_link.click()
    time.sleep(3)
    to_account_dropdown = driver.find_element(By.ID, "toAccountId")
    to_account_dropdown.click()
    second_option = driver.find_element(By.XPATH, "(//option[@value='14121'])[2]")
    second_option.click()
    amount_textbox = driver.find_element(By.ID, "amount")
    amount_textbox.send_keys("100")
    transfer_button = driver.find_element(By.XPATH, "//input[@value='Transfer']")
    transfer_button.click()
    time.sleep(3) # wait for transfer to complete

    # Transfer Status Validation
    transfer_status = driver.find_element(By.CSS_SELECTOR, "h1")
    transfer_status_text = transfer_status.text
    assert transfer_status_text == "Transfer Complete!"

    # Logout Validation
    logout_link = driver.find_element(By.LINK_TEXT, "Log Out")
    logout_link.click()
    time.sleep(2) #wait for logout

    # Validate logout successfully
    customer_login_header = driver.find_element(By.CSS_SELECTOR, "h2")
    customer_login_header_text = customer_login_header.text
    assert customer_login_header_text == "Customer Login"
