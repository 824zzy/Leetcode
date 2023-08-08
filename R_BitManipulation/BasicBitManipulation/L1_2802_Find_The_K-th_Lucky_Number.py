""" https://leetcode.com/problems/find-the-k-th-lucky-number/
Observation: answer is actually the binary representation of k+1
"""
class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        return bin(k+1)[3:].replace('0','4').replace('1','7')
    
# simulation solution
class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        n = 1
        while k>2**n:
            k -= 2**n
            n += 1
            
        ans = list('0'*n)
        for i, x in enumerate(reversed(bin(k-1)[2:])):
            if x=='0':
                ans[~i]= '4'
            else:
                ans[~i]= '7'
        return ''.join(x if x in '47' else '4' for x in ans)
        
"""
0, 1, 00, 01, 10, 11, 000, 001, 010, 011
"""