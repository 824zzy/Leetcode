""" Check each element by dynamic programming 
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        res = [0] * n
        res[0], res[1] = 0, 0

        for i in range(2, n):
            if res[i] == 1:
                for j in range(2, (n-1)//j+1):
                    res[i*j] = 0
        return res