from PySide6.QtCore import Qt, QAbstractListModel, QModelIndex

from sexbook.data import Report

UserRole = Qt.ItemDataRole.UserRole
TimeRole = UserRole
NameRole = UserRole + 1


class ReportListModel(QAbstractListModel):

    def __init__(self, reports: dict[int, Report]):
        super().__init__()
        self._items: list[Report] = list(reports.values())[:20]

    def rowCount(self, parent=QModelIndex()):
        return len(self._items)

    # noinspection PyMethodOverriding
    def data(self, index, role):
        if not index.isValid():
            return None
        if role == TimeRole:
            return self._items[index.row()].time
        if role == NameRole:
            return self._items[index.row()].name
        return None

    def roleNames(self):
        return {
            TimeRole: b"time",
            NameRole: b"name",
        }
