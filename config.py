import os

class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = 'NEED TO THINK of A STRONG PASSWORD'

class DevelopmentConfig(BaseConfig):
	DEBUG = True
	
	"""
	#For GMAIL server

	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 465
	MAIL_USE_TLS = False
	MAIL_USE_SSL = True
	MAIL_USERNAME = 'shiva.aratal@gmail.com'
	MAIL_PASSWORD = 'passwordpasswordPASSWORDPASSWORD'
	"""