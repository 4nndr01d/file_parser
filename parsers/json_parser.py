import json

from typing import List

from pydantic import parse_obj_as

from schemas import Work

from parsers.base import Parser


class JsonParser(Parser):
    def parse(self, file_path: str):
        content = open(file_path).read()
        data = json.loads(content)
        return parse_obj_as(List[Work], data)

