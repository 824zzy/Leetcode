""" https://leetcode.com/problems/rearrange-characters-to-make-target-string/
"""
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        cnt = Counter(s)
        target = Counter(target)
        
        ans = inf
        for k, v in target.items():
            if k in target:
                ans = min(ans, cnt[k]//v)
        return ans