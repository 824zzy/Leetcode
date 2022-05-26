""" https://leetcode.com/problems/minimum-absolute-difference/
keep track of minimal difference of each pair
"""
class Solution:
    def minimumAbsDifference(self, A: List[int]) -> List[List[int]]:
        A.sort()
        diff = inf
        ans = []
        for i in range(1, len(A)):
            if A[i]-A[i-1]<=diff:
                if A[i]-A[i-1]<diff:
                    ans, diff = [], A[i]-A[i-1]
                ans.append([A[i-1], A[i]])
        return ans
    
class Solution:
    def minimumAbsDifference(self, A: List[int]) -> List[List[int]]:
        A.sort()
        mp = defaultdict(list)
        for i in range(len(A)-1):
            mp[A[i+1]-A[i]].append([A[i], A[i+1]])
        return mp[min(mp)]