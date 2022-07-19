""" https://leetcode.com/problems/string-without-aaa-or-bbb/submissions/
"""
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = ''
        while a and b:
            if a>b:
                if len(ans)<2 or (len(ans)>=2 and ans[-2:]!='aa'):
                    ans += 'a'
                    a -= 1
                else:
                    ans += 'b'
                    b -= 1
            else:
                if len(ans)<2 or (len(ans)>=2 and ans[-2:]!='bb'):
                    ans += 'b'
                    b -= 1
                else:
                    ans += 'a'
                    a -= 1
        return ans+'a'*a+'b'*b