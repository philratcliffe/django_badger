from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_get_the_expected_root_home_page(self):
        # Terry has heard about a cool new online app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention Badge
        self.assertIn('Badge', self.browser.title)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
