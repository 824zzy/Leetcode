""" Maintain a MinStack
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.min = []
        
    def push(self, x: int) -> None:
        self.s.append(x)
        if self.min:
            self.min.append(min(self.min[-1], x))
        else:
            self.min.append(x)

    def pop(self) -> None:
        self.s.pop()
        self.min.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()