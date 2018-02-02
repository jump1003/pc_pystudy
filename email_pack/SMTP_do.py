from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import  Header
from email import encoders
from email.utils import parseaddr,formataddr
import smtplib

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))


# 输入Email地址和命令：
from_addr = '171149320@qq.com'  # input('From:')
password = 'TRYmybest.'  # input('Password:')
# 输入收件人地址：
to_addr = input('To:')
# 输入SMTP服务器地址：
smtp_server = 'smtp.qq.com'  # input('SMTP server:')

text = ''  # input('Send text:')
msg = MIMEMultipart()
msg['From'] = _format_addr('你黑哥 <%s>' % from_addr)
msg['to'] = _format_addr("兔崽 <%s>" % to_addr)
msg['Subject'] = Header('来自JUMP的测试。。。', 'utf-8').encode()

msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '<p>发个邮件测试下</p>' +
    '<p><img src="cid:0"></p>'
    '</body></html>', 'html', 'utf-8'))

with open(r'C:\Users\Jump hu\Pictures\psu.jpg', 'rb') as f:
	mime = MIMEBase('image', 'jpeg', filename='psu.jpg')
	mime.add_header('Content-Disposition', 'attachment', filename='psu.jpg')
	mime.add_header('Content-ID', '<0>')
	mime.add_header('X-Attachment-Id', '0')
	mime.set_payload(f.read())
	encoders.encode_base64(mime)
	msg.attach(mime)
	
server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
server.set_debuglevel(1)
server.starttls()
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
