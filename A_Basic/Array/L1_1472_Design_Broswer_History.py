""" https://leetcode.com/problems/design-browser-history/
simulate a dynamic array
"""


class BrowserHistory:
    def __init__(self, homepage: str):
        self.A = [homepage]
        self.idx = 0

    def visit(self, url: str) -> None:
        if self.idx != len(self.A) - 1:
            self.A = self.A[: self.idx + 1]
        self.A.append(url)
        self.idx += 1

    def back(self, steps: int) -> str:
        if steps <= self.idx:
            self.idx -= steps
            return self.A[self.idx]
        else:
            self.idx = 0
            return self.A[0]

    def forward(self, steps: int) -> str:
        if self.idx + steps < len(self.A):
            self.idx += steps
            return self.A[self.idx]
        else:
            self.idx = len(self.A) - 1
            return self.A[self.idx]
