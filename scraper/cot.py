#Scrape Cash or Trade Posts and Email me every 30 minutes with current for sale items.
#Using Python 2.7

from bs4 import BeautifulSoup
import urllib2
import math
import numpy as np
import pandas as pd
import string
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

base_url = "https://cashortrade.org/phish-tickets?&cash_or_trade=1"
base_page = urllib2.urlopen(base_url).read()
soup=BeautifulSoup(base_page,'html.parser')

texts = []
links = []
avails = []

for i in range(0,100):
    texts.append( soup.find_all("td", attrs={'class':"trade-tickets"})[i].find('a').get_text().encode('utf-8').strip())
    links.append(soup.find_all("td",attrs={'class':"trade-tickets"})[i].find('a').get('href').encode('utf-8').strip())
    avails.append(soup.find_all("td",attrs={'class':"buttons"})[i].get_text().encode('utf-8').strip())

    df = pd.DataFrame({'link':links,'text':texts,'available':avails})

def create_link(string):
    return 'cashortrade.org' + string

df['full_link'] = df['link'].apply(lambda x: create_link(x))

df = df[df['available']=='BUY NOW'].reset_index()

gmail_user = '{}' # Email where message will come from
gmail_password = '{}' #insert gmail password here.
#You have to allow gmail access to less secure apps for this to work.
#After running the script for the first time, gmail should send you an email which you can use to allow less secure apps.

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')

sent_from = '{}' #insert from email
to = ['{}'] # insert to email
subject = 'New Cash or Trade Posts!'
email_text = '''
<html>
  <head></head>
  <body>
{table}
</body>
</html>
'''.format(table=df[['text','full_link']].to_html())

part2 = MIMEText(email_text, 'html')
msg.attach(part2)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, msg.as_string())
    server.close()

    print 'Email sent!'
except:
    print 'Something went wrong...'
