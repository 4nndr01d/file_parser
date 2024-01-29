import openpyxl

from parsers.base import Parser
from schemas import Work


class XlsxParser(Parser):
    def parse(self, file_path: str):
        wb = openpyxl.load_workbook(file_path)
        worksheet = wb.active
        data = []
        for row in worksheet.iter_rows(min_row=2, values_only=True):
            # todo найти более простой способ считки данных
            data.append(Work(
                ID=row[0],
                WBS=row[1],
                NAME=row[2],
                START_DATE=row[3],
                END_DATE=row[4],
                EFFORT=row[5],
            ))
        return data
