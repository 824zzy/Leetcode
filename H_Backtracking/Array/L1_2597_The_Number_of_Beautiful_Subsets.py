""" https://leetcode.com/problems/the-number-of-beautiful-subsets/
subset ==> backtracking

1. sort the array
2. backtracking using hash table
"""
from header import *
class Solution:
    def beautifulSubsets(self, A: List[int], k: int) -> int:
        A.sort()
        
        def dfs(i):
            if i==len(A):
                return 0
            cnt = 0
            cnt += dfs(i+1)
            if sub[A[i]-k]==0:
                sub[A[i]] += 1
                cnt += 1 + dfs(i+1)
                sub[A[i]] -= 1
            return cnt
            
        sub = Counter()
        return dfs(0)
    
    
""" 1048575
[2,4,6]
2
[1]
1
[1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000]
1
"""