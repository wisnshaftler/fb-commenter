import time
import getpass
import random 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

email = str(input('enter email address or phone number: '))
passwd = getpass.getpass(prompt = "enter password: ")
print('\nenter comments [plese seperate comments using ~]' +"\n")
print("ex: i am iron man~on your left~i'm inevitable~:)"+"\n")
comments = str(input('enter comments: '))

comments = comments.split("~")
print("\n"+ str(comments))
print("\nPlease wait....")
browser = webdriver.Firefox()

browser.get("http://mbasic.facebook.com")

username = browser.find_element_by_name("email")
password = browser.find_element_by_name("pass")
submit   = browser.find_element_by_name("login")
username.send_keys(email)
password.send_keys(passwd)

submit.click()
browser.get("https://mbasic.facebook.com/stories.php")

print("\nFeel free :) we got this" +"\n")
print("we will print commenting links" +"\n")
counter =0
currentLink = ""

while True:
    browser.get("https://mbasic.facebook.com/stories.php")
        
    time.sleep(3)    
    
    link = browser.find_element_by_partial_link_text('Full Story')
    if currentLink == link.get_attribute("href"):
        print("skipping same links")
        continue
    print(link.get_attribute("href") + "\n")
    currentLink = link.get_attribute("href")
    link.click()
    
    time.sleep(3)
    
    commentButton = browser.find_element_by_xpath("//*[text()='Comment']")
    commentButton.click()

    time.sleep(5)
    
    randnum = random.randrange(0, len(comments)-1, 1)

    commentBox = browser.find_element_by_name("comment_text")
    commentBox.send_keys(comments[randnum])

    time.sleep(3)

    postComment = browser.find_element_by_name("post")
    postComment.click()

    counter +=1
    print("total comments: " +str(counter) +"\n")
    time.sleep(5)

