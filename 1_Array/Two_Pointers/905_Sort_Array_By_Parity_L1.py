class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even, odd = 0, len(A) - 1
        while even < odd:
            if A[even] % 2 == 0: even += 1
            else:
                A[even], A[odd] = A[odd], A[even]
                odd -= 1
            return A