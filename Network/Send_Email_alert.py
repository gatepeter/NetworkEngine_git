import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def SendEmail(subject,to,body ):
    
    gmail_user = 'devicemonitor2020@gmail.com'
    gmail_password = 'pVzIUIAZi9I79lccqw6d@#$$#'
    sent_from = gmail_user
    msg = MIMEMultipart()
    msg['From'] = sent_from
    msg['To'] = to
    msg['Subject'] = subject
    body = MIMEText(body)
    # body = 'This is the body of the email.'
    msg.attach(body)


    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, msg.as_string())
        server.close()
    except:
        print ('Something went wrong...')



