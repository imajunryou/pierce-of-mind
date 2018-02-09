class Config:
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(dev=DevelopmentConfig,
                      test=TestConfig,
                      prod=ProductionConfig
                      )
