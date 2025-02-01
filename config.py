import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('sqlite:///licencas.db')  
    SQLALCHEMY_TRACK_MODIFICATIONS = False