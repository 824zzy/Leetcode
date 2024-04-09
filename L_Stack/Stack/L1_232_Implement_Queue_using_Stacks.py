""" https://leetcode.com/problems/implement-queue-using-stacks/
using 2 stacks to implement a queue
"""


class MyQueue:
    def __init__(self):
        self.A = []
        self.B = []

    def push(self, x: int) -> None:
        self.A.append(x)

    def pop(self) -> int:
        if self.B:
            return self.B.pop()
        else:
            while self.A:
                self.B.append(self.A.pop())
            if self.B:
                return self.B.pop()

    def peek(self) -> int:
        if self.B:
            return self.B[-1]
        else:
            while self.A:
                self.B.append(self.A.pop())
            if self.B:
                return self.B[-1]

    def empty(self) -> bool:
        return (len(self.A) + len(self.B)) == 0
