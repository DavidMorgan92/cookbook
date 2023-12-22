import os
import smtplib
from email.message import EmailMessage

# https://docs.python.org/3/library/email.examples.html
def send_message(name, email, message):
    """Send a message to the configured recipient."""

    try:
        # Create message with user's input details
        msg = EmailMessage()
        msg.set_content(f"Name: {name}\nEmail: {email}\nMessage: {message}")

        # Use configured values for From and To
        msg["Subject"] = "Message from Cook Book user"
        msg["From"] = os.environ.get("EMAIL_FROM")
        msg["To"] = os.environ.get("EMAIL_TO")

        # Use configured values for SMTP host
        host = os.environ.get("EMAIL_HOST")
        port = int(os.environ.get("EMAIL_PORT"))
        user = os.environ.get("EMAIL_USER")
        password = os.environ.get("EMAIL_PASSWORD")

        # Send the SMTP message
        s = smtplib.SMTP(host, port)
        s.starttls()
        s.login(user, password)
        s.send_message(msg)
        s.quit()
    except:
        # Return False if anything goes wrong
        return False
    
    # Return True if the message was sent
    return True
