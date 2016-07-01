import sys
import os
import re
import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import requests

def main():

	print(findDates())


def findDates():

	r = requests.get("https://..com/rota/")

	data = r.text

	# soup = BeautifulSoup(open("test2.html"))
	soup = BeautifulSoup(data)

	listoflinks = soup.find_all('td')

	dates = []
	# print (listoflinks)

	for x in range(0,len(listoflinks)):

		test = str(listoflinks[x])

		if "allocateWindow" in test:
			# print(test)

			index = test.find('date')
			dates.append(("Date " + test[(index+6) : (index+8)].replace("<","")))
			for x in range(0,len(test)):
				if test[x] == ":":
					if test[x-5] !="n":
						if test[x-5] !="t":
							dates.append((test[(x-2):(x+3)]))

	return dates


def send_email(dates):

    gmail_user = "@gmail.com"
    gmail_pwd = ""
    FROM = gmail_user
    TO = ["@.net"]
    SUBJECT = "Shifts Available"
    TEXT = dates

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print ('successfully sent the mail')
    except:
        print ("failed to send mail")


if __name__ == "__main__":
	main()
