""" https://leetcode.com/problems/match-substring-after-replacement/
Since `1 <= sub.length <= s.length <= 5000`, O(n*m) is acceptable.

TODO: The optimal solution should be O(n+m) by KMP
"""
class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        mp = defaultdict(set)
        for v, k in mappings: mp[k].add(v)
        
        for i in range(len(s)-len(sub)+1):
            for j in range(len(sub)):
                if s[i+j]!=sub[j] and sub[j] not in mp[s[i+j]]: break
            else: return True
        return False