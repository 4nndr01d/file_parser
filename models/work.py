from sqlalchemy import Column, Integer, Date, Float, String
from sqlalchemy.orm import declarative_base

from config.database import engine

Base = declarative_base()


class Work(Base):
    __tablename__ = 'work'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    WBS = Column(String(80))
    NAME = Column(String(512))
    START_DATE = Column(Date, nullable=True)
    END_DATE = Column(Date, nullable=True)
    EFFORT = Column(Float)


Base.metadata.create_all(engine)
