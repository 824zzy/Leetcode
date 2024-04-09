""" https://leetcode.com/problems/design-sql/
two hash tables to store the tables and row indexes
"""
from header import *


class SQL:
    def __init__(self, names: List[str], columns: List[int]):
        self.T = defaultdict(dict)
        self.cnt = Counter(names)

    def insertRow(self, name: str, row: List[str]) -> None:
        self.T[name][self.cnt[name]] = row
        self.cnt[name] += 1

    def deleteRow(self, name: str, rowId: int) -> None:
        self.T[name].pop(rowId)

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.T[name][rowId][columnId - 1]
