""" https://leetcode.com/problems/sliding-subarray-beauty/
"""
from header import *

# sliding window + hash table


class Solution:
    def getSubarrayBeauty(self, A: List[int], k: int, x: int) -> List[int]:
        cnt = [0] * 101
        for i in range(k - 1):
            cnt[A[i]] += 1

        ans = [0] * (len(A) - k + 1)
        for i in range(k - 1, len(A)):
            # update end
            cnt[A[i]] += 1
            # update answer
            xx = 0
            for j in range(-50, 0):
                xx += cnt[j]
                if xx >= x:
                    ans[i - k + 1] = j
                    break
            # update head
            cnt[A[i - k + 1]] -= 1
        return ans


# or use sorted list
class Solution:
    def getSubarrayBeauty(self, A: List[int], k: int, x: int) -> List[int]:
        sl = SortedList(A[:k])
        ans = [min(sl[x - 1], 0)]
        for i in range(k, len(A)):
            sl.add(A[i])
            sl.remove(A[i - k])
            ans.append(min(sl[x - 1], 0))
        return ans
