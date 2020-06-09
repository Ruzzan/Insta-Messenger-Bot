from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
from getpass import getpass
import time

"""
TODO:
login to instagram 
go to users profile
click to message 
send messages from file
"""

username = str(input('enter username:'))
password = str(getpass(prompt="enter password:"))
reciever = str(input('reciever username:'))

# Your chromedriver path 
PATH   = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

url = "https://instagram.com"
reciever_url = "https://www.instagram.com/{}/".format(reciever)
driver.get(url)
time.sleep(1)

# logging in 
USERNAME = driver.find_element_by_name("username").send_keys(username)
PASSWORD = driver.find_element_by_name("password").send_keys(password)

login_btn = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
login_btn.click()

time.sleep(5)

# going to instagram  to avoid save password section
driver.get(url)

# this will handle the not now in turn on notificcation or not modal
try:
    not_now_btn = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")
    not_now_btn.click()
    print('not now')
except:
    pass

# go to recievers profile section  and click the message the button 
driver.get(reciever_url)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/button').click()

# focus on messagebox and type messages
time.sleep(15) # wait 15 seconds to load the messsage page or use WebDriverWait 

message_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

# read the file and send text 
with open("text.txt", "r") as f:
    words = f.read().split()

    for word in words:
        message_box.send_keys(word)
        message_box.send_keys(Keys.RETURN)
        time.sleep(1)

