""" https://leetcode.com/problems/minimize-xor/
Let bits count of n1 and n2 be x1 and x2, d as abs(x1-x2). there are two conditions from lower bit to higher bit:
1. if x1>=x2, we flip n1's 1 to 0 until d==0
2. if x1<x2, we flip n1's 0 to 1 until d==0

"""
class Solution:
    def minimizeXor(self, n1: int, n2: int) -> int:
        x1, x2 = n1.bit_count(), n2.bit_count()
        d = abs(x1-x2)
        for i in range(31):
            if (x1>=x2 and n1&(1<<i)) or (x1<x2 and not n1&(1<<i)):
                if d:
                    d -= 1
                    n1 ^= (1<<i)
                else: break
        return n1