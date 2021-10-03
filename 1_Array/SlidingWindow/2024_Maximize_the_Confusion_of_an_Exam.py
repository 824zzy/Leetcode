""" L1
bound equation: j-i+1 > max(cnt.values())+k 
"""
class Solution:
    def maxConsecutiveAnswers(self, A: str, k: int) -> int:
        cnt = Counter()
        i = 0
        for j in range(len(A)):
            cnt[A[j]] += 1
            if j-i+1 > max(cnt.values())+k:
                cnt[A[i]] -= 1
                i += 1
        return len(A)-i