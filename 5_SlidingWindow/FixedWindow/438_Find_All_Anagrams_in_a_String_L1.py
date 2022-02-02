""" https://leetcode.com/problems/find-all-anagrams-in-a-string/
use a fixed sliding window and a Counter to record p's frequency
when Counter values are all 0, an answer is found
"""
class Solution:
    def findAnagrams(self, A: str, p: str) -> List[int]:
        cnt = Counter(p)
        ans = []
        for i in range(len(A)):
            cnt[A[i]] -= 1
            if i>=len(p): cnt[A[i-len(p)]] += 1
            if all(x==0 for x in cnt.values()): ans.append(i-len(p)+1)
        return ans