import os

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Session

from sexbook.base import Model
from sexbook.ctrl import Exporter
from sexbook.data import Crush

data_dir: str = os.path.join(os.getenv("APPDATA"), "Sexbook")
if not os.path.isdir(data_dir): os.mkdir(data_dir)
engine: Engine = create_engine("sqlite:///" + os.path.join(data_dir, "sexbook.db"))
Model.metadata.create_all(engine)

with Session(engine) as session:
    Exporter.replace(session, Exporter.import_("../../Dropbox/Personal/sexbook.json"))
    # noinspection PyArgumentList
    print(session.get_one(Crush, "Yuriko").to_json())
