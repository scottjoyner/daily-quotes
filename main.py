import pandas as pd
import random
from datetime import datetime
import configparser
import mailbox
from main import smtplib
import wikipediaapi
import time

w = wikipediaapi.Wikipedia(language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)

config = configparser.ConfigParser()
config.read('cfg.ini')


user = config['mail']['user']
pw = config['mail']['pw']
reciever = config['mail']['reciever']
sender_name = config['mail']['sender_name']
reciever_name = config['mail']['sender_name']
# read by default 1st sheet of an excel file
quote_list = pd.read_csv('quotes.csv')
# used_list = pd.read_csv('used.csv')

# Randomly choose the quote you want
choice = random.randint(0,45574)

# Check and make sure the quote has not been used before
# while choice in used_list.values:
#     choice = random.randint(0,45574)




today = quote_list.iloc[choice]
print(today['Quotes'], today['Author'])
date = "{:%B %d, %Y}".format(datetime.now())
now = datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)

greeting = ""
message = ""
summary = ""
if now.hour < 12:
    greeting = "Morning"
if 12 < now.hour and now.hour < 18:
    greeting = "Afternoon"
if 18 < now.hour:
    greeting = "Evening"

p = w.page(today['Author'])
if p.exists():
    message = "Good {} {}!\n Today is {} and I hope you have a wonderful day today!\n\n Today reminds me of a quote, it reads \n\n\t\"{}\"\n\n I have always liked quotes becasue no matter where you came from or where you are going everybody can resonate with something like the wisdom of historys greatest.\n\n {}\n\n I hope this makes your day a little bit better!\n\tYours Truly, {}".format(greeting, str(reciever_name), str(date), str(today['Quotes']), str(p.summary), sender_name)
    # print(p.summary, '\n')
    # print(p.fullurl, '\n')
else:
    message = "Good {} {}!\n Today is {} and I hope you have a wonderful day today!\n\n Today reminds me of a quote, it reads \n\n\t\"{}\"\n\t- {}\n I have always liked quotes becasue no matter where you came from or where you are going everybody can resonate with something like the wisdom of historys greatest.\n\n {}\n\n I hope this makes your day a little bit better!\n\tYours Truly, {}".format(greeting, str(reciever_name), str(date), str(today['Quotes']), str(today['Author']), sender_name)

message.encode("ascii", errors="replace")
#message.encode("ascii", errors="ignore")
# message = "Good Morning {}\n Today is {} and I hope you have a wonderful day today!\n\n Today reminds me of a quote, it reads \n\n\t\"{}\"\n\t- {}\n I have always liked quotes becasue no matter where you came from or where you are going everybody can resonate with something like the wisdom of historys greatest.\nI hope this makes your day a little bit better!".format(name, date, today['Quotes'], today['Author'])
# manages a connection to an SMTP server
server = smtplib.SMTP(host="smtp.gmail.com", port=587)
# connect to the SMTP server as TLS mode ( for security )
server.starttls()
# login to the email account

server.login(user, pw)
# send the actual message
server.sendmail(user, reciever, message)
# terminates the session
server.quit()
print("Message Sent")
current_time = datetime.now()
used_list = pd.DataFrame([current_time, choice])
# used_list.concat([current_time, choice])
# used.to_csv("used.csv")
file1 = open("used.csv", "w")  # append mode
file1.write(used_list.to_string())
file1.close()
# print(choice)

