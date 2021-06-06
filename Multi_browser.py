from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Selenium_driver\chromedriver_win32\chromedriver.exe")
#driver=webdriver.Ie(executable_path="C:\Selenium_driver\IEDriverServer_x64_3.150.1\IEDriverServer.exe")

driver.get("http://skunkworks.ignitesol.com:3000/")
