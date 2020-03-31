from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Firefox(executable_path='YOUR_PATH_TO_GECKODRIVER')
driver.get("https://web.whatsapp.com")
driver.find_element_by_class_name('C28xL').click()
driver.find_element_by_class_name('_2MSJr').send_keys('Valentina Malcotti')
driver.find_element_by_class_name('_3j7s9').click()
for i in range(1, 10):
    driver.find_element_by_class_name('_3j7s9').send_keys(str(i))
    driver.find_element_by_class_name('_2lkdt').click()
soup = BeautifulSoup(driver.page_source, 'html.parser')

for message in soup.find_all('div', {'class', '_3_7SH'}):
    time = str(message.find('div', {'class', 'copyable-text'}))

driver.quit()
