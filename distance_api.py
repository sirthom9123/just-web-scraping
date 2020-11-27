#Create a config.ini file with your API and email credentials 

import requests
import smtplib
from configparser import ConfigParser
import datetime as dt

# Open config file and get keys
config_object = ConfigParser()
config_object.read('config_key.ini')
api_key = config_object['MAPS']
api_key['api_key']
email_to = config_object['DEFAULT']
from_email = config_object['DEFAULT']
password = config_object['DEFAULT']
server = config_object['DEFAULT']
port = config_object['DEFAULT']
email_to['to']
from_email['user']
password['password']
server['server']
port['port']

# Input Addresses
home = input(str('Enter home address\n'))
work = input(str('Enter work address\n'))

# base url
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

# get response
r = requests.get(url, "origins=" + str(home) + "&destinations=" + str(work) + "&key=" + str(api_key)) 
 
# return time as text and as seconds
time = r.json()["rows"][0]["elements"][0]["duration"]["text"]       
seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]


# print the travel time
print("\nThe total travel time from home to work is", time)

if seconds < 3600:
    sender = email_to
    recipient = from_email
    message = "Hi Team,\n\nSorry, but I can't make it into work today."
    subject = "Sick Day"   
    email = "Subject: {}\n\n{}".format(subject, message)
    
    # Connect to server
    s = smtplib.SMTP_SSL(server, port)
    server.login(sender, password)
    server.send_message(sender, recipient, email)
    server.quit()

    # success message
    print("\nSuccessfully sent a sick-day email to", recipient, "since the travel time was too long")