""" https://leetcode.com/problems/subsets-ii/
To deduplicate, we need to
1. sort the array
2. use set to store subsets
"""
class Solution:
    def subsetsWithDup(self, A: List[int]) -> List[List[int]]:
        ans = set()
        n = len(A)
        A.sort()
        
        for mask in range(1<<n):
            tmp = []
            for i in range(n):
                if mask & 1<<i:
                    tmp.append(A[i])
            ans.add(tuple(tmp))
                
        return ans