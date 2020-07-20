from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        target = Counter(p)
        curr = Counter(s[:len(p)])
        if target==curr:
            ans.append(0)
        for i in range(1, len(s)-len(p)+1):
            curr[s[i-1]] -= 1
            if curr[s[i-1]]==0:
                curr.pop(s[i-1])
            curr[s[i+len(p)-1]] += 1
            if target==curr:
                ans.append(i)
        return ans