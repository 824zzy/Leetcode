""" https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/
Intuition: we just need to count the occurrences of all substring with minSize
"""
# Time: O(n)
class Solution:
    def maxFreq(self, A: str, maxL: int, minS: int, maxS: int) -> int:
        ans = Counter()
        seen = Counter()
        for i in range(len(A)):
            seen[A[i]] += 1
            if i>=minS:
                seen[A[i-minS]] -= 1
                if not seen[A[i-minS]]: seen.pop(A[i-minS])
            if i>=minS-1 and len(seen)<=maxL:
                s = A[i-minS+1:i+1]
                ans[s] += 1
        return max(ans.values(), default=0)
    

# alternative solution: brute force to fina all substring with minSize
# Time: O(k*n), where k = minSize
class Solution:
    def maxFreq(self, A: str, maxL: int, minS: int, maxS: int) -> int:
        cnt = Counter()
        for i in range(len(A)-minS+1):
            cnt[A[i:i+minS]] += 1
        
        ans = 0
        for k, v in cnt.items():
            if len(set(k))<=maxL: ans = max(ans, v)
        return ans
        