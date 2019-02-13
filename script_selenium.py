#! /usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.firefox.options import Options

import time

url = 'https://listado.mercadolibre.com.uy/casa-en-venta-floresta#D[A:casa%20en%20venta%20floresta]'



#options = Options()
#options.add_argument('headless')


#driver = webdriver.PhantomJS()

driver = webdriver.Firefox()
#driver = webdriver.Remote(
 #          command_executor='http://127.0.0.1:4444',
  #            desired_capabilities=DesiredCapabilities.PHANTOMJS)


driver.implicitly_wait(30)
driver.get(url)
for next_item in driver.find_elements_by_css_selector('li.results-item div > a'):
    next_item.click()
    time.sleep(5)
    driver.back()
    
print(driver.current_url)
driver.quit


