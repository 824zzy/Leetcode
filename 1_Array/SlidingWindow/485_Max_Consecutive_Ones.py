# non-while loop sliding window
class Solution:
    def findMaxConsecutiveOnes(self, A: List[int]) -> int:
        ans = 0
        i = 0
        for j in range(len(A)):
            if A[j]==1:  ans = max(ans, j-i+1)
            else: i = j + 1
        return ans

# split string by '0'
class Solution:
    def findMaxConsecutiveOnes(self, A: List[int]) -> int:
        ans = 0
        i = 0
        for j in range(len(A)):
            if A[j]==1:  ans = max(ans, j-i+1)
            else: i = j + 1
        return ans