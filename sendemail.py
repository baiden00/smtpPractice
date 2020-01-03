import smtplib


conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()




conn.login(email, passwprd) #pass in email and password as string

emailaddies = [] #list of email addresses you want to broadcast to as strings

for addy in emailaddies:

  conn.sendmail(senderemail, addy, 'Subject: TESTING....\n\nDear Charles,\nSo long, and thanks for all the memes.\n\n-Charles')
  #type in sender email as string, edit the subject and body of the email

conn.quit()
