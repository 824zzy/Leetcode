""" https://leetcode.com/problems/repeated-dna-sequences/submissions/
use hash table to find all substrings which frequence>1
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = Counter()
        cur = ''
        for i in range(len(s)):
            cur += s[i]
            if i>=9:
                seen[cur] += 1
                cur = cur[1:]
        return [k for k, v in seen.items() if v>1]


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        freq = defaultdict(int)
        for i in range(len(s)-9): freq[s[i:i+10]] += 1
        return [k for k, v in freq.items() if v > 1]