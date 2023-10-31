from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        # Initialize the WebDriver
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_homepage(self):
        self.driver.get('http://localhost:5000')
        self.assertIn('Welcome to Flask App', self.driver.page_source)

        
        button = self.driver.find_element(By.ID, 'myButton')
        self.assertEqual(button.text, 'Click Me')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
