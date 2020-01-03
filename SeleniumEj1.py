from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path='/home/administrador/PycharmProjects/DriverFirefox')
driver.get("http:/wikipedia.com")

search = driver.find_element_by_name("search")
search.send_keys("selenium")
search.send_keys(Keys.ENTER)
time.sleep(3)

image = driver.find_element_by_class_name("image")
image.click()
time.sleep(3)

close_img = driver.find_element_by_class_name("mw-mmv-close")
close_img.click()
time.sleep(3)

driver.find_element_by_link_text("English").click()

time.sleep(3)

driver.close()
