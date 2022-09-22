# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 13:21:21 2022

@author: znoll
"""

import os 
import time

### Counting files and folders ###
dir_path = r'C:\Users\znoll\OneDrive\Documents\aaaPersonal\Personal-2022\Personal-Projects-2022\Squat-Rack'

# Iterate directory
def count_file():
    count = 0
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    # print('File count:', count)
    return count 

def count_folder():
    count = 0
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isdir(os.path.join(dir_path, path)):
            count += 1
    # print('Folder count:', count) 
    return count


### Emailing ###
email_sender = 'scriptaethelred@gmail.com'
# email_password = os.environ.get("EMAIL_PASSWORD")
email_password = 'abwzytrirrysqisr'
# email_password = 'Aethelred968AD'
email_receiver = 'nollerzeke@gmail.com'

subject = 'ANSYS Simulation Update'

from email.message import EmailMessage
import ssl
import smtplib

context = ssl.create_default_context()
def send_email(body):
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content = (body)
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())
    pass


### Loop ###
init_foldercount = count_folder()
init_filecount = count_file()
while True:
    # dir_path = r'C:\Users\znoll\OneDrive\Documents\aaaPersonal\Personal-2022\Personal-Projects-2022\Squat-Rack'
    
    if count_folder() != init_foldercount:
        print("New folder has been added")
        body = """ New folder has been added"""
        # break
    if count_file() != init_filecount:
        print("New file has been added!")
        break
    time.sleep(5)







