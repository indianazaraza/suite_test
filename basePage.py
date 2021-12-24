class BasePage():
	"""Base class for all pages object
	"""
	def __init__(self, driver):
		"""Initialize an driver

		:param driver: driver to interact with web browser 
		:type driver: webdriver
		"""
		self.driver = driver


	def find_element(self, locator):
		"""Find an element on the actual page 

		:param locator: attribute or path of the element to locate
		:type locator: tuple
		:rtype: web page	
		:return: an element 
		"""
		return self.driver.find_element(*locator)


	def get_the_attribute(self, locator, value):
		"""Get element attribute value 

		:param locator: attribute or path of the element to locate
		:param value: element attribute value
		:type locator: tuple
		:type value: string
		:rtype: value of the attribute	
		:return: string
		"""
		return self.driver.find_element(*locator).get_attribute(value)

	
	def get_page(self, url):
		"""Get a web page 

		:param url: url of a web psge
		:type value: string
		"""
		self.driver.get(url)


	def quit_driver(self):
		"""Close the driver and page
		"""
		self.driver.quit()

	
