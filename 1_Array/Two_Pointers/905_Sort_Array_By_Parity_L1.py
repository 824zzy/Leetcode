class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even, odd = 0, len(A) - 1
        while even < odd:
            if A[even] % 2 == 0: even += 1
            else:
                A[even], A[odd] = A[odd], A[even]
                odd -= 1
            return A
        
        
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l, r = 0, len(A)-1
        ans = [0]*len(A)
        cur = 0
        while l<=r:
            if A[cur]%2==0:
                ans[l] = A[cur]
                l += 1
            else:
                ans[r] = A[cur]
                r -= 1
            cur += 1
        return ans