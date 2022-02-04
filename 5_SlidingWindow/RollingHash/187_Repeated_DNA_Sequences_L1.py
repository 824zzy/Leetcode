""" https://leetcode.com/problems/repeated-dna-sequences/
apply rolling hash and return the sequence whose hash has appeared before
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mp = dict(zip("ACGT", range(4)))
        hs = 0
        seen = set()
        ans = set()
        
        for i in range(len(s)):
            # hash function: hs = mpSize * hs + mpVal
            hs = 4*hs+mp[s[i]]
            if i>=9:
                if hs in seen: ans.add(s[i-9:i+1])
                seen.add(hs)
                # update rolling hash: hs -= mpval * mpSize ** (seqSize-1)
                hs -= mp[s[i-9]]*4**9 
        return ans