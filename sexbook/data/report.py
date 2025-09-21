from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from sexbook.base import Model


class Report(Model):
    __tablename__ = "Report"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    time: Mapped[int]
    name: Mapped[Optional[str]]
    type: Mapped[int] = mapped_column(default=1)
    place: Mapped[Optional[int]]
    description: Mapped[Optional[str]]
    accurate: Mapped[bool] = mapped_column(default=True)
    orgasmed: Mapped[bool] = mapped_column(default=True)

    def analyse(self):
        # noinspection PyAttributeOutsideInit
        self.analysis = map(
            lambda s: s.strip(),
            (self.name.replace(" and ", " + ")
             .replace(" & ", " + ")
             .replace(", ", " + ")
             .split(" + "))
        ) if self.name else list()

    def to_json(self) -> dict:
        ret = dict()
        ret['time'] = self.time
        if self.name is not None and len(self.name) > 0:
            ret['name'] = self.name
        ret['type'] = self.type
        if self.place is not None:
            ret['place'] = self.place
        if self.description is not None and len(self.description) > 0:
            ret['description'] = self.description
        if not self.accurate:
            ret['accurate'] = self.accurate
        if not self.orgasmed:
            ret['orgasmed'] = self.orgasmed
        return ret

    @staticmethod
    def from_json(o: dict):
        return Report(
            time=o['time'],
            name=o['name'] if 'name' in o else None,
            type=o['type'],
            place=o['place'] if 'place' in o else None,
            description=o['description'] if 'description' in o else None,
            accurate=o['accurate'] if 'accurate' in o else True,
            orgasmed=o['orgasmed'] if 'orgasmed' in o else True,
        )

    class Filter:
        """
        A timeframe for dividing a long list of `Reports`

        :ivar id a sortable hash integer made out of `year` and `month`
        :ivar year
        :ivar month
        :ivar reports ID numbers of the `Report`s that belong to this timeframe
        """

        def __init__(self, report):
            if not hasattr(report, "datetime"):
                report.datetime = datetime.fromtimestamp(report.time / 1000.0)
            self.year: int = report.datetime.year
            self.month: int = report.datetime.month
            self.id = (self.year << 4) | self.month
            self.reports: list[int] = list()

        def __hash__(self):
            return self.id

        def __eq__(self, other):
            return self.id == other.__hash__()

        def __ne__(self, other):
            return self.id != other.__hash__()

        def __lt__(self, other):
            return self.id < other.__hash__()

        def __le__(self, other):
            return self.id <= other.__hash__()

        def __gt__(self, other):
            return self.id > other.__hash__()

        def __ge__(self, other):
            return self.id >= other.__hash__()

        def __repr__(self):
            return (f"Filter-{self.year}.{self.month}-"
                    f"({len(self.reports)} item{"s" if len(self.reports) != 1 else ""})")
