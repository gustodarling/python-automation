import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_user = ''
email_password = ''
email_send = ''
subject = 'Python'

msg = MIMEMultipart()
msg['FROM'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

good_morning = 'Good Morning,\n\nPlease advise on these parts.\n\nKindest Regards,'
good_afternoon = 'Good Afternoon,\n\nPlease advise on these parts.\n\nKindest Regards,'

msg.attach(MIMEText(good_morning, 'plain'))
text = msg.as_string()

server = smtplib.SMTP('', )
server.starttls()
server.login(email_user, email_password)

server.sendmail(email_user, email_send, text)
server.quit()