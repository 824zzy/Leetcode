""" https://leetcode.com/problems/recover-the-original-array/
similiar to 2007
similar idea with 954, the pairs are not doubled but with constant difference

greedily check every difference that is positive and even,


min(A) = min(_A)-k
max(A) = max(_A)+k
"""
class Solution:
    def recoverArray(self, A: List[int]) -> List[int]:
        A = sorted(A)
        n = len(A)

        def check(A, k, cnt):
            ans = []
            for x in A:
                if cnt[x] == 0: continue
                if cnt[x + k] == 0: return False, []
                cnt[x] -= 1
                cnt[x + k] -= 1
                ans += [x + k // 2]
            return True, ans
        
        cnt = Counter(A)
        for i in range(1, n):
            k = A[i] - A[0]
            if k != 0 and k & 1 == 0:
                a, b = check(A, k, cnt.copy())
                if a: return b