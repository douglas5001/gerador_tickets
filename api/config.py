DEBUG = True

USERNAME = 'root'
PASSWORD = 'postgres'
SERVER = 'localhost'
DB = 'mydatabase'

SQLALCHEMY_DATABASE_URI = f'postgresql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
