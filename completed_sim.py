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
    file_list = []
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
            file_list += path
    return count, file_list

def count_folder():
    count = 0
    folder_list = []
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isdir(os.path.join(dir_path, path)):
            count += 1
            folder_list += path
    # print('Folder count:', count) 
    return count, folder_list


### Emailing ###
email_sender = 'scriptaethelred@gmail.com'
# email_password = os.environ.get("EMAIL_PASSWORD")
# email_password = 'abwzytrirrysqisr'
email_password = 'Aethelred968AD'
email_receiver = 'nollerzeke@gmail.com'

subject = 'ANSYS Simulation Update'

# import ssl
import smtplib

# Import smtplib for the actual sending function

# Import the email modules we'll need
from email.message import EmailMessage


# Method 3
def send_email3(body):
    msg = EmailMessage()
    msg.set_content(body)
    
    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = 'Simulation Update'
    msg['From'] = email_sender
    msg['To'] = email_receiver
    
    # Send the message via our own SMTP server.
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()


# Method 2
def send_email2(body):
    context = ssl.create_default_context()

    # Instantiating SMTP
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    
    # Authentication 
    s.login("scriptaethelred@gmail.com","abwzytrirrysqisr")
    
    # Sending 
    s.sendmail(email_sender, email_receiver, body)
 
    # Quitting SMTP
    s.quit()
    
    
# Method 1
import ssl 
def send_email1(body):
    context = ssl.create_default_context()
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = 'Simulation Update'
    em.set_content = (body)
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())
    pass


### Loop ###
init_foldercount = count_folder()[0]
init_filecount = count_file()[0]

# while True:
#     if count_folder()[0] != init_foldercount:
#         print("Simulation update: new folder added!")
#         print(f"Current list of folders is: {count_folder()[1]}")
#         send_email(f"Simulation update: new folder added! \
#                    Current list of folders is {count_folder()[1]}")
#         # body = """ New folder has been added"""
#     if count_file()[0] != init_filecount:
#         print("Simulation update: new file added!")
#         print(f"Current list of files is: {count_file()[1]}")
#         send_email(f"Simulation update: new file added! \
#                    Current list of files is {count_file()[1]}")
#     time.sleep(10)







