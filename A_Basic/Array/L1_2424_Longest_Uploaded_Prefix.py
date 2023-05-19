""" https://leetcode.com/problems/longest-uploaded-prefix/
If we maintain a list for all the segments so far, the longest uploaded prefix essentially is the size of the first element a.k.a self.P[1] in my case for avoiding index overflow.

The only tricky part is the way to update left&right most endpoints:
1. find left most endpoint(x-self.P[x-1]) and rightmost endpoint(x+self.P[x+1])
2. update the whole segment by summing up two segments and plus more element (self.P[x-1]+self.P[x+1]+1)
"""
class LUPrefix:
    def __init__(self, n: int):
        self.P = [0]*(n+2)

    def upload(self, x: int) -> None:
        self.P[x-self.P[x-1]] = self.P[x+self.P[x+1]] = self.P[x-1]+self.P[x+1]+1

    def longest(self) -> int:
        return self.P[1]