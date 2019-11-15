# Use hash table as a slide window
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        comp = Counter(s[:len(p)])
        target = Counter(p)
        ans = []
        if comp==target:
            ans.append(0)
        
        for i in range(1, len(s)-len(p)+1):
            # pop last word from Counter
            comp[s[i-1]] -= 1
            if comp[s[i-1]]==0:
                comp.pop(s[i-1])
            # add next word to Counter as like sliding window
            if s[i+len(p)-1] not in comp:
                comp[s[i+len(p)-1]] = 1
            else:
                comp[s[i+len(p)-1]] += 1
            # check windows(Counter)
            if comp==target:
                ans.append(i)
        return ans