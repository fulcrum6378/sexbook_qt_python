from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from sexbook.base import Model


class Guess(Model):
    __tablename__ = "Guess"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[Optional[str]]
    since: Mapped[Optional[int]]
    until: Mapped[Optional[int]]
    frequency: Mapped[float] = mapped_column(default=0)
    type: Mapped[int] = mapped_column(default=1)
    place: Mapped[Optional[int]]
    description: Mapped[Optional[str]]
    active: Mapped[bool]

    def to_json(self) -> dict:
        ret = dict()
        if self.name is not None and len(self.name) > 0:
            ret['name'] = self.name
        if self.since is not None:
            ret['since'] = self.since
        if self.until is not None:
            ret['until'] = self.until
        ret['frequency'] = self.frequency
        ret['type'] = self.type
        if self.place is not None:
            ret['place'] = self.place
        if self.description is not None and len(self.description) > 0:
            ret['description'] = self.description
        if not self.active:
            ret['active'] = self.active
        return ret

    @staticmethod
    def from_json(o: dict):
        return Guess(
            name=o['name'] if 'name' in o else None,
            since=o['since'] if 'since' in o else None,
            until=o['until'] if 'until' in o else None,
            frequency=o['frequency'],
            type=o['type'],
            place=o['place'] if 'place' in o else None,
            description=o['description'] if 'description' in o else None,
            active=o['active'] if 'active' in o else True,
        )
