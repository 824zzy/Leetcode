""" https://leetcode.com/problems/min-stack/
maintain minimum in the stack, note that reset minimum when stack is empty
"""
class MinStack:
    def __init__(self):
        self.stk = []
        self.min = inf

    def push(self, val: int) -> None:
        if val<self.min: self.min = val
        self.stk.append([val, self.min])
        

    def pop(self) -> None:
        self.stk.pop()
        if self.stk: self.min = self.stk[-1][1]
        else: self.min = inf

    def top(self) -> int:
        return self.stk[-1][0]
        
    def getMin(self) -> int:
        return self.stk[-1][1]