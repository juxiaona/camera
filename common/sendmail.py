import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

class SendMail():

	def __init__(self,server,username,password,receiver):

		#发件邮箱的服务器
		self.server=server
		#发件邮箱的用户名和密码
		self.username=username
		self.password=password
		#发件邮箱使用用户名
		self.sender=username
		#收件邮箱
		self.receiver=receiver

	#发送邮件
	def sendmail(self,filename):

		'''主题'''
		subject="自动化测试报告"

		'''正文'''
		mail_text=MIMEText('自动化测试报告','plain','utf-8')

		'''附件'''
		sendfile=open(filename,'rb').read()
		mail_att = MIMEText(sendfile, 'base64', 'utf-8')
		mail_att["Content-Type"] = 'application/octet-stream'
		mail_att["Content-Disposition"] = 'attachment; filename="test_report.html"'

		'''创建一个带附件的实例'''
		msg= MIMEMultipart()
		msg['Subject'] = subject
		msg['From']='API Test'
		msg.attach(mail_text)
		msg.attach(mail_att)

		'''连接发送邮件'''
		smtp=smtplib.SMTP_SSL()
		smtp.connect(self.server)
		smtp.helo(self.server)
		smtp.ehlo(self.server)
		smtp.login(self.username, self.password)
		smtp.sendmail(self.sender, self.receiver, msg.as_string())
		smtp.quit()



