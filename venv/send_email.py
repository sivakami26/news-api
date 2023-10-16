import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    password = "zeiz pbaw gkia gsyf"
    username = "sivakami2607@gmail.com"
    receiver = "sivakami2607@gmail.com"
    context = ssl.create_default_context()

   
    

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)



