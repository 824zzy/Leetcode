""" https://leetcode.com/problems/count-numbers-with-unique-digits/
For any number whose length is n, the count of all unique digit numbers is: 
    A(10, n) - A(9, n-1)
as we need to choose n numbers from 0~9 and remove the leading zero numbers which is selecting from n-1 numbers from 1~9
"""
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def A(n, k):
            ans = 1
            for i in range(n-k+1, n+1):
                ans *= i
            return ans
            
        ans = 1
        for i in range(1, n+1):
            ans += A(10, i)-A(9, i-1)
        return ans