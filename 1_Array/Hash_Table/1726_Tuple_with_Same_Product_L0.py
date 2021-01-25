class Solution:
    def tupleSameProduct(self, A: List[int]) -> int:
        prod = collections.Counter()
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                prod[A[i]*A[j]] += 1
        ans = 0
        for k, v in prod.items():
            if v>1: ans += v*(v-1)//2*8
        return ans