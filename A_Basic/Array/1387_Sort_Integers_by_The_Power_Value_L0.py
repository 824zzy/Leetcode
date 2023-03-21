""" https://leetcode.com/problems/sort-integers-by-the-power-value/
implementation using hash table
"""
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def fn(x):
            cnt = 0
            while x!=1:
                if x&1:
                    x = 3*x+1
                else:
                    x //= 2
                cnt += 1
            return cnt
            
        mp = {}
        for i in range(lo, hi+1):
            mp[i] = fn(i)
        return sorted(mp.items(), key=lambda x: (x[1], x[0]))[k-1][0]