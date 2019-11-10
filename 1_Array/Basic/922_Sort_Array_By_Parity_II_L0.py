class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd, even = [], []
        for i in range(len(A)):
            if A[i]%2==0:
                even.append(A[i])
            else:
                odd.append(A[i])
        ans = []
        for i in range(len(odd)):
            ans.append(even[i])
            ans.append(odd[i])
        return ans