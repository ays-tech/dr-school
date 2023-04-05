class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"
    OPENAI_KEY = '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'

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}



key= 'AIzaSyDkUOlygb5IEw-B3XqM8ii-z31-WaFmg68'