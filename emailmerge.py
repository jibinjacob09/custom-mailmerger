import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import emailmerge_lib

sender_name = emailmerge_lib.sender_email[0]
sender_email = emailmerge_lib.sender_email[1]
failed_emails = list()

#opening connection to server
try:
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.ehlo()
except SMTPHeloError:
    print ("couldnt say ehlo to the server")
try:
    server.login(sender_email, emailmerge_lib.sender_email[2])
except smtplib.SMTPAuthenticationError:
    print("trouble with authentication ")

#looping through all in email_list
print("Sending email to:")
for email in emailmerge_lib.email_list:
    if emailmerge_lib.email_list.index(email) == 0:
        continue

    # drafting email
    target_email = email[2]
    first_name = email[0]
    last_name = email[1]
    subject = emailmerge_lib.email_subject
    email_body = emailmerge_lib.email_body.format(f_name = first_name, l_name = last_name)
    msg = MIMEMultipart()

    msg['From'] = sender_name
    msg['To'] = target_email
    msg['Subject'] = subject

    msg.attach(MIMEText(email_body, 'html'))

    # adding attachments
    msg.attach(emailmerge_lib.attachment_part)

    # sending email
    print("\t{} {}".format(first_name, last_name)) # name of the recieptant
    try:
        message = msg.as_string()
        server.sendmail(sender_email, target_email, message)
    except SMTPException:
        # adding emails to the failed list
        failed_emails.append(target_email)

server.close()

if len(failed_emails) > 0:
    print ("\n{0} of {1} could not be sent".format(len(failed_emails), len(emailmerge_lib.email_list)))
    for email in failed_emails:
        print("\t" + email)
else:
    print ("Emails sent")
