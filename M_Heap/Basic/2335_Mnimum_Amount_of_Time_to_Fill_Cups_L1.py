""" https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/
Since amount[i]<=100, we can simply use heap to simulate the process.

Time complexity: O(NlogN)
"""
class Solution:
    def fillCups(self, A: List[int]) -> int:
        ans = 0
        A = [-x for x in A if -x]
        heapify(A)
        while len(A)>1:
            a = -heappop(A)
            b = -heappop(A)
            if a-1>0: heappush(A, -(a-1))
            if b-1>0: heappush(A, -(b-1))
            ans += 1
        if A: ans += -A[0]
        return ans


""" smart solution from lee: https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/discuss/2261394/JavaC%2B%2BPython-max(max(A)-(sum(A)-%2B-1)-2)
the answer can be only two cases: 
    1. max(A): [10000, 1, 1]
    2. ceil(sum(A) / 2): [10, 9, 9]
"""
# 

class Solution:
    def fillCups(self, A: List[int]) -> int:
        return max(max(A), (sum(A) + 1) // 2)