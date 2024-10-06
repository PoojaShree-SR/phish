//pip install smtplib
//pip install email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_phishing_email(sender_email, app_password, recipients, subject, body):
    # SMTP server configuration for Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create SMTP session for sending email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, app_password)

        for recipient in recipients:
            try:
                # Create the email content
                message = MIMEMultipart()
                message['From'] = sender_email
                message['To'] = recipient
                message['Subject'] = subject

                # Attach the email body to the MIME message
                message.attach(MIMEText(body, 'html'))

                # Send the email
                server.sendmail(sender_email, recipient, message.as_string())
                print(f"Email sent to {recipient}")
            except Exception as e:
                print(f"Failed to send email to {recipient}: {e}")

if __name__ == "__main__":
    # Sender details
    sender_email = "your-email@gmail.com"
    app_password = "your-app-password"

    # List of recipient email addresses (your test users)
    recipients = [
        "user1@example.com",
        "user2@example.com",
        "user3@example.com"
    ]

    # Email subject and body (you can customize this)
    subject = "Urgent: Action Required for Your Account"
    body = """
    <html>
    <body>
        <p>Dear User,</p>
        <p>We have detected unusual activity on your account. Please click the link below to verify your credentials and secure your account:</p>
        <p><a href="http://your-phishing-link.com">Verify Your Account</a></p>
        <p>Thank you,</p>
        <p>Your Security Team</p>
    </body>
    </html>
    """

    # Call the function to send the email
    send_phishing_email(sender_email, app_password, recipients, subject, body)
