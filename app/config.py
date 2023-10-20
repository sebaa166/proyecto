# Fichero de configuración config.py

class Config(object):
    SECRET_KEY = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_pass@prod_host:port/db_name'

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_pass@dev_host:port/db_name'

class StagingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_pass@staging_host:port/db_name'

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_pass@test_host:port/db_name'