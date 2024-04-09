""" https://leetcode.com/problems/missing-number/
variance of 136
XOR i+1 with its corresponding element. And based on commutative property, the answer is naturally the missing number.

For example:
[0, 1, 3] ==> (1^0)^(2^1)^(3^3) =(commutative property)=> (1^1)^(3^3)^(0^2) ==> 2
"""


class Solution:
    def missingNumber(self, A: List[int]) -> int:
        ans = 0
        for i in range(len(A)):
            ans ^= (i + 1) ^ A[i]
        return ans
