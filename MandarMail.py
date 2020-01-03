from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path='/home/administrador/PycharmProjects/DriverFirefox')
driver.get("http://gmail.com")

usuario = driver.find_element_by_id("identifierId")
usuario.send_keys("gaston3x@gmail.com")
usuario.send_keys(Keys.ENTER)
time.sleep(3)

clave = driver.find_element_by_name("password")
clave.send_keys("123aaa123")
clave.send_keys(Keys.ENTER)

redactar = driver.find_element_by_link_text('Redactar').click()



