""" https://leetcode.com/problems/decode-string/
""" 
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = num = ""
        for c in s: 
            if c.isalpha(): ans += c
            elif c.isdigit(): num += c
            elif c == "[": 
                stack.append(num)
                stack.append(ans)
                ans = num = ""
            else: # c == "]"
                ans = stack.pop() + ans*int(stack.pop())
        return ans