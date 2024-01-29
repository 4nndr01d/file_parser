from sqlalchemy import Column, Integer, Date, Float, String
from sqlalchemy.orm import declarative_base

from config.database import engine

Base = declarative_base()


class Work(Base):
    __tablename__ = 'work'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    WBS = Column(String(80), index=True, unique=True)
    NAME = Column(String(512))
    START_DATE = Column(Date)
    END_DATE = Column(Date)
    EFFORT = Column(Float, default=0)


Base.metadata.create_all(engine)
