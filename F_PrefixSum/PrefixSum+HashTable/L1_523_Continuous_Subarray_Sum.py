""" https://leetcode.com/problems/continuous-subarray-sum/
prefix sum + hash table

(presum[j]-presum[i]) % k = 0
==> presum[j] % k = presum[i] % k, when presum[j]-presum[i] is positive
"""
from header import *

class Solution:
    def checkSubarraySum(self, A: List[int], k: int) -> bool:
        cnt = Counter()
        cnt[0] = -1
        pre = 0
        for i, x in enumerate(A):
            pre = (pre+x)%k
            if pre in cnt:
                if i-cnt[pre]>1:
                    return True
            cnt.setdefault(pre, i)
        return False

"""
[23,2,4,6,7]
6
[23,2,6,4,7]
6
[23,2,6,4,7]
13
[23,2,4,6,6]
7
[1,2,3]
5
[0]
1
[5,0,0,0]
3
[2,4,3]
6
"""