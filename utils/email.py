import smtplib
import datetime
from email.message import EmailMessage
import pytz
import utils.config as config


def send_email():
    x = datetime.datetime.now(pytz.timezone("America/Costa_Rica"))
    msg = EmailMessage()
    to = config.email_to
    msg.set_content(
        f"""
        Hi Team,

        The automated regression tests have completed successfully on {x.strftime("%c")}. You can access the test report using the following link:

        https://dalaian.github.io/full_me/

        Please review the results and let me know if you have any questions or concerns.
        Best regards,

        QA Team
        """
    )

    msg["Subject"] = "Testing report"
    msg["From"] = config.email_from
    msg["To"] = to

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(config.email_from, config.email_from_pass)
    server.send_message(msg)
    server.quit()
