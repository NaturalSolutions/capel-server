import os
from datetime import timedelta
try:
    from dba import DATABASE_URL, SENDGRID_KEY
    print('yay')
except Exception:
    # DATABASE_URL = f'postgresql://postgres:@localhost/capel'
    DATABASE_URL = os.environ.get('DATABASE_URL')
    SENDGRID_KEY = os.environ.get('SENDGRID_KEY')
    print('env')

SQLALCHEMY_DATABASE_URI = DATABASE_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWTSECRET = b'SUPER_SECRET'
JWT_AUTH_TYPE = 'Bearer'
JWT_ID_TK_EXP = timedelta(seconds=86400)
VALID_PWD_MIN_LEN = 6
VALID_EMAIL_REGEX = r'^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$'
PERMIT_TEMPLATE = 'assets/reglement_2017.pdf'
PERMITS_DIR = 'permits'
SENDGRID_API_KEY = SENDGRID_KEY
WEBAPP_URL = 'http://localhost:4200'
SERVER_URL = 'http://localhost:5000'
# SERVER_URL = 'https://capel-beta.herokuapp.com/'