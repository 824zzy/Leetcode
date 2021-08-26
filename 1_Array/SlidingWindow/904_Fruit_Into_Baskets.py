""" L2:
It took me sometime to come up with seen(seen.values()-1), I am not sure I can do it next time.
"""
class Solution:
    def totalFruit(self, A: List[int]) -> int:
        ans, i = 0, 0
        seen = Counter()
        for j in range(len(A)):
            seen[A[j]] += 1
            while len(seen)>2:
                ans = max(ans, sum(seen.values())-1)
                seen[A[i]] -= 1
                if seen[A[i]]==0: del seen[A[i]]
                i += 1
            
        return max(ans, sum(seen.values()))