""" https://leetcode.com/problems/minimum-average-difference/
basic usage of prefix sum, note that the answer is index rather than value!
"""
class Solution:
    def minimumAverageDifference(self, A: List[int]) -> int:
        prefix = list(accumulate(A))
        mi = inf
        ans = -1
        for i in range(len(A)):
            l = prefix[i]//(i+1)
            if i==len(A)-1: r = 0
            else: r = (prefix[-1]-prefix[i])//(len(A)-i-1)
            
            if abs(l-r)<mi:
                mi = min(mi, abs(l-r))
                ans = i
        return ans
    
"""
[2,5,3,9,5,3]
[0]
[0,1,0,1,0,1]
"""