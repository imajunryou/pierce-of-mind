import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True,
    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" + os.path.join(basedir, "pierceofmind.db")
    )


class TestConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(dev=DevelopmentConfig,
                      test=TestConfig,
                      prod=ProductionConfig
                      )
