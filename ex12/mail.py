from flask import Flask, request, jsonify
import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

app = Flask(__name__)

def send_test_mail(body):
    sender_email = "cheseo@student.42seoul.kr"
    receiver_email = "cheseo@sharklasers.com"
    user = input("Enter your smtp user: ")
    password = getpass.getpass("Enter password: ")

    msg = MIMEMultipart()
    msg['Subject'] = '[Email Test]'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    msgText = MIMEText('<b>%s</b>' % (body), 'html')
    msg.attach(msgText)

    #filename = "example.txt"
    #msg.attach(MIMEText(open(filename).read()))

    with open('./42.png', 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', 'attachment', filename="42.png")
        msg.attach(img)
        
    #pdf = MIMEApplication(open("example.pdf", 'rb').read())
    #pdf.add_header('Content-Disposition', 'attachment', filename= "example.pdf")
    #msg.attach(pdf)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtpObj:
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login(user, password)
            smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        print(e)
        
@app.route('/')
def hello_world():
    return "Hello world!"

if __name__ == "__main__":
    send_test_mail("Welcome to cheseo smtp email!")
    app.run('0.0.0.0',port=5000)
