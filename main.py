import pandas as pd
import random
from datetime import datetime
import configparser
import mailbox
import smtplib
import wikipediaapi

w = wikipediaapi.Wikipedia(language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)

config = configparser.ConfigParser()
config.read('.\..\configs.ini')

# username = config['mail']['user']
# password = config['mail']['pw']
# reciever = config['mail']['reciever']
# read by default 1st sheet of an excel file
quote_list = pd.read_csv('quotes.csv')
used_list = pd.read_csv('used.csv')

# Randomly choose the quote you want
choice = random.randint(0,45574)

# Check and make sure the quote has not been used before
while choice in used_list.values:
    choice = random.randint(0,45574)




today = quote_list.iloc[choice]
print(today['Quotes'], today['Author'])
date = "{:%B %d, %Y}".format(datetime.now())
message = ""
summary = ""
p = w.page(today['Author'])
if p.exists():
    message = "Good Morning {}!\n Today is {} and I hope you have a wonderful day today!\n\n Today reminds me of a quote, it reads \n\n\t\"{}\"\n\n I have always liked quotes becasue no matter where you came from or where you are going everybody can resonate with something like the wisdom of historys greatest.\n\n {}\n\n I hope this makes your day a little bit better!".format(str(name), str(date), str(today['Quotes']), str(p.summary))
    print(message)
    # print(p.summary, '\n')
    # print(p.fullurl, '\n')
else:
    message = "Good Morning {}!\n Today is {} and I hope you have a wonderful day today!\n\n Today reminds me of a quote, it reads \n\n\t\"{}\"\n\t- {}\n I have always liked quotes becasue no matter where you came from or where you are going everybody can resonate with something like the wisdom of historys greatest.\n\n {}\n\n I hope this makes your day a little bit better!".format(str(name), str(date), str(today['Quotes']), str(today['Author']))
    print(message)

# message = "Good Morning {}\n Today is {} and I hope you have a wonderful day today!\n\n Today reminds me of a quote, it reads \n\n\t\"{}\"\n\t- {}\n I have always liked quotes becasue no matter where you came from or where you are going everybody can resonate with something like the wisdom of historys greatest.\nI hope this makes your day a little bit better!".format(name, date, today['Quotes'], today['Author'])
# manages a connection to an SMTP server
server = smtplib.SMTP(host="smtp.gmail.com", port=587)
# connect to the SMTP server as TLS mode ( for security )
server.starttls()
# login to the email account
print(user, pw)
server.login(user, pw)
# send the actual message
server.sendmail(user, reciever, str(message))
# terminates the session
server.quit()

current_time = datetime.now()
file1 = open("used.csv", "a")  # append mode
file1.write("{},{}\n".format(current_time, str(choice), ))
file1.close()
print(choice)

