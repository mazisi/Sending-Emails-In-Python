import smtplib
from email.message import EmailMessage
from string import Template #https://docs.python.org/3/library/string.html
from pathlib import Path #similar to os.path

def useGmailServer():
    template = Template(Path('email_template/emai_temp.html').read_text())
    email = EmailMessage()
    email['from'] = 'Mazisi Msebele'
    email['to'] = 'msebeletest@gmail.com'
    email['subject'] = 'Scripting With Python'

    # email.set_content('Come lets enjoy scripting with python') #plain text mail body
    email.set_content(template.substitute({'language': 'Python', 'name': 'mazisi'}), 'html')  #send using html template
    with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
        smtp.ehlo()
        smtp.starttls() #use tls encyption algorithm
        smtp.login('mazisi@gmail.com','fqpmizvkkhrsclqk') #remember to generate app password
        smtp.send_message(email)


#sending email with attachement use MIMEMultipart

def useMailtrapServer():
    sender = "Private Person <from@example.com>"
    receiver = "A Test User <to@example.com>"

    message = f"""\
    Subject: Hi Mailtrap
    To: {receiver}
    From: {sender}
    
    Come lets enjoy scripting with python."""

    with smtplib.SMTP("smtp.mailtrap.io") as server:
        server.login("cc6ff816900d6a", "9e77b9d1c21041")
        server.sendmail(sender, receiver, message)

# useMailtrapServer()
useGmailServer()