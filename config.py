"""Contains the various configuration settings for different app environments"""
import os

class Config:
    """
    Contains the common setings that all configuration options must have
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or\
                'You cannot hack this site fool'

    @staticmethod
    def init_app(app):
        """
        To perform configuration specific initializations
        """
        pass

class Development(Config):
    """
    Configurations used by developer
    """
    DEBUG = True


class Testing(Config):
    """
    Configurations used for testing
    """
    TESTING = True

class Production(Config):
    """C
    onfigurations used after product release
    """
    DEBUG = False
#Registers the various configurations and provides a default
config = {
    'development': Development,
    'testing': Testing,
    'production': Production,
    'default': Development
}
