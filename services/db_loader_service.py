from typing import List, Dict

from sqlalchemy.dialects.sqlite import insert

from config.database import Session
from models import Work


class DbLoaderService:

    def __init__(self, session: Session) -> None:
        self.session = session

    def upload(self, data: List[Dict]) -> None:
        # todo Убрать этот костыль
        data = [val.dict() for val in data]

        offset = 0
        while offset < len(data):
            stmt = insert(Work).values(data[offset:offset+100])

            stmt = stmt.on_conflict_do_update(
                index_elements=[Work.ID],
                set_=dict(WBS=stmt.excluded.WBS)
            )
            self.session.execute(stmt)
            self.session.commit()
            offset += 100
