""" https://leetcode.com/problems/minimum-operations-to-halve-array-sum/
push and pop heap until the sum reaches half
"""            
class Solution:
    def halveArray(self, A: List[int]) -> int:
        SUM = s = sum(A)
        A = [-x for x in A]
        heapify(A)
        ans = 0
        while s>SUM/2:
            x = heappop(A)
            s += x/2
            heappush(A, x/2)
            ans += 1
        return ans