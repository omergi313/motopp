import os
class Config:
    if os.environ.get('ENV') == 'prod':
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@mysql:3306/motopp'
        SECRET_KEY = '123456789'
        SQLALCHEMY_ECHO = True

    else:
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/motopp'
        SECRET_KEY = '123456789'
        SQLALCHEMY_ECHO = False
