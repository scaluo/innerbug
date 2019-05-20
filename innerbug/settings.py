import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

class BaseConfig():
    SECRET_KEY = '3e88661142ee49ecbee578818d8csfd'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = \
        prefix + os.path.join(basedir, 'data-dev.db')
    

class ProductConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = \
        prefix + os.path.join(basedir, 'data.db')

config = {'development':DevelopmentConfig,
          'production':ProductConfig}