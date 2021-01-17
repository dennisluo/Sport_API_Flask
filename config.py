class Config(object):
    TESTING = False
    DEBUG = False


class Development(Config):
    DEBUG = True


class TESTING(Config):
    TESTING = True


class PRODUCTION(Config):
    TESTING = False
    DEBUG = False


config = {
    'development': Development,
    'testing': TESTING,
    'production': PRODUCTION
}
