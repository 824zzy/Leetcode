class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        l = 2
        ans = 0
        for i in range(2, len(A)):
            if A[i-1]-A[i-2]==A[i]-A[i-1]: l += 1
            else:
                if l>2: ans += (l-1)*(l-2)//2
                l = 2
        if l>2: ans += (l-1)*(l-2)//2
        return ans
