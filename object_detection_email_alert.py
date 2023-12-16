import smtplib

def send_email(subject, body):
    smtp_server = 'your_smtp_server'
    smtp_port = 587
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_email_password'
    receiver_email = 'receiver_email@gmail.com'

    message = f'Subject: {subject}\n\n{body}'

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)

# Call send_email when object is detected
