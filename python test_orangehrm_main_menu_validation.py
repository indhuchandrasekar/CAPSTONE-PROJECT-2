import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class OrangeHRMMainMenuValidationTest(unittest.TestCase):

    def setUp(self):
        # Set up Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()

    def login(self, username, password):
        driver = self.driver
        # Enter username
        driver.find_element(By.NAME, "username").send_keys(username)

        # Enter password
        driver.find_element(By.NAME, "password").send_keys(password)

        # Click "Login" button
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Wait for login to process
        time.sleep(2)

    def test_main_menu_validation(self):
        driver = self.driver

        # Precondition: Ensure a valid Admin account is available
        username = "Admin"
        password = "admin123"

        # Step 1: Launch URL and Login as "Admin"
        self.login(username, password)

        # Expected Result: The system should log in successfully, and the Admin dashboard should be displayed
        self.assertTrue("dashboard" in driver.current_url.lower())

        # Step 2: Navigate to Admin Page
        driver.find_element(By.XPATH, "//span[text()='Admin']").click()
        time.sleep(2)  # Wait for the Admin page to load

        # Validate the presence of main menu options on the side pane
        main_menu_options = [
            "Admin",
            "PIM",
            "Leave",
            "Time",
            "Recruitment",
            "My Info",
            "Performance",
            "Dashboard",
            "Directory",
            "Maintenance",
            "Buzz"
        ]

        for option in main_menu_options:
            self.assertTrue(driver.find_element(By.XPATH, f"//span[text()='{option}']").is_displayed(), f"{option} is not displayed")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
