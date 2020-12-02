# -- coding: utf-8 --
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get("https://afisha.tut.by/")

    def test_title_text(self):
        text = "Афиша Минска: развлечения, мероприятия, куда сходить?"
        self.assertEqual(text, self.browser.title)

    def test_search_line(self):
        browser = self.browser
        field = browser.find_element_by_name("str")
        text = 'Bring Me The Horizon'
        field.send_keys(text)
        field.send_keys(Keys.ENTER)
        title = browser.find_element_by_link_text(text)
        assert text in title.text

    def test_searching_the_wrong_query(self):
        browser = self.browser
        field = browser.find_element_by_name("str")
        field.send_keys('Dfcbkbq rhenjq rtyn')
        field.send_keys(Keys.ENTER)
        assert "По вашему запросу ничего не найдено" in browser.page_source
        time.sleep(2)

    def tearDown(self):
        self.browser.close()
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
