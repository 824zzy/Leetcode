""" https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/
count legit periods( (j-i+1)*(j-i)//2 ) by sliding window i..j, note that the last period need to be calculated at the end
or use i to count legit periods, and reset i to 0 if A[j-1]!=A[j]+1
"""


class Solution:
    def getDescentPeriods(self, A: List[int]) -> int:
        i = 0
        ans = 0
        for j in range(len(A)):
            if j and A[j - 1] - 1 != A[j]:
                ans += (j - i + 1) * (j - i) // 2
                i = j
        return ans + (j - i + 2) * (j - i + 1) // 2


class Solution:
    def getDescentPeriods(self, A: List[int]) -> int:
        ans = 0
        i = 0
        for j in range(len(A)):
            if j and A[j - 1] != A[j] + 1:
                i = 0
            i += 1
            ans += i
        return ans
