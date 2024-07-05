""" https://leetcode.com/problems/group-shifted-strings/
hash table + counting
"""
from header import *


class Solution:
    def groupStrings(self, A: List[str]) -> List[List[str]]:
        cnt = defaultdict(list)
        for s in A:
            diff = []
            for i in range(1, len(s)):
                x = (ord(s[i]) - ord(s[i - 1])) % 26
                diff.append(str(x))
            cnt[" ".join(diff)].append(s)
        return cnt.values()


"""
["abc","bcd","acef","xyz","az","ba","a","z"]
["a"]
["abc","bcd","acef","xyz","az","ba","a","z","al"]
"""
