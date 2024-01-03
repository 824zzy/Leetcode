""" https://leetcode.com/problems/split-array-into-consecutive-subsequences/
1. greedily append x to x-1's sequence
2. otherwise, look for x+1 and x+2 and create a new sequence
"""
from header import *

class Solution:
    def isPossible(self, A: List[int]) -> bool:
        seen = Counter()
        left = Counter(A)
        for x in A:
            if left[x]==0: continue
            # greedily append x to x-1's sequence
            if seen[x-1]>0:
                seen[x-1] -= 1
                seen[x] += 1
                left[x] -= 1
            # otherwise, look for x+1 and x+2 and create a new sequence
            else:
                if left[x+1]==0 or left[x+2]==0: return False
                left[x] -= 1
                left[x+1] -= 1
                left[x+2] -= 1
                seen[x+2] += 1
        return True


s = Solution()
ans = s.isPossible([1,2,3,3,4,5])
print(ans)