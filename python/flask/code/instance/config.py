DEBUG = True

DBUSER = 'postgres'
DBPASS = 'test'
DBHOST = 'db'
DBPORT = '5432'
DBNAME = 'flaskdb'

SQLALCHEMY_DATABASE_URI = \
    'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=DBUSER,
        passwd=DBPASS,
        host=DBHOST,
        port=DBPORT,
        db=DBNAME
    )

SQLALCHEMY_TRACK_MODIFICATIONS = True

MAIL_SERVER = 'maildev'
MAIL_PORT = 25
MAIL_DEFAULT_SENDER : None
MAIL_SUPPRESS_SEND: False