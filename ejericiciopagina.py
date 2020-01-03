from selenium import webdriver
import time

class usando_unittest():

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'/home/administrador/PycharmProjects/DriverFirefox')

    def test_PaginadePractica(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    test = usando_unittest()
    test.test_PaginadePractica()
    test.tearDown()