import unittest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def test_searchProject(self):
        self.driver.get("http://github.com")
        self.driver.find_element(By.NAME,"q").send_keys("")
        self.driver.find_element(By.NAME, "q").send_keys("react")
        self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
        self.driver.find_element(By.LINK_TEXT,"Advanced search").click()
        selectLanguage = Select(self.driver.find_element(By.ID, "search_language"))
        selectLanguage.select_by_visible_text("JavaScript")
        selectInTheState = Select(self.driver.find_element(By.ID, "search_state"))
        selectInTheState.select_by_value("closed")
        self.driver.find_element(By.ID,"search_stars").send_keys(">45")
        self.driver.find_element(By.ID, "search_followers").send_keys(">50")
        selectLicense = Select(self.driver.find_element(By.ID, "search_license"))
        selectLicense.select_by_visible_text("Boost Software License 1.0")
        self.driver.find_element(By.XPATH, "//*[@id='search_form']/div[2]/div/div/button").click()
        resultsFound = self.driver.find_element(By.XPATH, "//h3[contains(text (), '1 repository result')]")
        assert resultsFound.text == "1 repository result"
        linkRepositoryFound = self.driver.find_element(By.LINK_TEXT, "mvoloskov/decider")
        assert linkRepositoryFound.is_displayed()
        linkRepositoryFound.click()
        readmeText = self.driver.find_element(By.ID, "readme")
        threeHundredChars = readmeText.text
        print("300 characters")
        print("starts here: "threeHundredChars[0:299])
        time.sleep(10)




    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
