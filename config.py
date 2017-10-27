import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    
    SECRET_KEY = 'You cannot hack this site fool'

    @staticmethod
    def init_app(app):
        pass

class Development(Config):
    DEBUG = True


class Testing(Config):
    TESTING = True

class Production(Config):
    DEBUG = False

config = {
    'development': Development,
    'testing': Testing,
    'production': Production,
    'default': Development
}
