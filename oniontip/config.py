# -*- config:utf-8 -*-
import os

project_name = 'tortip'
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
TESTING = False

# DATABASE CONFIGURATION
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'sqlite.db')
LOGGER_NAME = "%s_log" % project_name

# BITCOIN ADDRESS SEED - MUST BE SET TO A RANDOM VALUE
BITCOIN_KEY_SEED = os.environ.get('BITCOIN_KEY_SEED')

# MAIL SERVER SETTINGS
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None
MAIL_EMAIL = None

# administrator email list
ADMINS = ['twilde@bitcoin-home.krellis.org']

SERVER_NAME = 'tortip.com'
