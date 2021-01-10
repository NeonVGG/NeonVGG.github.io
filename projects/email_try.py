import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
from PIL import Image 
from PIL import ImageFont
from PIL import ImageDraw



file=pd.read_csv('feedback.csv')
df=pd.DataFrame(file)
emails=list(df["Username"])
names=list(df["Name"])

mail_content = '''Dear Participant,
Greetings from Atom Robotics Club
Thank you for attending our Webinar.
Your participant certificate is attached in this mail.
We hope to see you again!
'''
#The mail addresses and password
sender_address = 'sender@abc.com' 
sender_pass = 'password123'
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
    


for email_id,name in zip(emails,names):
    
    
    font = ImageFont.truetype("arial.ttf",size=30) #for different font,will have to copy font file into soruce folder
    img = Image.open('input.jpeg')
    draw =ImageDraw.Draw(img)
    draw.text((320,303),name,(0,0,0),font=font)
    img.save('CERTIFICATE.jpeg')
     
    receiver_address = email_id 
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Participation Certificate for attending our Webinar on Artificial Intelligence.'
    #Setup the MIME

    #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name ='CERTIFICATE.jpeg'
    attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload) #encode the attachment
    #add payload header with filename
    payload.add_header('Content-Disposition', "attachment; filename= %s" % attach_file_name)
    message.attach(payload)
    #Create SMTP session for sending the mail
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    print('Mail Sent to '+name)

session.quit()
