from selenium import webdriver
import unittest #chropath
import time
class GoogleDemo(unittest.TestCase):
    def setUp(self):
        global driver
        driver = webdriver.Firefox(executable_path='/home/juned8236/Desktop/Coaching_MP/geckodriver')
        driver.get('https://www.google.com/')
        driver.maximize_window()

    def test(self):
        a=driver.find_element_by_xpath('//body/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]')
        a.send_keys('Mumtaj parveen mansoorie')
        time.sleep(3)
        driver.find_element_by_xpath('//body/div[1]/div[3]/form[1]/div[1]/div[1]/div[3]/center[1]/input[1]').click()
        time.sleep(5)
    
    def tearDown(self):
        print('teardown method')
        driver.close()

unittest.main()