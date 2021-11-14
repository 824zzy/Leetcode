""" L0: simulation
"""
class MyCalendar:
    def __init__(self):
        self.C = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.C:
            if s<start<e or s<end<e or (start<=s and end>=e):
                return False
        self.C.append((start, end))
        return True