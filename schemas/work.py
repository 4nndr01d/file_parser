from datetime import date

from pydantic import BaseModel


class Work(BaseModel):
    ID: int
    WBS: str
    NAME: str
    START_DATE: date
    END_DATE: date
    EFFORT: float
