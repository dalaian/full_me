import smtplib
import datetime
from email.message import EmailMessage
import pytz
import utils.config as config

def send_email():
    x = datetime.datetime.now(pytz.timezone('America/Costa_Rica'))    
    msg = EmailMessage()
    to = config.email_to
    msg.set_content(f'''
        Hi, please review the test report executed on {x.strftime("%c")} by clicking on the following link:

        https://dalaian.github.io/full_me/

        Regards,

        QA Team
         ''')

    msg['Subject'] = 'Testing report'
    msg['From'] = config.email_from
    msg['To'] = to

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(config.email_from, config.email_from_pass)
    server.send_message(msg)
    server.quit()
    