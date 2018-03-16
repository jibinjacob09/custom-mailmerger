from os import path
from email.mime.base import MIMEBase
from email import encoders
import csv

# getting email list
email_list = list()
with open("email_list.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        email_list.append(row)
f.close()

# getting emailbody
print("Fetching the emailbody")
email_subject = ""
email_body = ""
with open("emailtext.html") as f:
    email_subject = f.readline()

    # getting the Subject Line
    if email_subject[0:len("<Subject:")] != "<Subject:":
        print("\n\nEmail text in wrong format, cannot read a subject line. "+
              " Please make sure Subject: field is present")
        exit(0)
    else: # filtering the subject line
        email_subject = email_subject[len("<Subject: "):email_subject.find(">")]

    email_body = f.read()
f.close()

# getting sender's email address and password
print ("Fetching account credentials")
sender_email =  None
with open("secrets.txt") as f:
    reader = csv.reader(f)
    for row in reader:
        sender_email = row
f.close()

# getting the attachments
print ("Fetching all attachments")
lst_attachments = open(path.realpath("") + "/attachments/sample.txt")
file_name = "sample.txt"
attachment_part = MIMEBase('application', 'octet-stream')
attachment_part.set_payload((lst_attachments).read())
encoders.encode_base64(attachment_part)
attachment_part.add_header('Content-Disposition', "attachment; filename= %s" % file_name)
