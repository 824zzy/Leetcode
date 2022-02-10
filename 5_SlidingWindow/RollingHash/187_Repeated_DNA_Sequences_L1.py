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
    
    
class RabinKarp: 

    def __init__(self, s): 
        """Calculate rolling hash of s"""
        self.m = 10**9+7
        self.pow = [1]
        self.roll = [0] # rolling hash 
        self.mp = mp = dict(zip("ACGT", range(4)))

        p = 4
        for x in s: 
            self.pow.append(self.pow[-1] * p % self.m)
            self.roll.append((self.roll[-1] * p + self.mp[x]) % self.m)

    def query(self, i, j): 
        """Return rolling hash of s[i:j]"""
        return (self.roll[j] - self.roll[i] * self.pow[j-i]) % self.m
    
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        rks = RabinKarp(s)
        seen = set()
        ans = set()
        for i in range(10, len(rks.roll)):
            hs = rks.query(i-10, i)
            if hs in seen: ans.add(s[i-10:i])
            seen.add(hs)
        return ans