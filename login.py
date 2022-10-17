import pandas as pd

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument ('--ignore-certificate-errors')
driver = webdriver.Chrome(executable_path='path\\chromedriver.exe', options=options)

driver.get('pagina rel')
time.sleep(10)

driver.find_element_by_id('idToken1').send_keys('')
driver.find_element_by_id('idToken2').send_keys('')
driver.find_element_by_id('loginButton_0').click()

time.sleep(10)
