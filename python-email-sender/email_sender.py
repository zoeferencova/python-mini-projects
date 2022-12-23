import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Zoe Ferencova'
email['to'] = 'zoeferencova@gmail.com'
email['subject'] = 'Hello There'

email.set_content(html.substitute({'name': 'Zoe'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('zoeferencova@gmail.com', 'zqpzelsodvcrfdyo')
    smtp.send_message(email)
    print('all good')
