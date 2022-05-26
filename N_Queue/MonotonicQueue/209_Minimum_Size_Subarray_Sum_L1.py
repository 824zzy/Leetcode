""" https://leetcode.com/problems/minimum-size-subarray-sum/
since there is no negative value in the array, we can maintain a deque with target as threshold. 
"""
class Solution:
    def minSubArrayLen(self, target: int, A: List[int]) -> int:
        A = list(accumulate(A, initial=0))
        ans = inf
        dq = deque()
        
        for i in range(len(A)):
            while dq and A[i]-A[dq[0]]>=target:
                ans = min(ans, i-dq[0])
                dq.popleft()
            dq.append(i)
        return ans if ans!=inf else 0 