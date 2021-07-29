

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver_path='C:\\webdriver\\chromedriver.exe'   
driver=webdriver.Chrome(driver_path)

url= 'https://www.google.com.tw'

driver.get(url)
a=driver.find_element_by_name('q')
a.send_keys('nba')
a.submit()

driver.back()
a=driver.find_element_by_name('q')
a.send_keys('wnba')
a.send_keys(Keys.ENTER)

body=driver.find_element_by_tag_name('body')
body.send_keys(Keys.PAGE_DOWN)



# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# driver_path='C:\\webdriver\\chromedriver.exe'   
# driver=webdriver.Chrome(driver_path)

# url= 'https://www.google.com.tw'

# driver.get(url)
# a=driver.find_elements_by_xpath("//input[@name='q']")
# print(a.get_attribute('innerHTML'))
# b=driver.find_element_by_xpath('//input[@type="submit"]')
# b.click()
