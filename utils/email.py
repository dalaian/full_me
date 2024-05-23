import os
import smtplib
import datetime
from email.message import EmailMessage


def send_email():
    x = datetime.datetime.now()    
    msg = EmailMessage()
    msg.set_content(f'''
        Hi, please review the test report executed on {x.strftime("%c")} by clicking on the following link:

        https://dalaian.github.io/full_me/

        Regards,

        QA Team
         ''')

    msg['Subject'] = 'Testing report'
    msg['From'] = "dalaianxd@gmail.com"
    msg['To'] = "dalaian@outlook.com"

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('dalaianxd@gmail.com', os.environ.get('email_password'))
    server.send_message(msg)
    server.quit()