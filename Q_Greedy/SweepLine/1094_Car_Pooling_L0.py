""" https://leetcode.com/problems/car-pooling/
greedily find max
"""
# template 1
class Solution:
    def carPooling(self, A: List[List[int]], c: int) -> bool:
        A = [x for n, i, j in A for x in [[i, n], [j, -n]]]
        for i, v in sorted(A):
            c -= v
            if c<0: return False
        return True

# template 2    
class Solution:
    def carPooling(self, A: List[List[int]], c: int) -> bool:
        n = max([x for _, _, x in A])
        cnt = [0]*(n+1)
        for x, i, j in A:
            cnt[i] += x
            cnt[j] -= x
        for i in range(1, n+1):
            cnt[i] += cnt[i-1]
        return all([x<=c for x in cnt])