""" https://leetcode.com/problems/distinct-echo-substrings/
brute force check A[i:j]==A[j:2*j-i]
"""
class Solution:
    def distinctEchoSubstrings(self, A: str) -> int:
        ans = set()
        for i in range(len(A)):
            for j in range(i+1, (i+len(A))//2+1):
                if A[i:j]==A[j:2*j-i]: ans.add(A[i:j])
        return len(ans)