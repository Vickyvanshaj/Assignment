import smtplib
class Solution:
	def fn(self):
		s=smtplib.SMTP('smtp.gmail.com',587)
		s.starttls()
		s.login("your_email","your_password")
		SUBJECT=input("Subject?")
		TEXT=input("Body?")
		recipient=input("Recipient?")
		message='Subject: {}\n\n{}'.format(SUBJECT, TEXT)

		s.sendmail("your_email",recipient,message)
		print('Email Sent!')
		s.quit()


Solution().fn()


