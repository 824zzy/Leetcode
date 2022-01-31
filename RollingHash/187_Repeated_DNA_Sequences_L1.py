""" https://leetcode.com/problems/repeated-dna-sequences/
apply rolling hash and return the sequence whose hash has appeared before
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # define hash map from char to int
        mp = dict(zip("ACGT", range(4)))
        ans, seen = set(), set()
        hs = 0 # initiate rolling hash 
        for i, x in enumerate(s): 
            hs = 4*hs + mp[x] # hash function: mpSize*hs+mpVal
            if i >= 10: hs -= mp[s[i-10]]*4**10 # update rolling hash: mpSize*hs+mpVal
            if i >= 9: 
                if hs in seen: ans.add(s[i-9:i+1])
                seen.add(hs)
        return ans