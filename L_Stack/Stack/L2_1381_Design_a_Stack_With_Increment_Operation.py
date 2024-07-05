""" https://leetcode.com/problems/design-a-stack-with-increment-operation/
lazy increment stack
steal from: https://leetcode.com/problems/design-a-stack-with-increment-operation/discuss/539716/JavaC%2B%2BPython-Lazy-increment-O(1)
"""


class CustomStack:
    def __init__(self, maxSize: int):
        self.size = maxSize
        self.stk = []
        self.lazy_inc = []

    def push(self, x: int) -> None:
        if len(self.stk) < self.size:
            self.stk.append(x)
            self.lazy_inc.append(0)

    def pop(self) -> int:
        if not self.stk:
            return -1
        if len(self.lazy_inc) > 1:
            self.lazy_inc[-2] += self.lazy_inc[-1]
        return self.stk.pop() + self.lazy_inc.pop()

    def increment(self, k: int, val: int) -> None:
        if self.lazy_inc:
            self.lazy_inc[min(k, len(self.lazy_inc)) - 1] += val
