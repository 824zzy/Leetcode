""" https://leetcode.com/problems/1-bit-and-2-bit-characters/
https://leetcode.com/problems/1-bit-and-2-bit-characters/discuss/108967/JAVA-check-only-the-end-of-array
find pattern and greedily find continuous ones:
1. if there is only one symbol in array the answer is always true (as last element is 0)
2. if there are two 0s at the end again the answer is true no matter what the rest symbols are( ...1100, ...1000,)
3. if there is 1 right before the last element(...10), the outcome depends on the count of sequential 1, i.e.
    a) if there is odd amount of 1(10, ...01110, etc) the answer is false as there is a single 1 without pair
    b) if it's even (110, ...011110, etc) the answer is true, as 0 at the end doesn't have anything to pair with
"""


class Solution:
    def isOneBitCharacter(self, A: List[int]) -> bool:
        ones = 0
        for i in range(len(A) - 2, -1, -1):
            if A[i] != 0:
                ones += 1
            else:
                break
        return not ones & 1


# or brute force dp
class Solution:
    def isOneBitCharacter(self, A: List[int]) -> bool:
        @cache
        def dfs(i):
            if i == len(A):
                return True
            ans = False
            if A[i] == 0:
                ans |= dfs(i + 1)
            if i + 2 < len(A) and A[i] == 1 and A[i + 1] in [1, 0]:
                ans |= dfs(i + 2)
            return ans

        return dfs(0)
