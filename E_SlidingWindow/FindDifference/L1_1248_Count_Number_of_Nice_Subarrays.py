""" https://leetcode.com/problems/count-number-of-nice-subarrays/
The same as 992
"""
class Solution:
    def numberOfSubarrays(self, A: List[int], k: int) -> int:
        def atMost(A, k):
            i, ans = 0, 0
            for j in range(len(A)):
                if A[j]%2: k -= 1
                while k<0:
                    if A[i]%2: k += 1
                    i += 1
                ans += j-i+1
            return ans
        return atMost(A, k)-atMost(A, k-1)