""" https://leetcode.com/problems/repeated-dna-sequences/submissions/
apply rolling hash and return the sequence whose hash has appeared before
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mp = dict(zip("ACGT", range(4)))
        
        ans, seen = set(), set()
        hs = 0 # rolling hash 
        for i, x in enumerate(s): 
            hs = 4*hs + mp[x]
            if i >= 10: hs -= mp[s[i-10]]*4**10 
            if i >= 9: 
                if hs in seen: ans.add(s[i-9:i+1])
                seen.add(hs)
        return ans