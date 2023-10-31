from selenium import webdriver
import unittest

class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        # Path to your WebDriver executable within your repository
        self.driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
        self.driver.implicitly_wait(10)

    def test_homepage(self):
        self.driver.get('http://localhost:5000')
        self.assertIn('Welcome to Flask App', self.driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
