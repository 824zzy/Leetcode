""" https://leetcode.com/problems/binary-subarrays-with-sum/
find subarry which has at most S 1's and at most S-1 1's.
tricky line: ans += j-i+1
"""
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        def atMost(S):
            if S<0: return 0
            i = 0
            ans = 0
            for j in range(len(A)):
                S -= A[j]
                while S<0:
                    S += A[i]
                    i += 1
                ans += j - i + 1
            return ans
        return atMost(S) - atMost(S-1)