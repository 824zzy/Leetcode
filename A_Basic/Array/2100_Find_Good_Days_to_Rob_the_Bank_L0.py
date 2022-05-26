""" https://leetcode.com/problems/find-good-days-to-rob-the-bank/
pre-calculate prefix and suffix array of increasing and decreasing elements counts
then find days whose counts larger than time
"""
class Solution:
    def goodDaysToRobBank(self, S: List[int], time: int) -> List[int]:
        A, B = [], []
        cntA, cntB = 0, 0
        rS = S[::-1]
        for i in range(len(S)):
            if i and S[i-1]>=S[i]: cntA += 1    
            else: cntA = 0
            A.append(cntA)
            
            if i and rS[i-1]>=rS[i]: cntB += 1    
            else: cntB = 0
            B.append(cntB)
        
        ans = []
        for i, (a, b) in enumerate(zip(A, B[::-1])):
            if a>=time and b>=time:
                ans.append(i)
        return ans