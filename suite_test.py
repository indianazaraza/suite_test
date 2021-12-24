import unittest2 
from unittest2 import TestCase
from link_page import LinkPage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome

class TestLinkPage(TestCase):
	def setUp(self):
		self.path = Service("/home/maca/chromedriver")
		self.chrome_options = Options()
		self.chrome_options.add_argument("--headless")
		self.driver = Chrome(service=self.path, options=self.chrome_options)
		self.link_page = LinkPage(self.driver)
		self.link_page.get_page("https://asanteit.com.ar/")


	def test_href_twitter(self):
		self.assertIn("twitter", self.link_page.href_twitter())

	def test_href_facebook(self):
		self.assertIn("facebook", self.link_page.href_facebook())

	def test_href_behance(self):
		self.assertIn("behance", self.link_page.href_behance())

	def test_href_linkedin(self):
		self.assertIn("linkedin", self.link_page.href_linkedin())

	def test_href_dribbble(self):
		self.assertIn("dribbble", self.link_page.href_dribbble())

	def tearDown(self):
		self.link_page.quit_driver()


if __name__ == "__main__":
	unittest2.main()			

