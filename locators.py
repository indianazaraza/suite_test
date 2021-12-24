from selenium.webdriver.common.by import By

class Locators():
	"""Class that contains all locators
	"""
	twitter_link = (By.XPATH, "/html/body/div/footer/div/div/div/div[2]/div/ul/li[2]/a")
	facebook_link = (By.XPATH, "/html/body/div/footer/div/div/div/div[2]/div/ul/li[1]/a")
	behance_link = (By.XPATH, "/html/body/div/footer/div/div/div/div[2]/div/ul/li[3]/a")
	linkedin_link = (By.XPATH, "/html/body/div/footer/div/div/div/div[2]/div/ul/li[4]/a")
	dribbble_link = (By.XPATH, "/html/body/div/footer/div/div/div/div[2]/div/ul/li[5]/a")


