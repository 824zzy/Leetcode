""" https://leetcode.com/problems/maximum-running-time-of-n-computers/
TODO:
https://leetcode.com/problems/maximum-running-time-of-n-computers/discuss/1692965/Python3-greedy
https://leetcode.com/problems/maximum-running-time-of-n-computers/discuss/1692939/JavaC%2B%2BPython-Sort-Solution
"""
class Solution:
    def maxRunTime(self, n: int, A: List[int]) -> int:
        A.sort()
        extra = sum(A[:-n])
        A = A[-n:]
        
        ans = prefix = 0 
        for i, x in enumerate(A): 
            prefix += x 
            if i+1 < len(A) and A[i+1]*(i+1) - prefix > extra: return (prefix + extra) // (i+1)
        return (prefix + extra) // n