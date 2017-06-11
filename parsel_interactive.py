import parsel
from selenium import webdriver

class interactive(object):
	def __init__(self):
		self.elements = []

	def open(self, url):
		self.driver = webdriver.Chrome('./chromedriver')
		self.driver.get(url)

	def check_css(self, css_selector):
		self.elements = self.driver.find_elements_by_css_selector(css_selector)
		for elem in self.elements:
			self.driver.execute_script("arguments[0].setAttribute('style','background-color:yellow;')", elem)

	def check_xpath(self, xpath):
		self.elements = self.driver.find_elements_by_xpath(xpath)
		for elem in self.elements:
			self.driver.execute_script("arguments[0].setAttribute('style','background-color:yellow;')", elem)

	def clear(self):
		for elem in self.elements:
			self.driver.execute_script("arguments[0].setAttribute('style','')", elem)

	def close(self):
		self.driver.quit()




			