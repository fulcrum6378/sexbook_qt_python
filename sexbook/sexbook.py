import os
import sys

from PySide6.QtCore import QStringListModel
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from sqlalchemy import create_engine, select
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Session

from sexbook.base import Model
from sexbook.data import *


class Sexbook(QGuiApplication):
    """
    :ivar data_dir

    :ivar db: SQLAlchemy database engine
    :ivar reports: all [Report] instances in the database
    :ivar people: all [Crush] instances in the database
    :ivar places: all [Place] instances in the database
    :ivar guesses: all [Guess] instances in the database
    """

    # noinspection PyTypeChecker
    def __init__(self):
        super().__init__(sys.argv)

        # define and create a main data directory if it doesn't exist
        self.data_dir: str = os.path.join(os.getenv("APPDATA"), "Sexbook")
        if not os.path.isdir(self.data_dir): os.mkdir(self.data_dir)

        # initialise the database
        self.db: Engine = create_engine("sqlite:///" + os.path.join(self.data_dir, "sexbook.db"))
        Model.metadata.create_all(self.db)

        # load the entire database (all necessary!)
        with Session(self.db) as session:
            self.reports: dict[Report] = \
                dict(map(lambda r: (r.id, r), session.scalars(select(Report)).all()))
            self.people: dict[Crush] = \
                dict(map(lambda p: (p.key, p), session.scalars(select(Crush)).all()))
            self.places: list[Place] = session.scalars(select(Place)).all()
            self.guesses: list[Guess] = session.scalars(select(Guess)).all()

        # load the UI
        engine = QQmlApplicationEngine()
        string_model = QStringListModel(["Apple", "Banana", "Cherry"])
        engine.rootContext().setContextProperty("stringModel", string_model)
        engine.load("qml/Main.qml")
        if not engine.rootObjects():
            sys.exit(-1)

        sys.exit(self.exec())
