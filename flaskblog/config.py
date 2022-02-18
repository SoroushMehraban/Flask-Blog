import os


class Config:
    SECRET_KEY = 'd704758b66871626262414b5c48f51bc'
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"

    # Mail server
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
