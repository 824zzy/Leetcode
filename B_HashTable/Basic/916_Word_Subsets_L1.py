""" https://leetcode.com/problems/word-subsets/
reduce B to single counter and compare counter(a) and counter(b)
"""
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        cnt = Counter()
        for b in B: cnt |= Counter(b)
        
        ans = []
        for a in A:
            if Counter(a)>=cnt:
                ans.append(a)
        return ans