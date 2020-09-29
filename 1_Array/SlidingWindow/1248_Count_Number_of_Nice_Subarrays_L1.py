class Solution:
    def numberOfSubarrays(self, A: List[int], k: int) -> int:
        i = 0
        ans = 0
        count = 0
        s = k
        for j in range(len(A)):
            if A[j]%2==1:
                k -= 1
                count = 0
            while k<=0:
                if A[i]%2==1:
                    k += 1
                i += 1
                count += 1
            ans += count
        return ans