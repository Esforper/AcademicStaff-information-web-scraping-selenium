from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.maximize_window()
print("enter your web url for university web site academic staff page")
url = input()
driver.get(url)
print("Enter the class of the html element written by academicians' emails")
class_name = input()
a = 0
allAcademicians = driver.find_elements(By.CLASS_NAME,class_name)
for academician in allAcademicians :
    print(academician.text)
    a+=1
print(a)