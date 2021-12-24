from basePage import BasePage
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait

class LinkPage(BasePage):
	"""Class that obtains the links of the page
	"""
	def __init__(self, driver):
		super().__init__(driver)
		element = WebDriverWait(self.driver, 4)


	def href_facebook(self):
		"""Get the facebook link

		:rtype: string
		:return: a link
		"""
		return self.get_the_attribute(Locators.facebook_link, "href")
	

	def href_twitter(self):
		"""Get the twitter link

		:rtype: string
		:return: a link
		"""
		return self.get_the_attribute(Locators.twitter_link, "href")
	

	def href_behance(self):
		"""Get the behance link

		:rtype: string
		:return: a link
		"""
		return self.get_the_attribute(Locators.behance_link, "href")
	

	def href_linkedin(self):
		"""Get the linkedin link

		:rtype: string
		:return: a link
		"""
		return self.get_the_attribute(Locators.linkedin_link, "href")


	def href_dribbble(self):
		"""Get the dribbble link

		:rtype: string
		:return: a link
		"""
		return self.get_the_attribute(Locators.dribbble_link, "href")
