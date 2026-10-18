import os

class Config:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False