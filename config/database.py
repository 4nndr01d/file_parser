from decouple import config

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

SQLITE_PATH = config('SQLITE_PATH', default='sqlite.db', cast=str)
engine = db.create_engine(f'sqlite:///{SQLITE_PATH}')
Session = sessionmaker(bind=engine)
