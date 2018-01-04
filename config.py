import os

class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = 'NEED TO THINK of A STRONG PASSWORD'

class DevelopmentConfig(BaseConfig):
	DEBUG = True
