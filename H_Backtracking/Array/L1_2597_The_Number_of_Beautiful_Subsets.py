""" https://leetcode.com/problems/the-number-of-beautiful-subsets/
subset ==> backtracking

1. sort the array
2. backtracking using hash table or bitmask power set
"""
from header import *


class Solution:
    def beautifulSubsets(self, A: List[int], k: int) -> int:
        A.sort()

        def dfs(i):
            if i == len(A):
                return 0
            cnt = 0
            cnt += dfs(i + 1)
            if sub[A[i] - k] == 0:
                sub[A[i]] += 1
                cnt += 1 + dfs(i + 1)
                sub[A[i]] -= 1
            return cnt

        sub = Counter()
        return dfs(0)


class Solution:
    def beautifulSubsets(self, A: List[int], k: int) -> int:
        A.sort()
        ans = 0
        for mask in range(1, 1 << len(A)):
            seen = set()
            for i in range(len(A)):
                if mask & 1 << i:
                    if A[i] - k in seen:
                        break
                    seen.add(A[i])
            else:
                ans += 1
        return ans


""" 1048575
[2,4,6]
2
[1]
1
[1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000]
1
"""
