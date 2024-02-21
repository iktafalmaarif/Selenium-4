from selenium import webdriver
from selenium.webdriver.common import by

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=options)

driver.get('https://google.com/')