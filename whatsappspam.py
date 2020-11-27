"""
                  _                 
                 | |                
  ___ ____  _   _| |__   ___  _   _ 
 /___)  _ \| | | |  _ \ / _ \| | | |
|___ | |_| | |_| | |_) ) |_| | |_| |
(___/|  __/ \__  |____/ \___/ \__  |
     |_|   (____/            (____/   
"""
# -----------------------------------------------------------
# demonstrates how to spam specif person or group on whatsaapp
# 💥🤖🤫
# Python3 or above must be installed on your System.
# Selenium must be installed 
# To install type "pip install selenium"
# ChromeDriverManager must be installed on the system
# To install type "pip install webdriver_manager"
# R0cK & R0oL !!
# -----------------------------------------------------------

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = int(input('Enter the count : '))

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('DuUXI')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_2Ujuu')
    button.click()
