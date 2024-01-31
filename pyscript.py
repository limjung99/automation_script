from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
import undetected_chromedriver as uc
import time
from dotenv import load_dotenv
import os 


####################################################

"""
Unimplemented classes for my program. 
But , it is now just simple script 
OOP is not important I think
Later, I would code more ;; 
"""
class DriverManager:
    # TODO 
    pass 
class TimeManager:
    # TODO 
    pass 

##################################################


########### OS environment variables ##################################
# Later , you can add your configuration for your credentials
url = os.environ.get("url")
id = os.environ.get("user_id")
password = os.environ.get("user_password")
#########################################################################

def init_driver()->Chrome:
    driver = uc.Chrome()
    driver.get(url)
    return driver

def do_login(driver : Chrome)->None:
    driver.implicitly_wait(5)
    
    driver.find_element(By.ID,'userId').send_keys(id)
    driver.find_element(By.ID,"userPwd").send_keys(password)
    driver.find_element(By.CLASS_NAME,"btn").click()

def do_checkout(driver:Chrome)->None:
    driver.find_element(By.ID,"checkOut").click()

def do_checkin(driver:Chrome)->None:
    driver.find_element(By.ID,"checkIn").click()

if  __name__  ==  "__main__" :
    driver = init_driver()
    do_login(driver)

    now_time = time.localtime()

    if 8<= now_time.tm_hour <=9:
        do_checkin(driver)
    elif 17<= now_time.tm_hour <= 18:
        do_checkout(driver)
        
