import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class OrangeHRMForgotPasswordTest(unittest.TestCase):

    def setUp(self):
        # Set up Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()

    def test_forgot_password(self):
        driver = self.driver

        # Step 1: Verify if the "Username" textbox is visible on the login page
        username_textbox = driver.find_element(By.NAME, "username")
        self.assertTrue(username_textbox.is_displayed())

        # Step 2: Provide a valid username
        username = "Admin"
        username_textbox.send_keys(username)

        # Step 3: Click on the "Forgot Password" link
        driver.find_element(By.LINK_TEXT, "Forgot your password?").click()
        time.sleep(2)  # Wait for the forgot password page to load

        # Step 4: Verify if a success message "Reset Password link sent successfully" is displayed
        # Note: Adjust the verification based on actual implementation details of OrangeHRM forgot password feature
        success_message_element = driver.find_element(By.CSS_SELECTOR, "div.oxd-alert-content > p")
        success_message = success_message_element.text
        self.assertEqual(success_message, "Reset Password link sent successfully")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
