""" https://leetcode.com/problems/implement-queue-using-stacks/
using 2 stacks to implement a queue
"""
# Using 2 stacks
class MyQueue:
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def push(self, x: int) -> None:
        self.stk1.append(x)

    def pop(self) -> int:
        ans = self.peek()
        self.stk2.pop()
        return ans        

    def peek(self) -> int:
        if not self.stk2:
            while self.stk1:
                self.stk2.append(self.stk1.pop())
        return self.stk2[-1]

    def empty(self) -> bool:
        return (len(self.stk1)+len(self.stk2))==0

# cheating
class MyQueue:
    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.q.pop(0)

    def peek(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q)==0