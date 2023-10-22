# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 14:49:20 2023

@author: c.samanja09
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/")
time.sleep(3)
driver.maximize_window()

email=driver.find_element(By.ID,"session_key")
password = driver.find_element(By.ID,"session_password")
submit = driver.find_element(By.XPATH,"/html[1]/body[1]/main[1]/section[1]/div[1]/div[1]/form[1]/div[2]/button[1]")
email.send_keys("cart.samanja09@gmail.com")
password.send_keys("Sam#Carta32")
submit.click()
time.sleep(10)

driver.get('https://www.linkedin.com/search/results/people/?keywords=real%20estate%20&origin=SWITCH_SEARCH_VERTICAL&searchId=63a4e7f0-dd5b-4467-90f6-b73c5c01ae7c&sid=Lvu')
j =0
while j < 20:
  time.sleep(10)
  driver.execute_script("document.activeElement") 
  all_buttons= driver.find_elements(By.TAG_NAME,"button")
  messages=[btn for btn in all_buttons if btn.text =='Message']

  for i in range(len(messages)):
    
    driver.execute_script("arguments[0].click();",messages[i])  
    try:
        driver.find_element(By.XPATH,"//div[@role='dialog']").is_displayed()
        time.sleep(5)
        driver.find_element(By.XPATH,"//button[@aria-label='Dismiss']").click()
        time.sleep(5)
    except:
        print('No dialogs have been found')
        try:
          driver.find_element(By.XPATH,"//input[@name='subject']").is_displayed()
          subject=driver.find_element(By.XPATH,"//input[@name='subject']")
          subject.send_keys('Hi')
         
          main_div  = driver.find_element(By.CLASS_NAME,"msg-form__contenteditable")
          main_div.click()
          main_div.send_keys("Hi, Nice to meet you")
          time.sleep(5)
          send_button=driver.find_element(By.CLASS_NAME,'msg-form__send-button') 
          send_button.click() 
        except:
          print('No messages')
          try:
             driver.find_element(By.XPATH,"//div[@aria-label='Messaging']").is_displayed()
             message=driver.find_element(By.CLASS_NAME,"msg-overlay-bubble-header__badge-container").click()
          except:
              print('Awesome')
  time.sleep(10)
  driver.execute_script("window.scrollBy(0,1000)","")
  time.sleep(5)
  next = driver.find_element(By.XPATH,"//button[@aria-label='Next']")
  next.click()

            
time.sleep(5)

    
print('Automation Complete')
driver.quit()