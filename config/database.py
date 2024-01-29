from decouple import config

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

SQLITE_PATH = config('SQLITE_PATH', 'sqlite.db')
engine = db.create_engine(f'sqlite:///{SQLITE_PATH}')
Session = sessionmaker(bind=engine)
