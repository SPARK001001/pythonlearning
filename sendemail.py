# _*_coding:utf-8_*_
from email import encoders 
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr,formataddr

import smtplib

def _format_addr(s):
	name,addr = parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))

from_addr = 'seepjr@sina.com'
password = input('Password: ')
to_addr = '13718921299@163.com'
smtp_server = 'smtp.sina.com'

msg = MIMEMultipart()
msg['From'] = _format_addr('嗨<%s>'% from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('你好...','utf-8').encode()

msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))

with open('./good.png','rb') as f:
	mime = MIMEBase('image','png',filename='good.png')
	mime.add_header('Content-Discription','attachment',filename='good.png')
	mime.add_header('Content-ID','<0>')
	mime.add_header('X-Attachment-Id','0')
	mime.set_payload(f.read())
	encoders.encode_base64(mime)
	msg.attach(mime)



server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
