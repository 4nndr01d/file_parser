import os

import typer

from config.database import Session
from parsers import JsonParser, XlsxParser
from services import DbLoaderService
from parsers.exceptions import InvalidFileExtension, FileNotExists

app = typer.Typer()


@app.command()
def loader(path: str):
    if not os.path.isfile(path):
        raise FileNotExists
    extension = path.split('.')

    if extension[-1] == 'json':
        parser = JsonParser()
        data = parser.parse(path)
    elif extension[-1] == 'xlsx':
        parser = XlsxParser()
        data = parser.parse(path)
    else:
        raise InvalidFileExtension

    session = Session()
    service = DbLoaderService(session)
    service.upload(data)


@app.callback()
def callback():
    # todo Костыль что бы команда работала в соответствии с тз(как в доке)
    pass


# todo В скрине даты являются обязательными полями, при этом в файлах есть пустые поля

if __name__ == "__main__":
    app()
