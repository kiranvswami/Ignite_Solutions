from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Selenium_driver\chromedriver_win32\chromedriver.exe")

driver.get("http://skunkworks.ignitesol.com:3000/")

print(driver.title) #find the title of the webpage

driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[2]/div[1]/div/div/a/button/span[1]/span").click() #locate the Fiction button and click

element=driver.find_element_by_name("query") #locate the Seach bar
print(element.is_displayed())  #prints True/ False whether the search button is displayed or not
print(element.is_enabled())    #prints True/ False whether the search button is enabled or not

element.send_keys("Harry")
driver.find_element_by_xpath("//*[@id='root']/div/div/div[1]/button").click()
