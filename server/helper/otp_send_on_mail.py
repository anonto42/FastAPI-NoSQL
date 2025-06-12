import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from server.templates.otp_template import otp_body
from server.config import env

def send_email(otp, recipient_email, recipient_name, subject):
    
    # Email server configuration
    smtp_host = env.SMTP_HOST
    smtp_port = env.SMTP_PORT
    sender_email = env.SENDER_EMAIL
    sender_password = env.SENDER_PASSWORD

    # Create email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = 'Your OTP Code'

    # Replace placeholders in template with OTP and recipient name
    html_content = otp_body(otp,recipient_name,subject)

    # Attach HTML content to the email
    message.attach(MIMEText(html_content, 'html'))

    # Send email using SMTP server
    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()  # Secure connection using TLS
            server.login(sender_email, sender_password)  # Login to the email account
            server.sendmail(sender_email, recipient_email, message.as_string())  # Send the email
            print("OTP email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
