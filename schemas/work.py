from datetime import date
from typing import Optional

from pydantic import BaseModel


class Work(BaseModel):
    ID: int
    WBS: str
    NAME: str
    START_DATE: Optional[date]
    END_DATE: Optional[date]
    EFFORT: float
