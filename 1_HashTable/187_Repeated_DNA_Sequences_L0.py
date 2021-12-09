""" https://leetcode.com/problems/repeated-dna-sequences/submissions/
use hash table to find all substrings which frequence>1
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        freq = defaultdict(int)
        for i in range(len(s)-9): freq[s[i:i+10]] += 1
        return [k for k, v in freq.items() if v > 1]