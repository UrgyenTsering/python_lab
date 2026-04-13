from mailerpy import Mailer

password = "qgwk rnkt unrn izom"

my_mailer = Mailer("smtp.gmail.com", 587, "urgentsering77@gmail.com", password)

to_emails = [
    "bijayayer68@gmail.com",
    "urgentsering77@gmail.com",
]
attachment = [r"/Users/urgyentsering/Desktop/python.txt"]
subject = "Test From Python"
body = f"""
Hello Guys,

This is from code.

Regards,
Automation Engine
"""


for to_email in to_emails:
    mail_body = body.replace("Guys", to_email.split("@")[0])
    my_mailer.send_mail([to_email], subject, mail_body, attachments=attachment)
