from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path='/home/juned8236/Desktop/Coaching_MP/geckodriver')
print(driver)
driver.get('https://lf-platform.lambdafunction.ai/login')
driver.find_element_by_xpath("//input[@id='exampleInputEmail']").send_keys('Mumtaj parveen mansoorie')
driver.find_element_by_xpath("//input[@id='exampleInputPassword']").send_keys('jkjhkfsjkd')
time.sleep(10)
# print(driver.title)
# print(driver.current_url)
# driver.refresh()
# driver.get('https://www.google.com/')
# time.sleep(3)
# driver.back()
# time.sleep(3)
# driver.forward()
# time.sleep(3)
driver.close()#close current window
# driver.quit()  #close associated window
