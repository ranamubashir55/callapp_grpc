import os
import unittest
from appium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime as d
   
class CallApp():
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['noReset'] = 'True'
        desired_caps['appPackage'] = 'com.callapp.contacts'
        desired_caps['appActivity'] = 'com.callapp.contacts.activity.contact.list.ContactsListActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_add_contacts(self,number):
        dist={}
        email=[]
        try:
            search=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.callapp.contacts:id/title")))
            search.click()
            searchno=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.callapp.contacts:id/search_src_text")))
            searchno.send_keys(number)
            searchfor=WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.TextView")))
            searchfor[2].click()
        except Exception:
            return {"Status":"no data"}
        try:
            progress=WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.ID, "com.callapp.contacts:id/progress_wheel")))
            while progress:
                progress=WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.ID, "com.callapp.contacts:id/progress_wheel")))
        except Exception:
            print()  

        try:
            
            el3=WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.ID, "com.callapp.contacts:id/nameText")))
            name=el3.text
            if name[:3].isdigit()==True:
                raise Exception("no name")
            else:
                dist["name"]=name    
        except Exception:
           
            dist["name"]=""
        try:
            emailexist=self.driver.find_elements_by_class_name("android.widget.TextView")
            for i in emailexist:
                if '@' in i:
                    email.append(i)
            if len(email) !=0:
                dist["email"]=email
        except Exception:
            dist["email"]=""            
        return dist
            