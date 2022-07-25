""" https://leetcode.com/problems/fruit-into-baskets/submissions/
1. use a Counter to represent the two baskets
2. use a dynamic sliding window to control the fruit types
3. while fruit types >= 2, then move i to remove fruits
"""
class Solution:
    def totalFruit(self, A: List[int]) -> int:
        seen = Counter()
        i = 0
        ans = 0
        for j in range(len(A)):
            seen[A[j]] += 1
            while len(seen)>2:
                seen[A[i]] -= 1
                if not seen[A[i]]: del seen[A[i]]
                i += 1
            ans = max(ans, j-i+1)
        return ans