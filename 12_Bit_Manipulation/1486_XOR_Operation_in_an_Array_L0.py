""" Reduce trick
"""
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return reduce(lambda a,b: a^b, [start+2*i for i in range(n)])